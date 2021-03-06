import random


secret = random.randint(1, 10)
print('请输入一个整数【1,10】：')
guess = 0
while guess != secret:
    temp = input()
    try:
        guess = int(temp)
    except (ValueError, EOFError, KeyboardInterrupt) as reason:
        ''' 
        input()函数有可能产生两类异常：EOFError（文件末尾endoffile，当用户按下组合键Ctrl+d产生）
        和KeyboardInterrupt（取消输入，当用户按下组合键Ctrl+c产生）捕获处理input()的两类异常.
        '''
        print('请输入正确的整数！')
        break
    if guess == secret:
        print('猜对了！真棒')
    elif guess > secret:
        print('猜的数字太大了！请重新输入：')
    else:
        print('猜的数字太小了！请重新输入：')
print('游戏结束，再见~')
