import unittest

from src.colors import RgbColor, RgbColorUtils


class TestRgbColorUtils(unittest.TestCase):
    def test_interpolate_colors(self):
        color1 = RgbColor(255, 0, 0)
        color2 = RgbColor(0, 255, 0)
        steps = 5

        result = list(RgbColorUtils.interpolate_colors(color1, color2, steps))

        # Assuming the interpolation is correct, the result should contain 'steps' number of colors
        self.assertEqual(len(result), 255//steps)

        # Checking the first and last colors to ensure they match the provided input colors
        self.assertEqual(result[0], color1)
        self.assertEqual(result[-1], color2)

    def test_interpolate_colors_same_color(self):
        color1 = RgbColor(0, 0, 0)
        steps = 5

        result = list(RgbColorUtils.interpolate_colors(color1, color1, steps))

        # Assuming the interpolation is correct, the result should contain 'steps' number of colors
        self.assertEqual(len(result), 1)

        # Checking the first and last colors to ensure they match the provided input colors
        self.assertEqual(result[0], color1)


if __name__ == '__main__':
    unittest.main()
