from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class IndicatorOccurrence4(Enum):
    Before = "Before"
    After = "After"
class NumberTypeType1(Enum):
    Single = "Single"
    Range = "Range"
class IndicatorOccurrence(Enum):
    Before = "Before"
    After = "After"
class NumberRangeOccurence(Enum):
    BeforeName = "BeforeName"
    AfterName = "AfterName"
    BeforeType = "BeforeType"
    AfterType = "AfterType"
class TypeOccurrence1(Enum):
    Before = "Before"
    After = "After"
class NumberTypeOccurrence1(Enum):
    Before = "Before"
    After = "After"
class NumberTypeOccurrence(Enum):
    Before = "Before"
    After = "After"
class IndicatorOccurrence3(Enum):
    Before = "Before"
    After = "After"
class IndicatorOccurrence2(Enum):
    Before = "Before"
    After = "After"
class NameNumberOccurrence(Enum):
    Before = "Before"
    After = "After"
class NumberRangeOccurrence(Enum):
    BeforeName = "BeforeName"
    AfterName = "AfterName"
    BeforeType = "BeforeType"
    AfterType = "AfterType"
class IndicatorOccurrence1(Enum):
    Before = "Before"
    After = "After"
class TypeOccurrence(Enum):
    Before = "Before"
    After = "After"
class TypeOccurrence2(Enum):
    Before = "Before"
    After = "After"
class NumberTypeType(Enum):
    Single = "Single"
    Range = "Range"
class RangeTypeType(Enum):
    Odd = "Odd"
    Even = "Even"
class IndicatorOccurence(Enum):
    Before = "Before"
    After = "After"
class NumberOccurrence(Enum):
    BeforeName = "BeforeName"
    AfterName = "AfterName"
    BeforeType = "BeforeType"
    AfterType = "AfterType"
class DependentThoroughfaresType(Enum):
    Yes = "Yes"
    No = "No"


############################################
# Definition of Classes
############################################

class xal_ThoroughfareNumberTo:

    def __init__(self, mixed: str, code: str, anyAttribute: str, xal_ThoroughfareNumberTo: "xal_ThoroughfareNumberRange" = None, xal_ThoroughfareNumberTo461: set["xal_AddressLine"] = None, xal_ThoroughfareNumberTo464: set["xal_ThoroughfareNumberPrefix"] = None, xal_ThoroughfareNumberTo467: set["xal_ThoroughfareNumber"] = None, xal_ThoroughfareNumberTo470: set["xal_ThoroughfareNumberSuffix"] = None):
        self.mixed = mixed
        self.code = code
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareNumberTo = xal_ThoroughfareNumberTo
        self.xal_ThoroughfareNumberTo461 = xal_ThoroughfareNumberTo461 if xal_ThoroughfareNumberTo461 is not None else set()
        self.xal_ThoroughfareNumberTo464 = xal_ThoroughfareNumberTo464 if xal_ThoroughfareNumberTo464 is not None else set()
        self.xal_ThoroughfareNumberTo467 = xal_ThoroughfareNumberTo467 if xal_ThoroughfareNumberTo467 is not None else set()
        self.xal_ThoroughfareNumberTo470 = xal_ThoroughfareNumberTo470 if xal_ThoroughfareNumberTo470 is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_ThoroughfareNumberTo464(self):
        return self.__xal_ThoroughfareNumberTo464

    @xal_ThoroughfareNumberTo464.setter
    def xal_ThoroughfareNumberTo464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberTo__xal_ThoroughfareNumberTo464", None)
        self.__xal_ThoroughfareNumberTo464 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix465"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix465", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberPrefix465", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix465"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix465", None)
                    
                    setattr(item, "xal_ThoroughfareNumberPrefix465", self)
                    

    @property
    def xal_ThoroughfareNumberTo461(self):
        return self.__xal_ThoroughfareNumberTo461

    @xal_ThoroughfareNumberTo461.setter
    def xal_ThoroughfareNumberTo461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberTo__xal_ThoroughfareNumberTo461", None)
        self.__xal_ThoroughfareNumberTo461 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine462"):
                    opp_val = getattr(item, "xal_AddressLine462", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine462", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine462"):
                    opp_val = getattr(item, "xal_AddressLine462", None)
                    
                    setattr(item, "xal_AddressLine462", self)
                    

    @property
    def xal_ThoroughfareNumberTo470(self):
        return self.__xal_ThoroughfareNumberTo470

    @xal_ThoroughfareNumberTo470.setter
    def xal_ThoroughfareNumberTo470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberTo__xal_ThoroughfareNumberTo470", None)
        self.__xal_ThoroughfareNumberTo470 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix471"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix471", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberSuffix471", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix471"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix471", None)
                    
                    setattr(item, "xal_ThoroughfareNumberSuffix471", self)
                    

    @property
    def xal_ThoroughfareNumberTo467(self):
        return self.__xal_ThoroughfareNumberTo467

    @xal_ThoroughfareNumberTo467.setter
    def xal_ThoroughfareNumberTo467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberTo__xal_ThoroughfareNumberTo467", None)
        self.__xal_ThoroughfareNumberTo467 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumber468"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber468", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumber468", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumber468"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber468", None)
                    
                    setattr(item, "xal_ThoroughfareNumber468", self)
                    

    @property
    def xal_ThoroughfareNumberTo(self):
        return self.__xal_ThoroughfareNumberTo

    @xal_ThoroughfareNumberTo.setter
    def xal_ThoroughfareNumberTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberTo__xal_ThoroughfareNumberTo", None)
        self.__xal_ThoroughfareNumberTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberRange459"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberRange459", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareNumberRange459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberRange459"):
                opp_val = getattr(value, "xal_ThoroughfareNumberRange459", None)
                setattr(value, "xal_ThoroughfareNumberRange459", self)

class xal_ThoroughfareNumberFrom:

    def __init__(self, mixed: str, code: str, anyAttribute: str, xal_ThoroughfareNumberFrom: set["xal_AddressLine"] = None, xal_ThoroughfareNumberFrom444: set["xal_ThoroughfareNumberPrefix"] = None, xal_ThoroughfareNumberFrom450: set["xal_ThoroughfareNumberSuffix"] = None, xal_ThoroughfareNumberFrom447: set["xal_ThoroughfareNumber"] = None, xal_ThoroughfareNumberFrom457: "xal_ThoroughfareNumberRange" = None):
        self.mixed = mixed
        self.code = code
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareNumberFrom = xal_ThoroughfareNumberFrom if xal_ThoroughfareNumberFrom is not None else set()
        self.xal_ThoroughfareNumberFrom444 = xal_ThoroughfareNumberFrom444 if xal_ThoroughfareNumberFrom444 is not None else set()
        self.xal_ThoroughfareNumberFrom450 = xal_ThoroughfareNumberFrom450 if xal_ThoroughfareNumberFrom450 is not None else set()
        self.xal_ThoroughfareNumberFrom447 = xal_ThoroughfareNumberFrom447 if xal_ThoroughfareNumberFrom447 is not None else set()
        self.xal_ThoroughfareNumberFrom457 = xal_ThoroughfareNumberFrom457
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_ThoroughfareNumberFrom450(self):
        return self.__xal_ThoroughfareNumberFrom450

    @xal_ThoroughfareNumberFrom450.setter
    def xal_ThoroughfareNumberFrom450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberFrom__xal_ThoroughfareNumberFrom450", None)
        self.__xal_ThoroughfareNumberFrom450 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix451"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix451", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberSuffix451", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix451"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix451", None)
                    
                    setattr(item, "xal_ThoroughfareNumberSuffix451", self)
                    

    @property
    def xal_ThoroughfareNumberFrom447(self):
        return self.__xal_ThoroughfareNumberFrom447

    @xal_ThoroughfareNumberFrom447.setter
    def xal_ThoroughfareNumberFrom447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberFrom__xal_ThoroughfareNumberFrom447", None)
        self.__xal_ThoroughfareNumberFrom447 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumber448"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber448", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumber448", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumber448"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber448", None)
                    
                    setattr(item, "xal_ThoroughfareNumber448", self)
                    

    @property
    def xal_ThoroughfareNumberFrom444(self):
        return self.__xal_ThoroughfareNumberFrom444

    @xal_ThoroughfareNumberFrom444.setter
    def xal_ThoroughfareNumberFrom444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberFrom__xal_ThoroughfareNumberFrom444", None)
        self.__xal_ThoroughfareNumberFrom444 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix445"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix445", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberPrefix445", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix445"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix445", None)
                    
                    setattr(item, "xal_ThoroughfareNumberPrefix445", self)
                    

    @property
    def xal_ThoroughfareNumberFrom(self):
        return self.__xal_ThoroughfareNumberFrom

    @xal_ThoroughfareNumberFrom.setter
    def xal_ThoroughfareNumberFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberFrom__xal_ThoroughfareNumberFrom", None)
        self.__xal_ThoroughfareNumberFrom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine442"):
                    opp_val = getattr(item, "xal_AddressLine442", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine442", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine442"):
                    opp_val = getattr(item, "xal_AddressLine442", None)
                    
                    setattr(item, "xal_AddressLine442", self)
                    

    @property
    def xal_ThoroughfareNumberFrom457(self):
        return self.__xal_ThoroughfareNumberFrom457

    @xal_ThoroughfareNumberFrom457.setter
    def xal_ThoroughfareNumberFrom457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberFrom__xal_ThoroughfareNumberFrom457", None)
        self.__xal_ThoroughfareNumberFrom457 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberRange456"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberRange456", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareNumberRange456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberRange456"):
                opp_val = getattr(value, "xal_ThoroughfareNumberRange456", None)
                setattr(value, "xal_ThoroughfareNumberRange456", self)

