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


    path = sys.argv[1]
    nullpath = path[:-4]
    #path = 'E:\\ai\\csv\\'+scv_name+'.csv'
    
    data = pd.read_csv(path)    
	
    #鐩墠涓嬮潰鏄啓姝荤殑,鍒版椂鍊欏簲璇ヤ細鏍规嵁浼犲叆鐨刢sv鐨勭壒鐐瑰啀鍋氫慨鏀�
    
    x = data[['0', '1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39']]
    y = data[['40']]
	
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1) #灏嗙煩闃甸殢鏈哄垝鍒嗕负璁粌瀛愰泦鍜屾祴璇曞瓙闆�
    	
    linreg = LinearRegression()
	
    model = linreg.fit(x_train, y_train)
	
    f = open(nullpath+'123.txt', 'w') 
    f2 = open(nullpath+'123.csv', 'w')
    x = 1
    f.write('{\n')
	
    for n in linreg.coef_[0]:
       if n == linreg.coef_[0][-1]:
          f.write('"coef_'+str(x)+'":'+str(n)+'\n')
          f2.write(str(n))
       else:  
          f.write('"coef_'+str(x)+'":'+str(n)+',\n')
          f2.write(str(n)+',')
       x+=1
       

    f.write('}')
	
    f.close()
    f2.close()

    y_hat = linreg.predict(np.array(x_test))
	
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    R_square = 1 - (mse/np.var(y_test))
    print(R_square)
	
    #mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    #rmse = np.sqrt(mse)  # Root Mean Squared Error
    #print(mse, rmse)

    t = np.arange(len(x_test)) #鏈潵鏈夊緢澶氫笉鍚岀殑鍙橀噺,姣旇緝闅剧敾鍥�,鐢ㄨ繖涓猼浣滀负妗ユ,鍙互鐢诲嚭鍥惧儚,姣旇緝褰㈣薄鐨勭湅鐪嬫ā鍨嬫晥鏋滄�庝箞鏍�
    
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
	
    plt.savefig("D:\\2018BK\\overfit\\NAMA.png") # 鍐欎簬show涔嬪墠,
	
    #plt.show()
	
    
    
	
	#this done
	
	#闂
	#41鍒楁暟鎹�,鍝垪鏄痽
    #濡備綍鏍规嵁鍏紡姹傚叿浣撶殑鐨勭郴鏁板��,鎴戠幇鍦ㄥ彧鑳芥眰鍚勯」鐨勭郴鏁�
	#鏁翠竴涓瘎鍒ゆ爣鍑�,鏂瑰樊涔嬬被鐨�
	
	
	#缁忛獙
	#鏍锋湰鐗瑰埆澶�,涔熷氨鏄缁冩暟鎹壒鍒鐨勬椂鍊�,涓旀病鏈夋潅闊崇殑鏃跺��,鎴戠幇鍦ㄧ敤鐨勮繖绉嶈缁冩柟娉曟槸鏈�濂界殑,Y=a1*x1+a2*x2+a3*x3+... ...+an*xn
	#鏍锋湰姣旇緝灏戠殑鏃跺��,鐢ㄧ幇鏈夊叕寮忕殑灏辨洿鍑嗙‘,鍒版椂鍊欐湁鍙兘灏变笉闇�瑕佸叏閮ㄧ殑鏁版嵁闆嗕簡,浼氭牴鎹叕寮忛噷鏈夌殑鏈煡鏁�, 閫夊彇杩欎簺鏈煡鏁�, 鐒跺悗甯﹀叆鍏紡, 鐒跺悗姹傜郴鏁�. 鍦ㄨ繖绉嶆儏鍐典笅, 灏辨洿鍜岄珮涓椂鐨勬眰绯绘暟闂涓�鏍蜂簡, 甯﹀叆x, 鏈�鍚庡氨鍙樻垚浜嗚В绯绘暟鐨勬柟绋嬩簡
	#鎺ヤ笅鏉ユ瘮杈冭泲鐤�,鎴戝緱鎶婅繖涓柟娉曞仛鎴怶ebService,妯″瀷鎸佷箙鍖�,瀛樺浘,鎴戝揩鎵撳嚭GG浜�
	#鏁版嵁鐨勮瓒婂瓒婄簿纭�,鍥犱负杩欐槸鏁版嵁鐨勯噺, 浣嗘槸鏁版嵁鐨勫垪涓嶆槸瓒婂瓒婄簿纭�, 鍥犱负閲岄潰鏄湁鍙兘鏈夊櫔澹扮殑