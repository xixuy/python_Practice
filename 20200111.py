"""
递归，汉诺塔算法
"""

def hannot(n,x,y,z):
    """

    :param n: 盘子的数量
    :param x: 1号针
    :param y: 2号针
    :param z: 3号针
    :return:
    """
    if n==1:
        print(x,'-->',z)
    else:
        hannot(n-1,x,z,y)#将前n-1个盘子从x一到y上
        print(x,'-->',z)#将最底下的最后一个盘子移动到z上
        hannot(n-1,y,x,z)#将y上的n-1个盘子移动到z上

n=int(input("请输入盘子的数量："))
hannot(n,'x','y','z')
