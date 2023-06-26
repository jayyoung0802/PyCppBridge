# PyCppBridge

Examples show bidirectional interaction between Python and C++.

### cython

```Shell
cd cython/
bash compile.sh
python demo.py
```

### pybind

```Shell
cd pybind/
git clone https://github.com/pybind/pybind11.git
bash compile.sh
python main.py
```

Another Compile Method: (Reference: https://www.jianshu.com/p/0b4b49dd706a)

```Shell
cd pybind/
git clone https://github.com/pybind/pybind11.git
cd another_compile/
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)
python run_example.py
```
