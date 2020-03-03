"""
进制的转换
"""

num10=int(input("请输入十进制数："))
print("转换为16进制数为：",hex(num10))
print("转换为8进制数为：",oct(num10))
print("转换为2进制数为：",bin(num10))

num2=input("请输入二进制数：")
print("转换为10进制数为：",int(num2,2))

num8=input("请输入八进制数：")
print("转换为10进制数为：",int(num2,8))

num16=input("请输入十六进制数：")
print("转换为10进制数为：",int(num2,16))