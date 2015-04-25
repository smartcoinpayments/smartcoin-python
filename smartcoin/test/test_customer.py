# -*- coding: utf-8 -*-

import unittest

import smartcoin

from smartcoin.exception import RequiredParameters
from smartcoin.test.helper import SmartcoinTestCase, CUSTOMER_DATA, TOKEN_DATA


class CustomerTests(SmartcoinTestCase):

    def setUp(self):
        super(CustomerTests, self).setUp()
        self._customer_api = smartcoin.Customer()

    def test_customer_create(self):
        data = self._customer_api.create(CUSTOMER_DATA)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_customer_create_fail(self):
        ERROR_DATA = CUSTOMER_DATA.copy()
        del ERROR_DATA['email']
        self.assertRaises(
            RequiredParameters,
            self._customer_api.create,
            ERROR_DATA
        )

    def test_customer_create_with_card(self):
        _token_api = smartcoin.Token()
        token = _token_api.create(TOKEN_DATA)
        self.assert_response_type(token)
        self.assert_not_error(token)
        CUSTOMER_DATA_WITH_CARD = CUSTOMER_DATA.copy()
        CUSTOMER_DATA_WITH_CARD.update({'card': token['id']})
        data = self._customer_api.create(CUSTOMER_DATA_WITH_CARD)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_customer_search_with_id(self):
        customer = self._customer_api.create(CUSTOMER_DATA)
        data = self._customer_api.search(customer)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_customer_search_with_email(self):
        customer = self._customer_api.create(CUSTOMER_DATA)
        data = self._customer_api.search(CUSTOMER_DATA)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('email', data['data'][0])

    def test_customer_search_fail(self):
        self.assertRaises(
            RequiredParameters,
            self._customer_api.create,
            {}
        )

    def test_customer_change(self):
        _token_api = smartcoin.Token()
        TOKEN_DATA_CHANGE = TOKEN_DATA.copy()
        TOKEN_DATA_CHANGE['number'] = '5454545454545454'
        token = _token_api.create(TOKEN_DATA_CHANGE)
        customer = self._customer_api.create(CUSTOMER_DATA)
        data = self._customer_api.change(customer['id'], {'card': token['id']})
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_customer_change_fail(self):
        customer = self._customer_api.create(CUSTOMER_DATA)
        self.assertRaises(
            RequiredParameters,
            self._customer_api.change,
            customer['id'],
            {}
        )

    def test_customer_remove(self):
        customer = self._customer_api.create(CUSTOMER_DATA)
        data = self._customer_api.remove(customer['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_customer_remove_fail(self):
        data = self._customer_api.remove(1)
        self.assert_response_type(data)
        self.assert_error(data)

    def test_customer_list(self):
        data = self._customer_api.list()
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)
        self.assertIn('email', data['data'][0])

if __name__ == '__main__':
    unittest.main()
