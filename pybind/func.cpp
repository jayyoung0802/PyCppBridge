#include <iostream>
#include <vector>
#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

std::vector<std::vector<double>> matrix_multiply(const std::vector<std::vector<double>>& A, const std::vector<std::vector<double>>& B) {
    int n = A.size();
    int m = B[0].size();
    int p = A[0].size();

    std::vector<std::vector<double>> result(n, std::vector<double>(m, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < p; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}


namespace py = pybind11;

PYBIND11_MODULE(func, m) {
    m.def("matrix_multiply", &matrix_multiply, "Matrix multiplication");
}