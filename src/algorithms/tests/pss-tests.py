import sys
sys.path.append("..")
sys.path.append("../..")

import unittest
import pss
import models
import math

from models import Material
from models import BeamSection2d
from models import Structure
from models import MassedNode2d
from models import Spring2d
from pss import pssResetForce
from pss import pssCalculateElementForces
from pss import pssCalculateAccelerations
from pss import start_pss

class ParticleSpringSystemAlgorithmTests(unittest.TestCase):
    """Tests for Particle Spring System algorithm"""

    def setUp(self):
        self.stiffness = 10.0
        self.original_length = 0.9
        self.spacing = 1.0
        self.mass = 1.0
        
        #set up the structure
        self.structure=Structure("001")
        for i in range(10):
            self.structure.addNode(MassedNode2d("%s" % str(i+1),(self.spacing*i),0.0,self.mass))
        for i in range(9):
            self.structure.addElement(Spring2d("%s" % str(i+1), self.structure.n[i], self.structure.n[i+1], self.stiffness, self.original_length))
        self.structure.n[0].cx=True
        self.structure.n[0].cy=True
        self.structure.n[9].cx=True
        self.structure.n[9].cy=True

    def test_nodeCount(self):
        self.assertEqual(self.structure.nodeCount,10)

    def test_springCount(self):
        self.assertEqual(self.structure.elementCount,9)

    def test_pssResetForce(self):
        pssResetForce(self.structure)
        for node in self.structure.n:
            self.assertEqual(node.rx, 0.0)
            self.assertEqual(node.ry, 0.0)

    def test_pssCalculateElementForces_horizontal(self):
        pssCalculateElementForces(self.structure)
        for element in self.structure.e:
            self.assertEqual(element.nx,(self.spacing/self.original_length)*self.stiffness)
            self.assertEqual(element.ny,0.0)

    def test_pssCalculateElementForces_vertical(self):
        self.displacement=self.spacing*2.0
        self.structure.n[1].y=self.displacement

        self.assertEqual(self.structure.n[1].x, self.spacing)
        self.assertEqual(self.structure.n[1].y, self.displacement)

        self.assertEqual(self.structure.e[0].dx, self.spacing)
        self.assertEqual(self.structure.e[0].dy, self.displacement)

        length=self.structure.e[0].length
        self.assertEqual(length,math.sqrt((self.displacement**2)+(self.spacing**2)))
        
        pssCalculateElementForces(self.structure)

        force=math.sqrt(self.structure.e[0].nx**2+self.structure.e[0].ny**2)
        self.assertEqual(force, (length/self.original_length)*self.stiffness)

    def test_pssCalculateAccelerations(self):
        xforce = 1.0
        yforce = 2.0
        for node in self.structure.n:
            node.rx = xforce
            node.ry = yforce
        pssCalculateAccelerations(self.structure)
        for node in self.structure.n:
            ax=xforce/self.mass
            ay=yforce/self.mass
            if node.cx: ax=0.0
            if node.cy: ay=0.0
            self.assertEqual(node.ax, ax)
            self.assertEqual(node.ay, ay)
 
    def test_particleSpringSystemAlgorithm(self):
        self.assertEqual(start_pss(self.structure,1.0,0.01,10000),True)           

"""Set up the test suite"""
current_module = sys.modules[__name__]
suite = unittest.TestLoader().loadTestsFromModule(current_module)
unittest.TextTestRunner(verbosity=2).run(suite)
