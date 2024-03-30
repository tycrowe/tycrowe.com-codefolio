import os
import json
import boto3


# Constants
QUERY_STRING_PARAMETERS = 'queryStringParameters'
LIMIT = 'limit'
NEXT_TOKEN = 'nextToken'
DEFAULT_LIMIT = 10


def get_query_parameters(event):
    """
    Get query parameters from the event data.
    :param event:   Event data passed to the function
    :return:        Tuple containing limit and next token
    """
    query_params = event.get(QUERY_STRING_PARAMETERS, {})
    limit = int(query_params.get(LIMIT, DEFAULT_LIMIT))
    next_token = query_params.get(NEXT_TOKEN)
    return limit, next_token


def query_dynamodb(limit, next_token):
    """
    Query DynamoDB for projects.
    :param limit:       Maximum number of items to return
    :param next_token:  Token to start from
    :return:            Tuple containing items and next token
    """
    dynamodb = boto3.client('dynamodb')
    table = os.environ['TABLE_NAME']
    paginator = dynamodb.get_paginator('query')

    paginator_input = {
        'TableName': table,
        'KeyConditions': {
            'PK': {
                'AttributeValueList': [{'S': 'PROJECT'}],
                'ComparisonOperator': 'EQ'
            }
        },
        'PaginationConfig': {
            'PageSize': 10
        }
    }

    if next_token:
        paginator_input['PaginationConfig']['StartingToken'] = next_token

    response_iterator = paginator.paginate(**paginator_input)

    items = []
    token = None
    for page in response_iterator:
        for item in page['Items']:
            items.append({
                'Type': item['PK']['S'],
                'Name': item['SK']['S'],
                'Description': item['Description']['S'],
                'Details': {
                    'LatestRelease': item['Details']['M']['LatestRelease']['S'],
                    'Tags': [tag['S'] for tag in item['Details']['M']['Tags']['L']],
                    'TechStack': [tech['S'] for tech in item['Details']['M']['TechStack']['L']],
                    'Version': item['Details']['M']['Version']['S']
                }
            })
            if len(items) == limit:
                token = page['NextToken']
                break
        if token:
            break
    return items, token


def lambda_handler(event, context):
    """
    Lambda function to read from DynamoDB.
    :param event:       Event data passed to the function
    :param context:     Runtime information provided by Lambda
    :return:            Response data for the client
    """
    limit, next_token = get_query_parameters(event)
    items, token = query_dynamodb(limit, next_token)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'items': items,
            'nextToken': token
        })
    }