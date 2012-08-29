class PointXd():
    """
    Model for general points in x dimensions
    """
    def __init__(self):
         return 'PointXd'

class Point2d(PointXd):
    """
    Model for 2D points
    """
    x = 0.0
    y = 0.0
    def __init__(self):
        return 'Point2d'

class Point3d(PointXd):
    """
    Model for 3D points
    """
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self):
        return 'Point3d'

class StructuralElement():
    """
    Model for structural elements
    """
    def __init__(self):
        return 'Structural Element'

class Material():
    """
    Model for materials
    """
    E = 0.0
    G = 0.0

    def __init__(self):
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

    def __init__(self):
        return 'Beam section'

class Node2d(Point2d,StructuralElement):
    """
    Model for 2D nodes
    """
    def __init__(self):
        return 'Node2d'

class Beam2d(StructuralElement):
    """
    Model for 2D beams
    """
    section = BeamSection()

    def __init__(self):
        return 'Beam2d'

class Structure():
    """
    Model for the structure
    """

    def __init__(self):
         return 'Structure'
