# smartcoin-python

Smartcoin Python lib

## Instalação

### Instalação utilizando pip

Execute o comando:

    $ pip install smartcoin

### Instalação via repositório

Clone o código:

    $ git clone git@github.com:smartcoinpayments/smartcoin-python.git

Execute o script de setup:

    $ cd smartcoin-python
    $ python setup.py install

## Documentação

Visite [smartcoin.com.br/api/](https://smartcoin.com.br/api/) for api reference.

## Exemplo de uso:

```python

# Setup Account keys

import smartcoin

smartcoin.config(key='pk_test_407d1f51a61756',
                 secret='sk_test_86e4486a0078b2') # Replace keys by your account keys

# Create a Token with card information

TOKEN_DATA = {
    'number': '4242424242424242',
    'exp_month': '12',
    'exp_year': '2018',
    'name': 'Luke Skywalker',
    'cvc': '123'
}

try:
	token = smartcoin.Token().create(TOKEN_DATA)
except Exception, message:
	print message

# Create Charge with token as card param

try:
	smartcoin.Charge().create({
	    'amount': '100',
	    'currency': 'brl',
	    'capture': 'true',
	    'type': 'credit_card',
	    'card': token['id'],
	    'description': 'Smartcoin charge test for example@test.com'
	})
except Exception, message:
	print message


# Create Bank Slip Charge

try:
	smartcoin.Charge().create({
	    'amount': '100',
	    'currency': 'brl',
	    'capture': 'true',
	    'type': 'bank_slip'
	})
except Exception, message:
	print message	

# Create Subscription

try:
	smartcoin.Subscription().create('customer_id', {
    	'plan': 'plan_id'
	})
except Exception, message:
	print message

```

## Autor

Originally by [Felipe Tomaz](https://github.com/Arenhardt).

Colaborador(es):
    [Ricardo Caldeira](https://github.com/ricocaldeira)