from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("reimplementacion_2/general_2.pyx", compiler_directives={'language_level' : 3}))
