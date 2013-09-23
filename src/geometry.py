"""
engineering-open: open-source tooling for engineering
Copyright (C) 2013 Jeroen Coenders

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

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


