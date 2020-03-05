#include <pybind11/pybind11.h>

#include "Daidalus.h"

namespace py = pybind11;

using daa = Daidalus;

PYBIND11_MODULE(daidalus_wrapper, m)
{

    py::class_<daa>(m, "Daidalus")
        .def(py::init())
        //.def(py::init(daa&))
        .def(py::init<double, double>(), py::arg("x"), py::arg("y"))
        .def_property_readonly("x", &Point::x)
        .def_property_readonly("y", &Point::y)
        .def("__repr__",
             [](const Point &p) {
                 std::string r("Point(");
                 r += boost::lexical_cast<std::string>(p.x());
                 r += ", ";
                 r += boost::lexical_cast<std::string>(p.y());
                 r += ")";
                 return r;
             })
        .def("__hash__",
             [](const Point &p) {
                 std::hash<double> double_hash;
                 auto x_hash = double_hash(p.x());
                 auto y_hash = double_hash(p.y());
                 return y_hash ^ x_hash + 0x9e3779b9 + (y_hash << 6) + (y_hash >> 2);
             }
        )
        .def("__eq__",
            [](const Point &p, const Point & q) {
                return p == q;
            }
        )
        ;
}