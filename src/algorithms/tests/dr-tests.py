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
import dr
import models
import math

class DynamicRelaxationAlgorithmTests(unittest.TestCase):
    """Tests for Dynamic Relaxation algorithm"""

    def setUp(self):
        self.stiffness = 10.0
        self.original_length = 0.9
        self.spacing = 1.0
        self.mass = 1.0
        
        #set up the structure
        self.structure=Structure("001")
        
        for i in range(10):
            self.structure.addNode(MassedNode2d("%s" % str(i+1),(self.spacing*i),0.0,self.mass))
        for i in range(9):
            self.structure.addElement(Spring2d("%s" % str(i+1), self.structure.n[i], self.structure.n[i+1], self.stiffness, self.original_length))
        self.structure.n[0].cx=True
        self.structure.n[0].cy=True
        self.structure.n[9].cx=True
        self.structure.n[9].cy=True
    
"""Set up the test suite"""
if __name__ == '__main__':
    current_module = sys.modules[__name__]
    suite = unittest.TestLoader().loadTestsFromModule(current_module)
    unittest.TextTestRunner(verbosity=2).run(suite)