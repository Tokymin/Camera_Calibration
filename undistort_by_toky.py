import cv2 as cv
import numpy as np
import os
import glob


def undistort(frame):
    k = np.array([[7.3942515969024680e+02, 0., 9.5964783192857260e+02, ],
                  [0., 7.3924233324072225e+02, 5.3271837398060302e+02],
                  [0., 0., 1.]])

    d = np.array([-4.3034061365409648e-01, 1.8516783169850456e-01,
                  2.1600233382861045e-03, 7.9227501640548184e-04, 0.])
    h, w = frame.shape[:2]
    mapx, mapy = cv.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv.remap(frame, mapx, mapy, cv.INTER_LINEAR)


if __name__ == '__main__':

    img_dir = "./pic/Colon_images_chess_board"
    img_paths = []
    for extension in ["jpg", "png", "jpeg"]:
        img_paths += glob.glob(os.path.join(img_dir, "*.{}".format(extension)))
    for i,img_path in zip(range(len(img_paths)),img_paths):
        img = cv.imread(img_path)
        undistort_img = undistort(img)
        cv.imshow('img', undistort(img))
        # 恢复畸变并且保存图像
        save_dir = "./pic/Colon_images_dedistortion"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        cv.imwrite(os.path.join(save_dir, str(i)+".jpg"), undistort_img)
        cv.waitKey(2)

    cv.destroyAllWindows()
