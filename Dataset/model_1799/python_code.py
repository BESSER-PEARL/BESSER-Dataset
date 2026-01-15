from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OSIType(Enum):
    Application = "Application"
    Presentation = "Presentation"
    Session = "Session"
    Transport = "Transport"
    Network = "Network"
    DataLink = "DataLink"
    Physiscal = "Physiscal"
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
class RedundancyType(Enum):
    n = "n"
    n1 = "n1"
    _11 = "_11"


############################################
# Definition of Classes
############################################

class Company:

    pass
class library_Vendor(Company):

    pass
class library_Company:

    pass
class library_ProductInfo:

    def __init__(self, availableDate: str, endOfSalesDate: str, endOfSupportDate: str, productCode: str, salesCode: str, underDevelopmentDate: str, library_ProductInfo138: set["library_Function"] = None, library_ProductInfo141: set["library_NodeType"] = None, library_ProductInfo: set["library_Equipment"] = None, library_ProductInfo152: "library_Vendor" = None):
        self.availableDate = availableDate
        self.endOfSalesDate = endOfSalesDate
        self.endOfSupportDate = endOfSupportDate
        self.productCode = productCode
        self.salesCode = salesCode
        self.underDevelopmentDate = underDevelopmentDate
        self.library_ProductInfo138 = library_ProductInfo138 if library_ProductInfo138 is not None else set()
        self.library_ProductInfo141 = library_ProductInfo141 if library_ProductInfo141 is not None else set()
        self.library_ProductInfo = library_ProductInfo if library_ProductInfo is not None else set()
        self.library_ProductInfo152 = library_ProductInfo152
        
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
    def library_ProductInfo138(self):
        return self.__library_ProductInfo138

    @library_ProductInfo138.setter
    def library_ProductInfo138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo138", None)
        self.__library_ProductInfo138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function139"):
                    opp_val = getattr(item, "library_Function139", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function139"):
                    opp_val = getattr(item, "library_Function139", None)
                    
                    setattr(item, "library_Function139", self)
                    

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
                if hasattr(item, "library_Equipment136"):
                    opp_val = getattr(item, "library_Equipment136", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment136"):
                    opp_val = getattr(item, "library_Equipment136", None)
                    
                    setattr(item, "library_Equipment136", self)
                    

    @property
    def library_ProductInfo152(self):
        return self.__library_ProductInfo152

    @library_ProductInfo152.setter
    def library_ProductInfo152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo152", None)
        self.__library_ProductInfo152 = value
        
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
    def library_ProductInfo141(self):
        return self.__library_ProductInfo141

    @library_ProductInfo141.setter
    def library_ProductInfo141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_ProductInfo__library_ProductInfo141", None)
        self.__library_ProductInfo141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NodeType142"):
                    opp_val = getattr(item, "library_NodeType142", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NodeType142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NodeType142"):
                    opp_val = getattr(item, "library_NodeType142", None)
                    
                    setattr(item, "library_NodeType142", self)
                    

class library_Procedure:

    def __init__(self, name: str, library_Procedure: set["library_Message"] = None, library_Procedure145: "library_Protocol" = None):
        self.name = name
        self.library_Procedure = library_Procedure if library_Procedure is not None else set()
        self.library_Procedure145 = library_Procedure145
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Procedure145(self):
        return self.__library_Procedure145

    @library_Procedure145.setter
    def library_Procedure145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Procedure__library_Procedure145", None)
        self.__library_Procedure145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Protocol144"):
                opp_val = getattr(old_value, "library_Protocol144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Protocol144"):
                opp_val = getattr(value, "library_Protocol144", None)
                if opp_val is None:
                    setattr(value, "library_Protocol144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Procedure(self):
        return self.__library_Procedure

    @library_Procedure.setter
    def library_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Procedure__library_Procedure", None)
        self.__library_Procedure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Message"):
                    opp_val = getattr(item, "library_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Message"):
                    opp_val = getattr(item, "library_Message", None)
                    
                    setattr(item, "library_Message", self)
                    

class library_Value:

    pass
class library_MetricValueRange:

    pass
class library_Meta:

    def __init__(self, author: str, description: str, version: str, library_Meta: "library_Library" = None):
        self.author = author
        self.description = description
        self.version = version
        self.library_Meta = library_Meta
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def library_Meta(self):
        return self.__library_Meta

    @library_Meta.setter
    def library_Meta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Meta__library_Meta", None)
        self.__library_Meta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library111"):
                opp_val = getattr(old_value, "library_Library111", None)
                if opp_val == self:
                    setattr(old_value, "library_Library111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library111"):
                opp_val = getattr(value, "library_Library111", None)
                setattr(value, "library_Library111", self)

class library_Message:

    def __init__(self, name: str, library_Message: "library_Procedure" = None):
        self.name = name
        self.library_Message = library_Message
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Message(self):
        return self.__library_Message

    @library_Message.setter
    def library_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Message__library_Message", None)
        self.__library_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Procedure"):
                opp_val = getattr(old_value, "library_Procedure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Procedure"):
                opp_val = getattr(value, "library_Procedure", None)
                if opp_val is None:
                    setattr(value, "library_Procedure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Unit:

    def __init__(self, code: str, description: str, name: str, library_Unit: "library_Library" = None, library_Unit127: "library_NetXResource" = None, library_Unit149: "library_MultiImage" = None):
        self.code = code
        self.description = description
        self.name = name
        self.library_Unit = library_Unit
        self.library_Unit127 = library_Unit127
        self.library_Unit149 = library_Unit149
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def library_Unit(self):
        return self.__library_Unit

    @library_Unit.setter
    def library_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit", None)
        self.__library_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library109"):
                opp_val = getattr(old_value, "library_Library109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library109"):
                opp_val = getattr(value, "library_Library109", None)
                if opp_val is None:
                    setattr(value, "library_Library109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Unit149(self):
        return self.__library_Unit149

    @library_Unit149.setter
    def library_Unit149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit149", None)
        self.__library_Unit149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage150"):
                opp_val = getattr(old_value, "library_MultiImage150", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage150"):
                opp_val = getattr(value, "library_MultiImage150", None)
                setattr(value, "library_MultiImage150", self)

    @property
    def library_Unit127(self):
        return self.__library_Unit127

    @library_Unit127.setter
    def library_Unit127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Unit__library_Unit127", None)
        self.__library_Unit127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NetXResource126"):
                opp_val = getattr(old_value, "library_NetXResource126", None)
                if opp_val == self:
                    setattr(old_value, "library_NetXResource126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NetXResource126"):
                opp_val = getattr(value, "library_NetXResource126", None)
                setattr(value, "library_NetXResource126", self)

class library_Library:

    def __init__(self, name: str, library_Library89: set["library_NodeType"] = None, library_Library91: set["library_Equipment"] = None, library_Library94: set["library_Metric"] = None, library_Library: set["library_Function"] = None, library_Library103: set["library_Tolerance"] = None, library_Library106: set["library_Expression"] = None, library_Library109: set["library_Unit"] = None, library_Library97: set["library_Parameter"] = None, library_Library100: set["library_Protocol"] = None, library_Library111: "library_Meta" = None):
        self.name = name
        self.library_Library89 = library_Library89 if library_Library89 is not None else set()
        self.library_Library91 = library_Library91 if library_Library91 is not None else set()
        self.library_Library94 = library_Library94 if library_Library94 is not None else set()
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library103 = library_Library103 if library_Library103 is not None else set()
        self.library_Library106 = library_Library106 if library_Library106 is not None else set()
        self.library_Library109 = library_Library109 if library_Library109 is not None else set()
        self.library_Library97 = library_Library97 if library_Library97 is not None else set()
        self.library_Library100 = library_Library100 if library_Library100 is not None else set()
        self.library_Library111 = library_Library111
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library106(self):
        return self.__library_Library106

    @library_Library106.setter
    def library_Library106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library106", None)
        self.__library_Library106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Expression107"):
                    opp_val = getattr(item, "library_Expression107", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Expression107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Expression107"):
                    opp_val = getattr(item, "library_Expression107", None)
                    
                    setattr(item, "library_Expression107", self)
                    

    @property
    def library_Library109(self):
        return self.__library_Library109

    @library_Library109.setter
    def library_Library109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library109", None)
        self.__library_Library109 = value if value is not None else set()
        
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
                if hasattr(item, "library_Function87"):
                    opp_val = getattr(item, "library_Function87", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function87"):
                    opp_val = getattr(item, "library_Function87", None)
                    
                    setattr(item, "library_Function87", self)
                    

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
                if hasattr(item, "library_Parameter98"):
                    opp_val = getattr(item, "library_Parameter98", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter98"):
                    opp_val = getattr(item, "library_Parameter98", None)
                    
                    setattr(item, "library_Parameter98", self)
                    

    @property
    def library_Library103(self):
        return self.__library_Library103

    @library_Library103.setter
    def library_Library103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library103", None)
        self.__library_Library103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance104"):
                    opp_val = getattr(item, "library_Tolerance104", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance104"):
                    opp_val = getattr(item, "library_Tolerance104", None)
                    
                    setattr(item, "library_Tolerance104", self)
                    

    @property
    def library_Library100(self):
        return self.__library_Library100

    @library_Library100.setter
    def library_Library100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library100", None)
        self.__library_Library100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Protocol101"):
                    opp_val = getattr(item, "library_Protocol101", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Protocol101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Protocol101"):
                    opp_val = getattr(item, "library_Protocol101", None)
                    
                    setattr(item, "library_Protocol101", self)
                    

    @property
    def library_Library94(self):
        return self.__library_Library94

    @library_Library94.setter
    def library_Library94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library94", None)
        self.__library_Library94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric95"):
                    opp_val = getattr(item, "library_Metric95", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric95"):
                    opp_val = getattr(item, "library_Metric95", None)
                    
                    setattr(item, "library_Metric95", self)
                    

    @property
    def library_Library111(self):
        return self.__library_Library111

    @library_Library111.setter
    def library_Library111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library111", None)
        self.__library_Library111 = value
        
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
    def library_Library91(self):
        return self.__library_Library91

    @library_Library91.setter
    def library_Library91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library91", None)
        self.__library_Library91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Equipment92"):
                    opp_val = getattr(item, "library_Equipment92", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment92"):
                    opp_val = getattr(item, "library_Equipment92", None)
                    
                    setattr(item, "library_Equipment92", self)
                    

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
                    

class library_NodeType:

    pass
class library_FunctionRelationship:

    pass
class library_ServiceProfile:

    pass
class library_Function:

    def __init__(self, description: str, functionName: str, Function: "library_Expression" = None, library_Function: set["library_DiagramInfo"] = None, library_Function56: "library_MultiImage" = None, library_Function72: set["library_Tolerance"] = None, library_Function60: "library_Function" = None, library_Function58: set["library_Function"] = None, library_Function62: set["library_NetXResource"] = None, library_Function65: set["library_Metric"] = None, library_Function68: set["library_FunctionRelationship"] = None, functionRefs: set["library_Expression"] = None, library_Function75: set["library_Protocol"] = None, library_Function78: set["library_Parameter"] = None, library_Function81: set["library_NetXResource"] = None, library_Function85: "library_Function" = None, library_Function83: set["library_Function"] = None, library_Function87: "library_Library" = None, library_Function130: "library_NodeType" = None, library_Function139: "library_ProductInfo" = None):
        self.description = description
        self.functionName = functionName
        self.Function = Function
        self.library_Function = library_Function if library_Function is not None else set()
        self.library_Function56 = library_Function56
        self.library_Function72 = library_Function72 if library_Function72 is not None else set()
        self.library_Function60 = library_Function60
        self.library_Function58 = library_Function58 if library_Function58 is not None else set()
        self.library_Function62 = library_Function62 if library_Function62 is not None else set()
        self.library_Function65 = library_Function65 if library_Function65 is not None else set()
        self.library_Function68 = library_Function68 if library_Function68 is not None else set()
        self.functionRefs = functionRefs if functionRefs is not None else set()
        self.library_Function75 = library_Function75 if library_Function75 is not None else set()
        self.library_Function78 = library_Function78 if library_Function78 is not None else set()
        self.library_Function81 = library_Function81 if library_Function81 is not None else set()
        self.library_Function85 = library_Function85
        self.library_Function83 = library_Function83 if library_Function83 is not None else set()
        self.library_Function87 = library_Function87
        self.library_Function130 = library_Function130
        self.library_Function139 = library_Function139
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def library_Function87(self):
        return self.__library_Function87

    @library_Function87.setter
    def library_Function87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function87", None)
        self.__library_Function87 = value
        
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

    @property
    def library_Function78(self):
        return self.__library_Function78

    @library_Function78.setter
    def library_Function78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function78", None)
        self.__library_Function78 = value if value is not None else set()
        
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
    def library_Function139(self):
        return self.__library_Function139

    @library_Function139.setter
    def library_Function139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function139", None)
        self.__library_Function139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_ProductInfo138"):
                opp_val = getattr(old_value, "library_ProductInfo138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_ProductInfo138"):
                opp_val = getattr(value, "library_ProductInfo138", None)
                if opp_val is None:
                    setattr(value, "library_ProductInfo138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function72(self):
        return self.__library_Function72

    @library_Function72.setter
    def library_Function72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function72", None)
        self.__library_Function72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Tolerance73"):
                    opp_val = getattr(item, "library_Tolerance73", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Tolerance73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Tolerance73"):
                    opp_val = getattr(item, "library_Tolerance73", None)
                    
                    setattr(item, "library_Tolerance73", self)
                    

    @property
    def library_Function60(self):
        return self.__library_Function60

    @library_Function60.setter
    def library_Function60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function60", None)
        self.__library_Function60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function58"):
                opp_val = getattr(old_value, "library_Function58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function58"):
                opp_val = getattr(value, "library_Function58", None)
                if opp_val is None:
                    setattr(value, "library_Function58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function68(self):
        return self.__library_Function68

    @library_Function68.setter
    def library_Function68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function68", None)
        self.__library_Function68 = value if value is not None else set()
        
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
    def library_Function75(self):
        return self.__library_Function75

    @library_Function75.setter
    def library_Function75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function75", None)
        self.__library_Function75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Protocol76"):
                    opp_val = getattr(item, "library_Protocol76", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Protocol76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Protocol76"):
                    opp_val = getattr(item, "library_Protocol76", None)
                    
                    setattr(item, "library_Protocol76", self)
                    

    @property
    def library_Function62(self):
        return self.__library_Function62

    @library_Function62.setter
    def library_Function62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function62", None)
        self.__library_Function62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource63"):
                    opp_val = getattr(item, "library_NetXResource63", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource63"):
                    opp_val = getattr(item, "library_NetXResource63", None)
                    
                    setattr(item, "library_NetXResource63", self)
                    

    @property
    def library_Function85(self):
        return self.__library_Function85

    @library_Function85.setter
    def library_Function85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function85", None)
        self.__library_Function85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function83"):
                opp_val = getattr(old_value, "library_Function83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function83"):
                opp_val = getattr(value, "library_Function83", None)
                if opp_val is None:
                    setattr(value, "library_Function83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function130(self):
        return self.__library_Function130

    @library_Function130.setter
    def library_Function130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function130", None)
        self.__library_Function130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType129"):
                opp_val = getattr(old_value, "library_NodeType129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType129"):
                opp_val = getattr(value, "library_NodeType129", None)
                if opp_val is None:
                    setattr(value, "library_NodeType129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Function81(self):
        return self.__library_Function81

    @library_Function81.setter
    def library_Function81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function81", None)
        self.__library_Function81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource82"):
                    opp_val = getattr(item, "library_NetXResource82", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource82"):
                    opp_val = getattr(item, "library_NetXResource82", None)
                    
                    setattr(item, "library_NetXResource82", self)
                    

    @property
    def library_Function56(self):
        return self.__library_Function56

    @library_Function56.setter
    def library_Function56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function56", None)
        self.__library_Function56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_MultiImage57"):
                opp_val = getattr(old_value, "library_MultiImage57", None)
                if opp_val == self:
                    setattr(old_value, "library_MultiImage57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_MultiImage57"):
                opp_val = getattr(value, "library_MultiImage57", None)
                setattr(value, "library_MultiImage57", self)

    @property
    def library_Function58(self):
        return self.__library_Function58

    @library_Function58.setter
    def library_Function58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function58", None)
        self.__library_Function58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Function60"):
                    opp_val = getattr(item, "library_Function60", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function60"):
                    opp_val = getattr(item, "library_Function60", None)
                    
                    setattr(item, "library_Function60", self)
                    

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
                if hasattr(item, "library_Function85"):
                    opp_val = getattr(item, "library_Function85", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Function85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Function85"):
                    opp_val = getattr(item, "library_Function85", None)
                    
                    setattr(item, "library_Function85", self)
                    

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
                if hasattr(item, "library_DiagramInfo54"):
                    opp_val = getattr(item, "library_DiagramInfo54", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo54"):
                    opp_val = getattr(item, "library_DiagramInfo54", None)
                    
                    setattr(item, "library_DiagramInfo54", self)
                    

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
                if hasattr(item, "Expression70"):
                    opp_val = getattr(item, "Expression70", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression70"):
                    opp_val = getattr(item, "Expression70", None)
                    
                    setattr(item, "Expression70", self)
                    

    @property
    def library_Function65(self):
        return self.__library_Function65

    @library_Function65.setter
    def library_Function65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Function__library_Function65", None)
        self.__library_Function65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metric66"):
                    opp_val = getattr(item, "library_Metric66", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metric66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metric66"):
                    opp_val = getattr(item, "library_Metric66", None)
                    
                    setattr(item, "library_Metric66", self)
                    

class library_MultiImage:

    pass
class library_Parameter:

    def __init__(self, description: str, value: str, expressionName: str, modifiable: str, name: str, library_Parameter: "library_Equipment" = None, library_Parameter42: "library_EquipmentGroup" = None, library_Parameter79: "library_Function" = None, library_Parameter98: "library_Library" = None):
        self.description = description
        self.value = value
        self.expressionName = expressionName
        self.modifiable = modifiable
        self.name = name
        self.library_Parameter = library_Parameter
        self.library_Parameter42 = library_Parameter42
        self.library_Parameter79 = library_Parameter79
        self.library_Parameter98 = library_Parameter98
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def expressionName(self) -> str:
        return self.__expressionName

    @expressionName.setter
    def expressionName(self, expressionName: str):
        self.__expressionName = expressionName

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
            if hasattr(old_value, "library_Function78"):
                opp_val = getattr(old_value, "library_Function78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function78"):
                opp_val = getattr(value, "library_Function78", None)
                if opp_val is None:
                    setattr(value, "library_Function78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Parameter98(self):
        return self.__library_Parameter98

    @library_Parameter98.setter
    def library_Parameter98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter98", None)
        self.__library_Parameter98 = value
        
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
    def library_Parameter42(self):
        return self.__library_Parameter42

    @library_Parameter42.setter
    def library_Parameter42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter42", None)
        self.__library_Parameter42 = value
        
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
    def library_Parameter(self):
        return self.__library_Parameter

    @library_Parameter.setter
    def library_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Parameter__library_Parameter", None)
        self.__library_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Equipment20"):
                opp_val = getattr(old_value, "library_Equipment20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment20"):
                opp_val = getattr(value, "library_Equipment20", None)
                if opp_val is None:
                    setattr(value, "library_Equipment20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Protocol:

    def __init__(self, name: str, oSI: str, specification: str, description: str, library_Protocol: "library_Equipment" = None, library_Protocol76: "library_Function" = None, library_Protocol101: "library_Library" = None, library_Protocol144: set["library_Procedure"] = None, library_Protocol147: "library_Company" = None):
        self.name = name
        self.oSI = oSI
        self.specification = specification
        self.description = description
        self.library_Protocol = library_Protocol
        self.library_Protocol76 = library_Protocol76
        self.library_Protocol101 = library_Protocol101
        self.library_Protocol144 = library_Protocol144 if library_Protocol144 is not None else set()
        self.library_Protocol147 = library_Protocol147
        
    @property
    def oSI(self) -> str:
        return self.__oSI

    @oSI.setter
    def oSI(self, oSI: str):
        self.__oSI = oSI

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

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
    def library_Protocol(self):
        return self.__library_Protocol

    @library_Protocol.setter
    def library_Protocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Protocol__library_Protocol", None)
        self.__library_Protocol = value
        
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

    @property
    def library_Protocol147(self):
        return self.__library_Protocol147

    @library_Protocol147.setter
    def library_Protocol147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Protocol__library_Protocol147", None)
        self.__library_Protocol147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Company"):
                opp_val = getattr(old_value, "library_Company", None)
                if opp_val == self:
                    setattr(old_value, "library_Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Company"):
                opp_val = getattr(value, "library_Company", None)
                setattr(value, "library_Company", self)

    @property
    def library_Protocol144(self):
        return self.__library_Protocol144

    @library_Protocol144.setter
    def library_Protocol144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Protocol__library_Protocol144", None)
        self.__library_Protocol144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Procedure145"):
                    opp_val = getattr(item, "library_Procedure145", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Procedure145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Procedure145"):
                    opp_val = getattr(item, "library_Procedure145", None)
                    
                    setattr(item, "library_Procedure145", self)
                    

    @property
    def library_Protocol76(self):
        return self.__library_Protocol76

    @library_Protocol76.setter
    def library_Protocol76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Protocol__library_Protocol76", None)
        self.__library_Protocol76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function75"):
                opp_val = getattr(old_value, "library_Function75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function75"):
                opp_val = getattr(value, "library_Function75", None)
                if opp_val is None:
                    setattr(value, "library_Function75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Protocol101(self):
        return self.__library_Protocol101

    @library_Protocol101.setter
    def library_Protocol101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Protocol__library_Protocol101", None)
        self.__library_Protocol101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library100"):
                opp_val = getattr(old_value, "library_Library100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library100"):
                opp_val = getattr(value, "library_Library100", None)
                if opp_val is None:
                    setattr(value, "library_Library100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Tolerance:

    def __init__(self, expression: str, level: str, name: str, library_Tolerance: "library_Equipment" = None, library_Tolerance73: "library_Function" = None, library_Tolerance104: "library_Library" = None):
        self.expression = expression
        self.level = level
        self.name = name
        self.library_Tolerance = library_Tolerance
        self.library_Tolerance73 = library_Tolerance73
        self.library_Tolerance104 = library_Tolerance104
        
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
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def library_Tolerance73(self):
        return self.__library_Tolerance73

    @library_Tolerance73.setter
    def library_Tolerance73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance73", None)
        self.__library_Tolerance73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function72"):
                opp_val = getattr(old_value, "library_Function72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function72"):
                opp_val = getattr(value, "library_Function72", None)
                if opp_val is None:
                    setattr(value, "library_Function72", set([self]))
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
            if hasattr(old_value, "library_Equipment16"):
                opp_val = getattr(old_value, "library_Equipment16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Equipment16"):
                opp_val = getattr(value, "library_Equipment16", None)
                if opp_val is None:
                    setattr(value, "library_Equipment16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Tolerance104(self):
        return self.__library_Tolerance104

    @library_Tolerance104.setter
    def library_Tolerance104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Tolerance__library_Tolerance104", None)
        self.__library_Tolerance104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library103"):
                opp_val = getattr(old_value, "library_Library103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library103"):
                opp_val = getattr(value, "library_Library103", None)
                if opp_val is None:
                    setattr(value, "library_Library103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_EquipmentGroup:

    def __init__(self, description: str, count: str, name: str, library_EquipmentGroup: "library_Equipment" = None, library_EquipmentGroup30: set["library_DiagramInfo"] = None, library_EquipmentGroup33: set["library_NetXResource"] = None, equipmentGroupRefs: set["library_Expression"] = None, library_EquipmentGroup38: set["library_Equipment"] = None, library_EquipmentGroup41: set["library_Parameter"] = None, library_EquipmentGroup44: set["library_NetXResource"] = None, library_EquipmentGroup47: set["library_Equipment"] = None, EquipmentGroup: "library_Expression" = None):
        self.description = description
        self.count = count
        self.name = name
        self.library_EquipmentGroup = library_EquipmentGroup
        self.library_EquipmentGroup30 = library_EquipmentGroup30 if library_EquipmentGroup30 is not None else set()
        self.library_EquipmentGroup33 = library_EquipmentGroup33 if library_EquipmentGroup33 is not None else set()
        self.equipmentGroupRefs = equipmentGroupRefs if equipmentGroupRefs is not None else set()
        self.library_EquipmentGroup38 = library_EquipmentGroup38 if library_EquipmentGroup38 is not None else set()
        self.library_EquipmentGroup41 = library_EquipmentGroup41 if library_EquipmentGroup41 is not None else set()
        self.library_EquipmentGroup44 = library_EquipmentGroup44 if library_EquipmentGroup44 is not None else set()
        self.library_EquipmentGroup47 = library_EquipmentGroup47 if library_EquipmentGroup47 is not None else set()
        self.EquipmentGroup = EquipmentGroup
        
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
                if hasattr(item, "Expression36"):
                    opp_val = getattr(item, "Expression36", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression36"):
                    opp_val = getattr(item, "Expression36", None)
                    
                    setattr(item, "Expression36", self)
                    

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
                if hasattr(item, "library_NetXResource45"):
                    opp_val = getattr(item, "library_NetXResource45", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource45"):
                    opp_val = getattr(item, "library_NetXResource45", None)
                    
                    setattr(item, "library_NetXResource45", self)
                    

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
    def library_EquipmentGroup33(self):
        return self.__library_EquipmentGroup33

    @library_EquipmentGroup33.setter
    def library_EquipmentGroup33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup33", None)
        self.__library_EquipmentGroup33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_NetXResource34"):
                    opp_val = getattr(item, "library_NetXResource34", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource34"):
                    opp_val = getattr(item, "library_NetXResource34", None)
                    
                    setattr(item, "library_NetXResource34", self)
                    

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
                if hasattr(item, "library_Equipment39"):
                    opp_val = getattr(item, "library_Equipment39", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment39"):
                    opp_val = getattr(item, "library_Equipment39", None)
                    
                    setattr(item, "library_Equipment39", self)
                    

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
                if hasattr(item, "library_Equipment48"):
                    opp_val = getattr(item, "library_Equipment48", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment48"):
                    opp_val = getattr(item, "library_Equipment48", None)
                    
                    setattr(item, "library_Equipment48", self)
                    

    @property
    def library_EquipmentGroup30(self):
        return self.__library_EquipmentGroup30

    @library_EquipmentGroup30.setter
    def library_EquipmentGroup30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_EquipmentGroup__library_EquipmentGroup30", None)
        self.__library_EquipmentGroup30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_DiagramInfo31"):
                    opp_val = getattr(item, "library_DiagramInfo31", None)
                    
                    if opp_val == self:
                        setattr(item, "library_DiagramInfo31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_DiagramInfo31"):
                    opp_val = getattr(item, "library_DiagramInfo31", None)
                    
                    setattr(item, "library_DiagramInfo31", self)
                    

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
                if hasattr(item, "library_Parameter42"):
                    opp_val = getattr(item, "library_Parameter42", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Parameter42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Parameter42"):
                    opp_val = getattr(item, "library_Parameter42", None)
                    
                    setattr(item, "library_Parameter42", self)
                    

class library_Expression:

    def __init__(self, expressionLines: str, name: str, Expression: "library_Equipment" = None, Expression36: "library_EquipmentGroup" = None, equipmentExpressionRefs: set["library_Equipment"] = None, functionExpressionRefs: set["library_Function"] = None, expressionRefs: set["library_EquipmentGroup"] = None, library_Expression: set["library_ServiceProfile"] = None, Expression70: "library_Function" = None, library_Expression107: "library_Library" = None):
        self.expressionLines = expressionLines
        self.name = name
        self.Expression = Expression
        self.Expression36 = Expression36
        self.equipmentExpressionRefs = equipmentExpressionRefs if equipmentExpressionRefs is not None else set()
        self.functionExpressionRefs = functionExpressionRefs if functionExpressionRefs is not None else set()
        self.expressionRefs = expressionRefs if expressionRefs is not None else set()
        self.library_Expression = library_Expression if library_Expression is not None else set()
        self.Expression70 = Expression70
        self.library_Expression107 = library_Expression107
        
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
    def Expression70(self):
        return self.__Expression70

    @Expression70.setter
    def Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__Expression70", None)
        self.__Expression70 = value
        
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
                    

    @property
    def library_Expression(self):
        return self.__library_Expression

    @library_Expression.setter
    def library_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression", None)
        self.__library_Expression = value if value is not None else set()
        
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
    def library_Expression107(self):
        return self.__library_Expression107

    @library_Expression107.setter
    def library_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__library_Expression107", None)
        self.__library_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library106"):
                opp_val = getattr(old_value, "library_Library106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library106"):
                opp_val = getattr(value, "library_Library106", None)
                if opp_val is None:
                    setattr(value, "library_Library106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Expression36(self):
        return self.__Expression36

    @Expression36.setter
    def Expression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Expression__Expression36", None)
        self.__Expression36 = value
        
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

class library_EquipmentRelationship:

    pass
class library_Metric:

    pass
class library_NetXResource:

    def __init__(self, detailDisplay: str, expressionName: str, longName: str, shortName: str, summaryDisplay: str, library_NetXResource: "library_Equipment" = None, library_NetXResource23: "library_Equipment" = None, library_NetXResource34: "library_EquipmentGroup" = None, library_NetXResource45: "library_EquipmentGroup" = None, library_NetXResource63: "library_Function" = None, library_NetXResource82: "library_Function" = None, library_NetXResource113: set["library_MetricValueRange"] = None, library_NetXResource115: set["library_Value"] = None, library_NetXResource117: set["library_Value"] = None, library_NetXResource120: set["library_Value"] = None, library_NetXResource123: set["library_Value"] = None, library_NetXResource126: "library_Unit" = None):
        self.detailDisplay = detailDisplay
        self.expressionName = expressionName
        self.longName = longName
        self.shortName = shortName
        self.summaryDisplay = summaryDisplay
        self.library_NetXResource = library_NetXResource
        self.library_NetXResource23 = library_NetXResource23
        self.library_NetXResource34 = library_NetXResource34
        self.library_NetXResource45 = library_NetXResource45
        self.library_NetXResource63 = library_NetXResource63
        self.library_NetXResource82 = library_NetXResource82
        self.library_NetXResource113 = library_NetXResource113 if library_NetXResource113 is not None else set()
        self.library_NetXResource115 = library_NetXResource115 if library_NetXResource115 is not None else set()
        self.library_NetXResource117 = library_NetXResource117 if library_NetXResource117 is not None else set()
        self.library_NetXResource120 = library_NetXResource120 if library_NetXResource120 is not None else set()
        self.library_NetXResource123 = library_NetXResource123 if library_NetXResource123 is not None else set()
        self.library_NetXResource126 = library_NetXResource126
        
    @property
    def summaryDisplay(self) -> str:
        return self.__summaryDisplay

    @summaryDisplay.setter
    def summaryDisplay(self, summaryDisplay: str):
        self.__summaryDisplay = summaryDisplay

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
    def detailDisplay(self) -> str:
        return self.__detailDisplay

    @detailDisplay.setter
    def detailDisplay(self, detailDisplay: str):
        self.__detailDisplay = detailDisplay

    @property
    def library_NetXResource113(self):
        return self.__library_NetXResource113

    @library_NetXResource113.setter
    def library_NetXResource113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource113", None)
        self.__library_NetXResource113 = value if value is not None else set()
        
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
                    

    @property
    def library_NetXResource23(self):
        return self.__library_NetXResource23

    @library_NetXResource23.setter
    def library_NetXResource23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource23", None)
        self.__library_NetXResource23 = value
        
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
    def library_NetXResource82(self):
        return self.__library_NetXResource82

    @library_NetXResource82.setter
    def library_NetXResource82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource82", None)
        self.__library_NetXResource82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function81"):
                opp_val = getattr(old_value, "library_Function81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function81"):
                opp_val = getattr(value, "library_Function81", None)
                if opp_val is None:
                    setattr(value, "library_Function81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource126(self):
        return self.__library_NetXResource126

    @library_NetXResource126.setter
    def library_NetXResource126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource126", None)
        self.__library_NetXResource126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Unit127"):
                opp_val = getattr(old_value, "library_Unit127", None)
                if opp_val == self:
                    setattr(old_value, "library_Unit127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Unit127"):
                opp_val = getattr(value, "library_Unit127", None)
                setattr(value, "library_Unit127", self)

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
    def library_NetXResource45(self):
        return self.__library_NetXResource45

    @library_NetXResource45.setter
    def library_NetXResource45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource45", None)
        self.__library_NetXResource45 = value
        
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

    @property
    def library_NetXResource63(self):
        return self.__library_NetXResource63

    @library_NetXResource63.setter
    def library_NetXResource63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource63", None)
        self.__library_NetXResource63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Function62"):
                opp_val = getattr(old_value, "library_Function62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Function62"):
                opp_val = getattr(value, "library_Function62", None)
                if opp_val is None:
                    setattr(value, "library_Function62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_NetXResource115(self):
        return self.__library_NetXResource115

    @library_NetXResource115.setter
    def library_NetXResource115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource115", None)
        self.__library_NetXResource115 = value if value is not None else set()
        
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
    def library_NetXResource120(self):
        return self.__library_NetXResource120

    @library_NetXResource120.setter
    def library_NetXResource120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource120", None)
        self.__library_NetXResource120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value121"):
                    opp_val = getattr(item, "library_Value121", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value121"):
                    opp_val = getattr(item, "library_Value121", None)
                    
                    setattr(item, "library_Value121", self)
                    

    @property
    def library_NetXResource34(self):
        return self.__library_NetXResource34

    @library_NetXResource34.setter
    def library_NetXResource34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource34", None)
        self.__library_NetXResource34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup33"):
                opp_val = getattr(old_value, "library_EquipmentGroup33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup33"):
                opp_val = getattr(value, "library_EquipmentGroup33", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "library_Value124"):
                    opp_val = getattr(item, "library_Value124", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value124"):
                    opp_val = getattr(item, "library_Value124", None)
                    
                    setattr(item, "library_Value124", self)
                    

    @property
    def library_NetXResource117(self):
        return self.__library_NetXResource117

    @library_NetXResource117.setter
    def library_NetXResource117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_NetXResource__library_NetXResource117", None)
        self.__library_NetXResource117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Value118"):
                    opp_val = getattr(item, "library_Value118", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Value118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Value118"):
                    opp_val = getattr(item, "library_Value118", None)
                    
                    setattr(item, "library_Value118", self)
                    

class library_Equipment:

    def __init__(self, redundancy: str, count: str, description: str, equipmentCode: str, equipmentName: str, position: str, state: str, library_Equipment: "library_Lifecycle" = None, library_Equipment2: set["library_DiagramInfo"] = None, library_Equipment5: "library_Equipment" = None, library_Equipment3: set["library_Equipment"] = None, library_Equipment9: set["library_NetXResource"] = None, library_Equipment11: set["library_Metric"] = None, library_Equipment13: set["library_EquipmentRelationship"] = None, equipmentRefs: set["library_Expression"] = None, library_Equipment7: set["library_EquipmentGroup"] = None, library_Equipment16: set["library_Tolerance"] = None, library_Equipment18: set["library_Protocol"] = None, library_Equipment20: set["library_Parameter"] = None, library_Equipment22: set["library_NetXResource"] = None, library_Equipment26: "library_Equipment" = None, library_Equipment24: set["library_Equipment"] = None, library_Equipment28: "library_MultiImage" = None, library_Equipment39: "library_EquipmentGroup" = None, library_Equipment48: "library_EquipmentGroup" = None, Equipment: "library_Expression" = None, library_Equipment92: "library_Library" = None, library_Equipment133: "library_NodeType" = None, library_Equipment136: "library_ProductInfo" = None):
        self.redundancy = redundancy
        self.count = count
        self.description = description
        self.equipmentCode = equipmentCode
        self.equipmentName = equipmentName
        self.position = position
        self.state = state
        self.library_Equipment = library_Equipment
        self.library_Equipment2 = library_Equipment2 if library_Equipment2 is not None else set()
        self.library_Equipment5 = library_Equipment5
        self.library_Equipment3 = library_Equipment3 if library_Equipment3 is not None else set()
        self.library_Equipment9 = library_Equipment9 if library_Equipment9 is not None else set()
        self.library_Equipment11 = library_Equipment11 if library_Equipment11 is not None else set()
        self.library_Equipment13 = library_Equipment13 if library_Equipment13 is not None else set()
        self.equipmentRefs = equipmentRefs if equipmentRefs is not None else set()
        self.library_Equipment7 = library_Equipment7 if library_Equipment7 is not None else set()
        self.library_Equipment16 = library_Equipment16 if library_Equipment16 is not None else set()
        self.library_Equipment18 = library_Equipment18 if library_Equipment18 is not None else set()
        self.library_Equipment20 = library_Equipment20 if library_Equipment20 is not None else set()
        self.library_Equipment22 = library_Equipment22 if library_Equipment22 is not None else set()
        self.library_Equipment26 = library_Equipment26
        self.library_Equipment24 = library_Equipment24 if library_Equipment24 is not None else set()
        self.library_Equipment28 = library_Equipment28
        self.library_Equipment39 = library_Equipment39
        self.library_Equipment48 = library_Equipment48
        self.Equipment = Equipment
        self.library_Equipment92 = library_Equipment92
        self.library_Equipment133 = library_Equipment133
        self.library_Equipment136 = library_Equipment136
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def equipmentCode(self) -> str:
        return self.__equipmentCode

    @equipmentCode.setter
    def equipmentCode(self, equipmentCode: str):
        self.__equipmentCode = equipmentCode

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def equipmentName(self) -> str:
        return self.__equipmentName

    @equipmentName.setter
    def equipmentName(self, equipmentName: str):
        self.__equipmentName = equipmentName

    @property
    def redundancy(self) -> str:
        return self.__redundancy

    @redundancy.setter
    def redundancy(self, redundancy: str):
        self.__redundancy = redundancy

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def library_Equipment39(self):
        return self.__library_Equipment39

    @library_Equipment39.setter
    def library_Equipment39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment39", None)
        self.__library_Equipment39 = value
        
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
                    

    @property
    def library_Equipment136(self):
        return self.__library_Equipment136

    @library_Equipment136.setter
    def library_Equipment136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment136", None)
        self.__library_Equipment136 = value
        
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
                if hasattr(item, "library_NetXResource23"):
                    opp_val = getattr(item, "library_NetXResource23", None)
                    
                    if opp_val == self:
                        setattr(item, "library_NetXResource23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_NetXResource23"):
                    opp_val = getattr(item, "library_NetXResource23", None)
                    
                    setattr(item, "library_NetXResource23", self)
                    

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
    def library_Equipment133(self):
        return self.__library_Equipment133

    @library_Equipment133.setter
    def library_Equipment133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment133", None)
        self.__library_Equipment133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_NodeType132"):
                opp_val = getattr(old_value, "library_NodeType132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_NodeType132"):
                opp_val = getattr(value, "library_NodeType132", None)
                if opp_val is None:
                    setattr(value, "library_NodeType132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def library_Equipment48(self):
        return self.__library_Equipment48

    @library_Equipment48.setter
    def library_Equipment48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment48", None)
        self.__library_Equipment48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_EquipmentGroup47"):
                opp_val = getattr(old_value, "library_EquipmentGroup47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_EquipmentGroup47"):
                opp_val = getattr(value, "library_EquipmentGroup47", None)
                if opp_val is None:
                    setattr(value, "library_EquipmentGroup47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment92(self):
        return self.__library_Equipment92

    @library_Equipment92.setter
    def library_Equipment92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment92", None)
        self.__library_Equipment92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library91"):
                opp_val = getattr(old_value, "library_Library91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library91"):
                opp_val = getattr(value, "library_Library91", None)
                if opp_val is None:
                    setattr(value, "library_Library91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Equipment16(self):
        return self.__library_Equipment16

    @library_Equipment16.setter
    def library_Equipment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment16", None)
        self.__library_Equipment16 = value if value is not None else set()
        
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
    def library_Equipment26(self):
        return self.__library_Equipment26

    @library_Equipment26.setter
    def library_Equipment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment26", None)
        self.__library_Equipment26 = value
        
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
    def library_Equipment28(self):
        return self.__library_Equipment28

    @library_Equipment28.setter
    def library_Equipment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Equipment__library_Equipment28", None)
        self.__library_Equipment28 = value
        
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
                if hasattr(item, "library_Equipment26"):
                    opp_val = getattr(item, "library_Equipment26", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Equipment26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Equipment26"):
                    opp_val = getattr(item, "library_Equipment26", None)
                    
                    setattr(item, "library_Equipment26", self)
                    

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
                    

class library_DiagramInfo:

    pass
class library_Lifecycle:

    pass