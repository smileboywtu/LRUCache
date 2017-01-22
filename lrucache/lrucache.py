# -*- coding: utf-8 -*-

"""

    use python order dict to implement lrucache
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :Created: 2017/1/22
    :Copyright: (c) 2016<smileboywtu@gmail.com>

"""


import pprint
import functools
from collections import (
    MutableMapping, OrderedDict
)


class LRUCache(MutableMapping):
    """python implementation for lru cache"""

    def __init__(self, capacity=50, *args, **kwargs):
        """
        init the cache class

        :param capacity: max objects can be cached
        :param args: default iterable obj
        :param kwargs: default obj to be cached
        """
        self.store = OrderedDict()
        self.capacity = capacity
        self.update(dict(*args, **kwargs))

    def __setitem__(self, key, value):
        """
        add item to cache

        :param key: cache key
        :param value: cache value
        :return: None
        """
        if self.__len__() >= self.capacity:
            self.store.popitem(last=False)
        if key in self.store:
            self.store.pop(key)
        self.store[key] = value

    def __getitem__(self, key):
        """
        get cache value from cache

        :param key: cache key
        :return: cached value
        """
        self.store[key] = self.store.pop(key)
        return self.store[key]

    def __delitem__(self, key):
        """
        delete cache key

        :param key: cache be delete with key
        :return: None
        """
        del self.store[key]

    def __iter__(self):
        """
        cache key, value iterable
        :return: iterable
        """
        return iter(self.store)

    def __len__(self):
        """
        cache length
        :return: size of the current cache
        """
        return len(self.store)

    def __repr__(self):
        """show string when use interpreter"""
        return self.__str__()

    def __str__(self):
        """used by print function"""
        objs = [
            "cache key: {0}, value: {1}".format(key, value)
            for key, value in self.store.items()
        ]
        return pprint.pformat(objs)

    def __call__(self, func):
        """
        decorator for function, use to cache function value

        :param func: func to be wrapped and return value will be cached
        :return: wrapped function
        """
        def wrapper(*args, **kwargs):
            kwtuple = tuple((key, kwargs[key]) for key in sorted(kwargs.keys()))
            key = (args, kwtuple)

            if key in self.store:
                return self.store[key]

            value = func(*args, **kwargs)
            self.store[key] = value
            return value

        wrapper.cache = self.store
        wrapper.clear = self.clear
        wrapper.size = self.store.__len__()
        return functools.update_wrapper(wrapper, func)

    def clear(self):
        """
        clear all the cached value

        :return: None
        """
        self.store.clear()