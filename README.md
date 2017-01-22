# Python LRU Cache

LRU(last recently used) algorithm is a generic cache algorithm.
it's implemented use the python collections `OrderedDict` as default,
but you can implement other wrapper backend memory like mem-cache and
redis.


# Install

```shell
python setup.py install
```


# Example

after you have installed the package, you can then use as follow example:

``` python

# -*- coding: utf-8 -*-

from lrucache import LRUCache

cache = LRUCache(capacity=50)


@cache
def func(a, b):
    pass

cache["x"] = 1

print cache

cache.clear()

print cache

```


# License

MIT