import os
import pickle
import time


# 描述符MyDes2：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件
class Record:
    def __init__(self, initval=None, name='x'):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" %
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改，%s = %s\n" %
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value


class FileRec:
    x = Record(23)


file = FileRec()
print(file.x)
file.x = 25
print(file.x)


# 编写描述符MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle的文件中。
# 如果属性被删除了,文件也会同时被删除,属性的名字也会被注销。
class MyDes:
    saved = []

    def __init__(self, name='attr'):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb', encoding='utf8') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)


class Test:
    x = MyDes()


test = Test()
test.x = 10
del test.x
