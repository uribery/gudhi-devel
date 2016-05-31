from distutils.core import setup, Extension
from Cython.Build import cythonize

"""This file is part of the Gudhi Library. The Gudhi library
   (Geometric Understanding in Higher Dimensions) is a generic C++
   library for computational topology.

   Author(s):       Vincent Rouvreau

   Copyright (C) 2016  INRIA Saclay (France)

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Vincent Rouvreau"
__copyright__ = "Copyright (C) 2016  INRIA Saclay (France)"
__license__ = "GPL v3"

gudhi = Extension(
    "gudhi",
    sources = ['gudhi.pyx',],
    language = 'c++',
    extra_compile_args=['-frounding-math','-std=c++11','-DCGAL_EIGEN3_ENABLED','-DCGAL_USE_GMP','-DCGAL_USE_GMPXX','-DCGAL_USE_MPFR'],
    libraries=['mpfr','gmpxx','gmp','CGAL'],
    library_dirs=['/usr/local/lib/'],
    include_dirs = ['../include','./src/cpp','/usr/local/include/eigen3'],
)

setup(
    name = 'gudhi',
    author='Vincent Rouvreau',
    author_email='gudhi-contact@lists.gforge.inria.fr',
    version='0.1.0',
    url='http://gudhi.gforge.inria.fr/',
    ext_modules = cythonize(gudhi),
)
