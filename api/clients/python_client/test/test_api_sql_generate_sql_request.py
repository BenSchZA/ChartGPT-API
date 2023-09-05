# coding: utf-8

"""
    ChartGPT API

    The ChartGPT API is a REST API that generates charts and SQL queries based on natural language questions.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import chartgpt_client
from chartgpt_client.models.api_sql_generate_sql_request import ApiSqlGenerateSqlRequest  # noqa: E501
from chartgpt_client.rest import ApiException

class TestApiSqlGenerateSqlRequest(unittest.TestCase):
    """ApiSqlGenerateSqlRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiSqlGenerateSqlRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSqlGenerateSqlRequest`
        """
        model = chartgpt_client.models.api_sql_generate_sql_request.ApiSqlGenerateSqlRequest()  # noqa: E501
        if include_optional :
            return ApiSqlGenerateSqlRequest(
                question = 'Which NFTFi protocol provided the lowest APRs in the past month?'
            )
        else :
            return ApiSqlGenerateSqlRequest(
        )
        """

    def testApiSqlGenerateSqlRequest(self):
        """Test ApiSqlGenerateSqlRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
