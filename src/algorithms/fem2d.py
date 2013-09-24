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
        
        # Initialise the initial force and displacement vector per node
        # (Future- This could also done directly on the main force and displacement vectors)
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
            
        # Initialise the global force and displacement vector and the global stiffness matrix
        f=[]
        u=[]
        s=[[]]
        for i in range(nn3):
            f.append(0.0)
            u.append(0.0)
            s.append([])
            for j in range(nn3):
                s[i].append(0.0)
        
        # Initialise local stiffness matrix        
        t=[]
        sl=[[]]
        for i in range(6):
            t.append(0.0)
            sl.append([])
            for j in range(6):
                sl[i].append(0.0)
                
        # Set the loads on the force vector
        for load in self.structure.l:
            nnr=self.structure.findNode(load.node)
            fx[nnr]+=load.X
            fy[nnr]+=load.Y
            ft[nnr]+=load.T
            
        # Construct the stiffness matrix
        for i in range(nm):
            member=self.structure.e[i]
            kk=self.structure.findNode(member.endnode)
            mm=self.structure.findNode(member.startnode)
            dx=member.dx
            dz=member.dy

            #Produce the local stiffness matrix
            #Future- This can probably be simplified
            b = member.beamsection.EA / member.length**3
            t[0] = dx
            t[1] = dz
            t[2] = 0.0
            t[3] = -dx
            t[4] = -dz
            t[5] = 0.0
            for k in range(6):
                for m in range(6):
                    sl[k][m]=b * t[k] * t[m]

            b = (12 * member.beamsection.EIzz) / (member.length**5)
            t[0] = dz
            t[1] = -dx
            t[2] = -member.length**2 / 2
            t[3] = -dz
            t[4] = dx
            t[5] = -member.length**2 / 2
            for k in range(6):
                for m in range(6):
                    sl[k][m]=s[k][m]+b*t[k]*t[m]
            
            b = member.beamsection.EIzz / member.length;
            sl[2][2] = sl[2][2] + b
            sl[2][5] = sl[2][5] - b
            sl[5][2] = sl[5][2] - b
            sl[5][5] = sl[5][5] + b
            
            #Add the local stiffness matrix to the global stiffness matrix
            ns=[]
            ns.append(3 * mm)
            ns.append(3 * mm + 1)
            ns.append(3 * mm + 2)
            ns.append(3 * kk)
            ns.append(3 * kk + 1)
            ns.append(3 * kk + 2)
            for k in range(6):
                kk1 = ns[k]
                for m in range(6):
                    mm1 = ns[m]
                    s[kk1][mm1]= s[kk1][mm1]+sl[k][m]
            
        #Construction of the global stiffness vector
        for i in range(nn):
            kx = 3 * i
            ky = 3 * i + 1
            kt = 3 * i + 2
            f[kx] = fx[i]
            f[ky] = fy[i]
            f[kt] = ft[i]
                        
            
        return True

