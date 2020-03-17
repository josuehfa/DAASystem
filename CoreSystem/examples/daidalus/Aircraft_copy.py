"""
Class for plotting a aircraft

Author: Josue H. F. Andrade

Based on: Daniel Ingram (daniel-s-ingram)
"""

from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib, time

class Aircraft():
    def __init__(self, x=0, y=0, z=0, roll=0, pitch=0, yaw=0, size=1.0, show_animation=True):
        self.p1 = np.array([(size-0.1)/2, 0, 0, 1]).T
        self.p2 = np.array([0,(size/2), 0, 1]).T
        self.p3 = np.array([-(size/2),(size/6), 0, 1]).T
        self.p4 = np.array([-(size+0.2)/2, 0, 0, 1]).T
        self.p5 = np.array([-(size+0.2)/2, 0,(size/6), 1]).T
        self.p6 = np.array([-(size/2),-(size/6), 0, 1]).T
        self.p7 = np.array([0,-(size/2), 0, 1]).T
        self.p8 = np.array([-(size/2),0, 0, 1]).T

        self.x_data = []
        self.y_data = []
        self.z_data = []
        self.show_animation = show_animation

        if self.show_animation:
            plt.ion()
            fig = plt.figure()
            # for stopping simulation with the esc key.
            fig.canvas.mpl_connect('key_release_event',
                    lambda event: [exit(0) if event.key == 'escape' else None])

            self.ax = fig.add_subplot(111, projection='3d')

        self.update_pose(x, y, z, roll, pitch, yaw)

    def update_pose(self, x, y, z, roll, pitch, yaw):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.x_data.append(x)
        self.y_data.append(y)
        self.z_data.append(z)

        if self.show_animation:
            self.plot()

    def transformation_matrix(self):
        x = self.x
        y = self.y
        z = self.z
        roll = self.roll
        pitch = self.pitch
        yaw = self.yaw
        return np.array(
            [[cos(yaw) * cos(pitch), -sin(yaw) * cos(roll) + cos(yaw) * sin(pitch) * sin(roll), sin(yaw) * sin(roll) + cos(yaw) * sin(pitch) * cos(roll), x],
             [sin(yaw) * cos(pitch), cos(yaw) * cos(roll) + sin(yaw) * sin(pitch)
              * sin(roll), -cos(yaw) * sin(roll) + sin(yaw) * sin(pitch) * cos(roll), y],
             [-sin(pitch), cos(pitch) * sin(roll), cos(pitch) * cos(yaw), z]
             ])

    def plot(self):  # pragma: no cover
        T = self.transformation_matrix()

        #p1_t = np.matmul(T, self.p1)
        #p2_t = np.matmul(T, self.p2)
        #p3_t = np.matmul(T, self.p3)
        #p4_t = np.matmul(T, self.p4)
        #p5_t = np.matmul(T, self.p5)
        #p6_t = np.matmul(T, self.p6)
        #p7_t = np.matmul(T, self.p7)
        #p8_t = np.matmul(T, self.p8)


        plt.cla()

        #self.ax.plot([p1_t[0], p2_t[0], p3_t[0], p4_t[0], p5_t[0], p6_t[0], p7_t[0], p8_t[0]],
        #             [p1_t[1], p2_t[1], p3_t[1], p4_t[1], p5_t[1], p6_t[1], p7_t[1], p8_t[1]],
        #             [p1_t[2], p2_t[2], p3_t[2], p4_t[2], p5_t[2], p6_t[2], p7_t[2], p8_t[2]], 'k.', markersize=4)

        #self.ax.plot([p1_t[0], p4_t[0]], [p1_t[1], p4_t[1]],
        #             [p1_t[2], p4_t[2]], 'r-')

        #self.ax.plot([p2_t[0], p7_t[0]], [p2_t[1], p7_t[1]],
        #             [p2_t[2], p7_t[2]], 'r-')

        #self.ax.plot([p3_t[0], p6_t[0]], [p3_t[1], p6_t[1]],
        #             [p3_t[2], p6_t[2]], 'r-')
        
        #self.ax.plot([p4_t[0], p5_t[0]], [p4_t[1], p5_t[1]],
        #             [p4_t[2], p5_t[2]], 'r-')
        
        #self.ax.plot([p5_t[0], p8_t[0]], [p5_t[1], p8_t[1]],
        #             [p5_t[2], p8_t[2]], 'r-')
        

        #self.ax.plot(self.x_data, self.y_data, self.z_data, 'b:')

        
        points = []
        import csv
        with open('/home/josuehfa/PFC/Mesh_3.asc') as mesh_file:
            csv_reader = csv.reader(mesh_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                points.append(np.array([float(row[0])/100, float(row[1])/100, float(row[2])/100, 1]).T)

                #X_mesh.append(float(row[0])/100)
                #Y_mesh.append(float(row[1])/100)
                #Z_mesh.append(float(row[2])/100)
        
        points_t = []
        for point in points:
            points_t.append(np.matmul(T, point))


        x_mesh = []
        y_mesh = []
        z_mesh = []
        for point_t in points_t:
            x_mesh.append(point_t[0])
            y_mesh.append(point_t[1])
            z_mesh.append(point_t[2])

        self.ax.plot(x_mesh, y_mesh, z_mesh, 'b*', markersize=0.6)
        plt.xlim(-400, 400)
        plt.ylim(-400, 400)
        self.ax.set_zlim(-400, 400)

        plt.pause(0.02)


#air = Aircraft()
#air.plot()