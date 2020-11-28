import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        print('初始位置:(%d, %d)' % (self.x, self.y))

    def move(self):
        self.x += r.choice([1, -1, -2, 2])
        self.y += r.choice([1, -1, -2, 2])
        print('移动后位置:(%d, %d)' % (self.x, self.y))


class Goldfish(Fish):
    pass


class Turtle(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('大快朵颐时刻！！！！')
            self.hungry = False
        else:
            print('吃不下了')


fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
turtle = Turtle()
turtle.move()
shark = Shark()
shark.move()
shark.eat()
