import sys
sys.path.append("..")
sys.path.append("../..")

import unittest
import pss
import models

from models import Material
from models import BeamSection2d
from models import Structure
from models import Node2d
from models import Beam2d

class ParticleSpringSystemAlgorithmTests(unittest.TestCase):
    """Tests for Particle Spring System algorithm"""

    def setUp(self):
        steel=Material("Steel", 1.0, 1.0)
        section=BeamSection2d("HE200A", steel)
        self.structure=Structure("001")
        for i in range(10):
            self.structure.addNode(Node2d("%s" % str(i+1),0.0+i,0.0))
        for i in range(9):
            self.structure.addElement(Beam2d("%s" % str(i+1), self.structure.n[i], self.structure.n[i+1], section))

    def test_something(self):
        print(self.structure.description)
        self.assertEqual(True,False)

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
