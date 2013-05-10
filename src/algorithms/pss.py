# Particle Spring System algorithm
import math

def pssResetForce(structure):
    """Resets the residual forces on a structures"""
	    
    for node in structure.n:
       	node.rx=0.0
       	node.ry=0.0

def pssCalculateElementForces(structure):
    """Calculates the forces on each element in a structure"""

    for element in structure.e:
       	element.nx=element.stiffness*(element.dx/element.original_length)
        element.ny=element.stiffness*(element.dy/element.original_length)

def pssCalculateAccelerations(structure):
    for node in structure.n:
	node.ax=node.rx/node.mass
	node.ay=node.ry/node.mass
	if node.cx: node.ax=0.0
	if node.cy: node.ay=0.0
 
def start_pss(structure,weight,tolerance,maximum_steps):
    """Starts the particle spring system"""
    for node in structure.n:
        node.lx=0.0
        node.ly=-weight
        node.rx=0.0
        node.ry=0.0
        node.ax=0.0
        node.ay=0.0
        node.vx=0.0
        node.vy=0.0

    n=0
    error=(10*tolerance)
    timestep=0.01
    damping=0.9
    while (error>tolerance)&(n<maximum_steps):
        pssResetForce(structure)
        pssCalculateElementForces(structure)
        for node in structure.n:
            node.rx=node.lx
            node.ry=node.ly

        for element in structure.e:
       	    element.startnode.rx+=element.nx
            element.startnode.ry+=element.ny
            element.endnode.rx-=element.nx
            element.endnode.ry-=element.ny

        pssCalculateAccelerations(structure)

        for node in structure.n:
       	    node.vx=node.ax*timestep+node.vx*damping
            node.vy=node.ay*timestep+node.vy*damping

        for node in structure.n:
       	    node.x+=node.vx*timestep
            node.y+=node.vy*timestep
      
        error=0.0 
        for node in structure.n:
            error+=abs(node.vx)+abs(node.vy)

        n=n+1

    if (error>tolerance):
        return False 
    else:
        return True
