from geometry import Point2d
from geometry import CoreClass

class StructuralBaseClass(CoreClass):
    """
    Model for top level structural entity
    """

    def __init__(self, name):
        self.name = name

class StructuralElement(StructuralBaseClass):
    """
    Model for structural elements
    """

    def __unicode__(self):
        return 'Structural Element %s' % self.name

class Material(StructuralBaseClass):
    """
    Model for materials
    """

    def __init__(self, name, E, G):
        super(Material, self).__init__(name)
        self.E = E
        self.G = G

    def __unicode__(self):
        return 'Material %s' % self.name

    @property
    def shortname(self):
        return self.name

class BeamSection2d(StructuralBaseClass):
    """
    Model for beam sections
    """

    def __init__(self):
        A = 0.0
        Sy = 0.0
        Sz = 0.0
        Iyy = 0.0
        Izz = 0.0
        Iyz = 0.0
        Izy = 0.0

    def __unicode__(self):
        return 'Beam section %s' % self.name

class Node2d(Point2d,StructuralElement):
    """
    Model for 2D nodes
    """
    def __unicode__(self):
        return 'Node2d %s' % self.name

class Beam2d(StructuralElement):
    """
    Model for 2D beams
    """

    def __unicode__(self):
        return 'Beam2d %s' % self.name

class Structure(StructuralBaseClass):
    """
    Model for the structure
    """

    def __init__(self, name):
        super(Structure, self).__init__(name)
        self.n = []
        self.e = []

    def __unicode__(self):
        return 'Structure %s' % self.name

    def addNode(self, node):
        """Adds a node to the structure"""
        self.n.append(node)

    def addElement(self, element):
        """Adds an element to the structure"""
        self.e.append(element)

    @property
    def nodeCount(self):
        return len(self.n)
