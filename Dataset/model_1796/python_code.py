from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RedundancyType(Enum):
    n = "n"
    n1 = "n1"
    _11 = "_11"
class StateType(Enum):
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    IDLE = "IDLE"
    DEFECT = "DEFECT"
    RESERVED = "RESERVED"
class LevelType(Enum):
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
class library_ProductInfo:

    def __init__(self, availableDate: str, endOfSalesDate: str, endOfSupportDate: str, productCode: str, salesCode: str, underDevelopmentDate: str, library_ProductInfo153: set["library_NodeType"] = None, library_ProductInfo: set["library_Equipment"] = None, library_ProductInfo150: set["library_Function"] = None, library_ProductInfo159: "library_Vendor" = None):
        self.availableDate = availableDate
        self.endOfSalesDate = endOfSalesDate
        self.endOfSupportDate = endOfSupportDate
        self.productCode = productCode
        self.salesCode = salesCode
        self.underDevelopmentDate = underDevelopmentDate
        self.library_ProductInfo153 = library_ProductInfo153 if library_ProductInfo153 is not None else set()
        self.library_ProductInfo = library_ProductInfo if library_ProductInfo is not None else set()
        self.library_ProductInfo150 = library_ProductInfo150 if library_ProductInfo150 is not None else set()
        self.library_ProductInfo159 = library_ProductInfo159
        
    @property
    def availableDate(self) -> str:
        return self.__availableDate

    @availableDate.setter
    def availableDate(self, availableDate: str):
        self.__availableDate = availableDate

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
    def underDevelopmentDate(self) -> str:
        return self.__underDevelopmentDate

    @underDevelopmentDate.setter
    def underDevelopmentDate(self, underDevelopmentDate: str):
        self.__underDevelopmentDate = underDevelopmentDate

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
                if hasattr(item, "library_Equipment148"):
                    opp_val = getattr(item, "library_Equipment148", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment148"):
                    opp_val = getattr(item, "library_Equipment148", None)
                    
                    setattr(item, "library_Equipment148", self)
                    

    @property
    def library_ProductInfo150(self):
        return self.__library_ProductInfo150

    @library_ProductInfo150.setter
    def library_ProductInfo150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo150", None)
        self.__library_ProductInfo150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function151"):
                    opp_val = getattr(item, "library_Function151", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function151"):
                    opp_val = getattr(item, "library_Function151", None)
                    
                    setattr(item, "library_Function151", self)
                    

    @property
    def library_ProductInfo159(self):
        return self.__library_ProductInfo159

    @library_ProductInfo159.setter
    def library_ProductInfo159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo159", None)
        self.__library_ProductInfo159 = value
        
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

    @property
    def library_ProductInfo153(self):
        return self.__library_ProductInfo153

    @library_ProductInfo153.setter
    def library_ProductInfo153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo153", None)
        self.__library_ProductInfo153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType154"):
                    opp_val = getattr(item, "library_NodeType154", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType154"):
                    opp_val = getattr(item, "library_NodeType154", None)
                    
                    setattr(item, "library_NodeType154", self)
                    

class library_Value:

    pass
class library_MetricValueRange:

    pass
class library_Meta:

    pass
class library_Unit:

    def __init__(self, code: str, description: str, name: str, library_Unit: "library_Library" = None, library_Unit140: "library_NetXResource" = None, library_Unit156: "library_MultiImage" = None):
        self.code = code
        self.description = description
        self.name = name
        self.library_Unit = library_Unit
        self.library_Unit140 = library_Unit140
        self.library_Unit156 = library_Unit156
        
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
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
            if hasattr(old_value, "library_Library116"):
                opp_val = getattr(old_value, "library_Library116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library116"):
                opp_val = getattr(value, "library_Library116", None)
                if opp_val is None:
                    setattr(value, "library_Library116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Unit156(self):
        return self.__library_Unit156

    @library_Unit156.setter
    def library_Unit156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit156", None)
        self.__library_Unit156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage157"):
                opp_val = getattr(old_value, "library_MultiImage157", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage157"):
                opp_val = getattr(value, "library_MultiImage157", None)
                setattr(value, "library_MultiImage157", self)

    @property
    def library_Unit140(self):
        return self.__library_Unit140

    @library_Unit140.setter
    def library_Unit140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit140", None)
        self.__library_Unit140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NetXResource139"):
                opp_val = getattr(old_value, "library_NetXResource139", None)
                if opp_val == self:
                    setattr(old_value, "library_NetXResource139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NetXResource139"):
                opp_val = getattr(value, "library_NetXResource139", None)
                setattr(value, "library_NetXResource139", self)

class library_MetricSource:

    pass
class library_NodeType:

    def __init__(self, leafNode: str, library_NodeType: "library_Library" = None, library_NodeType142: set["library_Function"] = None, library_NodeType145: set["library_Equipment"] = None, library_NodeType154: "library_ProductInfo" = None):
        self.leafNode = leafNode
        self.library_NodeType = library_NodeType
        self.library_NodeType142 = library_NodeType142 if library_NodeType142 is not None else set()
        self.library_NodeType145 = library_NodeType145 if library_NodeType145 is not None else set()
        self.library_NodeType154 = library_NodeType154
        
    @property
    def leafNode(self) -> str:
        return self.__leafNode

    @leafNode.setter
    def leafNode(self, leafNode: str):
        self.__leafNode = leafNode

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
            if hasattr(old_value, "library_Library97"):
                opp_val = getattr(old_value, "library_Library97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library97"):
                opp_val = getattr(value, "library_Library97", None)
                if opp_val is None:
                    setattr(value, "library_Library97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NodeType145(self):
        return self.__library_NodeType145

    @library_NodeType145.setter
    def library_NodeType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType145", None)
        self.__library_NodeType145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment146"):
                    opp_val = getattr(item, "library_Equipment146", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment146"):
                    opp_val = getattr(item, "library_Equipment146", None)
                    
                    setattr(item, "library_Equipment146", self)
                    

    @property
    def library_NodeType154(self):
        return self.__library_NodeType154

    @library_NodeType154.setter
    def library_NodeType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType154", None)
        self.__library_NodeType154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo153"):
                opp_val = getattr(old_value, "library_ProductInfo153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo153"):
                opp_val = getattr(value, "library_ProductInfo153", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NodeType142(self):
        return self.__library_NodeType142

    @library_NodeType142.setter
    def library_NodeType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NodeType__library_NodeType142", None)
        self.__library_NodeType142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function143"):
                    opp_val = getattr(item, "library_Function143", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function143"):
                    opp_val = getattr(item, "library_Function143", None)
                    
                    setattr(item, "library_Function143", self)
                    

class library_Library:

    def __init__(self, protocols: str, name: str, library_Library97: set["library_NodeType"] = None, library_Library: set["library_Function"] = None, library_Library99: set["library_Equipment"] = None, library_Library102: set["library_Metric"] = None, library_Library105: set["library_MetricSource"] = None, library_Library107: set["library_Parameter"] = None, library_Library110: set["library_Tolerance"] = None, library_Library113: set["library_Expression"] = None, library_Library116: set["library_Unit"] = None, library_Library118: "library_Meta" = None):
        self.protocols = protocols
        self.name = name
        self.library_Library97 = library_Library97 if library_Library97 is not None else set()
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library99 = library_Library99 if library_Library99 is not None else set()
        self.library_Library102 = library_Library102 if library_Library102 is not None else set()
        self.library_Library105 = library_Library105 if library_Library105 is not None else set()
        self.library_Library107 = library_Library107 if library_Library107 is not None else set()
        self.library_Library110 = library_Library110 if library_Library110 is not None else set()
        self.library_Library113 = library_Library113 if library_Library113 is not None else set()
        self.library_Library116 = library_Library116 if library_Library116 is not None else set()
        self.library_Library118 = library_Library118
        
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
    def library_Library118(self):
        return self.__library_Library118

    @library_Library118.setter
    def library_Library118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library118", None)
        self.__library_Library118 = value
        
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
    def library_Library102(self):
        return self.__library_Library102

    @library_Library102.setter
    def library_Library102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library102", None)
        self.__library_Library102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric103"):
                    opp_val = getattr(item, "library_Metric103", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric103"):
                    opp_val = getattr(item, "library_Metric103", None)
                    
                    setattr(item, "library_Metric103", self)
                    

    @property
    def library_Library113(self):
        return self.__library_Library113

    @library_Library113.setter
    def library_Library113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library113", None)
        self.__library_Library113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression114"):
                    opp_val = getattr(item, "library_Expression114", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression114"):
                    opp_val = getattr(item, "library_Expression114", None)
                    
                    setattr(item, "library_Expression114", self)
                    

    @property
    def library_Library107(self):
        return self.__library_Library107

    @library_Library107.setter
    def library_Library107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library107", None)
        self.__library_Library107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter108"):
                    opp_val = getattr(item, "library_Parameter108", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter108"):
                    opp_val = getattr(item, "library_Parameter108", None)
                    
                    setattr(item, "library_Parameter108", self)
                    

    @property
    def library_Library116(self):
        return self.__library_Library116

    @library_Library116.setter
    def library_Library116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library116", None)
        self.__library_Library116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Unit"):
                    opp_val = getattr(item, "library_Unit", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Unit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Unit"):
                    opp_val = getattr(item, "library_Unit", None)
                    
                    setattr(item, "library_Unit", self)
                    

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
                if hasattr(item, "library_Function95"):
                    opp_val = getattr(item, "library_Function95", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function95"):
                    opp_val = getattr(item, "library_Function95", None)
                    
                    setattr(item, "library_Function95", self)
                    

    @property
    def library_Library99(self):
        return self.__library_Library99

    @library_Library99.setter
    def library_Library99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library99", None)
        self.__library_Library99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment100"):
                    opp_val = getattr(item, "library_Equipment100", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment100"):
                    opp_val = getattr(item, "library_Equipment100", None)
                    
                    setattr(item, "library_Equipment100", self)
                    

    @property
    def library_Library105(self):
        return self.__library_Library105

    @library_Library105.setter
    def library_Library105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library105", None)
        self.__library_Library105 = value if value is not None else set()
        
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
    def library_Library97(self):
        return self.__library_Library97

    @library_Library97.setter
    def library_Library97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library97", None)
        self.__library_Library97 = value if value is not None else set()
        
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
    def library_Library110(self):
        return self.__library_Library110

    @library_Library110.setter
    def library_Library110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library110", None)
        self.__library_Library110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance111"):
                    opp_val = getattr(item, "library_Tolerance111", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance111"):
                    opp_val = getattr(item, "library_Tolerance111", None)
                    
                    setattr(item, "library_Tolerance111", self)
                    

class library_FunctionRelationship:

    pass
class library_ExpressionResult:

    pass
class library_ServiceProfile:

    pass
class library_Function:

    def __init__(self, description: str, functionName: str, Function: "library_Expression" = None, library_Function: set["library_DiagramInfo"] = None, library_Function61: "library_MultiImage" = None, library_Function65: "library_Function" = None, library_Function63: set["library_Function"] = None, library_Function67: set["library_NetXResource"] = None, library_Function70: set["library_Metric"] = None, library_Function73: set["library_FunctionRelationship"] = None, functionRefs: set["library_Expression"] = None, library_Function77: "library_Expression" = None, library_Function80: set["library_Tolerance"] = None, library_Function83: set["library_Protocol"] = None, library_Function86: set["library_Parameter"] = None, library_Function89: set["library_NetXResource"] = None, library_Function93: "library_Function" = None, library_Function91: set["library_Function"] = None, library_Function95: "library_Library" = None, library_Function143: "library_NodeType" = None, library_Function151: "library_ProductInfo" = None):
        self.description = description
        self.functionName = functionName
        self.Function = Function
        self.library_Function = library_Function if library_Function is not None else set()
        self.library_Function61 = library_Function61
        self.library_Function65 = library_Function65
        self.library_Function63 = library_Function63 if library_Function63 is not None else set()
        self.library_Function67 = library_Function67 if library_Function67 is not None else set()
        self.library_Function70 = library_Function70 if library_Function70 is not None else set()
        self.library_Function73 = library_Function73 if library_Function73 is not None else set()
        self.functionRefs = functionRefs if functionRefs is not None else set()
        self.library_Function77 = library_Function77
        self.library_Function80 = library_Function80 if library_Function80 is not None else set()
        self.library_Function83 = library_Function83 if library_Function83 is not None else set()
        self.library_Function86 = library_Function86 if library_Function86 is not None else set()
        self.library_Function89 = library_Function89 if library_Function89 is not None else set()
        self.library_Function93 = library_Function93
        self.library_Function91 = library_Function91 if library_Function91 is not None else set()
        self.library_Function95 = library_Function95
        self.library_Function143 = library_Function143
        self.library_Function151 = library_Function151
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def library_Function86(self):
        return self.__library_Function86

    @library_Function86.setter
    def library_Function86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function86", None)
        self.__library_Function86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Parameter87"):
                    opp_val = getattr(item, "library_Parameter87", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter87"):
                    opp_val = getattr(item, "library_Parameter87", None)
                    
                    setattr(item, "library_Parameter87", self)
                    

    @property
    def library_Function83(self):
        return self.__library_Function83

    @library_Function83.setter
    def library_Function83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function83", None)
        self.__library_Function83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Protocol84"):
                    opp_val = getattr(item, "library_Protocol84", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Protocol84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Protocol84"):
                    opp_val = getattr(item, "library_Protocol84", None)
                    
                    setattr(item, "library_Protocol84", self)
                    

    @property
    def library_Function61(self):
        return self.__library_Function61

    @library_Function61.setter
    def library_Function61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function61", None)
        self.__library_Function61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage62"):
                opp_val = getattr(old_value, "library_MultiImage62", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage62"):
                opp_val = getattr(value, "library_MultiImage62", None)
                setattr(value, "library_MultiImage62", self)

    @property
    def library_Function89(self):
        return self.__library_Function89

    @library_Function89.setter
    def library_Function89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function89", None)
        self.__library_Function89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource90"):
                    opp_val = getattr(item, "library_NetXResource90", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource90"):
                    opp_val = getattr(item, "library_NetXResource90", None)
                    
                    setattr(item, "library_NetXResource90", self)
                    

    @property
    def library_Function143(self):
        return self.__library_Function143

    @library_Function143.setter
    def library_Function143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function143", None)
        self.__library_Function143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType142"):
                opp_val = getattr(old_value, "library_NodeType142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType142"):
                opp_val = getattr(value, "library_NodeType142", None)
                if opp_val is None:
                    setattr(value, "library_NodeType142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function91(self):
        return self.__library_Function91

    @library_Function91.setter
    def library_Function91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function91", None)
        self.__library_Function91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function93"):
                    opp_val = getattr(item, "library_Function93", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function93"):
                    opp_val = getattr(item, "library_Function93", None)
                    
                    setattr(item, "library_Function93", self)
                    

    @property
    def library_Function67(self):
        return self.__library_Function67

    @library_Function67.setter
    def library_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function67", None)
        self.__library_Function67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource68"):
                    opp_val = getattr(item, "library_NetXResource68", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource68"):
                    opp_val = getattr(item, "library_NetXResource68", None)
                    
                    setattr(item, "library_NetXResource68", self)
                    

    @property
    def library_Function80(self):
        return self.__library_Function80

    @library_Function80.setter
    def library_Function80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function80", None)
        self.__library_Function80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance81"):
                    opp_val = getattr(item, "library_Tolerance81", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance81"):
                    opp_val = getattr(item, "library_Tolerance81", None)
                    
                    setattr(item, "library_Tolerance81", self)
                    

    @property
    def library_Function77(self):
        return self.__library_Function77

    @library_Function77.setter
    def library_Function77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function77", None)
        self.__library_Function77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Expression78"):
                opp_val = getattr(old_value, "library_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "library_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Expression78"):
                opp_val = getattr(value, "library_Expression78", None)
                setattr(value, "library_Expression78", self)

    @property
    def library_Function73(self):
        return self.__library_Function73

    @library_Function73.setter
    def library_Function73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function73", None)
        self.__library_Function73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_FunctionRelationship"):
                    opp_val = getattr(item, "library_FunctionRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "library_FunctionRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_FunctionRelationship"):
                    opp_val = getattr(item, "library_FunctionRelationship", None)
                    
                    setattr(item, "library_FunctionRelationship", self)
                    

    @property
    def library_Function151(self):
        return self.__library_Function151

    @library_Function151.setter
    def library_Function151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function151", None)
        self.__library_Function151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo150"):
                opp_val = getattr(old_value, "library_ProductInfo150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo150"):
                opp_val = getattr(value, "library_ProductInfo150", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function63(self):
        return self.__library_Function63

    @library_Function63.setter
    def library_Function63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function63", None)
        self.__library_Function63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function65"):
                    opp_val = getattr(item, "library_Function65", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function65"):
                    opp_val = getattr(item, "library_Function65", None)
                    
                    setattr(item, "library_Function65", self)
                    

    @property
    def library_Function93(self):
        return self.__library_Function93

    @library_Function93.setter
    def library_Function93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function93", None)
        self.__library_Function93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function91"):
                opp_val = getattr(old_value, "library_Function91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function91"):
                opp_val = getattr(value, "library_Function91", None)
                if opp_val is None:
                    setattr(value, "library_Function91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def functionRefs(self):
        return self.__functionRefs

    @functionRefs.setter
    def functionRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__functionRefs", None)
        self.__functionRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression75"):
                    opp_val = getattr(item, "Expression75", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression75"):
                    opp_val = getattr(item, "Expression75", None)
                    
                    setattr(item, "Expression75", self)
                    

    @property
    def library_Function70(self):
        return self.__library_Function70

    @library_Function70.setter
    def library_Function70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function70", None)
        self.__library_Function70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric71"):
                    opp_val = getattr(item, "library_Metric71", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric71"):
                    opp_val = getattr(item, "library_Metric71", None)
                    
                    setattr(item, "library_Metric71", self)
                    

    @property
    def Function(self):
        return self.__Function

    @Function.setter
    def Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__Function", None)
        self.__Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functionExpressionRefs"):
                opp_val = getattr(old_value, "functionExpressionRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functionExpressionRefs"):
                opp_val = getattr(value, "functionExpressionRefs", None)
                if opp_val is None:
                    setattr(value, "functionExpressionRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function65(self):
        return self.__library_Function65

    @library_Function65.setter
    def library_Function65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function65", None)
        self.__library_Function65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function63"):
                opp_val = getattr(old_value, "library_Function63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function63"):
                opp_val = getattr(value, "library_Function63", None)
                if opp_val is None:
                    setattr(value, "library_Function63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function(self):
        return self.__library_Function

    @library_Function.setter
    def library_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function", None)
        self.__library_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo59"):
                    opp_val = getattr(item, "library_DiagramInfo59", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo59"):
                    opp_val = getattr(item, "library_DiagramInfo59", None)
                    
                    setattr(item, "library_DiagramInfo59", self)
                    

    @property
    def library_Function95(self):
        return self.__library_Function95

    @library_Function95.setter
    def library_Function95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function95", None)
        self.__library_Function95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_EObject:

    pass
class library_MultiImage:

    pass
class library_Parameter:

    def __init__(self, modifiable: str, name: str, value: str, description: str, expressionName: str, library_Parameter: "library_Equipment" = None, library_Parameter44: "library_EquipmentGroup" = None, library_Parameter87: "library_Function" = None, library_Parameter108: "library_Library" = None):
        self.modifiable = modifiable
        self.name = name
        self.value = value
        self.description = description
        self.expressionName = expressionName
        self.library_Parameter = library_Parameter
        self.library_Parameter44 = library_Parameter44
        self.library_Parameter87 = library_Parameter87
        self.library_Parameter108 = library_Parameter108
        
    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def library_Parameter87(self):
        return self.__library_Parameter87

    @library_Parameter87.setter
    def library_Parameter87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter87", None)
        self.__library_Parameter87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function86"):
                opp_val = getattr(old_value, "library_Function86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function86"):
                opp_val = getattr(value, "library_Function86", None)
                if opp_val is None:
                    setattr(value, "library_Function86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter44(self):
        return self.__library_Parameter44

    @library_Parameter44.setter
    def library_Parameter44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter44", None)
        self.__library_Parameter44 = value
        
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
    def library_Parameter(self):
        return self.__library_Parameter

    @library_Parameter.setter
    def library_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter", None)
        self.__library_Parameter = value
        
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

    @property
    def library_Parameter108(self):
        return self.__library_Parameter108

    @library_Parameter108.setter
    def library_Parameter108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter108", None)
        self.__library_Parameter108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library107"):
                opp_val = getattr(old_value, "library_Library107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library107"):
                opp_val = getattr(value, "library_Library107", None)
                if opp_val is None:
                    setattr(value, "library_Library107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Protocol:

    pass
class library_Tolerance:

    def __init__(self, expression: str, level: str, name: str, library_Tolerance: "library_Equipment" = None, library_Tolerance81: "library_Function" = None, library_Tolerance111: "library_Library" = None):
        self.expression = expression
        self.level = level
        self.name = name
        self.library_Tolerance = library_Tolerance
        self.library_Tolerance81 = library_Tolerance81
        self.library_Tolerance111 = library_Tolerance111
        
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
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def library_Tolerance111(self):
        return self.__library_Tolerance111

    @library_Tolerance111.setter
    def library_Tolerance111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance111", None)
        self.__library_Tolerance111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library110"):
                opp_val = getattr(old_value, "library_Library110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library110"):
                opp_val = getattr(value, "library_Library110", None)
                if opp_val is None:
                    setattr(value, "library_Library110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Tolerance81(self):
        return self.__library_Tolerance81

    @library_Tolerance81.setter
    def library_Tolerance81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance81", None)
        self.__library_Tolerance81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function80"):
                opp_val = getattr(old_value, "library_Function80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function80"):
                opp_val = getattr(value, "library_Function80", None)
                if opp_val is None:
                    setattr(value, "library_Function80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "library_Equipment18"):
                opp_val = getattr(old_value, "library_Equipment18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment18"):
                opp_val = getattr(value, "library_Equipment18", None)
                if opp_val is None:
                    setattr(value, "library_Equipment18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Expression:

    def __init__(self, expressionLines: str, name: str, Expression: "library_Equipment" = None, library_Expression: "library_Equipment" = None, Expression38: "library_EquipmentGroup" = None, library_Expression52: "library_EObject" = None, equipmentExpressionRefs: set["library_Equipment"] = None, functionExpressionRefs: set["library_Function"] = None, expressionRefs: set["library_EquipmentGroup"] = None, library_Expression57: set["library_ServiceProfile"] = None, Expression75: "library_Function" = None, library_Expression78: "library_Function" = None, library_Expression114: "library_Library" = None):
        self.expressionLines = expressionLines
        self.name = name
        self.Expression = Expression
        self.library_Expression = library_Expression
        self.Expression38 = Expression38
        self.library_Expression52 = library_Expression52
        self.equipmentExpressionRefs = equipmentExpressionRefs if equipmentExpressionRefs is not None else set()
        self.functionExpressionRefs = functionExpressionRefs if functionExpressionRefs is not None else set()
        self.expressionRefs = expressionRefs if expressionRefs is not None else set()
        self.library_Expression57 = library_Expression57 if library_Expression57 is not None else set()
        self.Expression75 = Expression75
        self.library_Expression78 = library_Expression78
        self.library_Expression114 = library_Expression114
        
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
    def library_Expression52(self):
        return self.__library_Expression52

    @library_Expression52.setter
    def library_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression52", None)
        self.__library_Expression52 = value
        
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
    def functionExpressionRefs(self):
        return self.__functionExpressionRefs

    @functionExpressionRefs.setter
    def functionExpressionRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__functionExpressionRefs", None)
        self.__functionExpressionRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    setattr(item, "Function", self)
                    

    @property
    def library_Expression114(self):
        return self.__library_Expression114

    @library_Expression114.setter
    def library_Expression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression114", None)
        self.__library_Expression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library113"):
                opp_val = getattr(old_value, "library_Library113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library113"):
                opp_val = getattr(value, "library_Library113", None)
                if opp_val is None:
                    setattr(value, "library_Library113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression57(self):
        return self.__library_Expression57

    @library_Expression57.setter
    def library_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression57", None)
        self.__library_Expression57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_ServiceProfile"):
                    opp_val = getattr(item, "library_ServiceProfile", None)
                    
                    if opp_val == self:
                        setattr(item, "library_ServiceProfile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_ServiceProfile"):
                    opp_val = getattr(item, "library_ServiceProfile", None)
                    
                    setattr(item, "library_ServiceProfile", self)
                    

    @property
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__Expression", None)
        self.__Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipmentRefs"):
                opp_val = getattr(old_value, "equipmentRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipmentRefs"):
                opp_val = getattr(value, "equipmentRefs", None)
                if opp_val is None:
                    setattr(value, "equipmentRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Expression38(self):
        return self.__Expression38

    @Expression38.setter
    def Expression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__Expression38", None)
        self.__Expression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipmentGroupRefs"):
                opp_val = getattr(old_value, "equipmentGroupRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipmentGroupRefs"):
                opp_val = getattr(value, "equipmentGroupRefs", None)
                if opp_val is None:
                    setattr(value, "equipmentGroupRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expressionRefs(self):
        return self.__expressionRefs

    @expressionRefs.setter
    def expressionRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__expressionRefs", None)
        self.__expressionRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquipmentGroup"):
                    opp_val = getattr(item, "EquipmentGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "EquipmentGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquipmentGroup"):
                    opp_val = getattr(item, "EquipmentGroup", None)
                    
                    setattr(item, "EquipmentGroup", self)
                    

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
            if hasattr(old_value, "library_Equipment16"):
                opp_val = getattr(old_value, "library_Equipment16", None)
                if opp_val == self:
                    setattr(old_value, "library_Equipment16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment16"):
                opp_val = getattr(value, "library_Equipment16", None)
                setattr(value, "library_Equipment16", self)

    @property
    def Expression75(self):
        return self.__Expression75

    @Expression75.setter
    def Expression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__Expression75", None)
        self.__Expression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functionRefs"):
                opp_val = getattr(old_value, "functionRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functionRefs"):
                opp_val = getattr(value, "functionRefs", None)
                if opp_val is None:
                    setattr(value, "functionRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Expression78(self):
        return self.__library_Expression78

    @library_Expression78.setter
    def library_Expression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression78", None)
        self.__library_Expression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function77"):
                opp_val = getattr(old_value, "library_Function77", None)
                if opp_val == self:
                    setattr(old_value, "library_Function77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function77"):
                opp_val = getattr(value, "library_Function77", None)
                setattr(value, "library_Function77", self)

    @property
    def equipmentExpressionRefs(self):
        return self.__equipmentExpressionRefs

    @equipmentExpressionRefs.setter
    def equipmentExpressionRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__equipmentExpressionRefs", None)
        self.__equipmentExpressionRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Equipment"):
                    opp_val = getattr(item, "Equipment", None)
                    
                    if opp_val == self:
                        setattr(item, "Equipment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Equipment"):
                    opp_val = getattr(item, "Equipment", None)
                    
                    setattr(item, "Equipment", self)
                    

class library_EquipmentRelationship:

    pass
class library_Metric:

    pass
class library_NetXResource:

    def __init__(self, detailDisplay: str, expressionName: str, longName: str, shortName: str, summaryDisplay: str, library_NetXResource: "library_Equipment" = None, library_NetXResource25: "library_Equipment" = None, library_NetXResource36: "library_EquipmentGroup" = None, library_NetXResource47: "library_EquipmentGroup" = None, library_NetXResource68: "library_Function" = None, library_NetXResource90: "library_Function" = None, library_NetXResource120: "library_Metric" = None, library_NetXResource123: set["library_MetricValueRange"] = None, library_NetXResource125: set["library_Value"] = None, library_NetXResource127: set["library_Value"] = None, library_NetXResource130: set["library_Value"] = None, library_NetXResource133: set["library_Value"] = None, library_NetXResource136: set["library_Value"] = None, library_NetXResource139: "library_Unit" = None):
        self.detailDisplay = detailDisplay
        self.expressionName = expressionName
        self.longName = longName
        self.shortName = shortName
        self.summaryDisplay = summaryDisplay
        self.library_NetXResource = library_NetXResource
        self.library_NetXResource25 = library_NetXResource25
        self.library_NetXResource36 = library_NetXResource36
        self.library_NetXResource47 = library_NetXResource47
        self.library_NetXResource68 = library_NetXResource68
        self.library_NetXResource90 = library_NetXResource90
        self.library_NetXResource120 = library_NetXResource120
        self.library_NetXResource123 = library_NetXResource123 if library_NetXResource123 is not None else set()
        self.library_NetXResource125 = library_NetXResource125 if library_NetXResource125 is not None else set()
        self.library_NetXResource127 = library_NetXResource127 if library_NetXResource127 is not None else set()
        self.library_NetXResource130 = library_NetXResource130 if library_NetXResource130 is not None else set()
        self.library_NetXResource133 = library_NetXResource133 if library_NetXResource133 is not None else set()
        self.library_NetXResource136 = library_NetXResource136 if library_NetXResource136 is not None else set()
        self.library_NetXResource139 = library_NetXResource139
        
    @property
    def longName(self) -> str:
        return self.__longName

    @longName.setter
    def longName(self, longName: str):
        self.__longName = longName

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
    def summaryDisplay(self) -> str:
        return self.__summaryDisplay

    @summaryDisplay.setter
    def summaryDisplay(self, summaryDisplay: str):
        self.__summaryDisplay = summaryDisplay

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def library_NetXResource136(self):
        return self.__library_NetXResource136

    @library_NetXResource136.setter
    def library_NetXResource136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource136", None)
        self.__library_NetXResource136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value137"):
                    opp_val = getattr(item, "library_Value137", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value137"):
                    opp_val = getattr(item, "library_Value137", None)
                    
                    setattr(item, "library_Value137", self)
                    

    @property
    def library_NetXResource130(self):
        return self.__library_NetXResource130

    @library_NetXResource130.setter
    def library_NetXResource130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource130", None)
        self.__library_NetXResource130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value131"):
                    opp_val = getattr(item, "library_Value131", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value131"):
                    opp_val = getattr(item, "library_Value131", None)
                    
                    setattr(item, "library_Value131", self)
                    

    @property
    def library_NetXResource120(self):
        return self.__library_NetXResource120

    @library_NetXResource120.setter
    def library_NetXResource120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource120", None)
        self.__library_NetXResource120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Metric121"):
                opp_val = getattr(old_value, "library_Metric121", None)
                if opp_val == self:
                    setattr(old_value, "library_Metric121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Metric121"):
                opp_val = getattr(value, "library_Metric121", None)
                setattr(value, "library_Metric121", self)

    @property
    def library_NetXResource68(self):
        return self.__library_NetXResource68

    @library_NetXResource68.setter
    def library_NetXResource68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource68", None)
        self.__library_NetXResource68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function67"):
                opp_val = getattr(old_value, "library_Function67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function67"):
                opp_val = getattr(value, "library_Function67", None)
                if opp_val is None:
                    setattr(value, "library_Function67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource133(self):
        return self.__library_NetXResource133

    @library_NetXResource133.setter
    def library_NetXResource133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource133", None)
        self.__library_NetXResource133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value134"):
                    opp_val = getattr(item, "library_Value134", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value134"):
                    opp_val = getattr(item, "library_Value134", None)
                    
                    setattr(item, "library_Value134", self)
                    

    @property
    def library_NetXResource139(self):
        return self.__library_NetXResource139

    @library_NetXResource139.setter
    def library_NetXResource139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource139", None)
        self.__library_NetXResource139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Unit140"):
                opp_val = getattr(old_value, "library_Unit140", None)
                if opp_val == self:
                    setattr(old_value, "library_Unit140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Unit140"):
                opp_val = getattr(value, "library_Unit140", None)
                setattr(value, "library_Unit140", self)

    @property
    def library_NetXResource36(self):
        return self.__library_NetXResource36

    @library_NetXResource36.setter
    def library_NetXResource36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource36", None)
        self.__library_NetXResource36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup35"):
                opp_val = getattr(old_value, "library_EquipmentGroup35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup35"):
                opp_val = getattr(value, "library_EquipmentGroup35", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource25(self):
        return self.__library_NetXResource25

    @library_NetXResource25.setter
    def library_NetXResource25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource25", None)
        self.__library_NetXResource25 = value
        
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
    def library_NetXResource127(self):
        return self.__library_NetXResource127

    @library_NetXResource127.setter
    def library_NetXResource127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource127", None)
        self.__library_NetXResource127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value128"):
                    opp_val = getattr(item, "library_Value128", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value128"):
                    opp_val = getattr(item, "library_Value128", None)
                    
                    setattr(item, "library_Value128", self)
                    

    @property
    def library_NetXResource(self):
        return self.__library_NetXResource

    @library_NetXResource.setter
    def library_NetXResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource", None)
        self.__library_NetXResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment9"):
                opp_val = getattr(old_value, "library_Equipment9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment9"):
                opp_val = getattr(value, "library_Equipment9", None)
                if opp_val is None:
                    setattr(value, "library_Equipment9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource47(self):
        return self.__library_NetXResource47

    @library_NetXResource47.setter
    def library_NetXResource47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource47", None)
        self.__library_NetXResource47 = value
        
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

    @property
    def library_NetXResource90(self):
        return self.__library_NetXResource90

    @library_NetXResource90.setter
    def library_NetXResource90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource90", None)
        self.__library_NetXResource90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function89"):
                opp_val = getattr(old_value, "library_Function89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function89"):
                opp_val = getattr(value, "library_Function89", None)
                if opp_val is None:
                    setattr(value, "library_Function89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource125(self):
        return self.__library_NetXResource125

    @library_NetXResource125.setter
    def library_NetXResource125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource125", None)
        self.__library_NetXResource125 = value if value is not None else set()
        
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
                    

    @property
    def library_NetXResource123(self):
        return self.__library_NetXResource123

    @library_NetXResource123.setter
    def library_NetXResource123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource123", None)
        self.__library_NetXResource123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_MetricValueRange"):
                    opp_val = getattr(item, "library_MetricValueRange", None)
                    
                    if opp_val == self:
                        setattr(item, "library_MetricValueRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_MetricValueRange"):
                    opp_val = getattr(item, "library_MetricValueRange", None)
                    
                    setattr(item, "library_MetricValueRange", self)
                    

class library_EquipmentGroup:

    def __init__(self, count: str, description: str, name: str, library_EquipmentGroup: "library_Equipment" = None, library_EquipmentGroup32: set["library_DiagramInfo"] = None, library_EquipmentGroup35: set["library_NetXResource"] = None, library_EquipmentGroup49: set["library_Equipment"] = None, equipmentGroupRefs: set["library_Expression"] = None, library_EquipmentGroup40: set["library_Equipment"] = None, library_EquipmentGroup43: set["library_Parameter"] = None, library_EquipmentGroup46: set["library_NetXResource"] = None, EquipmentGroup: "library_Expression" = None):
        self.count = count
        self.description = description
        self.name = name
        self.library_EquipmentGroup = library_EquipmentGroup
        self.library_EquipmentGroup32 = library_EquipmentGroup32 if library_EquipmentGroup32 is not None else set()
        self.library_EquipmentGroup35 = library_EquipmentGroup35 if library_EquipmentGroup35 is not None else set()
        self.library_EquipmentGroup49 = library_EquipmentGroup49 if library_EquipmentGroup49 is not None else set()
        self.equipmentGroupRefs = equipmentGroupRefs if equipmentGroupRefs is not None else set()
        self.library_EquipmentGroup40 = library_EquipmentGroup40 if library_EquipmentGroup40 is not None else set()
        self.library_EquipmentGroup43 = library_EquipmentGroup43 if library_EquipmentGroup43 is not None else set()
        self.library_EquipmentGroup46 = library_EquipmentGroup46 if library_EquipmentGroup46 is not None else set()
        self.EquipmentGroup = EquipmentGroup
        
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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
                if hasattr(item, "library_NetXResource47"):
                    opp_val = getattr(item, "library_NetXResource47", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource47"):
                    opp_val = getattr(item, "library_NetXResource47", None)
                    
                    setattr(item, "library_NetXResource47", self)
                    

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
                if hasattr(item, "library_Equipment41"):
                    opp_val = getattr(item, "library_Equipment41", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment41"):
                    opp_val = getattr(item, "library_Equipment41", None)
                    
                    setattr(item, "library_Equipment41", self)
                    

    @property
    def EquipmentGroup(self):
        return self.__EquipmentGroup

    @EquipmentGroup.setter
    def EquipmentGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__EquipmentGroup", None)
        self.__EquipmentGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionRefs"):
                opp_val = getattr(old_value, "expressionRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionRefs"):
                opp_val = getattr(value, "expressionRefs", None)
                if opp_val is None:
                    setattr(value, "expressionRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "library_Equipment50"):
                    opp_val = getattr(item, "library_Equipment50", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment50"):
                    opp_val = getattr(item, "library_Equipment50", None)
                    
                    setattr(item, "library_Equipment50", self)
                    

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
                if hasattr(item, "library_Parameter44"):
                    opp_val = getattr(item, "library_Parameter44", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter44"):
                    opp_val = getattr(item, "library_Parameter44", None)
                    
                    setattr(item, "library_Parameter44", self)
                    

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
            if hasattr(old_value, "library_Equipment7"):
                opp_val = getattr(old_value, "library_Equipment7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment7"):
                opp_val = getattr(value, "library_Equipment7", None)
                if opp_val is None:
                    setattr(value, "library_Equipment7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def equipmentGroupRefs(self):
        return self.__equipmentGroupRefs

    @equipmentGroupRefs.setter
    def equipmentGroupRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__equipmentGroupRefs", None)
        self.__equipmentGroupRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression38"):
                    opp_val = getattr(item, "Expression38", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression38"):
                    opp_val = getattr(item, "Expression38", None)
                    
                    setattr(item, "Expression38", self)
                    

class library_DiagramInfo:

    pass
class library_Lifecycle:

    pass
class library_Equipment:

    def __init__(self, count: str, description: str, equipmentCode: str, equipmentName: str, position: str, redundancy: str, state: str, library_Equipment: "library_Lifecycle" = None, library_Equipment2: set["library_DiagramInfo"] = None, library_Equipment5: "library_Equipment" = None, library_Equipment3: set["library_Equipment"] = None, library_Equipment7: set["library_EquipmentGroup"] = None, library_Equipment9: set["library_NetXResource"] = None, library_Equipment11: set["library_Metric"] = None, library_Equipment13: set["library_EquipmentRelationship"] = None, equipmentRefs: set["library_Expression"] = None, library_Equipment16: "library_Expression" = None, library_Equipment18: set["library_Tolerance"] = None, library_Equipment20: set["library_Protocol"] = None, library_Equipment22: set["library_Parameter"] = None, library_Equipment24: set["library_NetXResource"] = None, library_Equipment28: "library_Equipment" = None, library_Equipment26: set["library_Equipment"] = None, library_Equipment30: "library_MultiImage" = None, library_Equipment50: "library_EquipmentGroup" = None, library_Equipment41: "library_EquipmentGroup" = None, Equipment: "library_Expression" = None, library_Equipment100: "library_Library" = None, library_Equipment146: "library_NodeType" = None, library_Equipment148: "library_ProductInfo" = None):
        self.count = count
        self.description = description
        self.equipmentCode = equipmentCode
        self.equipmentName = equipmentName
        self.position = position
        self.redundancy = redundancy
        self.state = state
        self.library_Equipment = library_Equipment
        self.library_Equipment2 = library_Equipment2 if library_Equipment2 is not None else set()
        self.library_Equipment5 = library_Equipment5
        self.library_Equipment3 = library_Equipment3 if library_Equipment3 is not None else set()
        self.library_Equipment7 = library_Equipment7 if library_Equipment7 is not None else set()
        self.library_Equipment9 = library_Equipment9 if library_Equipment9 is not None else set()
        self.library_Equipment11 = library_Equipment11 if library_Equipment11 is not None else set()
        self.library_Equipment13 = library_Equipment13 if library_Equipment13 is not None else set()
        self.equipmentRefs = equipmentRefs if equipmentRefs is not None else set()
        self.library_Equipment16 = library_Equipment16
        self.library_Equipment18 = library_Equipment18 if library_Equipment18 is not None else set()
        self.library_Equipment20 = library_Equipment20 if library_Equipment20 is not None else set()
        self.library_Equipment22 = library_Equipment22 if library_Equipment22 is not None else set()
        self.library_Equipment24 = library_Equipment24 if library_Equipment24 is not None else set()
        self.library_Equipment28 = library_Equipment28
        self.library_Equipment26 = library_Equipment26 if library_Equipment26 is not None else set()
        self.library_Equipment30 = library_Equipment30
        self.library_Equipment50 = library_Equipment50
        self.library_Equipment41 = library_Equipment41
        self.Equipment = Equipment
        self.library_Equipment100 = library_Equipment100
        self.library_Equipment146 = library_Equipment146
        self.library_Equipment148 = library_Equipment148
        
    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

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
    def equipmentName(self) -> str:
        return self.__equipmentName

    @equipmentName.setter
    def equipmentName(self, equipmentName: str):
        self.__equipmentName = equipmentName

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def library_Equipment148(self):
        return self.__library_Equipment148

    @library_Equipment148.setter
    def library_Equipment148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment148", None)
        self.__library_Equipment148 = value
        
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
    def library_Equipment3(self):
        return self.__library_Equipment3

    @library_Equipment3.setter
    def library_Equipment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment3", None)
        self.__library_Equipment3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment5"):
                    opp_val = getattr(item, "library_Equipment5", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment5"):
                    opp_val = getattr(item, "library_Equipment5", None)
                    
                    setattr(item, "library_Equipment5", self)
                    

    @property
    def library_Equipment16(self):
        return self.__library_Equipment16

    @library_Equipment16.setter
    def library_Equipment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment16", None)
        self.__library_Equipment16 = value
        
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
    def Equipment(self):
        return self.__Equipment

    @Equipment.setter
    def Equipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__Equipment", None)
        self.__Equipment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipmentExpressionRefs"):
                opp_val = getattr(old_value, "equipmentExpressionRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipmentExpressionRefs"):
                opp_val = getattr(value, "equipmentExpressionRefs", None)
                if opp_val is None:
                    setattr(value, "equipmentExpressionRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment7(self):
        return self.__library_Equipment7

    @library_Equipment7.setter
    def library_Equipment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment7", None)
        self.__library_Equipment7 = value if value is not None else set()
        
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
    def library_Equipment11(self):
        return self.__library_Equipment11

    @library_Equipment11.setter
    def library_Equipment11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment11", None)
        self.__library_Equipment11 = value if value is not None else set()
        
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
    def library_Equipment41(self):
        return self.__library_Equipment41

    @library_Equipment41.setter
    def library_Equipment41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment41", None)
        self.__library_Equipment41 = value
        
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
    def library_Equipment50(self):
        return self.__library_Equipment50

    @library_Equipment50.setter
    def library_Equipment50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment50", None)
        self.__library_Equipment50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup49"):
                opp_val = getattr(old_value, "library_EquipmentGroup49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup49"):
                opp_val = getattr(value, "library_EquipmentGroup49", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment20(self):
        return self.__library_Equipment20

    @library_Equipment20.setter
    def library_Equipment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment20", None)
        self.__library_Equipment20 = value if value is not None else set()
        
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
    def library_Equipment100(self):
        return self.__library_Equipment100

    @library_Equipment100.setter
    def library_Equipment100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment100", None)
        self.__library_Equipment100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library99"):
                opp_val = getattr(old_value, "library_Library99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library99"):
                opp_val = getattr(value, "library_Library99", None)
                if opp_val is None:
                    setattr(value, "library_Library99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment9(self):
        return self.__library_Equipment9

    @library_Equipment9.setter
    def library_Equipment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment9", None)
        self.__library_Equipment9 = value if value is not None else set()
        
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
    def library_Equipment(self):
        return self.__library_Equipment

    @library_Equipment.setter
    def library_Equipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment", None)
        self.__library_Equipment = value
        
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
                if hasattr(item, "library_NetXResource25"):
                    opp_val = getattr(item, "library_NetXResource25", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource25"):
                    opp_val = getattr(item, "library_NetXResource25", None)
                    
                    setattr(item, "library_NetXResource25", self)
                    

    @property
    def library_Equipment2(self):
        return self.__library_Equipment2

    @library_Equipment2.setter
    def library_Equipment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment2", None)
        self.__library_Equipment2 = value if value is not None else set()
        
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
    def equipmentRefs(self):
        return self.__equipmentRefs

    @equipmentRefs.setter
    def equipmentRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__equipmentRefs", None)
        self.__equipmentRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    setattr(item, "Expression", self)
                    

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
    def library_Equipment28(self):
        return self.__library_Equipment28

    @library_Equipment28.setter
    def library_Equipment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment28", None)
        self.__library_Equipment28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment26"):
                opp_val = getattr(old_value, "library_Equipment26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment26"):
                opp_val = getattr(value, "library_Equipment26", None)
                if opp_val is None:
                    setattr(value, "library_Equipment26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment5(self):
        return self.__library_Equipment5

    @library_Equipment5.setter
    def library_Equipment5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment5", None)
        self.__library_Equipment5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment3"):
                opp_val = getattr(old_value, "library_Equipment3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment3"):
                opp_val = getattr(value, "library_Equipment3", None)
                if opp_val is None:
                    setattr(value, "library_Equipment3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment26(self):
        return self.__library_Equipment26

    @library_Equipment26.setter
    def library_Equipment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment26", None)
        self.__library_Equipment26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment28"):
                    opp_val = getattr(item, "library_Equipment28", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment28"):
                    opp_val = getattr(item, "library_Equipment28", None)
                    
                    setattr(item, "library_Equipment28", self)
                    

    @property
    def library_Equipment18(self):
        return self.__library_Equipment18

    @library_Equipment18.setter
    def library_Equipment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment18", None)
        self.__library_Equipment18 = value if value is not None else set()
        
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
    def library_Equipment30(self):
        return self.__library_Equipment30

    @library_Equipment30.setter
    def library_Equipment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment30", None)
        self.__library_Equipment30 = value
        
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
    def library_Equipment146(self):
        return self.__library_Equipment146

    @library_Equipment146.setter
    def library_Equipment146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment146", None)
        self.__library_Equipment146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType145"):
                opp_val = getattr(old_value, "library_NodeType145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType145"):
                opp_val = getattr(value, "library_NodeType145", None)
                if opp_val is None:
                    setattr(value, "library_NodeType145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment13(self):
        return self.__library_Equipment13

    @library_Equipment13.setter
    def library_Equipment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment13", None)
        self.__library_Equipment13 = value if value is not None else set()
        
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
                    
