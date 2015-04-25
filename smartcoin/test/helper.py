# -*- coding: utf-8 -*-

import string
import random
from datetime import date, timedelta

import unittest

import smartcoin

EXPIRATION_DATE = date.today() + timedelta(days=500)

TOKEN_DATA = {
    'number': '4242424242424242',
    'exp_month': '{}'.format(EXPIRATION_DATE.strftime('%m')),
    'exp_year': '{}'.format(EXPIRATION_DATE.strftime('%Y')),
    'name': 'Teste Name',
    'cvc': '123'
}

CUSTOMER_DATA = {
    'email': 'test@smartcoin.com.br'
}

CHARGE_DATA = {
    'amount': '1000',
    'currency': 'brl',
    'type': 'bank_slip',
    'capture': 'true',
}

def plan_data():
    return  {
        'id': ''.join(random.choice(string.digits) for _ in range(6)),
        'amount': '1000',
        'currency': 'brl',
        'interval': 'month',
        'name': 'Plan 1',
    }


class SmartcoinTestCase(unittest.TestCase):

    def setUp(self):
        super(SmartcoinTestCase, self).setUp()
        smartcoin.config(
            key='pk_test_407d1f51a61756',
            secret='sk_test_86e4486a0078b2'
        )

    def assert_response_type(self, data):
        self.assertIs(type(data), dict)

    def assert_not_error(self, data):
        self.assertNotIn('error', data)

    def assert_error(self, data):
        self.assertIn('error', data)
