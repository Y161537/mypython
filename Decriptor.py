import time


class MyDecriptor:
    def __get__(self, instance, owner):  # self:描述符类的对象实例，instance：被指派的属性的类对象实例，owner：被指派的类
        print('getting...', self, instance, owner)

    def __set__(self, instance, value):
        print('setting...', self, instance, value)

    def __delete__(self, instance):
        print('deleting...', self, instance)


class Test:
    x = MyDecriptor()


test = Test()
print(test.x)  # 发生访问，调用__get__()
"""
getting... 
<__main__.MyDecriptor object at 0x000002353F8CDFD0>  # 描述符类本身的实例
<__main__.Test object at 0x000002353F8CDFA0>  # 拥有者的实例，此时为test 可以在之后验证
<class '__main__.Test'>  # 拥有者类的本身，此时为Test
"""
print(test)
print(Test)
test.x = 'X_man'  # 发生赋值，调用__set__()
"""
setting... <__main__.MyDecriptor object at 0x000001A44F1FDFD0> <__main__.Test object at 0x000001A44F1FDFA0> X_man
"""
del test.x  # 发生对象删除，调用__delete__()
"""
deleting... <__main__.MyDecriptor object at 0x00000258CA83DFD0> <__main__.Test object at 0x00000258CA83DFA0>
"""
print(test.x)


# 编写描述符MyDes：当类的属性被访问、修改或设置的时候，分别作出提醒。
class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print('正在访问变量：', self.name)
        return self.val

    def __set__(self, instance, value):
        print('正在修改变量：', self.name)
        self.val = value

    def __delete__(self, instance):
        print('正在删除变量：', self.name)
        print('无法删除变量')


class Warnning:
    x = MyDes(5, 'X-man')


w = Warnning()
print(w.x)
del w.x
