from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    damage: float
    stamina: float


ferocious_kick = Skill(name="Свирепый пинок", damage=12, stamina=6)
powerful_thrust = Skill(name="Мощный укол", damage=15, stamina=5)
