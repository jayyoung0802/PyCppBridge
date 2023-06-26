from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules = cythonize(Extension(
    'demo', # the extension name
    sources=['demo.pyx'], # Cython source
    language='c++', # or "c"
    include_dirs=[numpy.get_include()],  # Specifies the include directories for necessary header files
    library_dirs=[],  # Specifies the library directories for linking
    libraries=[],     # Specifies the library names for linking
    extra_compile_args=[], # Specifies additional parameters for compilation
    extra_link_args=[] # Specifies additional parameters for linking
)))