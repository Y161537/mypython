def printfile(file_name, file_line):
    (start, end) = file_line.split(':')
    num = 0
    if start == '':
        start = 1
    else:
        start = int(start)
    if end == '':
        end = -1
    else:
        end = int(end)

    file = open(file_name, encoding='utf8')
    if start == 1:
        if end == -1:
            print('%s 全文的内容是：' % file_name)
        else:
            print('%s 第一行到第%d行的内容是：' % (file_name, end))
    else:
        if end == -1:
            print('%s 第%d开始到结尾的内容是：' % (file_name, start))
        else:
            print('%s 第%d行到第%d行的内容是：' % (file_name, start, end))

    for i in range(start - 1):
        file.readline()
        num = end - start + 1
    if num < 0:
        print(file.read())
    else:
        for i in range(num):
            print(file.readline())
    file.close()


def file_replace(file_name, key_word, new_word):
    file = open(file_name, encoding='utf8')
    count = 0
    content = []
    for each in file:
        if key_word in each:
            count += each.count(key_word)
            each = each.replace(key_word, new_word)
        content.append(each)
    decide = input('\n文件 %s 中有%d个字符\"%s\"\n您确定要将所有的\"%s\"替换为\"%s\"吗YES/NO？\n'
                   % (file_name, count, key_word, key_word, new_word))
    if decide in ['YES', 'yes', 'Yes']:
        file_write = open(file_name, 'w', encoding='utf8')
        file_write.writelines(content)
        file_write.close()
    file.close()


file_name = input('请输入文件名：')
file_line = input('请输入行数范围（格式【12:21,23:54】）:')
printfile(file_name, file_line)
order = input('接下来是否对 %s 进行替换字符操作YES/NO？:\n' % file_name)
if order in ['YES', 'Yes', 'yes']:
    key_word = input('请输入希望替换的字符：')
    new_word = input('请输入新的字符：')
    file_replace(file_name, key_word, new_word)
    print('字符替换成功，请打开该文件查看')
