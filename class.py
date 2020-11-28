# 矩形类，设定并获取矩形的属性，得到他的面积
class Func:
    __wid = 0
    __len = 0

    def setrect(self):
        print('请输入矩形参数')
        self.__len = float(input('长:'))
        self.__wid = float(input('宽:'))

    def getrect(self):
        print('该矩形的长为：%.2f，宽为：%.2f' % (self.__len, self.__wid))

    def getarea(self):
        print('该矩形的面积为： %.2f' % (self.__len * self.__wid))


p = Func()
p.setrect()
p.getrect()
print('该矩形的长为：%.2f，宽为：%.2f' % (p._Func__len, p._Func__wid))
# 这是利用_类名__变量名的形式进行访问实际使用不提倡这种粗暴的方式
p.getarea()


# 游乐园门票的类，计算平日价与周末价格，
# 平日票价100元
# 周末票价为平日的120%
# 儿童半票
class Ticket:
    adult = 0
    kid = 0
    flag = 0
    value = 1.0

    def num_people(self):
        self.adult = int(input('请输入成年人的数量：'))
        self.kid = int(input('请输入儿童的数量：'))

    def date_select(self):
        self.flag = int(input('请问去游玩的时间是何时？平日【1】/周末【0】：'))

    def price_cal(self):
        self.value = 1 if self.flag == 1 else 1.2
        print('您需要付的钱为 %d' % (100 * self.value * (self.adult + 0.5 * self.kid)))


play = Ticket()
play.num_people()
play.date_select()
play.price_cal()
