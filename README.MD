# DFRobot_LIS
LIS系列三轴加速度传感器


## DFRobot_LIS Library for Arduino
---------------------------------------------------------

Provide an Arduino library to get Three-axis acceleration by reading data from LIS.

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

Provide an Arduino library to get Three-axis acceleration by reading data from LIS.

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
  DFRobot_LIS();
  /**
   * @brief Initialize the function
   * @return Return 0 indicates a successful initialization, while other values indicates failure and return to error code.
   */
  int begin(void);
 
  /**
   * @brief Get chip id
   * @return Returns the 8 bit serial number
   */
  uint8_t getID();
  
  /**
   * @brief Enable interrupt
   * @param source Interrupt pin selection
              eINT1 = 0,/<int1 >/
              eINT2,/<int2>/
   * @param event Interrupt event selection
                   eXLowThanTh = 0,/<The acceleration in the x direction is less than the threshold>/
                   eXhigherThanTh ,/<The acceleration in the x direction is greater than the threshold>/
                   eYLowThanTh,/<The acceleration in the y direction is less than the threshold>/
                   eYhigherThanTh,/<The acceleration in the y direction is greater than the threshold>/
                   eZLowThanTh,/<The acceleration in the z direction is less than the threshold>/
                   eZhigherThanTh,/<The acceleration in the z direction is greater than the threshold>/
   */
  void enableInterruptEvent(eInterruptSource_t source, eInterruptEvent_t event);
  
  /**
   * @brief Set the measurement range
   * @param range Range(g)
                  eH3lis200dl_100g, //±100g
                  eH3lis200dl_200g, //±200g
                  
                  eLis331h_6g = 6,//±6g
                  eLis331h_12g = 12 //±12g
                  eLis331h_24g = 24 //±24g
   */
  bool setRange(eRange_t range);
  
  /**
   * @brief Set data measurement rate
   * @param rate:rate(HZ)
                  ePowerDown_0HZ   //测量关闭
                  eLowPower_halfHZ //0.5 hz
                  eLowPower_1HZ
                  eLowPower_2HZ
                  eLowPower_5HZ
                  eLowPower_10HZ
                  eNormal_50HZ
                  eNormal_100HZ
                  eNormal_400HZ
                  eNormal_1000HZ
   */
  void setAcquireRate(ePowerMode_t rate);
  
  /**
   * @brief Set data filtering mode
   * @param mode Four modes
                 eCutoffMode1 = 0,
                 eCutoffMode2,
                 eCutoffMode3,
                 eCutoffMode4,
                 eShutDown,  无过滤
   *|---------------------------High-pass filter cut-off frequency configuration-----------------------------|
   *|--------------------------------------------------------------------------------------------------------|
   *|                |    ft [Hz]      |        ft [Hz]       |       ft [Hz]        |        ft [Hz]        |
   *|   mode         |Data rate = 50 Hz|   Data rate = 100 Hz |  Data rate = 400 Hz  |   Data rate = 1000 Hz |
   *|--------------------------------------------------------------------------------------------------------|
   *|  eCutoffMode1  |     1           |         2            |            8         |             20        |
   *|--------------------------------------------------------------------------------------------------------|
   *|  eCutoffMode2  |    0.5          |         1            |            4         |             10        |
   *|--------------------------------------------------------------------------------------------------------|
   *|  eCutoffMode3  |    0.25         |         0.5          |            2         |             5         |
   *|--------------------------------------------------------------------------------------------------------|
   *|  eCutoffMode4  |    0.125        |         0.25         |            1         |             2.5       |
   *|--------------------------------------------------------------------------------------------------------|
   */
  void setHFilterMode(eHighPassFilter_t mode);

  /**
   * @brief Set the threshold of interrupt source 1 interrupt
   * @param threshold 设置的阈值在量程之内(unit:g)
   */
  void setInt1Th(uint8_t threshold);

  /**
   * @brief Set interrupt source 2 interrupt generation threshold
   * @param threshold 设置的阈值在量程之内(unit:g）
   */
  void setInt2Th(uint8_t threshold);

  /**
   * @brief Enable sleep wake function
   * @param enable true(enable)\false(disable)
   * @return 1 表示使能失败/0 表示使能成功
   */
  int enableSleep(bool enable);
  


  /**
   * @brief Check whether the interrupt event'event' is generated in interrupt 1
   * @param event Interrupt event
                   eXLowThanTh = 0,/<The acceleration in the x direction is less than the threshold>/
                   eXhigherThanTh ,/<The acceleration in the x direction is greater than the threshold>/
                   eYLowThanTh,/<The acceleration in the y direction is less than the threshold>/
                   eYhigherThanTh,/<The acceleration in the y direction is greater than the threshold>/
                   eZLowThanTh,/<The acceleration in the z direction is less than the threshold>/
                   eZhigherThanTh,/<The acceleration in the z direction is greater than the threshold>/
   * @return true 产生了此事件
             false 未产生此事件
   */
  bool getInt1Event(eInterruptEvent_t event);

  /**
   * @brief Check whether the interrupt event'event' is generated in interrupt 2
   * @param event Interrupt event
                   eXLowThanTh = 0,/<The acceleration in the x direction is less than the threshold>/
                   eXhigherThanTh ,/<The acceleration in the x direction is greater than the threshold>/
                   eYLowThanTh,/<The acceleration in the y direction is less than the threshold>/
                   eYhigherThanTh,/<The acceleration in the y direction is greater than the threshold>/
                   eZLowThanTh,/<The acceleration in the z direction is less than the threshold>/
                   eZhigherThanTh,/<The acceleration in the z direction is greater than the threshold>/
   * @return true 产生了此事件
             false 未产生此事件
   */
  bool getInt2Event(eInterruptEvent_t event);
  
  /**
   * @brief Get the acceleration in the x direction
   * @return acceleration (unit:g)
   */
  long readAccX();
  
  /**
   * @brief Get the acceleration in the y direction
   * @return acceleration (unit:g)
   */
  long readAccY();
  
  /**
   * @brief Get the acceleration in the z direction
   * @return acceleration (unit:g)
   */
  long readAccZ();
  
  /**
   * @brief Get the acceleration in the three directions of xyz
   * @param accx 储存x方向加速度的变量
   * @param accy 储存y方向加速度的变量
   * @param accz 储存z方向加速度的变量
   */
  bool getAcceFromXYZ(long &accx,long &accy,long &accz);

  /**
   * @brief 获取传感器是否处于睡眠模式
   * @return true(处于睡眠模式)/false(处于正常模式)
   */
  bool getSleepState();
  
  /**
   * @brief 设置睡眠状态的标志
   * @param true(将现在的模式标记为睡眠模式)
            false(将现在的模式标记为正常模式)
   */
  void setSleepFlag(bool into);
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino uno        |      √       |              |             | 
FireBeetle-ESP8266        |      √       |              |             | 
FireBeetle-ESP32        |      √       |              |             | 
Arduino MEGA2560        |      √       |              |             | 
Arduino Leonardo|      √       |              |             | 
microbit        |      √       |              |             | 
FireBeetle-M0        |      √       |              |             | 
raspberry pi 3      |      √       |              |             | 

## History

- data 2021-2-1
- version V1.0


## Credits

Written by(li.feng@dfrobot.com), 2020. (Welcome to our [website](https://www.dfrobot.com/))
