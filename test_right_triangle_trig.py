import right_triangle_trig
import unittest

class TestRight_triangle_trig(unittest.TestCase):
    
    def test_get_inputs(self):
        self.assertEqual(right_triangle_trig.get_inputs(),)
    
    def test_adjside_oppside(self):
        self.assertEqual(right_triangle_trig.adjside_oppside(),)
    
    def test_adjside_hyp(self):
        self.assertEqual(right_triangle_trig.adjside_hyp(),)
    
    def test_adjside_adjangle(self):
        self.assertEqual(right_triangle_trig.adjside_adjangle(),)
    
    def test_adjside_oppangle(self):
        self.assertEqual(right_triangle_trig.adjside_oppangle(),)
    
    def test_oppside_hyp(self):
        self.assertEqual(right_triangle_trig.oppside_hyp(),)
    
    def test_oppside_adjangle(self):
        self.assertEqual(right_triangle_trig.oppside_adjangle(),)
    
    def test_oppside_oppangle(self):
        self.assertEqual(right_triangle_trig.oppside_oppangle(),)
    
    def test_hyp_adjangle(self):
        self.assertEqual(right_triangle_trig.hyp_adjangle(),)
    
    def test_hyp_opp_angle(self):
        self.assertEqual(right_triangle_trig.hyp_opp_angle(),)
    
    def test_adjangle_oppangle(self):
        self.assertEqual(right_triangle_trig.adjangle_oppangle(),)
    
    def test_run_checks(self):
        self.assertEqual(right_triangle_trig.run_checks(),)
    
    def test_draw_triangle(self):
        self.assertEqual(right_triangle_trig.draw_triangle(),)


if __name__ == '__main__':
    unittest.main()
