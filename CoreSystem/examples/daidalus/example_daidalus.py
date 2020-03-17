
from daidalus_wrapper import ConstrainedDelaunayTriangulation as CDT
from daidalus_wrapper import Point
from daidalus_wrapper import Daidalus
from daidalus_wrapper import Units
from daidalus_wrapper import LatLonAlt
from daidalus_wrapper import Position 
from daidalus_wrapper import Velocity 
import daidalus_wrapper as DWrapper
	

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib, time



class plot3dClass( object ):

        def __init__( self, systemSideLength, lowerCutoffLength ):
            self.systemSideLength = systemSideLength
            self.lowerCutoffLength = lowerCutoffLength
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot( 111, projection='3d' )
            self.ax.set_zlim3d( -10e-9, 10e9 )

            rng = np.arange( 0, self.systemSideLength, self.lowerCutoffLength )
            self.X, self.Y = np.meshgrid(rng,rng)

            self.ax.w_zaxis.set_major_locator( LinearLocator( 10 ) )
            self.ax.w_zaxis.set_major_formatter( FormatStrFormatter( '%.03f' ) )

            heightR = np.zeros( self.X.shape )
            self.surf = self.ax.plot_surface( 
                self.X, self.Y, heightR, rstride=1, cstride=1, 
                cmap=cm.jet, linewidth=0, antialiased=False )
            # plt.draw() maybe you want to see this frame?

        def drawNow( self, heightR ):
            self.surf.remove()
            self.surf = self.ax.plot_surface( 
                self.X, self.Y, heightR, rstride=1, cstride=1, 
                cmap=cm.jet, linewidth=0, antialiased=False )
            plt.draw()                      # redraw the canvas
            time.sleep(1)


def printDetection(daa):
    # Aircraft at index 0 is ownship
    for ac_idx in range (0, daa.lastTrafficIndex()+1 ):
        t2los = daa.timeToViolation(ac_idx)
        if (t2los >= 0):
            print("Predicted Time to Loss of Well Clear with " + str(daa.getAircraftState(ac_idx).getId()) + ": " + DWrapper.Fm2(t2los) + " [s]")
        
def printAlerts(daa):
    #Aircraft at index 0 is ownship
    for ac_idx in range (0, daa.lastTrafficIndex() + 1):
        alert = daa.alerting(ac_idx)
        if (alert > 0):
            print( "Alert Level " + str(alert) + " with " +	daa.getAircraftState(ac_idx).getId())

