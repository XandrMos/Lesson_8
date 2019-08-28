# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:59:11 2019

@author: Xandr
"""

n = int(input())
spaces = {'global': {'parent': None, 'vars':[]}}
#####
def get_f(ns, var):
    if not(ns in spaces.keys()):
        return None
    else:
        if var in spaces[ns]['vars']:
            return ns
        else:
            return get_f(spaces[ns]['parent'], var)
#####
for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        spaces[namespace] = {'parent': arg, 'vars':[]}
    elif cmd == 'add':
        spaces[namespace]['vars'].append(arg)
    else:
        print(get_f(namespace, arg))