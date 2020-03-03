"""
类：定制一个计时器的类
"""
import time as t
class MyTimer:
    def __init__(self):
        """
        初始化
        """
        self.prompt="未开始计时"
        self.lasted=[]
        self.start=0
        self.stop=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def start(self):
        """
        开始计时
        :return:
        """
        self.start=t.localtime()
        print("开始计时！")

    def stop(self):
        """
        结束计时
        :return:
        """
        self.stop=t.localtime()
        self._calc()
        print("结束计时！")

    def _calc(self):
        """
        内部方法，计算运算时间
        :return:
        """
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt+=str(self.lasted[index])


t1=MyTimer()

