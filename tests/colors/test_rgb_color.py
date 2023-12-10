import unittest
from src.colors import RgbColor


class TestRgbColor(unittest.TestCase):
    def setUp(self):
        # Create instances for testing
        self.color1 = RgbColor(100, 150, 200)
        self.color2 = RgbColor(50, 75, 100)

    def test_init(self):
        # Test the constructor
        self.assertEqual(self.color1.red, 100)
        self.assertEqual(self.color1.green, 150)
        self.assertEqual(self.color1.blue, 200)

        # Test that values are clamped to the valid range
        self.assertEqual(self.color2.red, 50)
        self.assertEqual(self.color2.green, 75)
        self.assertEqual(self.color2.blue, 100)

    def test_to_tuple(self):
        # Test the to_tuple method
        self.assertEqual(self.color1.to_tuple(), (100, 150, 200))

    def test_from_tuple(self):
        # Test the from_tuple method
        color_tuple = (50, 75, 100)
        color = RgbColor.from_tuple(color_tuple)
        self.assertEqual(color.red, 50)
        self.assertEqual(color.green, 75)
        self.assertEqual(color.blue, 100)

    def test_str(self):
        # Test the __str__ method
        self.assertEqual(str(self.color1), "Red: 100, Green: 150, Blue: 200")

    def test_hash(self):
        # Test the __hash__ method
        self.assertEqual(hash(self.color1), hash((100, 150, 200)))

    def test_eq(self):
        # Test the __eq__ method
        self.assertEqual(self.color1, RgbColor(100, 150, 200))
        self.assertNotEqual(self.color1, self.color2)

    def test_add(self):
        # Test the __add__ method
        result = self.color1 + self.color2
        self.assertEqual(result.red, 150)
        self.assertEqual(result.green, 225)
        self.assertEqual(result.blue, 255)

    def test_sub(self):
        # Test the __sub__ method
        result = self.color1 - self.color2
        self.assertEqual(result.red, 50)
        self.assertEqual(result.green, 75)
        self.assertEqual(result.blue, 100)

    def test_mul(self):
        # Test the __mul__ method
        result = self.color1 * 2
        self.assertEqual(result.red, 200)
        self.assertEqual(result.green, 255)
        self.assertEqual(result.blue, 255)

    def test_truediv(self):
        # Test the __truediv__ method
        result = self.color1 / 2
        self.assertEqual(result.red, 50)
        self.assertEqual(result.green, 75)
        self.assertEqual(result.blue, 100)

    def test_distance(self):
        # Test the distance method
        distance = self.color1.distance(self.color2)
        self.assertEqual(distance, 100)

    def test_is_color_similar(self):
        # Test the is_color_similar method
        similar_color = RgbColor(105, 155, 205)
        self.assertTrue(self.color1.is_color_similar(similar_color, 10))
        self.assertFalse(self.color1.is_color_similar(self.color2, 10))

    def test_get_random_color(self):
        # Test the get_random_color static method
        random_color = RgbColor.get_random_color()
        self.assertTrue(0 <= random_color.red <= 255)
        self.assertTrue(0 <= random_color.green <= 255)
        self.assertTrue(0 <= random_color.blue <= 255)


if __name__ == '__main__':
    unittest.main()
