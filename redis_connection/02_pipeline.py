# coding: utf-8

"""
Gộp nhiều lệnh vào một request thay vì 1 lệnh 1 request như bình thường
"""
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')

pipe = r.pipeline()

pipe.set('a', 1)
pipe.set('b', 2)
pipe.set('c', 2)
pipe.set('d', 2)
pipe.set('e', 2)
pipe.get('foo')

pipe.execute()

print pipe.execute()
