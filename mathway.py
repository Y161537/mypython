# 重写__sub__魔法方法，使其完成字符串的减法
class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')
# 重写__lshift__和__rshift__魔法方法，使之完成字符串的按位左移或右移

    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]


a = Nstr('i love you! aaaaaaaaaaaaaaaaaaaa')
b = Nstr('a')
print(a - b)
c = Nstr('i love you')
print(c << 5)
print(c >> 4)
