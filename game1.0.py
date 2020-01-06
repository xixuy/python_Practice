"""
功能：猜谜游戏
作者：西西
日期：2020/01/06
知识点：1.while循环
       2.if条件语句
       3.随机数
"""
import random
secret=random.randint(1,10)
print("============猜谜小游戏============")
temp=input("请猜一下我心里想的是几：")
guess=int(temp)
while guess!=secret:
    temp=input("猜错了，请重新输入吧！")
    guess=int(temp)
    if guess==secret:
        print("恭喜你猜对啦！")
    else:
        if guess>secret:
            print("大了哦！")
        else:
            print("小了哦")
print("游戏结束")