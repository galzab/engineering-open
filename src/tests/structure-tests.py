import sys
sys.path.append("..")

import unittest
from models import StructuralElement
from models import Material
from models import BeamSection2d
from models import Structure
from models import Node2d

class StructuralElementTests(unittest.TestCase):
    """Tests for StructuralElement"""

    def test_unicode(self):
        element=StructuralElement('002')
        self.assertEqual(str(element), 'Structural Element 002')

class MaterialTests(unittest.TestCase):
    """Tests for Material"""

    def test_unicode(self):
        steel=Material('Steel', 1.0, 2.0)
        self.assertEqual(str(steel), 'Material Steel')

    def test_shortname(self):
        steel=Material('Steel', 1.0, 2.0)
        self.assertEqual(steel.shortname, 'Steel')

class BeamSection2dTests(unittest.TestCase):
    """Tests for BeamSection2d"""

    def test_unicode(self):
        he200a=BeamSection2d('HE200A')
        self.assertEqual(str(he200a), 'Beam section HE200A')

    def test_shortname(self):
        he200a=BeamSection2d('HE200A')
        self.assertEqual(he200a.shortname, 'HE200A')

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
