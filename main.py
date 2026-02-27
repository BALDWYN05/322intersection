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

def point_orientation_testing(p1:tuple[int], p2:tuple[int], p3:tuple[int])->str:
    pass

def add_positive_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be positive")
    return a + b