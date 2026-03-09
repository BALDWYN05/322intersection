"""
;Dylan Baldwin
;CSCI 322 Spring 2025
;Programming Assignment #class17
;I acknowledge that I have worked on this assignment independently, except where
;explicitly noted and referenced. Any collaboration or use of external resources
;has been properly cited. I am fully aware of the consequences of academic
;dishonesty and agree to abide by the university's academic integrity policy. I
;understand the importance the consequences of plagiarism.
"""

"""
Source: https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/

Usage: structure for intersection section

"""
def get_orientation(p:tuple[float], q:tuple[float], r:tuple[float])->str:
    result = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if result > 0:
        return "Clockwise"
    elif result < 0:
        return "Counter Clockwise"
    else:
        return "Linear"
    
def on_segment(p:tuple[float], q:tuple[float], r:tuple[float]) -> float:
    result = ((r[0] - p[0]) * (q[1] - p[1])) - ((r[0] - p[0]) * (q[0] - p[0]))

    if result == 0:
        return True
    else:
        return False
    

def do_segments_intersect(seg1, seg2):
    p1, p2 = seg1
    p3, p4 = seg2

    o1 = get_orientation(p1, p2, p3)
    o2 = get_orientation(p1, p2, p4)
    o3 = get_orientation(p3, p4, p1)
    o4 = get_orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4: 
        return True
    if o1 == "Linear" and on_segment(p1, p3, p2):
      return True
    if o2 == "Linear" and on_segment(p1, p4, p2):
      return True
    if o3 == "Linear" and on_segment(p3, p1, p4):
      return True
    if o4 == "Linear" and on_segment(p3, p2, p4):
        return True

    return False



if __name__ == "__main__":
    p1 = (1.0, 1.0)
    p2 = (4.0, 4.0)
    p3 = (2.0, 4.0)
    p4 = (4.0, 2.0)
    seg1 = (p1, p2)
    seg2 = (p3, p4)
    print(do_segments_intersect(seg1, seg2)) # Output: True