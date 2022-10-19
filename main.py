import numpy as np
import matplotlib.pyplot as plt
import xlrd

x = [0.75, 1.50, 2.25, 3.00, 3.75]
y = [2.50, 1.20, 1.12, 2.25, 4.28]
k = int(input('Введите k - четное '))
m = int(input('Введите m<=k '))
sum = 0.0
ylocal=[]

def mnk(x, y, m, k): #мнк
    c = []
    b = [[0] * (m+1) for i in range(k+1)]
    for i in range(k+1):
        sumy = 0.0
        for f in range(len(x)):
            sumy += (y[f] * (x[f] ** i))
        c.append(sumy)
        for j in range(m+1):
            sumx = 0.0
            for f in range(len(x)):
                sumx += (x[f]) ** (i + j)
            b[i][j] = sumx
    print(b, c)

    func = np.linalg.solve(b, c)
    return func

def localsg(x, y, m, k): #Локальное сглаживание
    k1 = k // 2
    for i in range(len(x)):
        ych = []
        xch = []
        if i < k1 or i + k1 > len(x) - 1:
            if i > len(x) - 1 - i:
                offset = len(x) - 1 - i
            else:
                offset = i
            if i == 0 or i == len(x)-1:
                ylocal.append(y[i])
            else:
                for j in range(i - offset, i + offset + 1):
                    xch.append(x[j])
                    ych.append(y[j])
                func = (mnk(xch, ych, m, k))
                sum = 0.0
                for i in range(len(x)): здесь ошибка надо посчитать только в одной точке
                    for j in range(len(func)):
                        sum += x[i] ** j * func[j]
                        print (sum)
                ylocal.append(sum)
        else:
            for j in range(i - k1, i + k1 + 1):
                xch.append(x[j])
                ych.append(y[j])
            mnk(xch, ych, m, k)
            func = (mnk(xch, ych, m, k))
            sum = 0.0
            for i in range(len(x)):
                for j in range(len(func)):
                    sum += x[i] ** j * func[j]
            ylocal.append(sum)

#def function(start, end, step): #функция нахождения точек по функции полученной из мнк
#    sum = 0.0
#    i = start
#    while i <= end:
#        for j in range(len(func)):
#            sum+=i**j*func[j]
#        masy.append(sum)
#        masx.append(i)
#        sum = 0.0
#        i+=step

def graf(x, y):
    plt.plot(x, ylocal)
    plt.plot(x, y, 'ro')

book = xlrd.open_workbook('your.xls')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for r in range(sheet.nrows) for c in range(sheet.ncols)]]
x1 = [sheet.cell_value(r, c) for r in range (1, sheet.nrows) for c in range(0, 1)]
y1 = [sheet.cell_value(r, c) for r in range (1, sheet.nrows) for c in range(2, 3)]

localsg(x, y, m, k)
graf(x, y) # массивы из учебника x y
plt.show()
