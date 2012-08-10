"""
Model for general points
"""
class PointXd():
    def __init__(self):
       return 'PointXd'

"""
Model for 2D points
"""
class Point2d(PointXd):
   x = 0.0
   y = 0.0
   def __init__(self):
        return 'Point2d'

"""
Model for 3D points
"""
class Point3d(PointXd):
    x = 0.0
    y = 0.0
    def __init__(self):
        return 'Point3d'

"""
Model for structural elements
"""
class StructuralElement():
    def __init__(self):
        return 'Structural Element'

"""
Model for materials
"""
class Material():
    E = 0.0
    def __init__(self):
        return 'Material'

"""
Model for beam sections
"""
class BeamSection():
    Iyy = 0.0
    Izz = 0.0
    Iyz = 0.0
    Izy = 0.0
    def __init__(self):
        return 'Beam section'

"""
Model for 2D nodes
"""
class Node2d(Point2d,StructuralElement):
    def __init__(self):
        return 'Node2d'

"""
Model for 2D beams
"""
class Beam2d(StructuralElement):
    def __init__(self):
        return 'Beam2d'

"""
Model for the structure
"""
class Structure():
    def __init__(self):
        return 'Structure'
