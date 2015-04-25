# -*- coding: utf-8 -*-

import unittest

import smartcoin

from smartcoin.exception import (RequiredParameters, ParameterValueNotAllowed,
    MethodNotAllowed, ParameterTypeError)
from smartcoin.test.helper import SmartcoinTestCase, plan_data


class PlanTests(SmartcoinTestCase):

    def setUp(self):
        super(PlanTests, self).setUp()
        self._plan_api = smartcoin.Plan()

    def test_plan_create(self):
        data = self._plan_api.create(plan_data())
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_plan_create_fail(self):
        PLAN_DATA_FAIL = plan_data().copy()
        del PLAN_DATA_FAIL['amount']
        self.assertRaises(
            RequiredParameters,
            self._plan_api.create,
            PLAN_DATA_FAIL
        )

    def test_plan_search(self):
        plan = self._plan_api.create(plan_data())
        self.assert_response_type(plan)
        self.assert_not_error(plan)
        self.assertIn('id', plan)
        data = self._plan_api.search(plan['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_plan_search_fail(self):
        data = self._plan_api.search(1)
        self.assert_response_type(data)
        self.assert_error(data)

    def test_plan_change(self):
        plan = self._plan_api.create(plan_data())
        self.assert_response_type(plan)
        self.assert_not_error(plan)
        self.assertIn('id', plan)
        data = self._plan_api.change(
            plan['id'],
            {'name': 'Test plan Change'}
        )
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_plan_change_fail(self):
        data = self._plan_api.create(plan_data())
        self.assertRaises(
            RequiredParameters,
            self._plan_api.change,
            data['id'],
            {}
        )

    def test_plan_remove(self):
        plan = self._plan_api.create(plan_data())
        self.assert_response_type(plan)
        self.assert_not_error(plan)
        self.assertIn('id', plan)
        data = self._plan_api.remove(plan['id'])
        self.assert_response_type(plan)
        self.assert_not_error(plan)
        self.assertIn('id', plan)

    def test_plan_list(self):
        data = self._plan_api.list()
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

if __name__ == '__main__':
    unittest.main()
