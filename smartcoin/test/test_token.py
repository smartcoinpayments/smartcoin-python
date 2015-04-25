# -*- coding: utf-8 -*-

import unittest

import smartcoin

from smartcoin.exception import RequiredParameters, MethodNotAllowed
from smartcoin.test.helper import SmartcoinTestCase, TOKEN_DATA


class TokenTests(SmartcoinTestCase):

    def setUp(self):
        super(TokenTests, self).setUp()
        self._token_api = smartcoin.Token()

    def test_token_create(self):
        data = self._token_api.create(TOKEN_DATA)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_token_create_fail(self):
        ERROR_DATA = TOKEN_DATA.copy()
        del ERROR_DATA['name']
        self.assertRaises(
            RequiredParameters,
            self._token_api.create,
            ERROR_DATA
        )

    def test_token_search(self):
        token = self._token_api.create(TOKEN_DATA)
        data = self._token_api.search(token['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_token_list(self):
        self.assertRaises(
            MethodNotAllowed,
            self._token_api.list,
        )

    def test_token_change(self):
        self.assertRaises(
            MethodNotAllowed,
            self._token_api.change,
        )

    def test_token_remove(self):
        self.assertRaises(
            MethodNotAllowed,
            self._token_api.remove,
        )

if __name__ == '__main__':
    unittest.main()
