# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.process_a_payout_api import ProcessAPayoutApi


class TestProcessAPayoutApi(unittest.TestCase):
    """ ProcessAPayoutApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.process_a_payout_api.ProcessAPayoutApi()

    def tearDown(self):
        pass

    def test_oct_create_payment(self):
        """
        Test case for oct_create_payment

        Process a Payout
        """
        pass


if __name__ == '__main__':
    unittest.main()
