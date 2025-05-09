######################################################################
#--*- coding: utf-8 -*-
#  Character.py
######################################################################
# Based on course material from: OOP Python Programming ASE1 2024-2025
# Version of: Matthieu GRIMM--KEMPF
# Date: 2025-04-26
# Description: This module defines a base class for characters and two derived classes: Warrior and Magician.
######################################################################
# Verification: ruff check --fix -> all checks passed
# ########################################################################

import logging
import random

log = logging.getLogger(__name__)

class CharacterError(Exception):
    # Custom exception for character-related errors
    def __init__(self, message: str):
        # Constructor for the CharacterError class
        super().__init__(message)
        self.message = message

    def __str__(self):
        # String representation of the error
        return f"CharacterError: {self.message}"
    
    def __repr__(self):
        # Representation of the error
        return f"CharacterError: {self.message}"
    


class Character:
    """Base class for all characters"""
    def __init__(self, name: str, life: float = 100.0 , attack : float = 20.0, defense : float = 0.1):
        # Constructor for the Character class
        self._name = name
        self._life = life
        self._attack = attack
        self._defense = defense

    @property
    def name(self)-> str:
        # Get the name property
        return self._name
    
    @property
    def is_dead(self)-> bool:
        # Check if the character is dead
        return self._life <= 0
    
    def __str__(self):
        # String representation of the character
        return f"{self._name} <{self._life:.3f}>"
        
    
    def __repr__(self):
        # Representation of the character
        return f"{self._name} <{self._life:.3f}>"
    
    def take_damages(self, damage_value: float)-> bool:
        # Verify the damage value
        if self.is_dead:
            raise CharacterError(f"Character {self._name} is already dead")
        if damage_value < 0:
            raise CharacterError(f"Damage value must be positive: {damage_value}")
        # Calculate the damage taken by the character
        damage_taken = damage_value * (1 - self._defense)
        self._life -= damage_taken
        # Turn life into 0 if it is negative
        if self._life < 0:
            self._life = 0
        # Return "True" as a security check
        return True
    
    def attack(self, target: 'Character')-> bool:
        # Attack another character
        target.take_damages(self._attack)
        # Return "True" as a security check
        return True


class Weapon:
    def __init__(self, name: str, attack: float):
        # Constructor for the Weapon class (no default values because of the class method)
        self._name = name
        self.attack = attack
    
    @classmethod
    # Alternative constructor for a weapon called "Wood stick" and attack value of 1.0
    def wood_stick(cls)-> 'Weapon':
        # Create a wood stick weapon
        return cls("Wood stick", 1.0)

    @property
    def name(self)-> str:
        # Get the name property
        return self._name


class Warrior(Character):
    # standard life and defense values were directly changed to 150 and 0.12 to save computation time
    def __init__(self, name: str, weapon: Weapon = None, life: float = 150.0, attack: float = 20.0, defense: float = 0.12):
        # Constructor for the Warrior class
        super().__init__(name, life, attack, defense)
        # Initialize the weapon
        if weapon is None:
            self._weapon = Weapon.wood_stick()
        else:
            self._weapon = weapon
    
    @property
    def is_raging(self)-> bool:
        # Check if the warrior is raging
        # Raging is activated when the life is less than 20% of the maximum life (150)
        if self._life < (150*0.2):
            return True
        return False

    def attack(self, target: 'Character')-> bool:
        # Attack another character
        attack_value = self._attack + self._weapon.attack
        if self.is_raging:
            attack_value *= 1.2
        target.take_damages(attack_value)
        # Return "True" as a security check
        return True


class Magician(Character):
    # standard life and attack values were directly changed to 80 and 40 to save computation time
    def __init__(self, name: str, life: float = 80.0, attack: float = 40.0, defense: float = 0.1):
        # Constructor for the Magician class
        super().__init__(name, life, attack, defense)

    def activate_magic_shield(self)-> bool:
        # Activate the magic shield 1 chance out of 3
        if random.randint(0, 2) == 0:
            return True
        return False
    
    def take_damages(self, damage_value: float)-> bool:
        # Calculate the damage taken by the character
        if self.activate_magic_shield():
            # If the magic shield is activated, magician takes no damage
            return True
        else:
            return super().take_damages(damage_value)