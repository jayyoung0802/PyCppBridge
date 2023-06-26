cmake_minimum_required(VERSION 2.8.12)
project(func)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(PythonInterp REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

add_subdirectory(pybind11)
pybind11_add_module(func func.cpp)