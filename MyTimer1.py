import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始计时'
        self.borrow = [1, 12, 31, 24, 60, 60]
        self.lasted = []
        self.begin = ()
        self.end = ()

    # 开始计时
    def start(self):
        self.begin = t.localtime()  # localtime()返回元祖，我们只需要前六个元素（秒 分 时 天 月 年）
        self.prompt = '提示：请先调用stop()停止计时'
        print('计时开始')

    # 停止计时
    def stop(self):
        if not self.begin:
            print('提示：请先调用start()停止计时')
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束')

    # 内部方法，计算时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了：'
        for index in range(6):  # 依次遍历六个单位各自的数值
            temp = self.end[index] - self.begin[index]
            if temp < 0:
                i = 1
                while self.lasted[index - i] < 1:
                    self.lasted[index - 1] += self.borrow[index - i] - 1
                    self.lasted[index - i - 1] -= 1
                    i += 1
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index - 1] -= 1
            else:
                self.lasted.append(temp)
        for index in range(6):
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 初始化变量
        self.begin = ()
        self.end = ()
        print(self.prompt)

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = '总共运行了：'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        print(prompt)


t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(65)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)
