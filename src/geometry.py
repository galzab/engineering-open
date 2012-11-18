class CoreClass():
    """
    Core class for all objects
    """
    def __unicode__(self):
        """Unicode representation of the object"""
        return 'CoreClass'

    def __str__(self):
        """Makes sure that __str__ returns the __unicode__"""
        return self.__unicode__()

class PointNd(CoreClass):
    """
    Model for general points in n dimensions
    """
    def __unicode__(self):
        return 'PointXd'

class Point2d(PointNd):
    """
    Model for 2D points
    """
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __unicode__(self):
        return 'Point2d'

class Point3d(PointNd):
    """
    Model for 3D points
    """
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __unicode__(self):
        return 'Point3d'


