# -*- coding: utf-8 -*-

import os
import re
import json
import base64
import requests
from smartcoin import exception
from smartcoin.version import __version__


class SmartcoinApi(object):

    def __init__(self, **kwargs):
        self.key = kwargs.get("key")
        self.secret = kwargs.get("secret")

    def headers(self):
        return {
            "Authorization": "Basic {}".format(base64.encodestring(
                "{}:{}".format(self.key, self.secret)).replace("\n", "")),
            "User-Agent": "Smartcoin Python Api {}".format(__version__),
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def base_request(self, url, method, data={}):
        try:
            response = requests.request(method, url,
                                        data=json.dumps(data),
                                        headers=self.headers())
            return json.loads(response.content.decode('utf-8'))
        #TODO: Create especifics exceptions
        except Exception as error:
            raise

    def get(self, url, data={}):
        return self.base_request(url, 'GET', data=data)

    def post(self, url, data={}):
        return self.base_request(url, 'POST', data=data)

    def put(self, url, data={}):
        return self.base_request(url, 'PUT', data=data)

    def delete(self, url, data={}):
        return self.base_request(url, 'DELETE', data=data)

    def make_url(self, paths):
        url = 'https://api.smartcoin.com.br/v1/'
        for path in paths:
            url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
        return url

__default_api__ = None


def default_api():

    global __default_api__
    if __default_api__ is None:
        try:
            key = os.environ["SMARTCOIN_API_KEY"]
            secret = os.environ["SMARTCOIN_API_SECRET"]
        except KeyError:
            raise exception.ConfigError(
                "Required SMARTCOIN_API_KEY and SMARTCOIN_API_SECRET")
        __default_api__ = SmartcoinApi(key=key, secret=secret)
    return __default_api__


def config(**kwargs):

    global __default_api__
    __default_api__ = SmartcoinApi(**kwargs)
    return __default_api__
