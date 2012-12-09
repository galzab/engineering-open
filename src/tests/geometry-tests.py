import sys
print sys.path
sys.path.append("..")

import unittest
import geometry

class VectorNdTests(unittest.TestCase):
    """Tests for VectorNd"""

    def test_unicode(self):
        vector=geometry.VectorNd()
        self.assertEqual(str(vector), 'VectorNd')

class PointNdTests(unittest.TestCase):
    """Tests for PointNd"""

    def test_unicode(self):
        point=geometry.PointNd()
        self.assertEqual(str(point), 'PointNd')

class Point2dTests(unittest.TestCase):
    """Tests for Point2d"""

    def test_unicode(self):
        point1=geometry.Point2d(0.0,0.0)
        self.assertEqual(str(point1), 'Point2d')

    def test_coordinates(self):
        point2=geometry.Point2d(1.0,2.0)
        self.assertEqual(point2.x, 1.0)
        self.assertEqual(point2.y, 2.0)

    def test_coordinate_getter(self):
        point3=geometry.Point2d(1.0,2.0)
        x=point3.x
        y=point3.y
        self.assertEqual(x, 1.0)
        self.assertEqual(y, 2.0)

    def test_coordinate_setter(self):
        point4=geometry.Point2d(1.0,2.0)
        point4.x=3.0
        point4.y=4.0
        self.assertEqual(point4.x, 3.0)
        self.assertEqual(point4.y, 4.0)

class Point3dTests(unittest.TestCase):
    """Tests for Point3d"""

    def test_unicode(self):
        point=geometry.Point3d(0.0,0.0,0.0)
        self.assertEqual(str(point), 'Point3d')

    def test_coordinates(self):
        point=geometry.Point3d(1.0,2.0,3.0)
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)
        self.assertEqual(point.z, 3.0)

    def test_coordinate_setter(self):
        point=geometry.Point3d(1.0,2.0,3.0)
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)
        self.assertEqual(point.z, 3.0)
        point.x=4.0
        point.y=5.0
        point.z=6.0
        self.assertEqual(point.x, 4.0)
        self.assertEqual(point.y, 5.0)
        self.assertEqual(point.z, 6.0)

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
