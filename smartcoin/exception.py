# -*- coding: utf-8 -*-


class ConfigError(Exception):
    pass


class RequiredParameters(Exception):
    pass


class CustomException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MethodNotAllowed(CustomException):

    def __init__(self):
        super(MethodNotAllowed, self).__init__(
            'This method is not allowed'
        )


class ParameterValueNotAllowed(CustomException):

    def __init__(self, parameter):
        super(ParameterValueNotAllowed, self).__init__(
            'The value sent to "{}" is not allowed'.format(parameter)
        )


class ParameterTypeError(CustomException):

    def __init__(self, parameter, type):
        super(ParameterTypeError, self).__init__(
            'The value sent to "{}" can not be {}'.format(parameter, type)
        )

class ObjectTypeNotAllowed(CustomException):

    def __init__(self, attribute, value):
        super(ObjectTypeNotAllowed, self).__init__(
            'The attribute "{}" can not be {} for this object'.format(attribute, value)
        )
