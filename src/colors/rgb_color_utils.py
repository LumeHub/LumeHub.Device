from . import RgbColor


class RgbColorUtils:
    @staticmethod
    def interpolate_colors(color1: RgbColor, color2: RgbColor, step_size: int) -> list[RgbColor]:
        """
        Interpolates between two colors
        :param color1: the first color
        :param color2: the second color
        :param step_size: the step size between the colors
        :return: a list of colors
        """
        step_count = max(int(color1.distance(color2) / step_size), 1)
        if step_count == 1:
            yield color2
            return
        for i in range(step_count):
            r = ((step_count - i - 1) * color1.red + i * color2.red) / (step_count - 1)
            g = ((step_count - i - 1) * color1.green + i * color2.green) / (step_count - 1)
            b = ((step_count - i - 1) * color1.blue + i * color2.blue) / (step_count - 1)
            yield RgbColor(r, g, b)
