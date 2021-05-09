from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("reimplementacion_1/problem_definition_1.pyx", compiler_directives={'language_level' : 3}))
