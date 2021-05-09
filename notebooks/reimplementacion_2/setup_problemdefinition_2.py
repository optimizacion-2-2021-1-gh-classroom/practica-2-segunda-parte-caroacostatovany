from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("reimplementacion_2/problem_definition_2.pyx", compiler_directives={'language_level' : 3}))
