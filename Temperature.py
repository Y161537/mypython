class Celsius:
    def __init__(self, value=26.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32  # temp即是instance，cel是Temperature类的属性

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


temp = Temperature()
"""
1.cel在这里既是Temperature类的属性又是Celsius类的实例,owner=Temperature类
2.对cel属性的操作实际上是Celsius类对cel实例的操作，赋值调用__set
3.解释下Celsius类参数：self=Temperature属性，instance=Temperature实例
4.作用：把对函数的调用表现成对属性的操作
"""
print(temp.cel)
temp.cel = 30
print(temp.cel)
print(temp.fah)
temp.fah = 273
print(temp.cel)
