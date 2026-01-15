from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class units_av_av_PerJoinPointScope:

    pass
class units_av_av_GlobalScope:

    pass
class units_av_av_Advice:

    pass
class units_av_av_PerJoinPointScopePerJoinPointScope:

    pass
class units_av_av_GlobalScopeGlobalScope:

    pass
class units_av_av_EObject:

    pass
class units_av_av_AdviceAdvice:

    pass
class Unit:

    pass
class units_av_av_UnitLiteral(Unit):

    pass
class units_av_av_UnitMultiplication(Unit):

    pass
class units_av_av_UnitRepository:

    pass
class units_av_av_BaseUnit:

    def __init__(self, name: str, units_av_av_BaseUnit: "units_av_av_UnitRepository" = None, units_av_av_BaseUnit7: "units_av_av_UnitLiteral" = None):
        self.name = name
        self.units_av_av_BaseUnit = units_av_av_BaseUnit
        self.units_av_av_BaseUnit7 = units_av_av_BaseUnit7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def units_av_av_BaseUnit7(self):
        return self.__units_av_av_BaseUnit7

    @units_av_av_BaseUnit7.setter
    def units_av_av_BaseUnit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_av_av_BaseUnit__units_av_av_BaseUnit7", None)
        self.__units_av_av_BaseUnit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_av_av_UnitLiteral"):
                opp_val = getattr(old_value, "units_av_av_UnitLiteral", None)
                if opp_val == self:
                    setattr(old_value, "units_av_av_UnitLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_av_av_UnitLiteral"):
                opp_val = getattr(value, "units_av_av_UnitLiteral", None)
                setattr(value, "units_av_av_UnitLiteral", self)

    @property
    def units_av_av_BaseUnit(self):
        return self.__units_av_av_BaseUnit

    @units_av_av_BaseUnit.setter
    def units_av_av_BaseUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_av_av_BaseUnit__units_av_av_BaseUnit", None)
        self.__units_av_av_BaseUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_av_av_UnitRepository"):
                opp_val = getattr(old_value, "units_av_av_UnitRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_av_av_UnitRepository"):
                opp_val = getattr(value, "units_av_av_UnitRepository", None)
                if opp_val is None:
                    setattr(value, "units_av_av_UnitRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class units_av_av_Unit:

    pass
class units_av_av_UnitCarryingElement:

    def __init__(self, unitSpecification: str, units_av_av_UnitCarryingElement: "units_av_av_Unit" = None):
        self.unitSpecification = unitSpecification
        self.units_av_av_UnitCarryingElement = units_av_av_UnitCarryingElement
        
    @property
    def unitSpecification(self) -> str:
        return self.__unitSpecification

    @unitSpecification.setter
    def unitSpecification(self, unitSpecification: str):
        self.__unitSpecification = unitSpecification

    @property
    def units_av_av_UnitCarryingElement(self):
        return self.__units_av_av_UnitCarryingElement

    @units_av_av_UnitCarryingElement.setter
    def units_av_av_UnitCarryingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_av_av_UnitCarryingElement__units_av_av_UnitCarryingElement", None)
        self.__units_av_av_UnitCarryingElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_av_av_Unit"):
                opp_val = getattr(old_value, "units_av_av_Unit", None)
                if opp_val == self:
                    setattr(old_value, "units_av_av_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_av_av_Unit"):
                opp_val = getattr(value, "units_av_av_Unit", None)
                setattr(value, "units_av_av_Unit", self)

class units_av_av_UnitPower(Unit):

    def __init__(self, exponent: int, units_av_av_UnitPower: "units_av_av_Unit" = None):
        self.exponent = exponent
        self.units_av_av_UnitPower = units_av_av_UnitPower
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def units_av_av_UnitPower(self):
        return self.__units_av_av_UnitPower

    @units_av_av_UnitPower.setter
    def units_av_av_UnitPower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_av_av_UnitPower__units_av_av_UnitPower", None)
        self.__units_av_av_UnitPower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_av_av_Unit5"):
                opp_val = getattr(old_value, "units_av_av_Unit5", None)
                if opp_val == self:
                    setattr(old_value, "units_av_av_Unit5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_av_av_Unit5"):
                opp_val = getattr(value, "units_av_av_Unit5", None)
                setattr(value, "units_av_av_Unit5", self)
