import sys
sys.path.append("..")

def simply_supported_beam_calculation(beam,q):
    """Produces results for a simply supported beam"""
    M=(1/8)*q*(beam.length**2)
    V=(1/2)*q*(beam.length)
    d=(5/384)*q*((beam.length**4)/beam.beamsection.EIyy)
    return (M,V,d)
