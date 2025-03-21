# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
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

    # Homogeneous transformation matrix
    T[:3, :3] = R

    return T

def getPose_fromT(T):
    # Extract translation
    x, y, z = T[:3, 3]

    # Extract rotation angles (Rx, Ry, Rz)
    # Assuming T is a valid transformation matrix
    ry = np.arcsin(-T[0, 2])
    rz = np.arctan2(T[0, 1], T[0, 0])
    rx = np.arctan2(T[1, 2], T[2, 2])

    return x, y, z, rx, ry, rz

# Test the functions
x, y, z, rx, ry, rz = 1, 2, 3, np.pi/4, np.pi/3, np.pi/6
T = getT_fromPose(x, y, z, rx, ry, rz)
x_out, y_out, z_out, rx_out, ry_out, rz_out = getPose_fromT(T)

print("Input Pose (x, y, z, rx, ry, rz):", x, y, z, rx, ry, rz)
print("Transform Matrix T:")
print(T)
print("Output Pose (x, y, z, rx, ry, rz):", x_out, y_out, z_out, rx_out, ry_out, rz_out)
