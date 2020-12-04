class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)


c = C()
print(c)
print(C)
c.x = 'X_man'
"""
c.x = 'X-man ‘ 先就近触发了MyProperty中的__init__,把C的getX,setX,delX赋值
给fget,fset,fdel,然后=触发了MyProperty中的__set__,instance是指c

c.x =  x-man：就是输入c（instance）‘x（self）‘x-man（value）三个给MyProperty，返回C两个c（self）'x-man（value）,并传给c’’

1.调用描述类Myproperty，传入三个参数，分别是三个方法 
2.将参数每个方法赋给变量 
3.当执行相应的访问，赋值，删除将调用此传入的方 法(instance相当于self)给self._x赋值

x既是c的成员变量(继承自C)，又是MyProperty的实例化对象
"""
del c.x
