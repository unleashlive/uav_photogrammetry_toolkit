cmake_minimum_required (VERSION 2.8)
project (SIFT_DOB)

find_package(OpenCV REQUIRED)

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS} -O3")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS} -O3")
endif()

include_directories(
    ${OPENCV_INCLUDE_DIRS}
    ${CMAKE_SOURCE_DIR}/include/
)

#set(CMAKE_C_FLAGS_RELEASE "-O0 -g3 -Wall -c -fmessage-length=0 -std=c++0x -MMD -MP")
#set(CMAKE_C_FLAGS_DEBUG "-O0 -g3 -Wall -c -fmessage-length=0 -std=c++0x -MMD -MP")

#add_definitions(-DVERBOSE)

add_executable(main
    src/main.cpp
    #src/sift.cpp
    src/write_sift.cpp
    src/write_mat.cpp
)
target_link_libraries(main ${OpenCV_LIBS})
