from src.effects.effect_base import EffectBase
from src.effects.normal import FadeColor, SetColor
from src.effects.repeating import RainbowWave


class EffectFactory:
    @staticmethod
    def create_effect(data: dict) -> EffectBase:
        effect_name = data.get('Name')

        if effect_name == 'FadeColor':
            return FadeColor.from_dict(data)
        elif effect_name == 'SetColor':
            return SetColor.from_dict(data)
        elif effect_name == 'RainbowWave':
            return RainbowWave.from_dict(data)
        else:
            raise ValueError(f"Unknown effect name: {effect_name}")
