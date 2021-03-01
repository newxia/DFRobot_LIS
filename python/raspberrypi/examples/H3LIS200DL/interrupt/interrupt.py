# -*- coding:utf-8 -*-
"""
   @file interrupt.py
   @brief 中断检测
   @n 本示例中使能eZHigherThanTh中断事件,当Z方向上面的加速度大于程序所设置的阈值时,
   @n 则会在我们设置的中断引脚int1/int2产生中断电平
   @n 在使用SPI时,片选引脚时可以通过改变宏RASPBERRY_PIN_CS的值修改
   @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
   @licence     The MIT License (MIT)
   @author [fengli](li.feng@dfrobot.com)
   @version  V1.0
   @date  2021-01-16
   @get from https://www.dfrobot.com
   @https://github.com/DFRobot/DFRobot_LIS
"""

import threading

import sys
sys.path.append("../../..") # set system path to top

from DFRobot_LIS import *
import time

INT1 = 26                           #Interrupt pin
int_pad_Flag = False                 #intPad flag
def int_pad_callback(status):
  global int_pad_Flag
  int_pad_Flag = True

#如果你想要用SPI驱动此模块，打开下面两行的注释,并通过SPI连接好模块和树莓派
#RASPBERRY_PIN_CS =  27              #Chip selection pin when SPI is selected
#acce = DFRobot_H3LIS200DL_SPI(RASPBERRY_PIN_CS)


#如果你想要应IIC驱动此模块，打开下面三行的注释，并通过I2C连接好模块和树莓树派,可通过板子上面的拨码切换I2C地址
I2C_BUS         = 0x01            #default use I2C1
#ADDRESS_0       = 0x18            #I2C address 0
ADDRESS_1       = 0x19            #I2C address 1
acce = DFRobot_H3LIS200DL_I2C(I2C_BUS ,ADDRESS_1)

# set int_Pad to input
GPIO.setup(INT1, GPIO.IN)
#set int_Pad interrupt callback
GPIO.add_event_detect(INT1,GPIO.RISING,int_pad_callback)

#Chip initialization
acce.begin()

#Get chip id
print('chip id :%x'%acce.get_id())

'''
set range:Range(g)
             H3LIS200DL_100G   # ±100g
             H3LIS200DL_200G   # ±200g
'''
acce.set_range(acce.H3LIS200DL_100G)

'''
Set data measurement rate
     POWERDOWN_0HZ 
     LOWPOWER_HALFHZ 
     LOWPOWER_1HZ 
     LOWPOWER_2HZ 
     LOWPOWER_5HZ 
     LOWPOWER_10HZ 
     NORMAL_50HZ 
     NORMAL_100HZ 
     NORMAL_400HZ 
     NORMAL_1000HZ 
'''
acce.set_acquire_rate(acce.NORMAL_50HZ)

'''
Set the threshold of interrupt source 1 interrupt
threshold Threshold(g),范围是设置好的的测量量程
'''
acce.set_int1_th(5);

'''
Enable interrupt
Interrupt pin selection
         INT_1 = 0,/<int pad 1 >/
         INT_2,/<int pad 2>/
Interrupt event selection
             X_LOWTHAN_TH     = 1<The acceleration in the x direction is less than the threshold>
             X_HIGHERTHAN_TH  = 2<The acceleration in the x direction is greater than the threshold>
             Y_LOWTHAN_TH     = 4<The acceleration in the y direction is less than the threshold>
             Y_HIGHERTHAN_TH  = 8<The acceleration in the y direction is greater than the threshold>
             Z_LOWTHAN_TH     = 0x10<The acceleration in the z direction is less than the threshold
             Z_HIGHERTHAN_TH  = 0x20<The acceleration in the z direction is greater than the threshold>
             EVENT_ERROR      = 0 <No event>
'''
acce.enable_int_event(acce.INT_1,acce.Z_HIGHERTHAN_TH)
time.sleep(1)

while True:
    
    if(int_pad_Flag == True):
      #Check whether the interrupt event is generated in interrupt 1
      if acce.get_int1_event(acce.Y_HIGHERTHAN_TH) == True:
         print("The acceleration in the y direction is greater than the threshold")
      
      if acce.get_int1_event(acce.Z_HIGHERTHAN_TH) == True:
        print("The acceleration in the z direction is greater than the threshold")
       
      if acce.get_int1_event(acce.X_HIGHERTHAN_TH) == True:
        print("The acceleration in the x direction is greater than the threshold")
      
      int_pad_Flag = False
    #Get the acceleration in the three directions of xyz
    x,y,z = acce.read_acce_xyz()
    time.sleep(0.1)
    print("Acceleration [X = %.2f g,Y = %.2f g,Z = %.2f g]"%(x,y,z))