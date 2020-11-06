import random
times = 3
secret = random.randint(1,10)
guess = 0
print("不妨猜一个数字[0,10]，你将有三次机会：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("猜对了！真棒")
    else:
        if guess > secret:
            print("猜的数字太大了")
        else:
            print("猜的数字太小了")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")
