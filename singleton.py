#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Implementation of the singleton pattern"""


class Shop(object):
    __address = None

    def __new__(self, *args, **kwargs):
        if not self.__address:
            self.__address = super(Shop, self).__new__(self, *args, **kwargs)
        return self.__address


if __name__ == '__main__':
    addr1 = Shop()
    addr2 = Shop()
    if id(addr1) == id(addr2):
        print "Same shop at " + str(id(addr1))
    else:
        print "Different shop"


