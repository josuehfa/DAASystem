cmake_minimum_required(VERSION 3.11.0)

set(CMAKE_VERBOSE_MAKEFILE ON)

project(CoreSystem)

# DAIDALUS and its components
#find_package( CGAL QUIET COMPONENTS Core GMP MPFI )
#if ( NOT CGAL_FOUND )
#    message(STATUS "This project requires the CGAL library, and will not be compiled.")
#    return()
#endif()
# include helper file
#include( ${CGAL_USE_FILE} )


# Boost and its components
#find_package( Boost REQUIRED )
#if ( NOT Boost_FOUND )
#    message(STATUS "This project requires the Boost library, and will not be compiled.")
#    return()
#endif()

set(SOURCE_DIR "src/wrapper")
include_directories(${SOURCE_DIR})

add_subdirectory(lib/daidalus)
add_subdirectory(lib/pybind11)
pybind11_add_module(CoreSystem ${SOURCES} "${SOURCE_DIR}/daidalus_wrapper.cpp")

