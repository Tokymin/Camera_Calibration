import cv2
import numpy as np
import xml.etree.ElementTree as ET
import os
import glob

# DPI 0.0016378020443511103
w = 7
h = 6
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.001)


def find_corners(img):
    params = cv2.SimpleBlobDetector_Params()
    params.maxArea = 10e4
    params.minArea = 10
    params.minDistBetweenBlobs = 1
    blobDetector = cv2.SimpleBlobDetector_create(params)
    ret, corners = cv2.findCirclesGrid(img, (w, h), cv2.CALIB_CB_SYMMETRIC_GRID, blobDetector, None)

    if ret:
        cv2.cornerSubPix(img, corners, (w, h), (1, 1), criteria)
        return corners
    return None


def process_img(img):
    mean_dpi = []
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(gray_img, (img.shape[1] * 2, img.shape[0] * 2))
    minThreshValue = 120
    _, binary = cv2.threshold(gray_img, minThreshValue, 255, cv2.THRESH_BINARY)
    corners = find_corners(binary)
    if corners is not None:
        # 计算距离
        dis_real = np.sqrt(np.power((w - 1) * 0.05, 2) + np.power((h - 1) * 0.05, 2))
        lr_points = corners[-1] - corners[0]
        dis_imge = np.sqrt(np.power(lr_points[0][0], 2) + np.power(lr_points[0][1], 2))
        DPI = dis_real / dis_imge
        mean_dpi.append(DPI)
        if len(mean_dpi) >= 3:
            # 如果运行到这儿表示标定成功
            print("success")
            DPI = np.mean(mean_dpi)
            configFile_xml = "wellConfig.xml"
            tree = ET.parse(configFile_xml)
            root = tree.getroot()
            secondRoot = root.find("DPI")
            # print(secondRoot.text)
            secondRoot.text = str(DPI)
            tree.write("wellConfig.xml")
            print("DPI", DPI)
            mean_dpi = []
            # 将角点在图像上显示
        cv2.drawChessboardCorners(img, (w, h), corners, corners is not None)
    return img


if __name__ == "__main__":
    img_dir = "./pic/Colon_images_chess_board"
    img_paths = []
    for extension in ["jpg", "png", "jpeg"]:
        img_paths += glob.glob(os.path.join(img_dir, "*.{}".format(extension)))
    for img_path in img_paths:
        img = cv2.imread(img_path)
        result = process_img(img)
        cv2.imshow('findCorners', result)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
