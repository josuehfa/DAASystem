cmake_minimum_required(VERSION 2.8.9)
project(daidalus)
set(CMAKE_BUILD_TYPE Release)  
 

#Bring the headers, such as Student.h into the project
include_directories(include)

#Can manually add the sources using the set command as follows:
#set(SOURCES src/mainapp.cpp src/Student.cpp)

#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES "src/*.cpp")
#list(REMOVE_ITEM SOURCES "src/DaidalusExample.cpp" "src/DaidalusAlerting.cpp" "src/DaidalusBatch.cpp")

add_library(daidalus SHARED ${SOURCES})
target_include_directories(daidalus PUBLIC include)
#install(TARGETS daidalus DESTINATION /usr/lib) 

set(SRC_Example ${SOURCES} "example/DaidalusExample.cpp")
add_executable(DaidalusExample ${SRC_Example})

set(SRC_Alerting ${SOURCES} "example/DaidalusAlerting.cpp")
add_executable(DaidalusAlerting ${SRC_Alerting})

set(SRC_Batch ${SOURCES} "example/DaidalusBatch.cpp")
add_executable(DaidalusBatch ${SRC_Batch})