# -*- coding: utf-8 -*-

import unittest

import smartcoin

from smartcoin.exception import (RequiredParameters, ParameterValueNotAllowed,
    MethodNotAllowed, ParameterTypeError)
from smartcoin.test.helper import (SmartcoinTestCase, CUSTOMER_DATA, TOKEN_DATA,
    CHARGE_DATA)


class ChargeTests(SmartcoinTestCase):

    def setUp(self):
        super(ChargeTests, self).setUp()
        self._charge_api = smartcoin.Charge()

    def test_charge_credit_card_create(self):
        _token_api = smartcoin.Token()
        token = _token_api.create(TOKEN_DATA)
        CHARGE_DATA_CARD = CHARGE_DATA.copy()
        CHARGE_DATA_CARD['type'] = 'credit_card'
        CHARGE_DATA_CARD['card'] = token['id']
        data = self._charge_api.create(CHARGE_DATA_CARD)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)

    def test_charge_create_fail_required_parameters(self):
        CHARGE_DATA_CARD = CHARGE_DATA.copy()
        CHARGE_DATA_CARD['type'] = 'credit_card'
        self.assertRaises(
            RequiredParameters,
            self._charge_api.create,
            CHARGE_DATA_CARD
        )

    def test_charge_create_fail_parameter_value_not_allowed(self):
        CHARGE_DATA_FAIL = CHARGE_DATA.copy()
        CHARGE_DATA_FAIL['type'] = 'test'
        self.assertRaises(
            ParameterValueNotAllowed,
            self._charge_api.create,
            CHARGE_DATA_FAIL
        )

    def test_charge_bank_slip_create(self):
        data = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIn('id', data)
        self.assertIn('link', data['bank_slip'])

    def test_charge_search(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        data = self._charge_api.search(charge['id'])
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_charge_search_fail(self):
        data = self._charge_api.search(1)
        self.assert_response_type(data)
        self.assert_error(data)

    def test_charge_change(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        data = self._charge_api.change(
            charge['id'],
            {'description': 'Test charge'}
        )
        self.assert_response_type(data)
        self.assert_not_error(data)

    def test_charge_change_fail(self):
        data = self._charge_api.create(CHARGE_DATA)
        self.assertRaises(
            RequiredParameters,
            self._charge_api.change,
            data['id'],
            {}
        )

    def test_charge_remove(self):
        self.assertRaises(
            MethodNotAllowed,
            self._charge_api.remove,
        )

    def test_charge_list(self):
        data = self._charge_api.list()
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

    def test_charge_list_count(self):
        data = self._charge_api.list({'count': '10'})
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

    def test_charge_list_count_fail(self):
        self.assertRaises(
            ParameterTypeError,
            self._charge_api.list,
            {'count': ['10']}   
        )

    def test_charge_list_offset(self):
        data = self._charge_api.list({'offset': 10})
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

    def test_charge_list_offset_fail(self):
        self.assertRaises(
            ParameterTypeError,
            self._charge_api.list,
            {'offset': {'10': 1}}   
        )

    def test_charge_list_created(self):
        data = self._charge_api.list({'created': 'gt:2015-05-10'})
        self.assert_response_type(data)
        self.assert_not_error(data)
        self.assertIs(type(data['data']), list)

    def test_charge_list_created_fail(self):
        self.assertRaises(
            ParameterValueNotAllowed,
            self._charge_api.list,
            {'created': 'gt:2015-05'}   
        )

    def test_charge_capture_total(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self._charge_api.capture(charge['id'])

    def test_charge_capture_partial(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self._charge_api.capture(charge['id'], amount=100)

    def test_charge_capture_partial_fail(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self.assertRaises(
            ParameterTypeError,
            self._charge_api.capture,
            charge['id'],
            [123]
        )

    def test_charge_refound_total(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self._charge_api.refound(charge['id'])

    def test_charge_refound_partial(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self._charge_api.refound(charge['id'], amount=100)

    def test_charge_refound_partial_fail(self):
        charge = self._charge_api.create(CHARGE_DATA)
        self.assert_response_type(charge)
        self.assert_not_error(charge)
        self.assertIn('id', charge)
        self.assertRaises(
            ParameterTypeError,
            self._charge_api.refound,
            charge['id'],
            [123] 
        )

if __name__ == '__main__':
    unittest.main()
