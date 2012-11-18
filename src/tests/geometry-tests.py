import sys
sys.path.append("..")

import unittest
import geometry

class PointNdTests(unittest.TestCase):
    """Tests for PointXd"""

    def test_unicode(self):
        point=geometry.PointNd()
        self.assertEqual(str(point), 'PointNd')

class Point2dTests(unittest.TestCase):
    """Tests for Point2d"""

    def test_unicode(self):
        point=geometry.Point2d(0.0,0.0)
        self.assertEqual(str(point), 'Point2d')

    def test_coordinates(self):
        point=geometry.Point2d(1.0,2.0)
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)

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

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
