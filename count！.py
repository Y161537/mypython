def count(*temp):
    length = len(temp)
    for i in range(length):
        word = 0
        space = 0
        num = 0
        others = 0
        for j in temp[i]:
            if j.isalpha():
                word += 1
            elif j.isspace():
                space += 1
            elif j.isdigit():
                num += 1
            else:
                others += 1
        print('第 %d 个字符串共有:英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个'% (i + 1 ,word ,num ,space ,others))

count('I Love you','1234 34 565 667 78','Just smile 12345!!!!!')