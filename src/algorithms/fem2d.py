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

# Finite Element Method 2D algorithm

from models import CoreClass
import geometry

class Fem2d(CoreClass):
    """ 
    FEM2D algorithm
    """
    
    def __init__(self, structure):
        self.structure=structure

    def __unicode__(self):
        return "FEM2D algorithm"

    def analyse(self):
        print "Running FEM2D analysis for %s" % self.structure
        
        nn=self.structure.nodeCount
        nm=self.structure.elementCount
        return True

