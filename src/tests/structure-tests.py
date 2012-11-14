import sys
sys.path.append("..")

import unittest
from models import Structure

class StructureTests(unittest.TestCase):
    """Tests for Structure"""

    def test_unicode(self):
        structure=Structure('001')
        self.assertEqual(str(structure), 'Structure 001')

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
