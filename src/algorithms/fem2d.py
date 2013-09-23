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

    def analyse(self,verbose=2):
        if (verbose>1):
            print "\n* Running FEM2D analysis for %s" % self.structure
            print "* Inputs"
            print self.structure.description
        
        nn=self.structure.nodeCount
        nm=self.structure.elementCount
        nl=self.structure.loadCount
        nn3=nn*3
        nm3=nn3-1
        
        # Build the initial force and displacement vector per node
        fx=[]
        fy=[]
        ft=[]
        ux=[]
        uy=[]
        ut=[]
        for i in range(nn):
            fx.append(0.0)
            fy.append(0.0)
            ft.append(0.0)
            ux.append(0.0)
            uy.append(0.0)
            ut.append(0.0)
            
        # Build the force and vector vector
        f=[]
        u=[]
        s=[[]]
        for i in range(nn3):
            f.append(0.0)
            u.append(0.0)
            s.append([])
            for j in range(nn3):
                s[i].append(0.0)
        
        # Build local stiffness matrix        
        t=[]
        sl=[[]]
        for i in range(6):
            t.append(0.0)
            sl.append([])
            for j in range(6):
                sl[i].append(0.0)
                
        # Set the loads on the force vector
        for load in self.structure.l:
            #nnr=load.node
        
        return True

