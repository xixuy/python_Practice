"""
文件操作
"""

import random
import os
import pickle
try:
    f=open('F:\\record.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦！\n错误原因是：'+str(reason))

my_list=[123,345,'xixuyan',['kouxingl']]
pickle_file=open('my_list.pkl','wb')
p=pickle.dump(my_list,pickle_file)
pickle_file.close()



