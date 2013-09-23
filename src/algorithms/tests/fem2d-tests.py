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
sys.path.append(".")
sys.path.append("algorithms")
sys.path.append("..")
sys.path.append("../..")

import unittest
import fem2d
import models
import math

from models import Structure

class FEM2dAlgorithmTests(unittest.TestCase):
    """Tests for FEM2d"""

    def setUp(self):
        #set up the structure
        self.structure=Structure("001")
        
    def test_nodeCount(self):
        self.assertEqual(self.structure.nodeCount,2)
    
"""Set up the test suite"""
if __name__ == '__main__':
    current_module = sys.modules[__name__]
    suite = unittest.TestLoader().loadTestsFromModule(current_module)
    unittest.TextTestRunner(verbosity=2).run(suite)