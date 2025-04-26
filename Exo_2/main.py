######################################################################
#--*- coding: utf-8 -*-
#  main.py
######################################################################
# Based on course material from: OOP Python Programming ASE1 2024-2025
# Version of: Matthieu GRIMM--KEMPF
# Date: 2025-04-26
# Description: This module contains the main function to run the fight simulator.
######################################################################
# Verification: ruff check --fix -> all checks passed
######################################################################

import logging
import sys

from character import Magician, Warrior, Weapon
from simulator import FightSimulator

log = logging.getLogger(__name__)


def main():
    simulator = FightSimulator(
        [
            Warrior("Thor", Weapon("Hammer", 3.0)),
            Magician("Gandalf"),
            Magician("Merlin"),
            Warrior("Gimli", Weapon("Axe", 4.0)),
        ]
    )

    simulator.run()


def test():
    from character import Character
    # Test the basic character class : EXO 2 1-4
    basic_fighter = Character("Soldier")
    print(basic_fighter) # will print character name and remaining amount of life.

if __name__ == "__main__":

    # Switch level to logging.DEBUG to activate debug logs
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    #test()
    main()
