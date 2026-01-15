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
class RedundancyType(Enum):
    n = "n"
    n1 = "n1"
    _11 = "_11"
class LevelKind(Enum):
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
class StateType(Enum):
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    IDLE = "IDLE"
    DEFECT = "DEFECT"
    RESERVED = "RESERVED"


############################################
# Definition of Classes
############################################

class Company:

    pass
class library_Vendor(Company):

    pass
class BaseResource:

    pass
class library_Meta:

    pass
class library_MetricValueRange:

    pass
class library_MetricSource:

    pass
class library_Library:

    def __init__(self, protocols: str, name: str, library_Library: set["library_Function"] = None, library_Library68: set["library_NodeType"] = None, library_Library70: set["library_Equipment"] = None, library_Library73: set["library_Metric"] = None, library_Library81: set["library_Tolerance"] = None, library_Library84: set["library_Expression"] = None, library_Library87: set["library_Unit"] = None, library_Library76: set["library_MetricSource"] = None, library_Library78: set["library_Parameter"] = None, library_Library90: "library_Meta" = None):
        self.protocols = protocols
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library68 = library_Library68 if library_Library68 is not None else set()
        self.library_Library70 = library_Library70 if library_Library70 is not None else set()
        self.library_Library73 = library_Library73 if library_Library73 is not None else set()
        self.library_Library81 = library_Library81 if library_Library81 is not None else set()
        self.library_Library84 = library_Library84 if library_Library84 is not None else set()
        self.library_Library87 = library_Library87 if library_Library87 is not None else set()
        self.library_Library76 = library_Library76 if library_Library76 is not None else set()
        self.library_Library78 = library_Library78 if library_Library78 is not None else set()
        self.library_Library90 = library_Library90
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def protocols(self) -> str:
        return self.__protocols

    @protocols.setter
    def protocols(self, protocols: str):
        self.__protocols = protocols

    @property
    def library_Library84(self):
        return self.__library_Library84

    @library_Library84.setter
    def library_Library84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library84", None)
        self.__library_Library84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression85"):
                    opp_val = getattr(item, "library_Expression85", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression85"):
                    opp_val = getattr(item, "library_Expression85", None)
                    
                    setattr(item, "library_Expression85", self)
                    

    @property
    def library_Library73(self):
        return self.__library_Library73

    @library_Library73.setter
    def library_Library73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library73", None)
        self.__library_Library73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric74"):
                    opp_val = getattr(item, "library_Metric74", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric74"):
                    opp_val = getattr(item, "library_Metric74", None)
                    
                    setattr(item, "library_Metric74", self)
                    

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
                if hasattr(item, "library_Function66"):
                    opp_val = getattr(item, "library_Function66", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function66"):
                    opp_val = getattr(item, "library_Function66", None)
                    
                    setattr(item, "library_Function66", self)
                    

    @property
    def library_Library81(self):
        return self.__library_Library81

    @library_Library81.setter
    def library_Library81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library81", None)
        self.__library_Library81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance82"):
                    opp_val = getattr(item, "library_Tolerance82", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance82"):
                    opp_val = getattr(item, "library_Tolerance82", None)
                    
                    setattr(item, "library_Tolerance82", self)
                    

    @property
    def library_Library68(self):
        return self.__library_Library68

    @library_Library68.setter
    def library_Library68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library68", None)
        self.__library_Library68 = value if value is not None else set()
        
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
    def library_Library90(self):
        return self.__library_Library90

    @library_Library90.setter
    def library_Library90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library90", None)
        self.__library_Library90 = value
        
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
                if hasattr(item, "library_Parameter79"):
                    opp_val = getattr(item, "library_Parameter79", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter79"):
                    opp_val = getattr(item, "library_Parameter79", None)
                    
                    setattr(item, "library_Parameter79", self)
                    

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
                if hasattr(item, "library_Equipment71"):
                    opp_val = getattr(item, "library_Equipment71", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment71"):
                    opp_val = getattr(item, "library_Equipment71", None)
                    
                    setattr(item, "library_Equipment71", self)
                    

    @property
    def library_Library76(self):
        return self.__library_Library76

    @library_Library76.setter
    def library_Library76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library76", None)
        self.__library_Library76 = value if value is not None else set()
        
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
    def library_Library87(self):
        return self.__library_Library87

    @library_Library87.setter
    def library_Library87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library87", None)
        self.__library_Library87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Unit88"):
                    opp_val = getattr(item, "library_Unit88", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Unit88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Unit88"):
                    opp_val = getattr(item, "library_Unit88", None)
                    
                    setattr(item, "library_Unit88", self)
                    

class library_FunctionRelationship:

    pass
class library_EObject:

    pass
class library_Value:

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

    def __init__(self, targetRange: str, targetIntervalHint: str, targetKindHint: str, library_ExpressionResult: "library_BaseResource" = None, library_ExpressionResult57: set["library_Value"] = None):
        self.targetRange = targetRange
        self.targetIntervalHint = targetIntervalHint
        self.targetKindHint = targetKindHint
        self.library_ExpressionResult = library_ExpressionResult
        self.library_ExpressionResult57 = library_ExpressionResult57 if library_ExpressionResult57 is not None else set()
        
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
            if hasattr(old_value, "library_BaseResource55"):
                opp_val = getattr(old_value, "library_BaseResource55", None)
                if opp_val == self:
                    setattr(old_value, "library_BaseResource55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BaseResource55"):
                opp_val = getattr(value, "library_BaseResource55", None)
                setattr(value, "library_BaseResource55", self)

    @property
    def library_ExpressionResult57(self):
        return self.__library_ExpressionResult57

    @library_ExpressionResult57.setter
    def library_ExpressionResult57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ExpressionResult__library_ExpressionResult57", None)
        self.__library_ExpressionResult57 = value if value is not None else set()
        
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

    def __init__(self, count: str, equipmentCode: str, position: str, redundancy: str, state: str, library_Equipment: "library_Equipment" = None, library_Equipment22: set["library_Equipment"] = None, library_Equipment30: "library_Equipment" = None, library_Equipment28: set["library_Equipment"] = None, library_Equipment25: set["library_EquipmentGroup"] = None, library_Equipment27: set["library_EquipmentRelationship"] = None, library_Equipment42: "library_EquipmentGroup" = None, library_Equipment51: "library_EquipmentGroup" = None, library_Equipment71: "library_Library" = None, library_Equipment117: "library_NodeType" = None, library_Equipment119: "library_ProductInfo" = None):
        self.count = count
        self.equipmentCode = equipmentCode
        self.position = position
        self.redundancy = redundancy
        self.state = state
        self.library_Equipment = library_Equipment
        self.library_Equipment22 = library_Equipment22 if library_Equipment22 is not None else set()
        self.library_Equipment30 = library_Equipment30
        self.library_Equipment28 = library_Equipment28 if library_Equipment28 is not None else set()
        self.library_Equipment25 = library_Equipment25 if library_Equipment25 is not None else set()
        self.library_Equipment27 = library_Equipment27 if library_Equipment27 is not None else set()
        self.library_Equipment42 = library_Equipment42
        self.library_Equipment51 = library_Equipment51
        self.library_Equipment71 = library_Equipment71
        self.library_Equipment117 = library_Equipment117
        self.library_Equipment119 = library_Equipment119
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def equipmentCode(self) -> str:
        return self.__equipmentCode

    @equipmentCode.setter
    def equipmentCode(self, equipmentCode: str):
        self.__equipmentCode = equipmentCode

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def redundancy(self) -> str:
        return self.__redundancy

    @redundancy.setter
    def redundancy(self, redundancy: str):
        self.__redundancy = redundancy

    @property
    def library_Equipment42(self):
        return self.__library_Equipment42

    @library_Equipment42.setter
    def library_Equipment42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment42", None)
        self.__library_Equipment42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup41"):
                opp_val = getattr(old_value, "library_EquipmentGroup41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup41"):
                opp_val = getattr(value, "library_EquipmentGroup41", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment117(self):
        return self.__library_Equipment117

    @library_Equipment117.setter
    def library_Equipment117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment117", None)
        self.__library_Equipment117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType116"):
                opp_val = getattr(old_value, "library_NodeType116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType116"):
                opp_val = getattr(value, "library_NodeType116", None)
                if opp_val is None:
                    setattr(value, "library_NodeType116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment30(self):
        return self.__library_Equipment30

    @library_Equipment30.setter
    def library_Equipment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment30", None)
        self.__library_Equipment30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment28"):
                opp_val = getattr(old_value, "library_Equipment28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment28"):
                opp_val = getattr(value, "library_Equipment28", None)
                if opp_val is None:
                    setattr(value, "library_Equipment28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def library_Equipment28(self):
        return self.__library_Equipment28

    @library_Equipment28.setter
    def library_Equipment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment28", None)
        self.__library_Equipment28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment30"):
                    opp_val = getattr(item, "library_Equipment30", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment30"):
                    opp_val = getattr(item, "library_Equipment30", None)
                    
                    setattr(item, "library_Equipment30", self)
                    

    @property
    def library_Equipment51(self):
        return self.__library_Equipment51

    @library_Equipment51.setter
    def library_Equipment51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment51", None)
        self.__library_Equipment51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup50"):
                opp_val = getattr(old_value, "library_EquipmentGroup50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup50"):
                opp_val = getattr(value, "library_EquipmentGroup50", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment71(self):
        return self.__library_Equipment71

    @library_Equipment71.setter
    def library_Equipment71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment71", None)
        self.__library_Equipment71 = value
        
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
    def library_Equipment25(self):
        return self.__library_Equipment25

    @library_Equipment25.setter
    def library_Equipment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment25", None)
        self.__library_Equipment25 = value if value is not None else set()
        
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
    def library_Equipment22(self):
        return self.__library_Equipment22

    @library_Equipment22.setter
    def library_Equipment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment22", None)
        self.__library_Equipment22 = value if value is not None else set()
        
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
    def library_Equipment(self):
        return self.__library_Equipment

    @library_Equipment.setter
    def library_Equipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment", None)
        self.__library_Equipment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment22"):
                opp_val = getattr(old_value, "library_Equipment22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment22"):
                opp_val = getattr(value, "library_Equipment22", None)
                if opp_val is None:
                    setattr(value, "library_Equipment22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Metric:

    pass
class library_Protocol:

    pass
class library_NetXResource(BaseResource):

    pass
class library_Lifecycle:

    pass
class Base:

    pass
class library_Expression(Base):

    def __init__(self, name: str, expressionLines: str, library_Expression: "library_Component" = None, library_Expression9: "library_Component" = None, library_Expression39: "library_EquipmentGroup" = None, library_Expression53: "library_EObject" = None, library_Expression85: "library_Library" = None, library_Expression128: "library_Tolerance" = None):
        self.name = name
        self.expressionLines = expressionLines
        self.library_Expression = library_Expression
        self.library_Expression9 = library_Expression9
        self.library_Expression39 = library_Expression39
        self.library_Expression53 = library_Expression53
        self.library_Expression85 = library_Expression85
        self.library_Expression128 = library_Expression128
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressionLines(self) -> str:
        return self.__expressionLines

    @expressionLines.setter
    def expressionLines(self, expressionLines: str):
        self.__expressionLines = expressionLines

    @property
    def library_Expression128(self):
        return self.__library_Expression128

    @library_Expression128.setter
    def library_Expression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression128", None)
        self.__library_Expression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Tolerance127"):
                opp_val = getattr(old_value, "library_Tolerance127", None)
                if opp_val == self:
                    setattr(old_value, "library_Tolerance127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Tolerance127"):
                opp_val = getattr(value, "library_Tolerance127", None)
                setattr(value, "library_Tolerance127", self)

    @property
    def library_Expression85(self):
        return self.__library_Expression85

    @library_Expression85.setter
    def library_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression85", None)
        self.__library_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library84"):
                opp_val = getattr(old_value, "library_Library84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library84"):
                opp_val = getattr(value, "library_Library84", None)
                if opp_val is None:
                    setattr(value, "library_Library84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression53(self):
        return self.__library_Expression53

    @library_Expression53.setter
    def library_Expression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression53", None)
        self.__library_Expression53 = value
        
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
            if hasattr(old_value, "library_Component6"):
                opp_val = getattr(old_value, "library_Component6", None)
                if opp_val == self:
                    setattr(old_value, "library_Component6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component6"):
                opp_val = getattr(value, "library_Component6", None)
                setattr(value, "library_Component6", self)

    @property
    def library_Expression39(self):
        return self.__library_Expression39

    @library_Expression39.setter
    def library_Expression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression39", None)
        self.__library_Expression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup38"):
                opp_val = getattr(old_value, "library_EquipmentGroup38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup38"):
                opp_val = getattr(value, "library_EquipmentGroup38", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression9(self):
        return self.__library_Expression9

    @library_Expression9.setter
    def library_Expression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression9", None)
        self.__library_Expression9 = value
        
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

class library_Parameter(Base):

    def __init__(self, description: str, expressionName: str, modifiable: str, name: str, value: str, library_Parameter: "library_Component" = None, library_Parameter45: "library_EquipmentGroup" = None, library_Parameter79: "library_Library" = None):
        self.description = description
        self.expressionName = expressionName
        self.modifiable = modifiable
        self.name = name
        self.value = value
        self.library_Parameter = library_Parameter
        self.library_Parameter45 = library_Parameter45
        self.library_Parameter79 = library_Parameter79
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

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

    @property
    def modifiable(self) -> str:
        return self.__modifiable

    @modifiable.setter
    def modifiable(self, modifiable: str):
        self.__modifiable = modifiable

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
            if hasattr(old_value, "library_Component15"):
                opp_val = getattr(old_value, "library_Component15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component15"):
                opp_val = getattr(value, "library_Component15", None)
                if opp_val is None:
                    setattr(value, "library_Component15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter79(self):
        return self.__library_Parameter79

    @library_Parameter79.setter
    def library_Parameter79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter79", None)
        self.__library_Parameter79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library78"):
                opp_val = getattr(old_value, "library_Library78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library78"):
                opp_val = getattr(value, "library_Library78", None)
                if opp_val is None:
                    setattr(value, "library_Library78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter45(self):
        return self.__library_Parameter45

    @library_Parameter45.setter
    def library_Parameter45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter45", None)
        self.__library_Parameter45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup44"):
                opp_val = getattr(old_value, "library_EquipmentGroup44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup44"):
                opp_val = getattr(value, "library_EquipmentGroup44", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_NodeType(Base):

    def __init__(self, name: str, leafNode: str, library_NodeType: "library_Library" = None, library_NodeType113: set["library_Function"] = None, library_NodeType116: set["library_Equipment"] = None, library_NodeType125: "library_ProductInfo" = None):
        self.name = name
        self.leafNode = leafNode
        self.library_NodeType = library_NodeType
        self.library_NodeType113 = library_NodeType113 if library_NodeType113 is not None else set()
        self.library_NodeType116 = library_NodeType116 if library_NodeType116 is not None else set()
        self.library_NodeType125 = library_NodeType125
        
    @property
    def leafNode(self) -> str:
        return self.__leafNode

    @leafNode.setter
    def leafNode(self, leafNode: str):
        self.__leafNode = leafNode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_NodeType125(self):
        return self.__library_NodeType125

    @library_NodeType125.setter
    def library_NodeType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType125", None)
        self.__library_NodeType125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo124"):
                opp_val = getattr(old_value, "library_ProductInfo124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo124"):
                opp_val = getattr(value, "library_ProductInfo124", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NodeType113(self):
        return self.__library_NodeType113

    @library_NodeType113.setter
    def library_NodeType113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType113", None)
        self.__library_NodeType113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function114"):
                    opp_val = getattr(item, "library_Function114", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function114"):
                    opp_val = getattr(item, "library_Function114", None)
                    
                    setattr(item, "library_Function114", self)
                    

    @property
    def library_NodeType116(self):
        return self.__library_NodeType116

    @library_NodeType116.setter
    def library_NodeType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType116", None)
        self.__library_NodeType116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment117"):
                    opp_val = getattr(item, "library_Equipment117", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment117"):
                    opp_val = getattr(item, "library_Equipment117", None)
                    
                    setattr(item, "library_Equipment117", self)
                    

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
            if hasattr(old_value, "library_Library68"):
                opp_val = getattr(old_value, "library_Library68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library68"):
                opp_val = getattr(value, "library_Library68", None)
                if opp_val is None:
                    setattr(value, "library_Library68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_ProductInfo(Base):

    def __init__(self, availableDate: str, endOfSalesDate: str, endOfSupportDate: str, productCode: str, salesCode: str, underDevelopmentDate: str, library_ProductInfo121: set["library_Function"] = None, library_ProductInfo124: set["library_NodeType"] = None, library_ProductInfo: set["library_Equipment"] = None, library_ProductInfo133: "library_Vendor" = None):
        self.availableDate = availableDate
        self.endOfSalesDate = endOfSalesDate
        self.endOfSupportDate = endOfSupportDate
        self.productCode = productCode
        self.salesCode = salesCode
        self.underDevelopmentDate = underDevelopmentDate
        self.library_ProductInfo121 = library_ProductInfo121 if library_ProductInfo121 is not None else set()
        self.library_ProductInfo124 = library_ProductInfo124 if library_ProductInfo124 is not None else set()
        self.library_ProductInfo = library_ProductInfo if library_ProductInfo is not None else set()
        self.library_ProductInfo133 = library_ProductInfo133
        
    @property
    def underDevelopmentDate(self) -> str:
        return self.__underDevelopmentDate

    @underDevelopmentDate.setter
    def underDevelopmentDate(self, underDevelopmentDate: str):
        self.__underDevelopmentDate = underDevelopmentDate

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
    def productCode(self) -> str:
        return self.__productCode

    @productCode.setter
    def productCode(self, productCode: str):
        self.__productCode = productCode

    @property
    def endOfSupportDate(self) -> str:
        return self.__endOfSupportDate

    @endOfSupportDate.setter
    def endOfSupportDate(self, endOfSupportDate: str):
        self.__endOfSupportDate = endOfSupportDate

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
    def library_ProductInfo124(self):
        return self.__library_ProductInfo124

    @library_ProductInfo124.setter
    def library_ProductInfo124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo124", None)
        self.__library_ProductInfo124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType125"):
                    opp_val = getattr(item, "library_NodeType125", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType125"):
                    opp_val = getattr(item, "library_NodeType125", None)
                    
                    setattr(item, "library_NodeType125", self)
                    

    @property
    def library_ProductInfo121(self):
        return self.__library_ProductInfo121

    @library_ProductInfo121.setter
    def library_ProductInfo121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo121", None)
        self.__library_ProductInfo121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function122"):
                    opp_val = getattr(item, "library_Function122", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function122"):
                    opp_val = getattr(item, "library_Function122", None)
                    
                    setattr(item, "library_Function122", self)
                    

    @property
    def library_ProductInfo133(self):
        return self.__library_ProductInfo133

    @library_ProductInfo133.setter
    def library_ProductInfo133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo133", None)
        self.__library_ProductInfo133 = value
        
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

class library_Unit(Base):

    def __init__(self, code: str, description: str, name: str, library_Unit: "library_BaseResource" = None, library_Unit88: "library_Library" = None, library_Unit130: "library_MultiImage" = None):
        self.code = code
        self.description = description
        self.name = name
        self.library_Unit = library_Unit
        self.library_Unit88 = library_Unit88
        self.library_Unit130 = library_Unit130
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
    def library_Unit88(self):
        return self.__library_Unit88

    @library_Unit88.setter
    def library_Unit88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit88", None)
        self.__library_Unit88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library87"):
                opp_val = getattr(old_value, "library_Library87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library87"):
                opp_val = getattr(value, "library_Library87", None)
                if opp_val is None:
                    setattr(value, "library_Library87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Unit130(self):
        return self.__library_Unit130

    @library_Unit130.setter
    def library_Unit130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit130", None)
        self.__library_Unit130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage131"):
                opp_val = getattr(old_value, "library_MultiImage131", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage131"):
                opp_val = getattr(value, "library_MultiImage131", None)
                setattr(value, "library_MultiImage131", self)

class library_Tolerance(Base):

    def __init__(self, level: str, name: str, library_Tolerance: "library_Component" = None, library_Tolerance82: "library_Library" = None, library_Tolerance127: "library_Expression" = None):
        self.level = level
        self.name = name
        self.library_Tolerance = library_Tolerance
        self.library_Tolerance82 = library_Tolerance82
        self.library_Tolerance127 = library_Tolerance127
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Tolerance82(self):
        return self.__library_Tolerance82

    @library_Tolerance82.setter
    def library_Tolerance82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance82", None)
        self.__library_Tolerance82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library81"):
                opp_val = getattr(old_value, "library_Library81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library81"):
                opp_val = getattr(value, "library_Library81", None)
                if opp_val is None:
                    setattr(value, "library_Library81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Tolerance127(self):
        return self.__library_Tolerance127

    @library_Tolerance127.setter
    def library_Tolerance127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance127", None)
        self.__library_Tolerance127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression128"):
                opp_val = getattr(old_value, "library_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression128"):
                opp_val = getattr(value, "library_Expression128", None)
                setattr(value, "library_Expression128", self)

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
            if hasattr(old_value, "library_Component11"):
                opp_val = getattr(old_value, "library_Component11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Component11"):
                opp_val = getattr(value, "library_Component11", None)
                if opp_val is None:
                    setattr(value, "library_Component11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_EquipmentGroup(Base):

    def __init__(self, count: str, description: str, name: str, library_EquipmentGroup: "library_Equipment" = None, library_EquipmentGroup32: set["library_DiagramInfo"] = None, library_EquipmentGroup35: set["library_NetXResource"] = None, library_EquipmentGroup38: set["library_Expression"] = None, library_EquipmentGroup41: set["library_Equipment"] = None, library_EquipmentGroup50: set["library_Equipment"] = None, library_EquipmentGroup44: set["library_Parameter"] = None, library_EquipmentGroup47: set["library_NetXResource"] = None):
        self.count = count
        self.description = description
        self.name = name
        self.library_EquipmentGroup = library_EquipmentGroup
        self.library_EquipmentGroup32 = library_EquipmentGroup32 if library_EquipmentGroup32 is not None else set()
        self.library_EquipmentGroup35 = library_EquipmentGroup35 if library_EquipmentGroup35 is not None else set()
        self.library_EquipmentGroup38 = library_EquipmentGroup38 if library_EquipmentGroup38 is not None else set()
        self.library_EquipmentGroup41 = library_EquipmentGroup41 if library_EquipmentGroup41 is not None else set()
        self.library_EquipmentGroup50 = library_EquipmentGroup50 if library_EquipmentGroup50 is not None else set()
        self.library_EquipmentGroup44 = library_EquipmentGroup44 if library_EquipmentGroup44 is not None else set()
        self.library_EquipmentGroup47 = library_EquipmentGroup47 if library_EquipmentGroup47 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "library_Equipment25"):
                opp_val = getattr(old_value, "library_Equipment25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment25"):
                opp_val = getattr(value, "library_Equipment25", None)
                if opp_val is None:
                    setattr(value, "library_Equipment25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_EquipmentGroup41(self):
        return self.__library_EquipmentGroup41

    @library_EquipmentGroup41.setter
    def library_EquipmentGroup41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup41", None)
        self.__library_EquipmentGroup41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment42"):
                    opp_val = getattr(item, "library_Equipment42", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment42"):
                    opp_val = getattr(item, "library_Equipment42", None)
                    
                    setattr(item, "library_Equipment42", self)
                    

    @property
    def library_EquipmentGroup35(self):
        return self.__library_EquipmentGroup35

    @library_EquipmentGroup35.setter
    def library_EquipmentGroup35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup35", None)
        self.__library_EquipmentGroup35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource36"):
                    opp_val = getattr(item, "library_NetXResource36", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource36"):
                    opp_val = getattr(item, "library_NetXResource36", None)
                    
                    setattr(item, "library_NetXResource36", self)
                    

    @property
    def library_EquipmentGroup44(self):
        return self.__library_EquipmentGroup44

    @library_EquipmentGroup44.setter
    def library_EquipmentGroup44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup44", None)
        self.__library_EquipmentGroup44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter45"):
                    opp_val = getattr(item, "library_Parameter45", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter45"):
                    opp_val = getattr(item, "library_Parameter45", None)
                    
                    setattr(item, "library_Parameter45", self)
                    

    @property
    def library_EquipmentGroup38(self):
        return self.__library_EquipmentGroup38

    @library_EquipmentGroup38.setter
    def library_EquipmentGroup38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup38", None)
        self.__library_EquipmentGroup38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression39"):
                    opp_val = getattr(item, "library_Expression39", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression39"):
                    opp_val = getattr(item, "library_Expression39", None)
                    
                    setattr(item, "library_Expression39", self)
                    

    @property
    def library_EquipmentGroup50(self):
        return self.__library_EquipmentGroup50

    @library_EquipmentGroup50.setter
    def library_EquipmentGroup50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup50", None)
        self.__library_EquipmentGroup50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment51"):
                    opp_val = getattr(item, "library_Equipment51", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment51"):
                    opp_val = getattr(item, "library_Equipment51", None)
                    
                    setattr(item, "library_Equipment51", self)
                    

    @property
    def library_EquipmentGroup47(self):
        return self.__library_EquipmentGroup47

    @library_EquipmentGroup47.setter
    def library_EquipmentGroup47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup47", None)
        self.__library_EquipmentGroup47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource48"):
                    opp_val = getattr(item, "library_NetXResource48", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource48"):
                    opp_val = getattr(item, "library_NetXResource48", None)
                    
                    setattr(item, "library_NetXResource48", self)
                    

    @property
    def library_EquipmentGroup32(self):
        return self.__library_EquipmentGroup32

    @library_EquipmentGroup32.setter
    def library_EquipmentGroup32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup32", None)
        self.__library_EquipmentGroup32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo33"):
                    opp_val = getattr(item, "library_DiagramInfo33", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo33"):
                    opp_val = getattr(item, "library_DiagramInfo33", None)
                    
                    setattr(item, "library_DiagramInfo33", self)
                    

class library_Component(Base):

    def __init__(self, description: str, duration: str, name: str, library_Component: "library_Lifecycle" = None, componentRef: set["library_NetXResource"] = None, library_Component11: set["library_Tolerance"] = None, library_Component13: set["library_Protocol"] = None, library_Component15: set["library_Parameter"] = None, library_Component4: set["library_Metric"] = None, library_Component6: "library_Expression" = None, library_Component8: "library_Expression" = None, library_Component17: set["library_NetXResource"] = None, library_Component19: set["library_DiagramInfo"] = None, library_Component21: "library_MultiImage" = None, Component: "library_NetXResource" = None):
        self.description = description
        self.duration = duration
        self.name = name
        self.library_Component = library_Component
        self.componentRef = componentRef if componentRef is not None else set()
        self.library_Component11 = library_Component11 if library_Component11 is not None else set()
        self.library_Component13 = library_Component13 if library_Component13 is not None else set()
        self.library_Component15 = library_Component15 if library_Component15 is not None else set()
        self.library_Component4 = library_Component4 if library_Component4 is not None else set()
        self.library_Component6 = library_Component6
        self.library_Component8 = library_Component8
        self.library_Component17 = library_Component17 if library_Component17 is not None else set()
        self.library_Component19 = library_Component19 if library_Component19 is not None else set()
        self.library_Component21 = library_Component21
        self.Component = Component
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

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

    @property
    def library_Component21(self):
        return self.__library_Component21

    @library_Component21.setter
    def library_Component21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component21", None)
        self.__library_Component21 = value
        
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
    def library_Component11(self):
        return self.__library_Component11

    @library_Component11.setter
    def library_Component11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component11", None)
        self.__library_Component11 = value if value is not None else set()
        
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
    def library_Component6(self):
        return self.__library_Component6

    @library_Component6.setter
    def library_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component6", None)
        self.__library_Component6 = value
        
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
    def library_Component8(self):
        return self.__library_Component8

    @library_Component8.setter
    def library_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Component__library_Component8", None)
        self.__library_Component8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression9"):
                opp_val = getattr(old_value, "library_Expression9", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression9"):
                opp_val = getattr(value, "library_Expression9", None)
                setattr(value, "library_Expression9", self)

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

class library_BaseResource(Base):

    def __init__(self, detailDisplay: str, expressionName: str, longName: str, shortName: str, summaryDisplay: str, library_BaseResource: "library_Unit" = None, library_BaseResource55: "library_ExpressionResult" = None):
        self.detailDisplay = detailDisplay
        self.expressionName = expressionName
        self.longName = longName
        self.shortName = shortName
        self.summaryDisplay = summaryDisplay
        self.library_BaseResource = library_BaseResource
        self.library_BaseResource55 = library_BaseResource55
        
    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

    @property
    def summaryDisplay(self) -> str:
        return self.__summaryDisplay

    @summaryDisplay.setter
    def summaryDisplay(self, summaryDisplay: str):
        self.__summaryDisplay = summaryDisplay

    @property
    def detailDisplay(self) -> str:
        return self.__detailDisplay

    @detailDisplay.setter
    def detailDisplay(self, detailDisplay: str):
        self.__detailDisplay = detailDisplay

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
    def library_BaseResource55(self):
        return self.__library_BaseResource55

    @library_BaseResource55.setter
    def library_BaseResource55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BaseResource__library_BaseResource55", None)
        self.__library_BaseResource55 = value
        
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

class library_BaseExpressionResult:

    pass