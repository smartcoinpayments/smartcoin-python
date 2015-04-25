# -*- coding: utf-8 -*-

from smartcoin.action import Action
from smartcoin.exception import RequiredParameters, MethodNotAllowed


class Token(Action):

    def create(self, data):
        if not data.get('number', None):
            raise RequiredParameters('Token number not informed')
        elif not data.get('exp_month', None):
            raise RequiredParameters('Token exp_month not informed')
        elif not data.get('exp_year', None):
            raise RequiredParameters('Token exp_year not informed')
        elif not data.get('name', None):
            raise RequiredParameters('Token name not informed')
        elif not data.get('cvc', None):
            raise RequiredParameters('Token cvc not informed')
        url = self.api.make_url(['tokens'])
        return super(Token, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['tokens', id])
        return super(Token, self).search(url)

    def list(self, *args, **kwargs):
        raise MethodNotAllowed

    def change(self, *args, **kwargs):
        raise MethodNotAllowed

    def remove(self, *args, **kwargs):
        raise MethodNotAllowed
