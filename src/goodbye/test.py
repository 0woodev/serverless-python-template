import json
from unittest import TestCase

from src.goodbye.handler import lambda_handler


class Test_Goodbye(TestCase):
    def test_with_empty_body(self):
        response = lambda_handler({}, None)
        response_body = json.loads(response['body'])
        self.assertEqual(response_body['message'], 'Goodbye! Anonymous')
