#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name="mex",
      version="0.2",
      description=u"Paquete que resuelve metodo simplex",
      url="",
      author="cecyar, lecepe00, eduardo-moreno, caroacostatovany",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "numpy",
                          "pandas",
                          "sphinx",
                          "scipy",
                          "line_profiler",
                          "memory_profiler",
                          "guppy3"
                          ],
      cmdclass={'build_ext': build_ext},
      ext_modules=[Extension("mex_c", sources=["mex/mex_c/general_c.pyx"], cython_directives={"embedsignature": True} )]
      )
