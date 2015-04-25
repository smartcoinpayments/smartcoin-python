# -*- coding: utf-8 -*-

from smartcoin.action import Action
from smartcoin.exception import RequiredParameters


class Customer(Action):

    def create(self, data):
        if not data.get('email', None):
            raise RequiredParameters('Customer email not informed')
        url = self.api.make_url(['customers'])
        return super(Customer, self).create(url, data)

    def search(self, data):
        if data.get('id', None):
            url = self.api.make_url(['customers', data.get('id')])
            return super(Customer, self).search(url)
        elif data.get('email', None):
            url = self.api.make_url(['customers'])
            return self.api.get(
                url,
                data={'email': data.get('email')}
            )
        else:
            raise RequiredParameters('Customer id or email not informed')

    def list(self):
        url = self.api.make_url(['customers'])
        return super(Customer, self).list(url)

    def remove(self, id):
        url = self.api.make_url(['customers', id])
        return super(Customer, self).remove(url)

    def change(self, id, data):
        if not data.get('card', None):
            raise RequiredParameters('Customer card not informed')
        url = self.api.make_url(['customers', id])
        return super(Customer, self).change(url, data)
