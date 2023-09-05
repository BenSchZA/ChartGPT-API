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
from chartgpt_client.models.response import Response  # noqa: E501
from chartgpt_client.rest import ApiException

class TestResponse(unittest.TestCase):
    """Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Response`
        """
        model = chartgpt_client.models.response.Response()  # noqa: E501
        if include_optional :
            return Response(
                id = '', 
                created_at = 56, 
                finished_at = 56, 
                status = '', 
                prompt = '', 
                dataset_id = '', 
                attempts = [
                    chartgpt_client.models.attempt.Attempt(
                        index = 56, 
                        created_at = 56, 
                        outputs = [
                            chartgpt_client.models.output.Output(
                                index = 56, 
                                created_at = 56, 
                                description = '', 
                                type = '', 
                                value = '', )
                            ], 
                        errors = [
                            chartgpt_client.models.error.Error(
                                index = 56, 
                                created_at = 56, 
                                type = '', 
                                value = '', )
                            ], )
                    ], 
                output_type = '', 
                outputs = [
                    chartgpt_client.models.output.Output(
                        index = 56, 
                        created_at = 56, 
                        description = '', 
                        type = '', 
                        value = '', )
                    ], 
                errors = [
                    chartgpt_client.models.error.Error(
                        index = 56, 
                        created_at = 56, 
                        type = '', 
                        value = '', )
                    ], 
                usage = chartgpt_client.models.response_usage.Response_usage(
                    tokens = 56, )
            )
        else :
            return Response(
        )
        """

    def testResponse(self):
        """Test Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
