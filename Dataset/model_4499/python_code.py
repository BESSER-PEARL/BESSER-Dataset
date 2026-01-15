from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Unit:

    pass
class model_DerivedQuantityUnit(Unit):

    pass
class model_BaseQuantityUnit(Unit):

    pass
class ConversionFactor:

    pass
class model_ThermodynamicTemperatureConversionFactor(ConversionFactor):

    pass
class model_AngleConversionFactor(ConversionFactor):

    pass
class model_TimeConversionFactor(ConversionFactor):

    pass
class model_LuminousIntensityConversionFactor(ConversionFactor):

    pass
class model_AmountOfSubstanceConversionFactor(ConversionFactor):

    pass
class model_MassConversionFactor(ConversionFactor):

    pass
class model_ElectricCurrentConversionFactor(ConversionFactor):

    pass
class model_LengthConversionFactor(ConversionFactor):

    pass
class Quantity:

    pass
class model_DerivedQuantity(Quantity):

    pass
class model_BaseQuantity(Quantity):

    pass
class model_Sample:

    pass
class MeasurementUncertaintyInformation:

    pass
class model_Sampling(MeasurementUncertaintyInformation):

    def __init__(self, measurementProcedure: str, model_Sampling: set["model_Sample"] = None):
        self.measurementProcedure = measurementProcedure
        self.model_Sampling = model_Sampling if model_Sampling is not None else set()
        
    @property
    def measurementProcedure(self) -> str:
        return self.__measurementProcedure

    @measurementProcedure.setter
    def measurementProcedure(self, measurementProcedure: str):
        self.__measurementProcedure = measurementProcedure

    @property
    def model_Sampling(self):
        return self.__model_Sampling

    @model_Sampling.setter
    def model_Sampling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Sampling__model_Sampling", None)
        self.__model_Sampling = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Sample"):
                    opp_val = getattr(item, "model_Sample", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Sample", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Sample"):
                    opp_val = getattr(item, "model_Sample", None)
                    
                    setattr(item, "model_Sample", self)
                    

class model_Interval(MeasurementUncertaintyInformation):

    pass
class model_NormalDistribution(MeasurementUncertaintyInformation):

    def __init__(self, meanValue: float, standardDeviation: float):
        self.meanValue = meanValue
        self.standardDeviation = standardDeviation
        
    @property
    def standardDeviation(self) -> float:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: float):
        self.__standardDeviation = standardDeviation

    @property
    def meanValue(self) -> float:
        return self.__meanValue

    @meanValue.setter
    def meanValue(self, meanValue: float):
        self.__meanValue = meanValue

class model_LevelConversionFactor(ConversionFactor):

    pass
class model_TrafficIntensityConversionFactor(ConversionFactor):

    pass
class model_EntropyConversionFactor(ConversionFactor):

    pass
class model_DataStorageCapacityConversionFactor(ConversionFactor):

    pass
class model_MeasurementUncertaintyInformation(ABC):

    pass
class model_MeasurementUncertainty:

    def __init__(self, standardUncertainty: float, model_MeasurementUncertainty: "model_QuantityValue" = None, model_MeasurementUncertainty15: "model_MeasurementUncertaintyInformation" = None):
        self.standardUncertainty = standardUncertainty
        self.model_MeasurementUncertainty = model_MeasurementUncertainty
        self.model_MeasurementUncertainty15 = model_MeasurementUncertainty15
        
    @property
    def standardUncertainty(self) -> float:
        return self.__standardUncertainty

    @standardUncertainty.setter
    def standardUncertainty(self, standardUncertainty: float):
        self.__standardUncertainty = standardUncertainty

    @property
    def model_MeasurementUncertainty15(self):
        return self.__model_MeasurementUncertainty15

    @model_MeasurementUncertainty15.setter
    def model_MeasurementUncertainty15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MeasurementUncertainty__model_MeasurementUncertainty15", None)
        self.__model_MeasurementUncertainty15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MeasurementUncertaintyInformation"):
                opp_val = getattr(old_value, "model_MeasurementUncertaintyInformation", None)
                if opp_val == self:
                    setattr(old_value, "model_MeasurementUncertaintyInformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MeasurementUncertaintyInformation"):
                opp_val = getattr(value, "model_MeasurementUncertaintyInformation", None)
                setattr(value, "model_MeasurementUncertaintyInformation", self)

    @property
    def model_MeasurementUncertainty(self):
        return self.__model_MeasurementUncertainty

    @model_MeasurementUncertainty.setter
    def model_MeasurementUncertainty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MeasurementUncertainty__model_MeasurementUncertainty", None)
        self.__model_MeasurementUncertainty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_QuantityValue13"):
                opp_val = getattr(old_value, "model_QuantityValue13", None)
                if opp_val == self:
                    setattr(old_value, "model_QuantityValue13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_QuantityValue13"):
                opp_val = getattr(value, "model_QuantityValue13", None)
                setattr(value, "model_QuantityValue13", self)

