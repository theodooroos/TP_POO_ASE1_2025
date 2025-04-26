import logging

log = logging.getLogger(__name__)

import random


class CharacterError(Exception):
    """Base class for Character error"""

class Character:
    """Base class for all characters"""
    def __init__(self, name: str, life: float = 100.0 , attack : float = 20.0, defense : float = 0.1):
        # Constructor for the Character class
        self._name = name
        self._life = life
        self._attack = attack
        self._defense = defense

    @property
    def name(self):
        # Get the name property
        return self._name
    
    @property
    def is_dead(self):
        # Check if the character is dead
        return self._life <= 0
    
    def __str__(self):
        # String representation of the character
        return f"{self._name} <{self._life:.3f}>"
        
    
    def __repr__(self):
        # Representation of the character
        return f"{self._name} <{self._life:.3f}>"
    
    def take_damages(self, damage_value: float):
        # Calulate the damage taken by the character
        damage_taken = damage_value * (1 - self._defense)
        self._life -= damage_taken
        return True
    
    def attack(self, target: 'Character'):
        # Attack another character
        target.take_damages(self._attack)
        return True


class Weapon:
    def __init__(self, name: str, attack: float):
        # Constructor for the Weapon class (no default values because of the class method)
        self._name = name
        self.attack = attack
    
    @classmethod
    # Alternative constructor for a weapon called "Wood stick" and attack value of 1.0
    def wood_stick(cls):
        # Create a wood stick weapon
        return cls("Wood stick", 1.0)

    @property
    def name(self):
        # Get the name property
        return self._name


class Warrior(Character):
    def __init__(self, name: str, weapon: Weapon = None, life: float = 150.0, attack: float = 20.0, defense: float = 0.12):
        # Constructor for the Warrior class
        super().__init__(name, life, attack, defense)
        # Initialize the weapon
        if weapon is None:
            self._weapon = Weapon.wood_stick()
        else:
            self._weapon = weapon
    
    @property
    def is_raging(self):
        # Check if the warrior is raging
        if self._life < (150*0.2):
            return True
        return False

    def attack(self, target: 'Character'):
        # Attack another character
        attack_value = self._attack + self._weapon.attack
        if self.is_raging:
            attack_value *= 1.2
        target.take_damages(attack_value)
        return True


class Magician(Character):
    def __init__(self, name: str, life: float = 80.0, attack: float = 40.0, defense: float = 0.1):
        # Constructor for the Magician class
        super().__init__(name, life, attack, defense)

    def activate_magic_shield(self):
        # Activate the magic shield 1 chance out of 3
        if random.randint(0, 2) == 0:
            return True
        return False
    
    def take_damages(self, damage_value: float):
        # Calculate the damage taken by the character
        if self.activate_magic_shield():
            return True
        else:
            return super().take_damages(damage_value)