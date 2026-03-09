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

import unittest
from main import do_segments_intersect

class TestSegmentIntersection(unittest.TestCase):
    def test_default(self):
        p1 = (1.0, 1.0)
        p2 = (4.0, 4.0)
        p3 = (2.0, 4.0)
        p4 = (4.0, 2.0)
        seg1 = (p1, p2)
        seg2 = (p3, p4)
        self.assertEqual(do_segments_intersect(seg1, seg2),True)

    def test_do_not_intersect(self):
        p1 = (0.0, 0.0)
        p2 = (0.0, 1.0)
        p3 = (1.0, 0.0)
        p4 = (1.0, 1.0)
        seg1 = (p1, p2)
        seg2 = (p3, p4)
        self.assertEqual(do_segments_intersect(seg1, seg2),False)
    
    def test_overlaping(self):
        p1 = (0.0, 0.0)
        p2 = (0.0, 2.0)
        p3 = (0.0, 1.0)
        p4 = (0.0, 3.0)
        seg1 = (p1, p2)
        seg2 = (p3, p4)
        self.assertEqual(do_segments_intersect(seg1,seg2), True)   

if __name__ == "__main__":
    unittest.main()