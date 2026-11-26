import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as trinagle_area, perimeter as triangle_perimeter

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.5398163397, places=5)
        self.assertEqual(circle_area(0), 0)
    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 6.2831853071, places=5)
        self.assertEqual(circle_perimeter(0), 0)
    def test_square_area(self):
            self.assertEqual(square_area(5), 120)
            self.assertEqual(square_area(0), 0)
            self.assertEqual(square_area(1), 1)
    def test_square_perimeter(self):
            self.assertEqual(square_perimeter(5), 20)
            self.assertEqual(square_perimeter(0), 0)
            self.assertEqual(square_perimeter(1), 4)
    def test_rectangle_area(self):
            self.assertEqual(rectangle_area(4, 12), 48)
            self.assertEqual(rectangle_area(10, 0), 0)
            self.assertEqual(rectangle_area(1, 1), 1)
    def test_rectangle_perimeter(self):
            self.assertEqual(rectangle_perimeter(4, 12), 32)
            self.assertEqual(rectangle_perimeter(10, 0), 20)
            self.assertEqual(rectangle_perimeter(1, 1), 4)
    def test_triangle_area(self):
            self.assertEqual(trinagle_area(3, 4, 5), 6)
            self.assertAlmostEqual(trinagle_area(2, 2, 2), 1.7320508, places=5)
    def test_triangle_perimeter(self):
            self.assertEqual(triangle_perimeter(3, 4, 5), 12)
            self.assertEqual(triangle_perimeter(2, 2, 2), 6)

if __name__ == '__main__':
      unittest.main()