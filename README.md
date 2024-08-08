# Project Title: Codefolio Showcase Platform

## Project Summary:
The Codefolio Showcase Platform is a cloud-native application designed to dynamically display software projects in a portfolio on a personal or company website. Utilizing a serverless architecture on AWS, the platform offers a cost-effective, scalable, and easy-to-manage solution for developers and companies to highlight their projects to potential clients or employers. The platform features a DynamoDB table for storing project data, a Lambda function for backend logic, an API Gateway for RESTful endpoint exposure, and a CloudFormation template for resource orchestration.

## Objective:

To develop a scalable, serverless platform that allows for the efficient showcasing of software projects on a website, with the goals of maximizing performance, minimizing costs, and providing an intuitive management interface for project data.
### Key Features:
- Dynamic Project Display: Projects are fetched in real-time from a DynamoDB table, ensuring that the portfolio is always up-to-date with the latest work.
- Serverless Backend: Utilizes AWS Lambda for handling backend logic, allowing for automatic scaling and payment for only the compute time used.
- RESTful API: API Gateway exposes a RESTful API to the frontend, enabling easy integration with any web development framework or technology.
- Cost-Effective: The use of AWS’s managed services reduces the need for manual scaling and maintenance, significantly lowering operational costs.
- Easy Deployment: The entire infrastructure is defined as code using AWS CloudFormation, allowing for easy replication, deployment, and version control of the infrastructure.

Technology Stack:

- AWS DynamoDB: NoSQL database service for storing and retrieving project data.
- AWS Lambda: Event-driven, serverless computing service for executing backend logic.
- AWS API Gateway: Service for creating, publishing, maintaining, monitoring, and securing RESTful APIs.
- AWS CloudFormation: Service for modeling and setting up AWS resources using code.
- Python: Runtime for the Lambda function (or any supported runtime as per project requirements).

## Installation and Setup

1. Clone the repository: `git clone https://github.com/tycrowe/tycrowe.com-codefolio.git`
2. Navigate to the project directory: `cd repository`
3. Install the dependencies: `pip install -r requirements.txt`
4. Set up the environment variables: `export TABLE_NAME=<your_table_name>`
5. Run the project: `python main.py`

### DynamoDB Table Schema
```json
{
    "TableName": "YourTableName",
    "KeySchema": [
        {"AttributeName": "PK", "KeyType": "HASH"},
        {"AttributeName": "SK", "KeyType": "RANGE"}
    ],
    "AttributeDefinitions": [
        {"AttributeName": "PK", "AttributeType": "S"},
        {"AttributeName": "SK", "AttributeType": "S"}
    ],
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
}
```

## Usage

The application exposes a RESTful API with the following endpoint:

- `GET /projects`: Returns a list of projects. Accepts optional query parameters `limit` (number of projects to return) and `nextToken` (pagination token).

## Testing

To run the tests, use the following command: `python -m unittest`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
