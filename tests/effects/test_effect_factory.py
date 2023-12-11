import unittest

from src.colors import RgbColor
from src.effects import EffectFactory
from src.effects.normal import FadeColor, SetColor
from src.effects.repeating import RainbowWave


class TestEffectFactory(unittest.TestCase):
    def test_create_effect_fade_color(self):
        data = {'Name': 'FadeColor', 'Color': {"Red": 255, "Green": 0, "Blue": 0}}
        effect = EffectFactory.create_effect(data)
        self.assertIsInstance(effect, FadeColor)
        self.assertEqual(effect.color, RgbColor(255, 0, 0))

    def test_create_effect_set_color(self):
        data = {'Name': 'SetColor', 'Color': {"Red": 0, "Green": 255, "Blue": 0}}
        effect = EffectFactory.create_effect(data)
        self.assertIsInstance(effect, SetColor)
        self.assertEqual(effect.color, RgbColor(0, 255, 0))

    def test_create_effect_rainbow_wave(self):
        data = {'Name': 'RainbowWave', 'Multiplier': 2}
        effect = EffectFactory.create_effect(data)
        self.assertIsInstance(effect, RainbowWave)
        self.assertEqual(effect.multiplier, 2)

    def test_create_effect_unknown_effect(self):
        data = {'Name': 'UnknownEffect'}
        with self.assertRaises(ValueError):
            EffectFactory.create_effect(data)


if __name__ == '__main__':
    unittest.main()
