import sys
sys.path.append("..")

import unittest
import geometry

class PointXdTests(unittest.TestCase):
    """Tests for PointXd"""

    def test_unicode(self):
        point=geometry.PointXd()
        self.assertEqual(str(point), 'PointXd')

class Point2dTests(unittest.TestCase):
    """Tests for Point2d"""

    def test_unicode(self):
        point=geometry.Point2d(0.0,0.0)
        self.assertEqual(str(point), 'Point2d')

class Point3dTests(unittest.TestCase):
    """Tests for Point3d"""

    def test_unicode(self):
        point=geometry.Point3d(0.0,0.0,0.0)
        self.assertEqual(str(point), 'Point3d')

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
