import random


secret = random.randint(1, 10)
print('请输入一个整数【1,10】：')

while guess != secret:
    temp = input()
    try:
        guess = int(temp)
    except ValueError as reason:
        print('请输入正确的整数！')
    if guess == secret:
        print('猜对了！真棒')
    elif guess > secret:
        print('猜的数字太大了！请重新输入：')
    else:
        print('猜的数字太小了！请重新输入：')
print('游戏结束，再见~')
