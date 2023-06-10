# -*- coding: utf-8 -*-
"""
这个用于正方形的标定格子
Calibrate the Camera with Zhang Zhengyou Method.
Picture File Folder: "./pic/IR_camera_calib_img/", With Distortion. 

By You Zhiyuan, 2022.07.04, zhiyuanyou@foxmail.com
"""

import os

from calibrate_helper import Calibrator


def main():
    img_dir = "./pic/Colon_images_chess_board"
    shape_inner_corner = (7, 7)
    size_grid = 0.005
    # 创建 calibrator
    calibrator = Calibrator(img_dir, shape_inner_corner, size_grid)
    # 相机标定
    mat_intri, coff_dis = calibrator.calibrate_camera()
    # 恢复畸变并且保存图像
    save_dir = "./pic/Colon_images_dedistortion"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    calibrator.dedistortion(save_dir)


if __name__ == '__main__':
    main()
