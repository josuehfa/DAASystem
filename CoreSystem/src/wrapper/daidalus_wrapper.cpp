#include <pybind11/pybind11.h>

#include <ErrorReporter.h>
#include <Daidalus.h>
#include <Position.h>
#include <Velocity.h>
#include <Units.h>
#include <LatLonAlt.h>
#include <format.h>
#include <TrafficState.h>


namespace py = pybind11;

// ------ DAIDALUS ------
using Units = larcfm::Units;
using Daidalus = larcfm::Daidalus;
using Position = larcfm::Position;
using Velocity = larcfm::Velocity;
using LatLonAlt = larcfm::LatLonAlt;
using TrafficState = larcfm::TrafficState;


PYBIND11_MODULE(daidalus_wrapper, m)
{

    // -------- DAIDALUS --------
    m.def("Fm2", &larcfm::Fm2);

    py::class_<Units>(m, "Units")
        .def(py::init<>())
        .def(py::init<Units&>())
        .def_static("from_unit", py::overload_cast<const std::string &, double>
            (&Units::from), "Convert the value from the given units into internal units ")
        ;
        
    py::class_<LatLonAlt>(m, "LatLonAlt")
        .def(py::init<>())
        .def(py::init<LatLonAlt&>())
        .def("lat", &LatLonAlt::lat)
        .def("lon", &LatLonAlt::lon)
        .def("alt", &LatLonAlt::alt)
        .def("latitude", &LatLonAlt::latitude)
        .def_static("make", py::overload_cast<double, std::string, double, std::string, double, std::string>
            (&LatLonAlt::make), "Creates a new position with coordinates (<code>lat</code>,<code>lon</code>,<code>alt</code>)")
        ;

    py::class_<Position>(m, "Position")
        .def(py::init<>())
        .def(py::init<Position&>())
        .def("toStringUnits", py::overload_cast<>
            (&Position::toStringUnits, py::const_), "Return a string representation using the given unit conversions")
        .def_static("makeLatLonAlt", py::overload_cast<double, std::string, double, std::string, double, std::string>
            (&Position::makeLatLonAlt), "Creates a new lat/lon position with coordinates (<code>lat</code>,<code>lon</code>,<code>alt</code>)")
        ;

    py::class_<Velocity>(m, "Velocity")
        .def(py::init<>())
        .def(py::init<Velocity&>())
        .def("toStringNP", py::overload_cast<>
            (&Velocity::toStringNP, py::const_), "String representation, default number of decimal places, without parentheses")
        .def_static("makeTrkGsVs", py::overload_cast<const double, const std::string&, const double, const std::string&, const double, const std::string&>
            (&Velocity::makeTrkGsVs), "New velocity from Track, Ground Speed, and Vertical speed in explicit units.")
        ;    

    py::class_<TrafficState>(m, "TrafficState")
        .def(py::init<>())
        .def(py::init<TrafficState&>())
        .def("getId", &TrafficState::getId)
        ;   

    py::class_<Daidalus>(m, "Daidalus")
        .def(py::init<>())
        .def(py::init<Daidalus&>())
        .def("toString", &Daidalus::toString)
        .def("getCurrentTime", &Daidalus::getCurrentTime)
        .def("set_WC_SC_228_MOPS", &Daidalus::set_WC_SC_228_MOPS)
        .def("set_Buffered_WC_SC_228_MOPS", &Daidalus::set_Buffered_WC_SC_228_MOPS)
        .def("numberOfAircraft", &Daidalus::numberOfAircraft)
        .def("setOwnshipState", py::overload_cast<const std::string &, const Position&, const Velocity&, double>
            (&Daidalus::setOwnshipState), "Clear all aircraft and set ownship state and current time.")
        .def("addTrafficState", py::overload_cast<const std::string&, const Position&, const Velocity&>
            (&Daidalus::addTrafficState),"Add traffic state at current time. Velocity vector is ground velocity.")
        .def("setWindField",&Daidalus::setWindField)
        .def("lastTrafficIndex",&Daidalus::lastTrafficIndex)
        .def("timeToViolation",&Daidalus::timeToViolation)
        .def("getAircraftState", &Daidalus::getAircraftState)
        .def("alerting", py::overload_cast<int>
            (&Daidalus::alerting), "Computes alerting type of ownship and aircraft at index ac_idx for current")
        ;
    
    // ------------------

}
