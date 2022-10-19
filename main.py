import numpy as np
import matplotlib.pyplot as plt
import xlrd

x = [0.75, 1.50, 2.25, 3.00, 3.75]
y = [2.50, 1.20, 1.12, 2.25, 4.28]
k = int(input('Введите k - четное '))
m = int(input('Введите m<=k '))
sum = 0.0

def mnk(x, y, m): #мнк
    c = []
    b = [[0] * (m+1) for i in range(m+1)]
    for k in range(m+1):
        sumy = 0.0
        for i in range(len(y)):
            sumy += (y[i] * (x[i] ** k))
        c.append(sumy)
        for l in range(m+1):
            sumx = 0.0
            for i in range(len(x)):
                sumx += x[i] ** (k + l)
            b[k][l] = sumx
    func = np.linalg.solve(b, c)
    return func

def localsg(x, y, m, k): #Локальное сглаживание
    k1 = k // 2
    ylocal=[]
    ylocal.append(y[0])
    for i in range(1, len(x) - 1):
        ych = []
        xch = []
        if i < k1 or i + k1 > len(x) - 1:
            if k1 > len(x) - 1 - i:
                offset = len(x) - 1 - i
            else:
                offset = i
        else:
            offset = k1
        for j in range(i - offset, i + offset + 1):
            xch.append(x[j])
            ych.append(y[j])
        func = (mnk(xch, ych, m))
        sum = 0.0
        for j in range(len(func)):
            sum += x[i] ** j * func[j]
        print(sum)
        ylocal.append(sum)

    ylocal.append(y[len(y)-1])
    return ylocal

book = xlrd.open_workbook('your.xls')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for r in range(sheet.nrows) for c in range(sheet.ncols)]]
x1 = [sheet.cell_value(r, c) for r in range (1, sheet.nrows) for c in range(0, 1)]
y1 = [sheet.cell_value(r, c) for r in range (1, sheet.nrows) for c in range(2, 3)]

#xsin = np.linspace(0,2*3.14,25)
#ysin = np.sin(xsin)
#plt.scatter(xsin, ysin)
#ylocal = localsg(xsin, ysin, m, k)
#plt.plot(xsin, ylocal)

ylocal=localsg(x1, y1, m, k)
plt.plot(x1, ylocal)
plt.plot(x1, y1, 'bo')

#ylocal=localsg(x, y, m, k)
#plt.plot(x, ylocal)
#plt.plot(x, y, 'bo')

plt.show()
