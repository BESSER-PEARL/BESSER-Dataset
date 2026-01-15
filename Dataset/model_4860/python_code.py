from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class units_pc_pc_Pointcut:

    pass
class units_pc_pc_EObject:

    pass
class units_pc_pc_PointcutPointcut:

    pass
class units_pc_pc_Unit:

    pass
class units_pc_pc_UnitCarryingElement:

    def __init__(self, unitSpecification: str, units_pc_pc_UnitCarryingElement: "units_pc_pc_Unit" = None):
        self.unitSpecification = unitSpecification
        self.units_pc_pc_UnitCarryingElement = units_pc_pc_UnitCarryingElement
        
    @property
    def unitSpecification(self) -> str:
        return self.__unitSpecification

    @unitSpecification.setter
    def unitSpecification(self, unitSpecification: str):
        self.__unitSpecification = unitSpecification

    @property
    def units_pc_pc_UnitCarryingElement(self):
        return self.__units_pc_pc_UnitCarryingElement

    @units_pc_pc_UnitCarryingElement.setter
    def units_pc_pc_UnitCarryingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_pc_pc_UnitCarryingElement__units_pc_pc_UnitCarryingElement", None)
        self.__units_pc_pc_UnitCarryingElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_pc_pc_Unit"):
                opp_val = getattr(old_value, "units_pc_pc_Unit", None)
                if opp_val == self:
                    setattr(old_value, "units_pc_pc_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_pc_pc_Unit"):
                opp_val = getattr(value, "units_pc_pc_Unit", None)
                setattr(value, "units_pc_pc_Unit", self)

class Unit:

    pass
class units_pc_pc_UnitLiteral(Unit):

    pass
class units_pc_pc_UnitPower(Unit):

    def __init__(self, exponent: int, units_pc_pc_UnitPower: "units_pc_pc_Unit" = None):
        self.exponent = exponent
        self.units_pc_pc_UnitPower = units_pc_pc_UnitPower
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def units_pc_pc_UnitPower(self):
        return self.__units_pc_pc_UnitPower

    @units_pc_pc_UnitPower.setter
    def units_pc_pc_UnitPower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_pc_pc_UnitPower__units_pc_pc_UnitPower", None)
        self.__units_pc_pc_UnitPower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_pc_pc_Unit5"):
                opp_val = getattr(old_value, "units_pc_pc_Unit5", None)
                if opp_val == self:
                    setattr(old_value, "units_pc_pc_Unit5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_pc_pc_Unit5"):
                opp_val = getattr(value, "units_pc_pc_Unit5", None)
                setattr(value, "units_pc_pc_Unit5", self)

class units_pc_pc_UnitMultiplication(Unit):

    pass
class units_pc_pc_UnitRepository:

    pass
class units_pc_pc_BaseUnit:

    def __init__(self, name: str, units_pc_pc_BaseUnit: "units_pc_pc_UnitRepository" = None, units_pc_pc_BaseUnit7: "units_pc_pc_UnitLiteral" = None):
        self.name = name
        self.units_pc_pc_BaseUnit = units_pc_pc_BaseUnit
        self.units_pc_pc_BaseUnit7 = units_pc_pc_BaseUnit7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def units_pc_pc_BaseUnit7(self):
        return self.__units_pc_pc_BaseUnit7

    @units_pc_pc_BaseUnit7.setter
    def units_pc_pc_BaseUnit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_pc_pc_BaseUnit__units_pc_pc_BaseUnit7", None)
        self.__units_pc_pc_BaseUnit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_pc_pc_UnitLiteral"):
                opp_val = getattr(old_value, "units_pc_pc_UnitLiteral", None)
                if opp_val == self:
                    setattr(old_value, "units_pc_pc_UnitLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_pc_pc_UnitLiteral"):
                opp_val = getattr(value, "units_pc_pc_UnitLiteral", None)
                setattr(value, "units_pc_pc_UnitLiteral", self)

    @property
    def units_pc_pc_BaseUnit(self):
        return self.__units_pc_pc_BaseUnit

    @units_pc_pc_BaseUnit.setter
    def units_pc_pc_BaseUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_pc_pc_BaseUnit__units_pc_pc_BaseUnit", None)
        self.__units_pc_pc_BaseUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_pc_pc_UnitRepository"):
                opp_val = getattr(old_value, "units_pc_pc_UnitRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_pc_pc_UnitRepository"):
                opp_val = getattr(value, "units_pc_pc_UnitRepository", None)
                if opp_val is None:
                    setattr(value, "units_pc_pc_UnitRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
