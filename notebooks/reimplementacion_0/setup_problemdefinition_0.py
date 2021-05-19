from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("reimplementacion_0/problem_definition_0.pyx", compiler_directives={'language_level' : 3}))
