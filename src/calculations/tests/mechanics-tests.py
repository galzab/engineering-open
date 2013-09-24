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
sys.path.append("calculations")
sys.path.append("..")
sys.path.append("../..")

import unittest
import mechanics
import models
from models import Node2d
from models import Beam2d
from models import Material
from models import BeamSection2d
from mechanics import simply_supported_beam_calculation

class SimplySupportedBeamTests(unittest.TestCase):
    """Tests for simply supported beam"""

    def setUp(self):
        node1=Node2d('001',0.0,0.0)
        node2=Node2d('001',1.0,0.0)
        steel=Material('Steel', 1.0, 1.0)
        section=BeamSection2d('HE200A', steel, Iyy=10.0)
        self.beam=Beam2d('beam001', node1, node2, section)

    def test_beam_length(self):
        self.assertEqual(self.beam.length, 1.0)

    def test_beam_dx(self):
        self.assertEqual(self.beam.dx, 1.0)

    def test_beam_dy(self):
        self.assertEqual(self.beam.dy, 0.0)

    def test_results(self):
        results=simply_supported_beam_calculation(self.beam,1.0)
        self.assertEqual(results[0],(1/8))
        self.assertEqual(results[1],(1/2))
        self.assertEqual(results[2],(5/384)*(1/10.0))
        

"""Set up the test suite"""
if __name__ == '__main__':
    current_module = sys.modules[__name__]
    suite = unittest.TestLoader().loadTestsFromModule(current_module)
    unittest.TextTestRunner(verbosity=2).run(suite)

