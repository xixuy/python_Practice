"""
对象
"""

class Turtle:
    def setName(self,name):
        self.name=name
    def kick(self):
        print("我叫%s"%self.name)

a=Turtle()
a.setName('ball')
a.kick()
