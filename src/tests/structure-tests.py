import sys
sys.path.append("..")

import unittest
from models import StructuralElement
from models import Material
from models import BeamSection2d
from models import Structure
from models import Node2d
from models import MassedNode2d
from models import Beam2d

class StructuralElementTests(unittest.TestCase):
    """Tests for StructuralElement"""

    def test_unicode(self):
        element=StructuralElement('002')
        self.assertEqual(str(element), 'Structural Element 002')

class Node2dTests(unittest.TestCase):
    """Tests for Node2d"""

    def setUp(self):
        self.node=Node2d('001', 1.0, 2.0)

    def test_unicode(self):
        self.assertEqual(str(self.node), 'Node2d 001')

    def test_description(self):
        self.assertEqual(self.node.description, 'Node 2d 001 (1.0,2.0)')

    def test_x(self):
        self.assertEqual(self.node.x, 1.0)

    def test_y(self):
        self.assertEqual(self.node.y, 2.0)

class MassedNode2dTests(unittest.TestCase):
    """Tests for MassedNode2d"""

    def setUp(self):
        self.node=MassedNode2d('001', 1.0, 2.0, 3.0)

    def test_unicode(self):
        self.assertEqual(str(self.node), 'MassedNode2d 001')

    def test_description(self):
        self.assertEqual(self.node.description, 'MassedNode2d 001 (1.0,2.0) mass 3.0')

    def test_mass(self):
        self.assertEqual(self.node.mass, 3.0)

class MaterialTests(unittest.TestCase):
    """Tests for Material"""

    def setUp(self):
        self.steel=Material('Steel', 1.0, 2.0)
 
    def test_unicode(self):
        self.assertEqual(str(self.steel), 'Material Steel')

    def test_shortname(self):
        self.assertEqual(self.steel.shortname, 'Steel')

class BeamSection2dTests(unittest.TestCase):
    """Tests for BeamSection2d"""

    def setUp(self):
        self.steel=Material('Steel', 1.0, 1.0)
        self.he200a=BeamSection2d('HE200A', self.steel) 

    def test_unicode(self):
        self.assertEqual(str(self.he200a), 'Beam section HE200A')

    def test_shortname(self):
        self.assertEqual(self.he200a.shortname, 'HE200A')

    def test_EIyy(self):
        self.assertEqual(self.he200a.EIyy,10.0)

class Node2dTests(unittest.TestCase):
    """Tests for Node2d"""

    def setUp(self):
        self.node=Node2d('003', 1.0, 2.0)
 
    def test_unicode(self):
        self.assertEqual(str(self.node), 'Node2d 003')

    def test_coordinates(self):
        self.assertEqual(self.node.x, 1.0)
        self.assertEqual(self.node.y, 2.0)

class Beam2dTests(unittest.TestCase):
    """Tests for Beam2d"""

    def setUp(self):
        self.node1=Node2d('001',0.0,0.0)
        self.node2=Node2d('002',10.0,0.0)
        self.steel=Material('Steel',1.0, 1.0)
        self.section=BeamSection2d('HE200A', self.steel)
        self.beam=Beam2d('005', self.node1, self.node2, self.section) 

    def test_unicode(self):
        self.assertEqual(str(self.beam), 'Beam2d 005')

    def test_nodes(self):
        self.assertEqual(self.beam.startnode, self.node1)
        self.assertEqual(self.beam.endnode, self.node2)

    def test_section(self):
        self.assertEqual(self.beam.beamsection, self.section)       

class StructureTests(unittest.TestCase):
    """Tests for Structure"""

    def setUp(self):
        self.structure=Structure('001')

    def test_unicode(self):
        self.assertEqual(str(self.structure), 'Structure 001')

    def test_add_node(self):
        self.node1=Node2d('001',0.0,0.0)
        self.structure.addNode(self.node1)
        self.assertEqual(self.structure.nodeCount, 1)

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
