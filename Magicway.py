class Rectangle:
    def __init__(self, width=0, length=0):
        self.width = width  # 已经调用__setattr__魔法方法（重写）
        self.length = length

    def __setattr__(self, key, value):
        """
        setattr__()在属性赋值时被调用，并且将值存储到实例字典中，这个字典应该是self的__dict__属性。
        即：在类实例的每个属性进行赋值时，都会首先调用__setattr__()方法，并在__setattr__()方法中将属性名和属性值添加到类实例的
        __dict__属性中。
        """
        if key == 'square':
            self.width = value
            self.length = value
        else:
            # super().__setattr__(key, value)  若写self.key == value, 则会发生无限递归
            self.__dict__[key] = value  # 将实例的属性和属性值作为__dict__的键值对(属性注册操作),故不会触发递归

    def getarea(self):
        return self.width * self.length


r1 = Rectangle(4, 5)
print('长：%d  宽：%d' % (r1.length, r1.width))
print('面积： %d' % r1.getarea())
r1.square = 10
print('长：%d  宽：%d' % (r1.length, r1.width))
print('面积： %d' % r1.getarea())
