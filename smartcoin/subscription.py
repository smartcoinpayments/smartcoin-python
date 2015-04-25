# -*- coding: utf-8 -*-

from smartcoin.action import Action
from smartcoin.exception import (
    RequiredParameters, ParameterValueNotAllowed,
    MethodNotAllowed, ParameterTypeError
)


class Subscription(Action):

    def create(self, customer_id, data):
        if not data.get('plan', None):
            raise RequiredParameters('Subscription plan not informed')
        url = self.api.make_url(['customers', customer_id, 'subscriptions'])
        return super(Subscription, self).create(url, data)

    def search(self, customer_id, id):
        url = self.api.make_url(
            ['customers', customer_id, 'subscriptions', id]
        )
        return super(Subscription, self).search(url)

    def change(self, *args, **kwargs):
        raise MethodNotAllowed

    def remove(self, customer_id, id, data={}):
        url = self.api.make_url(
            ['customers', customer_id, 'subscriptions', id]
        )
        return self.api.delete(url, data)

    def list(self, customer_id):
        url = self.api.make_url(['customers', customer_id, 'subscriptions'])
        return super(Subscription, self).list(url)
