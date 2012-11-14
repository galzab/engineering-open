import sys
sys.path.append("..")

import unittest
from models import Structure
from models import Node2d

class StructureTests(unittest.TestCase):
    """Tests for Structure"""

    def test_unicode(self):
        structure=Structure('001')
        self.assertEqual(str(structure), 'Structure 001')

    def test_add_node(self):
        structure=Structure('001')
        node1=Node2d(0.0,0.0)
        structure.addNode(node1)
        self.assertEqual(structure.nodeCount, 1)

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
