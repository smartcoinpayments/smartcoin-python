# -*- coding: utf-8 -*-

from smartcoin.action import Action
from smartcoin.exception import (
    RequiredParameters, ParameterValueNotAllowed,
    MethodNotAllowed, ParameterTypeError
)


class Plan(Action):

    def create(self, data):
        if not data.get('id', None):
            raise RequiredParameters('Plan amount not informed')
        elif not data.get('amount', None):
            raise RequiredParameters('Plan amount not informed')
        elif not data.get('currency', None):
            raise RequiredParameters('Plan currency not informed')
        elif not data.get('interval', None):
            raise RequiredParameters('Plan currency not informed')
        elif not data.get('name', None):
            raise RequiredParameters('Plan currency not informed')
        url = self.api.make_url(['plans'])
        return super(Plan, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['plans', id])
        return super(Plan, self).search(url)

    def change(self, id, data):
        if not data.get('name', None):
            raise RequiredParameters('Plan name not informed')
        url = self.api.make_url(['plans', id])
        return super(Plan, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(['plans', id])
        return super(Plan, self).remove(url)

    def list(self):
        url = self.api.make_url(['plans'])
        return super(Plan, self).list(url)
