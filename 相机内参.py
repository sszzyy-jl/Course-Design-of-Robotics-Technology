import cv2
import numpy as np

# 相机内参
f = 1000.0  # 焦距
cx = 960.0  # 图像中心x坐标
cy = 540.0  # 图像中心y坐标

# 相机外参
R = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])  # 旋转矩阵
t = np.array([[0], [0], [0]])  # 平移向量

# 相机成像的三维点坐标
point_3d = np.array([[1], [-1], [1]])

# 将三维点投影到二维图像平面
P = np.array([[f, 0, cx],
              [0, f, cy],
              [0, 0, 1]])  # 投影矩阵
point_2d = np.dot(P, np.dot(R, point_3d) + t)

# 归一化
point_2d /= point_2d[2]

# 输出结果
print("相机成像的像素坐标：", point_2d[:2].T)

