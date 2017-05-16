# -*- coding: utf-8 -*-
#
# This file is part of the python-shogi library.
# Copyright (C) 2012-2014 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>
# Copyright (C) 2015- Tasuku SUENAGA <tasuku-s-github@titech.ac>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from Cython.Distutils import build_ext
import setuptools
import os

__author__ = 'Tasuku SUENAGA a.k.a. gunyarakun'
__email__ = 'tasuku-s-github@titech.ac'
__version__ = '1.0.2'

ext_modules = [
    setuptools.Extension('cyshogi.KIF', sources=['cyshogi/KIF.pyx']),
    setuptools.Extension('cyshogi.Person', sources=['cyshogi/Person.pyx']),
    setuptools.Extension('cyshogi.cyshogi', sources=['cyshogi/cyshogi.pyx']),
    ]

def read_description():
  description = open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8').read()
  return description

setuptools.setup(
    name = 'cython-shogi',
    version = __version__,
    author = __author__,
    author_email = __email__,
    description = 'A Cython shogi library with move generation and validation and handling of common formats.',
    long_description = read_description(),
    license = "GPL3",
    keywords = 'shogi csa kif',
    url = 'https://github.com/YusukeSuzuki/cython-shogi',
    packages = ['cyshogi'],
    scripts = [],
    test_suite = 'nose.collector',
    tests_require = ['nose>=1.0', 'mock'],
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Topic :: Games/Entertainment :: Board Games',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)
