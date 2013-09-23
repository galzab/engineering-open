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
from models import Material
from models import Node2d
from models import BeamSection2d
from models import Beam2d
from models import Load2d
from fem2d import Fem2d

class FEM2dAlgorithmTests(unittest.TestCase):
    """Tests for FEM2d"""

    def setUp(self):
        self.spacing=1.0
        self.steel=Material("steel",2.1e5,0.0)
        self.section=BeamSection2d("HE200A",self.steel)
        
        #set up the structure
        self.structure=Structure("001")
        for i in range(10):
            self.structure.addNode(Node2d("%s" % str(i+1),(self.spacing*i),0.0))
        for i in range(9):
            self.structure.addElement(Beam2d("%s" % str(i+1), self.structure.n[i], self.structure.n[i+1], self.section))
        for i in range(10):
            self.structure.addLoad(Load2d("%s" % str(i+1), self.structure.n[i], 0.0, 1.0))
        self.structure.cx=True
        self.structure.cy=True
        
    def test_nodeCount(self):
        self.assertEqual(self.structure.nodeCount,10)
        
    def test_loadCount(self):
        self.assertEqual(self.structure.loadCount,10)
        
    def test_analysis(self):
        fem2d=Fem2d(self.structure)
        self.assertEqual(fem2d.analyse(),True)
    
"""Set up the test suite"""
if __name__ == '__main__':
    current_module = sys.modules[__name__]
    suite = unittest.TestLoader().loadTestsFromModule(current_module)
    unittest.TextTestRunner(verbosity=2).run(suite)