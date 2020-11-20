import os


def file_size():
    file_name = os.listdir(os.curdir)
    dict1 = dict()
    for each_file in file_name:
        if os.path.isfile(each_file):
            dict1.setdefault(each_file, os.path.getsize(each_file))
            print('%s的大小为;【%s Bytes】' % (each_file, dict1[each_file]))


file_size()