import numpy as np

# 摄像头内参
focal_length = 1920 / (2 * np.tan(np.radians(90) / 2))  # 计算焦距
cx, cy = 1920 / 2, 1080 / 2  # 图像中心坐标

# 摄像头外参
camera_position = np.array([0, -1.2, 1.5])  # 摄像头在车体坐标系下的位置
tilt_angle = np.radians(15)  # 倾斜角度

# 目标检测结果
bbox = np.array([1020, 440, 90, 90])  # 包围框坐标 (x, y, w, h)

# 将包围框中心点的像素坐标转换为相机坐标系下的三维坐标
u, v = bbox[0] + bbox[2] / 2, bbox[1] + bbox[3] / 2  # 包围框中心点的像素坐标
depth = 10  # 假设一个深度值，单位为米
point_3d_camera = np.array([(u - cx) * depth / focal_length, (v - cy) * depth / focal_length, depth])

# 将包围框中心点的相机坐标系下的三维坐标转换到车体坐标系下
rotation_matrix = np.array([[1, 0, 0],
                            [0, np.cos(tilt_angle), -np.sin(tilt_angle)],
                            [0, np.sin(tilt_angle), np.cos(tilt_angle)]])
translation_vector = camera_position
point_3d_vehicle = np.dot(rotation_matrix, point_3d_camera) + translation_vector

# 估计车辆与当前车头的位置关系和车辆的高度
vehicle_x, vehicle_y, vehicle_z = point_3d_vehicle
print("车辆在车体坐标系下的位置：", vehicle_x, "米（右侧为正方向）,", vehicle_y, "米（前方为正方向）,", vehicle_z, "米（上方为正方向）")
print("车辆的高度估计为：", vehicle_z)
