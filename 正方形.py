import numpy as np

# Step 1: 计算相机内参
theta = np.radians(60)  # 水平视场角（单位：弧度）
image_width = 1920
f = image_width / (2 * np.tan(theta / 2))  # 计算焦距
cx, cy = 960, 540  # 图像中心坐标

# Step 2: 计算相机外参
R = np.array([[np.cos(np.radians(30)), 0, np.sin(np.radians(30))],
              [0, 1, 0],
              [-np.sin(np.radians(30)), 0, np.cos(np.radians(30))]])
t = np.array([[1], [0], [1]])  # 平移向量

# Step 3: 定义正方形在世界坐标系下的坐标
square_points_world = np.array([[1, 1, -1, -1],
                                [0, 1, 1, 0],
                                [1, 1, 1, 1]])

# Step 4: 将三维点投影到二维图像平面
P = np.array([[f, 0, cx],
              [0, f, cy],
              [0, 0, 1]])
square_points_camera = np.dot(R, square_points_world) + t
projected_points = np.dot(P, square_points_camera)

# Step 5: 归一化得到像素坐标
normalized_points = projected_points[:2] / projected_points[2]

# 打印结果
print("Projected Points (Pixel Coordinates):\n", normalized_points.T)
