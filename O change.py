def DectoBin(num):
    temp = []
    result = ''
    while num:
        x = num % 2  # 取余数，当做个位...十位...百位...以此类推
        num = num // 2  #取整数当做下一次的被除数
        temp.append(x)
    while temp:
        result += str(temp.pop())#此步骤已经进行反转
    return result

print(DectoBin(444))
