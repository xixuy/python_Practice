"""
生成随机数，并去重排序
(不理解）
"""
import random

while True:
    try:
        a,res=int(input()).set()
        for i in range(a):
            res.add(int(input()))
            for i in sorted(res):
                print(i)
    except:
        break