class xal_ThoroughfareNumberRange:

    def __init__(self, code: str, indicator: str, indicatorOccurrence: str, numberRangeOccurrence: str, rangeType: str, separator: str, type: str, anyAttribute: str, xal_ThoroughfareNumberRange: "xal_Thoroughfare" = None, xal_ThoroughfareNumberRange459: "xal_ThoroughfareNumberTo" = None, xal_ThoroughfareNumberRange453: set["xal_AddressLine"] = None, xal_ThoroughfareNumberRange456: "xal_ThoroughfareNumberFrom" = None):
        self.code = code
        self.indicator = indicator
        self.indicatorOccurrence = indicatorOccurrence
        self.numberRangeOccurrence = numberRangeOccurrence
        self.rangeType = rangeType
        self.separator = separator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareNumberRange = xal_ThoroughfareNumberRange
        self.xal_ThoroughfareNumberRange459 = xal_ThoroughfareNumberRange459
        self.xal_ThoroughfareNumberRange453 = xal_ThoroughfareNumberRange453 if xal_ThoroughfareNumberRange453 is not None else set()
        self.xal_ThoroughfareNumberRange456 = xal_ThoroughfareNumberRange456
        
    @property
    def numberRangeOccurrence(self) -> str:
        return self.__numberRangeOccurrence

    @numberRangeOccurrence.setter
    def numberRangeOccurrence(self, numberRangeOccurrence: str):
        self.__numberRangeOccurrence = numberRangeOccurrence

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def rangeType(self) -> str:
        return self.__rangeType

    @rangeType.setter
    def rangeType(self, rangeType: str):
        self.__rangeType = rangeType

    @property
    def indicatorOccurrence(self) -> str:
        return self.__indicatorOccurrence

    @indicatorOccurrence.setter
    def indicatorOccurrence(self, indicatorOccurrence: str):
        self.__indicatorOccurrence = indicatorOccurrence

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def separator(self) -> str:
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_ThoroughfareNumberRange459(self):
        return self.__xal_ThoroughfareNumberRange459

    @xal_ThoroughfareNumberRange459.setter
    def xal_ThoroughfareNumberRange459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberRange__xal_ThoroughfareNumberRange459", None)
        self.__xal_ThoroughfareNumberRange459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberTo"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberTo", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareNumberTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberTo"):
                opp_val = getattr(value, "xal_ThoroughfareNumberTo", None)
                setattr(value, "xal_ThoroughfareNumberTo", self)

    @property
    def xal_ThoroughfareNumberRange(self):
        return self.__xal_ThoroughfareNumberRange

    @xal_ThoroughfareNumberRange.setter
    def xal_ThoroughfareNumberRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberRange__xal_ThoroughfareNumberRange", None)
        self.__xal_ThoroughfareNumberRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare404"):
                opp_val = getattr(old_value, "xal_Thoroughfare404", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare404"):
                opp_val = getattr(value, "xal_Thoroughfare404", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare404", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberRange456(self):
        return self.__xal_ThoroughfareNumberRange456

    @xal_ThoroughfareNumberRange456.setter
    def xal_ThoroughfareNumberRange456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberRange__xal_ThoroughfareNumberRange456", None)
        self.__xal_ThoroughfareNumberRange456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberFrom457"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberFrom457", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareNumberFrom457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberFrom457"):
                opp_val = getattr(value, "xal_ThoroughfareNumberFrom457", None)
                setattr(value, "xal_ThoroughfareNumberFrom457", self)

    @property
    def xal_ThoroughfareNumberRange453(self):
        return self.__xal_ThoroughfareNumberRange453

    @xal_ThoroughfareNumberRange453.setter
    def xal_ThoroughfareNumberRange453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberRange__xal_ThoroughfareNumberRange453", None)
        self.__xal_ThoroughfareNumberRange453 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine454"):
                    opp_val = getattr(item, "xal_AddressLine454", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine454", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine454"):
                    opp_val = getattr(item, "xal_AddressLine454", None)
                    
                    setattr(item, "xal_AddressLine454", self)
                    

class xal_SubPremiseLocation:

    def __init__(self, code: str, mixed: str, xal_SubPremiseLocation: "xal_SubPremise" = None):
        self.code = code
        self.mixed = mixed
        self.xal_SubPremiseLocation = xal_SubPremiseLocation
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_SubPremiseLocation(self):
        return self.__xal_SubPremiseLocation

    @xal_SubPremiseLocation.setter
    def xal_SubPremiseLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremiseLocation__xal_SubPremiseLocation", None)
        self.__xal_SubPremiseLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise375"):
                opp_val = getattr(old_value, "xal_SubPremise375", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise375"):
                opp_val = getattr(value, "xal_SubPremise375", None)
                setattr(value, "xal_SubPremise375", self)

class xal_SubPremiseName:

    def __init__(self, mixed: str, type: str, typeOccurrence: str, anyAttribute: str, code: str, xal_SubPremiseName: "xal_SubPremise" = None):
        self.mixed = mixed
        self.type = type
        self.typeOccurrence = typeOccurrence
        self.anyAttribute = anyAttribute
        self.code = code
        self.xal_SubPremiseName = xal_SubPremiseName
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def typeOccurrence(self) -> str:
        return self.__typeOccurrence

    @typeOccurrence.setter
    def typeOccurrence(self, typeOccurrence: str):
        self.__typeOccurrence = typeOccurrence

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_SubPremiseName(self):
        return self.__xal_SubPremiseName

    @xal_SubPremiseName.setter
    def xal_SubPremiseName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremiseName__xal_SubPremiseName", None)
        self.__xal_SubPremiseName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise373"):
                opp_val = getattr(old_value, "xal_SubPremise373", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise373"):
                opp_val = getattr(value, "xal_SubPremise373", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise373", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_SubPremiseNumberSuffix:

    def __init__(self, mixed: str, code: str, numberSuffixSeparator: str, type: str, anyAttribute: str, xal_SubPremiseNumberSuffix: "xal_SubPremise" = None):
        self.mixed = mixed
        self.code = code
        self.numberSuffixSeparator = numberSuffixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_SubPremiseNumberSuffix = xal_SubPremiseNumberSuffix
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberSuffixSeparator(self) -> str:
        return self.__numberSuffixSeparator

    @numberSuffixSeparator.setter
    def numberSuffixSeparator(self, numberSuffixSeparator: str):
        self.__numberSuffixSeparator = numberSuffixSeparator

    @property
    def xal_SubPremiseNumberSuffix(self):
        return self.__xal_SubPremiseNumberSuffix

    @xal_SubPremiseNumberSuffix.setter
    def xal_SubPremiseNumberSuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremiseNumberSuffix__xal_SubPremiseNumberSuffix", None)
        self.__xal_SubPremiseNumberSuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise381"):
                opp_val = getattr(old_value, "xal_SubPremise381", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise381"):
                opp_val = getattr(value, "xal_SubPremise381", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise381", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_SubPremiseNumberPrefix:

    def __init__(self, mixed: str, code: str, numberPrefixSeparator: str, type: str, anyAttribute: str, xal_SubPremiseNumberPrefix: "xal_SubPremise" = None):
        self.mixed = mixed
        self.code = code
        self.numberPrefixSeparator = numberPrefixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_SubPremiseNumberPrefix = xal_SubPremiseNumberPrefix
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def numberPrefixSeparator(self) -> str:
        return self.__numberPrefixSeparator

    @numberPrefixSeparator.setter
    def numberPrefixSeparator(self, numberPrefixSeparator: str):
        self.__numberPrefixSeparator = numberPrefixSeparator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_SubPremiseNumberPrefix(self):
        return self.__xal_SubPremiseNumberPrefix

    @xal_SubPremiseNumberPrefix.setter
    def xal_SubPremiseNumberPrefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremiseNumberPrefix__xal_SubPremiseNumberPrefix", None)
        self.__xal_SubPremiseNumberPrefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise379"):
                opp_val = getattr(old_value, "xal_SubPremise379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise379"):
                opp_val = getattr(value, "xal_SubPremise379", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_SubPremiseNumber:

    def __init__(self, mixed: str, code: str, indicator: str, indicatorOccurrence: str, type: str, anyAttribute: str, numberTypeOccurrence: str, premiseNumberSeparator: str, xal_SubPremiseNumber: "xal_SubPremise" = None):
        self.mixed = mixed
        self.code = code
        self.indicator = indicator
        self.indicatorOccurrence = indicatorOccurrence
        self.type = type
        self.anyAttribute = anyAttribute
        self.numberTypeOccurrence = numberTypeOccurrence
        self.premiseNumberSeparator = premiseNumberSeparator
        self.xal_SubPremiseNumber = xal_SubPremiseNumber
        
    @property
    def indicatorOccurrence(self) -> str:
        return self.__indicatorOccurrence

    @indicatorOccurrence.setter
    def indicatorOccurrence(self, indicatorOccurrence: str):
        self.__indicatorOccurrence = indicatorOccurrence

    @property
    def premiseNumberSeparator(self) -> str:
        return self.__premiseNumberSeparator

    @premiseNumberSeparator.setter
    def premiseNumberSeparator(self, premiseNumberSeparator: str):
        self.__premiseNumberSeparator = premiseNumberSeparator

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberTypeOccurrence(self) -> str:
        return self.__numberTypeOccurrence

    @numberTypeOccurrence.setter
    def numberTypeOccurrence(self, numberTypeOccurrence: str):
        self.__numberTypeOccurrence = numberTypeOccurrence

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def xal_SubPremiseNumber(self):
        return self.__xal_SubPremiseNumber

    @xal_SubPremiseNumber.setter
    def xal_SubPremiseNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremiseNumber__xal_SubPremiseNumber", None)
        self.__xal_SubPremiseNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise377"):
                opp_val = getattr(old_value, "xal_SubPremise377", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise377"):
                opp_val = getattr(value, "xal_SubPremise377", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise377", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_SubAdministrativeAreaName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_SubAdministrativeAreaName: "xal_SubAdministrativeArea" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_SubAdministrativeAreaName = xal_SubAdministrativeAreaName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_SubAdministrativeAreaName(self):
        return self.__xal_SubAdministrativeAreaName

    @xal_SubAdministrativeAreaName.setter
    def xal_SubAdministrativeAreaName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeAreaName__xal_SubAdministrativeAreaName", None)
        self.__xal_SubAdministrativeAreaName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea359"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea359", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea359"):
                opp_val = getattr(value, "xal_SubAdministrativeArea359", None)
                if opp_val is None:
                    setattr(value, "xal_SubAdministrativeArea359", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PremiseNumberRangeTo:

    pass
class xal_PremiseNumberRangeFrom:

    pass
class xal_SubPremise:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_SubPremise: "xal_Premise" = None, xal_SubPremise370: set["xal_AddressLine"] = None, xal_SubPremise377: set["xal_SubPremiseNumber"] = None, xal_SubPremise379: set["xal_SubPremiseNumberPrefix"] = None, xal_SubPremise381: set["xal_SubPremiseNumberSuffix"] = None, xal_SubPremise383: set["xal_BuildingName"] = None, xal_SubPremise373: set["xal_SubPremiseName"] = None, xal_SubPremise375: "xal_SubPremiseLocation" = None, xal_SubPremise392: "xal_PostalCode" = None, xal_SubPremise396: "xal_SubPremise" = None, xal_SubPremise394: "xal_SubPremise" = None, xal_SubPremise386: "xal_Firm" = None, xal_SubPremise389: "xal_MailStop" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_SubPremise = xal_SubPremise
        self.xal_SubPremise370 = xal_SubPremise370 if xal_SubPremise370 is not None else set()
        self.xal_SubPremise377 = xal_SubPremise377 if xal_SubPremise377 is not None else set()
        self.xal_SubPremise379 = xal_SubPremise379 if xal_SubPremise379 is not None else set()
        self.xal_SubPremise381 = xal_SubPremise381 if xal_SubPremise381 is not None else set()
        self.xal_SubPremise383 = xal_SubPremise383 if xal_SubPremise383 is not None else set()
        self.xal_SubPremise373 = xal_SubPremise373 if xal_SubPremise373 is not None else set()
        self.xal_SubPremise375 = xal_SubPremise375
        self.xal_SubPremise392 = xal_SubPremise392
        self.xal_SubPremise396 = xal_SubPremise396
        self.xal_SubPremise394 = xal_SubPremise394
        self.xal_SubPremise386 = xal_SubPremise386
        self.xal_SubPremise389 = xal_SubPremise389
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_SubPremise375(self):
        return self.__xal_SubPremise375

    @xal_SubPremise375.setter
    def xal_SubPremise375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise375", None)
        self.__xal_SubPremise375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremiseLocation"):
                opp_val = getattr(old_value, "xal_SubPremiseLocation", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremiseLocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremiseLocation"):
                opp_val = getattr(value, "xal_SubPremiseLocation", None)
                setattr(value, "xal_SubPremiseLocation", self)

    @property
    def xal_SubPremise394(self):
        return self.__xal_SubPremise394

    @xal_SubPremise394.setter
    def xal_SubPremise394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise394", None)
        self.__xal_SubPremise394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise396"):
                opp_val = getattr(old_value, "xal_SubPremise396", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise396"):
                opp_val = getattr(value, "xal_SubPremise396", None)
                setattr(value, "xal_SubPremise396", self)

    @property
    def xal_SubPremise(self):
        return self.__xal_SubPremise

    @xal_SubPremise.setter
    def xal_SubPremise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise", None)
        self.__xal_SubPremise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise314"):
                opp_val = getattr(old_value, "xal_Premise314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise314"):
                opp_val = getattr(value, "xal_Premise314", None)
                if opp_val is None:
                    setattr(value, "xal_Premise314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_SubPremise389(self):
        return self.__xal_SubPremise389

    @xal_SubPremise389.setter
    def xal_SubPremise389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise389", None)
        self.__xal_SubPremise389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop390"):
                opp_val = getattr(old_value, "xal_MailStop390", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop390", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop390"):
                opp_val = getattr(value, "xal_MailStop390", None)
                setattr(value, "xal_MailStop390", self)

    @property
    def xal_SubPremise396(self):
        return self.__xal_SubPremise396

    @xal_SubPremise396.setter
    def xal_SubPremise396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise396", None)
        self.__xal_SubPremise396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise394"):
                opp_val = getattr(old_value, "xal_SubPremise394", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise394"):
                opp_val = getattr(value, "xal_SubPremise394", None)
                setattr(value, "xal_SubPremise394", self)

    @property
    def xal_SubPremise373(self):
        return self.__xal_SubPremise373

    @xal_SubPremise373.setter
    def xal_SubPremise373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise373", None)
        self.__xal_SubPremise373 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubPremiseName"):
                    opp_val = getattr(item, "xal_SubPremiseName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubPremiseName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubPremiseName"):
                    opp_val = getattr(item, "xal_SubPremiseName", None)
                    
                    setattr(item, "xal_SubPremiseName", self)
                    

    @property
    def xal_SubPremise370(self):
        return self.__xal_SubPremise370

    @xal_SubPremise370.setter
    def xal_SubPremise370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise370", None)
        self.__xal_SubPremise370 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine371"):
                    opp_val = getattr(item, "xal_AddressLine371", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine371", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine371"):
                    opp_val = getattr(item, "xal_AddressLine371", None)
                    
                    setattr(item, "xal_AddressLine371", self)
                    

    @property
    def xal_SubPremise377(self):
        return self.__xal_SubPremise377

    @xal_SubPremise377.setter
    def xal_SubPremise377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise377", None)
        self.__xal_SubPremise377 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubPremiseNumber"):
                    opp_val = getattr(item, "xal_SubPremiseNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubPremiseNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubPremiseNumber"):
                    opp_val = getattr(item, "xal_SubPremiseNumber", None)
                    
                    setattr(item, "xal_SubPremiseNumber", self)
                    

    @property
    def xal_SubPremise386(self):
        return self.__xal_SubPremise386

    @xal_SubPremise386.setter
    def xal_SubPremise386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise386", None)
        self.__xal_SubPremise386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm387"):
                opp_val = getattr(old_value, "xal_Firm387", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm387"):
                opp_val = getattr(value, "xal_Firm387", None)
                setattr(value, "xal_Firm387", self)

    @property
    def xal_SubPremise381(self):
        return self.__xal_SubPremise381

    @xal_SubPremise381.setter
    def xal_SubPremise381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise381", None)
        self.__xal_SubPremise381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubPremiseNumberSuffix"):
                    opp_val = getattr(item, "xal_SubPremiseNumberSuffix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubPremiseNumberSuffix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubPremiseNumberSuffix"):
                    opp_val = getattr(item, "xal_SubPremiseNumberSuffix", None)
                    
                    setattr(item, "xal_SubPremiseNumberSuffix", self)
                    

    @property
    def xal_SubPremise392(self):
        return self.__xal_SubPremise392

    @xal_SubPremise392.setter
    def xal_SubPremise392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise392", None)
        self.__xal_SubPremise392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode393"):
                opp_val = getattr(old_value, "xal_PostalCode393", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode393"):
                opp_val = getattr(value, "xal_PostalCode393", None)
                setattr(value, "xal_PostalCode393", self)

    @property
    def xal_SubPremise383(self):
        return self.__xal_SubPremise383

    @xal_SubPremise383.setter
    def xal_SubPremise383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise383", None)
        self.__xal_SubPremise383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_BuildingName384"):
                    opp_val = getattr(item, "xal_BuildingName384", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_BuildingName384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_BuildingName384"):
                    opp_val = getattr(item, "xal_BuildingName384", None)
                    
                    setattr(item, "xal_BuildingName384", self)
                    

    @property
    def xal_SubPremise379(self):
        return self.__xal_SubPremise379

    @xal_SubPremise379.setter
    def xal_SubPremise379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubPremise__xal_SubPremise379", None)
        self.__xal_SubPremise379 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubPremiseNumberPrefix"):
                    opp_val = getattr(item, "xal_SubPremiseNumberPrefix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubPremiseNumberPrefix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubPremiseNumberPrefix"):
                    opp_val = getattr(item, "xal_SubPremiseNumberPrefix", None)
                    
                    setattr(item, "xal_SubPremiseNumberPrefix", self)
                    

class xal_PremiseNumberRange:

    def __init__(self, separator: str, indicator: str, indicatorOccurence: str, numberRangeOccurence: str, rangeType: str, type: str, xal_PremiseNumberRange: "xal_Premise" = None, xal_PremiseNumberRange328: "xal_PremiseNumberRangeFrom" = None, xal_PremiseNumberRange330: "xal_PremiseNumberRangeTo" = None):
        self.separator = separator
        self.indicator = indicator
        self.indicatorOccurence = indicatorOccurence
        self.numberRangeOccurence = numberRangeOccurence
        self.rangeType = rangeType
        self.type = type
        self.xal_PremiseNumberRange = xal_PremiseNumberRange
        self.xal_PremiseNumberRange328 = xal_PremiseNumberRange328
        self.xal_PremiseNumberRange330 = xal_PremiseNumberRange330
        
    @property
    def indicatorOccurence(self) -> str:
        return self.__indicatorOccurence

    @indicatorOccurence.setter
    def indicatorOccurence(self, indicatorOccurence: str):
        self.__indicatorOccurence = indicatorOccurence

    @property
    def numberRangeOccurence(self) -> str:
        return self.__numberRangeOccurence

    @numberRangeOccurence.setter
    def numberRangeOccurence(self, numberRangeOccurence: str):
        self.__numberRangeOccurence = numberRangeOccurence

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def rangeType(self) -> str:
        return self.__rangeType

    @rangeType.setter
    def rangeType(self, rangeType: str):
        self.__rangeType = rangeType

    @property
    def separator(self) -> str:
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator

    @property
    def xal_PremiseNumberRange328(self):
        return self.__xal_PremiseNumberRange328

    @xal_PremiseNumberRange328.setter
    def xal_PremiseNumberRange328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberRange__xal_PremiseNumberRange328", None)
        self.__xal_PremiseNumberRange328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeFrom"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeFrom", None)
                if opp_val == self:
                    setattr(old_value, "xal_PremiseNumberRangeFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeFrom"):
                opp_val = getattr(value, "xal_PremiseNumberRangeFrom", None)
                setattr(value, "xal_PremiseNumberRangeFrom", self)

    @property
    def xal_PremiseNumberRange330(self):
        return self.__xal_PremiseNumberRange330

    @xal_PremiseNumberRange330.setter
    def xal_PremiseNumberRange330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberRange__xal_PremiseNumberRange330", None)
        self.__xal_PremiseNumberRange330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeTo"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeTo", None)
                if opp_val == self:
                    setattr(old_value, "xal_PremiseNumberRangeTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeTo"):
                opp_val = getattr(value, "xal_PremiseNumberRangeTo", None)
                setattr(value, "xal_PremiseNumberRangeTo", self)

    @property
    def xal_PremiseNumberRange(self):
        return self.__xal_PremiseNumberRange

    @xal_PremiseNumberRange.setter
    def xal_PremiseNumberRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberRange__xal_PremiseNumberRange", None)
        self.__xal_PremiseNumberRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise303"):
                opp_val = getattr(old_value, "xal_Premise303", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise303"):
                opp_val = getattr(value, "xal_Premise303", None)
                setattr(value, "xal_Premise303", self)

class xal_PremiseLocation:

    def __init__(self, mixed: str, code: str, anyAttribute: str, xal_PremiseLocation: "xal_Premise" = None):
        self.mixed = mixed
        self.code = code
        self.anyAttribute = anyAttribute
        self.xal_PremiseLocation = xal_PremiseLocation
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PremiseLocation(self):
        return self.__xal_PremiseLocation

    @xal_PremiseLocation.setter
    def xal_PremiseLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseLocation__xal_PremiseLocation", None)
        self.__xal_PremiseLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise298"):
                opp_val = getattr(old_value, "xal_Premise298", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise298"):
                opp_val = getattr(value, "xal_Premise298", None)
                setattr(value, "xal_Premise298", self)

class xal_PremiseName:

    def __init__(self, mixed: str, type: str, typeOccurrence: str, anyAttribute: str, code: str, xal_PremiseName: "xal_Premise" = None):
        self.mixed = mixed
        self.type = type
        self.typeOccurrence = typeOccurrence
        self.anyAttribute = anyAttribute
        self.code = code
        self.xal_PremiseName = xal_PremiseName
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def typeOccurrence(self) -> str:
        return self.__typeOccurrence

    @typeOccurrence.setter
    def typeOccurrence(self, typeOccurrence: str):
        self.__typeOccurrence = typeOccurrence

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PremiseName(self):
        return self.__xal_PremiseName

    @xal_PremiseName.setter
    def xal_PremiseName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseName__xal_PremiseName", None)
        self.__xal_PremiseName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise296"):
                opp_val = getattr(old_value, "xal_Premise296", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise296"):
                opp_val = getattr(value, "xal_Premise296", None)
                if opp_val is None:
                    setattr(value, "xal_Premise296", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostTownSuffix:

    def __init__(self, mixed: str, code: str, anyAttribute: str, xal_PostTownSuffix: "xal_PostTown" = None):
        self.mixed = mixed
        self.code = code
        self.anyAttribute = anyAttribute
        self.xal_PostTownSuffix = xal_PostTownSuffix
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostTownSuffix(self):
        return self.__xal_PostTownSuffix

    @xal_PostTownSuffix.setter
    def xal_PostTownSuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTownSuffix__xal_PostTownSuffix", None)
        self.__xal_PostTownSuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostTown291"):
                opp_val = getattr(old_value, "xal_PostTown291", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostTown291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostTown291"):
                opp_val = getattr(value, "xal_PostTown291", None)
                setattr(value, "xal_PostTown291", self)

class xal_PostTownName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_PostTownName: "xal_PostTown" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostTownName = xal_PostTownName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_PostTownName(self):
        return self.__xal_PostTownName

    @xal_PostTownName.setter
    def xal_PostTownName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTownName__xal_PostTownName", None)
        self.__xal_PostTownName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostTown289"):
                opp_val = getattr(old_value, "xal_PostTown289", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostTown289"):
                opp_val = getattr(value, "xal_PostTown289", None)
                if opp_val is None:
                    setattr(value, "xal_PostTown289", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostOfficeNumber:

    def __init__(self, mixed: str, code: str, indicator: str, indicatorOccurrence: str, anyAttribute: str, xal_PostOfficeNumber: "xal_PostOffice" = None):
        self.mixed = mixed
        self.code = code
        self.indicator = indicator
        self.indicatorOccurrence = indicatorOccurrence
        self.anyAttribute = anyAttribute
        self.xal_PostOfficeNumber = xal_PostOfficeNumber
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def indicatorOccurrence(self) -> str:
        return self.__indicatorOccurrence

    @indicatorOccurrence.setter
    def indicatorOccurrence(self, indicatorOccurrence: str):
        self.__indicatorOccurrence = indicatorOccurrence

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostOfficeNumber(self):
        return self.__xal_PostOfficeNumber

    @xal_PostOfficeNumber.setter
    def xal_PostOfficeNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOfficeNumber__xal_PostOfficeNumber", None)
        self.__xal_PostOfficeNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice275"):
                opp_val = getattr(old_value, "xal_PostOffice275", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice275"):
                opp_val = getattr(value, "xal_PostOffice275", None)
                setattr(value, "xal_PostOffice275", self)

class xal_PostOfficeName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_PostOfficeName: "xal_PostOffice" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostOfficeName = xal_PostOfficeName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostOfficeName(self):
        return self.__xal_PostOfficeName

    @xal_PostOfficeName.setter
    def xal_PostOfficeName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOfficeName__xal_PostOfficeName", None)
        self.__xal_PostOfficeName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice273"):
                opp_val = getattr(old_value, "xal_PostOffice273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice273"):
                opp_val = getattr(value, "xal_PostOffice273", None)
                if opp_val is None:
                    setattr(value, "xal_PostOffice273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostBoxNumberExtension:

    def __init__(self, mixed: str, numberExtensionSeparator: str, anyAttribute: str, xal_PostBoxNumberExtension: "xal_PostBox" = None):
        self.mixed = mixed
        self.numberExtensionSeparator = numberExtensionSeparator
        self.anyAttribute = anyAttribute
        self.xal_PostBoxNumberExtension = xal_PostBoxNumberExtension
        
    @property
    def numberExtensionSeparator(self) -> str:
        return self.__numberExtensionSeparator

    @numberExtensionSeparator.setter
    def numberExtensionSeparator(self, numberExtensionSeparator: str):
        self.__numberExtensionSeparator = numberExtensionSeparator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_PostBoxNumberExtension(self):
        return self.__xal_PostBoxNumberExtension

    @xal_PostBoxNumberExtension.setter
    def xal_PostBoxNumberExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBoxNumberExtension__xal_PostBoxNumberExtension", None)
        self.__xal_PostBoxNumberExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox262"):
                opp_val = getattr(old_value, "xal_PostBox262", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox262"):
                opp_val = getattr(value, "xal_PostBox262", None)
                setattr(value, "xal_PostBox262", self)

class xal_PostBoxNumberSuffix:

    def __init__(self, mixed: str, code: str, numberSuffixSeparator: str, anyAttribute: str, xal_PostBoxNumberSuffix: "xal_PostBox" = None):
        self.mixed = mixed
        self.code = code
        self.numberSuffixSeparator = numberSuffixSeparator
        self.anyAttribute = anyAttribute
        self.xal_PostBoxNumberSuffix = xal_PostBoxNumberSuffix
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberSuffixSeparator(self) -> str:
        return self.__numberSuffixSeparator

    @numberSuffixSeparator.setter
    def numberSuffixSeparator(self, numberSuffixSeparator: str):
        self.__numberSuffixSeparator = numberSuffixSeparator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostBoxNumberSuffix(self):
        return self.__xal_PostBoxNumberSuffix

    @xal_PostBoxNumberSuffix.setter
    def xal_PostBoxNumberSuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBoxNumberSuffix__xal_PostBoxNumberSuffix", None)
        self.__xal_PostBoxNumberSuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox260"):
                opp_val = getattr(old_value, "xal_PostBox260", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox260"):
                opp_val = getattr(value, "xal_PostBox260", None)
                setattr(value, "xal_PostBox260", self)

class xal_PostBoxNumberPrefix:

    def __init__(self, mixed: str, code: str, numberPrefixSeparator: str, anyAttribute: str, xal_PostBoxNumberPrefix: "xal_PostBox" = None):
        self.mixed = mixed
        self.code = code
        self.numberPrefixSeparator = numberPrefixSeparator
        self.anyAttribute = anyAttribute
        self.xal_PostBoxNumberPrefix = xal_PostBoxNumberPrefix
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberPrefixSeparator(self) -> str:
        return self.__numberPrefixSeparator

    @numberPrefixSeparator.setter
    def numberPrefixSeparator(self, numberPrefixSeparator: str):
        self.__numberPrefixSeparator = numberPrefixSeparator

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostBoxNumberPrefix(self):
        return self.__xal_PostBoxNumberPrefix

    @xal_PostBoxNumberPrefix.setter
    def xal_PostBoxNumberPrefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBoxNumberPrefix__xal_PostBoxNumberPrefix", None)
        self.__xal_PostBoxNumberPrefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox258"):
                opp_val = getattr(old_value, "xal_PostBox258", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox258"):
                opp_val = getattr(value, "xal_PostBox258", None)
                setattr(value, "xal_PostBox258", self)

class xal_PostBoxNumber:

    def __init__(self, mixed: str, code: str, anyAttribute: str, xal_PostBoxNumber: "xal_PostBox" = None):
        self.mixed = mixed
        self.code = code
        self.anyAttribute = anyAttribute
        self.xal_PostBoxNumber = xal_PostBoxNumber
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_PostBoxNumber(self):
        return self.__xal_PostBoxNumber

    @xal_PostBoxNumber.setter
    def xal_PostBoxNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBoxNumber__xal_PostBoxNumber", None)
        self.__xal_PostBoxNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox256"):
                opp_val = getattr(old_value, "xal_PostBox256", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox256"):
                opp_val = getattr(value, "xal_PostBox256", None)
                setattr(value, "xal_PostBox256", self)

class xal_SupplementaryPostalServiceData:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_SupplementaryPostalServiceData: "xal_PostalServiceElements" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_SupplementaryPostalServiceData = xal_SupplementaryPostalServiceData
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_SupplementaryPostalServiceData(self):
        return self.__xal_SupplementaryPostalServiceData

    @xal_SupplementaryPostalServiceData.setter
    def xal_SupplementaryPostalServiceData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SupplementaryPostalServiceData__xal_SupplementaryPostalServiceData", None)
        self.__xal_SupplementaryPostalServiceData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements251"):
                opp_val = getattr(old_value, "xal_PostalServiceElements251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements251"):
                opp_val = getattr(value, "xal_PostalServiceElements251", None)
                if opp_val is None:
                    setattr(value, "xal_PostalServiceElements251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_SortingCode:

    def __init__(self, code: str, type: str, xal_SortingCode: "xal_PostalServiceElements" = None):
        self.code = code
        self.type = type
        self.xal_SortingCode = xal_SortingCode
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_SortingCode(self):
        return self.__xal_SortingCode

    @xal_SortingCode.setter
    def xal_SortingCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SortingCode__xal_SortingCode", None)
        self.__xal_SortingCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements241"):
                opp_val = getattr(old_value, "xal_PostalServiceElements241", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements241"):
                opp_val = getattr(value, "xal_PostalServiceElements241", None)
                setattr(value, "xal_PostalServiceElements241", self)

class xal_PostalRouteName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_PostalRouteName: "xal_PostalRoute" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostalRouteName = xal_PostalRouteName
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_PostalRouteName(self):
        return self.__xal_PostalRouteName

    @xal_PostalRouteName.setter
    def xal_PostalRouteName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRouteName__xal_PostalRouteName", None)
        self.__xal_PostalRouteName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute226"):
                opp_val = getattr(old_value, "xal_PostalRoute226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute226"):
                opp_val = getattr(value, "xal_PostalRoute226", None)
                if opp_val is None:
                    setattr(value, "xal_PostalRoute226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostalRouteNumber:

    def __init__(self, code: str, anyAttribute: str, mixed: str, xal_PostalRouteNumber: "xal_PostalRoute" = None):
        self.code = code
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.xal_PostalRouteNumber = xal_PostalRouteNumber
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_PostalRouteNumber(self):
        return self.__xal_PostalRouteNumber

    @xal_PostalRouteNumber.setter
    def xal_PostalRouteNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRouteNumber__xal_PostalRouteNumber", None)
        self.__xal_PostalRouteNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute228"):
                opp_val = getattr(old_value, "xal_PostalRoute228", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRoute228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute228"):
                opp_val = getattr(value, "xal_PostalRoute228", None)
                setattr(value, "xal_PostalRoute228", self)

class xal_PostTown:

    def __init__(self, type: str, anyAttribute: str, xal_PostTown: "xal_PostalCode" = None, xal_PostTown286: set["xal_AddressLine"] = None, xal_PostTown289: set["xal_PostTownName"] = None, xal_PostTown291: "xal_PostTownSuffix" = None):
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostTown = xal_PostTown
        self.xal_PostTown286 = xal_PostTown286 if xal_PostTown286 is not None else set()
        self.xal_PostTown289 = xal_PostTown289 if xal_PostTown289 is not None else set()
        self.xal_PostTown291 = xal_PostTown291
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_PostTown289(self):
        return self.__xal_PostTown289

    @xal_PostTown289.setter
    def xal_PostTown289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTown__xal_PostTown289", None)
        self.__xal_PostTown289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostTownName"):
                    opp_val = getattr(item, "xal_PostTownName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostTownName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostTownName"):
                    opp_val = getattr(item, "xal_PostTownName", None)
                    
                    setattr(item, "xal_PostTownName", self)
                    

    @property
    def xal_PostTown(self):
        return self.__xal_PostTown

    @xal_PostTown.setter
    def xal_PostTown(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTown__xal_PostTown", None)
        self.__xal_PostTown = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode221"):
                opp_val = getattr(old_value, "xal_PostalCode221", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode221"):
                opp_val = getattr(value, "xal_PostalCode221", None)
                setattr(value, "xal_PostalCode221", self)

    @property
    def xal_PostTown286(self):
        return self.__xal_PostTown286

    @xal_PostTown286.setter
    def xal_PostTown286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTown__xal_PostTown286", None)
        self.__xal_PostTown286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine287"):
                    opp_val = getattr(item, "xal_AddressLine287", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine287"):
                    opp_val = getattr(item, "xal_AddressLine287", None)
                    
                    setattr(item, "xal_AddressLine287", self)
                    

    @property
    def xal_PostTown291(self):
        return self.__xal_PostTown291

    @xal_PostTown291.setter
    def xal_PostTown291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostTown__xal_PostTown291", None)
        self.__xal_PostTown291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostTownSuffix"):
                opp_val = getattr(old_value, "xal_PostTownSuffix", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostTownSuffix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostTownSuffix"):
                opp_val = getattr(value, "xal_PostTownSuffix", None)
                setattr(value, "xal_PostTownSuffix", self)

class xal_PostalCodeNumberExtension:

    def __init__(self, mixed: str, code: str, numberExtensionSeparator: str, type: str, anyAttribute: str, xal_PostalCodeNumberExtension: "xal_PostalCode" = None):
        self.mixed = mixed
        self.code = code
        self.numberExtensionSeparator = numberExtensionSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostalCodeNumberExtension = xal_PostalCodeNumberExtension
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def numberExtensionSeparator(self) -> str:
        return self.__numberExtensionSeparator

    @numberExtensionSeparator.setter
    def numberExtensionSeparator(self, numberExtensionSeparator: str):
        self.__numberExtensionSeparator = numberExtensionSeparator

    @property
    def xal_PostalCodeNumberExtension(self):
        return self.__xal_PostalCodeNumberExtension

    @xal_PostalCodeNumberExtension.setter
    def xal_PostalCodeNumberExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCodeNumberExtension__xal_PostalCodeNumberExtension", None)
        self.__xal_PostalCodeNumberExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode219"):
                opp_val = getattr(old_value, "xal_PostalCode219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode219"):
                opp_val = getattr(value, "xal_PostalCode219", None)
                if opp_val is None:
                    setattr(value, "xal_PostalCode219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostalCodeNumber:

    def __init__(self, code: str, type: str, anyAttribute: str, mixed: str, xal_PostalCodeNumber: "xal_PostalCode" = None):
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.xal_PostalCodeNumber = xal_PostalCodeNumber
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_PostalCodeNumber(self):
        return self.__xal_PostalCodeNumber

    @xal_PostalCodeNumber.setter
    def xal_PostalCodeNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCodeNumber__xal_PostalCodeNumber", None)
        self.__xal_PostalCodeNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode217"):
                opp_val = getattr(old_value, "xal_PostalCode217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode217"):
                opp_val = getattr(value, "xal_PostalCode217", None)
                if opp_val is None:
                    setattr(value, "xal_PostalCode217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_MailStopNumber:

    def __init__(self, mixed: str, code: str, nameNumberSeparator: str, anyAttribute: str, xal_MailStopNumber: "xal_MailStop" = None):
        self.mixed = mixed
        self.code = code
        self.nameNumberSeparator = nameNumberSeparator
        self.anyAttribute = anyAttribute
        self.xal_MailStopNumber = xal_MailStopNumber
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def nameNumberSeparator(self) -> str:
        return self.__nameNumberSeparator

    @nameNumberSeparator.setter
    def nameNumberSeparator(self, nameNumberSeparator: str):
        self.__nameNumberSeparator = nameNumberSeparator

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_MailStopNumber(self):
        return self.__xal_MailStopNumber

    @xal_MailStopNumber.setter
    def xal_MailStopNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStopNumber__xal_MailStopNumber", None)
        self.__xal_MailStopNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop212"):
                opp_val = getattr(old_value, "xal_MailStop212", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop212"):
                opp_val = getattr(value, "xal_MailStop212", None)
                setattr(value, "xal_MailStop212", self)

class xal_MailStopName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_MailStopName: "xal_MailStop" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_MailStopName = xal_MailStopName
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_MailStopName(self):
        return self.__xal_MailStopName

    @xal_MailStopName.setter
    def xal_MailStopName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStopName__xal_MailStopName", None)
        self.__xal_MailStopName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop210"):
                opp_val = getattr(old_value, "xal_MailStop210", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop210"):
                opp_val = getattr(value, "xal_MailStop210", None)
                setattr(value, "xal_MailStop210", self)

class xal_LocalityName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_LocalityName: "xal_Locality" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_LocalityName = xal_LocalityName
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_LocalityName(self):
        return self.__xal_LocalityName

    @xal_LocalityName.setter
    def xal_LocalityName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LocalityName__xal_LocalityName", None)
        self.__xal_LocalityName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality181"):
                opp_val = getattr(old_value, "xal_Locality181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality181"):
                opp_val = getattr(value, "xal_Locality181", None)
                if opp_val is None:
                    setattr(value, "xal_Locality181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_LargeMailUserIdentifier:

    def __init__(self, mixed: str, code: str, indicator: str, anyAttribute: str, type: str, xal_LargeMailUserIdentifier: "xal_LargeMailUser" = None):
        self.mixed = mixed
        self.code = code
        self.indicator = indicator
        self.anyAttribute = anyAttribute
        self.type = type
        self.xal_LargeMailUserIdentifier = xal_LargeMailUserIdentifier
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_LargeMailUserIdentifier(self):
        return self.__xal_LargeMailUserIdentifier

    @xal_LargeMailUserIdentifier.setter
    def xal_LargeMailUserIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUserIdentifier__xal_LargeMailUserIdentifier", None)
        self.__xal_LargeMailUserIdentifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser162"):
                opp_val = getattr(old_value, "xal_LargeMailUser162", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser162"):
                opp_val = getattr(value, "xal_LargeMailUser162", None)
                setattr(value, "xal_LargeMailUser162", self)

class xal_LargeMailUserName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_LargeMailUserName: "xal_LargeMailUser" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_LargeMailUserName = xal_LargeMailUserName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_LargeMailUserName(self):
        return self.__xal_LargeMailUserName

    @xal_LargeMailUserName.setter
    def xal_LargeMailUserName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUserName__xal_LargeMailUserName", None)
        self.__xal_LargeMailUserName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser160"):
                opp_val = getattr(old_value, "xal_LargeMailUser160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser160"):
                opp_val = getattr(value, "xal_LargeMailUser160", None)
                if opp_val is None:
                    setattr(value, "xal_LargeMailUser160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_KeyLineCode:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_KeyLineCode: "xal_PostalServiceElements" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_KeyLineCode = xal_KeyLineCode
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_KeyLineCode(self):
        return self.__xal_KeyLineCode

    @xal_KeyLineCode.setter
    def xal_KeyLineCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_KeyLineCode__xal_KeyLineCode", None)
        self.__xal_KeyLineCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements237"):
                opp_val = getattr(old_value, "xal_PostalServiceElements237", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements237"):
                opp_val = getattr(value, "xal_PostalServiceElements237", None)
                setattr(value, "xal_PostalServiceElements237", self)

class xal_EndorsementLineCode:

    def __init__(self, anyAttribute: str, mixed: str, code: str, type: str, xal_EndorsementLineCode: "xal_PostalServiceElements" = None):
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.code = code
        self.type = type
        self.xal_EndorsementLineCode = xal_EndorsementLineCode
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_EndorsementLineCode(self):
        return self.__xal_EndorsementLineCode

    @xal_EndorsementLineCode.setter
    def xal_EndorsementLineCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_EndorsementLineCode__xal_EndorsementLineCode", None)
        self.__xal_EndorsementLineCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements235"):
                opp_val = getattr(old_value, "xal_PostalServiceElements235", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements235"):
                opp_val = getattr(value, "xal_PostalServiceElements235", None)
                setattr(value, "xal_PostalServiceElements235", self)

class xal_Xal:

    def __init__(self, version: str, anyAttribute: str, any: str, xal_Xal: "xal_DocumentRoot" = None, xal_Xal473: set["xal_AddressDetails"] = None):
        self.version = version
        self.anyAttribute = anyAttribute
        self.any = any
        self.xal_Xal = xal_Xal
        self.xal_Xal473 = xal_Xal473 if xal_Xal473 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_Xal473(self):
        return self.__xal_Xal473

    @xal_Xal473.setter
    def xal_Xal473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Xal__xal_Xal473", None)
        self.__xal_Xal473 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressDetails474"):
                    opp_val = getattr(item, "xal_AddressDetails474", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressDetails474", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressDetails474"):
                    opp_val = getattr(item, "xal_AddressDetails474", None)
                    
                    setattr(item, "xal_AddressDetails474", self)
                    

    @property
    def xal_Xal(self):
        return self.__xal_Xal

    @xal_Xal.setter
    def xal_Xal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Xal__xal_Xal", None)
        self.__xal_Xal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot142"):
                opp_val = getattr(old_value, "xal_DocumentRoot142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot142"):
                opp_val = getattr(value, "xal_DocumentRoot142", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_FirmName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_FirmName: "xal_Firm" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_FirmName = xal_FirmName
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_FirmName(self):
        return self.__xal_FirmName

    @xal_FirmName.setter
    def xal_FirmName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_FirmName__xal_FirmName", None)
        self.__xal_FirmName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm146"):
                opp_val = getattr(old_value, "xal_Firm146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm146"):
                opp_val = getattr(value, "xal_Firm146", None)
                if opp_val is None:
                    setattr(value, "xal_Firm146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_Firm:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_Firm: set["xal_AddressLine"] = None, xal_Firm146: set["xal_FirmName"] = None, xal_Firm148: set["xal_Department"] = None, xal_Firm151: "xal_MailStop" = None, xal_Firm154: "xal_PostalCode" = None, xal_Firm265: "xal_PostBox" = None, xal_Firm317: "xal_Premise" = None, xal_Firm387: "xal_SubPremise" = None, xal_Firm437: "xal_Thoroughfare" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_Firm = xal_Firm if xal_Firm is not None else set()
        self.xal_Firm146 = xal_Firm146 if xal_Firm146 is not None else set()
        self.xal_Firm148 = xal_Firm148 if xal_Firm148 is not None else set()
        self.xal_Firm151 = xal_Firm151
        self.xal_Firm154 = xal_Firm154
        self.xal_Firm265 = xal_Firm265
        self.xal_Firm317 = xal_Firm317
        self.xal_Firm387 = xal_Firm387
        self.xal_Firm437 = xal_Firm437
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_Firm151(self):
        return self.__xal_Firm151

    @xal_Firm151.setter
    def xal_Firm151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm151", None)
        self.__xal_Firm151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop152"):
                opp_val = getattr(old_value, "xal_MailStop152", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop152"):
                opp_val = getattr(value, "xal_MailStop152", None)
                setattr(value, "xal_MailStop152", self)

    @property
    def xal_Firm146(self):
        return self.__xal_Firm146

    @xal_Firm146.setter
    def xal_Firm146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm146", None)
        self.__xal_Firm146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_FirmName"):
                    opp_val = getattr(item, "xal_FirmName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_FirmName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_FirmName"):
                    opp_val = getattr(item, "xal_FirmName", None)
                    
                    setattr(item, "xal_FirmName", self)
                    

    @property
    def xal_Firm148(self):
        return self.__xal_Firm148

    @xal_Firm148.setter
    def xal_Firm148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm148", None)
        self.__xal_Firm148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Department149"):
                    opp_val = getattr(item, "xal_Department149", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Department149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Department149"):
                    opp_val = getattr(item, "xal_Department149", None)
                    
                    setattr(item, "xal_Department149", self)
                    

    @property
    def xal_Firm387(self):
        return self.__xal_Firm387

    @xal_Firm387.setter
    def xal_Firm387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm387", None)
        self.__xal_Firm387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise386"):
                opp_val = getattr(old_value, "xal_SubPremise386", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise386", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise386"):
                opp_val = getattr(value, "xal_SubPremise386", None)
                setattr(value, "xal_SubPremise386", self)

    @property
    def xal_Firm437(self):
        return self.__xal_Firm437

    @xal_Firm437.setter
    def xal_Firm437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm437", None)
        self.__xal_Firm437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare436"):
                opp_val = getattr(old_value, "xal_Thoroughfare436", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare436"):
                opp_val = getattr(value, "xal_Thoroughfare436", None)
                setattr(value, "xal_Thoroughfare436", self)

    @property
    def xal_Firm317(self):
        return self.__xal_Firm317

    @xal_Firm317.setter
    def xal_Firm317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm317", None)
        self.__xal_Firm317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise316"):
                opp_val = getattr(old_value, "xal_Premise316", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise316"):
                opp_val = getattr(value, "xal_Premise316", None)
                setattr(value, "xal_Premise316", self)

    @property
    def xal_Firm265(self):
        return self.__xal_Firm265

    @xal_Firm265.setter
    def xal_Firm265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm265", None)
        self.__xal_Firm265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox264"):
                opp_val = getattr(old_value, "xal_PostBox264", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox264"):
                opp_val = getattr(value, "xal_PostBox264", None)
                setattr(value, "xal_PostBox264", self)

    @property
    def xal_Firm154(self):
        return self.__xal_Firm154

    @xal_Firm154.setter
    def xal_Firm154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm154", None)
        self.__xal_Firm154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode155"):
                opp_val = getattr(old_value, "xal_PostalCode155", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode155"):
                opp_val = getattr(value, "xal_PostalCode155", None)
                setattr(value, "xal_PostalCode155", self)

    @property
    def xal_Firm(self):
        return self.__xal_Firm

    @xal_Firm.setter
    def xal_Firm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Firm__xal_Firm", None)
        self.__xal_Firm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine144"):
                    opp_val = getattr(item, "xal_AddressLine144", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine144"):
                    opp_val = getattr(item, "xal_AddressLine144", None)
                    
                    setattr(item, "xal_AddressLine144", self)
                    

class xal_PremiseNumberSuffix:

    def __init__(self, mixed: str, code: str, numberSuffixSeparator: str, type: str, anyAttribute: str, xal_PremiseNumberSuffix: "xal_DocumentRoot" = None, xal_PremiseNumberSuffix309: "xal_Premise" = None, xal_PremiseNumberSuffix342: "xal_PremiseNumberRangeFrom" = None, xal_PremiseNumberSuffix354: "xal_PremiseNumberRangeTo" = None):
        self.mixed = mixed
        self.code = code
        self.numberSuffixSeparator = numberSuffixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PremiseNumberSuffix = xal_PremiseNumberSuffix
        self.xal_PremiseNumberSuffix309 = xal_PremiseNumberSuffix309
        self.xal_PremiseNumberSuffix342 = xal_PremiseNumberSuffix342
        self.xal_PremiseNumberSuffix354 = xal_PremiseNumberSuffix354
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberSuffixSeparator(self) -> str:
        return self.__numberSuffixSeparator

    @numberSuffixSeparator.setter
    def numberSuffixSeparator(self, numberSuffixSeparator: str):
        self.__numberSuffixSeparator = numberSuffixSeparator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_PremiseNumberSuffix354(self):
        return self.__xal_PremiseNumberSuffix354

    @xal_PremiseNumberSuffix354.setter
    def xal_PremiseNumberSuffix354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberSuffix__xal_PremiseNumberSuffix354", None)
        self.__xal_PremiseNumberSuffix354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeTo353"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeTo353", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeTo353"):
                opp_val = getattr(value, "xal_PremiseNumberRangeTo353", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeTo353", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberSuffix(self):
        return self.__xal_PremiseNumberSuffix

    @xal_PremiseNumberSuffix.setter
    def xal_PremiseNumberSuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberSuffix__xal_PremiseNumberSuffix", None)
        self.__xal_PremiseNumberSuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot131"):
                opp_val = getattr(old_value, "xal_DocumentRoot131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot131"):
                opp_val = getattr(value, "xal_DocumentRoot131", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberSuffix342(self):
        return self.__xal_PremiseNumberSuffix342

    @xal_PremiseNumberSuffix342.setter
    def xal_PremiseNumberSuffix342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberSuffix__xal_PremiseNumberSuffix342", None)
        self.__xal_PremiseNumberSuffix342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeFrom341"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeFrom341", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeFrom341"):
                opp_val = getattr(value, "xal_PremiseNumberRangeFrom341", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeFrom341", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberSuffix309(self):
        return self.__xal_PremiseNumberSuffix309

    @xal_PremiseNumberSuffix309.setter
    def xal_PremiseNumberSuffix309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberSuffix__xal_PremiseNumberSuffix309", None)
        self.__xal_PremiseNumberSuffix309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise308"):
                opp_val = getattr(old_value, "xal_Premise308", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise308"):
                opp_val = getattr(value, "xal_Premise308", None)
                if opp_val is None:
                    setattr(value, "xal_Premise308", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PremiseNumberPrefix:

    def __init__(self, value: str, code: str, numberPrefixSeparator: str, type: str, anyAttribute: str, xal_PremiseNumberPrefix: "xal_DocumentRoot" = None, xal_PremiseNumberPrefix306: "xal_Premise" = None, xal_PremiseNumberPrefix336: "xal_PremiseNumberRangeFrom" = None, xal_PremiseNumberPrefix348: "xal_PremiseNumberRangeTo" = None):
        self.value = value
        self.code = code
        self.numberPrefixSeparator = numberPrefixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PremiseNumberPrefix = xal_PremiseNumberPrefix
        self.xal_PremiseNumberPrefix306 = xal_PremiseNumberPrefix306
        self.xal_PremiseNumberPrefix336 = xal_PremiseNumberPrefix336
        self.xal_PremiseNumberPrefix348 = xal_PremiseNumberPrefix348
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def numberPrefixSeparator(self) -> str:
        return self.__numberPrefixSeparator

    @numberPrefixSeparator.setter
    def numberPrefixSeparator(self, numberPrefixSeparator: str):
        self.__numberPrefixSeparator = numberPrefixSeparator

    @property
    def xal_PremiseNumberPrefix306(self):
        return self.__xal_PremiseNumberPrefix306

    @xal_PremiseNumberPrefix306.setter
    def xal_PremiseNumberPrefix306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberPrefix__xal_PremiseNumberPrefix306", None)
        self.__xal_PremiseNumberPrefix306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise305"):
                opp_val = getattr(old_value, "xal_Premise305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise305"):
                opp_val = getattr(value, "xal_Premise305", None)
                if opp_val is None:
                    setattr(value, "xal_Premise305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberPrefix336(self):
        return self.__xal_PremiseNumberPrefix336

    @xal_PremiseNumberPrefix336.setter
    def xal_PremiseNumberPrefix336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberPrefix__xal_PremiseNumberPrefix336", None)
        self.__xal_PremiseNumberPrefix336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeFrom335"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeFrom335", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeFrom335"):
                opp_val = getattr(value, "xal_PremiseNumberRangeFrom335", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeFrom335", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberPrefix348(self):
        return self.__xal_PremiseNumberPrefix348

    @xal_PremiseNumberPrefix348.setter
    def xal_PremiseNumberPrefix348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberPrefix__xal_PremiseNumberPrefix348", None)
        self.__xal_PremiseNumberPrefix348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeTo347"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeTo347", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeTo347"):
                opp_val = getattr(value, "xal_PremiseNumberRangeTo347", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeTo347", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumberPrefix(self):
        return self.__xal_PremiseNumberPrefix

    @xal_PremiseNumberPrefix.setter
    def xal_PremiseNumberPrefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumberPrefix__xal_PremiseNumberPrefix", None)
        self.__xal_PremiseNumberPrefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot129"):
                opp_val = getattr(old_value, "xal_DocumentRoot129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot129"):
                opp_val = getattr(value, "xal_DocumentRoot129", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PremiseNumber:

    def __init__(self, mixed: str, code: str, indicator: str, indicatorOccurrence: str, numberType: str, numberTypeOccurrence: str, type: str, anyAttribute: str, xal_PremiseNumber: "xal_DocumentRoot" = None, xal_PremiseNumber301: "xal_Premise" = None, xal_PremiseNumber351: "xal_PremiseNumberRangeTo" = None, xal_PremiseNumber339: "xal_PremiseNumberRangeFrom" = None):
        self.mixed = mixed
        self.code = code
        self.indicator = indicator
        self.indicatorOccurrence = indicatorOccurrence
        self.numberType = numberType
        self.numberTypeOccurrence = numberTypeOccurrence
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PremiseNumber = xal_PremiseNumber
        self.xal_PremiseNumber301 = xal_PremiseNumber301
        self.xal_PremiseNumber351 = xal_PremiseNumber351
        self.xal_PremiseNumber339 = xal_PremiseNumber339
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def numberType(self) -> str:
        return self.__numberType

    @numberType.setter
    def numberType(self, numberType: str):
        self.__numberType = numberType

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numberTypeOccurrence(self) -> str:
        return self.__numberTypeOccurrence

    @numberTypeOccurrence.setter
    def numberTypeOccurrence(self, numberTypeOccurrence: str):
        self.__numberTypeOccurrence = numberTypeOccurrence

    @property
    def indicatorOccurrence(self) -> str:
        return self.__indicatorOccurrence

    @indicatorOccurrence.setter
    def indicatorOccurrence(self, indicatorOccurrence: str):
        self.__indicatorOccurrence = indicatorOccurrence

    @property
    def xal_PremiseNumber339(self):
        return self.__xal_PremiseNumber339

    @xal_PremiseNumber339.setter
    def xal_PremiseNumber339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumber__xal_PremiseNumber339", None)
        self.__xal_PremiseNumber339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeFrom338"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeFrom338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeFrom338"):
                opp_val = getattr(value, "xal_PremiseNumberRangeFrom338", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeFrom338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumber(self):
        return self.__xal_PremiseNumber

    @xal_PremiseNumber.setter
    def xal_PremiseNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumber__xal_PremiseNumber", None)
        self.__xal_PremiseNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot127"):
                opp_val = getattr(old_value, "xal_DocumentRoot127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot127"):
                opp_val = getattr(value, "xal_DocumentRoot127", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumber301(self):
        return self.__xal_PremiseNumber301

    @xal_PremiseNumber301.setter
    def xal_PremiseNumber301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumber__xal_PremiseNumber301", None)
        self.__xal_PremiseNumber301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise300"):
                opp_val = getattr(old_value, "xal_Premise300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise300"):
                opp_val = getattr(value, "xal_Premise300", None)
                if opp_val is None:
                    setattr(value, "xal_Premise300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PremiseNumber351(self):
        return self.__xal_PremiseNumber351

    @xal_PremiseNumber351.setter
    def xal_PremiseNumber351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PremiseNumber__xal_PremiseNumber351", None)
        self.__xal_PremiseNumber351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeTo350"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeTo350", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeTo350"):
                opp_val = getattr(value, "xal_PremiseNumberRangeTo350", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeTo350", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_ThoroughfareNumberSuffix:

    def __init__(self, mixed: str, code: str, numberSuffixSeparator: str, type: str, anyAttribute: str, xal_ThoroughfareNumberSuffix: "xal_DocumentRoot" = None, xal_ThoroughfareNumberSuffix410: "xal_Thoroughfare" = None, xal_ThoroughfareNumberSuffix451: "xal_ThoroughfareNumberFrom" = None, xal_ThoroughfareNumberSuffix471: "xal_ThoroughfareNumberTo" = None):
        self.mixed = mixed
        self.code = code
        self.numberSuffixSeparator = numberSuffixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareNumberSuffix = xal_ThoroughfareNumberSuffix
        self.xal_ThoroughfareNumberSuffix410 = xal_ThoroughfareNumberSuffix410
        self.xal_ThoroughfareNumberSuffix451 = xal_ThoroughfareNumberSuffix451
        self.xal_ThoroughfareNumberSuffix471 = xal_ThoroughfareNumberSuffix471
        
    @property
    def numberSuffixSeparator(self) -> str:
        return self.__numberSuffixSeparator

    @numberSuffixSeparator.setter
    def numberSuffixSeparator(self, numberSuffixSeparator: str):
        self.__numberSuffixSeparator = numberSuffixSeparator

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_ThoroughfareNumberSuffix451(self):
        return self.__xal_ThoroughfareNumberSuffix451

    @xal_ThoroughfareNumberSuffix451.setter
    def xal_ThoroughfareNumberSuffix451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberSuffix__xal_ThoroughfareNumberSuffix451", None)
        self.__xal_ThoroughfareNumberSuffix451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberFrom450"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberFrom450", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberFrom450"):
                opp_val = getattr(value, "xal_ThoroughfareNumberFrom450", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberFrom450", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberSuffix471(self):
        return self.__xal_ThoroughfareNumberSuffix471

    @xal_ThoroughfareNumberSuffix471.setter
    def xal_ThoroughfareNumberSuffix471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberSuffix__xal_ThoroughfareNumberSuffix471", None)
        self.__xal_ThoroughfareNumberSuffix471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberTo470"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberTo470", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberTo470"):
                opp_val = getattr(value, "xal_ThoroughfareNumberTo470", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberTo470", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberSuffix(self):
        return self.__xal_ThoroughfareNumberSuffix

    @xal_ThoroughfareNumberSuffix.setter
    def xal_ThoroughfareNumberSuffix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberSuffix__xal_ThoroughfareNumberSuffix", None)
        self.__xal_ThoroughfareNumberSuffix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot140"):
                opp_val = getattr(old_value, "xal_DocumentRoot140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot140"):
                opp_val = getattr(value, "xal_DocumentRoot140", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberSuffix410(self):
        return self.__xal_ThoroughfareNumberSuffix410

    @xal_ThoroughfareNumberSuffix410.setter
    def xal_ThoroughfareNumberSuffix410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberSuffix__xal_ThoroughfareNumberSuffix410", None)
        self.__xal_ThoroughfareNumberSuffix410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare409"):
                opp_val = getattr(old_value, "xal_Thoroughfare409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare409"):
                opp_val = getattr(value, "xal_Thoroughfare409", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_ThoroughfareNumberPrefix:

    def __init__(self, mixed: str, numberPrefixSeparator: str, type: str, anyAttribute: str, code: str, xal_ThoroughfareNumberPrefix: "xal_DocumentRoot" = None, xal_ThoroughfareNumberPrefix407: "xal_Thoroughfare" = None, xal_ThoroughfareNumberPrefix445: "xal_ThoroughfareNumberFrom" = None, xal_ThoroughfareNumberPrefix465: "xal_ThoroughfareNumberTo" = None):
        self.mixed = mixed
        self.numberPrefixSeparator = numberPrefixSeparator
        self.type = type
        self.anyAttribute = anyAttribute
        self.code = code
        self.xal_ThoroughfareNumberPrefix = xal_ThoroughfareNumberPrefix
        self.xal_ThoroughfareNumberPrefix407 = xal_ThoroughfareNumberPrefix407
        self.xal_ThoroughfareNumberPrefix445 = xal_ThoroughfareNumberPrefix445
        self.xal_ThoroughfareNumberPrefix465 = xal_ThoroughfareNumberPrefix465
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def numberPrefixSeparator(self) -> str:
        return self.__numberPrefixSeparator

    @numberPrefixSeparator.setter
    def numberPrefixSeparator(self, numberPrefixSeparator: str):
        self.__numberPrefixSeparator = numberPrefixSeparator

    @property
    def xal_ThoroughfareNumberPrefix465(self):
        return self.__xal_ThoroughfareNumberPrefix465

    @xal_ThoroughfareNumberPrefix465.setter
    def xal_ThoroughfareNumberPrefix465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberPrefix__xal_ThoroughfareNumberPrefix465", None)
        self.__xal_ThoroughfareNumberPrefix465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberTo464"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberTo464", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberTo464"):
                opp_val = getattr(value, "xal_ThoroughfareNumberTo464", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberTo464", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberPrefix(self):
        return self.__xal_ThoroughfareNumberPrefix

    @xal_ThoroughfareNumberPrefix.setter
    def xal_ThoroughfareNumberPrefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberPrefix__xal_ThoroughfareNumberPrefix", None)
        self.__xal_ThoroughfareNumberPrefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot138"):
                opp_val = getattr(old_value, "xal_DocumentRoot138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot138"):
                opp_val = getattr(value, "xal_DocumentRoot138", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberPrefix445(self):
        return self.__xal_ThoroughfareNumberPrefix445

    @xal_ThoroughfareNumberPrefix445.setter
    def xal_ThoroughfareNumberPrefix445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberPrefix__xal_ThoroughfareNumberPrefix445", None)
        self.__xal_ThoroughfareNumberPrefix445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberFrom444"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberFrom444", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberFrom444"):
                opp_val = getattr(value, "xal_ThoroughfareNumberFrom444", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberFrom444", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumberPrefix407(self):
        return self.__xal_ThoroughfareNumberPrefix407

    @xal_ThoroughfareNumberPrefix407.setter
    def xal_ThoroughfareNumberPrefix407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumberPrefix__xal_ThoroughfareNumberPrefix407", None)
        self.__xal_ThoroughfareNumberPrefix407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare406"):
                opp_val = getattr(old_value, "xal_Thoroughfare406", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare406"):
                opp_val = getattr(value, "xal_Thoroughfare406", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare406", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_ThoroughfareNumber:

    def __init__(self, code: str, indicator: str, indicatorOccurrence: str, numberOccurrence: str, numberType: str, mixed: str, type: str, anyAttribute: str, xal_ThoroughfareNumber: "xal_DocumentRoot" = None, xal_ThoroughfareNumber402: "xal_Thoroughfare" = None, xal_ThoroughfareNumber448: "xal_ThoroughfareNumberFrom" = None, xal_ThoroughfareNumber468: "xal_ThoroughfareNumberTo" = None):
        self.code = code
        self.indicator = indicator
        self.indicatorOccurrence = indicatorOccurrence
        self.numberOccurrence = numberOccurrence
        self.numberType = numberType
        self.mixed = mixed
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareNumber = xal_ThoroughfareNumber
        self.xal_ThoroughfareNumber402 = xal_ThoroughfareNumber402
        self.xal_ThoroughfareNumber448 = xal_ThoroughfareNumber448
        self.xal_ThoroughfareNumber468 = xal_ThoroughfareNumber468
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def indicatorOccurrence(self) -> str:
        return self.__indicatorOccurrence

    @indicatorOccurrence.setter
    def indicatorOccurrence(self, indicatorOccurrence: str):
        self.__indicatorOccurrence = indicatorOccurrence

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def numberType(self) -> str:
        return self.__numberType

    @numberType.setter
    def numberType(self, numberType: str):
        self.__numberType = numberType

    @property
    def numberOccurrence(self) -> str:
        return self.__numberOccurrence

    @numberOccurrence.setter
    def numberOccurrence(self, numberOccurrence: str):
        self.__numberOccurrence = numberOccurrence

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_ThoroughfareNumber(self):
        return self.__xal_ThoroughfareNumber

    @xal_ThoroughfareNumber.setter
    def xal_ThoroughfareNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumber__xal_ThoroughfareNumber", None)
        self.__xal_ThoroughfareNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot136"):
                opp_val = getattr(old_value, "xal_DocumentRoot136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot136"):
                opp_val = getattr(value, "xal_DocumentRoot136", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumber448(self):
        return self.__xal_ThoroughfareNumber448

    @xal_ThoroughfareNumber448.setter
    def xal_ThoroughfareNumber448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumber__xal_ThoroughfareNumber448", None)
        self.__xal_ThoroughfareNumber448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberFrom447"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberFrom447", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberFrom447"):
                opp_val = getattr(value, "xal_ThoroughfareNumberFrom447", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberFrom447", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumber402(self):
        return self.__xal_ThoroughfareNumber402

    @xal_ThoroughfareNumber402.setter
    def xal_ThoroughfareNumber402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumber__xal_ThoroughfareNumber402", None)
        self.__xal_ThoroughfareNumber402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare401"):
                opp_val = getattr(old_value, "xal_Thoroughfare401", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare401"):
                opp_val = getattr(value, "xal_Thoroughfare401", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare401", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareNumber468(self):
        return self.__xal_ThoroughfareNumber468

    @xal_ThoroughfareNumber468.setter
    def xal_ThoroughfareNumber468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareNumber__xal_ThoroughfareNumber468", None)
        self.__xal_ThoroughfareNumber468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberTo467"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberTo467", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberTo467"):
                opp_val = getattr(value, "xal_ThoroughfareNumberTo467", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberTo467", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_DocumentRoot:

    def __init__(self, mixed: str, xal_DocumentRoot: set["xal_EStringToStringMapEntry"] = None, xal_DocumentRoot94: set["xal_EStringToStringMapEntry"] = None, xal_DocumentRoot97: set["xal_AddressDetails"] = None, xal_DocumentRoot100: set["xal_AddressLine"] = None, xal_DocumentRoot103: set["xal_AdministrativeArea"] = None, xal_DocumentRoot115: set["xal_PostalCode"] = None, xal_DocumentRoot118: set["xal_PostBox"] = None, xal_DocumentRoot121: set["xal_PostOffice"] = None, xal_DocumentRoot124: set["xal_Premise"] = None, xal_DocumentRoot106: set["xal_CountryName"] = None, xal_DocumentRoot109: set["xal_Department"] = None, xal_DocumentRoot112: set["xal_Locality"] = None, xal_DocumentRoot133: set["xal_Thoroughfare"] = None, xal_DocumentRoot136: set["xal_ThoroughfareNumber"] = None, xal_DocumentRoot138: set["xal_ThoroughfareNumberPrefix"] = None, xal_DocumentRoot140: set["xal_ThoroughfareNumberSuffix"] = None, xal_DocumentRoot127: set["xal_PremiseNumber"] = None, xal_DocumentRoot129: set["xal_PremiseNumberPrefix"] = None, xal_DocumentRoot131: set["xal_PremiseNumberSuffix"] = None, xal_DocumentRoot142: set["xal_Xal"] = None):
        self.mixed = mixed
        self.xal_DocumentRoot = xal_DocumentRoot if xal_DocumentRoot is not None else set()
        self.xal_DocumentRoot94 = xal_DocumentRoot94 if xal_DocumentRoot94 is not None else set()
        self.xal_DocumentRoot97 = xal_DocumentRoot97 if xal_DocumentRoot97 is not None else set()
        self.xal_DocumentRoot100 = xal_DocumentRoot100 if xal_DocumentRoot100 is not None else set()
        self.xal_DocumentRoot103 = xal_DocumentRoot103 if xal_DocumentRoot103 is not None else set()
        self.xal_DocumentRoot115 = xal_DocumentRoot115 if xal_DocumentRoot115 is not None else set()
        self.xal_DocumentRoot118 = xal_DocumentRoot118 if xal_DocumentRoot118 is not None else set()
        self.xal_DocumentRoot121 = xal_DocumentRoot121 if xal_DocumentRoot121 is not None else set()
        self.xal_DocumentRoot124 = xal_DocumentRoot124 if xal_DocumentRoot124 is not None else set()
        self.xal_DocumentRoot106 = xal_DocumentRoot106 if xal_DocumentRoot106 is not None else set()
        self.xal_DocumentRoot109 = xal_DocumentRoot109 if xal_DocumentRoot109 is not None else set()
        self.xal_DocumentRoot112 = xal_DocumentRoot112 if xal_DocumentRoot112 is not None else set()
        self.xal_DocumentRoot133 = xal_DocumentRoot133 if xal_DocumentRoot133 is not None else set()
        self.xal_DocumentRoot136 = xal_DocumentRoot136 if xal_DocumentRoot136 is not None else set()
        self.xal_DocumentRoot138 = xal_DocumentRoot138 if xal_DocumentRoot138 is not None else set()
        self.xal_DocumentRoot140 = xal_DocumentRoot140 if xal_DocumentRoot140 is not None else set()
        self.xal_DocumentRoot127 = xal_DocumentRoot127 if xal_DocumentRoot127 is not None else set()
        self.xal_DocumentRoot129 = xal_DocumentRoot129 if xal_DocumentRoot129 is not None else set()
        self.xal_DocumentRoot131 = xal_DocumentRoot131 if xal_DocumentRoot131 is not None else set()
        self.xal_DocumentRoot142 = xal_DocumentRoot142 if xal_DocumentRoot142 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_DocumentRoot(self):
        return self.__xal_DocumentRoot

    @xal_DocumentRoot.setter
    def xal_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot", None)
        self.__xal_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xal_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xal_EStringToStringMapEntry", None)
                    
                    setattr(item, "xal_EStringToStringMapEntry", self)
                    

    @property
    def xal_DocumentRoot106(self):
        return self.__xal_DocumentRoot106

    @xal_DocumentRoot106.setter
    def xal_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot106", None)
        self.__xal_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_CountryName107"):
                    opp_val = getattr(item, "xal_CountryName107", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_CountryName107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_CountryName107"):
                    opp_val = getattr(item, "xal_CountryName107", None)
                    
                    setattr(item, "xal_CountryName107", self)
                    

    @property
    def xal_DocumentRoot142(self):
        return self.__xal_DocumentRoot142

    @xal_DocumentRoot142.setter
    def xal_DocumentRoot142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot142", None)
        self.__xal_DocumentRoot142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Xal"):
                    opp_val = getattr(item, "xal_Xal", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Xal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Xal"):
                    opp_val = getattr(item, "xal_Xal", None)
                    
                    setattr(item, "xal_Xal", self)
                    

    @property
    def xal_DocumentRoot100(self):
        return self.__xal_DocumentRoot100

    @xal_DocumentRoot100.setter
    def xal_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot100", None)
        self.__xal_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine101"):
                    opp_val = getattr(item, "xal_AddressLine101", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine101"):
                    opp_val = getattr(item, "xal_AddressLine101", None)
                    
                    setattr(item, "xal_AddressLine101", self)
                    

    @property
    def xal_DocumentRoot127(self):
        return self.__xal_DocumentRoot127

    @xal_DocumentRoot127.setter
    def xal_DocumentRoot127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot127", None)
        self.__xal_DocumentRoot127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumber"):
                    opp_val = getattr(item, "xal_PremiseNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumber"):
                    opp_val = getattr(item, "xal_PremiseNumber", None)
                    
                    setattr(item, "xal_PremiseNumber", self)
                    

    @property
    def xal_DocumentRoot112(self):
        return self.__xal_DocumentRoot112

    @xal_DocumentRoot112.setter
    def xal_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot112", None)
        self.__xal_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Locality113"):
                    opp_val = getattr(item, "xal_Locality113", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Locality113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Locality113"):
                    opp_val = getattr(item, "xal_Locality113", None)
                    
                    setattr(item, "xal_Locality113", self)
                    

    @property
    def xal_DocumentRoot103(self):
        return self.__xal_DocumentRoot103

    @xal_DocumentRoot103.setter
    def xal_DocumentRoot103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot103", None)
        self.__xal_DocumentRoot103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AdministrativeArea104"):
                    opp_val = getattr(item, "xal_AdministrativeArea104", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AdministrativeArea104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AdministrativeArea104"):
                    opp_val = getattr(item, "xal_AdministrativeArea104", None)
                    
                    setattr(item, "xal_AdministrativeArea104", self)
                    

    @property
    def xal_DocumentRoot124(self):
        return self.__xal_DocumentRoot124

    @xal_DocumentRoot124.setter
    def xal_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot124", None)
        self.__xal_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Premise125"):
                    opp_val = getattr(item, "xal_Premise125", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Premise125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Premise125"):
                    opp_val = getattr(item, "xal_Premise125", None)
                    
                    setattr(item, "xal_Premise125", self)
                    

    @property
    def xal_DocumentRoot129(self):
        return self.__xal_DocumentRoot129

    @xal_DocumentRoot129.setter
    def xal_DocumentRoot129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot129", None)
        self.__xal_DocumentRoot129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumberPrefix"):
                    opp_val = getattr(item, "xal_PremiseNumberPrefix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumberPrefix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumberPrefix"):
                    opp_val = getattr(item, "xal_PremiseNumberPrefix", None)
                    
                    setattr(item, "xal_PremiseNumberPrefix", self)
                    

    @property
    def xal_DocumentRoot94(self):
        return self.__xal_DocumentRoot94

    @xal_DocumentRoot94.setter
    def xal_DocumentRoot94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot94", None)
        self.__xal_DocumentRoot94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_EStringToStringMapEntry95"):
                    opp_val = getattr(item, "xal_EStringToStringMapEntry95", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_EStringToStringMapEntry95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_EStringToStringMapEntry95"):
                    opp_val = getattr(item, "xal_EStringToStringMapEntry95", None)
                    
                    setattr(item, "xal_EStringToStringMapEntry95", self)
                    

    @property
    def xal_DocumentRoot133(self):
        return self.__xal_DocumentRoot133

    @xal_DocumentRoot133.setter
    def xal_DocumentRoot133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot133", None)
        self.__xal_DocumentRoot133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Thoroughfare134"):
                    opp_val = getattr(item, "xal_Thoroughfare134", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Thoroughfare134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Thoroughfare134"):
                    opp_val = getattr(item, "xal_Thoroughfare134", None)
                    
                    setattr(item, "xal_Thoroughfare134", self)
                    

    @property
    def xal_DocumentRoot121(self):
        return self.__xal_DocumentRoot121

    @xal_DocumentRoot121.setter
    def xal_DocumentRoot121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot121", None)
        self.__xal_DocumentRoot121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostOffice122"):
                    opp_val = getattr(item, "xal_PostOffice122", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostOffice122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostOffice122"):
                    opp_val = getattr(item, "xal_PostOffice122", None)
                    
                    setattr(item, "xal_PostOffice122", self)
                    

    @property
    def xal_DocumentRoot97(self):
        return self.__xal_DocumentRoot97

    @xal_DocumentRoot97.setter
    def xal_DocumentRoot97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot97", None)
        self.__xal_DocumentRoot97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressDetails98"):
                    opp_val = getattr(item, "xal_AddressDetails98", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressDetails98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressDetails98"):
                    opp_val = getattr(item, "xal_AddressDetails98", None)
                    
                    setattr(item, "xal_AddressDetails98", self)
                    

    @property
    def xal_DocumentRoot140(self):
        return self.__xal_DocumentRoot140

    @xal_DocumentRoot140.setter
    def xal_DocumentRoot140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot140", None)
        self.__xal_DocumentRoot140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberSuffix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix", None)
                    
                    setattr(item, "xal_ThoroughfareNumberSuffix", self)
                    

    @property
    def xal_DocumentRoot136(self):
        return self.__xal_DocumentRoot136

    @xal_DocumentRoot136.setter
    def xal_DocumentRoot136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot136", None)
        self.__xal_DocumentRoot136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumber"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumber"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber", None)
                    
                    setattr(item, "xal_ThoroughfareNumber", self)
                    

    @property
    def xal_DocumentRoot118(self):
        return self.__xal_DocumentRoot118

    @xal_DocumentRoot118.setter
    def xal_DocumentRoot118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot118", None)
        self.__xal_DocumentRoot118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostBox119"):
                    opp_val = getattr(item, "xal_PostBox119", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostBox119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostBox119"):
                    opp_val = getattr(item, "xal_PostBox119", None)
                    
                    setattr(item, "xal_PostBox119", self)
                    

    @property
    def xal_DocumentRoot115(self):
        return self.__xal_DocumentRoot115

    @xal_DocumentRoot115.setter
    def xal_DocumentRoot115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot115", None)
        self.__xal_DocumentRoot115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostalCode116"):
                    opp_val = getattr(item, "xal_PostalCode116", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostalCode116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostalCode116"):
                    opp_val = getattr(item, "xal_PostalCode116", None)
                    
                    setattr(item, "xal_PostalCode116", self)
                    

    @property
    def xal_DocumentRoot109(self):
        return self.__xal_DocumentRoot109

    @xal_DocumentRoot109.setter
    def xal_DocumentRoot109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot109", None)
        self.__xal_DocumentRoot109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_Department110"):
                    opp_val = getattr(item, "xal_Department110", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_Department110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_Department110"):
                    opp_val = getattr(item, "xal_Department110", None)
                    
                    setattr(item, "xal_Department110", self)
                    

    @property
    def xal_DocumentRoot138(self):
        return self.__xal_DocumentRoot138

    @xal_DocumentRoot138.setter
    def xal_DocumentRoot138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot138", None)
        self.__xal_DocumentRoot138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberPrefix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix", None)
                    
                    setattr(item, "xal_ThoroughfareNumberPrefix", self)
                    

    @property
    def xal_DocumentRoot131(self):
        return self.__xal_DocumentRoot131

    @xal_DocumentRoot131.setter
    def xal_DocumentRoot131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DocumentRoot__xal_DocumentRoot131", None)
        self.__xal_DocumentRoot131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumberSuffix"):
                    opp_val = getattr(item, "xal_PremiseNumberSuffix", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumberSuffix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumberSuffix"):
                    opp_val = getattr(item, "xal_PremiseNumberSuffix", None)
                    
                    setattr(item, "xal_PremiseNumberSuffix", self)
                    

class xal_EStringToStringMapEntry:

    pass
class xal_ThoroughfareLeadingType:

    def __init__(self, anyAttribute: str, mixed: str, code: str, type: str, xal_ThoroughfareLeadingType: "xal_DependentThoroughfare" = None, xal_ThoroughfareLeadingType416: "xal_Thoroughfare" = None):
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.code = code
        self.type = type
        self.xal_ThoroughfareLeadingType = xal_ThoroughfareLeadingType
        self.xal_ThoroughfareLeadingType416 = xal_ThoroughfareLeadingType416
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_ThoroughfareLeadingType(self):
        return self.__xal_ThoroughfareLeadingType

    @xal_ThoroughfareLeadingType.setter
    def xal_ThoroughfareLeadingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareLeadingType__xal_ThoroughfareLeadingType", None)
        self.__xal_ThoroughfareLeadingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare85"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare85", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentThoroughfare85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare85"):
                opp_val = getattr(value, "xal_DependentThoroughfare85", None)
                setattr(value, "xal_DependentThoroughfare85", self)

    @property
    def xal_ThoroughfareLeadingType416(self):
        return self.__xal_ThoroughfareLeadingType416

    @xal_ThoroughfareLeadingType416.setter
    def xal_ThoroughfareLeadingType416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareLeadingType__xal_ThoroughfareLeadingType416", None)
        self.__xal_ThoroughfareLeadingType416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare415"):
                opp_val = getattr(old_value, "xal_Thoroughfare415", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare415"):
                opp_val = getattr(value, "xal_Thoroughfare415", None)
                setattr(value, "xal_Thoroughfare415", self)

class xal_ThoroughfarePreDirection:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_ThoroughfarePreDirection: "xal_DependentThoroughfare" = None, xal_ThoroughfarePreDirection413: "xal_Thoroughfare" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfarePreDirection = xal_ThoroughfarePreDirection
        self.xal_ThoroughfarePreDirection413 = xal_ThoroughfarePreDirection413
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_ThoroughfarePreDirection413(self):
        return self.__xal_ThoroughfarePreDirection413

    @xal_ThoroughfarePreDirection413.setter
    def xal_ThoroughfarePreDirection413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfarePreDirection__xal_ThoroughfarePreDirection413", None)
        self.__xal_ThoroughfarePreDirection413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare412"):
                opp_val = getattr(old_value, "xal_Thoroughfare412", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare412"):
                opp_val = getattr(value, "xal_Thoroughfare412", None)
                setattr(value, "xal_Thoroughfare412", self)

    @property
    def xal_ThoroughfarePreDirection(self):
        return self.__xal_ThoroughfarePreDirection

    @xal_ThoroughfarePreDirection.setter
    def xal_ThoroughfarePreDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfarePreDirection__xal_ThoroughfarePreDirection", None)
        self.__xal_ThoroughfarePreDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare83"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare83", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentThoroughfare83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare83"):
                opp_val = getattr(value, "xal_DependentThoroughfare83", None)
                setattr(value, "xal_DependentThoroughfare83", self)

class xal_DependentThoroughfare:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_DependentThoroughfare87: set["xal_ThoroughfareName"] = None, xal_DependentThoroughfare89: "xal_ThoroughfareTrailingType" = None, xal_DependentThoroughfare91: "xal_ThoroughfarePostDirection" = None, xal_DependentThoroughfare: set["xal_AddressLine"] = None, xal_DependentThoroughfare83: "xal_ThoroughfarePreDirection" = None, xal_DependentThoroughfare85: "xal_ThoroughfareLeadingType" = None, xal_DependentThoroughfare428: "xal_Thoroughfare" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_DependentThoroughfare87 = xal_DependentThoroughfare87 if xal_DependentThoroughfare87 is not None else set()
        self.xal_DependentThoroughfare89 = xal_DependentThoroughfare89
        self.xal_DependentThoroughfare91 = xal_DependentThoroughfare91
        self.xal_DependentThoroughfare = xal_DependentThoroughfare if xal_DependentThoroughfare is not None else set()
        self.xal_DependentThoroughfare83 = xal_DependentThoroughfare83
        self.xal_DependentThoroughfare85 = xal_DependentThoroughfare85
        self.xal_DependentThoroughfare428 = xal_DependentThoroughfare428
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_DependentThoroughfare87(self):
        return self.__xal_DependentThoroughfare87

    @xal_DependentThoroughfare87.setter
    def xal_DependentThoroughfare87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare87", None)
        self.__xal_DependentThoroughfare87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareName"):
                    opp_val = getattr(item, "xal_ThoroughfareName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareName"):
                    opp_val = getattr(item, "xal_ThoroughfareName", None)
                    
                    setattr(item, "xal_ThoroughfareName", self)
                    

    @property
    def xal_DependentThoroughfare(self):
        return self.__xal_DependentThoroughfare

    @xal_DependentThoroughfare.setter
    def xal_DependentThoroughfare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare", None)
        self.__xal_DependentThoroughfare = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine81"):
                    opp_val = getattr(item, "xal_AddressLine81", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine81"):
                    opp_val = getattr(item, "xal_AddressLine81", None)
                    
                    setattr(item, "xal_AddressLine81", self)
                    

    @property
    def xal_DependentThoroughfare85(self):
        return self.__xal_DependentThoroughfare85

    @xal_DependentThoroughfare85.setter
    def xal_DependentThoroughfare85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare85", None)
        self.__xal_DependentThoroughfare85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareLeadingType"):
                opp_val = getattr(old_value, "xal_ThoroughfareLeadingType", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareLeadingType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareLeadingType"):
                opp_val = getattr(value, "xal_ThoroughfareLeadingType", None)
                setattr(value, "xal_ThoroughfareLeadingType", self)

    @property
    def xal_DependentThoroughfare83(self):
        return self.__xal_DependentThoroughfare83

    @xal_DependentThoroughfare83.setter
    def xal_DependentThoroughfare83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare83", None)
        self.__xal_DependentThoroughfare83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfarePreDirection"):
                opp_val = getattr(old_value, "xal_ThoroughfarePreDirection", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfarePreDirection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfarePreDirection"):
                opp_val = getattr(value, "xal_ThoroughfarePreDirection", None)
                setattr(value, "xal_ThoroughfarePreDirection", self)

    @property
    def xal_DependentThoroughfare89(self):
        return self.__xal_DependentThoroughfare89

    @xal_DependentThoroughfare89.setter
    def xal_DependentThoroughfare89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare89", None)
        self.__xal_DependentThoroughfare89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareTrailingType"):
                opp_val = getattr(old_value, "xal_ThoroughfareTrailingType", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareTrailingType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareTrailingType"):
                opp_val = getattr(value, "xal_ThoroughfareTrailingType", None)
                setattr(value, "xal_ThoroughfareTrailingType", self)

    @property
    def xal_DependentThoroughfare428(self):
        return self.__xal_DependentThoroughfare428

    @xal_DependentThoroughfare428.setter
    def xal_DependentThoroughfare428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare428", None)
        self.__xal_DependentThoroughfare428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare427"):
                opp_val = getattr(old_value, "xal_Thoroughfare427", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare427"):
                opp_val = getattr(value, "xal_Thoroughfare427", None)
                setattr(value, "xal_Thoroughfare427", self)

    @property
    def xal_DependentThoroughfare91(self):
        return self.__xal_DependentThoroughfare91

    @xal_DependentThoroughfare91.setter
    def xal_DependentThoroughfare91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentThoroughfare__xal_DependentThoroughfare91", None)
        self.__xal_DependentThoroughfare91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfarePostDirection"):
                opp_val = getattr(old_value, "xal_ThoroughfarePostDirection", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfarePostDirection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfarePostDirection"):
                opp_val = getattr(value, "xal_ThoroughfarePostDirection", None)
                setattr(value, "xal_ThoroughfarePostDirection", self)

class xal_ThoroughfarePostDirection:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_ThoroughfarePostDirection: "xal_DependentThoroughfare" = None, xal_ThoroughfarePostDirection425: "xal_Thoroughfare" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfarePostDirection = xal_ThoroughfarePostDirection
        self.xal_ThoroughfarePostDirection425 = xal_ThoroughfarePostDirection425
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_ThoroughfarePostDirection425(self):
        return self.__xal_ThoroughfarePostDirection425

    @xal_ThoroughfarePostDirection425.setter
    def xal_ThoroughfarePostDirection425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfarePostDirection__xal_ThoroughfarePostDirection425", None)
        self.__xal_ThoroughfarePostDirection425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare424"):
                opp_val = getattr(old_value, "xal_Thoroughfare424", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare424"):
                opp_val = getattr(value, "xal_Thoroughfare424", None)
                setattr(value, "xal_Thoroughfare424", self)

    @property
    def xal_ThoroughfarePostDirection(self):
        return self.__xal_ThoroughfarePostDirection

    @xal_ThoroughfarePostDirection.setter
    def xal_ThoroughfarePostDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfarePostDirection__xal_ThoroughfarePostDirection", None)
        self.__xal_ThoroughfarePostDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare91"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare91", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentThoroughfare91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare91"):
                opp_val = getattr(value, "xal_DependentThoroughfare91", None)
                setattr(value, "xal_DependentThoroughfare91", self)

class xal_ThoroughfareTrailingType:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_ThoroughfareTrailingType: "xal_DependentThoroughfare" = None, xal_ThoroughfareTrailingType422: "xal_Thoroughfare" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareTrailingType = xal_ThoroughfareTrailingType
        self.xal_ThoroughfareTrailingType422 = xal_ThoroughfareTrailingType422
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_ThoroughfareTrailingType(self):
        return self.__xal_ThoroughfareTrailingType

    @xal_ThoroughfareTrailingType.setter
    def xal_ThoroughfareTrailingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareTrailingType__xal_ThoroughfareTrailingType", None)
        self.__xal_ThoroughfareTrailingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare89"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare89", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentThoroughfare89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare89"):
                opp_val = getattr(value, "xal_DependentThoroughfare89", None)
                setattr(value, "xal_DependentThoroughfare89", self)

    @property
    def xal_ThoroughfareTrailingType422(self):
        return self.__xal_ThoroughfareTrailingType422

    @xal_ThoroughfareTrailingType422.setter
    def xal_ThoroughfareTrailingType422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareTrailingType__xal_ThoroughfareTrailingType422", None)
        self.__xal_ThoroughfareTrailingType422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare421"):
                opp_val = getattr(old_value, "xal_Thoroughfare421", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare421"):
                opp_val = getattr(value, "xal_Thoroughfare421", None)
                setattr(value, "xal_Thoroughfare421", self)

class xal_ThoroughfareName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_ThoroughfareName: "xal_DependentThoroughfare" = None, xal_ThoroughfareName419: "xal_Thoroughfare" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_ThoroughfareName = xal_ThoroughfareName
        self.xal_ThoroughfareName419 = xal_ThoroughfareName419
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_ThoroughfareName419(self):
        return self.__xal_ThoroughfareName419

    @xal_ThoroughfareName419.setter
    def xal_ThoroughfareName419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareName__xal_ThoroughfareName419", None)
        self.__xal_ThoroughfareName419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare418"):
                opp_val = getattr(old_value, "xal_Thoroughfare418", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare418"):
                opp_val = getattr(value, "xal_Thoroughfare418", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare418", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_ThoroughfareName(self):
        return self.__xal_ThoroughfareName

    @xal_ThoroughfareName.setter
    def xal_ThoroughfareName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_ThoroughfareName__xal_ThoroughfareName", None)
        self.__xal_ThoroughfareName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare87"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare87"):
                opp_val = getattr(value, "xal_DependentThoroughfare87", None)
                if opp_val is None:
                    setattr(value, "xal_DependentThoroughfare87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostalRoute:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_PostalRoute: "xal_DependentLocality" = None, xal_PostalRoute193: "xal_Locality" = None, xal_PostalRoute223: set["xal_AddressLine"] = None, xal_PostalRoute228: "xal_PostalRouteNumber" = None, xal_PostalRoute230: "xal_PostBox" = None, xal_PostalRoute226: set["xal_PostalRouteName"] = None, xal_PostalRoute278: "xal_PostOffice" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostalRoute = xal_PostalRoute
        self.xal_PostalRoute193 = xal_PostalRoute193
        self.xal_PostalRoute223 = xal_PostalRoute223 if xal_PostalRoute223 is not None else set()
        self.xal_PostalRoute228 = xal_PostalRoute228
        self.xal_PostalRoute230 = xal_PostalRoute230
        self.xal_PostalRoute226 = xal_PostalRoute226 if xal_PostalRoute226 is not None else set()
        self.xal_PostalRoute278 = xal_PostalRoute278
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_PostalRoute223(self):
        return self.__xal_PostalRoute223

    @xal_PostalRoute223.setter
    def xal_PostalRoute223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute223", None)
        self.__xal_PostalRoute223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine224"):
                    opp_val = getattr(item, "xal_AddressLine224", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine224"):
                    opp_val = getattr(item, "xal_AddressLine224", None)
                    
                    setattr(item, "xal_AddressLine224", self)
                    

    @property
    def xal_PostalRoute193(self):
        return self.__xal_PostalRoute193

    @xal_PostalRoute193.setter
    def xal_PostalRoute193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute193", None)
        self.__xal_PostalRoute193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality192"):
                opp_val = getattr(old_value, "xal_Locality192", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality192"):
                opp_val = getattr(value, "xal_Locality192", None)
                setattr(value, "xal_Locality192", self)

    @property
    def xal_PostalRoute(self):
        return self.__xal_PostalRoute

    @xal_PostalRoute.setter
    def xal_PostalRoute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute", None)
        self.__xal_PostalRoute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality68"):
                opp_val = getattr(old_value, "xal_DependentLocality68", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality68"):
                opp_val = getattr(value, "xal_DependentLocality68", None)
                setattr(value, "xal_DependentLocality68", self)

    @property
    def xal_PostalRoute230(self):
        return self.__xal_PostalRoute230

    @xal_PostalRoute230.setter
    def xal_PostalRoute230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute230", None)
        self.__xal_PostalRoute230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox231"):
                opp_val = getattr(old_value, "xal_PostBox231", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox231"):
                opp_val = getattr(value, "xal_PostBox231", None)
                setattr(value, "xal_PostBox231", self)

    @property
    def xal_PostalRoute226(self):
        return self.__xal_PostalRoute226

    @xal_PostalRoute226.setter
    def xal_PostalRoute226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute226", None)
        self.__xal_PostalRoute226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostalRouteName"):
                    opp_val = getattr(item, "xal_PostalRouteName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostalRouteName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostalRouteName"):
                    opp_val = getattr(item, "xal_PostalRouteName", None)
                    
                    setattr(item, "xal_PostalRouteName", self)
                    

    @property
    def xal_PostalRoute228(self):
        return self.__xal_PostalRoute228

    @xal_PostalRoute228.setter
    def xal_PostalRoute228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute228", None)
        self.__xal_PostalRoute228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRouteNumber"):
                opp_val = getattr(old_value, "xal_PostalRouteNumber", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRouteNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRouteNumber"):
                opp_val = getattr(value, "xal_PostalRouteNumber", None)
                setattr(value, "xal_PostalRouteNumber", self)

    @property
    def xal_PostalRoute278(self):
        return self.__xal_PostalRoute278

    @xal_PostalRoute278.setter
    def xal_PostalRoute278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalRoute__xal_PostalRoute278", None)
        self.__xal_PostalRoute278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice277"):
                opp_val = getattr(old_value, "xal_PostOffice277", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice277"):
                opp_val = getattr(value, "xal_PostOffice277", None)
                setattr(value, "xal_PostOffice277", self)

class xal_LargeMailUser:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_LargeMailUser: "xal_DependentLocality" = None, xal_LargeMailUser157: set["xal_AddressLine"] = None, xal_LargeMailUser160: set["xal_LargeMailUserName"] = None, xal_LargeMailUser164: set["xal_BuildingName"] = None, xal_LargeMailUser166: "xal_Department" = None, xal_LargeMailUser169: "xal_PostBox" = None, xal_LargeMailUser172: "xal_Thoroughfare" = None, xal_LargeMailUser175: "xal_PostalCode" = None, xal_LargeMailUser162: "xal_LargeMailUserIdentifier" = None, xal_LargeMailUser187: "xal_Locality" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_LargeMailUser = xal_LargeMailUser
        self.xal_LargeMailUser157 = xal_LargeMailUser157 if xal_LargeMailUser157 is not None else set()
        self.xal_LargeMailUser160 = xal_LargeMailUser160 if xal_LargeMailUser160 is not None else set()
        self.xal_LargeMailUser164 = xal_LargeMailUser164 if xal_LargeMailUser164 is not None else set()
        self.xal_LargeMailUser166 = xal_LargeMailUser166
        self.xal_LargeMailUser169 = xal_LargeMailUser169
        self.xal_LargeMailUser172 = xal_LargeMailUser172
        self.xal_LargeMailUser175 = xal_LargeMailUser175
        self.xal_LargeMailUser162 = xal_LargeMailUser162
        self.xal_LargeMailUser187 = xal_LargeMailUser187
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_LargeMailUser166(self):
        return self.__xal_LargeMailUser166

    @xal_LargeMailUser166.setter
    def xal_LargeMailUser166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser166", None)
        self.__xal_LargeMailUser166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Department167"):
                opp_val = getattr(old_value, "xal_Department167", None)
                if opp_val == self:
                    setattr(old_value, "xal_Department167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Department167"):
                opp_val = getattr(value, "xal_Department167", None)
                setattr(value, "xal_Department167", self)

    @property
    def xal_LargeMailUser157(self):
        return self.__xal_LargeMailUser157

    @xal_LargeMailUser157.setter
    def xal_LargeMailUser157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser157", None)
        self.__xal_LargeMailUser157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine158"):
                    opp_val = getattr(item, "xal_AddressLine158", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine158"):
                    opp_val = getattr(item, "xal_AddressLine158", None)
                    
                    setattr(item, "xal_AddressLine158", self)
                    

    @property
    def xal_LargeMailUser175(self):
        return self.__xal_LargeMailUser175

    @xal_LargeMailUser175.setter
    def xal_LargeMailUser175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser175", None)
        self.__xal_LargeMailUser175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode176"):
                opp_val = getattr(old_value, "xal_PostalCode176", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode176"):
                opp_val = getattr(value, "xal_PostalCode176", None)
                setattr(value, "xal_PostalCode176", self)

    @property
    def xal_LargeMailUser164(self):
        return self.__xal_LargeMailUser164

    @xal_LargeMailUser164.setter
    def xal_LargeMailUser164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser164", None)
        self.__xal_LargeMailUser164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_BuildingName"):
                    opp_val = getattr(item, "xal_BuildingName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_BuildingName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_BuildingName"):
                    opp_val = getattr(item, "xal_BuildingName", None)
                    
                    setattr(item, "xal_BuildingName", self)
                    

    @property
    def xal_LargeMailUser169(self):
        return self.__xal_LargeMailUser169

    @xal_LargeMailUser169.setter
    def xal_LargeMailUser169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser169", None)
        self.__xal_LargeMailUser169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox170"):
                opp_val = getattr(old_value, "xal_PostBox170", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox170"):
                opp_val = getattr(value, "xal_PostBox170", None)
                setattr(value, "xal_PostBox170", self)

    @property
    def xal_LargeMailUser162(self):
        return self.__xal_LargeMailUser162

    @xal_LargeMailUser162.setter
    def xal_LargeMailUser162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser162", None)
        self.__xal_LargeMailUser162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUserIdentifier"):
                opp_val = getattr(old_value, "xal_LargeMailUserIdentifier", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUserIdentifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUserIdentifier"):
                opp_val = getattr(value, "xal_LargeMailUserIdentifier", None)
                setattr(value, "xal_LargeMailUserIdentifier", self)

    @property
    def xal_LargeMailUser(self):
        return self.__xal_LargeMailUser

    @xal_LargeMailUser.setter
    def xal_LargeMailUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser", None)
        self.__xal_LargeMailUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality63"):
                opp_val = getattr(old_value, "xal_DependentLocality63", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality63"):
                opp_val = getattr(value, "xal_DependentLocality63", None)
                setattr(value, "xal_DependentLocality63", self)

    @property
    def xal_LargeMailUser160(self):
        return self.__xal_LargeMailUser160

    @xal_LargeMailUser160.setter
    def xal_LargeMailUser160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser160", None)
        self.__xal_LargeMailUser160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_LargeMailUserName"):
                    opp_val = getattr(item, "xal_LargeMailUserName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_LargeMailUserName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_LargeMailUserName"):
                    opp_val = getattr(item, "xal_LargeMailUserName", None)
                    
                    setattr(item, "xal_LargeMailUserName", self)
                    

    @property
    def xal_LargeMailUser172(self):
        return self.__xal_LargeMailUser172

    @xal_LargeMailUser172.setter
    def xal_LargeMailUser172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser172", None)
        self.__xal_LargeMailUser172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare173"):
                opp_val = getattr(old_value, "xal_Thoroughfare173", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare173"):
                opp_val = getattr(value, "xal_Thoroughfare173", None)
                setattr(value, "xal_Thoroughfare173", self)

    @property
    def xal_LargeMailUser187(self):
        return self.__xal_LargeMailUser187

    @xal_LargeMailUser187.setter
    def xal_LargeMailUser187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_LargeMailUser__xal_LargeMailUser187", None)
        self.__xal_LargeMailUser187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality186"):
                opp_val = getattr(old_value, "xal_Locality186", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality186"):
                opp_val = getattr(value, "xal_Locality186", None)
                setattr(value, "xal_Locality186", self)

class xal_Premise:

    def __init__(self, any: str, premiseDependency: str, premiseDependencyType: str, premiseThoroughfareConnector: str, type: str, anyAttribute: str, xal_Premise: "xal_DependentLocality" = None, xal_Premise125: "xal_DocumentRoot" = None, xal_Premise199: "xal_Locality" = None, xal_Premise293: set["xal_AddressLine"] = None, xal_Premise296: set["xal_PremiseName"] = None, xal_Premise298: "xal_PremiseLocation" = None, xal_Premise300: set["xal_PremiseNumber"] = None, xal_Premise303: "xal_PremiseNumberRange" = None, xal_Premise305: set["xal_PremiseNumberPrefix"] = None, xal_Premise308: set["xal_PremiseNumberSuffix"] = None, xal_Premise311: set["xal_BuildingName"] = None, xal_Premise314: set["xal_SubPremise"] = None, xal_Premise316: "xal_Firm" = None, xal_Premise319: "xal_MailStop" = None, xal_Premise322: "xal_PostalCode" = None, xal_Premise326: "xal_Premise" = None, xal_Premise324: "xal_Premise" = None, xal_Premise434: "xal_Thoroughfare" = None):
        self.any = any
        self.premiseDependency = premiseDependency
        self.premiseDependencyType = premiseDependencyType
        self.premiseThoroughfareConnector = premiseThoroughfareConnector
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_Premise = xal_Premise
        self.xal_Premise125 = xal_Premise125
        self.xal_Premise199 = xal_Premise199
        self.xal_Premise293 = xal_Premise293 if xal_Premise293 is not None else set()
        self.xal_Premise296 = xal_Premise296 if xal_Premise296 is not None else set()
        self.xal_Premise298 = xal_Premise298
        self.xal_Premise300 = xal_Premise300 if xal_Premise300 is not None else set()
        self.xal_Premise303 = xal_Premise303
        self.xal_Premise305 = xal_Premise305 if xal_Premise305 is not None else set()
        self.xal_Premise308 = xal_Premise308 if xal_Premise308 is not None else set()
        self.xal_Premise311 = xal_Premise311 if xal_Premise311 is not None else set()
        self.xal_Premise314 = xal_Premise314 if xal_Premise314 is not None else set()
        self.xal_Premise316 = xal_Premise316
        self.xal_Premise319 = xal_Premise319
        self.xal_Premise322 = xal_Premise322
        self.xal_Premise326 = xal_Premise326
        self.xal_Premise324 = xal_Premise324
        self.xal_Premise434 = xal_Premise434
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def premiseDependencyType(self) -> str:
        return self.__premiseDependencyType

    @premiseDependencyType.setter
    def premiseDependencyType(self, premiseDependencyType: str):
        self.__premiseDependencyType = premiseDependencyType

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def premiseThoroughfareConnector(self) -> str:
        return self.__premiseThoroughfareConnector

    @premiseThoroughfareConnector.setter
    def premiseThoroughfareConnector(self, premiseThoroughfareConnector: str):
        self.__premiseThoroughfareConnector = premiseThoroughfareConnector

    @property
    def premiseDependency(self) -> str:
        return self.__premiseDependency

    @premiseDependency.setter
    def premiseDependency(self, premiseDependency: str):
        self.__premiseDependency = premiseDependency

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_Premise298(self):
        return self.__xal_Premise298

    @xal_Premise298.setter
    def xal_Premise298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise298", None)
        self.__xal_Premise298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseLocation"):
                opp_val = getattr(old_value, "xal_PremiseLocation", None)
                if opp_val == self:
                    setattr(old_value, "xal_PremiseLocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseLocation"):
                opp_val = getattr(value, "xal_PremiseLocation", None)
                setattr(value, "xal_PremiseLocation", self)

    @property
    def xal_Premise293(self):
        return self.__xal_Premise293

    @xal_Premise293.setter
    def xal_Premise293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise293", None)
        self.__xal_Premise293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine294"):
                    opp_val = getattr(item, "xal_AddressLine294", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine294"):
                    opp_val = getattr(item, "xal_AddressLine294", None)
                    
                    setattr(item, "xal_AddressLine294", self)
                    

    @property
    def xal_Premise296(self):
        return self.__xal_Premise296

    @xal_Premise296.setter
    def xal_Premise296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise296", None)
        self.__xal_Premise296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseName"):
                    opp_val = getattr(item, "xal_PremiseName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseName"):
                    opp_val = getattr(item, "xal_PremiseName", None)
                    
                    setattr(item, "xal_PremiseName", self)
                    

    @property
    def xal_Premise308(self):
        return self.__xal_Premise308

    @xal_Premise308.setter
    def xal_Premise308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise308", None)
        self.__xal_Premise308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumberSuffix309"):
                    opp_val = getattr(item, "xal_PremiseNumberSuffix309", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumberSuffix309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumberSuffix309"):
                    opp_val = getattr(item, "xal_PremiseNumberSuffix309", None)
                    
                    setattr(item, "xal_PremiseNumberSuffix309", self)
                    

    @property
    def xal_Premise326(self):
        return self.__xal_Premise326

    @xal_Premise326.setter
    def xal_Premise326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise326", None)
        self.__xal_Premise326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise324"):
                opp_val = getattr(old_value, "xal_Premise324", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise324"):
                opp_val = getattr(value, "xal_Premise324", None)
                setattr(value, "xal_Premise324", self)

    @property
    def xal_Premise322(self):
        return self.__xal_Premise322

    @xal_Premise322.setter
    def xal_Premise322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise322", None)
        self.__xal_Premise322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode323"):
                opp_val = getattr(old_value, "xal_PostalCode323", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode323"):
                opp_val = getattr(value, "xal_PostalCode323", None)
                setattr(value, "xal_PostalCode323", self)

    @property
    def xal_Premise305(self):
        return self.__xal_Premise305

    @xal_Premise305.setter
    def xal_Premise305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise305", None)
        self.__xal_Premise305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumberPrefix306"):
                    opp_val = getattr(item, "xal_PremiseNumberPrefix306", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumberPrefix306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumberPrefix306"):
                    opp_val = getattr(item, "xal_PremiseNumberPrefix306", None)
                    
                    setattr(item, "xal_PremiseNumberPrefix306", self)
                    

    @property
    def xal_Premise319(self):
        return self.__xal_Premise319

    @xal_Premise319.setter
    def xal_Premise319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise319", None)
        self.__xal_Premise319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop320"):
                opp_val = getattr(old_value, "xal_MailStop320", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop320"):
                opp_val = getattr(value, "xal_MailStop320", None)
                setattr(value, "xal_MailStop320", self)

    @property
    def xal_Premise300(self):
        return self.__xal_Premise300

    @xal_Premise300.setter
    def xal_Premise300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise300", None)
        self.__xal_Premise300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PremiseNumber301"):
                    opp_val = getattr(item, "xal_PremiseNumber301", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PremiseNumber301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PremiseNumber301"):
                    opp_val = getattr(item, "xal_PremiseNumber301", None)
                    
                    setattr(item, "xal_PremiseNumber301", self)
                    

    @property
    def xal_Premise316(self):
        return self.__xal_Premise316

    @xal_Premise316.setter
    def xal_Premise316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise316", None)
        self.__xal_Premise316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm317"):
                opp_val = getattr(old_value, "xal_Firm317", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm317"):
                opp_val = getattr(value, "xal_Firm317", None)
                setattr(value, "xal_Firm317", self)

    @property
    def xal_Premise125(self):
        return self.__xal_Premise125

    @xal_Premise125.setter
    def xal_Premise125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise125", None)
        self.__xal_Premise125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot124"):
                opp_val = getattr(old_value, "xal_DocumentRoot124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot124"):
                opp_val = getattr(value, "xal_DocumentRoot124", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_Premise199(self):
        return self.__xal_Premise199

    @xal_Premise199.setter
    def xal_Premise199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise199", None)
        self.__xal_Premise199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality198"):
                opp_val = getattr(old_value, "xal_Locality198", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality198"):
                opp_val = getattr(value, "xal_Locality198", None)
                setattr(value, "xal_Locality198", self)

    @property
    def xal_Premise303(self):
        return self.__xal_Premise303

    @xal_Premise303.setter
    def xal_Premise303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise303", None)
        self.__xal_Premise303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRange"):
                opp_val = getattr(old_value, "xal_PremiseNumberRange", None)
                if opp_val == self:
                    setattr(old_value, "xal_PremiseNumberRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRange"):
                opp_val = getattr(value, "xal_PremiseNumberRange", None)
                setattr(value, "xal_PremiseNumberRange", self)

    @property
    def xal_Premise434(self):
        return self.__xal_Premise434

    @xal_Premise434.setter
    def xal_Premise434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise434", None)
        self.__xal_Premise434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare433"):
                opp_val = getattr(old_value, "xal_Thoroughfare433", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare433"):
                opp_val = getattr(value, "xal_Thoroughfare433", None)
                setattr(value, "xal_Thoroughfare433", self)

    @property
    def xal_Premise324(self):
        return self.__xal_Premise324

    @xal_Premise324.setter
    def xal_Premise324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise324", None)
        self.__xal_Premise324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise326"):
                opp_val = getattr(old_value, "xal_Premise326", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise326"):
                opp_val = getattr(value, "xal_Premise326", None)
                setattr(value, "xal_Premise326", self)

    @property
    def xal_Premise(self):
        return self.__xal_Premise

    @xal_Premise.setter
    def xal_Premise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise", None)
        self.__xal_Premise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality73"):
                opp_val = getattr(old_value, "xal_DependentLocality73", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality73"):
                opp_val = getattr(value, "xal_DependentLocality73", None)
                setattr(value, "xal_DependentLocality73", self)

    @property
    def xal_Premise311(self):
        return self.__xal_Premise311

    @xal_Premise311.setter
    def xal_Premise311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise311", None)
        self.__xal_Premise311 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_BuildingName312"):
                    opp_val = getattr(item, "xal_BuildingName312", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_BuildingName312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_BuildingName312"):
                    opp_val = getattr(item, "xal_BuildingName312", None)
                    
                    setattr(item, "xal_BuildingName312", self)
                    

    @property
    def xal_Premise314(self):
        return self.__xal_Premise314

    @xal_Premise314.setter
    def xal_Premise314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Premise__xal_Premise314", None)
        self.__xal_Premise314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubPremise"):
                    opp_val = getattr(item, "xal_SubPremise", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubPremise", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubPremise"):
                    opp_val = getattr(item, "xal_SubPremise", None)
                    
                    setattr(item, "xal_SubPremise", self)
                    

class xal_PostBox:

    def __init__(self, any: str, indicator: str, type: str, anyAttribute: str, xal_PostBox: "xal_DependentLocality" = None, xal_PostBox119: "xal_DocumentRoot" = None, xal_PostBox170: "xal_LargeMailUser" = None, xal_PostBox184: "xal_Locality" = None, xal_PostBox231: "xal_PostalRoute" = None, xal_PostBox253: set["xal_AddressLine"] = None, xal_PostBox256: "xal_PostBoxNumber" = None, xal_PostBox258: "xal_PostBoxNumberPrefix" = None, xal_PostBox260: "xal_PostBoxNumberSuffix" = None, xal_PostBox262: "xal_PostBoxNumberExtension" = None, xal_PostBox264: "xal_Firm" = None, xal_PostBox267: "xal_PostalCode" = None, xal_PostBox281: "xal_PostOffice" = None):
        self.any = any
        self.indicator = indicator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostBox = xal_PostBox
        self.xal_PostBox119 = xal_PostBox119
        self.xal_PostBox170 = xal_PostBox170
        self.xal_PostBox184 = xal_PostBox184
        self.xal_PostBox231 = xal_PostBox231
        self.xal_PostBox253 = xal_PostBox253 if xal_PostBox253 is not None else set()
        self.xal_PostBox256 = xal_PostBox256
        self.xal_PostBox258 = xal_PostBox258
        self.xal_PostBox260 = xal_PostBox260
        self.xal_PostBox262 = xal_PostBox262
        self.xal_PostBox264 = xal_PostBox264
        self.xal_PostBox267 = xal_PostBox267
        self.xal_PostBox281 = xal_PostBox281
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_PostBox(self):
        return self.__xal_PostBox

    @xal_PostBox.setter
    def xal_PostBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox", None)
        self.__xal_PostBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality61"):
                opp_val = getattr(old_value, "xal_DependentLocality61", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality61"):
                opp_val = getattr(value, "xal_DependentLocality61", None)
                setattr(value, "xal_DependentLocality61", self)

    @property
    def xal_PostBox267(self):
        return self.__xal_PostBox267

    @xal_PostBox267.setter
    def xal_PostBox267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox267", None)
        self.__xal_PostBox267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode268"):
                opp_val = getattr(old_value, "xal_PostalCode268", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode268"):
                opp_val = getattr(value, "xal_PostalCode268", None)
                setattr(value, "xal_PostalCode268", self)

    @property
    def xal_PostBox253(self):
        return self.__xal_PostBox253

    @xal_PostBox253.setter
    def xal_PostBox253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox253", None)
        self.__xal_PostBox253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine254"):
                    opp_val = getattr(item, "xal_AddressLine254", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine254"):
                    opp_val = getattr(item, "xal_AddressLine254", None)
                    
                    setattr(item, "xal_AddressLine254", self)
                    

    @property
    def xal_PostBox119(self):
        return self.__xal_PostBox119

    @xal_PostBox119.setter
    def xal_PostBox119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox119", None)
        self.__xal_PostBox119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot118"):
                opp_val = getattr(old_value, "xal_DocumentRoot118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot118"):
                opp_val = getattr(value, "xal_DocumentRoot118", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PostBox262(self):
        return self.__xal_PostBox262

    @xal_PostBox262.setter
    def xal_PostBox262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox262", None)
        self.__xal_PostBox262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBoxNumberExtension"):
                opp_val = getattr(old_value, "xal_PostBoxNumberExtension", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBoxNumberExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBoxNumberExtension"):
                opp_val = getattr(value, "xal_PostBoxNumberExtension", None)
                setattr(value, "xal_PostBoxNumberExtension", self)

    @property
    def xal_PostBox184(self):
        return self.__xal_PostBox184

    @xal_PostBox184.setter
    def xal_PostBox184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox184", None)
        self.__xal_PostBox184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality183"):
                opp_val = getattr(old_value, "xal_Locality183", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality183"):
                opp_val = getattr(value, "xal_Locality183", None)
                setattr(value, "xal_Locality183", self)

    @property
    def xal_PostBox256(self):
        return self.__xal_PostBox256

    @xal_PostBox256.setter
    def xal_PostBox256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox256", None)
        self.__xal_PostBox256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBoxNumber"):
                opp_val = getattr(old_value, "xal_PostBoxNumber", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBoxNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBoxNumber"):
                opp_val = getattr(value, "xal_PostBoxNumber", None)
                setattr(value, "xal_PostBoxNumber", self)

    @property
    def xal_PostBox258(self):
        return self.__xal_PostBox258

    @xal_PostBox258.setter
    def xal_PostBox258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox258", None)
        self.__xal_PostBox258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBoxNumberPrefix"):
                opp_val = getattr(old_value, "xal_PostBoxNumberPrefix", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBoxNumberPrefix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBoxNumberPrefix"):
                opp_val = getattr(value, "xal_PostBoxNumberPrefix", None)
                setattr(value, "xal_PostBoxNumberPrefix", self)

    @property
    def xal_PostBox281(self):
        return self.__xal_PostBox281

    @xal_PostBox281.setter
    def xal_PostBox281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox281", None)
        self.__xal_PostBox281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice280"):
                opp_val = getattr(old_value, "xal_PostOffice280", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice280"):
                opp_val = getattr(value, "xal_PostOffice280", None)
                setattr(value, "xal_PostOffice280", self)

    @property
    def xal_PostBox170(self):
        return self.__xal_PostBox170

    @xal_PostBox170.setter
    def xal_PostBox170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox170", None)
        self.__xal_PostBox170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser169"):
                opp_val = getattr(old_value, "xal_LargeMailUser169", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser169"):
                opp_val = getattr(value, "xal_LargeMailUser169", None)
                setattr(value, "xal_LargeMailUser169", self)

    @property
    def xal_PostBox260(self):
        return self.__xal_PostBox260

    @xal_PostBox260.setter
    def xal_PostBox260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox260", None)
        self.__xal_PostBox260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBoxNumberSuffix"):
                opp_val = getattr(old_value, "xal_PostBoxNumberSuffix", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBoxNumberSuffix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBoxNumberSuffix"):
                opp_val = getattr(value, "xal_PostBoxNumberSuffix", None)
                setattr(value, "xal_PostBoxNumberSuffix", self)

    @property
    def xal_PostBox264(self):
        return self.__xal_PostBox264

    @xal_PostBox264.setter
    def xal_PostBox264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox264", None)
        self.__xal_PostBox264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm265"):
                opp_val = getattr(old_value, "xal_Firm265", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm265"):
                opp_val = getattr(value, "xal_Firm265", None)
                setattr(value, "xal_Firm265", self)

    @property
    def xal_PostBox231(self):
        return self.__xal_PostBox231

    @xal_PostBox231.setter
    def xal_PostBox231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostBox__xal_PostBox231", None)
        self.__xal_PostBox231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute230"):
                opp_val = getattr(old_value, "xal_PostalRoute230", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRoute230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute230"):
                opp_val = getattr(value, "xal_PostalRoute230", None)
                setattr(value, "xal_PostalRoute230", self)

class xal_DependentLocalityNumber:

    def __init__(self, mixed: str, code: str, nameNumberOccurrence: str, anyAttribute: str, xal_DependentLocalityNumber: "xal_DependentLocality" = None):
        self.mixed = mixed
        self.code = code
        self.nameNumberOccurrence = nameNumberOccurrence
        self.anyAttribute = anyAttribute
        self.xal_DependentLocalityNumber = xal_DependentLocalityNumber
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def nameNumberOccurrence(self) -> str:
        return self.__nameNumberOccurrence

    @nameNumberOccurrence.setter
    def nameNumberOccurrence(self, nameNumberOccurrence: str):
        self.__nameNumberOccurrence = nameNumberOccurrence

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_DependentLocalityNumber(self):
        return self.__xal_DependentLocalityNumber

    @xal_DependentLocalityNumber.setter
    def xal_DependentLocalityNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocalityNumber__xal_DependentLocalityNumber", None)
        self.__xal_DependentLocalityNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality59"):
                opp_val = getattr(old_value, "xal_DependentLocality59", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality59"):
                opp_val = getattr(value, "xal_DependentLocality59", None)
                setattr(value, "xal_DependentLocality59", self)

class xal_DependentLocalityName:

    def __init__(self, code: str, type: str, anyAttribute: str, mixed: str, xal_DependentLocalityName: "xal_DependentLocality" = None):
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.xal_DependentLocalityName = xal_DependentLocalityName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_DependentLocalityName(self):
        return self.__xal_DependentLocalityName

    @xal_DependentLocalityName.setter
    def xal_DependentLocalityName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocalityName__xal_DependentLocalityName", None)
        self.__xal_DependentLocalityName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality57"):
                opp_val = getattr(old_value, "xal_DependentLocality57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality57"):
                opp_val = getattr(value, "xal_DependentLocality57", None)
                if opp_val is None:
                    setattr(value, "xal_DependentLocality57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_DependentLocality:

    def __init__(self, any: str, connector: str, indicator: str, type: str, usageType: str, anyAttribute: str, xal_DependentLocality: set["xal_AddressLine"] = None, xal_DependentLocality57: set["xal_DependentLocalityName"] = None, xal_DependentLocality59: "xal_DependentLocalityNumber" = None, xal_DependentLocality61: "xal_PostBox" = None, xal_DependentLocality73: "xal_Premise" = None, xal_DependentLocality76: "xal_DependentLocality" = None, xal_DependentLocality74: "xal_DependentLocality" = None, xal_DependentLocality78: "xal_PostalCode" = None, xal_DependentLocality63: "xal_LargeMailUser" = None, xal_DependentLocality65: "xal_PostOffice" = None, xal_DependentLocality68: "xal_PostalRoute" = None, xal_DependentLocality70: "xal_Thoroughfare" = None, xal_DependentLocality202: "xal_Locality" = None, xal_DependentLocality431: "xal_Thoroughfare" = None):
        self.any = any
        self.connector = connector
        self.indicator = indicator
        self.type = type
        self.usageType = usageType
        self.anyAttribute = anyAttribute
        self.xal_DependentLocality = xal_DependentLocality if xal_DependentLocality is not None else set()
        self.xal_DependentLocality57 = xal_DependentLocality57 if xal_DependentLocality57 is not None else set()
        self.xal_DependentLocality59 = xal_DependentLocality59
        self.xal_DependentLocality61 = xal_DependentLocality61
        self.xal_DependentLocality73 = xal_DependentLocality73
        self.xal_DependentLocality76 = xal_DependentLocality76
        self.xal_DependentLocality74 = xal_DependentLocality74
        self.xal_DependentLocality78 = xal_DependentLocality78
        self.xal_DependentLocality63 = xal_DependentLocality63
        self.xal_DependentLocality65 = xal_DependentLocality65
        self.xal_DependentLocality68 = xal_DependentLocality68
        self.xal_DependentLocality70 = xal_DependentLocality70
        self.xal_DependentLocality202 = xal_DependentLocality202
        self.xal_DependentLocality431 = xal_DependentLocality431
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def connector(self) -> str:
        return self.__connector

    @connector.setter
    def connector(self, connector: str):
        self.__connector = connector

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def usageType(self) -> str:
        return self.__usageType

    @usageType.setter
    def usageType(self, usageType: str):
        self.__usageType = usageType

    @property
    def xal_DependentLocality61(self):
        return self.__xal_DependentLocality61

    @xal_DependentLocality61.setter
    def xal_DependentLocality61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality61", None)
        self.__xal_DependentLocality61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox"):
                opp_val = getattr(old_value, "xal_PostBox", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox"):
                opp_val = getattr(value, "xal_PostBox", None)
                setattr(value, "xal_PostBox", self)

    @property
    def xal_DependentLocality65(self):
        return self.__xal_DependentLocality65

    @xal_DependentLocality65.setter
    def xal_DependentLocality65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality65", None)
        self.__xal_DependentLocality65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice66"):
                opp_val = getattr(old_value, "xal_PostOffice66", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice66"):
                opp_val = getattr(value, "xal_PostOffice66", None)
                setattr(value, "xal_PostOffice66", self)

    @property
    def xal_DependentLocality(self):
        return self.__xal_DependentLocality

    @xal_DependentLocality.setter
    def xal_DependentLocality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality", None)
        self.__xal_DependentLocality = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine55"):
                    opp_val = getattr(item, "xal_AddressLine55", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine55"):
                    opp_val = getattr(item, "xal_AddressLine55", None)
                    
                    setattr(item, "xal_AddressLine55", self)
                    

    @property
    def xal_DependentLocality57(self):
        return self.__xal_DependentLocality57

    @xal_DependentLocality57.setter
    def xal_DependentLocality57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality57", None)
        self.__xal_DependentLocality57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_DependentLocalityName"):
                    opp_val = getattr(item, "xal_DependentLocalityName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_DependentLocalityName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_DependentLocalityName"):
                    opp_val = getattr(item, "xal_DependentLocalityName", None)
                    
                    setattr(item, "xal_DependentLocalityName", self)
                    

    @property
    def xal_DependentLocality431(self):
        return self.__xal_DependentLocality431

    @xal_DependentLocality431.setter
    def xal_DependentLocality431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality431", None)
        self.__xal_DependentLocality431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare430"):
                opp_val = getattr(old_value, "xal_Thoroughfare430", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare430"):
                opp_val = getattr(value, "xal_Thoroughfare430", None)
                setattr(value, "xal_Thoroughfare430", self)

    @property
    def xal_DependentLocality70(self):
        return self.__xal_DependentLocality70

    @xal_DependentLocality70.setter
    def xal_DependentLocality70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality70", None)
        self.__xal_DependentLocality70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare71"):
                opp_val = getattr(old_value, "xal_Thoroughfare71", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare71"):
                opp_val = getattr(value, "xal_Thoroughfare71", None)
                setattr(value, "xal_Thoroughfare71", self)

    @property
    def xal_DependentLocality68(self):
        return self.__xal_DependentLocality68

    @xal_DependentLocality68.setter
    def xal_DependentLocality68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality68", None)
        self.__xal_DependentLocality68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute"):
                opp_val = getattr(old_value, "xal_PostalRoute", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRoute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute"):
                opp_val = getattr(value, "xal_PostalRoute", None)
                setattr(value, "xal_PostalRoute", self)

    @property
    def xal_DependentLocality74(self):
        return self.__xal_DependentLocality74

    @xal_DependentLocality74.setter
    def xal_DependentLocality74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality74", None)
        self.__xal_DependentLocality74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality76"):
                opp_val = getattr(old_value, "xal_DependentLocality76", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality76"):
                opp_val = getattr(value, "xal_DependentLocality76", None)
                setattr(value, "xal_DependentLocality76", self)

    @property
    def xal_DependentLocality73(self):
        return self.__xal_DependentLocality73

    @xal_DependentLocality73.setter
    def xal_DependentLocality73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality73", None)
        self.__xal_DependentLocality73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise"):
                opp_val = getattr(old_value, "xal_Premise", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise"):
                opp_val = getattr(value, "xal_Premise", None)
                setattr(value, "xal_Premise", self)

    @property
    def xal_DependentLocality59(self):
        return self.__xal_DependentLocality59

    @xal_DependentLocality59.setter
    def xal_DependentLocality59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality59", None)
        self.__xal_DependentLocality59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocalityNumber"):
                opp_val = getattr(old_value, "xal_DependentLocalityNumber", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocalityNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocalityNumber"):
                opp_val = getattr(value, "xal_DependentLocalityNumber", None)
                setattr(value, "xal_DependentLocalityNumber", self)

    @property
    def xal_DependentLocality202(self):
        return self.__xal_DependentLocality202

    @xal_DependentLocality202.setter
    def xal_DependentLocality202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality202", None)
        self.__xal_DependentLocality202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality201"):
                opp_val = getattr(old_value, "xal_Locality201", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality201"):
                opp_val = getattr(value, "xal_Locality201", None)
                setattr(value, "xal_Locality201", self)

    @property
    def xal_DependentLocality76(self):
        return self.__xal_DependentLocality76

    @xal_DependentLocality76.setter
    def xal_DependentLocality76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality76", None)
        self.__xal_DependentLocality76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality74"):
                opp_val = getattr(old_value, "xal_DependentLocality74", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality74"):
                opp_val = getattr(value, "xal_DependentLocality74", None)
                setattr(value, "xal_DependentLocality74", self)

    @property
    def xal_DependentLocality63(self):
        return self.__xal_DependentLocality63

    @xal_DependentLocality63.setter
    def xal_DependentLocality63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality63", None)
        self.__xal_DependentLocality63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser"):
                opp_val = getattr(old_value, "xal_LargeMailUser", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser"):
                opp_val = getattr(value, "xal_LargeMailUser", None)
                setattr(value, "xal_LargeMailUser", self)

    @property
    def xal_DependentLocality78(self):
        return self.__xal_DependentLocality78

    @xal_DependentLocality78.setter
    def xal_DependentLocality78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DependentLocality__xal_DependentLocality78", None)
        self.__xal_DependentLocality78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode79"):
                opp_val = getattr(old_value, "xal_PostalCode79", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode79"):
                opp_val = getattr(value, "xal_PostalCode79", None)
                setattr(value, "xal_PostalCode79", self)

class xal_Department:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_Department48: set["xal_DepartmentName"] = None, xal_Department50: "xal_MailStop" = None, xal_Department52: "xal_PostalCode" = None, xal_Department: set["xal_AddressLine"] = None, xal_Department110: "xal_DocumentRoot" = None, xal_Department149: "xal_Firm" = None, xal_Department167: "xal_LargeMailUser" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_Department48 = xal_Department48 if xal_Department48 is not None else set()
        self.xal_Department50 = xal_Department50
        self.xal_Department52 = xal_Department52
        self.xal_Department = xal_Department if xal_Department is not None else set()
        self.xal_Department110 = xal_Department110
        self.xal_Department149 = xal_Department149
        self.xal_Department167 = xal_Department167
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_Department48(self):
        return self.__xal_Department48

    @xal_Department48.setter
    def xal_Department48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department48", None)
        self.__xal_Department48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_DepartmentName"):
                    opp_val = getattr(item, "xal_DepartmentName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_DepartmentName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_DepartmentName"):
                    opp_val = getattr(item, "xal_DepartmentName", None)
                    
                    setattr(item, "xal_DepartmentName", self)
                    

    @property
    def xal_Department167(self):
        return self.__xal_Department167

    @xal_Department167.setter
    def xal_Department167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department167", None)
        self.__xal_Department167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser166"):
                opp_val = getattr(old_value, "xal_LargeMailUser166", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser166"):
                opp_val = getattr(value, "xal_LargeMailUser166", None)
                setattr(value, "xal_LargeMailUser166", self)

    @property
    def xal_Department110(self):
        return self.__xal_Department110

    @xal_Department110.setter
    def xal_Department110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department110", None)
        self.__xal_Department110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot109"):
                opp_val = getattr(old_value, "xal_DocumentRoot109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot109"):
                opp_val = getattr(value, "xal_DocumentRoot109", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_Department50(self):
        return self.__xal_Department50

    @xal_Department50.setter
    def xal_Department50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department50", None)
        self.__xal_Department50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop"):
                opp_val = getattr(old_value, "xal_MailStop", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop"):
                opp_val = getattr(value, "xal_MailStop", None)
                setattr(value, "xal_MailStop", self)

    @property
    def xal_Department149(self):
        return self.__xal_Department149

    @xal_Department149.setter
    def xal_Department149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department149", None)
        self.__xal_Department149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm148"):
                opp_val = getattr(old_value, "xal_Firm148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm148"):
                opp_val = getattr(value, "xal_Firm148", None)
                if opp_val is None:
                    setattr(value, "xal_Firm148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_Department52(self):
        return self.__xal_Department52

    @xal_Department52.setter
    def xal_Department52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department52", None)
        self.__xal_Department52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode53"):
                opp_val = getattr(old_value, "xal_PostalCode53", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode53"):
                opp_val = getattr(value, "xal_PostalCode53", None)
                setattr(value, "xal_PostalCode53", self)

    @property
    def xal_Department(self):
        return self.__xal_Department

    @xal_Department.setter
    def xal_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Department__xal_Department", None)
        self.__xal_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine46"):
                    opp_val = getattr(item, "xal_AddressLine46", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine46"):
                    opp_val = getattr(item, "xal_AddressLine46", None)
                    
                    setattr(item, "xal_AddressLine46", self)
                    

class xal_MailStop:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_MailStop: "xal_Department" = None, xal_MailStop152: "xal_Firm" = None, xal_MailStop207: set["xal_AddressLine"] = None, xal_MailStop210: "xal_MailStopName" = None, xal_MailStop212: "xal_MailStopNumber" = None, xal_MailStop320: "xal_Premise" = None, xal_MailStop390: "xal_SubPremise" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_MailStop = xal_MailStop
        self.xal_MailStop152 = xal_MailStop152
        self.xal_MailStop207 = xal_MailStop207 if xal_MailStop207 is not None else set()
        self.xal_MailStop210 = xal_MailStop210
        self.xal_MailStop212 = xal_MailStop212
        self.xal_MailStop320 = xal_MailStop320
        self.xal_MailStop390 = xal_MailStop390
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_MailStop(self):
        return self.__xal_MailStop

    @xal_MailStop.setter
    def xal_MailStop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop", None)
        self.__xal_MailStop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Department50"):
                opp_val = getattr(old_value, "xal_Department50", None)
                if opp_val == self:
                    setattr(old_value, "xal_Department50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Department50"):
                opp_val = getattr(value, "xal_Department50", None)
                setattr(value, "xal_Department50", self)

    @property
    def xal_MailStop207(self):
        return self.__xal_MailStop207

    @xal_MailStop207.setter
    def xal_MailStop207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop207", None)
        self.__xal_MailStop207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine208"):
                    opp_val = getattr(item, "xal_AddressLine208", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine208"):
                    opp_val = getattr(item, "xal_AddressLine208", None)
                    
                    setattr(item, "xal_AddressLine208", self)
                    

    @property
    def xal_MailStop390(self):
        return self.__xal_MailStop390

    @xal_MailStop390.setter
    def xal_MailStop390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop390", None)
        self.__xal_MailStop390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise389"):
                opp_val = getattr(old_value, "xal_SubPremise389", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise389"):
                opp_val = getattr(value, "xal_SubPremise389", None)
                setattr(value, "xal_SubPremise389", self)

    @property
    def xal_MailStop212(self):
        return self.__xal_MailStop212

    @xal_MailStop212.setter
    def xal_MailStop212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop212", None)
        self.__xal_MailStop212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStopNumber"):
                opp_val = getattr(old_value, "xal_MailStopNumber", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStopNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStopNumber"):
                opp_val = getattr(value, "xal_MailStopNumber", None)
                setattr(value, "xal_MailStopNumber", self)

    @property
    def xal_MailStop152(self):
        return self.__xal_MailStop152

    @xal_MailStop152.setter
    def xal_MailStop152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop152", None)
        self.__xal_MailStop152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm151"):
                opp_val = getattr(old_value, "xal_Firm151", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm151"):
                opp_val = getattr(value, "xal_Firm151", None)
                setattr(value, "xal_Firm151", self)

    @property
    def xal_MailStop210(self):
        return self.__xal_MailStop210

    @xal_MailStop210.setter
    def xal_MailStop210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop210", None)
        self.__xal_MailStop210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStopName"):
                opp_val = getattr(old_value, "xal_MailStopName", None)
                if opp_val == self:
                    setattr(old_value, "xal_MailStopName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStopName"):
                opp_val = getattr(value, "xal_MailStopName", None)
                setattr(value, "xal_MailStopName", self)

    @property
    def xal_MailStop320(self):
        return self.__xal_MailStop320

    @xal_MailStop320.setter
    def xal_MailStop320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_MailStop__xal_MailStop320", None)
        self.__xal_MailStop320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise319"):
                opp_val = getattr(old_value, "xal_Premise319", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise319"):
                opp_val = getattr(value, "xal_Premise319", None)
                setattr(value, "xal_Premise319", self)

class xal_DepartmentName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_DepartmentName: "xal_Department" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_DepartmentName = xal_DepartmentName
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_DepartmentName(self):
        return self.__xal_DepartmentName

    @xal_DepartmentName.setter
    def xal_DepartmentName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_DepartmentName__xal_DepartmentName", None)
        self.__xal_DepartmentName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Department48"):
                opp_val = getattr(old_value, "xal_Department48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Department48"):
                opp_val = getattr(value, "xal_Department48", None)
                if opp_val is None:
                    setattr(value, "xal_Department48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_CountryName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_CountryName: "xal_Country" = None, xal_CountryName107: "xal_DocumentRoot" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_CountryName = xal_CountryName
        self.xal_CountryName107 = xal_CountryName107
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_CountryName(self):
        return self.__xal_CountryName

    @xal_CountryName.setter
    def xal_CountryName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_CountryName__xal_CountryName", None)
        self.__xal_CountryName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country35"):
                opp_val = getattr(old_value, "xal_Country35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country35"):
                opp_val = getattr(value, "xal_Country35", None)
                if opp_val is None:
                    setattr(value, "xal_Country35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_CountryName107(self):
        return self.__xal_CountryName107

    @xal_CountryName107.setter
    def xal_CountryName107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_CountryName__xal_CountryName107", None)
        self.__xal_CountryName107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot106"):
                opp_val = getattr(old_value, "xal_DocumentRoot106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot106"):
                opp_val = getattr(value, "xal_DocumentRoot106", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_Barcode:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_Barcode: "xal_PostalServiceElements" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_Barcode = xal_Barcode
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_Barcode(self):
        return self.__xal_Barcode

    @xal_Barcode.setter
    def xal_Barcode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Barcode__xal_Barcode", None)
        self.__xal_Barcode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements239"):
                opp_val = getattr(old_value, "xal_PostalServiceElements239", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements239"):
                opp_val = getattr(value, "xal_PostalServiceElements239", None)
                setattr(value, "xal_PostalServiceElements239", self)

class xal_CountryNameCode:

    def __init__(self, mixed: str, code: str, scheme: str, anyAttribute: str, xal_CountryNameCode: "xal_Country" = None):
        self.mixed = mixed
        self.code = code
        self.scheme = scheme
        self.anyAttribute = anyAttribute
        self.xal_CountryNameCode = xal_CountryNameCode
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_CountryNameCode(self):
        return self.__xal_CountryNameCode

    @xal_CountryNameCode.setter
    def xal_CountryNameCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_CountryNameCode__xal_CountryNameCode", None)
        self.__xal_CountryNameCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country33"):
                opp_val = getattr(old_value, "xal_Country33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country33"):
                opp_val = getattr(value, "xal_Country33", None)
                if opp_val is None:
                    setattr(value, "xal_Country33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_BuildingName:

    def __init__(self, mixed: str, code: str, type: str, typeOccurrence: str, anyAttribute: str, xal_BuildingName: "xal_LargeMailUser" = None, xal_BuildingName312: "xal_Premise" = None, xal_BuildingName384: "xal_SubPremise" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.typeOccurrence = typeOccurrence
        self.anyAttribute = anyAttribute
        self.xal_BuildingName = xal_BuildingName
        self.xal_BuildingName312 = xal_BuildingName312
        self.xal_BuildingName384 = xal_BuildingName384
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def typeOccurrence(self) -> str:
        return self.__typeOccurrence

    @typeOccurrence.setter
    def typeOccurrence(self, typeOccurrence: str):
        self.__typeOccurrence = typeOccurrence

    @property
    def xal_BuildingName(self):
        return self.__xal_BuildingName

    @xal_BuildingName.setter
    def xal_BuildingName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_BuildingName__xal_BuildingName", None)
        self.__xal_BuildingName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser164"):
                opp_val = getattr(old_value, "xal_LargeMailUser164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser164"):
                opp_val = getattr(value, "xal_LargeMailUser164", None)
                if opp_val is None:
                    setattr(value, "xal_LargeMailUser164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_BuildingName312(self):
        return self.__xal_BuildingName312

    @xal_BuildingName312.setter
    def xal_BuildingName312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_BuildingName__xal_BuildingName312", None)
        self.__xal_BuildingName312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise311"):
                opp_val = getattr(old_value, "xal_Premise311", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise311"):
                opp_val = getattr(value, "xal_Premise311", None)
                if opp_val is None:
                    setattr(value, "xal_Premise311", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_BuildingName384(self):
        return self.__xal_BuildingName384

    @xal_BuildingName384.setter
    def xal_BuildingName384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_BuildingName__xal_BuildingName384", None)
        self.__xal_BuildingName384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise383"):
                opp_val = getattr(old_value, "xal_SubPremise383", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise383"):
                opp_val = getattr(value, "xal_SubPremise383", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise383", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostalCode:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_PostalCode: "xal_AdministrativeArea" = None, xal_PostalCode53: "xal_Department" = None, xal_PostalCode79: "xal_DependentLocality" = None, xal_PostalCode116: "xal_DocumentRoot" = None, xal_PostalCode155: "xal_Firm" = None, xal_PostalCode176: "xal_LargeMailUser" = None, xal_PostalCode205: "xal_Locality" = None, xal_PostalCode214: set["xal_AddressLine"] = None, xal_PostalCode217: set["xal_PostalCodeNumber"] = None, xal_PostalCode219: set["xal_PostalCodeNumberExtension"] = None, xal_PostalCode221: "xal_PostTown" = None, xal_PostalCode268: "xal_PostBox" = None, xal_PostalCode284: "xal_PostOffice" = None, xal_PostalCode323: "xal_Premise" = None, xal_PostalCode368: "xal_SubAdministrativeArea" = None, xal_PostalCode393: "xal_SubPremise" = None, xal_PostalCode440: "xal_Thoroughfare" = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostalCode = xal_PostalCode
        self.xal_PostalCode53 = xal_PostalCode53
        self.xal_PostalCode79 = xal_PostalCode79
        self.xal_PostalCode116 = xal_PostalCode116
        self.xal_PostalCode155 = xal_PostalCode155
        self.xal_PostalCode176 = xal_PostalCode176
        self.xal_PostalCode205 = xal_PostalCode205
        self.xal_PostalCode214 = xal_PostalCode214 if xal_PostalCode214 is not None else set()
        self.xal_PostalCode217 = xal_PostalCode217 if xal_PostalCode217 is not None else set()
        self.xal_PostalCode219 = xal_PostalCode219 if xal_PostalCode219 is not None else set()
        self.xal_PostalCode221 = xal_PostalCode221
        self.xal_PostalCode268 = xal_PostalCode268
        self.xal_PostalCode284 = xal_PostalCode284
        self.xal_PostalCode323 = xal_PostalCode323
        self.xal_PostalCode368 = xal_PostalCode368
        self.xal_PostalCode393 = xal_PostalCode393
        self.xal_PostalCode440 = xal_PostalCode440
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_PostalCode116(self):
        return self.__xal_PostalCode116

    @xal_PostalCode116.setter
    def xal_PostalCode116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode116", None)
        self.__xal_PostalCode116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot115"):
                opp_val = getattr(old_value, "xal_DocumentRoot115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot115"):
                opp_val = getattr(value, "xal_DocumentRoot115", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PostalCode205(self):
        return self.__xal_PostalCode205

    @xal_PostalCode205.setter
    def xal_PostalCode205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode205", None)
        self.__xal_PostalCode205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality204"):
                opp_val = getattr(old_value, "xal_Locality204", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality204"):
                opp_val = getattr(value, "xal_Locality204", None)
                setattr(value, "xal_Locality204", self)

    @property
    def xal_PostalCode368(self):
        return self.__xal_PostalCode368

    @xal_PostalCode368.setter
    def xal_PostalCode368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode368", None)
        self.__xal_PostalCode368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea367"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea367", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubAdministrativeArea367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea367"):
                opp_val = getattr(value, "xal_SubAdministrativeArea367", None)
                setattr(value, "xal_SubAdministrativeArea367", self)

    @property
    def xal_PostalCode440(self):
        return self.__xal_PostalCode440

    @xal_PostalCode440.setter
    def xal_PostalCode440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode440", None)
        self.__xal_PostalCode440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare439"):
                opp_val = getattr(old_value, "xal_Thoroughfare439", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare439", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare439"):
                opp_val = getattr(value, "xal_Thoroughfare439", None)
                setattr(value, "xal_Thoroughfare439", self)

    @property
    def xal_PostalCode393(self):
        return self.__xal_PostalCode393

    @xal_PostalCode393.setter
    def xal_PostalCode393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode393", None)
        self.__xal_PostalCode393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise392"):
                opp_val = getattr(old_value, "xal_SubPremise392", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubPremise392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise392"):
                opp_val = getattr(value, "xal_SubPremise392", None)
                setattr(value, "xal_SubPremise392", self)

    @property
    def xal_PostalCode219(self):
        return self.__xal_PostalCode219

    @xal_PostalCode219.setter
    def xal_PostalCode219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode219", None)
        self.__xal_PostalCode219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostalCodeNumberExtension"):
                    opp_val = getattr(item, "xal_PostalCodeNumberExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostalCodeNumberExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostalCodeNumberExtension"):
                    opp_val = getattr(item, "xal_PostalCodeNumberExtension", None)
                    
                    setattr(item, "xal_PostalCodeNumberExtension", self)
                    

    @property
    def xal_PostalCode221(self):
        return self.__xal_PostalCode221

    @xal_PostalCode221.setter
    def xal_PostalCode221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode221", None)
        self.__xal_PostalCode221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostTown"):
                opp_val = getattr(old_value, "xal_PostTown", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostTown", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostTown"):
                opp_val = getattr(value, "xal_PostTown", None)
                setattr(value, "xal_PostTown", self)

    @property
    def xal_PostalCode53(self):
        return self.__xal_PostalCode53

    @xal_PostalCode53.setter
    def xal_PostalCode53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode53", None)
        self.__xal_PostalCode53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Department52"):
                opp_val = getattr(old_value, "xal_Department52", None)
                if opp_val == self:
                    setattr(old_value, "xal_Department52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Department52"):
                opp_val = getattr(value, "xal_Department52", None)
                setattr(value, "xal_Department52", self)

    @property
    def xal_PostalCode323(self):
        return self.__xal_PostalCode323

    @xal_PostalCode323.setter
    def xal_PostalCode323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode323", None)
        self.__xal_PostalCode323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise322"):
                opp_val = getattr(old_value, "xal_Premise322", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise322"):
                opp_val = getattr(value, "xal_Premise322", None)
                setattr(value, "xal_Premise322", self)

    @property
    def xal_PostalCode176(self):
        return self.__xal_PostalCode176

    @xal_PostalCode176.setter
    def xal_PostalCode176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode176", None)
        self.__xal_PostalCode176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser175"):
                opp_val = getattr(old_value, "xal_LargeMailUser175", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser175"):
                opp_val = getattr(value, "xal_LargeMailUser175", None)
                setattr(value, "xal_LargeMailUser175", self)

    @property
    def xal_PostalCode214(self):
        return self.__xal_PostalCode214

    @xal_PostalCode214.setter
    def xal_PostalCode214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode214", None)
        self.__xal_PostalCode214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine215"):
                    opp_val = getattr(item, "xal_AddressLine215", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine215"):
                    opp_val = getattr(item, "xal_AddressLine215", None)
                    
                    setattr(item, "xal_AddressLine215", self)
                    

    @property
    def xal_PostalCode155(self):
        return self.__xal_PostalCode155

    @xal_PostalCode155.setter
    def xal_PostalCode155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode155", None)
        self.__xal_PostalCode155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm154"):
                opp_val = getattr(old_value, "xal_Firm154", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm154"):
                opp_val = getattr(value, "xal_Firm154", None)
                setattr(value, "xal_Firm154", self)

    @property
    def xal_PostalCode268(self):
        return self.__xal_PostalCode268

    @xal_PostalCode268.setter
    def xal_PostalCode268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode268", None)
        self.__xal_PostalCode268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox267"):
                opp_val = getattr(old_value, "xal_PostBox267", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox267"):
                opp_val = getattr(value, "xal_PostBox267", None)
                setattr(value, "xal_PostBox267", self)

    @property
    def xal_PostalCode217(self):
        return self.__xal_PostalCode217

    @xal_PostalCode217.setter
    def xal_PostalCode217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode217", None)
        self.__xal_PostalCode217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostalCodeNumber"):
                    opp_val = getattr(item, "xal_PostalCodeNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostalCodeNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostalCodeNumber"):
                    opp_val = getattr(item, "xal_PostalCodeNumber", None)
                    
                    setattr(item, "xal_PostalCodeNumber", self)
                    

    @property
    def xal_PostalCode79(self):
        return self.__xal_PostalCode79

    @xal_PostalCode79.setter
    def xal_PostalCode79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode79", None)
        self.__xal_PostalCode79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality78"):
                opp_val = getattr(old_value, "xal_DependentLocality78", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality78"):
                opp_val = getattr(value, "xal_DependentLocality78", None)
                setattr(value, "xal_DependentLocality78", self)

    @property
    def xal_PostalCode284(self):
        return self.__xal_PostalCode284

    @xal_PostalCode284.setter
    def xal_PostalCode284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode284", None)
        self.__xal_PostalCode284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice283"):
                opp_val = getattr(old_value, "xal_PostOffice283", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice283"):
                opp_val = getattr(value, "xal_PostOffice283", None)
                setattr(value, "xal_PostOffice283", self)

    @property
    def xal_PostalCode(self):
        return self.__xal_PostalCode

    @xal_PostalCode.setter
    def xal_PostalCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalCode__xal_PostalCode", None)
        self.__xal_PostalCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea28"):
                opp_val = getattr(old_value, "xal_AdministrativeArea28", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea28"):
                opp_val = getattr(value, "xal_AdministrativeArea28", None)
                setattr(value, "xal_AdministrativeArea28", self)

class xal_AdministrativeAreaName:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_AdministrativeAreaName: "xal_AdministrativeArea" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_AdministrativeAreaName = xal_AdministrativeAreaName
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_AdministrativeAreaName(self):
        return self.__xal_AdministrativeAreaName

    @xal_AdministrativeAreaName.setter
    def xal_AdministrativeAreaName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeAreaName__xal_AdministrativeAreaName", None)
        self.__xal_AdministrativeAreaName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea19"):
                opp_val = getattr(old_value, "xal_AdministrativeArea19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea19"):
                opp_val = getattr(value, "xal_AdministrativeArea19", None)
                if opp_val is None:
                    setattr(value, "xal_AdministrativeArea19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_PostOffice:

    def __init__(self, any: str, indicator: str, type: str, anyAttribute: str, xal_PostOffice: "xal_AdministrativeArea" = None, xal_PostOffice66: "xal_DependentLocality" = None, xal_PostOffice122: "xal_DocumentRoot" = None, xal_PostOffice190: "xal_Locality" = None, xal_PostOffice270: set["xal_AddressLine"] = None, xal_PostOffice273: set["xal_PostOfficeName"] = None, xal_PostOffice275: "xal_PostOfficeNumber" = None, xal_PostOffice277: "xal_PostalRoute" = None, xal_PostOffice280: "xal_PostBox" = None, xal_PostOffice283: "xal_PostalCode" = None, xal_PostOffice365: "xal_SubAdministrativeArea" = None):
        self.any = any
        self.indicator = indicator
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostOffice = xal_PostOffice
        self.xal_PostOffice66 = xal_PostOffice66
        self.xal_PostOffice122 = xal_PostOffice122
        self.xal_PostOffice190 = xal_PostOffice190
        self.xal_PostOffice270 = xal_PostOffice270 if xal_PostOffice270 is not None else set()
        self.xal_PostOffice273 = xal_PostOffice273 if xal_PostOffice273 is not None else set()
        self.xal_PostOffice275 = xal_PostOffice275
        self.xal_PostOffice277 = xal_PostOffice277
        self.xal_PostOffice280 = xal_PostOffice280
        self.xal_PostOffice283 = xal_PostOffice283
        self.xal_PostOffice365 = xal_PostOffice365
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def xal_PostOffice283(self):
        return self.__xal_PostOffice283

    @xal_PostOffice283.setter
    def xal_PostOffice283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice283", None)
        self.__xal_PostOffice283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode284"):
                opp_val = getattr(old_value, "xal_PostalCode284", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode284"):
                opp_val = getattr(value, "xal_PostalCode284", None)
                setattr(value, "xal_PostalCode284", self)

    @property
    def xal_PostOffice280(self):
        return self.__xal_PostOffice280

    @xal_PostOffice280.setter
    def xal_PostOffice280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice280", None)
        self.__xal_PostOffice280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox281"):
                opp_val = getattr(old_value, "xal_PostBox281", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox281"):
                opp_val = getattr(value, "xal_PostBox281", None)
                setattr(value, "xal_PostBox281", self)

    @property
    def xal_PostOffice122(self):
        return self.__xal_PostOffice122

    @xal_PostOffice122.setter
    def xal_PostOffice122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice122", None)
        self.__xal_PostOffice122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot121"):
                opp_val = getattr(old_value, "xal_DocumentRoot121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot121"):
                opp_val = getattr(value, "xal_DocumentRoot121", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_PostOffice66(self):
        return self.__xal_PostOffice66

    @xal_PostOffice66.setter
    def xal_PostOffice66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice66", None)
        self.__xal_PostOffice66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality65"):
                opp_val = getattr(old_value, "xal_DependentLocality65", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality65"):
                opp_val = getattr(value, "xal_DependentLocality65", None)
                setattr(value, "xal_DependentLocality65", self)

    @property
    def xal_PostOffice270(self):
        return self.__xal_PostOffice270

    @xal_PostOffice270.setter
    def xal_PostOffice270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice270", None)
        self.__xal_PostOffice270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine271"):
                    opp_val = getattr(item, "xal_AddressLine271", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine271"):
                    opp_val = getattr(item, "xal_AddressLine271", None)
                    
                    setattr(item, "xal_AddressLine271", self)
                    

    @property
    def xal_PostOffice365(self):
        return self.__xal_PostOffice365

    @xal_PostOffice365.setter
    def xal_PostOffice365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice365", None)
        self.__xal_PostOffice365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea364"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea364", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubAdministrativeArea364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea364"):
                opp_val = getattr(value, "xal_SubAdministrativeArea364", None)
                setattr(value, "xal_SubAdministrativeArea364", self)

    @property
    def xal_PostOffice190(self):
        return self.__xal_PostOffice190

    @xal_PostOffice190.setter
    def xal_PostOffice190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice190", None)
        self.__xal_PostOffice190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality189"):
                opp_val = getattr(old_value, "xal_Locality189", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality189"):
                opp_val = getattr(value, "xal_Locality189", None)
                setattr(value, "xal_Locality189", self)

    @property
    def xal_PostOffice(self):
        return self.__xal_PostOffice

    @xal_PostOffice.setter
    def xal_PostOffice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice", None)
        self.__xal_PostOffice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea26"):
                opp_val = getattr(old_value, "xal_AdministrativeArea26", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea26"):
                opp_val = getattr(value, "xal_AdministrativeArea26", None)
                setattr(value, "xal_AdministrativeArea26", self)

    @property
    def xal_PostOffice273(self):
        return self.__xal_PostOffice273

    @xal_PostOffice273.setter
    def xal_PostOffice273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice273", None)
        self.__xal_PostOffice273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_PostOfficeName"):
                    opp_val = getattr(item, "xal_PostOfficeName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_PostOfficeName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_PostOfficeName"):
                    opp_val = getattr(item, "xal_PostOfficeName", None)
                    
                    setattr(item, "xal_PostOfficeName", self)
                    

    @property
    def xal_PostOffice275(self):
        return self.__xal_PostOffice275

    @xal_PostOffice275.setter
    def xal_PostOffice275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice275", None)
        self.__xal_PostOffice275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOfficeNumber"):
                opp_val = getattr(old_value, "xal_PostOfficeNumber", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOfficeNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOfficeNumber"):
                opp_val = getattr(value, "xal_PostOfficeNumber", None)
                setattr(value, "xal_PostOfficeNumber", self)

    @property
    def xal_PostOffice277(self):
        return self.__xal_PostOffice277

    @xal_PostOffice277.setter
    def xal_PostOffice277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostOffice__xal_PostOffice277", None)
        self.__xal_PostOffice277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute278"):
                opp_val = getattr(old_value, "xal_PostalRoute278", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRoute278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute278"):
                opp_val = getattr(value, "xal_PostalRoute278", None)
                setattr(value, "xal_PostalRoute278", self)

class xal_SubAdministrativeArea:

    def __init__(self, usageType: str, anyAttribute: str, any: str, indicator: str, type: str, xal_SubAdministrativeArea: "xal_AdministrativeArea" = None, xal_SubAdministrativeArea356: set["xal_AddressLine"] = None, xal_SubAdministrativeArea359: set["xal_SubAdministrativeAreaName"] = None, xal_SubAdministrativeArea361: "xal_Locality" = None, xal_SubAdministrativeArea364: "xal_PostOffice" = None, xal_SubAdministrativeArea367: "xal_PostalCode" = None):
        self.usageType = usageType
        self.anyAttribute = anyAttribute
        self.any = any
        self.indicator = indicator
        self.type = type
        self.xal_SubAdministrativeArea = xal_SubAdministrativeArea
        self.xal_SubAdministrativeArea356 = xal_SubAdministrativeArea356 if xal_SubAdministrativeArea356 is not None else set()
        self.xal_SubAdministrativeArea359 = xal_SubAdministrativeArea359 if xal_SubAdministrativeArea359 is not None else set()
        self.xal_SubAdministrativeArea361 = xal_SubAdministrativeArea361
        self.xal_SubAdministrativeArea364 = xal_SubAdministrativeArea364
        self.xal_SubAdministrativeArea367 = xal_SubAdministrativeArea367
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def usageType(self) -> str:
        return self.__usageType

    @usageType.setter
    def usageType(self, usageType: str):
        self.__usageType = usageType

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_SubAdministrativeArea359(self):
        return self.__xal_SubAdministrativeArea359

    @xal_SubAdministrativeArea359.setter
    def xal_SubAdministrativeArea359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea359", None)
        self.__xal_SubAdministrativeArea359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SubAdministrativeAreaName"):
                    opp_val = getattr(item, "xal_SubAdministrativeAreaName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SubAdministrativeAreaName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SubAdministrativeAreaName"):
                    opp_val = getattr(item, "xal_SubAdministrativeAreaName", None)
                    
                    setattr(item, "xal_SubAdministrativeAreaName", self)
                    

    @property
    def xal_SubAdministrativeArea361(self):
        return self.__xal_SubAdministrativeArea361

    @xal_SubAdministrativeArea361.setter
    def xal_SubAdministrativeArea361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea361", None)
        self.__xal_SubAdministrativeArea361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality362"):
                opp_val = getattr(old_value, "xal_Locality362", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality362"):
                opp_val = getattr(value, "xal_Locality362", None)
                setattr(value, "xal_Locality362", self)

    @property
    def xal_SubAdministrativeArea367(self):
        return self.__xal_SubAdministrativeArea367

    @xal_SubAdministrativeArea367.setter
    def xal_SubAdministrativeArea367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea367", None)
        self.__xal_SubAdministrativeArea367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode368"):
                opp_val = getattr(old_value, "xal_PostalCode368", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode368"):
                opp_val = getattr(value, "xal_PostalCode368", None)
                setattr(value, "xal_PostalCode368", self)

    @property
    def xal_SubAdministrativeArea356(self):
        return self.__xal_SubAdministrativeArea356

    @xal_SubAdministrativeArea356.setter
    def xal_SubAdministrativeArea356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea356", None)
        self.__xal_SubAdministrativeArea356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine357"):
                    opp_val = getattr(item, "xal_AddressLine357", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine357"):
                    opp_val = getattr(item, "xal_AddressLine357", None)
                    
                    setattr(item, "xal_AddressLine357", self)
                    

    @property
    def xal_SubAdministrativeArea(self):
        return self.__xal_SubAdministrativeArea

    @xal_SubAdministrativeArea.setter
    def xal_SubAdministrativeArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea", None)
        self.__xal_SubAdministrativeArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea21"):
                opp_val = getattr(old_value, "xal_AdministrativeArea21", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea21"):
                opp_val = getattr(value, "xal_AdministrativeArea21", None)
                setattr(value, "xal_AdministrativeArea21", self)

    @property
    def xal_SubAdministrativeArea364(self):
        return self.__xal_SubAdministrativeArea364

    @xal_SubAdministrativeArea364.setter
    def xal_SubAdministrativeArea364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_SubAdministrativeArea__xal_SubAdministrativeArea364", None)
        self.__xal_SubAdministrativeArea364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice365"):
                opp_val = getattr(old_value, "xal_PostOffice365", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice365"):
                opp_val = getattr(value, "xal_PostOffice365", None)
                setattr(value, "xal_PostOffice365", self)

class xal_AddressLongitudeDirection:

    def __init__(self, code: str, type: str, mixed: str, anyAttribute: str, xal_AddressLongitudeDirection: "xal_PostalServiceElements" = None):
        self.code = code
        self.type = type
        self.mixed = mixed
        self.anyAttribute = anyAttribute
        self.xal_AddressLongitudeDirection = xal_AddressLongitudeDirection
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_AddressLongitudeDirection(self):
        return self.__xal_AddressLongitudeDirection

    @xal_AddressLongitudeDirection.setter
    def xal_AddressLongitudeDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLongitudeDirection__xal_AddressLongitudeDirection", None)
        self.__xal_AddressLongitudeDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements249"):
                opp_val = getattr(old_value, "xal_PostalServiceElements249", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements249"):
                opp_val = getattr(value, "xal_PostalServiceElements249", None)
                setattr(value, "xal_PostalServiceElements249", self)

class xal_AddressLongitude:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_AddressLongitude: "xal_PostalServiceElements" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_AddressLongitude = xal_AddressLongitude
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_AddressLongitude(self):
        return self.__xal_AddressLongitude

    @xal_AddressLongitude.setter
    def xal_AddressLongitude(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLongitude__xal_AddressLongitude", None)
        self.__xal_AddressLongitude = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements247"):
                opp_val = getattr(old_value, "xal_PostalServiceElements247", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements247"):
                opp_val = getattr(value, "xal_PostalServiceElements247", None)
                setattr(value, "xal_PostalServiceElements247", self)

class xal_AddressLine:

    def __init__(self, code: str, mixed: str, type: str, anyAttribute: str, xal_AddressLine: "xal_AddressLines" = None, xal_AddressLine17: "xal_AdministrativeArea" = None, xal_AddressLine31: "xal_Country" = None, xal_AddressLine46: "xal_Department" = None, xal_AddressLine55: "xal_DependentLocality" = None, xal_AddressLine81: "xal_DependentThoroughfare" = None, xal_AddressLine101: "xal_DocumentRoot" = None, xal_AddressLine144: "xal_Firm" = None, xal_AddressLine158: "xal_LargeMailUser" = None, xal_AddressLine179: "xal_Locality" = None, xal_AddressLine208: "xal_MailStop" = None, xal_AddressLine215: "xal_PostalCode" = None, xal_AddressLine224: "xal_PostalRoute" = None, xal_AddressLine254: "xal_PostBox" = None, xal_AddressLine271: "xal_PostOffice" = None, xal_AddressLine287: "xal_PostTown" = None, xal_AddressLine294: "xal_Premise" = None, xal_AddressLine333: "xal_PremiseNumberRangeFrom" = None, xal_AddressLine345: "xal_PremiseNumberRangeTo" = None, xal_AddressLine357: "xal_SubAdministrativeArea" = None, xal_AddressLine371: "xal_SubPremise" = None, xal_AddressLine399: "xal_Thoroughfare" = None, xal_AddressLine442: "xal_ThoroughfareNumberFrom" = None, xal_AddressLine454: "xal_ThoroughfareNumberRange" = None, xal_AddressLine462: "xal_ThoroughfareNumberTo" = None):
        self.code = code
        self.mixed = mixed
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_AddressLine = xal_AddressLine
        self.xal_AddressLine17 = xal_AddressLine17
        self.xal_AddressLine31 = xal_AddressLine31
        self.xal_AddressLine46 = xal_AddressLine46
        self.xal_AddressLine55 = xal_AddressLine55
        self.xal_AddressLine81 = xal_AddressLine81
        self.xal_AddressLine101 = xal_AddressLine101
        self.xal_AddressLine144 = xal_AddressLine144
        self.xal_AddressLine158 = xal_AddressLine158
        self.xal_AddressLine179 = xal_AddressLine179
        self.xal_AddressLine208 = xal_AddressLine208
        self.xal_AddressLine215 = xal_AddressLine215
        self.xal_AddressLine224 = xal_AddressLine224
        self.xal_AddressLine254 = xal_AddressLine254
        self.xal_AddressLine271 = xal_AddressLine271
        self.xal_AddressLine287 = xal_AddressLine287
        self.xal_AddressLine294 = xal_AddressLine294
        self.xal_AddressLine333 = xal_AddressLine333
        self.xal_AddressLine345 = xal_AddressLine345
        self.xal_AddressLine357 = xal_AddressLine357
        self.xal_AddressLine371 = xal_AddressLine371
        self.xal_AddressLine399 = xal_AddressLine399
        self.xal_AddressLine442 = xal_AddressLine442
        self.xal_AddressLine454 = xal_AddressLine454
        self.xal_AddressLine462 = xal_AddressLine462
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_AddressLine333(self):
        return self.__xal_AddressLine333

    @xal_AddressLine333.setter
    def xal_AddressLine333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine333", None)
        self.__xal_AddressLine333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeFrom332"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeFrom332", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeFrom332"):
                opp_val = getattr(value, "xal_PremiseNumberRangeFrom332", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeFrom332", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine144(self):
        return self.__xal_AddressLine144

    @xal_AddressLine144.setter
    def xal_AddressLine144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine144", None)
        self.__xal_AddressLine144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm"):
                opp_val = getattr(old_value, "xal_Firm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm"):
                opp_val = getattr(value, "xal_Firm", None)
                if opp_val is None:
                    setattr(value, "xal_Firm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine357(self):
        return self.__xal_AddressLine357

    @xal_AddressLine357.setter
    def xal_AddressLine357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine357", None)
        self.__xal_AddressLine357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea356"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea356", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea356"):
                opp_val = getattr(value, "xal_SubAdministrativeArea356", None)
                if opp_val is None:
                    setattr(value, "xal_SubAdministrativeArea356", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine215(self):
        return self.__xal_AddressLine215

    @xal_AddressLine215.setter
    def xal_AddressLine215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine215", None)
        self.__xal_AddressLine215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode214"):
                opp_val = getattr(old_value, "xal_PostalCode214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode214"):
                opp_val = getattr(value, "xal_PostalCode214", None)
                if opp_val is None:
                    setattr(value, "xal_PostalCode214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine208(self):
        return self.__xal_AddressLine208

    @xal_AddressLine208.setter
    def xal_AddressLine208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine208", None)
        self.__xal_AddressLine208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_MailStop207"):
                opp_val = getattr(old_value, "xal_MailStop207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_MailStop207"):
                opp_val = getattr(value, "xal_MailStop207", None)
                if opp_val is None:
                    setattr(value, "xal_MailStop207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine399(self):
        return self.__xal_AddressLine399

    @xal_AddressLine399.setter
    def xal_AddressLine399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine399", None)
        self.__xal_AddressLine399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare398"):
                opp_val = getattr(old_value, "xal_Thoroughfare398", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare398"):
                opp_val = getattr(value, "xal_Thoroughfare398", None)
                if opp_val is None:
                    setattr(value, "xal_Thoroughfare398", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine371(self):
        return self.__xal_AddressLine371

    @xal_AddressLine371.setter
    def xal_AddressLine371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine371", None)
        self.__xal_AddressLine371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubPremise370"):
                opp_val = getattr(old_value, "xal_SubPremise370", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubPremise370"):
                opp_val = getattr(value, "xal_SubPremise370", None)
                if opp_val is None:
                    setattr(value, "xal_SubPremise370", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine454(self):
        return self.__xal_AddressLine454

    @xal_AddressLine454.setter
    def xal_AddressLine454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine454", None)
        self.__xal_AddressLine454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberRange453"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberRange453", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberRange453"):
                opp_val = getattr(value, "xal_ThoroughfareNumberRange453", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberRange453", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine287(self):
        return self.__xal_AddressLine287

    @xal_AddressLine287.setter
    def xal_AddressLine287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine287", None)
        self.__xal_AddressLine287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostTown286"):
                opp_val = getattr(old_value, "xal_PostTown286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostTown286"):
                opp_val = getattr(value, "xal_PostTown286", None)
                if opp_val is None:
                    setattr(value, "xal_PostTown286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine17(self):
        return self.__xal_AddressLine17

    @xal_AddressLine17.setter
    def xal_AddressLine17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine17", None)
        self.__xal_AddressLine17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea16"):
                opp_val = getattr(old_value, "xal_AdministrativeArea16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea16"):
                opp_val = getattr(value, "xal_AdministrativeArea16", None)
                if opp_val is None:
                    setattr(value, "xal_AdministrativeArea16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine158(self):
        return self.__xal_AddressLine158

    @xal_AddressLine158.setter
    def xal_AddressLine158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine158", None)
        self.__xal_AddressLine158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser157"):
                opp_val = getattr(old_value, "xal_LargeMailUser157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser157"):
                opp_val = getattr(value, "xal_LargeMailUser157", None)
                if opp_val is None:
                    setattr(value, "xal_LargeMailUser157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine462(self):
        return self.__xal_AddressLine462

    @xal_AddressLine462.setter
    def xal_AddressLine462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine462", None)
        self.__xal_AddressLine462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberTo461"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberTo461", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberTo461"):
                opp_val = getattr(value, "xal_ThoroughfareNumberTo461", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberTo461", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine179(self):
        return self.__xal_AddressLine179

    @xal_AddressLine179.setter
    def xal_AddressLine179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine179", None)
        self.__xal_AddressLine179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality178"):
                opp_val = getattr(old_value, "xal_Locality178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality178"):
                opp_val = getattr(value, "xal_Locality178", None)
                if opp_val is None:
                    setattr(value, "xal_Locality178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine101(self):
        return self.__xal_AddressLine101

    @xal_AddressLine101.setter
    def xal_AddressLine101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine101", None)
        self.__xal_AddressLine101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot100"):
                opp_val = getattr(old_value, "xal_DocumentRoot100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot100"):
                opp_val = getattr(value, "xal_DocumentRoot100", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine31(self):
        return self.__xal_AddressLine31

    @xal_AddressLine31.setter
    def xal_AddressLine31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine31", None)
        self.__xal_AddressLine31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country30"):
                opp_val = getattr(old_value, "xal_Country30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country30"):
                opp_val = getattr(value, "xal_Country30", None)
                if opp_val is None:
                    setattr(value, "xal_Country30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine271(self):
        return self.__xal_AddressLine271

    @xal_AddressLine271.setter
    def xal_AddressLine271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine271", None)
        self.__xal_AddressLine271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice270"):
                opp_val = getattr(old_value, "xal_PostOffice270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice270"):
                opp_val = getattr(value, "xal_PostOffice270", None)
                if opp_val is None:
                    setattr(value, "xal_PostOffice270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine224(self):
        return self.__xal_AddressLine224

    @xal_AddressLine224.setter
    def xal_AddressLine224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine224", None)
        self.__xal_AddressLine224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute223"):
                opp_val = getattr(old_value, "xal_PostalRoute223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute223"):
                opp_val = getattr(value, "xal_PostalRoute223", None)
                if opp_val is None:
                    setattr(value, "xal_PostalRoute223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine294(self):
        return self.__xal_AddressLine294

    @xal_AddressLine294.setter
    def xal_AddressLine294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine294", None)
        self.__xal_AddressLine294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise293"):
                opp_val = getattr(old_value, "xal_Premise293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise293"):
                opp_val = getattr(value, "xal_Premise293", None)
                if opp_val is None:
                    setattr(value, "xal_Premise293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine46(self):
        return self.__xal_AddressLine46

    @xal_AddressLine46.setter
    def xal_AddressLine46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine46", None)
        self.__xal_AddressLine46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Department"):
                opp_val = getattr(old_value, "xal_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Department"):
                opp_val = getattr(value, "xal_Department", None)
                if opp_val is None:
                    setattr(value, "xal_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine254(self):
        return self.__xal_AddressLine254

    @xal_AddressLine254.setter
    def xal_AddressLine254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine254", None)
        self.__xal_AddressLine254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox253"):
                opp_val = getattr(old_value, "xal_PostBox253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox253"):
                opp_val = getattr(value, "xal_PostBox253", None)
                if opp_val is None:
                    setattr(value, "xal_PostBox253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine(self):
        return self.__xal_AddressLine

    @xal_AddressLine.setter
    def xal_AddressLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine", None)
        self.__xal_AddressLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLines14"):
                opp_val = getattr(old_value, "xal_AddressLines14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLines14"):
                opp_val = getattr(value, "xal_AddressLines14", None)
                if opp_val is None:
                    setattr(value, "xal_AddressLines14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine81(self):
        return self.__xal_AddressLine81

    @xal_AddressLine81.setter
    def xal_AddressLine81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine81", None)
        self.__xal_AddressLine81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare"):
                opp_val = getattr(value, "xal_DependentThoroughfare", None)
                if opp_val is None:
                    setattr(value, "xal_DependentThoroughfare", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine442(self):
        return self.__xal_AddressLine442

    @xal_AddressLine442.setter
    def xal_AddressLine442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine442", None)
        self.__xal_AddressLine442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareNumberFrom"):
                opp_val = getattr(old_value, "xal_ThoroughfareNumberFrom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareNumberFrom"):
                opp_val = getattr(value, "xal_ThoroughfareNumberFrom", None)
                if opp_val is None:
                    setattr(value, "xal_ThoroughfareNumberFrom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine345(self):
        return self.__xal_AddressLine345

    @xal_AddressLine345.setter
    def xal_AddressLine345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine345", None)
        self.__xal_AddressLine345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PremiseNumberRangeTo344"):
                opp_val = getattr(old_value, "xal_PremiseNumberRangeTo344", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PremiseNumberRangeTo344"):
                opp_val = getattr(value, "xal_PremiseNumberRangeTo344", None)
                if opp_val is None:
                    setattr(value, "xal_PremiseNumberRangeTo344", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressLine55(self):
        return self.__xal_AddressLine55

    @xal_AddressLine55.setter
    def xal_AddressLine55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLine__xal_AddressLine55", None)
        self.__xal_AddressLine55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality"):
                opp_val = getattr(old_value, "xal_DependentLocality", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality"):
                opp_val = getattr(value, "xal_DependentLocality", None)
                if opp_val is None:
                    setattr(value, "xal_DependentLocality", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_AddressLatitudeDirection:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_AddressLatitudeDirection: "xal_PostalServiceElements" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_AddressLatitudeDirection = xal_AddressLatitudeDirection
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_AddressLatitudeDirection(self):
        return self.__xal_AddressLatitudeDirection

    @xal_AddressLatitudeDirection.setter
    def xal_AddressLatitudeDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLatitudeDirection__xal_AddressLatitudeDirection", None)
        self.__xal_AddressLatitudeDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements245"):
                opp_val = getattr(old_value, "xal_PostalServiceElements245", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements245"):
                opp_val = getattr(value, "xal_PostalServiceElements245", None)
                setattr(value, "xal_PostalServiceElements245", self)

class xal_AddressLatitude:

    def __init__(self, anyAttribute: str, mixed: str, code: str, type: str, xal_AddressLatitude: "xal_PostalServiceElements" = None):
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.code = code
        self.type = type
        self.xal_AddressLatitude = xal_AddressLatitude
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def xal_AddressLatitude(self):
        return self.__xal_AddressLatitude

    @xal_AddressLatitude.setter
    def xal_AddressLatitude(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLatitude__xal_AddressLatitude", None)
        self.__xal_AddressLatitude = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements243"):
                opp_val = getattr(old_value, "xal_PostalServiceElements243", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements243"):
                opp_val = getattr(value, "xal_PostalServiceElements243", None)
                setattr(value, "xal_PostalServiceElements243", self)

class xal_AddressIdentifier:

    def __init__(self, code: str, mixed: str, identifierType: str, type: str, anyAttribute: str, xal_AddressIdentifier: "xal_PostalServiceElements" = None):
        self.code = code
        self.mixed = mixed
        self.identifierType = identifierType
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_AddressIdentifier = xal_AddressIdentifier
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def identifierType(self) -> str:
        return self.__identifierType

    @identifierType.setter
    def identifierType(self, identifierType: str):
        self.__identifierType = identifierType

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_AddressIdentifier(self):
        return self.__xal_AddressIdentifier

    @xal_AddressIdentifier.setter
    def xal_AddressIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressIdentifier__xal_AddressIdentifier", None)
        self.__xal_AddressIdentifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements233"):
                opp_val = getattr(old_value, "xal_PostalServiceElements233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements233"):
                opp_val = getattr(value, "xal_PostalServiceElements233", None)
                if opp_val is None:
                    setattr(value, "xal_PostalServiceElements233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_Thoroughfare:

    def __init__(self, group: str, any: str, dependentThoroughfaresIndicator: str, dependentThoroughfaresType: str, type: str, anyAttribute: str, dependentThoroughfares: str, dependentThoroughfaresConnector: str, xal_Thoroughfare: "xal_AddressDetails" = None, xal_Thoroughfare44: "xal_Country" = None, xal_Thoroughfare71: "xal_DependentLocality" = None, xal_Thoroughfare134: "xal_DocumentRoot" = None, xal_Thoroughfare173: "xal_LargeMailUser" = None, xal_Thoroughfare196: "xal_Locality" = None, xal_Thoroughfare401: set["xal_ThoroughfareNumber"] = None, xal_Thoroughfare404: set["xal_ThoroughfareNumberRange"] = None, xal_Thoroughfare398: set["xal_AddressLine"] = None, xal_Thoroughfare409: set["xal_ThoroughfareNumberSuffix"] = None, xal_Thoroughfare412: "xal_ThoroughfarePreDirection" = None, xal_Thoroughfare415: "xal_ThoroughfareLeadingType" = None, xal_Thoroughfare406: set["xal_ThoroughfareNumberPrefix"] = None, xal_Thoroughfare421: "xal_ThoroughfareTrailingType" = None, xal_Thoroughfare424: "xal_ThoroughfarePostDirection" = None, xal_Thoroughfare427: "xal_DependentThoroughfare" = None, xal_Thoroughfare430: "xal_DependentLocality" = None, xal_Thoroughfare418: set["xal_ThoroughfareName"] = None, xal_Thoroughfare436: "xal_Firm" = None, xal_Thoroughfare439: "xal_PostalCode" = None, xal_Thoroughfare433: "xal_Premise" = None):
        self.group = group
        self.any = any
        self.dependentThoroughfaresIndicator = dependentThoroughfaresIndicator
        self.dependentThoroughfaresType = dependentThoroughfaresType
        self.type = type
        self.anyAttribute = anyAttribute
        self.dependentThoroughfares = dependentThoroughfares
        self.dependentThoroughfaresConnector = dependentThoroughfaresConnector
        self.xal_Thoroughfare = xal_Thoroughfare
        self.xal_Thoroughfare44 = xal_Thoroughfare44
        self.xal_Thoroughfare71 = xal_Thoroughfare71
        self.xal_Thoroughfare134 = xal_Thoroughfare134
        self.xal_Thoroughfare173 = xal_Thoroughfare173
        self.xal_Thoroughfare196 = xal_Thoroughfare196
        self.xal_Thoroughfare401 = xal_Thoroughfare401 if xal_Thoroughfare401 is not None else set()
        self.xal_Thoroughfare404 = xal_Thoroughfare404 if xal_Thoroughfare404 is not None else set()
        self.xal_Thoroughfare398 = xal_Thoroughfare398 if xal_Thoroughfare398 is not None else set()
        self.xal_Thoroughfare409 = xal_Thoroughfare409 if xal_Thoroughfare409 is not None else set()
        self.xal_Thoroughfare412 = xal_Thoroughfare412
        self.xal_Thoroughfare415 = xal_Thoroughfare415
        self.xal_Thoroughfare406 = xal_Thoroughfare406 if xal_Thoroughfare406 is not None else set()
        self.xal_Thoroughfare421 = xal_Thoroughfare421
        self.xal_Thoroughfare424 = xal_Thoroughfare424
        self.xal_Thoroughfare427 = xal_Thoroughfare427
        self.xal_Thoroughfare430 = xal_Thoroughfare430
        self.xal_Thoroughfare418 = xal_Thoroughfare418 if xal_Thoroughfare418 is not None else set()
        self.xal_Thoroughfare436 = xal_Thoroughfare436
        self.xal_Thoroughfare439 = xal_Thoroughfare439
        self.xal_Thoroughfare433 = xal_Thoroughfare433
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def dependentThoroughfaresType(self) -> str:
        return self.__dependentThoroughfaresType

    @dependentThoroughfaresType.setter
    def dependentThoroughfaresType(self, dependentThoroughfaresType: str):
        self.__dependentThoroughfaresType = dependentThoroughfaresType

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def dependentThoroughfaresConnector(self) -> str:
        return self.__dependentThoroughfaresConnector

    @dependentThoroughfaresConnector.setter
    def dependentThoroughfaresConnector(self, dependentThoroughfaresConnector: str):
        self.__dependentThoroughfaresConnector = dependentThoroughfaresConnector

    @property
    def dependentThoroughfares(self) -> str:
        return self.__dependentThoroughfares

    @dependentThoroughfares.setter
    def dependentThoroughfares(self, dependentThoroughfares: str):
        self.__dependentThoroughfares = dependentThoroughfares

    @property
    def dependentThoroughfaresIndicator(self) -> str:
        return self.__dependentThoroughfaresIndicator

    @dependentThoroughfaresIndicator.setter
    def dependentThoroughfaresIndicator(self, dependentThoroughfaresIndicator: str):
        self.__dependentThoroughfaresIndicator = dependentThoroughfaresIndicator

    @property
    def xal_Thoroughfare424(self):
        return self.__xal_Thoroughfare424

    @xal_Thoroughfare424.setter
    def xal_Thoroughfare424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare424", None)
        self.__xal_Thoroughfare424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfarePostDirection425"):
                opp_val = getattr(old_value, "xal_ThoroughfarePostDirection425", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfarePostDirection425", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfarePostDirection425"):
                opp_val = getattr(value, "xal_ThoroughfarePostDirection425", None)
                setattr(value, "xal_ThoroughfarePostDirection425", self)

    @property
    def xal_Thoroughfare196(self):
        return self.__xal_Thoroughfare196

    @xal_Thoroughfare196.setter
    def xal_Thoroughfare196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare196", None)
        self.__xal_Thoroughfare196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality195"):
                opp_val = getattr(old_value, "xal_Locality195", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality195"):
                opp_val = getattr(value, "xal_Locality195", None)
                setattr(value, "xal_Locality195", self)

    @property
    def xal_Thoroughfare398(self):
        return self.__xal_Thoroughfare398

    @xal_Thoroughfare398.setter
    def xal_Thoroughfare398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare398", None)
        self.__xal_Thoroughfare398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine399"):
                    opp_val = getattr(item, "xal_AddressLine399", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine399"):
                    opp_val = getattr(item, "xal_AddressLine399", None)
                    
                    setattr(item, "xal_AddressLine399", self)
                    

    @property
    def xal_Thoroughfare71(self):
        return self.__xal_Thoroughfare71

    @xal_Thoroughfare71.setter
    def xal_Thoroughfare71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare71", None)
        self.__xal_Thoroughfare71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality70"):
                opp_val = getattr(old_value, "xal_DependentLocality70", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality70"):
                opp_val = getattr(value, "xal_DependentLocality70", None)
                setattr(value, "xal_DependentLocality70", self)

    @property
    def xal_Thoroughfare412(self):
        return self.__xal_Thoroughfare412

    @xal_Thoroughfare412.setter
    def xal_Thoroughfare412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare412", None)
        self.__xal_Thoroughfare412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfarePreDirection413"):
                opp_val = getattr(old_value, "xal_ThoroughfarePreDirection413", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfarePreDirection413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfarePreDirection413"):
                opp_val = getattr(value, "xal_ThoroughfarePreDirection413", None)
                setattr(value, "xal_ThoroughfarePreDirection413", self)

    @property
    def xal_Thoroughfare134(self):
        return self.__xal_Thoroughfare134

    @xal_Thoroughfare134.setter
    def xal_Thoroughfare134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare134", None)
        self.__xal_Thoroughfare134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot133"):
                opp_val = getattr(old_value, "xal_DocumentRoot133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot133"):
                opp_val = getattr(value, "xal_DocumentRoot133", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_Thoroughfare439(self):
        return self.__xal_Thoroughfare439

    @xal_Thoroughfare439.setter
    def xal_Thoroughfare439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare439", None)
        self.__xal_Thoroughfare439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode440"):
                opp_val = getattr(old_value, "xal_PostalCode440", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode440"):
                opp_val = getattr(value, "xal_PostalCode440", None)
                setattr(value, "xal_PostalCode440", self)

    @property
    def xal_Thoroughfare44(self):
        return self.__xal_Thoroughfare44

    @xal_Thoroughfare44.setter
    def xal_Thoroughfare44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare44", None)
        self.__xal_Thoroughfare44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country43"):
                opp_val = getattr(old_value, "xal_Country43", None)
                if opp_val == self:
                    setattr(old_value, "xal_Country43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country43"):
                opp_val = getattr(value, "xal_Country43", None)
                setattr(value, "xal_Country43", self)

    @property
    def xal_Thoroughfare404(self):
        return self.__xal_Thoroughfare404

    @xal_Thoroughfare404.setter
    def xal_Thoroughfare404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare404", None)
        self.__xal_Thoroughfare404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberRange"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberRange", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberRange"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberRange", None)
                    
                    setattr(item, "xal_ThoroughfareNumberRange", self)
                    

    @property
    def xal_Thoroughfare(self):
        return self.__xal_Thoroughfare

    @xal_Thoroughfare.setter
    def xal_Thoroughfare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare", None)
        self.__xal_Thoroughfare = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails12"):
                opp_val = getattr(old_value, "xal_AddressDetails12", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails12"):
                opp_val = getattr(value, "xal_AddressDetails12", None)
                setattr(value, "xal_AddressDetails12", self)

    @property
    def xal_Thoroughfare436(self):
        return self.__xal_Thoroughfare436

    @xal_Thoroughfare436.setter
    def xal_Thoroughfare436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare436", None)
        self.__xal_Thoroughfare436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Firm437"):
                opp_val = getattr(old_value, "xal_Firm437", None)
                if opp_val == self:
                    setattr(old_value, "xal_Firm437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Firm437"):
                opp_val = getattr(value, "xal_Firm437", None)
                setattr(value, "xal_Firm437", self)

    @property
    def xal_Thoroughfare430(self):
        return self.__xal_Thoroughfare430

    @xal_Thoroughfare430.setter
    def xal_Thoroughfare430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare430", None)
        self.__xal_Thoroughfare430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality431"):
                opp_val = getattr(old_value, "xal_DependentLocality431", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality431"):
                opp_val = getattr(value, "xal_DependentLocality431", None)
                setattr(value, "xal_DependentLocality431", self)

    @property
    def xal_Thoroughfare421(self):
        return self.__xal_Thoroughfare421

    @xal_Thoroughfare421.setter
    def xal_Thoroughfare421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare421", None)
        self.__xal_Thoroughfare421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareTrailingType422"):
                opp_val = getattr(old_value, "xal_ThoroughfareTrailingType422", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareTrailingType422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareTrailingType422"):
                opp_val = getattr(value, "xal_ThoroughfareTrailingType422", None)
                setattr(value, "xal_ThoroughfareTrailingType422", self)

    @property
    def xal_Thoroughfare401(self):
        return self.__xal_Thoroughfare401

    @xal_Thoroughfare401.setter
    def xal_Thoroughfare401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare401", None)
        self.__xal_Thoroughfare401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumber402"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber402", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumber402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumber402"):
                    opp_val = getattr(item, "xal_ThoroughfareNumber402", None)
                    
                    setattr(item, "xal_ThoroughfareNumber402", self)
                    

    @property
    def xal_Thoroughfare433(self):
        return self.__xal_Thoroughfare433

    @xal_Thoroughfare433.setter
    def xal_Thoroughfare433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare433", None)
        self.__xal_Thoroughfare433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise434"):
                opp_val = getattr(old_value, "xal_Premise434", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise434", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise434"):
                opp_val = getattr(value, "xal_Premise434", None)
                setattr(value, "xal_Premise434", self)

    @property
    def xal_Thoroughfare173(self):
        return self.__xal_Thoroughfare173

    @xal_Thoroughfare173.setter
    def xal_Thoroughfare173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare173", None)
        self.__xal_Thoroughfare173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser172"):
                opp_val = getattr(old_value, "xal_LargeMailUser172", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser172"):
                opp_val = getattr(value, "xal_LargeMailUser172", None)
                setattr(value, "xal_LargeMailUser172", self)

    @property
    def xal_Thoroughfare406(self):
        return self.__xal_Thoroughfare406

    @xal_Thoroughfare406.setter
    def xal_Thoroughfare406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare406", None)
        self.__xal_Thoroughfare406 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix407"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix407", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberPrefix407", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberPrefix407"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberPrefix407", None)
                    
                    setattr(item, "xal_ThoroughfareNumberPrefix407", self)
                    

    @property
    def xal_Thoroughfare418(self):
        return self.__xal_Thoroughfare418

    @xal_Thoroughfare418.setter
    def xal_Thoroughfare418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare418", None)
        self.__xal_Thoroughfare418 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareName419"):
                    opp_val = getattr(item, "xal_ThoroughfareName419", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareName419", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareName419"):
                    opp_val = getattr(item, "xal_ThoroughfareName419", None)
                    
                    setattr(item, "xal_ThoroughfareName419", self)
                    

    @property
    def xal_Thoroughfare409(self):
        return self.__xal_Thoroughfare409

    @xal_Thoroughfare409.setter
    def xal_Thoroughfare409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare409", None)
        self.__xal_Thoroughfare409 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix410"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix410", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_ThoroughfareNumberSuffix410", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_ThoroughfareNumberSuffix410"):
                    opp_val = getattr(item, "xal_ThoroughfareNumberSuffix410", None)
                    
                    setattr(item, "xal_ThoroughfareNumberSuffix410", self)
                    

    @property
    def xal_Thoroughfare427(self):
        return self.__xal_Thoroughfare427

    @xal_Thoroughfare427.setter
    def xal_Thoroughfare427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare427", None)
        self.__xal_Thoroughfare427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentThoroughfare428"):
                opp_val = getattr(old_value, "xal_DependentThoroughfare428", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentThoroughfare428", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentThoroughfare428"):
                opp_val = getattr(value, "xal_DependentThoroughfare428", None)
                setattr(value, "xal_DependentThoroughfare428", self)

    @property
    def xal_Thoroughfare415(self):
        return self.__xal_Thoroughfare415

    @xal_Thoroughfare415.setter
    def xal_Thoroughfare415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Thoroughfare__xal_Thoroughfare415", None)
        self.__xal_Thoroughfare415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_ThoroughfareLeadingType416"):
                opp_val = getattr(old_value, "xal_ThoroughfareLeadingType416", None)
                if opp_val == self:
                    setattr(old_value, "xal_ThoroughfareLeadingType416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_ThoroughfareLeadingType416"):
                opp_val = getattr(value, "xal_ThoroughfareLeadingType416", None)
                setattr(value, "xal_ThoroughfareLeadingType416", self)

class xal_Locality:

    def __init__(self, indicator: str, type: str, usageType: str, anyAttribute: str, any: str, xal_Locality: "xal_AddressDetails" = None, xal_Locality24: "xal_AdministrativeArea" = None, xal_Locality41: "xal_Country" = None, xal_Locality113: "xal_DocumentRoot" = None, xal_Locality178: set["xal_AddressLine"] = None, xal_Locality181: set["xal_LocalityName"] = None, xal_Locality186: "xal_LargeMailUser" = None, xal_Locality189: "xal_PostOffice" = None, xal_Locality192: "xal_PostalRoute" = None, xal_Locality195: "xal_Thoroughfare" = None, xal_Locality198: "xal_Premise" = None, xal_Locality201: "xal_DependentLocality" = None, xal_Locality204: "xal_PostalCode" = None, xal_Locality183: "xal_PostBox" = None, xal_Locality362: "xal_SubAdministrativeArea" = None):
        self.indicator = indicator
        self.type = type
        self.usageType = usageType
        self.anyAttribute = anyAttribute
        self.any = any
        self.xal_Locality = xal_Locality
        self.xal_Locality24 = xal_Locality24
        self.xal_Locality41 = xal_Locality41
        self.xal_Locality113 = xal_Locality113
        self.xal_Locality178 = xal_Locality178 if xal_Locality178 is not None else set()
        self.xal_Locality181 = xal_Locality181 if xal_Locality181 is not None else set()
        self.xal_Locality186 = xal_Locality186
        self.xal_Locality189 = xal_Locality189
        self.xal_Locality192 = xal_Locality192
        self.xal_Locality195 = xal_Locality195
        self.xal_Locality198 = xal_Locality198
        self.xal_Locality201 = xal_Locality201
        self.xal_Locality204 = xal_Locality204
        self.xal_Locality183 = xal_Locality183
        self.xal_Locality362 = xal_Locality362
        
    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def usageType(self) -> str:
        return self.__usageType

    @usageType.setter
    def usageType(self, usageType: str):
        self.__usageType = usageType

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xal_Locality192(self):
        return self.__xal_Locality192

    @xal_Locality192.setter
    def xal_Locality192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality192", None)
        self.__xal_Locality192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalRoute193"):
                opp_val = getattr(old_value, "xal_PostalRoute193", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalRoute193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalRoute193"):
                opp_val = getattr(value, "xal_PostalRoute193", None)
                setattr(value, "xal_PostalRoute193", self)

    @property
    def xal_Locality201(self):
        return self.__xal_Locality201

    @xal_Locality201.setter
    def xal_Locality201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality201", None)
        self.__xal_Locality201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DependentLocality202"):
                opp_val = getattr(old_value, "xal_DependentLocality202", None)
                if opp_val == self:
                    setattr(old_value, "xal_DependentLocality202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DependentLocality202"):
                opp_val = getattr(value, "xal_DependentLocality202", None)
                setattr(value, "xal_DependentLocality202", self)

    @property
    def xal_Locality183(self):
        return self.__xal_Locality183

    @xal_Locality183.setter
    def xal_Locality183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality183", None)
        self.__xal_Locality183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostBox184"):
                opp_val = getattr(old_value, "xal_PostBox184", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostBox184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostBox184"):
                opp_val = getattr(value, "xal_PostBox184", None)
                setattr(value, "xal_PostBox184", self)

    @property
    def xal_Locality198(self):
        return self.__xal_Locality198

    @xal_Locality198.setter
    def xal_Locality198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality198", None)
        self.__xal_Locality198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Premise199"):
                opp_val = getattr(old_value, "xal_Premise199", None)
                if opp_val == self:
                    setattr(old_value, "xal_Premise199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Premise199"):
                opp_val = getattr(value, "xal_Premise199", None)
                setattr(value, "xal_Premise199", self)

    @property
    def xal_Locality189(self):
        return self.__xal_Locality189

    @xal_Locality189.setter
    def xal_Locality189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality189", None)
        self.__xal_Locality189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice190"):
                opp_val = getattr(old_value, "xal_PostOffice190", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice190"):
                opp_val = getattr(value, "xal_PostOffice190", None)
                setattr(value, "xal_PostOffice190", self)

    @property
    def xal_Locality113(self):
        return self.__xal_Locality113

    @xal_Locality113.setter
    def xal_Locality113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality113", None)
        self.__xal_Locality113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot112"):
                opp_val = getattr(old_value, "xal_DocumentRoot112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot112"):
                opp_val = getattr(value, "xal_DocumentRoot112", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_Locality181(self):
        return self.__xal_Locality181

    @xal_Locality181.setter
    def xal_Locality181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality181", None)
        self.__xal_Locality181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_LocalityName"):
                    opp_val = getattr(item, "xal_LocalityName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_LocalityName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_LocalityName"):
                    opp_val = getattr(item, "xal_LocalityName", None)
                    
                    setattr(item, "xal_LocalityName", self)
                    

    @property
    def xal_Locality204(self):
        return self.__xal_Locality204

    @xal_Locality204.setter
    def xal_Locality204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality204", None)
        self.__xal_Locality204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode205"):
                opp_val = getattr(old_value, "xal_PostalCode205", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode205"):
                opp_val = getattr(value, "xal_PostalCode205", None)
                setattr(value, "xal_PostalCode205", self)

    @property
    def xal_Locality24(self):
        return self.__xal_Locality24

    @xal_Locality24.setter
    def xal_Locality24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality24", None)
        self.__xal_Locality24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea23"):
                opp_val = getattr(old_value, "xal_AdministrativeArea23", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea23"):
                opp_val = getattr(value, "xal_AdministrativeArea23", None)
                setattr(value, "xal_AdministrativeArea23", self)

    @property
    def xal_Locality41(self):
        return self.__xal_Locality41

    @xal_Locality41.setter
    def xal_Locality41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality41", None)
        self.__xal_Locality41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country40"):
                opp_val = getattr(old_value, "xal_Country40", None)
                if opp_val == self:
                    setattr(old_value, "xal_Country40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country40"):
                opp_val = getattr(value, "xal_Country40", None)
                setattr(value, "xal_Country40", self)

    @property
    def xal_Locality186(self):
        return self.__xal_Locality186

    @xal_Locality186.setter
    def xal_Locality186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality186", None)
        self.__xal_Locality186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_LargeMailUser187"):
                opp_val = getattr(old_value, "xal_LargeMailUser187", None)
                if opp_val == self:
                    setattr(old_value, "xal_LargeMailUser187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_LargeMailUser187"):
                opp_val = getattr(value, "xal_LargeMailUser187", None)
                setattr(value, "xal_LargeMailUser187", self)

    @property
    def xal_Locality178(self):
        return self.__xal_Locality178

    @xal_Locality178.setter
    def xal_Locality178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality178", None)
        self.__xal_Locality178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine179"):
                    opp_val = getattr(item, "xal_AddressLine179", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine179"):
                    opp_val = getattr(item, "xal_AddressLine179", None)
                    
                    setattr(item, "xal_AddressLine179", self)
                    

    @property
    def xal_Locality195(self):
        return self.__xal_Locality195

    @xal_Locality195.setter
    def xal_Locality195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality195", None)
        self.__xal_Locality195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare196"):
                opp_val = getattr(old_value, "xal_Thoroughfare196", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare196"):
                opp_val = getattr(value, "xal_Thoroughfare196", None)
                setattr(value, "xal_Thoroughfare196", self)

    @property
    def xal_Locality362(self):
        return self.__xal_Locality362

    @xal_Locality362.setter
    def xal_Locality362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality362", None)
        self.__xal_Locality362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea361"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea361", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubAdministrativeArea361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea361"):
                opp_val = getattr(value, "xal_SubAdministrativeArea361", None)
                setattr(value, "xal_SubAdministrativeArea361", self)

    @property
    def xal_Locality(self):
        return self.__xal_Locality

    @xal_Locality.setter
    def xal_Locality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Locality__xal_Locality", None)
        self.__xal_Locality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails10"):
                opp_val = getattr(old_value, "xal_AddressDetails10", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails10"):
                opp_val = getattr(value, "xal_AddressDetails10", None)
                setattr(value, "xal_AddressDetails10", self)

class xal_AdministrativeArea:

    def __init__(self, type: str, usageType: str, anyAttribute: str, any: str, indicator: str, xal_AdministrativeArea: "xal_AddressDetails" = None, xal_AdministrativeArea21: "xal_SubAdministrativeArea" = None, xal_AdministrativeArea23: "xal_Locality" = None, xal_AdministrativeArea26: "xal_PostOffice" = None, xal_AdministrativeArea16: set["xal_AddressLine"] = None, xal_AdministrativeArea19: set["xal_AdministrativeAreaName"] = None, xal_AdministrativeArea28: "xal_PostalCode" = None, xal_AdministrativeArea38: "xal_Country" = None, xal_AdministrativeArea104: "xal_DocumentRoot" = None):
        self.type = type
        self.usageType = usageType
        self.anyAttribute = anyAttribute
        self.any = any
        self.indicator = indicator
        self.xal_AdministrativeArea = xal_AdministrativeArea
        self.xal_AdministrativeArea21 = xal_AdministrativeArea21
        self.xal_AdministrativeArea23 = xal_AdministrativeArea23
        self.xal_AdministrativeArea26 = xal_AdministrativeArea26
        self.xal_AdministrativeArea16 = xal_AdministrativeArea16 if xal_AdministrativeArea16 is not None else set()
        self.xal_AdministrativeArea19 = xal_AdministrativeArea19 if xal_AdministrativeArea19 is not None else set()
        self.xal_AdministrativeArea28 = xal_AdministrativeArea28
        self.xal_AdministrativeArea38 = xal_AdministrativeArea38
        self.xal_AdministrativeArea104 = xal_AdministrativeArea104
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def indicator(self) -> str:
        return self.__indicator

    @indicator.setter
    def indicator(self, indicator: str):
        self.__indicator = indicator

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def usageType(self) -> str:
        return self.__usageType

    @usageType.setter
    def usageType(self, usageType: str):
        self.__usageType = usageType

    @property
    def xal_AdministrativeArea38(self):
        return self.__xal_AdministrativeArea38

    @xal_AdministrativeArea38.setter
    def xal_AdministrativeArea38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea38", None)
        self.__xal_AdministrativeArea38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country37"):
                opp_val = getattr(old_value, "xal_Country37", None)
                if opp_val == self:
                    setattr(old_value, "xal_Country37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country37"):
                opp_val = getattr(value, "xal_Country37", None)
                setattr(value, "xal_Country37", self)

    @property
    def xal_AdministrativeArea21(self):
        return self.__xal_AdministrativeArea21

    @xal_AdministrativeArea21.setter
    def xal_AdministrativeArea21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea21", None)
        self.__xal_AdministrativeArea21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SubAdministrativeArea"):
                opp_val = getattr(old_value, "xal_SubAdministrativeArea", None)
                if opp_val == self:
                    setattr(old_value, "xal_SubAdministrativeArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SubAdministrativeArea"):
                opp_val = getattr(value, "xal_SubAdministrativeArea", None)
                setattr(value, "xal_SubAdministrativeArea", self)

    @property
    def xal_AdministrativeArea26(self):
        return self.__xal_AdministrativeArea26

    @xal_AdministrativeArea26.setter
    def xal_AdministrativeArea26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea26", None)
        self.__xal_AdministrativeArea26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostOffice"):
                opp_val = getattr(old_value, "xal_PostOffice", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostOffice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostOffice"):
                opp_val = getattr(value, "xal_PostOffice", None)
                setattr(value, "xal_PostOffice", self)

    @property
    def xal_AdministrativeArea19(self):
        return self.__xal_AdministrativeArea19

    @xal_AdministrativeArea19.setter
    def xal_AdministrativeArea19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea19", None)
        self.__xal_AdministrativeArea19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AdministrativeAreaName"):
                    opp_val = getattr(item, "xal_AdministrativeAreaName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AdministrativeAreaName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AdministrativeAreaName"):
                    opp_val = getattr(item, "xal_AdministrativeAreaName", None)
                    
                    setattr(item, "xal_AdministrativeAreaName", self)
                    

    @property
    def xal_AdministrativeArea23(self):
        return self.__xal_AdministrativeArea23

    @xal_AdministrativeArea23.setter
    def xal_AdministrativeArea23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea23", None)
        self.__xal_AdministrativeArea23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality24"):
                opp_val = getattr(old_value, "xal_Locality24", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality24"):
                opp_val = getattr(value, "xal_Locality24", None)
                setattr(value, "xal_Locality24", self)

    @property
    def xal_AdministrativeArea16(self):
        return self.__xal_AdministrativeArea16

    @xal_AdministrativeArea16.setter
    def xal_AdministrativeArea16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea16", None)
        self.__xal_AdministrativeArea16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine17"):
                    opp_val = getattr(item, "xal_AddressLine17", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine17"):
                    opp_val = getattr(item, "xal_AddressLine17", None)
                    
                    setattr(item, "xal_AddressLine17", self)
                    

    @property
    def xal_AdministrativeArea28(self):
        return self.__xal_AdministrativeArea28

    @xal_AdministrativeArea28.setter
    def xal_AdministrativeArea28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea28", None)
        self.__xal_AdministrativeArea28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalCode"):
                opp_val = getattr(old_value, "xal_PostalCode", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalCode"):
                opp_val = getattr(value, "xal_PostalCode", None)
                setattr(value, "xal_PostalCode", self)

    @property
    def xal_AdministrativeArea(self):
        return self.__xal_AdministrativeArea

    @xal_AdministrativeArea.setter
    def xal_AdministrativeArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea", None)
        self.__xal_AdministrativeArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails8"):
                opp_val = getattr(old_value, "xal_AddressDetails8", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails8"):
                opp_val = getattr(value, "xal_AddressDetails8", None)
                setattr(value, "xal_AddressDetails8", self)

    @property
    def xal_AdministrativeArea104(self):
        return self.__xal_AdministrativeArea104

    @xal_AdministrativeArea104.setter
    def xal_AdministrativeArea104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AdministrativeArea__xal_AdministrativeArea104", None)
        self.__xal_AdministrativeArea104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot103"):
                opp_val = getattr(old_value, "xal_DocumentRoot103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot103"):
                opp_val = getattr(value, "xal_DocumentRoot103", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xal_Country:

    def __init__(self, any: str, anyAttribute: str, xal_Country: "xal_AddressDetails" = None, xal_Country30: set["xal_AddressLine"] = None, xal_Country33: set["xal_CountryNameCode"] = None, xal_Country35: set["xal_CountryName"] = None, xal_Country37: "xal_AdministrativeArea" = None, xal_Country40: "xal_Locality" = None, xal_Country43: "xal_Thoroughfare" = None):
        self.any = any
        self.anyAttribute = anyAttribute
        self.xal_Country = xal_Country
        self.xal_Country30 = xal_Country30 if xal_Country30 is not None else set()
        self.xal_Country33 = xal_Country33 if xal_Country33 is not None else set()
        self.xal_Country35 = xal_Country35 if xal_Country35 is not None else set()
        self.xal_Country37 = xal_Country37
        self.xal_Country40 = xal_Country40
        self.xal_Country43 = xal_Country43
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xal_Country35(self):
        return self.__xal_Country35

    @xal_Country35.setter
    def xal_Country35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country35", None)
        self.__xal_Country35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_CountryName"):
                    opp_val = getattr(item, "xal_CountryName", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_CountryName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_CountryName"):
                    opp_val = getattr(item, "xal_CountryName", None)
                    
                    setattr(item, "xal_CountryName", self)
                    

    @property
    def xal_Country(self):
        return self.__xal_Country

    @xal_Country.setter
    def xal_Country(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country", None)
        self.__xal_Country = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails6"):
                opp_val = getattr(old_value, "xal_AddressDetails6", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails6"):
                opp_val = getattr(value, "xal_AddressDetails6", None)
                setattr(value, "xal_AddressDetails6", self)

    @property
    def xal_Country43(self):
        return self.__xal_Country43

    @xal_Country43.setter
    def xal_Country43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country43", None)
        self.__xal_Country43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare44"):
                opp_val = getattr(old_value, "xal_Thoroughfare44", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare44"):
                opp_val = getattr(value, "xal_Thoroughfare44", None)
                setattr(value, "xal_Thoroughfare44", self)

    @property
    def xal_Country40(self):
        return self.__xal_Country40

    @xal_Country40.setter
    def xal_Country40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country40", None)
        self.__xal_Country40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality41"):
                opp_val = getattr(old_value, "xal_Locality41", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality41"):
                opp_val = getattr(value, "xal_Locality41", None)
                setattr(value, "xal_Locality41", self)

    @property
    def xal_Country33(self):
        return self.__xal_Country33

    @xal_Country33.setter
    def xal_Country33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country33", None)
        self.__xal_Country33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_CountryNameCode"):
                    opp_val = getattr(item, "xal_CountryNameCode", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_CountryNameCode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_CountryNameCode"):
                    opp_val = getattr(item, "xal_CountryNameCode", None)
                    
                    setattr(item, "xal_CountryNameCode", self)
                    

    @property
    def xal_Country30(self):
        return self.__xal_Country30

    @xal_Country30.setter
    def xal_Country30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country30", None)
        self.__xal_Country30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine31"):
                    opp_val = getattr(item, "xal_AddressLine31", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine31"):
                    opp_val = getattr(item, "xal_AddressLine31", None)
                    
                    setattr(item, "xal_AddressLine31", self)
                    

    @property
    def xal_Country37(self):
        return self.__xal_Country37

    @xal_Country37.setter
    def xal_Country37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Country__xal_Country37", None)
        self.__xal_Country37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea38"):
                opp_val = getattr(old_value, "xal_AdministrativeArea38", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea38"):
                opp_val = getattr(value, "xal_AdministrativeArea38", None)
                setattr(value, "xal_AdministrativeArea38", self)

class xal_AddressLines:

    def __init__(self, anyAttribute: str, any: str, xal_AddressLines: "xal_AddressDetails" = None, xal_AddressLines14: set["xal_AddressLine"] = None):
        self.anyAttribute = anyAttribute
        self.any = any
        self.xal_AddressLines = xal_AddressLines
        self.xal_AddressLines14 = xal_AddressLines14 if xal_AddressLines14 is not None else set()
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_AddressLines(self):
        return self.__xal_AddressLines

    @xal_AddressLines.setter
    def xal_AddressLines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLines__xal_AddressLines", None)
        self.__xal_AddressLines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails4"):
                opp_val = getattr(old_value, "xal_AddressDetails4", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails4"):
                opp_val = getattr(value, "xal_AddressDetails4", None)
                setattr(value, "xal_AddressDetails4", self)

    @property
    def xal_AddressLines14(self):
        return self.__xal_AddressLines14

    @xal_AddressLines14.setter
    def xal_AddressLines14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressLines__xal_AddressLines14", None)
        self.__xal_AddressLines14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressLine"):
                    opp_val = getattr(item, "xal_AddressLine", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressLine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressLine"):
                    opp_val = getattr(item, "xal_AddressLine", None)
                    
                    setattr(item, "xal_AddressLine", self)
                    

class xal_PostalServiceElements:

    def __init__(self, any: str, type: str, anyAttribute: str, xal_PostalServiceElements: "xal_AddressDetails" = None, xal_PostalServiceElements247: "xal_AddressLongitude" = None, xal_PostalServiceElements233: set["xal_AddressIdentifier"] = None, xal_PostalServiceElements235: "xal_EndorsementLineCode" = None, xal_PostalServiceElements237: "xal_KeyLineCode" = None, xal_PostalServiceElements239: "xal_Barcode" = None, xal_PostalServiceElements241: "xal_SortingCode" = None, xal_PostalServiceElements243: "xal_AddressLatitude" = None, xal_PostalServiceElements245: "xal_AddressLatitudeDirection" = None, xal_PostalServiceElements249: "xal_AddressLongitudeDirection" = None, xal_PostalServiceElements251: set["xal_SupplementaryPostalServiceData"] = None):
        self.any = any
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_PostalServiceElements = xal_PostalServiceElements
        self.xal_PostalServiceElements247 = xal_PostalServiceElements247
        self.xal_PostalServiceElements233 = xal_PostalServiceElements233 if xal_PostalServiceElements233 is not None else set()
        self.xal_PostalServiceElements235 = xal_PostalServiceElements235
        self.xal_PostalServiceElements237 = xal_PostalServiceElements237
        self.xal_PostalServiceElements239 = xal_PostalServiceElements239
        self.xal_PostalServiceElements241 = xal_PostalServiceElements241
        self.xal_PostalServiceElements243 = xal_PostalServiceElements243
        self.xal_PostalServiceElements245 = xal_PostalServiceElements245
        self.xal_PostalServiceElements249 = xal_PostalServiceElements249
        self.xal_PostalServiceElements251 = xal_PostalServiceElements251 if xal_PostalServiceElements251 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def xal_PostalServiceElements243(self):
        return self.__xal_PostalServiceElements243

    @xal_PostalServiceElements243.setter
    def xal_PostalServiceElements243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements243", None)
        self.__xal_PostalServiceElements243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLatitude"):
                opp_val = getattr(old_value, "xal_AddressLatitude", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressLatitude", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLatitude"):
                opp_val = getattr(value, "xal_AddressLatitude", None)
                setattr(value, "xal_AddressLatitude", self)

    @property
    def xal_PostalServiceElements245(self):
        return self.__xal_PostalServiceElements245

    @xal_PostalServiceElements245.setter
    def xal_PostalServiceElements245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements245", None)
        self.__xal_PostalServiceElements245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLatitudeDirection"):
                opp_val = getattr(old_value, "xal_AddressLatitudeDirection", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressLatitudeDirection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLatitudeDirection"):
                opp_val = getattr(value, "xal_AddressLatitudeDirection", None)
                setattr(value, "xal_AddressLatitudeDirection", self)

    @property
    def xal_PostalServiceElements235(self):
        return self.__xal_PostalServiceElements235

    @xal_PostalServiceElements235.setter
    def xal_PostalServiceElements235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements235", None)
        self.__xal_PostalServiceElements235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_EndorsementLineCode"):
                opp_val = getattr(old_value, "xal_EndorsementLineCode", None)
                if opp_val == self:
                    setattr(old_value, "xal_EndorsementLineCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_EndorsementLineCode"):
                opp_val = getattr(value, "xal_EndorsementLineCode", None)
                setattr(value, "xal_EndorsementLineCode", self)

    @property
    def xal_PostalServiceElements247(self):
        return self.__xal_PostalServiceElements247

    @xal_PostalServiceElements247.setter
    def xal_PostalServiceElements247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements247", None)
        self.__xal_PostalServiceElements247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLongitude"):
                opp_val = getattr(old_value, "xal_AddressLongitude", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressLongitude", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLongitude"):
                opp_val = getattr(value, "xal_AddressLongitude", None)
                setattr(value, "xal_AddressLongitude", self)

    @property
    def xal_PostalServiceElements(self):
        return self.__xal_PostalServiceElements

    @xal_PostalServiceElements.setter
    def xal_PostalServiceElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements", None)
        self.__xal_PostalServiceElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails"):
                opp_val = getattr(old_value, "xal_AddressDetails", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails"):
                opp_val = getattr(value, "xal_AddressDetails", None)
                setattr(value, "xal_AddressDetails", self)

    @property
    def xal_PostalServiceElements237(self):
        return self.__xal_PostalServiceElements237

    @xal_PostalServiceElements237.setter
    def xal_PostalServiceElements237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements237", None)
        self.__xal_PostalServiceElements237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_KeyLineCode"):
                opp_val = getattr(old_value, "xal_KeyLineCode", None)
                if opp_val == self:
                    setattr(old_value, "xal_KeyLineCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_KeyLineCode"):
                opp_val = getattr(value, "xal_KeyLineCode", None)
                setattr(value, "xal_KeyLineCode", self)

    @property
    def xal_PostalServiceElements249(self):
        return self.__xal_PostalServiceElements249

    @xal_PostalServiceElements249.setter
    def xal_PostalServiceElements249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements249", None)
        self.__xal_PostalServiceElements249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLongitudeDirection"):
                opp_val = getattr(old_value, "xal_AddressLongitudeDirection", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressLongitudeDirection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLongitudeDirection"):
                opp_val = getattr(value, "xal_AddressLongitudeDirection", None)
                setattr(value, "xal_AddressLongitudeDirection", self)

    @property
    def xal_PostalServiceElements239(self):
        return self.__xal_PostalServiceElements239

    @xal_PostalServiceElements239.setter
    def xal_PostalServiceElements239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements239", None)
        self.__xal_PostalServiceElements239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Barcode"):
                opp_val = getattr(old_value, "xal_Barcode", None)
                if opp_val == self:
                    setattr(old_value, "xal_Barcode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Barcode"):
                opp_val = getattr(value, "xal_Barcode", None)
                setattr(value, "xal_Barcode", self)

    @property
    def xal_PostalServiceElements233(self):
        return self.__xal_PostalServiceElements233

    @xal_PostalServiceElements233.setter
    def xal_PostalServiceElements233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements233", None)
        self.__xal_PostalServiceElements233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_AddressIdentifier"):
                    opp_val = getattr(item, "xal_AddressIdentifier", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_AddressIdentifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_AddressIdentifier"):
                    opp_val = getattr(item, "xal_AddressIdentifier", None)
                    
                    setattr(item, "xal_AddressIdentifier", self)
                    

    @property
    def xal_PostalServiceElements251(self):
        return self.__xal_PostalServiceElements251

    @xal_PostalServiceElements251.setter
    def xal_PostalServiceElements251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements251", None)
        self.__xal_PostalServiceElements251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xal_SupplementaryPostalServiceData"):
                    opp_val = getattr(item, "xal_SupplementaryPostalServiceData", None)
                    
                    if opp_val == self:
                        setattr(item, "xal_SupplementaryPostalServiceData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xal_SupplementaryPostalServiceData"):
                    opp_val = getattr(item, "xal_SupplementaryPostalServiceData", None)
                    
                    setattr(item, "xal_SupplementaryPostalServiceData", self)
                    

    @property
    def xal_PostalServiceElements241(self):
        return self.__xal_PostalServiceElements241

    @xal_PostalServiceElements241.setter
    def xal_PostalServiceElements241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_PostalServiceElements__xal_PostalServiceElements241", None)
        self.__xal_PostalServiceElements241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_SortingCode"):
                opp_val = getattr(old_value, "xal_SortingCode", None)
                if opp_val == self:
                    setattr(old_value, "xal_SortingCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_SortingCode"):
                opp_val = getattr(value, "xal_SortingCode", None)
                setattr(value, "xal_SortingCode", self)

class xal_AddressDetails:

    def __init__(self, code: str, any: str, addressDetailsKey: str, addressType: str, currentStatus: str, usage: str, validFromDate: str, validToDate: str, anyAttribute: str, xal_AddressDetails: "xal_PostalServiceElements" = None, xal_AddressDetails2: "xal_Address" = None, xal_AddressDetails4: "xal_AddressLines" = None, xal_AddressDetails6: "xal_Country" = None, xal_AddressDetails8: "xal_AdministrativeArea" = None, xal_AddressDetails10: "xal_Locality" = None, xal_AddressDetails12: "xal_Thoroughfare" = None, xal_AddressDetails98: "xal_DocumentRoot" = None, xal_AddressDetails474: "xal_Xal" = None):
        self.code = code
        self.any = any
        self.addressDetailsKey = addressDetailsKey
        self.addressType = addressType
        self.currentStatus = currentStatus
        self.usage = usage
        self.validFromDate = validFromDate
        self.validToDate = validToDate
        self.anyAttribute = anyAttribute
        self.xal_AddressDetails = xal_AddressDetails
        self.xal_AddressDetails2 = xal_AddressDetails2
        self.xal_AddressDetails4 = xal_AddressDetails4
        self.xal_AddressDetails6 = xal_AddressDetails6
        self.xal_AddressDetails8 = xal_AddressDetails8
        self.xal_AddressDetails10 = xal_AddressDetails10
        self.xal_AddressDetails12 = xal_AddressDetails12
        self.xal_AddressDetails98 = xal_AddressDetails98
        self.xal_AddressDetails474 = xal_AddressDetails474
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def currentStatus(self) -> str:
        return self.__currentStatus

    @currentStatus.setter
    def currentStatus(self, currentStatus: str):
        self.__currentStatus = currentStatus

    @property
    def addressType(self) -> str:
        return self.__addressType

    @addressType.setter
    def addressType(self, addressType: str):
        self.__addressType = addressType

    @property
    def validToDate(self) -> str:
        return self.__validToDate

    @validToDate.setter
    def validToDate(self, validToDate: str):
        self.__validToDate = validToDate

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def addressDetailsKey(self) -> str:
        return self.__addressDetailsKey

    @addressDetailsKey.setter
    def addressDetailsKey(self, addressDetailsKey: str):
        self.__addressDetailsKey = addressDetailsKey

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def usage(self) -> str:
        return self.__usage

    @usage.setter
    def usage(self, usage: str):
        self.__usage = usage

    @property
    def validFromDate(self) -> str:
        return self.__validFromDate

    @validFromDate.setter
    def validFromDate(self, validFromDate: str):
        self.__validFromDate = validFromDate

    @property
    def xal_AddressDetails2(self):
        return self.__xal_AddressDetails2

    @xal_AddressDetails2.setter
    def xal_AddressDetails2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails2", None)
        self.__xal_AddressDetails2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Address"):
                opp_val = getattr(old_value, "xal_Address", None)
                if opp_val == self:
                    setattr(old_value, "xal_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Address"):
                opp_val = getattr(value, "xal_Address", None)
                setattr(value, "xal_Address", self)

    @property
    def xal_AddressDetails(self):
        return self.__xal_AddressDetails

    @xal_AddressDetails.setter
    def xal_AddressDetails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails", None)
        self.__xal_AddressDetails = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_PostalServiceElements"):
                opp_val = getattr(old_value, "xal_PostalServiceElements", None)
                if opp_val == self:
                    setattr(old_value, "xal_PostalServiceElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_PostalServiceElements"):
                opp_val = getattr(value, "xal_PostalServiceElements", None)
                setattr(value, "xal_PostalServiceElements", self)

    @property
    def xal_AddressDetails6(self):
        return self.__xal_AddressDetails6

    @xal_AddressDetails6.setter
    def xal_AddressDetails6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails6", None)
        self.__xal_AddressDetails6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Country"):
                opp_val = getattr(old_value, "xal_Country", None)
                if opp_val == self:
                    setattr(old_value, "xal_Country", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Country"):
                opp_val = getattr(value, "xal_Country", None)
                setattr(value, "xal_Country", self)

    @property
    def xal_AddressDetails12(self):
        return self.__xal_AddressDetails12

    @xal_AddressDetails12.setter
    def xal_AddressDetails12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails12", None)
        self.__xal_AddressDetails12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Thoroughfare"):
                opp_val = getattr(old_value, "xal_Thoroughfare", None)
                if opp_val == self:
                    setattr(old_value, "xal_Thoroughfare", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Thoroughfare"):
                opp_val = getattr(value, "xal_Thoroughfare", None)
                setattr(value, "xal_Thoroughfare", self)

    @property
    def xal_AddressDetails98(self):
        return self.__xal_AddressDetails98

    @xal_AddressDetails98.setter
    def xal_AddressDetails98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails98", None)
        self.__xal_AddressDetails98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_DocumentRoot97"):
                opp_val = getattr(old_value, "xal_DocumentRoot97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_DocumentRoot97"):
                opp_val = getattr(value, "xal_DocumentRoot97", None)
                if opp_val is None:
                    setattr(value, "xal_DocumentRoot97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressDetails474(self):
        return self.__xal_AddressDetails474

    @xal_AddressDetails474.setter
    def xal_AddressDetails474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails474", None)
        self.__xal_AddressDetails474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Xal473"):
                opp_val = getattr(old_value, "xal_Xal473", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Xal473"):
                opp_val = getattr(value, "xal_Xal473", None)
                if opp_val is None:
                    setattr(value, "xal_Xal473", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xal_AddressDetails10(self):
        return self.__xal_AddressDetails10

    @xal_AddressDetails10.setter
    def xal_AddressDetails10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails10", None)
        self.__xal_AddressDetails10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_Locality"):
                opp_val = getattr(old_value, "xal_Locality", None)
                if opp_val == self:
                    setattr(old_value, "xal_Locality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_Locality"):
                opp_val = getattr(value, "xal_Locality", None)
                setattr(value, "xal_Locality", self)

    @property
    def xal_AddressDetails8(self):
        return self.__xal_AddressDetails8

    @xal_AddressDetails8.setter
    def xal_AddressDetails8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails8", None)
        self.__xal_AddressDetails8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AdministrativeArea"):
                opp_val = getattr(old_value, "xal_AdministrativeArea", None)
                if opp_val == self:
                    setattr(old_value, "xal_AdministrativeArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AdministrativeArea"):
                opp_val = getattr(value, "xal_AdministrativeArea", None)
                setattr(value, "xal_AdministrativeArea", self)

    @property
    def xal_AddressDetails4(self):
        return self.__xal_AddressDetails4

    @xal_AddressDetails4.setter
    def xal_AddressDetails4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_AddressDetails__xal_AddressDetails4", None)
        self.__xal_AddressDetails4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressLines"):
                opp_val = getattr(old_value, "xal_AddressLines", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressLines"):
                opp_val = getattr(value, "xal_AddressLines", None)
                setattr(value, "xal_AddressLines", self)

class xal_Address:

    def __init__(self, mixed: str, code: str, type: str, anyAttribute: str, xal_Address: "xal_AddressDetails" = None):
        self.mixed = mixed
        self.code = code
        self.type = type
        self.anyAttribute = anyAttribute
        self.xal_Address = xal_Address
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xal_Address(self):
        return self.__xal_Address

    @xal_Address.setter
    def xal_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xal_Address__xal_Address", None)
        self.__xal_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xal_AddressDetails2"):
                opp_val = getattr(old_value, "xal_AddressDetails2", None)
                if opp_val == self:
                    setattr(old_value, "xal_AddressDetails2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xal_AddressDetails2"):
                opp_val = getattr(value, "xal_AddressDetails2", None)
                setattr(value, "xal_AddressDetails2", self)
