from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SysML_ValueTypes_QUDV_QUDV_UnitFactor:

    def __init__(self, name: str, SysML_ValueTypes_QUDV_QUDV_UnitFactor: "Rational" = None, SysML_ValueTypes_QUDV_QUDV_UnitFactor91: "Unit" = None):
        self.name = name
        self.SysML_ValueTypes_QUDV_QUDV_UnitFactor = SysML_ValueTypes_QUDV_QUDV_UnitFactor
        self.SysML_ValueTypes_QUDV_QUDV_UnitFactor91 = SysML_ValueTypes_QUDV_QUDV_UnitFactor91
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SysML_ValueTypes_QUDV_QUDV_UnitFactor91(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_UnitFactor91

    @SysML_ValueTypes_QUDV_QUDV_UnitFactor91.setter
    def SysML_ValueTypes_QUDV_QUDV_UnitFactor91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_UnitFactor__SysML_ValueTypes_QUDV_QUDV_UnitFactor91", None)
        self.__SysML_ValueTypes_QUDV_QUDV_UnitFactor91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit92"):
                opp_val = getattr(old_value, "Unit92", None)
                if opp_val == self:
                    setattr(old_value, "Unit92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit92"):
                opp_val = getattr(value, "Unit92", None)
                setattr(value, "Unit92", self)

    @property
    def SysML_ValueTypes_QUDV_QUDV_UnitFactor(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_UnitFactor

    @SysML_ValueTypes_QUDV_QUDV_UnitFactor.setter
    def SysML_ValueTypes_QUDV_QUDV_UnitFactor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_UnitFactor__SysML_ValueTypes_QUDV_QUDV_UnitFactor", None)
        self.__SysML_ValueTypes_QUDV_QUDV_UnitFactor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rational89"):
                opp_val = getattr(old_value, "Rational89", None)
                if opp_val == self:
                    setattr(old_value, "Rational89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rational89"):
                opp_val = getattr(value, "Rational89", None)
                setattr(value, "Rational89", self)

class SysML_ValueTypes_QUDV_QUDV_SystemOfUnits:

    def __init__(self, symbol: str, name: str, definitionURI: str, description: str, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits: set["Unit"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72: set["Prefix"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75: "SystemOfQuantities" = None, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78: set["Unit"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81: set["SystemOfUnits"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69: set["SystemOfUnits"] = None):
        self.symbol = symbol
        self.name = name
        self.definitionURI = definitionURI
        self.description = description
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits if SysML_ValueTypes_QUDV_QUDV_SystemOfUnits is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72 = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72 if SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75 = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78 = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78 if SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81 = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81 if SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69 = SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69 if SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69 is not None else set()
        
    @property
    def definitionURI(self) -> str:
        return self.__definitionURI

    @definitionURI.setter
    def definitionURI(self, definitionURI: str):
        self.__definitionURI = definitionURI

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemOfUnits70"):
                    opp_val = getattr(item, "SystemOfUnits70", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemOfUnits70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemOfUnits70"):
                    opp_val = getattr(item, "SystemOfUnits70", None)
                    
                    setattr(item, "SystemOfUnits70", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemOfQuantities76"):
                opp_val = getattr(old_value, "SystemOfQuantities76", None)
                if opp_val == self:
                    setattr(old_value, "SystemOfQuantities76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemOfQuantities76"):
                opp_val = getattr(value, "SystemOfQuantities76", None)
                setattr(value, "SystemOfQuantities76", self)

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Unit67"):
                    opp_val = getattr(item, "Unit67", None)
                    
                    if opp_val == self:
                        setattr(item, "Unit67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Unit67"):
                    opp_val = getattr(item, "Unit67", None)
                    
                    setattr(item, "Unit67", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Unit79"):
                    opp_val = getattr(item, "Unit79", None)
                    
                    if opp_val == self:
                        setattr(item, "Unit79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Unit79"):
                    opp_val = getattr(item, "Unit79", None)
                    
                    setattr(item, "Unit79", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemOfUnits82"):
                    opp_val = getattr(item, "SystemOfUnits82", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemOfUnits82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemOfUnits82"):
                    opp_val = getattr(item, "SystemOfUnits82", None)
                    
                    setattr(item, "SystemOfUnits82", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72

    @SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfUnits__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Prefix73"):
                    opp_val = getattr(item, "Prefix73", None)
                    
                    if opp_val == self:
                        setattr(item, "Prefix73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Prefix73"):
                    opp_val = getattr(item, "Prefix73", None)
                    
                    setattr(item, "Prefix73", self)
                    

    def allMeasurementUnitsDefinedForSomeQuantityKind(self) -> bool:
        # TODO: Implement allMeasurementUnitsDefinedForSomeQuantityKind method
        pass

    def allUnits(self) -> str:
        # TODO: Implement allUnits method
        pass

    def allBaseUnits(self) -> str:
        # TODO: Implement allBaseUnits method
        pass

    def getUnit(self, name: str) -> str:
        # TODO: Implement getUnit method
        pass

    def getAdoptedQuantityKindForAdoptedBaseUnitOfMeasurementUnit(self, u: str) -> str:
        # TODO: Implement getAdoptedQuantityKindForAdoptedBaseUnitOfMeasurementUnit method
        pass

    def allAccessibleUnits(self) -> str:
        # TODO: Implement allAccessibleUnits method
        pass

    def allIncludedSystemOfUnits(self) -> str:
        # TODO: Implement allIncludedSystemOfUnits method
        pass

    def getAdoptedBaseUnitForMeasurementUnit(self, u: str) -> str:
        # TODO: Implement getAdoptedBaseUnitForMeasurementUnit method
        pass

    def allBaseQuantityKinds(self) -> str:
        # TODO: Implement allBaseQuantityKinds method
        pass

    def getKindOfQuantitiesForMeasurementUnit(self, u: str) -> str:
        # TODO: Implement getKindOfQuantitiesForMeasurementUnit method
        pass

    def isCoherent(self) -> bool:
        # TODO: Implement isCoherent method
        pass

    def getEffectiveSystemOfQuantities(self) -> str:
        # TODO: Implement getEffectiveSystemOfQuantities method
        pass

    def allPrefixes(self) -> str:
        # TODO: Implement allPrefixes method
        pass

    def allAccessibleSystemOfUnits(self) -> str:
        # TODO: Implement allAccessibleSystemOfUnits method
        pass

    def isCoherent(self, du: str) -> bool:
        # TODO: Implement isCoherent method
        pass

class SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities:

    def __init__(self, description: str, symbol: str, name: str, definitionURI: str, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58: set["SystemOfQuantities"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61: set["QuantityKind"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64: set["SystemOfQuantities"] = None, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities: set["QuantityKind"] = None):
        self.description = description
        self.symbol = symbol
        self.name = name
        self.definitionURI = definitionURI
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58 = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58 if SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61 = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61 if SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64 = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64 if SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities = SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities if SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities is not None else set()
        
    @property
    def definitionURI(self) -> str:
        return self.__definitionURI

    @definitionURI.setter
    def definitionURI(self, definitionURI: str):
        self.__definitionURI = definitionURI

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61

    @SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKind62"):
                    opp_val = getattr(item, "QuantityKind62", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKind62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKind62"):
                    opp_val = getattr(item, "QuantityKind62", None)
                    
                    setattr(item, "QuantityKind62", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64

    @SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemOfQuantities65"):
                    opp_val = getattr(item, "SystemOfQuantities65", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemOfQuantities65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemOfQuantities65"):
                    opp_val = getattr(item, "SystemOfQuantities65", None)
                    
                    setattr(item, "SystemOfQuantities65", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities

    @SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKind56"):
                    opp_val = getattr(item, "QuantityKind56", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKind56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKind56"):
                    opp_val = getattr(item, "QuantityKind56", None)
                    
                    setattr(item, "QuantityKind56", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58

    @SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58.setter
    def SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58", None)
        self.__SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemOfQuantities59"):
                    opp_val = getattr(item, "SystemOfQuantities59", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemOfQuantities59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemOfQuantities59"):
                    opp_val = getattr(item, "SystemOfQuantities59", None)
                    
                    setattr(item, "SystemOfQuantities59", self)
                    

    def allBaseQuantityKinds(self) -> str:
        # TODO: Implement allBaseQuantityKinds method
        pass

    def getDimension(self, qk: str) -> str:
        # TODO: Implement getDimension method
        pass

    def allAccessibleSystemOfQuantities(self) -> str:
        # TODO: Implement allAccessibleSystemOfQuantities method
        pass

    def allAccessibleQuantityKinds(self) -> str:
        # TODO: Implement allAccessibleQuantityKinds method
        pass

    def allIncludedSystemOfQuantities(self) -> str:
        # TODO: Implement allIncludedSystemOfQuantities method
        pass

    def allQuantityKinds(self) -> str:
        # TODO: Implement allQuantityKinds method
        pass

class SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor:

    def __init__(self, name: str, SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor: "Rational" = None, SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53: "QuantityKind" = None):
        self.name = name
        self.SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor = SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor
        self.SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53 = SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53

    @SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53.setter
    def SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53", None)
        self.__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuantityKind54"):
                opp_val = getattr(old_value, "QuantityKind54", None)
                if opp_val == self:
                    setattr(old_value, "QuantityKind54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuantityKind54"):
                opp_val = getattr(value, "QuantityKind54", None)
                setattr(value, "QuantityKind54", self)

    @property
    def SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor

    @SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor.setter
    def SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor", None)
        self.__SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rational51"):
                opp_val = getattr(old_value, "Rational51", None)
                if opp_val == self:
                    setattr(old_value, "Rational51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rational51"):
                opp_val = getattr(value, "Rational51", None)
                setattr(value, "Rational51", self)

class Rational:

    pass
class SysML_ValueTypes_QUDV_QUDV_Prefix:

    def __init__(self, symbol: str, name: str, SysML_ValueTypes_QUDV_QUDV_Prefix: "Rational" = None):
        self.symbol = symbol
        self.name = name
        self.SysML_ValueTypes_QUDV_QUDV_Prefix = SysML_ValueTypes_QUDV_QUDV_Prefix
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SysML_ValueTypes_QUDV_QUDV_Prefix(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_Prefix

    @SysML_ValueTypes_QUDV_QUDV_Prefix.setter
    def SysML_ValueTypes_QUDV_QUDV_Prefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_Prefix__SysML_ValueTypes_QUDV_QUDV_Prefix", None)
        self.__SysML_ValueTypes_QUDV_QUDV_Prefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rational"):
                opp_val = getattr(old_value, "Rational", None)
                if opp_val == self:
                    setattr(old_value, "Rational", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rational"):
                opp_val = getattr(value, "Rational", None)
                setattr(value, "Rational", self)

class SysML_ValueTypes_QUDV_QUDV_Dimension:

    def __init__(self, name: str, SysML_ValueTypes_QUDV_QUDV_Dimension: set["QuantityKindFactor"] = None):
        self.name = name
        self.SysML_ValueTypes_QUDV_QUDV_Dimension = SysML_ValueTypes_QUDV_QUDV_Dimension if SysML_ValueTypes_QUDV_QUDV_Dimension is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SysML_ValueTypes_QUDV_QUDV_Dimension(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_Dimension

    @SysML_ValueTypes_QUDV_QUDV_Dimension.setter
    def SysML_ValueTypes_QUDV_QUDV_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_Dimension__SysML_ValueTypes_QUDV_QUDV_Dimension", None)
        self.__SysML_ValueTypes_QUDV_QUDV_Dimension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKindFactor39"):
                    opp_val = getattr(item, "QuantityKindFactor39", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKindFactor39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKindFactor39"):
                    opp_val = getattr(item, "QuantityKindFactor39", None)
                    
                    setattr(item, "QuantityKindFactor39", self)
                    

class ConversionBasedUnit:

    pass
class SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit(ConversionBasedUnit):

    def __init__(self, expression: str, expressionLanguageURI: str):
        self.expression = expression
        self.expressionLanguageURI = expressionLanguageURI
        
    @property
    def expressionLanguageURI(self) -> str:
        return self.__expressionLanguageURI

    @expressionLanguageURI.setter
    def expressionLanguageURI(self, expressionLanguageURI: str):
        self.__expressionLanguageURI = expressionLanguageURI

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit(ConversionBasedUnit):

    pass
class SysML_ValueTypes_QUDV_QUDV_PrefixedUnit(ConversionBasedUnit):

    pass
class SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit(ConversionBasedUnit):

    pass
class SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit:

    def __init__(self, definitionURI: str, description: str, symbol: str, name: str, SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit: set["QuantityKind"] = None):
        self.definitionURI = definitionURI
        self.description = description
        self.symbol = symbol
        self.name = name
        self.SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit = SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit if SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def definitionURI(self) -> str:
        return self.__definitionURI

    @definitionURI.setter
    def definitionURI(self, definitionURI: str):
        self.__definitionURI = definitionURI

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(self):
        return self.__SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit

    @SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit.setter
    def SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit__SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit", None)
        self.__SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKind26"):
                    opp_val = getattr(item, "QuantityKind26", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKind26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKind26"):
                    opp_val = getattr(item, "QuantityKind26", None)
                    
                    setattr(item, "QuantityKind26", self)
                    

class SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind:

    def __init__(self, definitionURI: str, description: str, symbol: str, name: str):
        self.definitionURI = definitionURI
        self.description = description
        self.symbol = symbol
        self.name = name
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def definitionURI(self) -> str:
        return self.__definitionURI

    @definitionURI.setter
    def definitionURI(self, definitionURI: str):
        self.__definitionURI = definitionURI

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Integer:

    pass
class Real:

    pass
class Dimension:

    pass
class Unit:

    pass
class SysML_ValueTypes_QUDV_QUDV_DerivedUnit(Unit):

    def __init__(self, SysML_ValueTypes_QUDV_QUDV_DerivedUnit: set["UnitFactor"] = None, Unit67: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", Unit33: "SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", Unit79: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit87: "SysML_ValueTypes_QUDV_QUDV_Unit", Unit92: "SysML_ValueTypes_QUDV_QUDV_UnitFactor", Unit84: "SysML_ValueTypes_QUDV_QUDV_Unit"):
        self.SysML_ValueTypes_QUDV_QUDV_DerivedUnit = SysML_ValueTypes_QUDV_QUDV_DerivedUnit if SysML_ValueTypes_QUDV_QUDV_DerivedUnit is not None else set()
        
    @property
    def SysML_ValueTypes_QUDV_QUDV_DerivedUnit(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_DerivedUnit

    @SysML_ValueTypes_QUDV_QUDV_DerivedUnit.setter
    def SysML_ValueTypes_QUDV_QUDV_DerivedUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_DerivedUnit__SysML_ValueTypes_QUDV_QUDV_DerivedUnit", None)
        self.__SysML_ValueTypes_QUDV_QUDV_DerivedUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnitFactor37"):
                    opp_val = getattr(item, "UnitFactor37", None)
                    
                    if opp_val == self:
                        setattr(item, "UnitFactor37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnitFactor37"):
                    opp_val = getattr(item, "UnitFactor37", None)
                    
                    setattr(item, "UnitFactor37", self)
                    

    def dependsOnUnits(self) -> str:
        # TODO: Implement dependsOnUnits method
        pass

class SysML_ValueTypes_QUDV_QUDV_Unit(Unit):

    def __init__(self, isUnitCountOfEntities: bool, isUnitForQuantityOfDimensionOne: bool, SysML_ValueTypes_QUDV_QUDV_Unit86: set["Unit"] = None, SysML_ValueTypes_QUDV_QUDV_Unit: set["Unit"] = None, Unit67: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", Unit33: "SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", Unit79: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit87: "SysML_ValueTypes_QUDV_QUDV_Unit", Unit92: "SysML_ValueTypes_QUDV_QUDV_UnitFactor", Unit84: "SysML_ValueTypes_QUDV_QUDV_Unit"):
        self.isUnitCountOfEntities = isUnitCountOfEntities
        self.isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne
        self.SysML_ValueTypes_QUDV_QUDV_Unit86 = SysML_ValueTypes_QUDV_QUDV_Unit86 if SysML_ValueTypes_QUDV_QUDV_Unit86 is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_Unit = SysML_ValueTypes_QUDV_QUDV_Unit if SysML_ValueTypes_QUDV_QUDV_Unit is not None else set()
        
    @property
    def isUnitCountOfEntities(self) -> bool:
        return self.__isUnitCountOfEntities

    @isUnitCountOfEntities.setter
    def isUnitCountOfEntities(self, isUnitCountOfEntities: bool):
        self.__isUnitCountOfEntities = isUnitCountOfEntities

    @property
    def isUnitForQuantityOfDimensionOne(self) -> bool:
        return self.__isUnitForQuantityOfDimensionOne

    @isUnitForQuantityOfDimensionOne.setter
    def isUnitForQuantityOfDimensionOne(self, isUnitForQuantityOfDimensionOne: bool):
        self.__isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne

    @property
    def SysML_ValueTypes_QUDV_QUDV_Unit(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_Unit

    @SysML_ValueTypes_QUDV_QUDV_Unit.setter
    def SysML_ValueTypes_QUDV_QUDV_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_Unit__SysML_ValueTypes_QUDV_QUDV_Unit", None)
        self.__SysML_ValueTypes_QUDV_QUDV_Unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Unit84"):
                    opp_val = getattr(item, "Unit84", None)
                    
                    if opp_val == self:
                        setattr(item, "Unit84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Unit84"):
                    opp_val = getattr(item, "Unit84", None)
                    
                    setattr(item, "Unit84", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_Unit86(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_Unit86

    @SysML_ValueTypes_QUDV_QUDV_Unit86.setter
    def SysML_ValueTypes_QUDV_QUDV_Unit86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_Unit__SysML_ValueTypes_QUDV_QUDV_Unit86", None)
        self.__SysML_ValueTypes_QUDV_QUDV_Unit86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Unit87"):
                    opp_val = getattr(item, "Unit87", None)
                    
                    if opp_val == self:
                        setattr(item, "Unit87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Unit87"):
                    opp_val = getattr(item, "Unit87", None)
                    
                    setattr(item, "Unit87", self)
                    

    def dependsOnUnits(self) -> str:
        # TODO: Implement dependsOnUnits method
        pass

class SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit(Unit):

    def __init__(self, isInvertible: bool, SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit: "Unit" = None, Unit67: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", Unit33: "SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", Unit79: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit87: "SysML_ValueTypes_QUDV_QUDV_Unit", Unit92: "SysML_ValueTypes_QUDV_QUDV_UnitFactor", Unit84: "SysML_ValueTypes_QUDV_QUDV_Unit"):
        self.isInvertible = isInvertible
        self.SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit = SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit
        
    @property
    def isInvertible(self) -> bool:
        return self.__isInvertible

    @isInvertible.setter
    def isInvertible(self, isInvertible: bool):
        self.__isInvertible = isInvertible

    @property
    def SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit

    @SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit.setter
    def SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit__SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", None)
        self.__SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit33"):
                opp_val = getattr(old_value, "Unit33", None)
                if opp_val == self:
                    setattr(old_value, "Unit33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit33"):
                opp_val = getattr(value, "Unit33", None)
                setattr(value, "Unit33", self)

    def dependsOnUnits(self) -> str:
        # TODO: Implement dependsOnUnits method
        pass

class SysML_ValueTypes_QUDV_QUDV_SimpleUnit(Unit):

    def __init__(self, Unit67: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", Unit33: "SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", Unit79: "SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", Unit87: "SysML_ValueTypes_QUDV_QUDV_Unit", Unit92: "SysML_ValueTypes_QUDV_QUDV_UnitFactor", Unit84: "SysML_ValueTypes_QUDV_QUDV_Unit"):
        
    def dependsOnUnits(self) -> str:
        # TODO: Implement dependsOnUnits method
        pass

class QuantityKind:

    pass
class SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind(QuantityKind):

    def __init__(self, SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind: set["QuantityKindFactor"] = None, QuantityKind56: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", QuantityKind26: "SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit", QuantityKind46: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind49: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind62: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind54: "SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor"):
        self.SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind = SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind if SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind is not None else set()
        
    @property
    def SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind

    @SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind.setter
    def SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind__SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind", None)
        self.__SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKindFactor35"):
                    opp_val = getattr(item, "QuantityKindFactor35", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKindFactor35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKindFactor35"):
                    opp_val = getattr(item, "QuantityKindFactor35", None)
                    
                    setattr(item, "QuantityKindFactor35", self)
                    

    def dependsOnQuantityKinds(self) -> str:
        # TODO: Implement dependsOnQuantityKinds method
        pass

class SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind(QuantityKind):

    def __init__(self, QuantityKind56: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", QuantityKind26: "SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit", QuantityKind46: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind49: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind62: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind54: "SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor"):
        
    def dependsOnQuantityKinds(self) -> str:
        # TODO: Implement dependsOnQuantityKinds method
        pass

class SysML_ValueTypes_QUDV_QUDV_QuantityKind(QuantityKind):

    def __init__(self, isNumberOfEntities: bool, isQuantityOfDimensionOne: bool, SysML_ValueTypes_QUDV_QUDV_QuantityKind: set["QuantityKind"] = None, SysML_ValueTypes_QUDV_QUDV_QuantityKind48: set["QuantityKind"] = None, QuantityKind56: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", QuantityKind26: "SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit", QuantityKind46: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind49: "SysML_ValueTypes_QUDV_QUDV_QuantityKind", QuantityKind62: "SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", QuantityKind54: "SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor"):
        self.isNumberOfEntities = isNumberOfEntities
        self.isQuantityOfDimensionOne = isQuantityOfDimensionOne
        self.SysML_ValueTypes_QUDV_QUDV_QuantityKind = SysML_ValueTypes_QUDV_QUDV_QuantityKind if SysML_ValueTypes_QUDV_QUDV_QuantityKind is not None else set()
        self.SysML_ValueTypes_QUDV_QUDV_QuantityKind48 = SysML_ValueTypes_QUDV_QUDV_QuantityKind48 if SysML_ValueTypes_QUDV_QUDV_QuantityKind48 is not None else set()
        
    @property
    def isQuantityOfDimensionOne(self) -> bool:
        return self.__isQuantityOfDimensionOne

    @isQuantityOfDimensionOne.setter
    def isQuantityOfDimensionOne(self, isQuantityOfDimensionOne: bool):
        self.__isQuantityOfDimensionOne = isQuantityOfDimensionOne

    @property
    def isNumberOfEntities(self) -> bool:
        return self.__isNumberOfEntities

    @isNumberOfEntities.setter
    def isNumberOfEntities(self, isNumberOfEntities: bool):
        self.__isNumberOfEntities = isNumberOfEntities

    @property
    def SysML_ValueTypes_QUDV_QUDV_QuantityKind(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_QuantityKind

    @SysML_ValueTypes_QUDV_QUDV_QuantityKind.setter
    def SysML_ValueTypes_QUDV_QUDV_QuantityKind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_QuantityKind__SysML_ValueTypes_QUDV_QUDV_QuantityKind", None)
        self.__SysML_ValueTypes_QUDV_QUDV_QuantityKind = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKind46"):
                    opp_val = getattr(item, "QuantityKind46", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKind46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKind46"):
                    opp_val = getattr(item, "QuantityKind46", None)
                    
                    setattr(item, "QuantityKind46", self)
                    

    @property
    def SysML_ValueTypes_QUDV_QUDV_QuantityKind48(self):
        return self.__SysML_ValueTypes_QUDV_QUDV_QuantityKind48

    @SysML_ValueTypes_QUDV_QUDV_QuantityKind48.setter
    def SysML_ValueTypes_QUDV_QUDV_QuantityKind48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_QUDV_QuantityKind__SysML_ValueTypes_QUDV_QUDV_QuantityKind48", None)
        self.__SysML_ValueTypes_QUDV_QUDV_QuantityKind48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QuantityKind49"):
                    opp_val = getattr(item, "QuantityKind49", None)
                    
                    if opp_val == self:
                        setattr(item, "QuantityKind49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QuantityKind49"):
                    opp_val = getattr(item, "QuantityKind49", None)
                    
                    setattr(item, "QuantityKind49", self)
                    

    def dependsOnQuantityKinds(self) -> str:
        # TODO: Implement dependsOnQuantityKinds method
        pass

class Number:

    pass
class SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational(Number):

    def __init__(self, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational: "Integer" = None, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23: "Integer" = None, Number28: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number41: "SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit", Number31: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER"):
        self.SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational
        self.SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23 = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23
        
    @property
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23(self):
        return self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23

    @SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23.setter
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23", None)
        self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Integer24"):
                opp_val = getattr(old_value, "Integer24", None)
                if opp_val == self:
                    setattr(old_value, "Integer24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Integer24"):
                opp_val = getattr(value, "Integer24", None)
                setattr(value, "Integer24", self)

    @property
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational(self):
        return self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational

    @SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational.setter
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational", None)
        self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Integer"):
                opp_val = getattr(old_value, "Integer", None)
                if opp_val == self:
                    setattr(old_value, "Integer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Integer"):
                opp_val = getattr(value, "Integer", None)
                setattr(value, "Integer", self)

    def plus(self, r: str) -> str:
        # TODO: Implement plus method
        pass

    def times(self, r: str) -> str:
        # TODO: Implement times method
        pass

    def equivalent(self, r: str) -> bool:
        # TODO: Implement equivalent method
        pass

class SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real(Number):

    def __init__(self, Number28: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number41: "SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit", Number31: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER"):
        
    def plus(self, x: str) -> str:
        # TODO: Implement plus method
        pass

    def lessThan(self, x: str) -> bool:
        # TODO: Implement lessThan method
        pass

    def lessOrEqual(self, x: str) -> bool:
        # TODO: Implement lessOrEqual method
        pass

    def equals(self, x: str) -> bool:
        # TODO: Implement equals method
        pass

    def times(self, x: str) -> str:
        # TODO: Implement times method
        pass

class SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer(Number):

    def __init__(self, Number28: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number41: "SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit", Number31: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER"):
        
    def plus(self, x: str) -> str:
        # TODO: Implement plus method
        pass

    def times(self, x: str) -> str:
        # TODO: Implement times method
        pass

    def lessThan(self, x: str) -> bool:
        # TODO: Implement lessThan method
        pass

    def lessOrEqual(self, x: str) -> bool:
        # TODO: Implement lessOrEqual method
        pass

    def equals(self, x: str) -> bool:
        # TODO: Implement equals method
        pass

class SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER:

    pass
class SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex(Number):

    def __init__(self, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19: "Real" = None, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex: "Real" = None, Number28: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number41: "SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit", Number31: "SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", Number: "SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER"):
        self.SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19 = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19
        self.SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex = SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex
        
    @property
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex(self):
        return self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex

    @SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex.setter
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex", None)
        self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Real"):
                opp_val = getattr(old_value, "Real", None)
                if opp_val == self:
                    setattr(old_value, "Real", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Real"):
                opp_val = getattr(value, "Real", None)
                setattr(value, "Real", self)

    @property
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19(self):
        return self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19

    @SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19.setter
    def SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19", None)
        self.__SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Real20"):
                opp_val = getattr(old_value, "Real20", None)
                if opp_val == self:
                    setattr(old_value, "Real20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Real20"):
                opp_val = getattr(value, "Real20", None)
                setattr(value, "Real20", self)

    def lessOrEqual(self, x: str) -> bool:
        # TODO: Implement lessOrEqual method
        pass

    def plus(self, x: str) -> str:
        # TODO: Implement plus method
        pass

    def times(self, x: str) -> str:
        # TODO: Implement times method
        pass

    def equals(self, x: str) -> bool:
        # TODO: Implement equals method
        pass

    def lessThan(self, x: str) -> bool:
        # TODO: Implement lessThan method
        pass

class SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def equals(self, x: str) -> bool:
        # TODO: Implement equals method
        pass

class UnitFactor:

    pass
class SystemOfUnits:

    pass
class SystemOfQuantities:

    pass
class QuantityKindFactor:

    pass
class Prefix:

    pass