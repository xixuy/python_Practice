"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
知识点：字符串的切片与连接
       字符串与整型的转换
       [::-1] 表示的是从尾到头，步长为1
"""

num=str(input())
result=''
for i in num[::-1]:
    if i not in result:
        result=result+i
print(int(result))
