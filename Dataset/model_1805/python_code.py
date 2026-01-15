from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RangeKind(Enum):
    METRIC = "METRIC"
    METRICREMOVE = "METRICREMOVE"
    CAP = "CAP"
    DERIVED = "DERIVED"
    FORECAST = "FORECAST"
    FORECASTCAP = "FORECASTCAP"
    TRENDED = "TRENDED"
    UTILIZATION = "UTILIZATION"
    TOLERANCE = "TOLERANCE"
class StateType(Enum):
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    IDLE = "IDLE"
    DEFECT = "DEFECT"
    RESERVED = "RESERVED"
class RedundancyType(Enum):
    n = "n"
    n1 = "n1"
    _11 = "_11"
class LevelKind(Enum):
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    YELLOW = "YELLOW"


############################################
# Definition of Classes
############################################

class Company:

    pass
class library_Vendor(Company):

    pass
class library_MetricValueRange:

    pass
class BaseResource:

    pass
class library_Meta:

    pass
class library_Library:

    def __init__(self, name: str, protocols: str, library_Library75: set["library_Metric"] = None, library_Library78: set["library_MetricSource"] = None, library_Library80: set["library_Parameter"] = None, library_Library: set["library_Function"] = None, library_Library70: set["library_NodeType"] = None, library_Library72: set["library_Equipment"] = None, library_Library92: "library_Meta" = None, library_Library83: set["library_Tolerance"] = None, library_Library86: set["library_Expression"] = None, library_Library89: set["library_Unit"] = None):
        self.name = name
        self.protocols = protocols
        self.library_Library75 = library_Library75 if library_Library75 is not None else set()
        self.library_Library78 = library_Library78 if library_Library78 is not None else set()
        self.library_Library80 = library_Library80 if library_Library80 is not None else set()
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library70 = library_Library70 if library_Library70 is not None else set()
        self.library_Library72 = library_Library72 if library_Library72 is not None else set()
        self.library_Library92 = library_Library92
        self.library_Library83 = library_Library83 if library_Library83 is not None else set()
        self.library_Library86 = library_Library86 if library_Library86 is not None else set()
        self.library_Library89 = library_Library89 if library_Library89 is not None else set()
        
    @property
    def protocols(self) -> str:
        return self.__protocols

    @protocols.setter
    def protocols(self, protocols: str):
        self.__protocols = protocols

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library89(self):
        return self.__library_Library89

    @library_Library89.setter
    def library_Library89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library89", None)
        self.__library_Library89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Unit90"):
                    opp_val = getattr(item, "library_Unit90", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Unit90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Unit90"):
                    opp_val = getattr(item, "library_Unit90", None)
                    
                    setattr(item, "library_Unit90", self)
                    

    @property
    def library_Library83(self):
        return self.__library_Library83

    @library_Library83.setter
    def library_Library83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library83", None)
        self.__library_Library83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance84"):
                    opp_val = getattr(item, "library_Tolerance84", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance84"):
                    opp_val = getattr(item, "library_Tolerance84", None)
                    
                    setattr(item, "library_Tolerance84", self)
                    

    @property
    def library_Library72(self):
        return self.__library_Library72

    @library_Library72.setter
    def library_Library72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library72", None)
        self.__library_Library72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment73"):
                    opp_val = getattr(item, "library_Equipment73", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment73"):
                    opp_val = getattr(item, "library_Equipment73", None)
                    
                    setattr(item, "library_Equipment73", self)
                    

    @property
    def library_Library92(self):
        return self.__library_Library92

    @library_Library92.setter
    def library_Library92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library92", None)
        self.__library_Library92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Meta"):
                opp_val = getattr(old_value, "library_Meta", None)
                if opp_val == self:
                    setattr(old_value, "library_Meta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Meta"):
                opp_val = getattr(value, "library_Meta", None)
                setattr(value, "library_Meta", self)

    @property
    def library_Library78(self):
        return self.__library_Library78

    @library_Library78.setter
    def library_Library78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library78", None)
        self.__library_Library78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_MetricSource"):
                    opp_val = getattr(item, "library_MetricSource", None)
                    
                    if opp_val == self:
                        setattr(item, "library_MetricSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_MetricSource"):
                    opp_val = getattr(item, "library_MetricSource", None)
                    
                    setattr(item, "library_MetricSource", self)
                    

    @property
    def library_Library70(self):
        return self.__library_Library70

    @library_Library70.setter
    def library_Library70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library70", None)
        self.__library_Library70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType"):
                    opp_val = getattr(item, "library_NodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType"):
                    opp_val = getattr(item, "library_NodeType", None)
                    
                    setattr(item, "library_NodeType", self)
                    

    @property
    def library_Library86(self):
        return self.__library_Library86

    @library_Library86.setter
    def library_Library86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library86", None)
        self.__library_Library86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression87"):
                    opp_val = getattr(item, "library_Expression87", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression87"):
                    opp_val = getattr(item, "library_Expression87", None)
                    
                    setattr(item, "library_Expression87", self)
                    

    @property
    def library_Library80(self):
        return self.__library_Library80

    @library_Library80.setter
    def library_Library80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library80", None)
        self.__library_Library80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter81"):
                    opp_val = getattr(item, "library_Parameter81", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter81"):
                    opp_val = getattr(item, "library_Parameter81", None)
                    
                    setattr(item, "library_Parameter81", self)
                    

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function68"):
                    opp_val = getattr(item, "library_Function68", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function68"):
                    opp_val = getattr(item, "library_Function68", None)
                    
                    setattr(item, "library_Function68", self)
                    

    @property
    def library_Library75(self):
        return self.__library_Library75

    @library_Library75.setter
    def library_Library75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library75", None)
        self.__library_Library75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric76"):
                    opp_val = getattr(item, "library_Metric76", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric76"):
                    opp_val = getattr(item, "library_Metric76", None)
                    
                    setattr(item, "library_Metric76", self)
                    

class library_MetricSource:

    pass
class library_FunctionRelationship:

    pass
class library_Value:

    pass
class library_EObject:

    pass
class BaseExpressionResult:

    pass
class library_LastEvaluationExpressionResult(BaseExpressionResult):

    def __init__(self, lastEvalResult: str):
        self.lastEvalResult = lastEvalResult
        
    @property
    def lastEvalResult(self) -> str:
        return self.__lastEvalResult

    @lastEvalResult.setter
    def lastEvalResult(self, lastEvalResult: str):
        self.__lastEvalResult = lastEvalResult

class library_ExpressionResult(BaseExpressionResult):

    def __init__(self, targetRange: str, targetIntervalHint: str, targetKindHint: str, library_ExpressionResult: "library_BaseResource" = None, library_ExpressionResult59: set["library_Value"] = None):
        self.targetRange = targetRange
        self.targetIntervalHint = targetIntervalHint
        self.targetKindHint = targetKindHint
        self.library_ExpressionResult = library_ExpressionResult
        self.library_ExpressionResult59 = library_ExpressionResult59 if library_ExpressionResult59 is not None else set()
        
    @property
    def targetIntervalHint(self) -> str:
        return self.__targetIntervalHint

    @targetIntervalHint.setter
    def targetIntervalHint(self, targetIntervalHint: str):
        self.__targetIntervalHint = targetIntervalHint

    @property
    def targetRange(self) -> str:
        return self.__targetRange

    @targetRange.setter
    def targetRange(self, targetRange: str):
        self.__targetRange = targetRange

    @property
    def targetKindHint(self) -> str:
        return self.__targetKindHint

    @targetKindHint.setter
    def targetKindHint(self, targetKindHint: str):
        self.__targetKindHint = targetKindHint

    @property
    def library_ExpressionResult(self):
        return self.__library_ExpressionResult

    @library_ExpressionResult.setter
    def library_ExpressionResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ExpressionResult__library_ExpressionResult", None)
        self.__library_ExpressionResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_BaseResource57"):
                opp_val = getattr(old_value, "library_BaseResource57", None)
                if opp_val == self:
                    setattr(old_value, "library_BaseResource57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BaseResource57"):
                opp_val = getattr(value, "library_BaseResource57", None)
                setattr(value, "library_BaseResource57", self)

    @property
    def library_ExpressionResult59(self):
        return self.__library_ExpressionResult59

    @library_ExpressionResult59.setter
    def library_ExpressionResult59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ExpressionResult__library_ExpressionResult59", None)
        self.__library_ExpressionResult59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value"):
                    opp_val = getattr(item, "library_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value"):
                    opp_val = getattr(item, "library_Value", None)
                    
                    setattr(item, "library_Value", self)
                    

class library_EquipmentRelationship:

    pass
class library_MultiImage:

    pass
class library_DiagramInfo:

    pass
class Component:

    pass
class library_Function(Component):

    pass
class library_Equipment(Component):

    def __init__(self, equipmentCode: str, position: str, redundancy: str, state: str, count: str, library_Equipment: "library_Equipment" = None, library_Equipment24: set["library_Equipment"] = None, library_Equipment27: set["library_EquipmentGroup"] = None, library_Equipment29: set["library_EquipmentRelationship"] = None, library_Equipment32: "library_Equipment" = None, library_Equipment30: set["library_Equipment"] = None, library_Equipment53: "library_EquipmentGroup" = None, library_Equipment44: "library_EquipmentGroup" = None, library_Equipment73: "library_Library" = None, library_Equipment119: "library_NodeType" = None, library_Equipment121: "library_ProductInfo" = None):
        self.equipmentCode = equipmentCode
        self.position = position
        self.redundancy = redundancy
        self.state = state
        self.count = count
        self.library_Equipment = library_Equipment
        self.library_Equipment24 = library_Equipment24 if library_Equipment24 is not None else set()
        self.library_Equipment27 = library_Equipment27 if library_Equipment27 is not None else set()
        self.library_Equipment29 = library_Equipment29 if library_Equipment29 is not None else set()
        self.library_Equipment32 = library_Equipment32
        self.library_Equipment30 = library_Equipment30 if library_Equipment30 is not None else set()
        self.library_Equipment53 = library_Equipment53
        self.library_Equipment44 = library_Equipment44
        self.library_Equipment73 = library_Equipment73
        self.library_Equipment119 = library_Equipment119
        self.library_Equipment121 = library_Equipment121
        
    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def equipmentCode(self) -> str:
        return self.__equipmentCode

    @equipmentCode.setter
    def equipmentCode(self, equipmentCode: str):
        self.__equipmentCode = equipmentCode

    @property
    def redundancy(self) -> str:
        return self.__redundancy

    @redundancy.setter
    def redundancy(self, redundancy: str):
        self.__redundancy = redundancy

    @property
    def library_Equipment32(self):
        return self.__library_Equipment32

    @library_Equipment32.setter
    def library_Equipment32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment32", None)
        self.__library_Equipment32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment30"):
                opp_val = getattr(old_value, "library_Equipment30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment30"):
                opp_val = getattr(value, "library_Equipment30", None)
                if opp_val is None:
                    setattr(value, "library_Equipment30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment73(self):
        return self.__library_Equipment73

    @library_Equipment73.setter
    def library_Equipment73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment73", None)
        self.__library_Equipment73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library72"):
                opp_val = getattr(old_value, "library_Library72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library72"):
                opp_val = getattr(value, "library_Library72", None)
                if opp_val is None:
                    setattr(value, "library_Library72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment53(self):
        return self.__library_Equipment53

    @library_Equipment53.setter
    def library_Equipment53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment53", None)
        self.__library_Equipment53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup52"):
                opp_val = getattr(old_value, "library_EquipmentGroup52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup52"):
                opp_val = getattr(value, "library_EquipmentGroup52", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment29(self):
        return self.__library_Equipment29

    @library_Equipment29.setter
    def library_Equipment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment29", None)
        self.__library_Equipment29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_EquipmentRelationship"):
                    opp_val = getattr(item, "library_EquipmentRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "library_EquipmentRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_EquipmentRelationship"):
                    opp_val = getattr(item, "library_EquipmentRelationship", None)
                    
                    setattr(item, "library_EquipmentRelationship", self)
                    

    @property
    def library_Equipment(self):
        return self.__library_Equipment

    @library_Equipment.setter
    def library_Equipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment", None)
        self.__library_Equipment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment24"):
                opp_val = getattr(old_value, "library_Equipment24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment24"):
                opp_val = getattr(value, "library_Equipment24", None)
                if opp_val is None:
                    setattr(value, "library_Equipment24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment119(self):
        return self.__library_Equipment119

    @library_Equipment119.setter
    def library_Equipment119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment119", None)
        self.__library_Equipment119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType118"):
                opp_val = getattr(old_value, "library_NodeType118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType118"):
                opp_val = getattr(value, "library_NodeType118", None)
                if opp_val is None:
                    setattr(value, "library_NodeType118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment121(self):
        return self.__library_Equipment121

    @library_Equipment121.setter
    def library_Equipment121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment121", None)
        self.__library_Equipment121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo"):
                opp_val = getattr(old_value, "library_ProductInfo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo"):
                opp_val = getattr(value, "library_ProductInfo", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment30(self):
        return self.__library_Equipment30

    @library_Equipment30.setter
    def library_Equipment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment30", None)
        self.__library_Equipment30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment32"):
                    opp_val = getattr(item, "library_Equipment32", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment32"):
                    opp_val = getattr(item, "library_Equipment32", None)
                    
                    setattr(item, "library_Equipment32", self)
                    

    @property
    def library_Equipment27(self):
        return self.__library_Equipment27

    @library_Equipment27.setter
    def library_Equipment27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment27", None)
        self.__library_Equipment27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_EquipmentGroup"):
                    opp_val = getattr(item, "library_EquipmentGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "library_EquipmentGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_EquipmentGroup"):
                    opp_val = getattr(item, "library_EquipmentGroup", None)
                    
                    setattr(item, "library_EquipmentGroup", self)
                    

    @property
    def library_Equipment44(self):
        return self.__library_Equipment44

    @library_Equipment44.setter
    def library_Equipment44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment44", None)
        self.__library_Equipment44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup43"):
                opp_val = getattr(old_value, "library_EquipmentGroup43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup43"):
                opp_val = getattr(value, "library_EquipmentGroup43", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment24(self):
        return self.__library_Equipment24

    @library_Equipment24.setter
    def library_Equipment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment24", None)
        self.__library_Equipment24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment"):
                    opp_val = getattr(item, "library_Equipment", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment"):
                    opp_val = getattr(item, "library_Equipment", None)
                    
                    setattr(item, "library_Equipment", self)
                    

class library_Metric:

    pass
class library_ConfigAttribute:

    pass
class library_Protocol:

    pass
class library_NetXResource(BaseResource):

    pass
class library_Lifecycle:

    pass
class Base:

    pass
class library_Parameter(Base):

    def __init__(self, description: str, expressionName: str, modifiable: str, name: str, value: str, library_Parameter: "library_Component" = None, library_Parameter47: "library_EquipmentGroup" = None, library_Parameter81: "library_Library" = None):
        self.description = description
        self.expressionName = expressionName
        self.modifiable = modifiable
        self.name = name
        self.value = value
        self.library_Parameter = library_Parameter
        self.library_Parameter47 = library_Parameter47
        self.library_Parameter81 = library_Parameter81
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def modifiable(self) -> str:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: str):
        self.__modifiable = modifiable

    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def library_Parameter(self):
        return self.__library_Parameter

    @library_Parameter.setter
    def library_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter", None)
        self.__library_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Component17"):
                opp_val = getattr(old_value, "library_Component17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component17"):
                opp_val = getattr(value, "library_Component17", None)
                if opp_val is None:
                    setattr(value, "library_Component17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter81(self):
        return self.__library_Parameter81

    @library_Parameter81.setter
    def library_Parameter81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter81", None)
        self.__library_Parameter81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library80"):
                opp_val = getattr(old_value, "library_Library80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library80"):
                opp_val = getattr(value, "library_Library80", None)
                if opp_val is None:
                    setattr(value, "library_Library80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter47(self):
        return self.__library_Parameter47

    @library_Parameter47.setter
    def library_Parameter47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter47", None)
        self.__library_Parameter47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup46"):
                opp_val = getattr(old_value, "library_EquipmentGroup46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup46"):
                opp_val = getattr(value, "library_EquipmentGroup46", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_NodeType(Base):

    def __init__(self, leafNode: str, name: str, library_NodeType: "library_Library" = None, library_NodeType115: set["library_Function"] = None, library_NodeType118: set["library_Equipment"] = None, library_NodeType127: "library_ProductInfo" = None, library_NodeType143: "library_ReferenceRelationship" = None, library_NodeType132: "library_ReferenceNetwork" = None, library_NodeType146: "library_ReferenceRelationship" = None):
        self.leafNode = leafNode
        self.name = name
        self.library_NodeType = library_NodeType
        self.library_NodeType115 = library_NodeType115 if library_NodeType115 is not None else set()
        self.library_NodeType118 = library_NodeType118 if library_NodeType118 is not None else set()
        self.library_NodeType127 = library_NodeType127
        self.library_NodeType143 = library_NodeType143
        self.library_NodeType132 = library_NodeType132
        self.library_NodeType146 = library_NodeType146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def leafNode(self) -> str:
        return self.__leafNode

    @leafNode.setter
    def leafNode(self, leafNode: str):
        self.__leafNode = leafNode

    @property
    def library_NodeType118(self):
        return self.__library_NodeType118

    @library_NodeType118.setter
    def library_NodeType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType118", None)
        self.__library_NodeType118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment119"):
                    opp_val = getattr(item, "library_Equipment119", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment119"):
                    opp_val = getattr(item, "library_Equipment119", None)
                    
                    setattr(item, "library_Equipment119", self)
                    

    @property
    def library_NodeType(self):
        return self.__library_NodeType

    @library_NodeType.setter
    def library_NodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType", None)
        self.__library_NodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library70"):
                opp_val = getattr(old_value, "library_Library70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library70"):
                opp_val = getattr(value, "library_Library70", None)
                if opp_val is None:
                    setattr(value, "library_Library70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NodeType127(self):
        return self.__library_NodeType127

    @library_NodeType127.setter
    def library_NodeType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType127", None)
        self.__library_NodeType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo126"):
                opp_val = getattr(old_value, "library_ProductInfo126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo126"):
                opp_val = getattr(value, "library_ProductInfo126", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NodeType143(self):
        return self.__library_NodeType143

    @library_NodeType143.setter
    def library_NodeType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType143", None)
        self.__library_NodeType143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ReferenceRelationship142"):
                opp_val = getattr(old_value, "library_ReferenceRelationship142", None)
                if opp_val == self:
                    setattr(old_value, "library_ReferenceRelationship142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ReferenceRelationship142"):
                opp_val = getattr(value, "library_ReferenceRelationship142", None)
                setattr(value, "library_ReferenceRelationship142", self)

    @property
    def library_NodeType115(self):
        return self.__library_NodeType115

    @library_NodeType115.setter
    def library_NodeType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType115", None)
        self.__library_NodeType115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function116"):
                    opp_val = getattr(item, "library_Function116", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function116"):
                    opp_val = getattr(item, "library_Function116", None)
                    
                    setattr(item, "library_Function116", self)
                    

    @property
    def library_NodeType146(self):
        return self.__library_NodeType146

    @library_NodeType146.setter
    def library_NodeType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType146", None)
        self.__library_NodeType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ReferenceRelationship145"):
                opp_val = getattr(old_value, "library_ReferenceRelationship145", None)
                if opp_val == self:
                    setattr(old_value, "library_ReferenceRelationship145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ReferenceRelationship145"):
                opp_val = getattr(value, "library_ReferenceRelationship145", None)
                setattr(value, "library_ReferenceRelationship145", self)

    @property
    def library_NodeType132(self):
        return self.__library_NodeType132

    @library_NodeType132.setter
    def library_NodeType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType132", None)
        self.__library_NodeType132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ReferenceNetwork131"):
                opp_val = getattr(old_value, "library_ReferenceNetwork131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ReferenceNetwork131"):
                opp_val = getattr(value, "library_ReferenceNetwork131", None)
                if opp_val is None:
                    setattr(value, "library_ReferenceNetwork131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_EquipmentGroup(Base):

    def __init__(self, count: str, description: str, name: str, library_EquipmentGroup: "library_Equipment" = None, library_EquipmentGroup46: set["library_Parameter"] = None, library_EquipmentGroup49: set["library_NetXResource"] = None, library_EquipmentGroup52: set["library_Equipment"] = None, library_EquipmentGroup34: set["library_DiagramInfo"] = None, library_EquipmentGroup37: set["library_NetXResource"] = None, library_EquipmentGroup40: set["library_Expression"] = None, library_EquipmentGroup43: set["library_Equipment"] = None):
        self.count = count
        self.description = description
        self.name = name
        self.library_EquipmentGroup = library_EquipmentGroup
        self.library_EquipmentGroup46 = library_EquipmentGroup46 if library_EquipmentGroup46 is not None else set()
        self.library_EquipmentGroup49 = library_EquipmentGroup49 if library_EquipmentGroup49 is not None else set()
        self.library_EquipmentGroup52 = library_EquipmentGroup52 if library_EquipmentGroup52 is not None else set()
        self.library_EquipmentGroup34 = library_EquipmentGroup34 if library_EquipmentGroup34 is not None else set()
        self.library_EquipmentGroup37 = library_EquipmentGroup37 if library_EquipmentGroup37 is not None else set()
        self.library_EquipmentGroup40 = library_EquipmentGroup40 if library_EquipmentGroup40 is not None else set()
        self.library_EquipmentGroup43 = library_EquipmentGroup43 if library_EquipmentGroup43 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def library_EquipmentGroup49(self):
        return self.__library_EquipmentGroup49

    @library_EquipmentGroup49.setter
    def library_EquipmentGroup49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup49", None)
        self.__library_EquipmentGroup49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource50"):
                    opp_val = getattr(item, "library_NetXResource50", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource50"):
                    opp_val = getattr(item, "library_NetXResource50", None)
                    
                    setattr(item, "library_NetXResource50", self)
                    

    @property
    def library_EquipmentGroup43(self):
        return self.__library_EquipmentGroup43

    @library_EquipmentGroup43.setter
    def library_EquipmentGroup43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup43", None)
        self.__library_EquipmentGroup43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment44"):
                    opp_val = getattr(item, "library_Equipment44", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment44"):
                    opp_val = getattr(item, "library_Equipment44", None)
                    
                    setattr(item, "library_Equipment44", self)
                    

    @property
    def library_EquipmentGroup37(self):
        return self.__library_EquipmentGroup37

    @library_EquipmentGroup37.setter
    def library_EquipmentGroup37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup37", None)
        self.__library_EquipmentGroup37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource38"):
                    opp_val = getattr(item, "library_NetXResource38", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource38"):
                    opp_val = getattr(item, "library_NetXResource38", None)
                    
                    setattr(item, "library_NetXResource38", self)
                    

    @property
    def library_EquipmentGroup(self):
        return self.__library_EquipmentGroup

    @library_EquipmentGroup.setter
    def library_EquipmentGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup", None)
        self.__library_EquipmentGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment27"):
                opp_val = getattr(old_value, "library_Equipment27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment27"):
                opp_val = getattr(value, "library_Equipment27", None)
                if opp_val is None:
                    setattr(value, "library_Equipment27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_EquipmentGroup52(self):
        return self.__library_EquipmentGroup52

    @library_EquipmentGroup52.setter
    def library_EquipmentGroup52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup52", None)
        self.__library_EquipmentGroup52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment53"):
                    opp_val = getattr(item, "library_Equipment53", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment53"):
                    opp_val = getattr(item, "library_Equipment53", None)
                    
                    setattr(item, "library_Equipment53", self)
                    

    @property
    def library_EquipmentGroup40(self):
        return self.__library_EquipmentGroup40

    @library_EquipmentGroup40.setter
    def library_EquipmentGroup40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup40", None)
        self.__library_EquipmentGroup40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression41"):
                    opp_val = getattr(item, "library_Expression41", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression41"):
                    opp_val = getattr(item, "library_Expression41", None)
                    
                    setattr(item, "library_Expression41", self)
                    

    @property
    def library_EquipmentGroup46(self):
        return self.__library_EquipmentGroup46

    @library_EquipmentGroup46.setter
    def library_EquipmentGroup46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup46", None)
        self.__library_EquipmentGroup46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter47"):
                    opp_val = getattr(item, "library_Parameter47", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter47"):
                    opp_val = getattr(item, "library_Parameter47", None)
                    
                    setattr(item, "library_Parameter47", self)
                    

    @property
    def library_EquipmentGroup34(self):
        return self.__library_EquipmentGroup34

    @library_EquipmentGroup34.setter
    def library_EquipmentGroup34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup34", None)
        self.__library_EquipmentGroup34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo35"):
                    opp_val = getattr(item, "library_DiagramInfo35", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo35"):
                    opp_val = getattr(item, "library_DiagramInfo35", None)
                    
                    setattr(item, "library_DiagramInfo35", self)
                    

class library_ReferenceNetwork(Base):

    def __init__(self, description: str, name: str, library_ReferenceNetwork: set["library_DiagramInfo"] = None, library_ReferenceNetwork131: set["library_NodeType"] = None, library_ReferenceNetwork135: "library_ReferenceNetwork" = None, library_ReferenceNetwork133: set["library_ReferenceNetwork"] = None, library_ReferenceNetwork137: set["library_ReferenceRelationship"] = None):
        self.description = description
        self.name = name
        self.library_ReferenceNetwork = library_ReferenceNetwork if library_ReferenceNetwork is not None else set()
        self.library_ReferenceNetwork131 = library_ReferenceNetwork131 if library_ReferenceNetwork131 is not None else set()
        self.library_ReferenceNetwork135 = library_ReferenceNetwork135
        self.library_ReferenceNetwork133 = library_ReferenceNetwork133 if library_ReferenceNetwork133 is not None else set()
        self.library_ReferenceNetwork137 = library_ReferenceNetwork137 if library_ReferenceNetwork137 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def library_ReferenceNetwork137(self):
        return self.__library_ReferenceNetwork137

    @library_ReferenceNetwork137.setter
    def library_ReferenceNetwork137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceNetwork__library_ReferenceNetwork137", None)
        self.__library_ReferenceNetwork137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_ReferenceRelationship"):
                    opp_val = getattr(item, "library_ReferenceRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "library_ReferenceRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_ReferenceRelationship"):
                    opp_val = getattr(item, "library_ReferenceRelationship", None)
                    
                    setattr(item, "library_ReferenceRelationship", self)
                    

    @property
    def library_ReferenceNetwork135(self):
        return self.__library_ReferenceNetwork135

    @library_ReferenceNetwork135.setter
    def library_ReferenceNetwork135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceNetwork__library_ReferenceNetwork135", None)
        self.__library_ReferenceNetwork135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ReferenceNetwork133"):
                opp_val = getattr(old_value, "library_ReferenceNetwork133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ReferenceNetwork133"):
                opp_val = getattr(value, "library_ReferenceNetwork133", None)
                if opp_val is None:
                    setattr(value, "library_ReferenceNetwork133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_ReferenceNetwork(self):
        return self.__library_ReferenceNetwork

    @library_ReferenceNetwork.setter
    def library_ReferenceNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceNetwork__library_ReferenceNetwork", None)
        self.__library_ReferenceNetwork = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo129"):
                    opp_val = getattr(item, "library_DiagramInfo129", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo129"):
                    opp_val = getattr(item, "library_DiagramInfo129", None)
                    
                    setattr(item, "library_DiagramInfo129", self)
                    

    @property
    def library_ReferenceNetwork133(self):
        return self.__library_ReferenceNetwork133

    @library_ReferenceNetwork133.setter
    def library_ReferenceNetwork133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceNetwork__library_ReferenceNetwork133", None)
        self.__library_ReferenceNetwork133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_ReferenceNetwork135"):
                    opp_val = getattr(item, "library_ReferenceNetwork135", None)
                    
                    if opp_val == self:
                        setattr(item, "library_ReferenceNetwork135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_ReferenceNetwork135"):
                    opp_val = getattr(item, "library_ReferenceNetwork135", None)
                    
                    setattr(item, "library_ReferenceNetwork135", self)
                    

    @property
    def library_ReferenceNetwork131(self):
        return self.__library_ReferenceNetwork131

    @library_ReferenceNetwork131.setter
    def library_ReferenceNetwork131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceNetwork__library_ReferenceNetwork131", None)
        self.__library_ReferenceNetwork131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType132"):
                    opp_val = getattr(item, "library_NodeType132", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType132"):
                    opp_val = getattr(item, "library_NodeType132", None)
                    
                    setattr(item, "library_NodeType132", self)
                    

class library_Unit(Base):

    def __init__(self, code: str, description: str, name: str, library_Unit: "library_BaseResource" = None, library_Unit90: "library_Library" = None, library_Unit151: "library_MultiImage" = None):
        self.code = code
        self.description = description
        self.name = name
        self.library_Unit = library_Unit
        self.library_Unit90 = library_Unit90
        self.library_Unit151 = library_Unit151
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def library_Unit(self):
        return self.__library_Unit

    @library_Unit.setter
    def library_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit", None)
        self.__library_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_BaseResource"):
                opp_val = getattr(old_value, "library_BaseResource", None)
                if opp_val == self:
                    setattr(old_value, "library_BaseResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BaseResource"):
                opp_val = getattr(value, "library_BaseResource", None)
                setattr(value, "library_BaseResource", self)

    @property
    def library_Unit151(self):
        return self.__library_Unit151

    @library_Unit151.setter
    def library_Unit151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit151", None)
        self.__library_Unit151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage152"):
                opp_val = getattr(old_value, "library_MultiImage152", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage152"):
                opp_val = getattr(value, "library_MultiImage152", None)
                setattr(value, "library_MultiImage152", self)

    @property
    def library_Unit90(self):
        return self.__library_Unit90

    @library_Unit90.setter
    def library_Unit90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit90", None)
        self.__library_Unit90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library89"):
                opp_val = getattr(old_value, "library_Library89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library89"):
                opp_val = getattr(value, "library_Library89", None)
                if opp_val is None:
                    setattr(value, "library_Library89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Component(Base):

    def __init__(self, duration: str, name: str, description: str, library_Component: "library_Lifecycle" = None, library_Component10: "library_Expression" = None, componentRef: set["library_NetXResource"] = None, library_Component13: set["library_Tolerance"] = None, library_Component15: set["library_Protocol"] = None, library_Component17: set["library_Parameter"] = None, library_Component4: set["library_ConfigAttribute"] = None, library_Component6: set["library_Metric"] = None, library_Component8: "library_Expression" = None, library_Component19: set["library_NetXResource"] = None, library_Component21: set["library_DiagramInfo"] = None, library_Component23: "library_MultiImage" = None, Component: "library_NetXResource" = None):
        self.duration = duration
        self.name = name
        self.description = description
        self.library_Component = library_Component
        self.library_Component10 = library_Component10
        self.componentRef = componentRef if componentRef is not None else set()
        self.library_Component13 = library_Component13 if library_Component13 is not None else set()
        self.library_Component15 = library_Component15 if library_Component15 is not None else set()
        self.library_Component17 = library_Component17 if library_Component17 is not None else set()
        self.library_Component4 = library_Component4 if library_Component4 is not None else set()
        self.library_Component6 = library_Component6 if library_Component6 is not None else set()
        self.library_Component8 = library_Component8
        self.library_Component19 = library_Component19 if library_Component19 is not None else set()
        self.library_Component21 = library_Component21 if library_Component21 is not None else set()
        self.library_Component23 = library_Component23
        self.Component = Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def library_Component15(self):
        return self.__library_Component15

    @library_Component15.setter
    def library_Component15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component15", None)
        self.__library_Component15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Protocol"):
                    opp_val = getattr(item, "library_Protocol", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Protocol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Protocol"):
                    opp_val = getattr(item, "library_Protocol", None)
                    
                    setattr(item, "library_Protocol", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceRefs"):
                opp_val = getattr(old_value, "resourceRefs", None)
                if opp_val == self:
                    setattr(old_value, "resourceRefs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceRefs"):
                opp_val = getattr(value, "resourceRefs", None)
                setattr(value, "resourceRefs", self)

    @property
    def library_Component4(self):
        return self.__library_Component4

    @library_Component4.setter
    def library_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component4", None)
        self.__library_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_ConfigAttribute"):
                    opp_val = getattr(item, "library_ConfigAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "library_ConfigAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_ConfigAttribute"):
                    opp_val = getattr(item, "library_ConfigAttribute", None)
                    
                    setattr(item, "library_ConfigAttribute", self)
                    

    @property
    def library_Component8(self):
        return self.__library_Component8

    @library_Component8.setter
    def library_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component8", None)
        self.__library_Component8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression"):
                opp_val = getattr(old_value, "library_Expression", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression"):
                opp_val = getattr(value, "library_Expression", None)
                setattr(value, "library_Expression", self)

    @property
    def library_Component17(self):
        return self.__library_Component17

    @library_Component17.setter
    def library_Component17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component17", None)
        self.__library_Component17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter"):
                    opp_val = getattr(item, "library_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter"):
                    opp_val = getattr(item, "library_Parameter", None)
                    
                    setattr(item, "library_Parameter", self)
                    

    @property
    def library_Component10(self):
        return self.__library_Component10

    @library_Component10.setter
    def library_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component10", None)
        self.__library_Component10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression11"):
                opp_val = getattr(old_value, "library_Expression11", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression11"):
                opp_val = getattr(value, "library_Expression11", None)
                setattr(value, "library_Expression11", self)

    @property
    def library_Component21(self):
        return self.__library_Component21

    @library_Component21.setter
    def library_Component21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component21", None)
        self.__library_Component21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo"):
                    opp_val = getattr(item, "library_DiagramInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo"):
                    opp_val = getattr(item, "library_DiagramInfo", None)
                    
                    setattr(item, "library_DiagramInfo", self)
                    

    @property
    def library_Component(self):
        return self.__library_Component

    @library_Component.setter
    def library_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component", None)
        self.__library_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Lifecycle"):
                opp_val = getattr(old_value, "library_Lifecycle", None)
                if opp_val == self:
                    setattr(old_value, "library_Lifecycle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Lifecycle"):
                opp_val = getattr(value, "library_Lifecycle", None)
                setattr(value, "library_Lifecycle", self)

    @property
    def componentRef(self):
        return self.__componentRef

    @componentRef.setter
    def componentRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__componentRef", None)
        self.__componentRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NetXResource"):
                    opp_val = getattr(item, "NetXResource", None)
                    
                    if opp_val == self:
                        setattr(item, "NetXResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NetXResource"):
                    opp_val = getattr(item, "NetXResource", None)
                    
                    setattr(item, "NetXResource", self)
                    

    @property
    def library_Component23(self):
        return self.__library_Component23

    @library_Component23.setter
    def library_Component23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component23", None)
        self.__library_Component23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage"):
                opp_val = getattr(old_value, "library_MultiImage", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage"):
                opp_val = getattr(value, "library_MultiImage", None)
                setattr(value, "library_MultiImage", self)

    @property
    def library_Component13(self):
        return self.__library_Component13

    @library_Component13.setter
    def library_Component13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component13", None)
        self.__library_Component13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance"):
                    opp_val = getattr(item, "library_Tolerance", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance"):
                    opp_val = getattr(item, "library_Tolerance", None)
                    
                    setattr(item, "library_Tolerance", self)
                    

    @property
    def library_Component19(self):
        return self.__library_Component19

    @library_Component19.setter
    def library_Component19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component19", None)
        self.__library_Component19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource"):
                    opp_val = getattr(item, "library_NetXResource", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource"):
                    opp_val = getattr(item, "library_NetXResource", None)
                    
                    setattr(item, "library_NetXResource", self)
                    

    @property
    def library_Component6(self):
        return self.__library_Component6

    @library_Component6.setter
    def library_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component6", None)
        self.__library_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric"):
                    opp_val = getattr(item, "library_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric"):
                    opp_val = getattr(item, "library_Metric", None)
                    
                    setattr(item, "library_Metric", self)
                    

class library_Tolerance(Base):

    def __init__(self, level: str, name: str, library_Tolerance: "library_Component" = None, library_Tolerance84: "library_Library" = None, library_Tolerance148: "library_Expression" = None):
        self.level = level
        self.name = name
        self.library_Tolerance = library_Tolerance
        self.library_Tolerance84 = library_Tolerance84
        self.library_Tolerance148 = library_Tolerance148
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def library_Tolerance84(self):
        return self.__library_Tolerance84

    @library_Tolerance84.setter
    def library_Tolerance84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance84", None)
        self.__library_Tolerance84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library83"):
                opp_val = getattr(old_value, "library_Library83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library83"):
                opp_val = getattr(value, "library_Library83", None)
                if opp_val is None:
                    setattr(value, "library_Library83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Tolerance148(self):
        return self.__library_Tolerance148

    @library_Tolerance148.setter
    def library_Tolerance148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance148", None)
        self.__library_Tolerance148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression149"):
                opp_val = getattr(old_value, "library_Expression149", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression149"):
                opp_val = getattr(value, "library_Expression149", None)
                setattr(value, "library_Expression149", self)

    @property
    def library_Tolerance(self):
        return self.__library_Tolerance

    @library_Tolerance.setter
    def library_Tolerance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance", None)
        self.__library_Tolerance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Component13"):
                opp_val = getattr(old_value, "library_Component13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component13"):
                opp_val = getattr(value, "library_Component13", None)
                if opp_val is None:
                    setattr(value, "library_Component13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_ProductInfo(Base):

    def __init__(self, availableDate: str, salesCode: str, underDevelopmentDate: str, endOfSalesDate: str, endOfSupportDate: str, productCode: str, library_ProductInfo123: set["library_Function"] = None, library_ProductInfo126: set["library_NodeType"] = None, library_ProductInfo: set["library_Equipment"] = None, library_ProductInfo154: "library_Vendor" = None):
        self.availableDate = availableDate
        self.salesCode = salesCode
        self.underDevelopmentDate = underDevelopmentDate
        self.endOfSalesDate = endOfSalesDate
        self.endOfSupportDate = endOfSupportDate
        self.productCode = productCode
        self.library_ProductInfo123 = library_ProductInfo123 if library_ProductInfo123 is not None else set()
        self.library_ProductInfo126 = library_ProductInfo126 if library_ProductInfo126 is not None else set()
        self.library_ProductInfo = library_ProductInfo if library_ProductInfo is not None else set()
        self.library_ProductInfo154 = library_ProductInfo154
        
    @property
    def underDevelopmentDate(self) -> str:
        return self.__underDevelopmentDate

    @underDevelopmentDate.setter
    def underDevelopmentDate(self, underDevelopmentDate: str):
        self.__underDevelopmentDate = underDevelopmentDate

    @property
    def endOfSupportDate(self) -> str:
        return self.__endOfSupportDate

    @endOfSupportDate.setter
    def endOfSupportDate(self, endOfSupportDate: str):
        self.__endOfSupportDate = endOfSupportDate

    @property
    def productCode(self) -> str:
        return self.__productCode

    @productCode.setter
    def productCode(self, productCode: str):
        self.__productCode = productCode

    @property
    def endOfSalesDate(self) -> str:
        return self.__endOfSalesDate

    @endOfSalesDate.setter
    def endOfSalesDate(self, endOfSalesDate: str):
        self.__endOfSalesDate = endOfSalesDate

    @property
    def salesCode(self) -> str:
        return self.__salesCode

    @salesCode.setter
    def salesCode(self, salesCode: str):
        self.__salesCode = salesCode

    @property
    def availableDate(self) -> str:
        return self.__availableDate

    @availableDate.setter
    def availableDate(self, availableDate: str):
        self.__availableDate = availableDate

    @property
    def library_ProductInfo123(self):
        return self.__library_ProductInfo123

    @library_ProductInfo123.setter
    def library_ProductInfo123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo123", None)
        self.__library_ProductInfo123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function124"):
                    opp_val = getattr(item, "library_Function124", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function124"):
                    opp_val = getattr(item, "library_Function124", None)
                    
                    setattr(item, "library_Function124", self)
                    

    @property
    def library_ProductInfo(self):
        return self.__library_ProductInfo

    @library_ProductInfo.setter
    def library_ProductInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo", None)
        self.__library_ProductInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment121"):
                    opp_val = getattr(item, "library_Equipment121", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment121"):
                    opp_val = getattr(item, "library_Equipment121", None)
                    
                    setattr(item, "library_Equipment121", self)
                    

    @property
    def library_ProductInfo126(self):
        return self.__library_ProductInfo126

    @library_ProductInfo126.setter
    def library_ProductInfo126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo126", None)
        self.__library_ProductInfo126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType127"):
                    opp_val = getattr(item, "library_NodeType127", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType127"):
                    opp_val = getattr(item, "library_NodeType127", None)
                    
                    setattr(item, "library_NodeType127", self)
                    

    @property
    def library_ProductInfo154(self):
        return self.__library_ProductInfo154

    @library_ProductInfo154.setter
    def library_ProductInfo154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo154", None)
        self.__library_ProductInfo154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Vendor"):
                opp_val = getattr(old_value, "library_Vendor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Vendor"):
                opp_val = getattr(value, "library_Vendor", None)
                if opp_val is None:
                    setattr(value, "library_Vendor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_ReferenceRelationship(Base):

    def __init__(self, name: str, library_ReferenceRelationship139: "library_Protocol" = None, library_ReferenceRelationship: "library_ReferenceNetwork" = None, library_ReferenceRelationship142: "library_NodeType" = None, library_ReferenceRelationship145: "library_NodeType" = None):
        self.name = name
        self.library_ReferenceRelationship139 = library_ReferenceRelationship139
        self.library_ReferenceRelationship = library_ReferenceRelationship
        self.library_ReferenceRelationship142 = library_ReferenceRelationship142
        self.library_ReferenceRelationship145 = library_ReferenceRelationship145
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_ReferenceRelationship(self):
        return self.__library_ReferenceRelationship

    @library_ReferenceRelationship.setter
    def library_ReferenceRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceRelationship__library_ReferenceRelationship", None)
        self.__library_ReferenceRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ReferenceNetwork137"):
                opp_val = getattr(old_value, "library_ReferenceNetwork137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ReferenceNetwork137"):
                opp_val = getattr(value, "library_ReferenceNetwork137", None)
                if opp_val is None:
                    setattr(value, "library_ReferenceNetwork137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_ReferenceRelationship145(self):
        return self.__library_ReferenceRelationship145

    @library_ReferenceRelationship145.setter
    def library_ReferenceRelationship145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceRelationship__library_ReferenceRelationship145", None)
        self.__library_ReferenceRelationship145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType146"):
                opp_val = getattr(old_value, "library_NodeType146", None)
                if opp_val == self:
                    setattr(old_value, "library_NodeType146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType146"):
                opp_val = getattr(value, "library_NodeType146", None)
                setattr(value, "library_NodeType146", self)

    @property
    def library_ReferenceRelationship142(self):
        return self.__library_ReferenceRelationship142

    @library_ReferenceRelationship142.setter
    def library_ReferenceRelationship142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceRelationship__library_ReferenceRelationship142", None)
        self.__library_ReferenceRelationship142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType143"):
                opp_val = getattr(old_value, "library_NodeType143", None)
                if opp_val == self:
                    setattr(old_value, "library_NodeType143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType143"):
                opp_val = getattr(value, "library_NodeType143", None)
                setattr(value, "library_NodeType143", self)

    @property
    def library_ReferenceRelationship139(self):
        return self.__library_ReferenceRelationship139

    @library_ReferenceRelationship139.setter
    def library_ReferenceRelationship139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ReferenceRelationship__library_ReferenceRelationship139", None)
        self.__library_ReferenceRelationship139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Protocol140"):
                opp_val = getattr(old_value, "library_Protocol140", None)
                if opp_val == self:
                    setattr(old_value, "library_Protocol140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Protocol140"):
                opp_val = getattr(value, "library_Protocol140", None)
                setattr(value, "library_Protocol140", self)

class library_Expression(Base):

    def __init__(self, name: str, expressionLines: str, library_Expression11: "library_Component" = None, library_Expression: "library_Component" = None, library_Expression41: "library_EquipmentGroup" = None, library_Expression55: "library_EObject" = None, library_Expression87: "library_Library" = None, library_Expression149: "library_Tolerance" = None):
        self.name = name
        self.expressionLines = expressionLines
        self.library_Expression11 = library_Expression11
        self.library_Expression = library_Expression
        self.library_Expression41 = library_Expression41
        self.library_Expression55 = library_Expression55
        self.library_Expression87 = library_Expression87
        self.library_Expression149 = library_Expression149
        
    @property
    def expressionLines(self) -> str:
        return self.__expressionLines

    @expressionLines.setter
    def expressionLines(self, expressionLines: str):
        self.__expressionLines = expressionLines

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Expression87(self):
        return self.__library_Expression87

    @library_Expression87.setter
    def library_Expression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression87", None)
        self.__library_Expression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library86"):
                opp_val = getattr(old_value, "library_Library86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library86"):
                opp_val = getattr(value, "library_Library86", None)
                if opp_val is None:
                    setattr(value, "library_Library86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression41(self):
        return self.__library_Expression41

    @library_Expression41.setter
    def library_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression41", None)
        self.__library_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup40"):
                opp_val = getattr(old_value, "library_EquipmentGroup40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup40"):
                opp_val = getattr(value, "library_EquipmentGroup40", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression149(self):
        return self.__library_Expression149

    @library_Expression149.setter
    def library_Expression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression149", None)
        self.__library_Expression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Tolerance148"):
                opp_val = getattr(old_value, "library_Tolerance148", None)
                if opp_val == self:
                    setattr(old_value, "library_Tolerance148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Tolerance148"):
                opp_val = getattr(value, "library_Tolerance148", None)
                setattr(value, "library_Tolerance148", self)

    @property
    def library_Expression11(self):
        return self.__library_Expression11

    @library_Expression11.setter
    def library_Expression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression11", None)
        self.__library_Expression11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Component10"):
                opp_val = getattr(old_value, "library_Component10", None)
                if opp_val == self:
                    setattr(old_value, "library_Component10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component10"):
                opp_val = getattr(value, "library_Component10", None)
                setattr(value, "library_Component10", self)

    @property
    def library_Expression55(self):
        return self.__library_Expression55

    @library_Expression55.setter
    def library_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression55", None)
        self.__library_Expression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EObject"):
                opp_val = getattr(old_value, "library_EObject", None)
                if opp_val == self:
                    setattr(old_value, "library_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EObject"):
                opp_val = getattr(value, "library_EObject", None)
                setattr(value, "library_EObject", self)

    @property
    def library_Expression(self):
        return self.__library_Expression

    @library_Expression.setter
    def library_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression", None)
        self.__library_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Component8"):
                opp_val = getattr(old_value, "library_Component8", None)
                if opp_val == self:
                    setattr(old_value, "library_Component8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component8"):
                opp_val = getattr(value, "library_Component8", None)
                setattr(value, "library_Component8", self)

class library_BaseResource(Base):

    def __init__(self, shortName: str, summaryDisplay: str, detailDisplay: str, expressionName: str, longName: str, library_BaseResource: "library_Unit" = None, library_BaseResource57: "library_ExpressionResult" = None):
        self.shortName = shortName
        self.summaryDisplay = summaryDisplay
        self.detailDisplay = detailDisplay
        self.expressionName = expressionName
        self.longName = longName
        self.library_BaseResource = library_BaseResource
        self.library_BaseResource57 = library_BaseResource57
        
    @property
    def detailDisplay(self) -> str:
        return self.__detailDisplay

    @detailDisplay.setter
    def detailDisplay(self, detailDisplay: str):
        self.__detailDisplay = detailDisplay

    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def longName(self) -> str:
        return self.__longName

    @longName.setter
    def longName(self, longName: str):
        self.__longName = longName

    @property
    def summaryDisplay(self) -> str:
        return self.__summaryDisplay

    @summaryDisplay.setter
    def summaryDisplay(self, summaryDisplay: str):
        self.__summaryDisplay = summaryDisplay

    @property
    def library_BaseResource(self):
        return self.__library_BaseResource

    @library_BaseResource.setter
    def library_BaseResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BaseResource__library_BaseResource", None)
        self.__library_BaseResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Unit"):
                opp_val = getattr(old_value, "library_Unit", None)
                if opp_val == self:
                    setattr(old_value, "library_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Unit"):
                opp_val = getattr(value, "library_Unit", None)
                setattr(value, "library_Unit", self)

    @property
    def library_BaseResource57(self):
        return self.__library_BaseResource57

    @library_BaseResource57.setter
    def library_BaseResource57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BaseResource__library_BaseResource57", None)
        self.__library_BaseResource57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ExpressionResult"):
                opp_val = getattr(old_value, "library_ExpressionResult", None)
                if opp_val == self:
                    setattr(old_value, "library_ExpressionResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ExpressionResult"):
                opp_val = getattr(value, "library_ExpressionResult", None)
                setattr(value, "library_ExpressionResult", self)

class library_BaseExpressionResult:

    pass