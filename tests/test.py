import unittest
import requests


class CodefolioTests(unittest.TestCase):
    def test_verify_api_returns(self):
        response = requests.get('https://d2k2lddhvxruc.cloudfront.net/prod/projects', headers={'X-Api-Key': 'SEnaUh9kr42mLh0txIQ6La3a8JS0RMwI7vpr0ECN'})
        self.assertEqual(response.status_code, 200)
        # Ensure the response is a JSON object
        self.assertIsInstance(response.json(), dict)


if __name__ == '__main__':
    unittest.main()
