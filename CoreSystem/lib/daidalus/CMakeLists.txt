cmake_minimum_required(VERSION 2.8.9)
project(daidalus)

message(STATUS "Daidalus CMakeList.txt.")

set(LIBRARY_OUTPUT_PATH  ${CMAKE_BINARY_DIR}/lib)


#Bring the headers, such as Student.h into the project
include_directories(include)
include_directories(${CMAKE_SOURCE_DIR})

#Can manually add the sources using the set command as follows:
#set(SOURCES src/mainapp.cpp src/Student.cpp)

#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES "src/*.cpp")

add_library(daidalus SHARED ${SOURCES})

set(SRC_Example ${SOURCES} "example/DaidalusExample.cpp")
add_executable(DaidalusExample ${SRC_Example})

set(SRC_Alerting ${SOURCES} "example/DaidalusAlerting.cpp")
add_executable(DaidalusAlerting ${SRC_Alerting})

set(SRC_Batch ${SOURCES} "example/DaidalusBatch.cpp")
add_executable(DaidalusBatch ${SRC_Batch})