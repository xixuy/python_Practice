"""
生成器和迭代器
"""
# class CountList:
#     def __init__(self,*args):
#         self.values=[x for x in args]
#         self.count={}.fromkeys(range(len(self.values)),0)
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, key):
#         self.count[key]+=1
#         return self.values[key]

#列表生成式
lis=[x*x for x in range(10)]
print(lis)

#生成器生成式
generator_ex=(x*x for x in range(10))
for i in generator_ex:
    print(i)
