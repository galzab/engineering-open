import math
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
    def __init__(self, name):
        super(StructuralElement, self).__init__(name)

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

    def __init__(self, name, material):
        super(BeamSection2d, self).__init__(name)
        self.material=material
        self.A = 0.0
        self.Sy = 0.0
        self.Sz = 0.0
        self.Iyy = 10.0
        self.Izz = 0.0
        self.Iyz = 0.0
        self.Izy = 0.0

    def __unicode__(self):
        return 'Beam section %s' % self.name

    @property
    def shortname(self):
        return self.name

    @property
    def EIyy(self):
        return (self.material.E*self.Iyy)

class Node2d(Point2d,StructuralElement):
    """
    Model for 2D nodes
    """
    def __init__(self, name, x, y):
        super(Node2d, self).__init__(x, y)
        super(StructuralElement, self).__init__(name)

    def __unicode__(self):
        return 'Node2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s)" % (str(self),self.x,self.y)

class Beam2d(StructuralElement):
    """
    Model for 2D beams
    """

    def __init__(self, name, startnode, endnode, beamsection):
        super(Beam2d, self).__init__(name)
        self.startnode = startnode
        self.endnode = endnode
        self.beamsection = beamsection

    def __unicode__(self):
        return 'Beam2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s) %s" % (str(self), str(self.startnode), str(self.endnode), str(self.beamsection))

    @property
    def dx(self):
        return self.endnode.x-self.startnode.x
 
    @property
    def dy(self):
        return self.endnode.y-self.startnode.y
 
    @property
    def length(self):
        return math.sqrt(self.dx**2+self.dy**2)

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

    @property
    def description(self):
        s=str(self)+"\n"
        for node in self.n:
          s+=node.description+"\n"
        for element in self.e:
          s+=element.description+"\n"
        return s

    def addNode(self, node):
        """Adds a node to the structure"""
        self.n.append(node)

    def addElement(self, element):
        """Adds an element to the structure"""
        self.e.append(element)

    @property
    def nodeCount(self):
        return len(self.n)
