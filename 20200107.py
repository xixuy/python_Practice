"""
分支和循环

"""
#
score=int(input("请输入成绩："))
if score>=90 and score<=100:
    print("A")
elif score>=80 and score<90:
    print("B")
elif score>=60 and score<80:
    print("C")
elif score>=0 and score<60:
    print("D")
else:
    print("输入错误")


#for 循环
favourite='xixuyan'
for i in favourite:
    print(i)

#continue的用法
for i in range(10):
    print("循环中的i",i)
    if i%2!=0:
        print("符合条件的i",i)
        continue
    i+=2
    print(i)