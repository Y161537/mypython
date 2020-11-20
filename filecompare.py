def file_compare(file_name1, file_name2):
    with open(file_name1, encoding='utf8') as file1, open(file_name2, encoding='utf8') as file2:
        count = 0
        differ = []
        for each_line1 in file1:
            each_line2 = file2.readline()  # readline()每次读取一行
            count += 1
            if each_line1 != each_line2:
                differ.append(count)
    return differ


file_name1 = input('请输入需要比较的头一个文件名：')
file_name2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file_name1, file_name2)

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第%d行不一样' % each)
