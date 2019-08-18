# -*- coding: utf-8 -*-
#本题不是在leetcode上的题目，而是在runoob上的小游戏
#九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0} x {1} = {2}\t".format(j, i, i*j), end='')      #通过指定end参数的值，可以取消在末尾输出回车符，实现不换行
    print()