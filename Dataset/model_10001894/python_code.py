from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Dash2:

    def __init__(self, execute__: str):
        self.execute__ = execute__
        
        pass
    @property
    def execute__(self):
        return self.__execute__
    @execute__.setter
    def execute__(self, execute__: str):
        self.__execute__ = execute__



class Dash:

    def __init__(self, execute__: str):
        self.execute__ = execute__
        
        pass
    @property
    def execute__(self):
        return self.__execute__
    @execute__.setter
    def execute__(self, execute__: str):
        self.__execute__ = execute__



class Spell:

    pass


class Weapon:

    pass


class Action:

    def __init__(self, execute__: str):
        self.execute__ = execute__
        
        pass
    @property
    def execute__(self):
        return self.__execute__
    @execute__.setter
    def execute__(self, execute__: str):
        self.__execute__ = execute__



class CastSpell:

    def __init__(self, execute__: str, spell: Spell):
        self.execute__ = execute__
        self.spell = spell
        
        pass
    @property
    def spell(self):
        return self.__spell
    @spell.setter
    def spell(self, spell: Spell):
        self.__spell = spell

    @property
    def execute__(self):
        return self.__execute__
    @execute__.setter
    def execute__(self, execute__: str):
        self.__execute__ = execute__



class WeaponAttack:

    def __init__(self, execute__: str, weapon: Weapon):
        self.execute__ = execute__
        self.weapon = weapon
        
        pass
    @property
    def weapon(self):
        return self.__weapon
    @weapon.setter
    def weapon(self, weapon: Weapon):
        self.__weapon = weapon

    @property
    def execute__(self):
        return self.__execute__
    @execute__.setter
    def execute__(self, execute__: str):
        self.__execute__ = execute__

