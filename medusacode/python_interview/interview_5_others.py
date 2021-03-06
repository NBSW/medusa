#!/usr/bin/env python
# coding:utf-8

print '----------------------------------------------------------------------------------------------------'
# 一行代码计算阶乘
factorial = lambda x: reduce(int.__mul__, range(1, x+1), 1)
for i in range(10):
    print factorial(i)
print '----------------------------------------------------------------------------------------------------'
# 找出列表中出现最频繁的数
l = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
n = max(set(l), key=l.count)
print n
print '----------------------------------------------------------------------------------------------------'
# 检查一个对象的内存使用
import sys
t = (1, 2, 3)
l = [1, 2, 3]
d = {1: 1, 2: 2, 3: 3}
for o in t, l, d:
    print sys.getsizeof(o)  # Return the size of object in bytes.
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
print '----------------------------------------------------------------------------------------------------'
