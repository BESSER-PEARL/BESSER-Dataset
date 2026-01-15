from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Unit:

    pass
class units_UnitPower(Unit):

    def __init__(self, exponent: int, units_UnitPower: "units_Unit" = None):
        self.exponent = exponent
        self.units_UnitPower = units_UnitPower
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def units_UnitPower(self):
        return self.__units_UnitPower

    @units_UnitPower.setter
    def units_UnitPower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_UnitPower__units_UnitPower", None)
        self.__units_UnitPower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_Unit5"):
                opp_val = getattr(old_value, "units_Unit5", None)
                if opp_val == self:
                    setattr(old_value, "units_Unit5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_Unit5"):
                opp_val = getattr(value, "units_Unit5", None)
                setattr(value, "units_Unit5", self)

class units_UnitLiteral(Unit):

    pass
class units_UnitMultiplication(Unit):

    pass
class units_UnitRepository:

    pass
class units_BaseUnit:

    def __init__(self, name: str, units_BaseUnit: "units_UnitRepository" = None, units_BaseUnit7: "units_UnitLiteral" = None):
        self.name = name
        self.units_BaseUnit = units_BaseUnit
        self.units_BaseUnit7 = units_BaseUnit7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def units_BaseUnit7(self):
        return self.__units_BaseUnit7

    @units_BaseUnit7.setter
    def units_BaseUnit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_BaseUnit__units_BaseUnit7", None)
        self.__units_BaseUnit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_UnitLiteral"):
                opp_val = getattr(old_value, "units_UnitLiteral", None)
                if opp_val == self:
                    setattr(old_value, "units_UnitLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_UnitLiteral"):
                opp_val = getattr(value, "units_UnitLiteral", None)
                setattr(value, "units_UnitLiteral", self)

    @property
    def units_BaseUnit(self):
        return self.__units_BaseUnit

    @units_BaseUnit.setter
    def units_BaseUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_BaseUnit__units_BaseUnit", None)
        self.__units_BaseUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_UnitRepository"):
                opp_val = getattr(old_value, "units_UnitRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_UnitRepository"):
                opp_val = getattr(value, "units_UnitRepository", None)
                if opp_val is None:
                    setattr(value, "units_UnitRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class units_Unit(ABC):

    pass
class units_UnitCarryingElement(ABC):

    def __init__(self, unitSpecification: str, units_UnitCarryingElement: "units_Unit" = None):
        self.unitSpecification = unitSpecification
        self.units_UnitCarryingElement = units_UnitCarryingElement
        
    @property
    def unitSpecification(self) -> str:
        return self.__unitSpecification

    @unitSpecification.setter
    def unitSpecification(self, unitSpecification: str):
        self.__unitSpecification = unitSpecification

    @property
    def units_UnitCarryingElement(self):
        return self.__units_UnitCarryingElement

    @units_UnitCarryingElement.setter
    def units_UnitCarryingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_UnitCarryingElement__units_UnitCarryingElement", None)
        self.__units_UnitCarryingElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_Unit"):
                opp_val = getattr(old_value, "units_Unit", None)
                if opp_val == self:
                    setattr(old_value, "units_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_Unit"):
                opp_val = getattr(value, "units_Unit", None)
                setattr(value, "units_Unit", self)
