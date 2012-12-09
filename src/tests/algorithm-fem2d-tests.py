import sys
sys.path.append("..")

import unittest
from algorithms.fem2d import Fem2d

class fem2dTests(unittest.TestCase):
    """Tests for FEM2D algorithm"""
    
    def setUp(self):
        self.algorithm=Fem2d()

    def test_unicode(self):
        self.assertEqual(str(self.algorithm), "FEM2D algorithm")

    def test_start(self):
        self.algorithm.analyse()

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
