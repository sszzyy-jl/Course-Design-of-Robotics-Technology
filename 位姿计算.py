import numpy as np

def getT_fromPose(x, y, z, rx, ry, rz):
    # Translation matrix
    T = np.eye(4)
    T[:3, 3] = [x, y, z]

    # Rotation matrices
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(rx), -np.sin(rx)],
                    [0, np.sin(rx), np.cos(rx)]])

    R_y = np.array([[np.cos(ry), 0, np.sin(ry)],
                    [0, 1, 0],
                    [-np.sin(ry), 0, np.cos(ry)]])

    R_z = np.array([[np.cos(rz), -np.sin(rz), 0],
                    [np.sin(rz), np.cos(rz), 0],
                    [0, 0, 1]])

    # Rotation matrix
    R = R_z.dot(R_y).dot(R_x)
    T[:3, :3] = R
    return T

def getPose_fromT(T):
    x, y, z = T[:3, 3]

    ry = np.arcsin(-T[0, 2])
    rz = np.arctan2(T[0, 1], T[0, 0])
    rx = np.arctan2(T[1, 2], T[2, 2])

    return x, y, z, rx, ry, rz

# 输入初始位姿
x1, y1, z1, rx1, ry1, rz1 = -0.78399, -0.24807, 0.48833, 2.80385, -1.333807, -2.64379
# 计算初始位姿对应的变换矩阵T1
T1 = getT_fromPose(x1, y1, z1, rx1, ry1, rz1)

# 右侧20cm的位姿
delta_x = 0.2  # 右侧20cm，即x坐标增加0.2m
x2 = x1 + delta_x
y2, z2, rx2, ry2, rz2 = y1, z1, rx1, ry1, rz1  # 其他坐标和角度保持不变

# 输出结果
print("初始位姿 (x, y, z, rx, ry, rz):", x1, y1, z1, rx1, ry1, rz1)
print("右侧20cm的位姿 (x, y, z, rx, ry, rz):", x2, y2, z2, rx2, ry2, rz2)
