from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("reimplementacion_0/simplex_networks_0.pyx", compiler_directives={'language_level' : 3}))
