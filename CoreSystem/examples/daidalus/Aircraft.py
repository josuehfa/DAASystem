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
        
        self.x_center = -59.708
        self.y_center = 644.238
        self.z_center = -11868.3
        self.scale = 10000

        self.points = []
        import csv
        with open('/home/josuehfa/PFC/Mesh_3.asc') as mesh_file:
            csv_reader = csv.reader(mesh_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.points.append(np.array([((float(row[0])-self.x_center)/self.scale), \
                                    ((float(row[1])-self.y_center)/self.scale), \
                                    ((float(row[2])-self.z_center)/self.scale), 1]).T)

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
        self.roll = roll  + np.pi/2
        self.pitch = pitch + np.pi/2
        self.yaw = yaw  + np.pi/2
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
            [[cos(roll) * cos(pitch), -sin(roll) * cos(yaw) + sin(yaw) * sin(pitch) * cos(roll) , sin(yaw) * sin(roll) + cos(yaw) * sin(pitch) * cos(roll), x],
             [sin(roll) * cos(pitch), cos(yaw) * cos(roll) + sin(yaw) * sin(pitch)  * sin(roll), -cos(roll) * sin(yaw) + sin(roll) * sin(pitch) * cos(yaw), y],
             [-sin(pitch), cos(pitch) * sin(yaw), cos(pitch) * cos(yaw), z]
             ])

    def plot(self):  # pragma: no cover
        T = self.transformation_matrix()

        points_t = []
        for point in  self.points:
            points_t.append(np.matmul(T, point))

        pt_center = np.matmul(T, np.array([0,0,0,1]).T)
        

        x_mesh = []
        y_mesh = []
        z_mesh = []
        for point_t in points_t:
            x_mesh.append(point_t[0])
            y_mesh.append(point_t[1])
            z_mesh.append(point_t[2])


        plt.cla()

        self.ax.plot(self.x_data, self.y_data, self.z_data, 'b:')

        self.ax.plot(x_mesh, y_mesh, z_mesh, 'k*', markersize=0.8)
        self.ax.plot([pt_center[0],x_mesh[0]],[pt_center[1],y_mesh[0]],[pt_center[2],z_mesh[0]], 'r-', markersize=2)
        
        daa_band = 5

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = daa_band*(np.cos(u)*np.sin(v)) + pt_center[0]
        y = daa_band*(np.sin(u)*np.sin(v)) + pt_center[1]
        z = daa_band*(np.cos(v)) + pt_center[2]
        self.ax.plot_surface(x, y, z, color='#D9FFCB')
        ##FF9393 "red"
        ##FFFF8E "yellow"
        
        #self.ax.plot_wireframe(np.array([x_mesh,np.zeros(len(x_mesh))]), np.array([y_mesh,np.zeros(len(x_mesh))]), np.array([z_mesh,np.zeros(len(x_mesh))]), rstride=10, cstride=10)

        plt.xlim(-15, 15)
        plt.ylim(-15, 15)
        self.ax.set_zlim(-15, 15)

        plt.pause(0.001)

        #plt.pause(60)

#air = Aircraft()
#air.plot()