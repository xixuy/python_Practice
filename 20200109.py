"""
函数
"""

def myFirstfunction():
    print("我的第一个函数")


def mySecondfunction(name):
    print(name+"I LOVE YOU")


def add(num1,num2):
    result=num1+num2
    return result

def test(*params):
    """
    收集参数
    :param params:
    :return:
    """
    print("参数的长度：",len(params))
    print("第二个参数是：",params[1])


myFirstfunction()
mySecondfunction("臭臭")
add(3,5)
test(1,"women",4,5,"er")