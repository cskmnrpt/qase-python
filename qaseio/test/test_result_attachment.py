# coding: utf-8

"""
    Qase.io TestOps API

    Qase TestOps API Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qaseio.models.result_attachment import ResultAttachment

class TestResultAttachment(unittest.TestCase):
    """ResultAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultAttachment:
        """Test ResultAttachment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultAttachment`
        """
        model = ResultAttachment()
        if include_optional:
            return ResultAttachment(
                id = '',
                file_name = '',
                mime_type = '',
                file_path = '',
                content = '',
                size = 56
            )
        else:
            return ResultAttachment(
        )
        """

    def testResultAttachment(self):
        """Test ResultAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()