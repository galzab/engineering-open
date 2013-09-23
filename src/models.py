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

import math
from geometry import Point2d
from geometry import CoreClass

class StructuralBaseClass(CoreClass):
    """
    Model for top level structural entity
    """

    def __init__(self, name):
        self.name = name

class StructuralElement(StructuralBaseClass):
    """
    Model for structural elements
    """
    def __init__(self, name):
        super(StructuralElement, self).__init__(name)

    def __unicode__(self):
        return 'Structural Element %s' % self.name

class Material(StructuralBaseClass):
    """
    Model for materials
    """

    def __init__(self, name, E, G):
        super(Material, self).__init__(name)
        self.E = E
        self.G = G

    def __unicode__(self):
        return 'Material %s' % self.name

    @property
    def shortname(self):
        return self.name

class BeamSection2d(StructuralBaseClass):
    """
    Model for beam sections
    """

    def __init__(self, name, material):
        super(BeamSection2d, self).__init__(name)
        self.material=material
        self.A = 0.0
        self.Sy = 0.0
        self.Sz = 0.0
        self.Iyy = 10.0
        self.Izz = 0.0
        self.Iyz = 0.0
        self.Izy = 0.0

    def __unicode__(self):
        return 'Beam section %s' % self.name

    @property
    def shortname(self):
        return self.name

    @property
    def EIyy(self):
        return (self.material.E*self.Iyy)

class Node2d(Point2d,StructuralElement):
    """
    Model for 2D nodes
    """
    def __init__(self, name, x, y):
        super(Node2d, self).__init__(x, y)
        super(StructuralElement, self).__init__(name)

    def __unicode__(self):
        return 'Node2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s)" % (str(self),self.x,self.y)

class MassedNode2d(Node2d):
    """
    Model for 2D nodes with a mass
    """
    def __init__(self, name, x, y, mass, cx=False, cy=False):
        super(MassedNode2d, self).__init__(name,x, y)
        self.mass=mass
        self.cx=cx
        self.cy=cy

    def __unicode__(self):
        return 'MassedNode2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s) mass %s constraints (%s,%s)" % (str(self),self.x,self.y,self.mass,self.cx,self.cy)

class Element2d(StructuralElement):
    """
    Model for 2D elements
    """
    def __init__(self, name, startnode, endnode):
        super(Element2d, self).__init__(name)
        self.startnode = startnode
        self.endnode = endnode

    def __unicode__(self):
        return 'Element2d %s' % self.name

    @property
    def dx(self):
        return self.endnode.x-self.startnode.x
 
    @property
    def dy(self):
        return self.endnode.y-self.startnode.y
 
    @property
    def length(self):
        return math.sqrt(self.dx**2+self.dy**2)

class Beam2d(Element2d):
    """
    Model for 2D beams
    """
    def __init__(self, name, startnode, endnode, beamsection):
        super(Beam2d, self).__init__(name, startnode, endnode)
        self.beamsection = beamsection

    def __unicode__(self):
        return 'Beam2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s) %s" % (str(self), str(self.startnode), str(self.endnode), str(self.beamsection))

class Spring2d(Element2d):
    """
    Model for 2D springs
    """
    def __init__(self, name, startnode, endnode, stiffness, original_length):
        super(Spring2d, self).__init__(name, startnode, endnode)
        self.stiffness=stiffness
        self.original_length=original_length

    def __unicode__(self):
        return 'Spring2d %s' % self.name

    @property
    def description(self):
        return "%s (%s,%s) %s" % (str(self), str(self.startnode), str(self.endnode), str(self.stiffness))
        
class Load2d(StructuralBaseClass):
    """
    Model for a two-dimensional node load
    """
    
    def __init__(self, name, node, lx, ly):
        super(Load2d, self).__init__(name)
        self.node = node
        self.lx = lx
        self.ly = ly
        
    def __unicode__(self):
        return 'Load2d %s (%s,%s) on node %s' % (self.name, self.lx, self.ly, self.node.name)
        
    @property
    def description(self):
        return str(self)
        
    @property
    def X(self):
        return self.lx
    
    @property
    def Y(self):
        return self.ly

class Structure(StructuralBaseClass):
    """
    Model for the structure
    """

    def __init__(self, name):
        super(Structure, self).__init__(name)
        self.n = []
        self.e = []
        self.l = []

    def __unicode__(self):
        return 'Structure %s' % self.name

    @property
    def description(self):
        s=str(self)+"\n"
        for node in self.n:
            s+=node.description+"\n"
        for element in self.e:
            s+=element.description+"\n"
        for load in self.l:
            s+=load.description+"\n"
        return s

    def addNode(self, node):
        """Adds a node to the structure"""
        self.n.append(node)

    def addElement(self, element):
        """Adds an element to the structure"""
        self.e.append(element)
    
    def addLoad(self, load):
        """Adds a load to the structure"""
        self.l.append(load)

    @property
    def nodeCount(self):
        return len(self.n)

    @property
    def elementCount(self):
        return len(self.e)
    
    @property
    def loadCount(self):
        return len(self.l)
