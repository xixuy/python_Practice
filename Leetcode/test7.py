"""
接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""

f=float(input("请输入浮点数："))
print(int(f)+1 if f-int(f)>=0.5 else int(f))