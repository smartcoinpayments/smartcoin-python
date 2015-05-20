# -*- coding: utf-8 -*-

import re

created_re = re.compile(
    r'^(gte?|lte?)\:([0-9]{4})\-([0-9]{2})\-([0-9]{2})$'
)

from smartcoin.action import Action
from smartcoin.exception import (
    RequiredParameters, ParameterValueNotAllowed, MethodNotAllowed,
    ParameterTypeError
)


class Charge(Action):

    def create(self, data):
        if not data.get('amount', None):
            raise RequiredParameters('Charge amount not informed')
        elif not data.get('currency', None):
            raise RequiredParameters('Charge currency not informed')
        elif not data.get('type', None):
            raise RequiredParameters('Charge amount not informed')
        elif data.get('type') not in ['credit_card', 'bank_slip']:
            raise ParameterValueNotAllowed('type')
        elif data.get('type') == 'credit_card' and not data.get('card', None):
            raise RequiredParameters('Charge card not informed')
        url = self.api.make_url(['charges'])
        return super(Charge, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['charges', id])
        return super(Charge, self).search(url)

    def list(self, data={}):
        if data.get('count', None):
            if type(data.get('count')) not in (int, str):
                raise ParameterTypeError('count', type(data.get('offset')))
            try:
                data['count'] = int(data.get('count'))
            except ValueError:
                data['count'] = 10
            except:
                raise
            finally:
                if data['count'] < 1:
                    data['count'] = 10
        if data.get('offset', None):
            if type(data.get('offset')) not in (int, str):
                raise ParameterTypeError('offset', type(data.get('offset')))
            try:
                data['offset'] = int(data.get('offset'))
            except ValueError:
                data['offset'] = 10
            except:
                raise
            finally:
                if data['offset'] < 0:
                    data['offset'] = 0
        created = data.get('created', None)
        if created and not created_re.match(created):
            raise ParameterValueNotAllowed('created')
        url = self.api.make_url(['charges'])
        return super(Charge, self).list(url)

    def remove(self, *args, **kwargs):
        raise MethodNotAllowed

    def change(self, id, data):
        if not data.get('description', None):
            raise RequiredParameters('Charge description not informed')
        url = self.api.make_url(['charges', id])
        return super(Charge, self).change(url, data)

    def refund(self, id, amount=0):
        data = {}
        if type(amount) not in (int, str):
            raise ParameterTypeError('amount', type(amount))
        try:
            data['amount'] = int(amount)
        except ValueError:
            pass
        except:
            raise
        finally:
            if amount <= 0:
                del data['amount']

        url = self.api.make_url(['charges', id, 'refund'])
        return self.api.post(url, data)

    def capture(self, id, amount=0):
        data = {}
        if type(amount) not in (int, str):
            raise ParameterTypeError('amount', type(amount))
        try:
            data['amount'] = int(amount)
        except ValueError:    
            pass
        except:
            raise
        finally:
            if amount <= 0:
                del data['amount']

        url = self.api.make_url(['charges', id, 'capture'])
        return self.api.post(url, data)
