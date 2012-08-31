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


