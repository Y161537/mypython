print('========== 欢迎使用通讯录管理系统 ==========')
print('========== 1.查询联系人信息 ==========')
print('========== 2.添加新的联系人 ==========')
print('========== 3.删除已有联系人 ==========')
print('========== 4.查看所有联系人==========')
print('========== 5.退出管理系统 ==========')

contacts = dict()
while True:
    ordernum = input('请输入操作序号：')
    if ordernum.isdigit():
        ordernum = int(ordernum)
    else:
        print('你输入的命令有误，请重新输入')
    if ordernum == 1:
        name = input('请输入需要查询的联系人姓名:')
        if name in contacts:
            print('姓名:%s' % name)
            print('电话：' + str(contacts[name]))
        else:
            print('没有该联系人，是否添加？（YES/NO）:')
            answer = input()
            if answer == 'YES':
                numb = input('请输入该联系人的联系电话:')
                if numb.isdigit():
                    contacts[name] = int(numb)
                    print('新增用户 %s 成功' % name)
                else:
                    print('电话输入错误，请重新输入：')
            else:
                print('联系人列表未发生改变')

            if numb.isdigit():
                contacts[name] = int(numb)

    if ordernum == 2:
        name = input('请输入需要添加的联系人的姓名：')
        if name in contacts:
            print('该联系人已存在！该用户信息为：')
            print('姓名:%s' % name)
            print('电话:' + str(contacts[name]))
            print('是否修改改用户的信息（YES/NO）：')
            answer = input()
            if answer == 'YES':
                numb = input('请重新输入该用户的电话:')
                if numb.isdigit():
                    contacts[name] = int(numb)
                else:
                    print('电话输入错误，请重新输入：')
            else:
                print('该用户信息未发生修改')
        else:
            numb = input('请输入该新增用户的联系电话：')
            if numb.isdigit():
                contacts[name] = int(numb)
                print('新增用户 %s 成功' % name)
            else:
                print('请输入正确的联系电话')
    if ordernum == 3:
        name = input('请输入需要删除的联系人姓名：')
        if name in contacts:
            del (contacts[name])
            print('联系人: %s 已删除' % name)
        else:
            print('该输入的联系人不存在。')
    if ordernum == 4:
        print('姓名\t手机号码')
        for key, value in contacts.items():
            print(key, value)
    if ordernum == 5:
        break

print('|--- 感谢使用通讯录程序！ ---|')
