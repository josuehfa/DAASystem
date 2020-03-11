
from daidalus_wrapper import ConstrainedDelaunayTriangulation as CDT
from daidalus_wrapper import Point
from daidalus_wrapper import Daidalus
#from daidalus_wrapper import Position 
#from daidalus_wrapper import Veocity 


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
    print("Number of Aircraft: " + str(daa.numberOfAircraft()) )
#   parameters = "parameters.txt"
#   daa.parameters.saveToFile(parameters)

#   so = Position.makeLatLonAlt(33.95,"deg", -96.7,"deg", 8700.0,"ft")
#	vo = Velocity.makeTrkGsVs(206.0,"deg", 151.0,"knot", 0.0,"fpm")
#	daa.setOwnshipState("ownship",so,vo,t)
    
#   Position si = Position::makeLatLonAlt(33.86191658,"deg", -96.73272601,"deg", 9000.0,"ft");
#	Velocity vi = Velocity::makeTrkGsVs(0.0,"deg", 210.0,"knot", 0,"fpm");
#	daa.addTrafficState("ith-intruder",si,vi);

#   Velocity wind = Velocity::makeTrkGsVs(45,"deg", 10,"knot", 0,"fpm");
#	daa.setWindField(wind);

#   std::cout << daa.toString() << std::endl; 

#   std::cout << "Number of Aircraft: " << daa.numberOfAircraft() << std::endl;
#	std::cout << "Last Aircraft Index: " << daa.lastTrafficIndex() << std::endl;
#   printDetection(daa);

#   void printDetection(Daidalus& daa) {
#       // Aircraft at index 0 is ownship
#       for (int ac_idx=1; ac_idx <= daa.lastTrafficIndex(); ++ac_idx) {
#           double t2los = daa.timeToViolation(ac_idx);
#           if (t2los >= 0) {
#               std::cout << "Predicted Time to Loss of Well Clear with " << daa.getAircraftState(ac_idx).getId() << ": " <<
#                       Fm2(t2los) << " [s]" << std::endl;
#           }
#       }
#   }




if __name__ == '__main__':
    main()

