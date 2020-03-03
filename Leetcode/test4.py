"""
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

"""

class Strcount(object):
    def strcountout(self,str1,str2):
        s1=str1.lower()
        s2=str2.lower()
        print(s1.count(s2)) #计算s2在s1中出现的次数

s=Strcount()
str1=str(input("请输入字符串："))
str2=str(input("请输入要查询的字母："))
s.strcountout(str1,str2)