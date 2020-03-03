"""
计算字符串最后一个单词的长度，单词以空格隔开。
"""
class Strlength(object):
    def wordlength(self, str):
        str1 = str.split()  #把字符串转换为列表
        if len(str1) > 1:
            print(len(str1[-1]))
        else:
            print(len(str1[0]))


s = Strlength()
str = input("请输入字符串：")
s.wordlength(str)