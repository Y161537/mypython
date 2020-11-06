def findstr():
    print('请输入目标字符串:',end = '')
    temp = input()
    print('请输入目标字符串(两个字符):',end = '')
    comp = input()
    count = 0
    i = 0
    for i in range(len(temp)):
        if temp[i] == comp[0]  and temp[i+1] == comp[1]:
            count += 1
            i += 1
        else:
            i += 1
    count = int(count)
    print('目标字符串出现的次数为：%d' % count)


findstr()