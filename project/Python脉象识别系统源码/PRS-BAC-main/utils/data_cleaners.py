import os

import pandas as pd
import numpy as np


class WaveProgress(object):
    def __init__(self):
        self.High = 1.05
        self.Low = 0.95

    def GetMaxMin(self, y, yn, yLow, yHigh):
        result = 1
        ymin = np.min(yn[y:600])
        if (ymin < yLow):
            result = 0
            return result
        ymax = np.max(yn[y:600])
        if (ymax > yHigh):
            result = 0
            return result
        return result

    def minmaxscale(self, data):
        data = (data - np.min(data)) / (np.max(data) - np.min(data))
        return data

    def WaveFiter(self, x, y):
        # 第二列从0开始，取中间600行
        ym = np.mean(y)
        yn = y
        yLow = ym * self.Low
        yHigh = ym * self.High
        tty = 0
        # 移动平均法
        for i in range(0, len(yn)):
            flag = self.GetMaxMin(i, yn, yLow, yHigh)
            if (flag == 1):
                tty = i
                break
        y = yn[tty:tty + 600]
        return x, y, tty

    def Progress(self, filename):
        # 读取数据
        df = pd.read_csv(filename)
        # 设置600个数，间隔0.08
        xl = np.linspace(0, 4792, 600)
        xn = []
        for m in xl:
            xn.append(m / 1000)
        df.columns = ['y', 'x']
        # 从有数据开始
        df = df[df.y != 0]
        yn = df.y.tolist()
        x, y, tty = self.WaveFiter(xn, yn)
        # plt.plot(x,y,label='first')
        y = yn[tty:]
        x, y, tty = self.WaveFiter(xn, y)
        y = self.minmaxscale(y)
        c = {"y": y, "x": x}
        df = pd.DataFrame(c)
        os.remove(filename)
        df.to_csv(filename, header=False, index=False)


if __name__ == '__main__':
    wave = WaveProgress()
    wave.Progress('0text1.csv')
