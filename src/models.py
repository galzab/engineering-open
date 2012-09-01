from geometry import Point2d

class StructuralElement():
    """
    Model for structural elements
    """
    def __unicode__(self):
        return 'Structural Element'

class Material():
    """
    Model for materials
    """
    E = 0.0
    G = 0.0

    def __unicode__(self):
        return 'Material'

class BeamSection():
    """
    Model for beam sections
    """
    A = 0.0
    Sy = 0.0
    Sz = 0.0
    Iyy = 0.0
    Izz = 0.0
    Iyz = 0.0
    Izy = 0.0

    def __unicode__(self):
        return 'Beam section'

class Node2d(Point2d,StructuralElement):
    """
    Model for 2D nodes
    """
    def __unicode__(self):
        return 'Node2d'

class Beam2d(StructuralElement):
    """
    Model for 2D beams
    """
    section = BeamSection()

    def __unicode__(self):
        return 'Beam2d'

class Structure():
    """
    Model for the structure
    """
    n = []
    e = []

    def __unicode__(self):
        return 'Structure'

    def addNode(node):
        """Adds a node to the structure"""
        n.append(node)

    def addElement(element):
        """Adds an element to the structure"""
        e.append(element)
