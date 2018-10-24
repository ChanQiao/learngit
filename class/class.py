#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Student(object):

    def __init__(self, name, source, sex):
        self.__name = name
        self.__source = source
        self.__sex = sex

    def show_info(self):
        print("name : %s  source : %0.1f" % (self.__name, self.__source))

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    bob = Student("Bob", 89.6)
    bob.show_info()
