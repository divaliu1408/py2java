#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sys

if __name__ == "__main__":
    strname = sys.argv[1]
    path = ''+strname
    #path = r'C:\Users\Launcher\Downloads\lr\spss.csv'
    # # 鎵嬪啓璇诲彇鏁版嵁 - 璇疯嚜琛屽垎鏋愶紝鍦�8.2.Iris浠ｇ爜涓粰鍑虹被浼肩殑渚嬪瓙
    # f = file(path)
    # x = []
    # y = []
    # for i, d in enumerate(f):
    #     if i == 0:
    #         continue
    #     d = d.strip()
    #     if not d:
    #         continue
    #     d = map(float, d.split(','))
    #     x.append(d[1:-1])
    #     y.append(d[-1])
    # print x
    # print y
    # x = np.array(x)
    # y = np.array(y)

    # # Python鑷甫搴�
    # f = file(path, 'rb')
    # print f
    # d = csv.reader(f)
    # for line in d:
    #     print line
    # f.close()

    # # numpy璇诲叆
    # p = np.loadtxt(path, delimiter=',', skiprows=1)
    # print p

    # pandas璇诲叆
    data = pd.read_csv(path)    # TV銆丷adio銆丯ewspaper銆丼ales
    print(data)
    
    x = data[['0', '1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39']]
    # x = data[['TV', 'Radio']]
    y = data[['40']]
    print(x)
    print(y)
    

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1) #灏嗙煩闃甸殢鏈哄垝鍒嗕负璁粌瀛愰泦鍜屾祴璇曞瓙闆�
    print('x_test',x_test)

    # print x_train, y_train
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print(model)
    print("绯绘暟涓�:",linreg.coef_)
    print(linreg.intercept_)

    y_hat = linreg.predict(np.array(x_test))
    #mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    #rmse = np.sqrt(mse)  # Root Mean Squared Error
    #print(mse, rmse)

    t = np.arange(len(x_test)) #鏈潵鏈夊緢澶氫笉鍚岀殑鍙橀噺,姣旇緝闅剧敾鍥�,鐢ㄨ繖涓猼浣滀负妗ユ,鍙互鐢诲嚭鍥惧儚,姣旇緝褰㈣薄鐨勭湅鐪嬫ā鍨嬫晥鏋滄�庝箞鏍�
    print(t)
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
    plt.savefig(path[:-3]+'jpg')
	#this done
	