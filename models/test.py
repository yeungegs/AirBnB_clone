#!/usr/bin/python3
import json
from datetime import datetime

 
simple = {"text": "string", "none": None,
          "boolean": True, "number": 3.44,
          "int_list": [1, 2, 3]}

print(json.dumps(simple, indent=2))

class A(object):

    def __init__(self, simple):
        self.simple = simple
    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False
        return self.simple == other.simple
    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True
        return self.simple != other.simple
 
class CustomEncoder(json.JSONEncoder):

     def default(self, o):
         if isinstance(o, datetime):
             return {'__datetime__': o.replace(microsecond=0).isoformat()}
         return {'__{}__'.format(o.__class__.__name__): o.__dict__}

complex = dict(a=A(simple), when=datetime(2016, 3, 7))
serialized = json.dumps(complex, indent=4, cls=CustomEncoder)
 
#print(serialized)
