"""
lambda 表达式:不需要考虑命名的问题，简化可读性
递归:调用函数自身的行为，有终止条件
"""
# def factorial(n):
#     result=n
#     for i in range(1,n):
#         result*=i
#     return result
# number=int(input("请输入一个正整数："))
# result=factorial(number)
# print("%d的阶乘是%d"%(number,result))


def factorial_2(n):
    """
    递归写法
    :param n:
    :return:
    """
    if n==1:
        return 1
    else:
        return n*factorial_2(n-1)

number=int(input("请输入一个正整数："))
result=factorial_2(number)
print("%d的阶乘是%d"%(number,result))