def main():
    cdt = CDT()
    va = cdt.insert(Point(100, 269))
    vb = cdt.insert(Point(246, 269))
    vc = cdt.insert(Point(246, 223))
    vd = cdt.insert(Point(303, 223))
    ve = cdt.insert(Point(303, 298))
    vf = cdt.insert(Point(246, 298))
    vg = cdt.insert(Point(246, 338))
    vh = cdt.insert(Point(355, 338))
    vi = cdt.insert(Point(355, 519))
    vj = cdt.insert(Point(551, 519))
    vk = cdt.insert(Point(551, 445))
    vl = cdt.insert(Point(463, 445))
    vm = cdt.insert(Point(463, 377))
    vn = cdt.insert(Point(708, 377))
    vo = cdt.insert(Point(708, 229))
    vp = cdt.insert(Point(435, 229))
    vq = cdt.insert(Point(435, 100))
    vr = cdt.insert(Point(100, 100))

    cdt.insert_constraint(va, vb)
    cdt.insert_constraint(vb, vc)
    cdt.insert_constraint(vc, vd)
    cdt.insert_constraint(vd, ve)
    cdt.insert_constraint(ve, vf)
    cdt.insert_constraint(vf, vg)
    cdt.insert_constraint(vg, vh)
    cdt.insert_constraint(vh, vi)
    cdt.insert_constraint(vi, vj)
    cdt.insert_constraint(vj, vk)
    cdt.insert_constraint(vk, vl)
    cdt.insert_constraint(vl, vm)
    cdt.insert_constraint(vm, vn)
    cdt.insert_constraint(vn, vo)
    cdt.insert_constraint(vo, vp)
    cdt.insert_constraint(vp, vq)
    cdt.insert_constraint(vq, vr)
    cdt.insert_constraint(vr, va)

    vs = cdt.insert(Point(349, 236))
    vt = cdt.insert(Point(370, 236))
    vu = cdt.insert(Point(370, 192))
    vv = cdt.insert(Point(403, 192))
    vw = cdt.insert(Point(403, 158))
    vx = cdt.insert(Point(349, 158))

    cdt.insert_constraint(vs, vt)
    cdt.insert_constraint(vt, vu)
    cdt.insert_constraint(vu, vv)
    cdt.insert_constraint(vv, vw)
    cdt.insert_constraint(vw, vx)
    cdt.insert_constraint(vx, vs)

    vy = cdt.insert(Point(501, 336))
    vz = cdt.insert(Point(533, 336))
    v1 = cdt.insert(Point(519, 307))
    v2 = cdt.insert(Point(484, 307))

    cdt.insert_constraint(vy, vz)
    cdt.insert_constraint(vz, v1)
    cdt.insert_constraint(v1, v2)
    cdt.insert_constraint(v2, vy)

    print("Number of vertices:", cdt.number_of_vertices())


    daa = Daidalus()
    daa.set_Buffered_WC_SC_228_MOPS(True)
    print("Number of Aircraft: " + str(daa.numberOfAircraft()))

    unit = Units()

    unit_from = unit.from_unit('deg',21)
    print ("Unit Test:" + str(unit_from))

    latlon = LatLonAlt()
    latlon = latlon.make(21,"deg", 21,"deg", 8700.0,"ft")
    print ("Lat:" + str(latlon.lat()))
    print ("Lon:" + str(latlon.lon()))
    print ("Alt:" + str(latlon.alt()))
    print ("latitude:" + str(latlon.latitude()))
    


    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    

    lat_in = np.array([])
    lon_in = np.array([])
    alt_in = np.array([])

    lat_on = np.array([])
    lon_on = np.array([])
    alt_on = np.array([])
    

    for time in range (50):
        print("Time: " + str(time))
        
        so = Position.makeLatLonAlt(33.95 - time,"deg", -96.7,"deg", 8900.0,"ft")
        vo = Velocity.makeTrkGsVs(206.0,"deg", 151.0 * time/5,"knot", 0.0,"fpm")
        daa.setOwnshipState("ownship",so,vo,time)
        print("Position Ownship:" + so.toStringUnits())
        print("Velocity Ownship:" + vo.toStringNP())

        si = Position.makeLatLonAlt(-33.86191658 + time,"deg", -96.73272601,"deg", 9000.0,"ft")
        vi = Velocity.makeTrkGsVs(0.0,"deg", 210.0,"knot", 0,"fpm")
        daa.addTrafficState("ith-intruder",si,vi)
        print("Position Intruder:" + si.toStringUnits())
        print("Velocity Intruder:" + vi.toStringNP())

        wind = Velocity.makeTrkGsVs(45,"deg", 10,"knot", 0,"fpm")
        daa.setWindField(wind)

        #print(daa.toString())
        print("Number of Aircraft: " + str(daa.numberOfAircraft()))
        print("Last Aircraft Index: " + str(daa.lastTrafficIndex()))

       
        printDetection(daa)
        printAlerts(daa)


        lat_in = np.append(lat_in, [33.86191658 - time])
        lon_in = np.append(lon_in, [-96.73272601])
        alt_in = np.append(alt_in, [9000])

        lat_on = np.append(lat_on, [-33.95 + time])
        lon_on = np.append(lon_on, [-96.7])
        alt_on = np.append(alt_on, [8900])

        ax.scatter(lat_in, lon_in, alt_in, c ='r')
        ax.scatter(lat_on, lon_on, alt_on, c ='b')

        ax.set_xlim(-100, 100)
        ax.set_ylim(-200, 200)
        ax.set_zlim(0, 15000)
        plt.draw()
        plt.pause(0.4)
        ax.cla()


    # mpl.rcParams['legend.fontsize'] = 10

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')

    # # Prepare arrays x, y, z
    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z**2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)

    # ax.plot(x, y, z, label='parametric curve')
    # ax.legend()

    # plt.show()



    

    #plt.ion()
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    

    #for k in range(1, 10):
    #    theta = np.linspace(-4 * np.pi, 4 * np.pi, 10*k)
    #    z = np.linspace(-2, 2, 10*k)
    #    r = z**2 + 1
    #    x = r * np.sin(theta)
    #    y = r * np.cos(theta)
    #    ax.plot(x, y, z)
    #    plt.draw()
    #    plt.pause(0.2)
    #    ax.cla()
        


if __name__ == '__main__':
    main()

