import open3d as open3d
import numpy as np


def draw_pc(pc_xyzrgb):
    """
    Plot pointcloud with color
    Parameter:
        pc_xyzrgb: [[x, y, z, r, g, b],...]
    """
    pc = open3d.PointCloud()
    pc.points = open3d.Vector3dVector(pc_xyzrgb[:, 0:3])
    if pc_xyzrgb.shape[1] == 3:
        open3d.draw_geometries([pc])
        return 0
    if np.max(pc_xyzrgb[:, 3:6]) > 20:  ## 0-255
        pc.colors = open3d.Vector3dVector(pc_xyzrgb[:, 3:6] / 255.)
    else:
        pc.colors = open3d.Vector3dVector(pc_xyzrgb[:, 3:6])
    open3d.draw_geometries([pc])
    return 0



def read_pcd(path):
    """
    Read pcd file generated by ./func.py/save_pc
    Parameter:
        path: path of pcd file
    Return:
        xyzrgb: numpy array of colored pointcloud [[x, y, z. r, g, b], ...]
    """
    xyzrgb = []
    with open(path, 'r') as f:
        content = f.readlines()
        for i in content[10:]:
            i_content = i.split(" ")
            x, y, z = float(i_content[0]), float(i_content[1]), float(i_content[2])
            r, g, b = float(i_content[3]), float(i_content[4]), float(i_content[5][:-1])

            xyzrgb.append([x,y,z,r,g,b])

    return np.array(xyzrgb)



if __name__ == "__main__":
    PATH = "./result/pcd/xxxxxx.pcd"

    # Read
    pc = read_pcd(PATH)
    # Draw
    draw_pc(pc)
