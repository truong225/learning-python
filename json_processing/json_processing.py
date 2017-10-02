# coding: utf-8

import json

string = '{"a":1,"b":2,"c":3}'
data = json.loads(string)
print data

mystring = {
    'name': 'Koba',
    'age': 20
}
data = json.dumps(mystring)
print data
