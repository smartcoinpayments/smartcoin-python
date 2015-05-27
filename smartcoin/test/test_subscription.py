# -*- coding: utf-8 -*-

import unittest

import smartcoin

from smartcoin.exception import (RequiredParameters, ParameterValueNotAllowed,
    MethodNotAllowed, ParameterTypeError)
from smartcoin.test.helper import (SmartcoinTestCase, plan_data, TOKEN_DATA,
    CUSTOMER_DATA)


class SubscriptionTests(SmartcoinTestCase):

    def setUp(self):
        super(SubscriptionTests, self).setUp()
        self._subscription_api = smartcoin.Subscription()
        _plan_api = smartcoin.Plan()
        self.plan = _plan_api.create(plan_data())
        _token_api = smartcoin.Token()
        token = _token_api.create(TOKEN_DATA)
        _customer_api = smartcoin.Customer()
        CUSTOMER_DATA_WITH_CARD = CUSTOMER_DATA.copy()
        CUSTOMER_DATA_WITH_CARD.update({'card': token['id']})
        self.customer =  _customer_api.create(CUSTOMER_DATA_WITH_CARD)

    def test_subscription_create(self):
        data = self._subscription_api.create(self.customer['id'],
                                             {'plan': self.plan['id']})
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_subscription_create_fail(self):
        self.assertRaises(
            RequiredParameters,
            self._subscription_api.create,
            self.customer['id'],
            {}
        )

    def test_subscription_search(self):
        subscription = self._subscription_api.create(self.customer['id'],
                                                     {'plan': self.plan['id']})
        self.assert_response_type(subscription)
        self.assert_not_error(subscription)
        self.assertIn('id', subscription)
        data = self._subscription_api.search(self.customer['id'],
                                             subscription['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_subscription_search_fail(self):
        data = self._subscription_api.search(self.customer['id'], 1)
        self.assert_response_type(data)
        self.assert_error(data)

    def test_subscription_change(self):
        self.assertRaises(
            MethodNotAllowed,
            self._subscription_api.change,
        )

    def test_subscription_remove(self):
        subscription = self._subscription_api.create(self.customer['id'],
                                                     {'plan': self.plan['id']})
        self.assert_response_type(subscription)
        self.assert_not_error(subscription)
        self.assertIn('id', subscription)
        data = self._subscription_api.remove(self.customer['id'],
                                             subscription['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_subscription_at_period_end_remove(self):
        subscription = self._subscription_api.create(self.customer['id'],
                                                     {'plan': self.plan['id']})
        self.assert_response_type(subscription)
        self.assert_not_error(subscription)
        self.assertIn('id', subscription)
        data = self._subscription_api.remove(self.customer['id'],
                                             subscription['id'],
                                             {'at_period_end': 'true'})
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_subscription_list(self):
        data = self._subscription_api.list(self.customer['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

    def test_subscription_list_without_customer(self):
        data = self._subscription_api.list_all()
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

if __name__ == '__main__':
    unittest.main()
