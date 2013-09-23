"""
engineering-open: open-source tooling for engineering
Copyright (C) 2013 Jeroen Coenders

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""
import sys
sys.path.append("tests")
sys.path.append("algorithms/tests")
sys.path.append("calculations/tests")

import unittest

tests = ['geometry-tests',
         'structure-tests',
         'pss-tests',
         'mechanics-tests',
         'fem2d-tests'
        ]

suite = unittest.TestLoader().loadTestsFromNames(tests)
unittest.TextTestRunner(verbosity=2).run(suite)
