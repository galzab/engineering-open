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
        
    def print_system(self,nn3,f,s,u):
        #Show the system of equations
        print "nn3=%s" % str(nn3)
        error=1e-15
        for i in xrange(nn3):
            if (i % 3==0):
                st = "x["
            elif (i%3==1):
                st = "y["
            else:
                st = "t["
            if (abs(f[i])<error):
                st+="0="
            elif (abs(f[i])-1.0<error):
                st+="1="
            else:
                st+="*="
            for j in xrange(nn3):
            #    st+="%s-" % str(s[i][j])
                if (abs(s[i][j])<error):
                    st+="0"
                elif (abs(s[i][j])-1.0<error):
                    st+="1"
                else:
                    st+="*"
            if (abs(u[i])<error):
                st+=".0"
            elif (abs(u[i])-1.0<error):
                st+=".1"
            else:
                st+=".*"                    
            st += "]"
            print st
    
    def solve_system_gje(self,nn3,f,s,u):
        nm3=nn3-1
        for i in xrange(nn3):
            a = 1 / s[i][i]
            f[i] = a * f[i]
            for j in xrange(nn3):
                s[i][j] = a * s[i][j]
            ii = i + 1
            for j in xrange(ii,nn3):
                b = s[j][i]
                f[j]=f[j] - b * f[i]
                for k in xrange(i, nn3):
                    s[j][k] = s[j][k] - b * s[i][k]
        u[nn3-1] = f[nn3-1] / s[nn3-1][nn3-1]
        
        for i in xrange(nm3-1):
            m = nn3 - i -1
            u[m] = f[m]
            mm = m + 1
            for j in xrange(mm,nn3):
                u[m] = u[m] - s[m][j] *u[j]

    def analyse(self,verbose=2):
        if (verbose>1):
            print "\n* Running FEM2D analysis for %s" % self.structure
            print "* Inputs"
            print self.structure.description
            print "* Setting up system of equations"
        
        nn=self.structure.nodeCount
        nm=self.structure.elementCount
        nl=self.structure.loadCount
        nn3=self.structure.nodeCount*3
        nm3=self.structure.nodeCount*3 - 1
        
        # Initialise the initial force and displacement vector per node
        # (Future- This could also done directly on the main force and displacement vectors)
        ux=[]
        uy=[]
        ut=[]
        for i in xrange(self.structure.nodeCount):
            ux.append(0.0)
            uy.append(0.0)
            ut.append(0.0)
            
        # Initialise the global force and displacement vector and the global stiffness matrix
        f=[]
        u=[]
        s=[[]]
        for i in xrange(self.structure.nodeCount * 3):
            f.append(0.0)
            u.append(0.0)
            s.append([])
            for j in range(self.structure.nodeCount * 3):
                s[i].append(0.0)
        
        #Initialise local stiffness matrix
        #Future- This can be removed if we refactor the construction of the global stiffness
        #        matrix
        t=[]
        sl=[[]]
        for i in xrange(6):
            t.append(0.0)
            sl.append([])
            for j in xrange(6):
                sl[i].append(0.0)
                
        # Set the loads on the force vector
        for load in self.structure.l:
            nnr=self.structure.findNode(load.node)
            f[nnr*3] += load.X
            f[nnr*3+1] += load.Y
            f[nnr*3+2] += load.T
            
        # Construct the global stiffness matrix
        for member in self.structure.e:
            kk=self.structure.findNode(member.endnode)
            mm=self.structure.findNode(member.startnode)

            #Produce the local stiffness matrix
            #Future- This can probably be simplified
            b = member.beamsection.EA / member.length**3
            t[0] = member.dx
            t[1] = member.dy
            t[2] = 0.0
            t[3] = -member.dx
            t[4] = -member.dy
            t[5] = 0.0
            for k in xrange(6):
                for m in xrange(6):
                    sl[k][m]= b * t[k] * t[m]

            b = (12 * member.beamsection.EIzz) / (member.length**5)
            t[0] = member.dy
            t[1] = -member.dx
            t[2] = -member.length**2 / 2
            t[3] = -member.dy
            t[4] = member.dx
            t[5] = -member.length**2 / 2
            for k in xrange(6):
                for m in xrange(6):
                    sl[k][m]= sl[k][m] + b * t[k] * t[m]
            
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
            for k in xrange(6):
                kk1 = ns[k]
                for m in xrange(6):
                    mm1 = ns[m]
                    s[kk1][mm1]= s[kk1][mm1]+sl[k][m]
        
        #Calculation of predescribed displacements
        for i in xrange(nn):
            node = self.structure.n[i]
            if (node.cx):
                #print "node %s has x restraint" % str(i)
                ux[i]=0.0
                ii = 3 * i
                for j in xrange(nn3):
                    s[ii][j] = 0.0
                s[ii][ii] = 1.0
                f[ii] = ux[i]
            if (node.cy):
                #print "node %s has y restraint" % str(i)
                uy[i]=0.0
                ii = 3 * i + 1
                for j in xrange(nn3):
                    s[ii][j] = 0.0
                s[ii][ii] = 1.0
                f[ii] = uy[i]
            if (node.cr):
                #print "node %s has t restraint" % str(i)
                ut[i]=0.0
                ii = 3 * i + 2
                for j in xrange(nn3):
                    s[ii][j] = 0.0
                s[ii][ii] = 1.0
                f[ii] = ut[i]
        
        #Solution of system of equations using Gauss-Jordan elimination
        if (verbose>1):
            print "* Solving system of equations"
        self.solve_system_gje(nn3,f,s,u)
     
        if (verbose>1):
            print "* Post-processing"
            
        # Post-processing displacements
        for i in xrange(nn):
            ux[i]=u[i*3]
            uy[i]=u[i*3+1]
            ut[i]=u[i*3+2]
            
        #Post-processing internal forces
        fm=[]
        t1=[]
        t2=[]
        v=[]
        for i in xrange(nm):
            member=self.structure.e[i]
            k = self.structure.findNode(member.endnode)
            m = self.structure.findNode(member.startnode)
            b = member.beamsection.EA / member.length**2
            c = member.dx * (ux[k] - ux[m]) + member.dy * (uy[k] - uy[m])
            fm.append(b * c)
            c = member.dx * (uy[k] - uy[m]) - member.dy * (ux[k] - ux[m])
            b = c / member.length**2
            c = 2 * member.beamsection.EIzz / member.length
            t1.append(c * (2 * ut[m] + ut[k] -3 * b))
            t2.append(-c * (2 * ut[k] + ut[m] - 3 * b))
            v.append ((t2[i]-t1[i])/ member.length)
        
        #Post-processing: calculation of stresses
        sigma1=[]
        sigma2=[]
        for i in xrange(nm):
            member=self.structure.e[i]
            sigma1.append((t1[i] / member.beamsection.Wy)+(fm[i] / member.beamsection.A))
            sigma2.append((t2[i] / member.beamsection.Wy)+(fm[i] / member.beamsection.A))
        
        #Output
        if (verbose>1):
            #Future- This could use some better formatting
            print "* Outputs"
            print "Nodal results"
            for i in xrange(nn):
                print "%s: %+.4f %+.4f %+.4f %+.4f %+.4f %+.4f" % (str(i), f[i*3], f[i*3+1] ,f[i*3+2], ux[i], uy[i], ut[i])
            print "Member results"
            for i in xrange(nm):
                print "%s: %+.2f %+.2f %+.2f %+.2f %+.2f %+.2f" % (str(i), fm[i], t1[i], t2[i], v[i], sigma1[i], sigma2[i])
            
        return True