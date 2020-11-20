def showmaxfactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d最大素因数是：%d' % (num, count))
            break
        count -= 1
    else:
        print('%d 是一个素数' % num)


num = int(input('请输入一个数字:'))
showmaxfactor(num)
