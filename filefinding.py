import os
# 用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索


def file_find(start_dir, file_name):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == file_name:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            file_find(each_file, file_name)
            os.chdir(os.pardir)


start_dir = input('请输入查找的初始目录：')
file_name = input('请输入需要查找的目标文件：')
file_find(start_dir, file_name)