class Dimension:

    pass
class model_DataStorageCapacityDimension(Dimension):

    pass
class model_LuminousIntensityDimension(Dimension):

    pass
class model_TrafficIntensityDimension(Dimension):

    pass
class model_MassDimension(Dimension):

    pass
class model_EntropyDimension(Dimension):

    pass
class model_TimeDimension(Dimension):

    pass
class model_ElectricCurrentDimension(Dimension):

    pass
class model_ThermodynamicTemperatureDimension(Dimension):

    pass
class model_LevelDimension(Dimension):

    pass
class model_AngleDimension(Dimension):

    pass
class model_AmountOfSubstanceDimension(Dimension):

    pass
class model_LengthDimension(Dimension):

    pass
class model_SystemOfUnits:

    def __init__(self, name: str, standardizationBody: str, model_SystemOfUnits: set["model_Unit"] = None):
        self.name = name
        self.standardizationBody = standardizationBody
        self.model_SystemOfUnits = model_SystemOfUnits if model_SystemOfUnits is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def standardizationBody(self) -> str:
        return self.__standardizationBody

    @standardizationBody.setter
    def standardizationBody(self, standardizationBody: str):
        self.__standardizationBody = standardizationBody

    @property
    def model_SystemOfUnits(self):
        return self.__model_SystemOfUnits

    @model_SystemOfUnits.setter
    def model_SystemOfUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_SystemOfUnits__model_SystemOfUnits", None)
        self.__model_SystemOfUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Unit8"):
                    opp_val = getattr(item, "model_Unit8", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Unit8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Unit8"):
                    opp_val = getattr(item, "model_Unit8", None)
                    
                    setattr(item, "model_Unit8", self)
                    

class BaseQuantityUnit:

    pass
class model_AngleUnit(BaseQuantityUnit):

    pass
class model_ElectricCurrentUnit(BaseQuantityUnit):

    pass
class model_MassUnit(BaseQuantityUnit):

    pass
class model_ThermodynamicTemperatureUnit(BaseQuantityUnit):

    pass
class model_DataStorageCapacityUnit(BaseQuantityUnit):

    pass
class model_TimeUnit(BaseQuantityUnit):

    pass
class model_TrafficIntensityUnit(BaseQuantityUnit):

    pass
class model_EntropyUnit(BaseQuantityUnit):

    pass
class model_LevelUnit(BaseQuantityUnit):

    pass
class model_AmountOfSubstanceUnit(BaseQuantityUnit):

    pass
class model_LuminousIntensityUnit(BaseQuantityUnit):

    pass
class model_LengthUnit(BaseQuantityUnit):

    pass
class model_ConversionFactor(ABC):

    def __init__(self, multiplicator: float, offset: float, model_ConversionFactor: "model_Unit" = None, model_ConversionFactor10: "model_Unit" = None):
        self.multiplicator = multiplicator
        self.offset = offset
        self.model_ConversionFactor = model_ConversionFactor
        self.model_ConversionFactor10 = model_ConversionFactor10
        
    @property
    def offset(self) -> float:
        return self.__offset

    @offset.setter
    def offset(self, offset: float):
        self.__offset = offset

    @property
    def multiplicator(self) -> float:
        return self.__multiplicator

    @multiplicator.setter
    def multiplicator(self, multiplicator: float):
        self.__multiplicator = multiplicator

    @property
    def model_ConversionFactor10(self):
        return self.__model_ConversionFactor10

    @model_ConversionFactor10.setter
    def model_ConversionFactor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ConversionFactor__model_ConversionFactor10", None)
        self.__model_ConversionFactor10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Unit11"):
                opp_val = getattr(old_value, "model_Unit11", None)
                if opp_val == self:
                    setattr(old_value, "model_Unit11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Unit11"):
                opp_val = getattr(value, "model_Unit11", None)
                setattr(value, "model_Unit11", self)

    @property
    def model_ConversionFactor(self):
        return self.__model_ConversionFactor

    @model_ConversionFactor.setter
    def model_ConversionFactor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ConversionFactor__model_ConversionFactor", None)
        self.__model_ConversionFactor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Unit6"):
                opp_val = getattr(old_value, "model_Unit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Unit6"):
                opp_val = getattr(value, "model_Unit6", None)
                if opp_val is None:
                    setattr(value, "model_Unit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Dimension(ABC):

    def __init__(self, exponent: float, model_Dimension: "model_Unit" = None):
        self.exponent = exponent
        self.model_Dimension = model_Dimension
        
    @property
    def exponent(self) -> float:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: float):
        self.__exponent = exponent

    @property
    def model_Dimension(self):
        return self.__model_Dimension

    @model_Dimension.setter
    def model_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Dimension__model_Dimension", None)
        self.__model_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Unit4"):
                opp_val = getattr(old_value, "model_Unit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Unit4"):
                opp_val = getattr(value, "model_Unit4", None)
                if opp_val is None:
                    setattr(value, "model_Unit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BaseQuantity:

    pass
class model_TrafficIntensity(BaseQuantity):

    pass
class model_Level(BaseQuantity):

    pass
class model_Time(BaseQuantity):

    pass
class model_AmountOfSubstance(BaseQuantity):

    pass
class model_Entropy(BaseQuantity):

    pass
class model_Mass(BaseQuantity):

    pass
class model_ElectricCurrent(BaseQuantity):

    pass
class model_ThermodynamicTemperature(BaseQuantity):

    pass
class model_Angle(BaseQuantity):

    pass
class model_DataStorageCapacity(BaseQuantity):

    pass
class model_LuminousIntensity(BaseQuantity):

    pass
class model_Length(BaseQuantity):

    pass
class model_QuantityValue:

    def __init__(self, value: float, model_QuantityValue: "model_Quantity" = None, model_QuantityValue13: "model_MeasurementUncertainty" = None):
        self.value = value
        self.model_QuantityValue = model_QuantityValue
        self.model_QuantityValue13 = model_QuantityValue13
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def model_QuantityValue(self):
        return self.__model_QuantityValue

    @model_QuantityValue.setter
    def model_QuantityValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_QuantityValue__model_QuantityValue", None)
        self.__model_QuantityValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Quantity2"):
                opp_val = getattr(old_value, "model_Quantity2", None)
                if opp_val == self:
                    setattr(old_value, "model_Quantity2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Quantity2"):
                opp_val = getattr(value, "model_Quantity2", None)
                setattr(value, "model_Quantity2", self)

    @property
    def model_QuantityValue13(self):
        return self.__model_QuantityValue13

    @model_QuantityValue13.setter
    def model_QuantityValue13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_QuantityValue__model_QuantityValue13", None)
        self.__model_QuantityValue13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MeasurementUncertainty"):
                opp_val = getattr(old_value, "model_MeasurementUncertainty", None)
                if opp_val == self:
                    setattr(old_value, "model_MeasurementUncertainty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MeasurementUncertainty"):
                opp_val = getattr(value, "model_MeasurementUncertainty", None)
                setattr(value, "model_MeasurementUncertainty", self)

class model_Unit(ABC):

    def __init__(self, name: str, symbol: str, isRatioScaled: bool, isBaseUnit: bool, isDerivedUnit: bool, isCoherentDerivedUnit: bool, isIntervalScaled: bool, model_Unit: "model_Quantity" = None, model_Unit4: set["model_Dimension"] = None, model_Unit6: set["model_ConversionFactor"] = None, model_Unit8: "model_SystemOfUnits" = None, model_Unit11: "model_ConversionFactor" = None):
        self.name = name
        self.symbol = symbol
        self.isRatioScaled = isRatioScaled
        self.isBaseUnit = isBaseUnit
        self.isDerivedUnit = isDerivedUnit
        self.isCoherentDerivedUnit = isCoherentDerivedUnit
        self.isIntervalScaled = isIntervalScaled
        self.model_Unit = model_Unit
        self.model_Unit4 = model_Unit4 if model_Unit4 is not None else set()
        self.model_Unit6 = model_Unit6 if model_Unit6 is not None else set()
        self.model_Unit8 = model_Unit8
        self.model_Unit11 = model_Unit11
        
    @property
    def isDerivedUnit(self) -> bool:
        return self.__isDerivedUnit

    @isDerivedUnit.setter
    def isDerivedUnit(self, isDerivedUnit: bool):
        self.__isDerivedUnit = isDerivedUnit

    @property
    def isCoherentDerivedUnit(self) -> bool:
        return self.__isCoherentDerivedUnit

    @isCoherentDerivedUnit.setter
    def isCoherentDerivedUnit(self, isCoherentDerivedUnit: bool):
        self.__isCoherentDerivedUnit = isCoherentDerivedUnit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isIntervalScaled(self) -> bool:
        return self.__isIntervalScaled

    @isIntervalScaled.setter
    def isIntervalScaled(self, isIntervalScaled: bool):
        self.__isIntervalScaled = isIntervalScaled

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def isBaseUnit(self) -> bool:
        return self.__isBaseUnit

    @isBaseUnit.setter
    def isBaseUnit(self, isBaseUnit: bool):
        self.__isBaseUnit = isBaseUnit

    @property
    def isRatioScaled(self) -> bool:
        return self.__isRatioScaled

    @isRatioScaled.setter
    def isRatioScaled(self, isRatioScaled: bool):
        self.__isRatioScaled = isRatioScaled

    @property
    def model_Unit8(self):
        return self.__model_Unit8

    @model_Unit8.setter
    def model_Unit8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Unit__model_Unit8", None)
        self.__model_Unit8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_SystemOfUnits"):
                opp_val = getattr(old_value, "model_SystemOfUnits", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_SystemOfUnits"):
                opp_val = getattr(value, "model_SystemOfUnits", None)
                if opp_val is None:
                    setattr(value, "model_SystemOfUnits", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Unit4(self):
        return self.__model_Unit4

    @model_Unit4.setter
    def model_Unit4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Unit__model_Unit4", None)
        self.__model_Unit4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Dimension"):
                    opp_val = getattr(item, "model_Dimension", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Dimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Dimension"):
                    opp_val = getattr(item, "model_Dimension", None)
                    
                    setattr(item, "model_Dimension", self)
                    

    @property
    def model_Unit(self):
        return self.__model_Unit

    @model_Unit.setter
    def model_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Unit__model_Unit", None)
        self.__model_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Quantity"):
                opp_val = getattr(old_value, "model_Quantity", None)
                if opp_val == self:
                    setattr(old_value, "model_Quantity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Quantity"):
                opp_val = getattr(value, "model_Quantity", None)
                setattr(value, "model_Quantity", self)

    @property
    def model_Unit6(self):
        return self.__model_Unit6

    @model_Unit6.setter
    def model_Unit6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Unit__model_Unit6", None)
        self.__model_Unit6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ConversionFactor"):
                    opp_val = getattr(item, "model_ConversionFactor", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ConversionFactor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ConversionFactor"):
                    opp_val = getattr(item, "model_ConversionFactor", None)
                    
                    setattr(item, "model_ConversionFactor", self)
                    

    @property
    def model_Unit11(self):
        return self.__model_Unit11

    @model_Unit11.setter
    def model_Unit11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Unit__model_Unit11", None)
        self.__model_Unit11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ConversionFactor10"):
                opp_val = getattr(old_value, "model_ConversionFactor10", None)
                if opp_val == self:
                    setattr(old_value, "model_ConversionFactor10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ConversionFactor10"):
                opp_val = getattr(value, "model_ConversionFactor10", None)
                setattr(value, "model_ConversionFactor10", self)

class model_Quantity(ABC):

    pass