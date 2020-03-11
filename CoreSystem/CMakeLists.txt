cmake_minimum_required(VERSION 3.11.0)

set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

project(CoreSystem)

# CGAL and its components
find_package( CGAL QUIET COMPONENTS Core GMP MPFI )

if ( NOT CGAL_FOUND )

    message(STATUS "This project requires the CGAL library, and will not be compiled.")
    return()

endif()

# include helper file
include( ${CGAL_USE_FILE} )


# Boost and its components
find_package( Boost REQUIRED )

if ( NOT Boost_FOUND )

    message(STATUS "This project requires the Boost library, and will not be compiled.")

    return()

endif()



find_library(daidalus "daidalus" "/src" "/lib")

if( NOT daidalus_FOUND )
    message(STATUS "Daidalus Library not found... Building the library...")
    include_directories(lib/daidalus/include)
    file(GLOB SOURCES "lib/daidalus/src/*.cpp")
    add_library(daidalus SHARED ${SOURCES})
endif()



set(SOURCE_DIR "src/wrapper")
include_directories(${SOURCE_DIR})

add_subdirectory(lib/pybind11)
pybind11_add_module(daidalus_wrapper ${SOURCES} "${SOURCE_DIR}/daidalus_wrapper.cpp")
target_link_libraries(daidalus_wrapper PRIVATE daidalus)