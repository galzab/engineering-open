class CoreClass(object):
    """
    Core class for all objects
    """
    def __unicode__(self):
        """Unicode representation of the object"""
        return 'CoreClass'

    def __str__(self):
        """Makes sure that __str__ returns the __unicode__"""
        return self.__unicode__()

class VectorNd(CoreClass):
    """
    Model for vector in n dimensions
    """

    def __init__(self):
        self._c = []

    def __unicode__(self):
        return 'VectorNd'

    def c_count(self):
        return len(self._c)

    def vector(self):
        s="("
        for cp in self._c:
            s = s + str(cp) + ","
        s = s + ")"
        return s

class PointNd(VectorNd):
    """
    Model for general points in n dimensions
    """

    def __unicode__(self):
        return 'PointNd'

class Point2d(PointNd):
    """
    Model for 2D points
    """

    def __init__(self, x, y):
        super(Point2d, self).__init__()
        self._c.append(0.0)
        self._c.append(0.0)
        self._c[0] = x
        self._c[1] = y

    def __unicode__(self):
        return 'Point2d'

    @property
    def x(self):
        return self._c[0]

    @x.setter
    def x(self, x):
        self._c[0] = x

    @property
    def y(self):
        return self._c[1]

    @y.setter
    def y(self, y):
        self._c[1] = y

class Point3d(PointNd):
    """
    Model for 3D points
    """

    def __init__(self, x, y, z):
        super(Point3d, self).__init__()
        self._c.append(0.0)
        self._c.append(0.0)
        self._c.append(0.0)
        self._c[0] = x
        self._c[1] = y
        self._c[2] = z

    def __unicode__(self):
        return 'Point3d'

    @property
    def x(self):
        return self._c[0]

    @x.setter
    def x(self, x):
        self._c[0] = x

    @property
    def y(self):
        return self._c[1]

    @y.setter
    def y(self, y):
        self._c[1] = y

    @property
    def z(self):
        return self._c[2]

    @z.setter
    def z(self, z):
        self._c[2] = z


