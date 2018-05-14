import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

delta = 0.0341

# 直线方程函数
def linear(x, k, b):
    return k * x + b


def getline(x0, y0, label, linestyle):
    x0, y0 = y0, x0

    plt.scatter(x0[:], y0[:], 20, "black")                # 20 表示散点的大小。
    k, b = optimize.curve_fit(linear, x0[3:], y0[3:])[0]  # 去除三个数据，拟合得出直线的k和b
    x = np.arange(min(x0), max(x0), 0.1)              
    y = k * x + b
    return plt.plot(x, y, 'black', label='s=%.5ft%c%.4f' % (k, '+' if b >= 0 else '-', abs(b)), linestyle=linestyle)


def plot(x0, y1, y2, y3, tag):
    plt.figure()
    l1, = getline(x0, y1, 'line1', ':')
    l2, = getline(x0, y2, 'line2', '-.')
    l3, = getline(x0, y3, 'line3', '--')
    plt.title("Displacement-Time Graph of Ball %s" % tag)
    plt.xlabel('Time (t/s)')
    plt.ylabel('Displacement (s/m)')
    plt.legend(handles=[l1, l2, l3, ], loc='best')

    plt.show()

    return

x0 = [delta * (x - 1) for x in [1, 2, 3, 4, 5, 6, 7, 8]]
A1 = [x - 18 for x in [18.86, 20.70, 22.67, 24.70, 26.64, 28.64, 30.64, 32.79]]
A2 = [3.93,  5.91,  7.90,  9.93, 11.80, 13.84, 15.71, 17.90]
A3 = [3.38,  5.35,  7.30,  9.27, 11.24, 13.26, 15.34, 17.46]
B1 = [6.41, 9.85, 13.16, 16.50, 19.91, 23.32, 26.79, 30.26]
B2 = [5.96, 9.29, 12.68, 15.93, 19.41, 22.71, 26.71, 29.20]
B3 = [5.13, 8.43, 11.81, 15.26, 18.63, 21.95, 25.41, 28.84]
C1 = [19.62, 27.95, 36.24, 44.82, 53.23, 61.66, 69.30, 76.74]
C2 = [ 9.50, 16.95, 24.75, 32.73, 40.48, 48.60, 56.77, 64.90]
C3 = [12.63, 20.53, 28.48, 36.42, 44.41, 52.36, 60.45, 68.50]

plot(x0, A1, A2, A3, 'A')
plot(x0, B1, B2, B3, 'B')
plot(x0, C1, C2, C3, 'C')