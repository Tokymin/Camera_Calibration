# Calibration_ZhangZhengyou_Method

#####calibration_for_circle_board_by_toky.py

#####undistort_by_toky.py
两个脚本文件为后续编写，用于圆形标定板，如'.pic/Colon_images_chess_board/'目录下的图片

标定程序使用opencv自带的cpp，可参见：https://github.com/Tokymin/Collect_Colon_Image.git

其他脚本与文件参考自https://github.com/zhiyuanyou/Calibration-ZhangZhengyou-Method
是知乎文章[相机标定之张正友标定法数学原理详解(含python源码)](https://zhuanlan.zhihu.com/p/94244568)的源代码。
1. "run_calib_IR.py"和"run_calib_RGB.py"分别对应"./pic/IR_camera_calib_img"文件夹和"./pic/RGB_camera_calib_img"文件夹；
2. "./pic/IR_camera_calib_img"文件夹下图片含有畸变，执行"run_calib_IR.py"得到到相机的内外参数与畸变参数，并对畸变图片做矫正，矫正图片保存在"./pic/IR_dedistortion"文件夹下；
3. "./pic/RGB_camera_calib_img"文件夹下图片不含畸变，执行"run_calib_RGB.py"得到到相机的内外参数与畸变参数；
4. 棋盘格规格为12乘9，格点长度0.02m，由于opencv输入参数为内角点个数，所以输入参数为11乘8。

  相关配置：   
  win 10 / Ubuntu 16.04    
  python 3.7    
  opencv-contrib-python 3.4.2.16    
  opencv-python 3.4.2.16    
Calibrate the camera with Zhang Zhengyou method (in both distortion case and no distortion case)
