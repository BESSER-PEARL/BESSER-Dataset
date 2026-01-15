from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LinkEndStyle(Enum):
    Unknown = "Unknown"
    NoArrow = "NoArrow"
    OpenTriangle = "OpenTriangle"
    EmptyTriangle = "EmptyTriangle"
    FilledTriangle = "FilledTriangle"
    EmptyRhombus = "EmptyRhombus"
    FilledRhombus = "FilledRhombus"
class JoinSplitType(Enum):
    None = "None"
    XOR = "XOR"
    AND = "AND"
    OR = "OR"
class OrientationType(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"
class ActivityImplementationType(Enum):
    Manual = "Manual"
    Application = "Application"
    Subprocess = "Subprocess"
    Route = "Route"
class LinkCardinality(Enum):
    Unknown = "Unknown"
    One = "One"
    Many = "Many"
class LoopType(Enum):
    Unknown = "Unknown"
    None = "None"
    While = "While"
    Repeat = "Repeat"
class DirectionType(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class LinkColor(Enum):
    Unknown = "Unknown"
    Black = "Black"
    DarkBlue = "DarkBlue"
    DarkGray = "DarkGray"
    Blue = "Blue"
    LightGray = "LightGray"
    Red = "Red"
    Yellow = "Yellow"
class LinkLineStyle(Enum):
    Unknown = "Unknown"
    Normal = "Normal"
    ShortStrokes = "ShortStrokes"
    LongStrokes = "LongStrokes"
class ImplementationType(Enum):
    engine = "engine"
    pull = "pull"
    push = "push"
class DiagramModeType(Enum):
    MODE_4_0_0 = "MODE_4_0_0"
    MODE_4_5_0 = "MODE_4_5_0"
class FlowControlType(Enum):
    none = "none"
    join = "join"
    split = "split"
class SubProcessModeType(Enum):
    sync_shared = "sync_shared"
    sync_separate = "sync_separate"
    async_separate = "async_separate"
class RoutingType(Enum):
    Default = "Default"
    ShortestPath = "ShortestPath"
    Manhattan = "Manhattan"
    Explicit = "Explicit"


############################################
# Definition of Classes
############################################

class extensions_carnot_DataType:

    pass
class carnot_extensions_FormalParameterMappingType:

    pass
class FormalParameterMappingType:

    pass
class carnot_extensions_FormalParameterMappingsType:

    def __init__(self, carnot_extensions_FormalParameterMappingsType: set["FormalParameterMappingType"] = None):
        self.carnot_extensions_FormalParameterMappingsType = carnot_extensions_FormalParameterMappingsType if carnot_extensions_FormalParameterMappingsType is not None else set()
        
    @property
    def carnot_extensions_FormalParameterMappingsType(self):
        return self.__carnot_extensions_FormalParameterMappingsType

    @carnot_extensions_FormalParameterMappingsType.setter
    def carnot_extensions_FormalParameterMappingsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_extensions_FormalParameterMappingsType__carnot_extensions_FormalParameterMappingsType", None)
        self.__carnot_extensions_FormalParameterMappingsType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormalParameterMappingType"):
                    opp_val = getattr(item, "FormalParameterMappingType", None)
                    
                    if opp_val == self:
                        setattr(item, "FormalParameterMappingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormalParameterMappingType"):
                    opp_val = getattr(item, "FormalParameterMappingType", None)
                    
                    setattr(item, "FormalParameterMappingType", self)
                    

    def getMappedData(self, formalParameter: str) -> str:
        # TODO: Implement getMappedData method
        pass

    def setMappedData(self, data: str, formalParameter: str):
        # TODO: Implement setMappedData method
        pass

class extensions_carnot_FormalParameterType:

    pass
class carnot_ViewableType:

    pass
class FormalParameterMappingsType:

    pass
class carnot_FormalParametersType:

    pass
class carnot_QualityControlType:

    pass
class carnot_TypeDeclarationsType:

    pass
class carnot_ScriptType:

    pass
class carnot_ExternalPackages:

    pass
class ISwimlaneSymbol:

    pass
class carnot_IdRefOwner(ABC):

    pass
class carnot_ExternalPackage:

    pass
class carnot_IdRef:

    def __init__(self, ref: str, carnot_IdRef: "carnot_ExternalPackage" = None, carnot_IdRef193: "carnot_IdRefOwner" = None):
        self.ref = ref
        self.carnot_IdRef = carnot_IdRef
        self.carnot_IdRef193 = carnot_IdRef193
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def carnot_IdRef193(self):
        return self.__carnot_IdRef193

    @carnot_IdRef193.setter
    def carnot_IdRef193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IdRef__carnot_IdRef193", None)
        self.__carnot_IdRef193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IdRefOwner"):
                opp_val = getattr(old_value, "carnot_IdRefOwner", None)
                if opp_val == self:
                    setattr(old_value, "carnot_IdRefOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IdRefOwner"):
                opp_val = getattr(value, "carnot_IdRefOwner", None)
                setattr(value, "carnot_IdRefOwner", self)

    @property
    def carnot_IdRef(self):
        return self.__carnot_IdRef

    @carnot_IdRef.setter
    def carnot_IdRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IdRef__carnot_IdRef", None)
        self.__carnot_IdRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ExternalPackage"):
                opp_val = getattr(old_value, "carnot_ExternalPackage", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ExternalPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ExternalPackage"):
                opp_val = getattr(value, "carnot_ExternalPackage", None)
                setattr(value, "carnot_ExternalPackage", self)

class AbstractEventSymbol:

    pass
class carnot_EStringToStringMapEntry:

    pass
class carnot_DocumentRoot:

    def __init__(self, mixed: str, carnot_DocumentRoot: set["carnot_EStringToStringMapEntry"] = None, carnot_DocumentRoot171: set["carnot_EStringToStringMapEntry"] = None, carnot_DocumentRoot174: set["carnot_ModelType"] = None):
        self.mixed = mixed
        self.carnot_DocumentRoot = carnot_DocumentRoot if carnot_DocumentRoot is not None else set()
        self.carnot_DocumentRoot171 = carnot_DocumentRoot171 if carnot_DocumentRoot171 is not None else set()
        self.carnot_DocumentRoot174 = carnot_DocumentRoot174 if carnot_DocumentRoot174 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def carnot_DocumentRoot171(self):
        return self.__carnot_DocumentRoot171

    @carnot_DocumentRoot171.setter
    def carnot_DocumentRoot171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DocumentRoot__carnot_DocumentRoot171", None)
        self.__carnot_DocumentRoot171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EStringToStringMapEntry172"):
                    opp_val = getattr(item, "carnot_EStringToStringMapEntry172", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EStringToStringMapEntry172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EStringToStringMapEntry172"):
                    opp_val = getattr(item, "carnot_EStringToStringMapEntry172", None)
                    
                    setattr(item, "carnot_EStringToStringMapEntry172", self)
                    

    @property
    def carnot_DocumentRoot174(self):
        return self.__carnot_DocumentRoot174

    @carnot_DocumentRoot174.setter
    def carnot_DocumentRoot174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DocumentRoot__carnot_DocumentRoot174", None)
        self.__carnot_DocumentRoot174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ModelType"):
                    opp_val = getattr(item, "carnot_ModelType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ModelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ModelType"):
                    opp_val = getattr(item, "carnot_ModelType", None)
                    
                    setattr(item, "carnot_ModelType", self)
                    

    @property
    def carnot_DocumentRoot(self):
        return self.__carnot_DocumentRoot

    @carnot_DocumentRoot.setter
    def carnot_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DocumentRoot__carnot_DocumentRoot", None)
        self.__carnot_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EStringToStringMapEntry"):
                    opp_val = getattr(item, "carnot_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EStringToStringMapEntry"):
                    opp_val = getattr(item, "carnot_EStringToStringMapEntry", None)
                    
                    setattr(item, "carnot_EStringToStringMapEntry", self)
                    

class ISymbolContainer:

    pass
class carnot_ExternalReferenceType:

    pass
class carnot_PoolSymbol(ISymbolContainer, ISwimlaneSymbol):

    def __init__(self, boundaryVisible: str, PoolSymbol: "carnot_DiagramType" = None, PoolSymbol201: "carnot_LaneSymbol" = None, poolSymbols: "carnot_DiagramType" = None, carnot_PoolSymbol: "carnot_ProcessDefinitionType" = None, parentPool: set["carnot_LaneSymbol"] = None):
        self.boundaryVisible = boundaryVisible
        self.PoolSymbol = PoolSymbol
        self.PoolSymbol201 = PoolSymbol201
        self.poolSymbols = poolSymbols
        self.carnot_PoolSymbol = carnot_PoolSymbol
        self.parentPool = parentPool if parentPool is not None else set()
        
    @property
    def boundaryVisible(self) -> str:
        return self.__boundaryVisible

    @boundaryVisible.setter
    def boundaryVisible(self, boundaryVisible: str):
        self.__boundaryVisible = boundaryVisible

    @property
    def parentPool(self):
        return self.__parentPool

    @parentPool.setter
    def parentPool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_PoolSymbol__parentPool", None)
        self.__parentPool = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LaneSymbol281"):
                    opp_val = getattr(item, "LaneSymbol281", None)
                    
                    if opp_val == self:
                        setattr(item, "LaneSymbol281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LaneSymbol281"):
                    opp_val = getattr(item, "LaneSymbol281", None)
                    
                    setattr(item, "LaneSymbol281", self)
                    

    @property
    def PoolSymbol(self):
        return self.__PoolSymbol

    @PoolSymbol.setter
    def PoolSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_PoolSymbol__PoolSymbol", None)
        self.__PoolSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PoolSymbol201(self):
        return self.__PoolSymbol201

    @PoolSymbol201.setter
    def PoolSymbol201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_PoolSymbol__PoolSymbol201", None)
        self.__PoolSymbol201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lanes"):
                opp_val = getattr(old_value, "lanes", None)
                if opp_val == self:
                    setattr(old_value, "lanes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lanes"):
                opp_val = getattr(value, "lanes", None)
                setattr(value, "lanes", self)

    @property
    def poolSymbols(self):
        return self.__poolSymbols

    @poolSymbols.setter
    def poolSymbols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_PoolSymbol__poolSymbols", None)
        self.__poolSymbols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramType"):
                opp_val = getattr(old_value, "DiagramType", None)
                if opp_val == self:
                    setattr(old_value, "DiagramType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramType"):
                opp_val = getattr(value, "DiagramType", None)
                setattr(value, "DiagramType", self)

    @property
    def carnot_PoolSymbol(self):
        return self.__carnot_PoolSymbol

    @carnot_PoolSymbol.setter
    def carnot_PoolSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_PoolSymbol__carnot_PoolSymbol", None)
        self.__carnot_PoolSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ProcessDefinitionType279"):
                opp_val = getattr(old_value, "carnot_ProcessDefinitionType279", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ProcessDefinitionType279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ProcessDefinitionType279"):
                opp_val = getattr(value, "carnot_ProcessDefinitionType279", None)
                setattr(value, "carnot_ProcessDefinitionType279", self)

class IConnectionSymbol:

    pass
class IModelParticipant:

    pass
class carnot_RoleType(IModelParticipant):

    def __init__(self, cardinality: int, carnot_RoleType: "carnot_ModelType" = None, RoleType: "carnot_OrganizationType" = None, teamLead: set["carnot_OrganizationType"] = None, role: set["carnot_RoleSymbolType"] = None, RoleType313: "carnot_RoleSymbolType" = None):
        self.cardinality = cardinality
        self.carnot_RoleType = carnot_RoleType
        self.RoleType = RoleType
        self.teamLead = teamLead if teamLead is not None else set()
        self.role = role if role is not None else set()
        self.RoleType313 = RoleType313
        
    @property
    def cardinality(self) -> int:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality

    @property
    def teamLead(self):
        return self.__teamLead

    @teamLead.setter
    def teamLead(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_RoleType__teamLead", None)
        self.__teamLead = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganizationType320"):
                    opp_val = getattr(item, "OrganizationType320", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationType320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationType320"):
                    opp_val = getattr(item, "OrganizationType320", None)
                    
                    setattr(item, "OrganizationType320", self)
                    

    @property
    def carnot_RoleType(self):
        return self.__carnot_RoleType

    @carnot_RoleType.setter
    def carnot_RoleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_RoleType__carnot_RoleType", None)
        self.__carnot_RoleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType235"):
                opp_val = getattr(old_value, "carnot_ModelType235", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType235"):
                opp_val = getattr(value, "carnot_ModelType235", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType235", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoleType313(self):
        return self.__RoleType313

    @RoleType313.setter
    def RoleType313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_RoleType__RoleType313", None)
        self.__RoleType313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roleSymbols"):
                opp_val = getattr(old_value, "roleSymbols", None)
                if opp_val == self:
                    setattr(old_value, "roleSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roleSymbols"):
                opp_val = getattr(value, "roleSymbols", None)
                setattr(value, "roleSymbols", self)

    @property
    def RoleType(self):
        return self.__RoleType

    @RoleType.setter
    def RoleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_RoleType__RoleType", None)
        self.__RoleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teams"):
                opp_val = getattr(old_value, "teams", None)
                if opp_val == self:
                    setattr(old_value, "teams", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teams"):
                opp_val = getattr(value, "teams", None)
                setattr(value, "teams", self)

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_RoleType__role", None)
        self.__role = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoleSymbolType"):
                    opp_val = getattr(item, "RoleSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "RoleSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoleSymbolType"):
                    opp_val = getattr(item, "RoleSymbolType", None)
                    
                    setattr(item, "RoleSymbolType", self)
                    

class carnot_OrganizationType(IModelParticipant):

    pass
class carnot_ConditionalPerformerType(IModelParticipant):

    def __init__(self, dataPath: str, isUser: str, ConditionalPerformerType: "carnot_ConditionalPerformerSymbolType" = None, conditionalPerformers: "carnot_DataType" = None, participant133: set["carnot_ConditionalPerformerSymbolType"] = None, ConditionalPerformerType159: "carnot_DataType" = None, carnot_ConditionalPerformerType: "carnot_ModelType" = None):
        self.dataPath = dataPath
        self.isUser = isUser
        self.ConditionalPerformerType = ConditionalPerformerType
        self.conditionalPerformers = conditionalPerformers
        self.participant133 = participant133 if participant133 is not None else set()
        self.ConditionalPerformerType159 = ConditionalPerformerType159
        self.carnot_ConditionalPerformerType = carnot_ConditionalPerformerType
        
    @property
    def isUser(self) -> str:
        return self.__isUser

    @isUser.setter
    def isUser(self, isUser: str):
        self.__isUser = isUser

    @property
    def dataPath(self) -> str:
        return self.__dataPath

    @dataPath.setter
    def dataPath(self, dataPath: str):
        self.__dataPath = dataPath

    @property
    def conditionalPerformers(self):
        return self.__conditionalPerformers

    @conditionalPerformers.setter
    def conditionalPerformers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ConditionalPerformerType__conditionalPerformers", None)
        self.__conditionalPerformers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def ConditionalPerformerType(self):
        return self.__ConditionalPerformerType

    @ConditionalPerformerType.setter
    def ConditionalPerformerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ConditionalPerformerType__ConditionalPerformerType", None)
        self.__ConditionalPerformerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conditionalPerformerSymbols"):
                opp_val = getattr(old_value, "conditionalPerformerSymbols", None)
                if opp_val == self:
                    setattr(old_value, "conditionalPerformerSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conditionalPerformerSymbols"):
                opp_val = getattr(value, "conditionalPerformerSymbols", None)
                setattr(value, "conditionalPerformerSymbols", self)

    @property
    def ConditionalPerformerType159(self):
        return self.__ConditionalPerformerType159

    @ConditionalPerformerType159.setter
    def ConditionalPerformerType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ConditionalPerformerType__ConditionalPerformerType159", None)
        self.__ConditionalPerformerType159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data158"):
                opp_val = getattr(old_value, "data158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data158"):
                opp_val = getattr(value, "data158", None)
                if opp_val is None:
                    setattr(value, "data158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participant133(self):
        return self.__participant133

    @participant133.setter
    def participant133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ConditionalPerformerType__participant133", None)
        self.__participant133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalPerformerSymbolType"):
                    opp_val = getattr(item, "ConditionalPerformerSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalPerformerSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalPerformerSymbolType"):
                    opp_val = getattr(item, "ConditionalPerformerSymbolType", None)
                    
                    setattr(item, "ConditionalPerformerSymbolType", self)
                    

    @property
    def carnot_ConditionalPerformerType(self):
        return self.__carnot_ConditionalPerformerType

    @carnot_ConditionalPerformerType.setter
    def carnot_ConditionalPerformerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ConditionalPerformerType__carnot_ConditionalPerformerType", None)
        self.__carnot_ConditionalPerformerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType239"):
                opp_val = getattr(old_value, "carnot_ModelType239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType239"):
                opp_val = getattr(value, "carnot_ModelType239", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IModelParticipantSymbol:

    pass
class carnot_XmlTextNode:

    def __init__(self, mixed: str, carnot_XmlTextNode: "carnot_AttributeType" = None, carnot_XmlTextNode345: "carnot_TransitionType" = None):
        self.mixed = mixed
        self.carnot_XmlTextNode = carnot_XmlTextNode
        self.carnot_XmlTextNode345 = carnot_XmlTextNode345
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def carnot_XmlTextNode345(self):
        return self.__carnot_XmlTextNode345

    @carnot_XmlTextNode345.setter
    def carnot_XmlTextNode345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_XmlTextNode__carnot_XmlTextNode345", None)
        self.__carnot_XmlTextNode345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_TransitionType344"):
                opp_val = getattr(old_value, "carnot_TransitionType344", None)
                if opp_val == self:
                    setattr(old_value, "carnot_TransitionType344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_TransitionType344"):
                opp_val = getattr(value, "carnot_TransitionType344", None)
                setattr(value, "carnot_TransitionType344", self)

    @property
    def carnot_XmlTextNode(self):
        return self.__carnot_XmlTextNode

    @carnot_XmlTextNode.setter
    def carnot_XmlTextNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_XmlTextNode__carnot_XmlTextNode", None)
        self.__carnot_XmlTextNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_AttributeType128"):
                opp_val = getattr(old_value, "carnot_AttributeType128", None)
                if opp_val == self:
                    setattr(old_value, "carnot_AttributeType128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_AttributeType128"):
                opp_val = getattr(value, "carnot_AttributeType128", None)
                setattr(value, "carnot_AttributeType128", self)

class AbstractEventAction:

    pass
class carnot_UnbindActionType(AbstractEventAction):

    pass
class carnot_EventActionType(AbstractEventAction):

    pass
class carnot_BindActionType(AbstractEventAction):

    pass
class IMetaType:

    pass
class carnot_TriggerTypeType(IMetaType):

    def __init__(self, panelClass: str, pullTrigger: str, pullTriggerEvaluator: str, rule: str, carnot_TriggerTypeType: "carnot_ModelType" = None, TriggerTypeType: "carnot_TriggerType" = None, type364: set["carnot_TriggerType"] = None):
        self.panelClass = panelClass
        self.pullTrigger = pullTrigger
        self.pullTriggerEvaluator = pullTriggerEvaluator
        self.rule = rule
        self.carnot_TriggerTypeType = carnot_TriggerTypeType
        self.TriggerTypeType = TriggerTypeType
        self.type364 = type364 if type364 is not None else set()
        
    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def pullTrigger(self) -> str:
        return self.__pullTrigger

    @pullTrigger.setter
    def pullTrigger(self, pullTrigger: str):
        self.__pullTrigger = pullTrigger

    @property
    def pullTriggerEvaluator(self) -> str:
        return self.__pullTriggerEvaluator

    @pullTriggerEvaluator.setter
    def pullTriggerEvaluator(self, pullTriggerEvaluator: str):
        self.__pullTriggerEvaluator = pullTriggerEvaluator

    @property
    def TriggerTypeType(self):
        return self.__TriggerTypeType

    @TriggerTypeType.setter
    def TriggerTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TriggerTypeType__TriggerTypeType", None)
        self.__TriggerTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triggers"):
                opp_val = getattr(old_value, "triggers", None)
                if opp_val == self:
                    setattr(old_value, "triggers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triggers"):
                opp_val = getattr(value, "triggers", None)
                setattr(value, "triggers", self)

    @property
    def type364(self):
        return self.__type364

    @type364.setter
    def type364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TriggerTypeType__type364", None)
        self.__type364 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TriggerType365"):
                    opp_val = getattr(item, "TriggerType365", None)
                    
                    if opp_val == self:
                        setattr(item, "TriggerType365", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TriggerType365"):
                    opp_val = getattr(item, "TriggerType365", None)
                    
                    setattr(item, "TriggerType365", self)
                    

    @property
    def carnot_TriggerTypeType(self):
        return self.__carnot_TriggerTypeType

    @carnot_TriggerTypeType.setter
    def carnot_TriggerTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TriggerTypeType__carnot_TriggerTypeType", None)
        self.__carnot_TriggerTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType219"):
                opp_val = getattr(old_value, "carnot_ModelType219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType219"):
                opp_val = getattr(value, "carnot_ModelType219", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_EventConditionTypeType(IMetaType):

    def __init__(self, activityCondition: str, binderClass: str, implementation: str, panelClass: str, processCondition: str, pullEventEmitterClass: str, rule: str, type178: set["carnot_EventHandlerType"] = None, EventConditionTypeType: "carnot_EventHandlerType" = None, carnot_EventConditionTypeType: "carnot_ModelType" = None):
        self.activityCondition = activityCondition
        self.binderClass = binderClass
        self.implementation = implementation
        self.panelClass = panelClass
        self.processCondition = processCondition
        self.pullEventEmitterClass = pullEventEmitterClass
        self.rule = rule
        self.type178 = type178 if type178 is not None else set()
        self.EventConditionTypeType = EventConditionTypeType
        self.carnot_EventConditionTypeType = carnot_EventConditionTypeType
        
    @property
    def pullEventEmitterClass(self) -> str:
        return self.__pullEventEmitterClass

    @pullEventEmitterClass.setter
    def pullEventEmitterClass(self, pullEventEmitterClass: str):
        self.__pullEventEmitterClass = pullEventEmitterClass

    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def processCondition(self) -> str:
        return self.__processCondition

    @processCondition.setter
    def processCondition(self, processCondition: str):
        self.__processCondition = processCondition

    @property
    def binderClass(self) -> str:
        return self.__binderClass

    @binderClass.setter
    def binderClass(self, binderClass: str):
        self.__binderClass = binderClass

    @property
    def activityCondition(self) -> str:
        return self.__activityCondition

    @activityCondition.setter
    def activityCondition(self, activityCondition: str):
        self.__activityCondition = activityCondition

    @property
    def type178(self):
        return self.__type178

    @type178.setter
    def type178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventConditionTypeType__type178", None)
        self.__type178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventHandlerType"):
                    opp_val = getattr(item, "EventHandlerType", None)
                    
                    if opp_val == self:
                        setattr(item, "EventHandlerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventHandlerType"):
                    opp_val = getattr(item, "EventHandlerType", None)
                    
                    setattr(item, "EventHandlerType", self)
                    

    @property
    def carnot_EventConditionTypeType(self):
        return self.__carnot_EventConditionTypeType

    @carnot_EventConditionTypeType.setter
    def carnot_EventConditionTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventConditionTypeType__carnot_EventConditionTypeType", None)
        self.__carnot_EventConditionTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType221"):
                opp_val = getattr(old_value, "carnot_ModelType221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType221"):
                opp_val = getattr(value, "carnot_ModelType221", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EventConditionTypeType(self):
        return self.__EventConditionTypeType

    @EventConditionTypeType.setter
    def EventConditionTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventConditionTypeType__EventConditionTypeType", None)
        self.__EventConditionTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventHandlers"):
                opp_val = getattr(old_value, "eventHandlers", None)
                if opp_val == self:
                    setattr(old_value, "eventHandlers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventHandlers"):
                opp_val = getattr(value, "eventHandlers", None)
                setattr(value, "eventHandlers", self)

class carnot_ApplicationTypeType(IMetaType):

    def __init__(self, panelClass: str, synchronous: str, validatorClass: str, accessPointProviderClass: str, instanceClass: str, ApplicationTypeType: "carnot_ApplicationType" = None, type125: set["carnot_ApplicationType"] = None, carnot_ApplicationTypeType: "carnot_ModelType" = None):
        self.panelClass = panelClass
        self.synchronous = synchronous
        self.validatorClass = validatorClass
        self.accessPointProviderClass = accessPointProviderClass
        self.instanceClass = instanceClass
        self.ApplicationTypeType = ApplicationTypeType
        self.type125 = type125 if type125 is not None else set()
        self.carnot_ApplicationTypeType = carnot_ApplicationTypeType
        
    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def accessPointProviderClass(self) -> str:
        return self.__accessPointProviderClass

    @accessPointProviderClass.setter
    def accessPointProviderClass(self, accessPointProviderClass: str):
        self.__accessPointProviderClass = accessPointProviderClass

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def synchronous(self) -> str:
        return self.__synchronous

    @synchronous.setter
    def synchronous(self, synchronous: str):
        self.__synchronous = synchronous

    @property
    def validatorClass(self) -> str:
        return self.__validatorClass

    @validatorClass.setter
    def validatorClass(self, validatorClass: str):
        self.__validatorClass = validatorClass

    @property
    def carnot_ApplicationTypeType(self):
        return self.__carnot_ApplicationTypeType

    @carnot_ApplicationTypeType.setter
    def carnot_ApplicationTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationTypeType__carnot_ApplicationTypeType", None)
        self.__carnot_ApplicationTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType215"):
                opp_val = getattr(old_value, "carnot_ModelType215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType215"):
                opp_val = getattr(value, "carnot_ModelType215", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def type125(self):
        return self.__type125

    @type125.setter
    def type125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationTypeType__type125", None)
        self.__type125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationType126"):
                    opp_val = getattr(item, "ApplicationType126", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationType126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationType126"):
                    opp_val = getattr(item, "ApplicationType126", None)
                    
                    setattr(item, "ApplicationType126", self)
                    

    @property
    def ApplicationTypeType(self):
        return self.__ApplicationTypeType

    @ApplicationTypeType.setter
    def ApplicationTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationTypeType__ApplicationTypeType", None)
        self.__ApplicationTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applications"):
                opp_val = getattr(old_value, "applications", None)
                if opp_val == self:
                    setattr(old_value, "applications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applications"):
                opp_val = getattr(value, "applications", None)
                setattr(value, "applications", self)

class carnot_ApplicationContextTypeType(IMetaType):

    def __init__(self, accessPointProviderClass: str, hasApplicationPath: str, hasMappingId: str, panelClass: str, validatorClass: str, type: set["carnot_ContextType"] = None, ApplicationContextTypeType: "carnot_ContextType" = None, carnot_ApplicationContextTypeType: "carnot_ModelType" = None):
        self.accessPointProviderClass = accessPointProviderClass
        self.hasApplicationPath = hasApplicationPath
        self.hasMappingId = hasMappingId
        self.panelClass = panelClass
        self.validatorClass = validatorClass
        self.type = type if type is not None else set()
        self.ApplicationContextTypeType = ApplicationContextTypeType
        self.carnot_ApplicationContextTypeType = carnot_ApplicationContextTypeType
        
    @property
    def validatorClass(self) -> str:
        return self.__validatorClass

    @validatorClass.setter
    def validatorClass(self, validatorClass: str):
        self.__validatorClass = validatorClass

    @property
    def hasApplicationPath(self) -> str:
        return self.__hasApplicationPath

    @hasApplicationPath.setter
    def hasApplicationPath(self, hasApplicationPath: str):
        self.__hasApplicationPath = hasApplicationPath

    @property
    def accessPointProviderClass(self) -> str:
        return self.__accessPointProviderClass

    @accessPointProviderClass.setter
    def accessPointProviderClass(self, accessPointProviderClass: str):
        self.__accessPointProviderClass = accessPointProviderClass

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def hasMappingId(self) -> str:
        return self.__hasMappingId

    @hasMappingId.setter
    def hasMappingId(self, hasMappingId: str):
        self.__hasMappingId = hasMappingId

    @property
    def ApplicationContextTypeType(self):
        return self.__ApplicationContextTypeType

    @ApplicationContextTypeType.setter
    def ApplicationContextTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationContextTypeType__ApplicationContextTypeType", None)
        self.__ApplicationContextTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contexts"):
                opp_val = getattr(old_value, "contexts", None)
                if opp_val == self:
                    setattr(old_value, "contexts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contexts"):
                opp_val = getattr(value, "contexts", None)
                setattr(value, "contexts", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationContextTypeType__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContextType"):
                    opp_val = getattr(item, "ContextType", None)
                    
                    if opp_val == self:
                        setattr(item, "ContextType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContextType"):
                    opp_val = getattr(item, "ContextType", None)
                    
                    setattr(item, "ContextType", self)
                    

    @property
    def carnot_ApplicationContextTypeType(self):
        return self.__carnot_ApplicationContextTypeType

    @carnot_ApplicationContextTypeType.setter
    def carnot_ApplicationContextTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationContextTypeType__carnot_ApplicationContextTypeType", None)
        self.__carnot_ApplicationContextTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType217"):
                opp_val = getattr(old_value, "carnot_ModelType217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType217"):
                opp_val = getattr(value, "carnot_ModelType217", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_TextType:

    def __init__(self, mixed: str, carnot_TextType: "carnot_AnnotationSymbolType" = None):
        self.mixed = mixed
        self.carnot_TextType = carnot_TextType
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def carnot_TextType(self):
        return self.__carnot_TextType

    @carnot_TextType.setter
    def carnot_TextType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TextType__carnot_TextType", None)
        self.__carnot_TextType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_AnnotationSymbolType112"):
                opp_val = getattr(old_value, "carnot_AnnotationSymbolType112", None)
                if opp_val == self:
                    setattr(old_value, "carnot_AnnotationSymbolType112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_AnnotationSymbolType112"):
                opp_val = getattr(value, "carnot_AnnotationSymbolType112", None)
                setattr(value, "carnot_AnnotationSymbolType112", self)

class carnot_LoopType:

    pass
class IAccessPointOwner:

    pass
class carnot_Code:

    def __init__(self, code: str, value: str, name: str, carnot_Code: "carnot_ActivityType" = None, carnot_Code308: "carnot_QualityControlType" = None):
        self.code = code
        self.value = value
        self.name = name
        self.carnot_Code = carnot_Code
        self.carnot_Code308 = carnot_Code308
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def carnot_Code308(self):
        return self.__carnot_Code308

    @carnot_Code308.setter
    def carnot_Code308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_Code__carnot_Code308", None)
        self.__carnot_Code308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_QualityControlType307"):
                opp_val = getattr(old_value, "carnot_QualityControlType307", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_QualityControlType307"):
                opp_val = getattr(value, "carnot_QualityControlType307", None)
                if opp_val is None:
                    setattr(value, "carnot_QualityControlType307", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_Code(self):
        return self.__carnot_Code

    @carnot_Code.setter
    def carnot_Code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_Code__carnot_Code", None)
        self.__carnot_Code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ActivityType108"):
                opp_val = getattr(old_value, "carnot_ActivityType108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ActivityType108"):
                opp_val = getattr(value, "carnot_ActivityType108", None)
                if opp_val is None:
                    setattr(value, "carnot_ActivityType108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IdRefOwner:

    pass
class IEventHandlerOwner:

    pass
class IFlowObjectSymbol:

    pass
class carnot_EventActionTypeType(IMetaType):

    def __init__(self, actionClass: str, activityAction: str, panelClass: str, processAction: str, supportedConditionTypes: str, unsupportedContexts: str, EventActionTypeType: "carnot_AbstractEventAction" = None, type176: set["carnot_AbstractEventAction"] = None, carnot_EventActionTypeType: "carnot_ModelType" = None):
        self.actionClass = actionClass
        self.activityAction = activityAction
        self.panelClass = panelClass
        self.processAction = processAction
        self.supportedConditionTypes = supportedConditionTypes
        self.unsupportedContexts = unsupportedContexts
        self.EventActionTypeType = EventActionTypeType
        self.type176 = type176 if type176 is not None else set()
        self.carnot_EventActionTypeType = carnot_EventActionTypeType
        
    @property
    def unsupportedContexts(self) -> str:
        return self.__unsupportedContexts

    @unsupportedContexts.setter
    def unsupportedContexts(self, unsupportedContexts: str):
        self.__unsupportedContexts = unsupportedContexts

    @property
    def activityAction(self) -> str:
        return self.__activityAction

    @activityAction.setter
    def activityAction(self, activityAction: str):
        self.__activityAction = activityAction

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def actionClass(self) -> str:
        return self.__actionClass

    @actionClass.setter
    def actionClass(self, actionClass: str):
        self.__actionClass = actionClass

    @property
    def processAction(self) -> str:
        return self.__processAction

    @processAction.setter
    def processAction(self, processAction: str):
        self.__processAction = processAction

    @property
    def supportedConditionTypes(self) -> str:
        return self.__supportedConditionTypes

    @supportedConditionTypes.setter
    def supportedConditionTypes(self, supportedConditionTypes: str):
        self.__supportedConditionTypes = supportedConditionTypes

    @property
    def carnot_EventActionTypeType(self):
        return self.__carnot_EventActionTypeType

    @carnot_EventActionTypeType.setter
    def carnot_EventActionTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventActionTypeType__carnot_EventActionTypeType", None)
        self.__carnot_EventActionTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType223"):
                opp_val = getattr(old_value, "carnot_ModelType223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType223"):
                opp_val = getattr(value, "carnot_ModelType223", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def type176(self):
        return self.__type176

    @type176.setter
    def type176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventActionTypeType__type176", None)
        self.__type176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractEventAction"):
                    opp_val = getattr(item, "AbstractEventAction", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractEventAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractEventAction"):
                    opp_val = getattr(item, "AbstractEventAction", None)
                    
                    setattr(item, "AbstractEventAction", self)
                    

    @property
    def EventActionTypeType(self):
        return self.__EventActionTypeType

    @EventActionTypeType.setter
    def EventActionTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventActionTypeType__EventActionTypeType", None)
        self.__EventActionTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actionInstances"):
                opp_val = getattr(old_value, "actionInstances", None)
                if opp_val == self:
                    setattr(old_value, "actionInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actionInstances"):
                opp_val = getattr(value, "actionInstances", None)
                setattr(value, "actionInstances", self)

class ITypedElement:

    pass
class IModelElementNodeSymbol:

    pass
class carnot_AbstractEventSymbol(IModelElementNodeSymbol, IFlowObjectSymbol):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class carnot_IModelParticipantSymbol(IModelElementNodeSymbol):

    pass
class carnot_ParticipantType:

    pass
class carnot_DataTypeType(IMetaType):

    def __init__(self, accessPathEditor: str, evaluator: str, instanceClass: str, panelClass: str, readable: str, storageStrategy: str, validatorClass: str, valueCreator: str, writable: str, carnot_DataTypeType: "carnot_AccessPointType" = None, DataTypeType: "carnot_DataType" = None, type166: set["carnot_DataType"] = None, carnot_DataTypeType213: "carnot_ModelType" = None):
        self.accessPathEditor = accessPathEditor
        self.evaluator = evaluator
        self.instanceClass = instanceClass
        self.panelClass = panelClass
        self.readable = readable
        self.storageStrategy = storageStrategy
        self.validatorClass = validatorClass
        self.valueCreator = valueCreator
        self.writable = writable
        self.carnot_DataTypeType = carnot_DataTypeType
        self.DataTypeType = DataTypeType
        self.type166 = type166 if type166 is not None else set()
        self.carnot_DataTypeType213 = carnot_DataTypeType213
        
    @property
    def readable(self) -> str:
        return self.__readable

    @readable.setter
    def readable(self, readable: str):
        self.__readable = readable

    @property
    def evaluator(self) -> str:
        return self.__evaluator

    @evaluator.setter
    def evaluator(self, evaluator: str):
        self.__evaluator = evaluator

    @property
    def panelClass(self) -> str:
        return self.__panelClass

    @panelClass.setter
    def panelClass(self, panelClass: str):
        self.__panelClass = panelClass

    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def validatorClass(self) -> str:
        return self.__validatorClass

    @validatorClass.setter
    def validatorClass(self, validatorClass: str):
        self.__validatorClass = validatorClass

    @property
    def writable(self) -> str:
        return self.__writable

    @writable.setter
    def writable(self, writable: str):
        self.__writable = writable

    @property
    def accessPathEditor(self) -> str:
        return self.__accessPathEditor

    @accessPathEditor.setter
    def accessPathEditor(self, accessPathEditor: str):
        self.__accessPathEditor = accessPathEditor

    @property
    def storageStrategy(self) -> str:
        return self.__storageStrategy

    @storageStrategy.setter
    def storageStrategy(self, storageStrategy: str):
        self.__storageStrategy = storageStrategy

    @property
    def valueCreator(self) -> str:
        return self.__valueCreator

    @valueCreator.setter
    def valueCreator(self, valueCreator: str):
        self.__valueCreator = valueCreator

    @property
    def carnot_DataTypeType213(self):
        return self.__carnot_DataTypeType213

    @carnot_DataTypeType213.setter
    def carnot_DataTypeType213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataTypeType__carnot_DataTypeType213", None)
        self.__carnot_DataTypeType213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType212"):
                opp_val = getattr(old_value, "carnot_ModelType212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType212"):
                opp_val = getattr(value, "carnot_ModelType212", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_DataTypeType(self):
        return self.__carnot_DataTypeType

    @carnot_DataTypeType.setter
    def carnot_DataTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataTypeType__carnot_DataTypeType", None)
        self.__carnot_DataTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_AccessPointType81"):
                opp_val = getattr(old_value, "carnot_AccessPointType81", None)
                if opp_val == self:
                    setattr(old_value, "carnot_AccessPointType81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_AccessPointType81"):
                opp_val = getattr(value, "carnot_AccessPointType81", None)
                setattr(value, "carnot_AccessPointType81", self)

    @property
    def DataTypeType(self):
        return self.__DataTypeType

    @DataTypeType.setter
    def DataTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataTypeType__DataTypeType", None)
        self.__DataTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data153"):
                opp_val = getattr(old_value, "data153", None)
                if opp_val == self:
                    setattr(old_value, "data153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data153"):
                opp_val = getattr(value, "data153", None)
                setattr(value, "data153", self)

    @property
    def type166(self):
        return self.__type166

    @type166.setter
    def type166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataTypeType__type166", None)
        self.__type166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType167"):
                    opp_val = getattr(item, "DataType167", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType167"):
                    opp_val = getattr(item, "DataType167", None)
                    
                    setattr(item, "DataType167", self)
                    

class carnot_LaneSymbol(ISymbolContainer, ISwimlaneSymbol):

    pass
class INodeSymbol:

    pass
class carnot_IModelElementNodeSymbol(INodeSymbol):

    def __init__(self):
        
    def setModelElement(self, element: IIdentifiableModelElement):
        # TODO: Implement setModelElement method
        pass

    def getModelElement(self) -> IIdentifiableModelElement:
        # TODO: Implement getModelElement method
        pass

class carnot_IFlowObjectSymbol(INodeSymbol):

    pass
class IGraphicalObject:

    pass
class carnot_IConnectionSymbol(IGraphicalObject):

    def __init__(self, sourceAnchor: str, targetAnchor: str, routing: str, carnot_IConnectionSymbol: set["carnot_Coordinates"] = None):
        self.sourceAnchor = sourceAnchor
        self.targetAnchor = targetAnchor
        self.routing = routing
        self.carnot_IConnectionSymbol = carnot_IConnectionSymbol if carnot_IConnectionSymbol is not None else set()
        
    @property
    def sourceAnchor(self) -> str:
        return self.__sourceAnchor

    @sourceAnchor.setter
    def sourceAnchor(self, sourceAnchor: str):
        self.__sourceAnchor = sourceAnchor

    @property
    def routing(self) -> str:
        return self.__routing

    @routing.setter
    def routing(self, routing: str):
        self.__routing = routing

    @property
    def targetAnchor(self) -> str:
        return self.__targetAnchor

    @targetAnchor.setter
    def targetAnchor(self, targetAnchor: str):
        self.__targetAnchor = targetAnchor

    @property
    def carnot_IConnectionSymbol(self):
        return self.__carnot_IConnectionSymbol

    @carnot_IConnectionSymbol.setter
    def carnot_IConnectionSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IConnectionSymbol__carnot_IConnectionSymbol", None)
        self.__carnot_IConnectionSymbol = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_Coordinates"):
                    opp_val = getattr(item, "carnot_Coordinates", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_Coordinates", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_Coordinates"):
                    opp_val = getattr(item, "carnot_Coordinates", None)
                    
                    setattr(item, "carnot_Coordinates", self)
                    

    def setSourceNode(self, nodeSymbol: INodeSymbol):
        # TODO: Implement setSourceNode method
        pass

    def setTargetNode(self, nodeSymbol: INodeSymbol):
        # TODO: Implement setTargetNode method
        pass

    def getTargetNode(self) -> INodeSymbol:
        # TODO: Implement getTargetNode method
        pass

    def getSourceNode(self) -> INodeSymbol:
        # TODO: Implement getSourceNode method
        pass

class carnot_INodeSymbol(IGraphicalObject):

    def __init__(self, xPos: str, yPos: str, width: str, height: str, shape: str, targetSymbol: set["carnot_GenericLinkConnectionType"] = None, sourceSymbol: set["carnot_GenericLinkConnectionType"] = None, INodeSymbol: "carnot_GenericLinkConnectionType" = None, INodeSymbol199: "carnot_GenericLinkConnectionType" = None):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.shape = shape
        self.targetSymbol = targetSymbol if targetSymbol is not None else set()
        self.sourceSymbol = sourceSymbol if sourceSymbol is not None else set()
        self.INodeSymbol = INodeSymbol
        self.INodeSymbol199 = INodeSymbol199
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def xPos(self) -> str:
        return self.__xPos

    @xPos.setter
    def xPos(self, xPos: str):
        self.__xPos = xPos

    @property
    def yPos(self) -> str:
        return self.__yPos

    @yPos.setter
    def yPos(self, yPos: str):
        self.__yPos = yPos

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def INodeSymbol(self):
        return self.__INodeSymbol

    @INodeSymbol.setter
    def INodeSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_INodeSymbol__INodeSymbol", None)
        self.__INodeSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outLinks"):
                opp_val = getattr(old_value, "outLinks", None)
                if opp_val == self:
                    setattr(old_value, "outLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outLinks"):
                opp_val = getattr(value, "outLinks", None)
                setattr(value, "outLinks", self)

    @property
    def sourceSymbol(self):
        return self.__sourceSymbol

    @sourceSymbol.setter
    def sourceSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_INodeSymbol__sourceSymbol", None)
        self.__sourceSymbol = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GenericLinkConnectionType64"):
                    opp_val = getattr(item, "GenericLinkConnectionType64", None)
                    
                    if opp_val == self:
                        setattr(item, "GenericLinkConnectionType64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GenericLinkConnectionType64"):
                    opp_val = getattr(item, "GenericLinkConnectionType64", None)
                    
                    setattr(item, "GenericLinkConnectionType64", self)
                    

    @property
    def INodeSymbol199(self):
        return self.__INodeSymbol199

    @INodeSymbol199.setter
    def INodeSymbol199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_INodeSymbol__INodeSymbol199", None)
        self.__INodeSymbol199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inLinks"):
                opp_val = getattr(old_value, "inLinks", None)
                if opp_val == self:
                    setattr(old_value, "inLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inLinks"):
                opp_val = getattr(value, "inLinks", None)
                setattr(value, "inLinks", self)

    @property
    def targetSymbol(self):
        return self.__targetSymbol

    @targetSymbol.setter
    def targetSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_INodeSymbol__targetSymbol", None)
        self.__targetSymbol = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GenericLinkConnectionType"):
                    opp_val = getattr(item, "GenericLinkConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "GenericLinkConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GenericLinkConnectionType"):
                    opp_val = getattr(item, "GenericLinkConnectionType", None)
                    
                    setattr(item, "GenericLinkConnectionType", self)
                    

    def getInConnectionFeatures(self) -> str:
        # TODO: Implement getInConnectionFeatures method
        pass

    def getOutConnectionFeatures(self) -> str:
        # TODO: Implement getOutConnectionFeatures method
        pass

class carnot_TeamLeadConnectionType(IConnectionSymbol):

    pass
class carnot_WorksForConnectionType(IConnectionSymbol):

    pass
class carnot_TransitionConnectionType(IConnectionSymbol):

    def __init__(self, points: str, carnot_TransitionConnectionType: "carnot_ISymbolContainer" = None, TransitionConnectionType: "carnot_IFlowObjectSymbol" = None, TransitionConnectionType70: "carnot_IFlowObjectSymbol" = None, outTransitions: "carnot_IFlowObjectSymbol" = None, inTransitions: "carnot_IFlowObjectSymbol" = None, transitionConnections: "carnot_TransitionType" = None, TransitionConnectionType353: "carnot_TransitionType" = None):
        self.points = points
        self.carnot_TransitionConnectionType = carnot_TransitionConnectionType
        self.TransitionConnectionType = TransitionConnectionType
        self.TransitionConnectionType70 = TransitionConnectionType70
        self.outTransitions = outTransitions
        self.inTransitions = inTransitions
        self.transitionConnections = transitionConnections
        self.TransitionConnectionType353 = TransitionConnectionType353
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def outTransitions(self):
        return self.__outTransitions

    @outTransitions.setter
    def outTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__outTransitions", None)
        self.__outTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IFlowObjectSymbol"):
                opp_val = getattr(old_value, "IFlowObjectSymbol", None)
                if opp_val == self:
                    setattr(old_value, "IFlowObjectSymbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IFlowObjectSymbol"):
                opp_val = getattr(value, "IFlowObjectSymbol", None)
                setattr(value, "IFlowObjectSymbol", self)

    @property
    def TransitionConnectionType353(self):
        return self.__TransitionConnectionType353

    @TransitionConnectionType353.setter
    def TransitionConnectionType353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__TransitionConnectionType353", None)
        self.__TransitionConnectionType353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                if opp_val is None:
                    setattr(value, "transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TransitionConnectionType(self):
        return self.__TransitionConnectionType

    @TransitionConnectionType.setter
    def TransitionConnectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__TransitionConnectionType", None)
        self.__TransitionConnectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetActivitySymbol"):
                opp_val = getattr(old_value, "targetActivitySymbol", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetActivitySymbol"):
                opp_val = getattr(value, "targetActivitySymbol", None)
                if opp_val is None:
                    setattr(value, "targetActivitySymbol", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_TransitionConnectionType(self):
        return self.__carnot_TransitionConnectionType

    @carnot_TransitionConnectionType.setter
    def carnot_TransitionConnectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__carnot_TransitionConnectionType", None)
        self.__carnot_TransitionConnectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ISymbolContainer54"):
                opp_val = getattr(old_value, "carnot_ISymbolContainer54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ISymbolContainer54"):
                opp_val = getattr(value, "carnot_ISymbolContainer54", None)
                if opp_val is None:
                    setattr(value, "carnot_ISymbolContainer54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transitionConnections(self):
        return self.__transitionConnections

    @transitionConnections.setter
    def transitionConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__transitionConnections", None)
        self.__transitionConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransitionType342"):
                opp_val = getattr(old_value, "TransitionType342", None)
                if opp_val == self:
                    setattr(old_value, "TransitionType342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransitionType342"):
                opp_val = getattr(value, "TransitionType342", None)
                setattr(value, "TransitionType342", self)

    @property
    def TransitionConnectionType70(self):
        return self.__TransitionConnectionType70

    @TransitionConnectionType70.setter
    def TransitionConnectionType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__TransitionConnectionType70", None)
        self.__TransitionConnectionType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceActivitySymbol"):
                opp_val = getattr(old_value, "sourceActivitySymbol", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceActivitySymbol"):
                opp_val = getattr(value, "sourceActivitySymbol", None)
                if opp_val is None:
                    setattr(value, "sourceActivitySymbol", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inTransitions(self):
        return self.__inTransitions

    @inTransitions.setter
    def inTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionConnectionType__inTransitions", None)
        self.__inTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IFlowObjectSymbol340"):
                opp_val = getattr(old_value, "IFlowObjectSymbol340", None)
                if opp_val == self:
                    setattr(old_value, "IFlowObjectSymbol340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IFlowObjectSymbol340"):
                opp_val = getattr(value, "IFlowObjectSymbol340", None)
                setattr(value, "IFlowObjectSymbol340", self)

class carnot_SubProcessOfConnectionType(IConnectionSymbol):

    pass
class carnot_RefersToConnectionType(IConnectionSymbol):

    pass
class carnot_TriggersConnectionType(IConnectionSymbol):

    pass
class carnot_PerformsConnectionType(IConnectionSymbol):

    pass
class carnot_PartOfConnectionType(IConnectionSymbol):

    pass
class carnot_GenericLinkConnectionType(IConnectionSymbol, ITypedElement):

    pass
class carnot_ExecutedByConnectionType(IConnectionSymbol):

    pass
class carnot_DataMappingConnectionType(IConnectionSymbol):

    pass
class carnot_TextSymbolType(INodeSymbol):

    def __init__(self, text: str, carnot_TextSymbolType: "carnot_ISymbolContainer" = None):
        self.text = text
        self.carnot_TextSymbolType = carnot_TextSymbolType
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def carnot_TextSymbolType(self):
        return self.__carnot_TextSymbolType

    @carnot_TextSymbolType.setter
    def carnot_TextSymbolType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TextSymbolType__carnot_TextSymbolType", None)
        self.__carnot_TextSymbolType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ISymbolContainer36"):
                opp_val = getattr(old_value, "carnot_ISymbolContainer36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ISymbolContainer36"):
                opp_val = getattr(value, "carnot_ISymbolContainer36", None)
                if opp_val is None:
                    setattr(value, "carnot_ISymbolContainer36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_StartEventSymbol(AbstractEventSymbol):

    pass
class carnot_RoleSymbolType(IModelParticipantSymbol):

    pass
class carnot_PublicInterfaceSymbol(AbstractEventSymbol):

    pass
class carnot_ProcessSymbolType(IModelElementNodeSymbol):

    pass
class carnot_OrganizationSymbolType(IModelParticipantSymbol):

    pass
class carnot_ModelerSymbolType(IModelElementNodeSymbol):

    pass
class carnot_IntermediateEventSymbol(AbstractEventSymbol):

    pass
class carnot_GroupSymbolType(ISymbolContainer, INodeSymbol):

    pass
class carnot_GatewaySymbol(IFlowObjectSymbol):

    def __init__(self, flowKind: str, carnot_GatewaySymbol: "carnot_ISymbolContainer" = None, GatewaySymbol: "carnot_ActivitySymbolType" = None, gatewaySymbols: "carnot_ActivitySymbolType" = None):
        self.flowKind = flowKind
        self.carnot_GatewaySymbol = carnot_GatewaySymbol
        self.GatewaySymbol = GatewaySymbol
        self.gatewaySymbols = gatewaySymbols
        
    @property
    def flowKind(self) -> str:
        return self.__flowKind

    @flowKind.setter
    def flowKind(self, flowKind: str):
        self.__flowKind = flowKind

    @property
    def carnot_GatewaySymbol(self):
        return self.__carnot_GatewaySymbol

    @carnot_GatewaySymbol.setter
    def carnot_GatewaySymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_GatewaySymbol__carnot_GatewaySymbol", None)
        self.__carnot_GatewaySymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ISymbolContainer18"):
                opp_val = getattr(old_value, "carnot_ISymbolContainer18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ISymbolContainer18"):
                opp_val = getattr(value, "carnot_ISymbolContainer18", None)
                if opp_val is None:
                    setattr(value, "carnot_ISymbolContainer18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GatewaySymbol(self):
        return self.__GatewaySymbol

    @GatewaySymbol.setter
    def GatewaySymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_GatewaySymbol__GatewaySymbol", None)
        self.__GatewaySymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitySymbol91"):
                opp_val = getattr(old_value, "activitySymbol91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitySymbol91"):
                opp_val = getattr(value, "activitySymbol91", None)
                if opp_val is None:
                    setattr(value, "activitySymbol91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gatewaySymbols(self):
        return self.__gatewaySymbols

    @gatewaySymbols.setter
    def gatewaySymbols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_GatewaySymbol__gatewaySymbols", None)
        self.__gatewaySymbols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitySymbolType195"):
                opp_val = getattr(old_value, "ActivitySymbolType195", None)
                if opp_val == self:
                    setattr(old_value, "ActivitySymbolType195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitySymbolType195"):
                opp_val = getattr(value, "ActivitySymbolType195", None)
                setattr(value, "ActivitySymbolType195", self)

class carnot_EndEventSymbol(AbstractEventSymbol):

    pass
class carnot_DataSymbolType(IModelElementNodeSymbol):

    pass
class carnot_ConditionalPerformerSymbolType(IModelParticipantSymbol):

    pass
class carnot_ApplicationSymbolType(IModelElementNodeSymbol):

    pass
class carnot_AnnotationSymbolType(INodeSymbol):

    pass
class carnot_ActivitySymbolType(IModelElementNodeSymbol, IFlowObjectSymbol):

    pass
class carnot_ITypedElement(ABC):

    def __init__(self):
        
    def getMetaType(self) -> str:
        # TODO: Implement getMetaType method
        pass

class IIdentifiableModelElement:

    pass
class carnot_ModelerType(IIdentifiableModelElement):

    def __init__(self, email: str, password: str, modeler: set["carnot_ModelerSymbolType"] = None, ModelerType: "carnot_ModelerSymbolType" = None, carnot_ModelerType: "carnot_ModelType" = None):
        self.email = email
        self.password = password
        self.modeler = modeler if modeler is not None else set()
        self.ModelerType = ModelerType
        self.carnot_ModelerType = carnot_ModelerType
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def carnot_ModelerType(self):
        return self.__carnot_ModelerType

    @carnot_ModelerType.setter
    def carnot_ModelerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelerType__carnot_ModelerType", None)
        self.__carnot_ModelerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType231"):
                opp_val = getattr(old_value, "carnot_ModelType231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType231"):
                opp_val = getattr(value, "carnot_ModelType231", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modeler(self):
        return self.__modeler

    @modeler.setter
    def modeler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelerType__modeler", None)
        self.__modeler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelerSymbolType"):
                    opp_val = getattr(item, "ModelerSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelerSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelerSymbolType"):
                    opp_val = getattr(item, "ModelerSymbolType", None)
                    
                    setattr(item, "ModelerSymbolType", self)
                    

    @property
    def ModelerType(self):
        return self.__ModelerType

    @ModelerType.setter
    def ModelerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelerType__ModelerType", None)
        self.__ModelerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelerSymbols"):
                opp_val = getattr(old_value, "modelerSymbols", None)
                if opp_val == self:
                    setattr(old_value, "modelerSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelerSymbols"):
                opp_val = getattr(value, "modelerSymbols", None)
                setattr(value, "modelerSymbols", self)

class carnot_DataType(ITypedElement, IIdentifiableModelElement):

    def __init__(self, predefined: str, DataType: "carnot_ConditionalPerformerType" = None, DataType146: "carnot_DataPathType" = None, DataType144: "carnot_DataMappingType" = None, data155: set["carnot_DataSymbolType"] = None, data158: set["carnot_ConditionalPerformerType"] = None, data161: set["carnot_DataPathType"] = None, data163: set["carnot_ParameterMappingType"] = None, DataType148: "carnot_DataSymbolType" = None, data: set["carnot_DataMappingType"] = None, data153: "carnot_DataTypeType" = None, carnot_DataType: "carnot_ExternalReferenceType" = None, DataType167: "carnot_DataTypeType" = None, carnot_DataType226: "carnot_ModelType" = None, DataType266: "carnot_ParameterMappingType" = None):
        self.predefined = predefined
        self.DataType = DataType
        self.DataType146 = DataType146
        self.DataType144 = DataType144
        self.data155 = data155 if data155 is not None else set()
        self.data158 = data158 if data158 is not None else set()
        self.data161 = data161 if data161 is not None else set()
        self.data163 = data163 if data163 is not None else set()
        self.DataType148 = DataType148
        self.data = data if data is not None else set()
        self.data153 = data153
        self.carnot_DataType = carnot_DataType
        self.DataType167 = DataType167
        self.carnot_DataType226 = carnot_DataType226
        self.DataType266 = DataType266
        
    @property
    def predefined(self) -> str:
        return self.__predefined

    @predefined.setter
    def predefined(self, predefined: str):
        self.__predefined = predefined

    @property
    def data161(self):
        return self.__data161

    @data161.setter
    def data161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data161", None)
        self.__data161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataPathType"):
                    opp_val = getattr(item, "DataPathType", None)
                    
                    if opp_val == self:
                        setattr(item, "DataPathType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataPathType"):
                    opp_val = getattr(item, "DataPathType", None)
                    
                    setattr(item, "DataPathType", self)
                    

    @property
    def carnot_DataType(self):
        return self.__carnot_DataType

    @carnot_DataType.setter
    def carnot_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__carnot_DataType", None)
        self.__carnot_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ExternalReferenceType"):
                opp_val = getattr(old_value, "carnot_ExternalReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ExternalReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ExternalReferenceType"):
                opp_val = getattr(value, "carnot_ExternalReferenceType", None)
                setattr(value, "carnot_ExternalReferenceType", self)

    @property
    def data163(self):
        return self.__data163

    @data163.setter
    def data163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data163", None)
        self.__data163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterMappingType"):
                    opp_val = getattr(item, "ParameterMappingType", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterMappingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterMappingType"):
                    opp_val = getattr(item, "ParameterMappingType", None)
                    
                    setattr(item, "ParameterMappingType", self)
                    

    @property
    def DataType167(self):
        return self.__DataType167

    @DataType167.setter
    def DataType167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType167", None)
        self.__DataType167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type166"):
                opp_val = getattr(old_value, "type166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type166"):
                opp_val = getattr(value, "type166", None)
                if opp_val is None:
                    setattr(value, "type166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_DataType226(self):
        return self.__carnot_DataType226

    @carnot_DataType226.setter
    def carnot_DataType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__carnot_DataType226", None)
        self.__carnot_DataType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType225"):
                opp_val = getattr(old_value, "carnot_ModelType225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType225"):
                opp_val = getattr(value, "carnot_ModelType225", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def data155(self):
        return self.__data155

    @data155.setter
    def data155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data155", None)
        self.__data155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataSymbolType156"):
                    opp_val = getattr(item, "DataSymbolType156", None)
                    
                    if opp_val == self:
                        setattr(item, "DataSymbolType156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataSymbolType156"):
                    opp_val = getattr(item, "DataSymbolType156", None)
                    
                    setattr(item, "DataSymbolType156", self)
                    

    @property
    def DataType148(self):
        return self.__DataType148

    @DataType148.setter
    def DataType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType148", None)
        self.__DataType148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataSymbols"):
                opp_val = getattr(old_value, "dataSymbols", None)
                if opp_val == self:
                    setattr(old_value, "dataSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataSymbols"):
                opp_val = getattr(value, "dataSymbols", None)
                setattr(value, "dataSymbols", self)

    @property
    def DataType266(self):
        return self.__DataType266

    @DataType266.setter
    def DataType266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType266", None)
        self.__DataType266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterMappings"):
                opp_val = getattr(old_value, "parameterMappings", None)
                if opp_val == self:
                    setattr(old_value, "parameterMappings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterMappings"):
                opp_val = getattr(value, "parameterMappings", None)
                setattr(value, "parameterMappings", self)

    @property
    def data158(self):
        return self.__data158

    @data158.setter
    def data158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data158", None)
        self.__data158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalPerformerType159"):
                    opp_val = getattr(item, "ConditionalPerformerType159", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalPerformerType159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalPerformerType159"):
                    opp_val = getattr(item, "ConditionalPerformerType159", None)
                    
                    setattr(item, "ConditionalPerformerType159", self)
                    

    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType", None)
        self.__DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conditionalPerformers"):
                opp_val = getattr(old_value, "conditionalPerformers", None)
                if opp_val == self:
                    setattr(old_value, "conditionalPerformers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conditionalPerformers"):
                opp_val = getattr(value, "conditionalPerformers", None)
                setattr(value, "conditionalPerformers", self)

    @property
    def DataType144(self):
        return self.__DataType144

    @DataType144.setter
    def DataType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType144", None)
        self.__DataType144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataMappings143"):
                opp_val = getattr(old_value, "dataMappings143", None)
                if opp_val == self:
                    setattr(old_value, "dataMappings143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataMappings143"):
                opp_val = getattr(value, "dataMappings143", None)
                setattr(value, "dataMappings143", self)

    @property
    def data153(self):
        return self.__data153

    @data153.setter
    def data153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data153", None)
        self.__data153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeType"):
                opp_val = getattr(old_value, "DataTypeType", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeType"):
                opp_val = getattr(value, "DataTypeType", None)
                setattr(value, "DataTypeType", self)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__data", None)
        self.__data = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataMappingType"):
                    opp_val = getattr(item, "DataMappingType", None)
                    
                    if opp_val == self:
                        setattr(item, "DataMappingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataMappingType"):
                    opp_val = getattr(item, "DataMappingType", None)
                    
                    setattr(item, "DataMappingType", self)
                    

    @property
    def DataType146(self):
        return self.__DataType146

    @DataType146.setter
    def DataType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataType__DataType146", None)
        self.__DataType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataPaths"):
                opp_val = getattr(old_value, "dataPaths", None)
                if opp_val == self:
                    setattr(old_value, "dataPaths", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataPaths"):
                opp_val = getattr(value, "dataPaths", None)
                setattr(value, "dataPaths", self)

class carnot_DataPathType(IIdentifiableModelElement):

    def __init__(self, dataPath: str, descriptor: str, key: str, direction: str, dataPaths: "carnot_DataType" = None, DataPathType: "carnot_DataType" = None, carnot_DataPathType: "carnot_ProcessDefinitionType" = None):
        self.dataPath = dataPath
        self.descriptor = descriptor
        self.key = key
        self.direction = direction
        self.dataPaths = dataPaths
        self.DataPathType = DataPathType
        self.carnot_DataPathType = carnot_DataPathType
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

    @property
    def dataPath(self) -> str:
        return self.__dataPath

    @dataPath.setter
    def dataPath(self, dataPath: str):
        self.__dataPath = dataPath

    @property
    def carnot_DataPathType(self):
        return self.__carnot_DataPathType

    @carnot_DataPathType.setter
    def carnot_DataPathType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataPathType__carnot_DataPathType", None)
        self.__carnot_DataPathType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ProcessDefinitionType290"):
                opp_val = getattr(old_value, "carnot_ProcessDefinitionType290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ProcessDefinitionType290"):
                opp_val = getattr(value, "carnot_ProcessDefinitionType290", None)
                if opp_val is None:
                    setattr(value, "carnot_ProcessDefinitionType290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataPaths(self):
        return self.__dataPaths

    @dataPaths.setter
    def dataPaths(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataPathType__dataPaths", None)
        self.__dataPaths = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType146"):
                opp_val = getattr(old_value, "DataType146", None)
                if opp_val == self:
                    setattr(old_value, "DataType146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType146"):
                opp_val = getattr(value, "DataType146", None)
                setattr(value, "DataType146", self)

    @property
    def DataPathType(self):
        return self.__DataPathType

    @DataPathType.setter
    def DataPathType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataPathType__DataPathType", None)
        self.__DataPathType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data161"):
                opp_val = getattr(old_value, "data161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data161"):
                opp_val = getattr(value, "data161", None)
                if opp_val is None:
                    setattr(value, "data161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_ActivityType(IdRefOwner, IEventHandlerOwner, IIdentifiableModelElement):

    def __init__(self, hibernateOnCreation: str, implementation: str, allowsAbortByPerformer: str, join: str, loopCondition: str, loopType: str, split: str, subProcessMode: str, ActivityType: "carnot_IModelParticipant" = None, ActivityType83: "carnot_ActivitySymbolType" = None, carnot_ActivityType: set["carnot_DataMappingType"] = None, executedActivities: "carnot_ApplicationType" = None, startActivity: set["carnot_StartEventSymbol"] = None, to103: set["carnot_TransitionType"] = None, from105: set["carnot_TransitionType"] = None, carnot_ActivityType108: set["carnot_Code"] = None, executingActivities: "carnot_ProcessDefinitionType" = None, performedActivities: "carnot_IModelParticipant" = None, carnot_ActivityType98: "carnot_IModelParticipant" = None, activity: set["carnot_ActivitySymbolType"] = None, carnot_ActivityType110: "carnot_LoopType" = None, ActivityType121: "carnot_ApplicationType" = None, carnot_ActivityType284: "carnot_ProcessDefinitionType" = None, ActivityType295: "carnot_ProcessDefinitionType" = None, ActivityType327: "carnot_StartEventSymbol" = None, ActivityType348: "carnot_TransitionType" = None, ActivityType351: "carnot_TransitionType" = None):
        self.hibernateOnCreation = hibernateOnCreation
        self.implementation = implementation
        self.allowsAbortByPerformer = allowsAbortByPerformer
        self.join = join
        self.loopCondition = loopCondition
        self.loopType = loopType
        self.split = split
        self.subProcessMode = subProcessMode
        self.ActivityType = ActivityType
        self.ActivityType83 = ActivityType83
        self.carnot_ActivityType = carnot_ActivityType if carnot_ActivityType is not None else set()
        self.executedActivities = executedActivities
        self.startActivity = startActivity if startActivity is not None else set()
        self.to103 = to103 if to103 is not None else set()
        self.from105 = from105 if from105 is not None else set()
        self.carnot_ActivityType108 = carnot_ActivityType108 if carnot_ActivityType108 is not None else set()
        self.executingActivities = executingActivities
        self.performedActivities = performedActivities
        self.carnot_ActivityType98 = carnot_ActivityType98
        self.activity = activity if activity is not None else set()
        self.carnot_ActivityType110 = carnot_ActivityType110
        self.ActivityType121 = ActivityType121
        self.carnot_ActivityType284 = carnot_ActivityType284
        self.ActivityType295 = ActivityType295
        self.ActivityType327 = ActivityType327
        self.ActivityType348 = ActivityType348
        self.ActivityType351 = ActivityType351
        
    @property
    def loopCondition(self) -> str:
        return self.__loopCondition

    @loopCondition.setter
    def loopCondition(self, loopCondition: str):
        self.__loopCondition = loopCondition

    @property
    def allowsAbortByPerformer(self) -> str:
        return self.__allowsAbortByPerformer

    @allowsAbortByPerformer.setter
    def allowsAbortByPerformer(self, allowsAbortByPerformer: str):
        self.__allowsAbortByPerformer = allowsAbortByPerformer

    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

    @property
    def hibernateOnCreation(self) -> str:
        return self.__hibernateOnCreation

    @hibernateOnCreation.setter
    def hibernateOnCreation(self, hibernateOnCreation: str):
        self.__hibernateOnCreation = hibernateOnCreation

    @property
    def split(self) -> str:
        return self.__split

    @split.setter
    def split(self, split: str):
        self.__split = split

    @property
    def subProcessMode(self) -> str:
        return self.__subProcessMode

    @subProcessMode.setter
    def subProcessMode(self, subProcessMode: str):
        self.__subProcessMode = subProcessMode

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

    @property
    def ActivityType351(self):
        return self.__ActivityType351

    @ActivityType351.setter
    def ActivityType351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType351", None)
        self.__ActivityType351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTransitions350"):
                opp_val = getattr(old_value, "inTransitions350", None)
                if opp_val == self:
                    setattr(old_value, "inTransitions350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTransitions350"):
                opp_val = getattr(value, "inTransitions350", None)
                setattr(value, "inTransitions350", self)

    @property
    def carnot_ActivityType98(self):
        return self.__carnot_ActivityType98

    @carnot_ActivityType98.setter
    def carnot_ActivityType98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__carnot_ActivityType98", None)
        self.__carnot_ActivityType98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IModelParticipant99"):
                opp_val = getattr(old_value, "carnot_IModelParticipant99", None)
                if opp_val == self:
                    setattr(old_value, "carnot_IModelParticipant99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IModelParticipant99"):
                opp_val = getattr(value, "carnot_IModelParticipant99", None)
                setattr(value, "carnot_IModelParticipant99", self)

    @property
    def carnot_ActivityType110(self):
        return self.__carnot_ActivityType110

    @carnot_ActivityType110.setter
    def carnot_ActivityType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__carnot_ActivityType110", None)
        self.__carnot_ActivityType110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_LoopType"):
                opp_val = getattr(old_value, "carnot_LoopType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_LoopType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_LoopType"):
                opp_val = getattr(value, "carnot_LoopType", None)
                setattr(value, "carnot_LoopType", self)

    @property
    def ActivityType348(self):
        return self.__ActivityType348

    @ActivityType348.setter
    def ActivityType348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType348", None)
        self.__ActivityType348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outTransitions347"):
                opp_val = getattr(old_value, "outTransitions347", None)
                if opp_val == self:
                    setattr(old_value, "outTransitions347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outTransitions347"):
                opp_val = getattr(value, "outTransitions347", None)
                setattr(value, "outTransitions347", self)

    @property
    def startActivity(self):
        return self.__startActivity

    @startActivity.setter
    def startActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__startActivity", None)
        self.__startActivity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StartEventSymbol"):
                    opp_val = getattr(item, "StartEventSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "StartEventSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StartEventSymbol"):
                    opp_val = getattr(item, "StartEventSymbol", None)
                    
                    setattr(item, "StartEventSymbol", self)
                    

    @property
    def carnot_ActivityType284(self):
        return self.__carnot_ActivityType284

    @carnot_ActivityType284.setter
    def carnot_ActivityType284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__carnot_ActivityType284", None)
        self.__carnot_ActivityType284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ProcessDefinitionType283"):
                opp_val = getattr(old_value, "carnot_ProcessDefinitionType283", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ProcessDefinitionType283"):
                opp_val = getattr(value, "carnot_ProcessDefinitionType283", None)
                if opp_val is None:
                    setattr(value, "carnot_ProcessDefinitionType283", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def executedActivities(self):
        return self.__executedActivities

    @executedActivities.setter
    def executedActivities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__executedActivities", None)
        self.__executedActivities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationType"):
                opp_val = getattr(old_value, "ApplicationType", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationType"):
                opp_val = getattr(value, "ApplicationType", None)
                setattr(value, "ApplicationType", self)

    @property
    def ActivityType(self):
        return self.__ActivityType

    @ActivityType.setter
    def ActivityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType", None)
        self.__ActivityType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performer"):
                opp_val = getattr(old_value, "performer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performer"):
                opp_val = getattr(value, "performer", None)
                if opp_val is None:
                    setattr(value, "performer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityType327(self):
        return self.__ActivityType327

    @ActivityType327.setter
    def ActivityType327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType327", None)
        self.__ActivityType327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "startingEventSymbols326"):
                opp_val = getattr(old_value, "startingEventSymbols326", None)
                if opp_val == self:
                    setattr(old_value, "startingEventSymbols326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "startingEventSymbols326"):
                opp_val = getattr(value, "startingEventSymbols326", None)
                setattr(value, "startingEventSymbols326", self)

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitySymbolType"):
                    opp_val = getattr(item, "ActivitySymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitySymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitySymbolType"):
                    opp_val = getattr(item, "ActivitySymbolType", None)
                    
                    setattr(item, "ActivitySymbolType", self)
                    

    @property
    def ActivityType121(self):
        return self.__ActivityType121

    @ActivityType121.setter
    def ActivityType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType121", None)
        self.__ActivityType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application"):
                opp_val = getattr(old_value, "application", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application"):
                opp_val = getattr(value, "application", None)
                if opp_val is None:
                    setattr(value, "application", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def executingActivities(self):
        return self.__executingActivities

    @executingActivities.setter
    def executingActivities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__executingActivities", None)
        self.__executingActivities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessDefinitionType"):
                opp_val = getattr(old_value, "ProcessDefinitionType", None)
                if opp_val == self:
                    setattr(old_value, "ProcessDefinitionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessDefinitionType"):
                opp_val = getattr(value, "ProcessDefinitionType", None)
                setattr(value, "ProcessDefinitionType", self)

    @property
    def to103(self):
        return self.__to103

    @to103.setter
    def to103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__to103", None)
        self.__to103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionType"):
                    opp_val = getattr(item, "TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionType"):
                    opp_val = getattr(item, "TransitionType", None)
                    
                    setattr(item, "TransitionType", self)
                    

    @property
    def from105(self):
        return self.__from105

    @from105.setter
    def from105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__from105", None)
        self.__from105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionType106"):
                    opp_val = getattr(item, "TransitionType106", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionType106"):
                    opp_val = getattr(item, "TransitionType106", None)
                    
                    setattr(item, "TransitionType106", self)
                    

    @property
    def ActivityType295(self):
        return self.__ActivityType295

    @ActivityType295.setter
    def ActivityType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType295", None)
        self.__ActivityType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "implementationProcess"):
                opp_val = getattr(old_value, "implementationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "implementationProcess"):
                opp_val = getattr(value, "implementationProcess", None)
                if opp_val is None:
                    setattr(value, "implementationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def performedActivities(self):
        return self.__performedActivities

    @performedActivities.setter
    def performedActivities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__performedActivities", None)
        self.__performedActivities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IModelParticipant96"):
                opp_val = getattr(old_value, "IModelParticipant96", None)
                if opp_val == self:
                    setattr(old_value, "IModelParticipant96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IModelParticipant96"):
                opp_val = getattr(value, "IModelParticipant96", None)
                setattr(value, "IModelParticipant96", self)

    @property
    def carnot_ActivityType108(self):
        return self.__carnot_ActivityType108

    @carnot_ActivityType108.setter
    def carnot_ActivityType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__carnot_ActivityType108", None)
        self.__carnot_ActivityType108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_Code"):
                    opp_val = getattr(item, "carnot_Code", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_Code", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_Code"):
                    opp_val = getattr(item, "carnot_Code", None)
                    
                    setattr(item, "carnot_Code", self)
                    

    @property
    def ActivityType83(self):
        return self.__ActivityType83

    @ActivityType83.setter
    def ActivityType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__ActivityType83", None)
        self.__ActivityType83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitySymbols"):
                opp_val = getattr(old_value, "activitySymbols", None)
                if opp_val == self:
                    setattr(old_value, "activitySymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitySymbols"):
                opp_val = getattr(value, "activitySymbols", None)
                setattr(value, "activitySymbols", self)

    @property
    def carnot_ActivityType(self):
        return self.__carnot_ActivityType

    @carnot_ActivityType.setter
    def carnot_ActivityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ActivityType__carnot_ActivityType", None)
        self.__carnot_ActivityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataMappingType"):
                    opp_val = getattr(item, "carnot_DataMappingType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataMappingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataMappingType"):
                    opp_val = getattr(item, "carnot_DataMappingType", None)
                    
                    setattr(item, "carnot_DataMappingType", self)
                    

class carnot_ProcessDefinitionType(IdRefOwner, IEventHandlerOwner, IIdentifiableModelElement):

    def __init__(self, defaultPriority: str, ProcessDefinitionType: "carnot_ActivityType" = None, carnot_ProcessDefinitionType: "carnot_ModelType" = None, carnot_ProcessDefinitionType288: set["carnot_TriggerType"] = None, carnot_ProcessDefinitionType290: set["carnot_DataPathType"] = None, carnot_ProcessDefinitionType292: set["carnot_DiagramType"] = None, carnot_ProcessDefinitionType279: "carnot_PoolSymbol" = None, carnot_ProcessDefinitionType283: set["carnot_ActivityType"] = None, carnot_ProcessDefinitionType286: set["carnot_TransitionType"] = None, implementationProcess: set["carnot_ActivityType"] = None, process: set["carnot_ProcessSymbolType"] = None, carnot_ProcessDefinitionType298: "carnot_FormalParametersType" = None, carnot_ProcessDefinitionType300: "FormalParameterMappingsType" = None, ProcessDefinitionType302: "carnot_ProcessSymbolType" = None):
        self.defaultPriority = defaultPriority
        self.ProcessDefinitionType = ProcessDefinitionType
        self.carnot_ProcessDefinitionType = carnot_ProcessDefinitionType
        self.carnot_ProcessDefinitionType288 = carnot_ProcessDefinitionType288 if carnot_ProcessDefinitionType288 is not None else set()
        self.carnot_ProcessDefinitionType290 = carnot_ProcessDefinitionType290 if carnot_ProcessDefinitionType290 is not None else set()
        self.carnot_ProcessDefinitionType292 = carnot_ProcessDefinitionType292 if carnot_ProcessDefinitionType292 is not None else set()
        self.carnot_ProcessDefinitionType279 = carnot_ProcessDefinitionType279
        self.carnot_ProcessDefinitionType283 = carnot_ProcessDefinitionType283 if carnot_ProcessDefinitionType283 is not None else set()
        self.carnot_ProcessDefinitionType286 = carnot_ProcessDefinitionType286 if carnot_ProcessDefinitionType286 is not None else set()
        self.implementationProcess = implementationProcess if implementationProcess is not None else set()
        self.process = process if process is not None else set()
        self.carnot_ProcessDefinitionType298 = carnot_ProcessDefinitionType298
        self.carnot_ProcessDefinitionType300 = carnot_ProcessDefinitionType300
        self.ProcessDefinitionType302 = ProcessDefinitionType302
        
    @property
    def defaultPriority(self) -> str:
        return self.__defaultPriority

    @defaultPriority.setter
    def defaultPriority(self, defaultPriority: str):
        self.__defaultPriority = defaultPriority

    @property
    def carnot_ProcessDefinitionType290(self):
        return self.__carnot_ProcessDefinitionType290

    @carnot_ProcessDefinitionType290.setter
    def carnot_ProcessDefinitionType290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType290", None)
        self.__carnot_ProcessDefinitionType290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataPathType"):
                    opp_val = getattr(item, "carnot_DataPathType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataPathType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataPathType"):
                    opp_val = getattr(item, "carnot_DataPathType", None)
                    
                    setattr(item, "carnot_DataPathType", self)
                    

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__process", None)
        self.__process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcessSymbolType"):
                    opp_val = getattr(item, "ProcessSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessSymbolType"):
                    opp_val = getattr(item, "ProcessSymbolType", None)
                    
                    setattr(item, "ProcessSymbolType", self)
                    

    @property
    def carnot_ProcessDefinitionType292(self):
        return self.__carnot_ProcessDefinitionType292

    @carnot_ProcessDefinitionType292.setter
    def carnot_ProcessDefinitionType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType292", None)
        self.__carnot_ProcessDefinitionType292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DiagramType293"):
                    opp_val = getattr(item, "carnot_DiagramType293", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DiagramType293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DiagramType293"):
                    opp_val = getattr(item, "carnot_DiagramType293", None)
                    
                    setattr(item, "carnot_DiagramType293", self)
                    

    @property
    def ProcessDefinitionType302(self):
        return self.__ProcessDefinitionType302

    @ProcessDefinitionType302.setter
    def ProcessDefinitionType302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__ProcessDefinitionType302", None)
        self.__ProcessDefinitionType302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processSymbols"):
                opp_val = getattr(old_value, "processSymbols", None)
                if opp_val == self:
                    setattr(old_value, "processSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processSymbols"):
                opp_val = getattr(value, "processSymbols", None)
                setattr(value, "processSymbols", self)

    @property
    def carnot_ProcessDefinitionType283(self):
        return self.__carnot_ProcessDefinitionType283

    @carnot_ProcessDefinitionType283.setter
    def carnot_ProcessDefinitionType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType283", None)
        self.__carnot_ProcessDefinitionType283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ActivityType284"):
                    opp_val = getattr(item, "carnot_ActivityType284", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ActivityType284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ActivityType284"):
                    opp_val = getattr(item, "carnot_ActivityType284", None)
                    
                    setattr(item, "carnot_ActivityType284", self)
                    

    @property
    def carnot_ProcessDefinitionType298(self):
        return self.__carnot_ProcessDefinitionType298

    @carnot_ProcessDefinitionType298.setter
    def carnot_ProcessDefinitionType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType298", None)
        self.__carnot_ProcessDefinitionType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_FormalParametersType"):
                opp_val = getattr(old_value, "carnot_FormalParametersType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_FormalParametersType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_FormalParametersType"):
                opp_val = getattr(value, "carnot_FormalParametersType", None)
                setattr(value, "carnot_FormalParametersType", self)

    @property
    def carnot_ProcessDefinitionType279(self):
        return self.__carnot_ProcessDefinitionType279

    @carnot_ProcessDefinitionType279.setter
    def carnot_ProcessDefinitionType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType279", None)
        self.__carnot_ProcessDefinitionType279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_PoolSymbol"):
                opp_val = getattr(old_value, "carnot_PoolSymbol", None)
                if opp_val == self:
                    setattr(old_value, "carnot_PoolSymbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_PoolSymbol"):
                opp_val = getattr(value, "carnot_PoolSymbol", None)
                setattr(value, "carnot_PoolSymbol", self)

    @property
    def implementationProcess(self):
        return self.__implementationProcess

    @implementationProcess.setter
    def implementationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__implementationProcess", None)
        self.__implementationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityType295"):
                    opp_val = getattr(item, "ActivityType295", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityType295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityType295"):
                    opp_val = getattr(item, "ActivityType295", None)
                    
                    setattr(item, "ActivityType295", self)
                    

    @property
    def ProcessDefinitionType(self):
        return self.__ProcessDefinitionType

    @ProcessDefinitionType.setter
    def ProcessDefinitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__ProcessDefinitionType", None)
        self.__ProcessDefinitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executingActivities"):
                opp_val = getattr(old_value, "executingActivities", None)
                if opp_val == self:
                    setattr(old_value, "executingActivities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executingActivities"):
                opp_val = getattr(value, "executingActivities", None)
                setattr(value, "executingActivities", self)

    @property
    def carnot_ProcessDefinitionType286(self):
        return self.__carnot_ProcessDefinitionType286

    @carnot_ProcessDefinitionType286.setter
    def carnot_ProcessDefinitionType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType286", None)
        self.__carnot_ProcessDefinitionType286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TransitionType"):
                    opp_val = getattr(item, "carnot_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TransitionType"):
                    opp_val = getattr(item, "carnot_TransitionType", None)
                    
                    setattr(item, "carnot_TransitionType", self)
                    

    @property
    def carnot_ProcessDefinitionType288(self):
        return self.__carnot_ProcessDefinitionType288

    @carnot_ProcessDefinitionType288.setter
    def carnot_ProcessDefinitionType288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType288", None)
        self.__carnot_ProcessDefinitionType288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TriggerType"):
                    opp_val = getattr(item, "carnot_TriggerType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TriggerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TriggerType"):
                    opp_val = getattr(item, "carnot_TriggerType", None)
                    
                    setattr(item, "carnot_TriggerType", self)
                    

    @property
    def carnot_ProcessDefinitionType300(self):
        return self.__carnot_ProcessDefinitionType300

    @carnot_ProcessDefinitionType300.setter
    def carnot_ProcessDefinitionType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType300", None)
        self.__carnot_ProcessDefinitionType300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FormalParameterMappingsType"):
                opp_val = getattr(old_value, "FormalParameterMappingsType", None)
                if opp_val == self:
                    setattr(old_value, "FormalParameterMappingsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FormalParameterMappingsType"):
                opp_val = getattr(value, "FormalParameterMappingsType", None)
                setattr(value, "FormalParameterMappingsType", self)

    @property
    def carnot_ProcessDefinitionType(self):
        return self.__carnot_ProcessDefinitionType

    @carnot_ProcessDefinitionType.setter
    def carnot_ProcessDefinitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ProcessDefinitionType__carnot_ProcessDefinitionType", None)
        self.__carnot_ProcessDefinitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType241"):
                opp_val = getattr(old_value, "carnot_ModelType241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType241"):
                opp_val = getattr(value, "carnot_ModelType241", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_ApplicationType(IAccessPointOwner, ITypedElement, IIdentifiableModelElement):

    def __init__(self, interactive: str, ApplicationType: "carnot_ActivityType" = None, ApplicationType117: "carnot_ApplicationSymbolType" = None, carnot_ApplicationType: set["carnot_ContextType"] = None, applications: "carnot_ApplicationTypeType" = None, application: set["carnot_ActivityType"] = None, application123: set["carnot_ApplicationSymbolType"] = None, ApplicationType126: "carnot_ApplicationTypeType" = None, carnot_ApplicationType229: "carnot_ModelType" = None):
        self.interactive = interactive
        self.ApplicationType = ApplicationType
        self.ApplicationType117 = ApplicationType117
        self.carnot_ApplicationType = carnot_ApplicationType if carnot_ApplicationType is not None else set()
        self.applications = applications
        self.application = application if application is not None else set()
        self.application123 = application123 if application123 is not None else set()
        self.ApplicationType126 = ApplicationType126
        self.carnot_ApplicationType229 = carnot_ApplicationType229
        
    @property
    def interactive(self) -> str:
        return self.__interactive

    @interactive.setter
    def interactive(self, interactive: str):
        self.__interactive = interactive

    @property
    def ApplicationType(self):
        return self.__ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__ApplicationType", None)
        self.__ApplicationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executedActivities"):
                opp_val = getattr(old_value, "executedActivities", None)
                if opp_val == self:
                    setattr(old_value, "executedActivities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executedActivities"):
                opp_val = getattr(value, "executedActivities", None)
                setattr(value, "executedActivities", self)

    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__application", None)
        self.__application = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityType121"):
                    opp_val = getattr(item, "ActivityType121", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityType121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityType121"):
                    opp_val = getattr(item, "ActivityType121", None)
                    
                    setattr(item, "ActivityType121", self)
                    

    @property
    def carnot_ApplicationType(self):
        return self.__carnot_ApplicationType

    @carnot_ApplicationType.setter
    def carnot_ApplicationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__carnot_ApplicationType", None)
        self.__carnot_ApplicationType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ContextType"):
                    opp_val = getattr(item, "carnot_ContextType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ContextType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ContextType"):
                    opp_val = getattr(item, "carnot_ContextType", None)
                    
                    setattr(item, "carnot_ContextType", self)
                    

    @property
    def ApplicationType126(self):
        return self.__ApplicationType126

    @ApplicationType126.setter
    def ApplicationType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__ApplicationType126", None)
        self.__ApplicationType126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type125"):
                opp_val = getattr(old_value, "type125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type125"):
                opp_val = getattr(value, "type125", None)
                if opp_val is None:
                    setattr(value, "type125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ApplicationType117(self):
        return self.__ApplicationType117

    @ApplicationType117.setter
    def ApplicationType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__ApplicationType117", None)
        self.__ApplicationType117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicationSymbols"):
                opp_val = getattr(old_value, "applicationSymbols", None)
                if opp_val == self:
                    setattr(old_value, "applicationSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicationSymbols"):
                opp_val = getattr(value, "applicationSymbols", None)
                setattr(value, "applicationSymbols", self)

    @property
    def carnot_ApplicationType229(self):
        return self.__carnot_ApplicationType229

    @carnot_ApplicationType229.setter
    def carnot_ApplicationType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__carnot_ApplicationType229", None)
        self.__carnot_ApplicationType229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType228"):
                opp_val = getattr(old_value, "carnot_ModelType228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType228"):
                opp_val = getattr(value, "carnot_ModelType228", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applications(self):
        return self.__applications

    @applications.setter
    def applications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__applications", None)
        self.__applications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ApplicationTypeType"):
                opp_val = getattr(old_value, "ApplicationTypeType", None)
                if opp_val == self:
                    setattr(old_value, "ApplicationTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ApplicationTypeType"):
                opp_val = getattr(value, "ApplicationTypeType", None)
                setattr(value, "ApplicationTypeType", self)

    @property
    def application123(self):
        return self.__application123

    @application123.setter
    def application123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ApplicationType__application123", None)
        self.__application123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationSymbolType"):
                    opp_val = getattr(item, "ApplicationSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationSymbolType"):
                    opp_val = getattr(item, "ApplicationSymbolType", None)
                    
                    setattr(item, "ApplicationSymbolType", self)
                    

class carnot_AbstractEventAction(ITypedElement, IIdentifiableModelElement):

    pass
class carnot_IModelParticipant(IIdentifiableModelElement):

    pass
class carnot_TransitionType(IIdentifiableModelElement):

    def __init__(self, condition: str, forkOnTraversal: str, TransitionType: "carnot_ActivityType" = None, TransitionType106: "carnot_ActivityType" = None, carnot_TransitionType: "carnot_ProcessDefinitionType" = None, carnot_TransitionType344: "carnot_XmlTextNode" = None, outTransitions347: "carnot_ActivityType" = None, TransitionType342: "carnot_TransitionConnectionType" = None, inTransitions350: "carnot_ActivityType" = None, transition: set["carnot_TransitionConnectionType"] = None):
        self.condition = condition
        self.forkOnTraversal = forkOnTraversal
        self.TransitionType = TransitionType
        self.TransitionType106 = TransitionType106
        self.carnot_TransitionType = carnot_TransitionType
        self.carnot_TransitionType344 = carnot_TransitionType344
        self.outTransitions347 = outTransitions347
        self.TransitionType342 = TransitionType342
        self.inTransitions350 = inTransitions350
        self.transition = transition if transition is not None else set()
        
    @property
    def forkOnTraversal(self) -> str:
        return self.__forkOnTraversal

    @forkOnTraversal.setter
    def forkOnTraversal(self, forkOnTraversal: str):
        self.__forkOnTraversal = forkOnTraversal

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def TransitionType(self):
        return self.__TransitionType

    @TransitionType.setter
    def TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__TransitionType", None)
        self.__TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to103"):
                opp_val = getattr(old_value, "to103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to103"):
                opp_val = getattr(value, "to103", None)
                if opp_val is None:
                    setattr(value, "to103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inTransitions350(self):
        return self.__inTransitions350

    @inTransitions350.setter
    def inTransitions350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__inTransitions350", None)
        self.__inTransitions350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityType351"):
                opp_val = getattr(old_value, "ActivityType351", None)
                if opp_val == self:
                    setattr(old_value, "ActivityType351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityType351"):
                opp_val = getattr(value, "ActivityType351", None)
                setattr(value, "ActivityType351", self)

    @property
    def carnot_TransitionType(self):
        return self.__carnot_TransitionType

    @carnot_TransitionType.setter
    def carnot_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__carnot_TransitionType", None)
        self.__carnot_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ProcessDefinitionType286"):
                opp_val = getattr(old_value, "carnot_ProcessDefinitionType286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ProcessDefinitionType286"):
                opp_val = getattr(value, "carnot_ProcessDefinitionType286", None)
                if opp_val is None:
                    setattr(value, "carnot_ProcessDefinitionType286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__transition", None)
        self.__transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionConnectionType353"):
                    opp_val = getattr(item, "TransitionConnectionType353", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionConnectionType353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionConnectionType353"):
                    opp_val = getattr(item, "TransitionConnectionType353", None)
                    
                    setattr(item, "TransitionConnectionType353", self)
                    

    @property
    def TransitionType342(self):
        return self.__TransitionType342

    @TransitionType342.setter
    def TransitionType342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__TransitionType342", None)
        self.__TransitionType342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitionConnections"):
                opp_val = getattr(old_value, "transitionConnections", None)
                if opp_val == self:
                    setattr(old_value, "transitionConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitionConnections"):
                opp_val = getattr(value, "transitionConnections", None)
                setattr(value, "transitionConnections", self)

    @property
    def carnot_TransitionType344(self):
        return self.__carnot_TransitionType344

    @carnot_TransitionType344.setter
    def carnot_TransitionType344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__carnot_TransitionType344", None)
        self.__carnot_TransitionType344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_XmlTextNode345"):
                opp_val = getattr(old_value, "carnot_XmlTextNode345", None)
                if opp_val == self:
                    setattr(old_value, "carnot_XmlTextNode345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_XmlTextNode345"):
                opp_val = getattr(value, "carnot_XmlTextNode345", None)
                setattr(value, "carnot_XmlTextNode345", self)

    @property
    def outTransitions347(self):
        return self.__outTransitions347

    @outTransitions347.setter
    def outTransitions347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__outTransitions347", None)
        self.__outTransitions347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityType348"):
                opp_val = getattr(old_value, "ActivityType348", None)
                if opp_val == self:
                    setattr(old_value, "ActivityType348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityType348"):
                opp_val = getattr(value, "ActivityType348", None)
                setattr(value, "ActivityType348", self)

    @property
    def TransitionType106(self):
        return self.__TransitionType106

    @TransitionType106.setter
    def TransitionType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_TransitionType__TransitionType106", None)
        self.__TransitionType106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from105"):
                opp_val = getattr(old_value, "from105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from105"):
                opp_val = getattr(value, "from105", None)
                if opp_val is None:
                    setattr(value, "from105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_TriggerType(IAccessPointOwner, ITypedElement, IIdentifiableModelElement):

    pass
class carnot_IMetaType(IIdentifiableModelElement):

    def __init__(self, isPredefined: str):
        self.isPredefined = isPredefined
        
    @property
    def isPredefined(self) -> str:
        return self.__isPredefined

    @isPredefined.setter
    def isPredefined(self, isPredefined: str):
        self.__isPredefined = isPredefined

    def getExtensionPointId(self) -> str:
        # TODO: Implement getExtensionPointId method
        pass

    def getTypedElements(self):
        # TODO: Implement getTypedElements method
        pass

class carnot_AccessPointType(ITypedElement, IIdentifiableModelElement):

    def __init__(self, direction: str, carnot_AccessPointType: "carnot_IAccessPointOwner" = None, carnot_AccessPointType81: "carnot_DataTypeType" = None):
        self.direction = direction
        self.carnot_AccessPointType = carnot_AccessPointType
        self.carnot_AccessPointType81 = carnot_AccessPointType81
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def carnot_AccessPointType(self):
        return self.__carnot_AccessPointType

    @carnot_AccessPointType.setter
    def carnot_AccessPointType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AccessPointType__carnot_AccessPointType", None)
        self.__carnot_AccessPointType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IAccessPointOwner"):
                opp_val = getattr(old_value, "carnot_IAccessPointOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IAccessPointOwner"):
                opp_val = getattr(value, "carnot_IAccessPointOwner", None)
                if opp_val is None:
                    setattr(value, "carnot_IAccessPointOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_AccessPointType81(self):
        return self.__carnot_AccessPointType81

    @carnot_AccessPointType81.setter
    def carnot_AccessPointType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AccessPointType__carnot_AccessPointType81", None)
        self.__carnot_AccessPointType81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_DataTypeType"):
                opp_val = getattr(old_value, "carnot_DataTypeType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_DataTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_DataTypeType"):
                opp_val = getattr(value, "carnot_DataTypeType", None)
                setattr(value, "carnot_DataTypeType", self)

class carnot_IAccessPointOwner(ABC):

    pass
class carnot_EventHandlerType(IAccessPointOwner, ITypedElement, IIdentifiableModelElement):

    def __init__(self, autoBind: str, consumeOnMatch: str, logHandler: str, unbindOnMatch: str, carnot_EventHandlerType: "carnot_IEventHandlerOwner" = None, EventHandlerType: "carnot_EventConditionTypeType" = None, carnot_EventHandlerType180: set["carnot_BindActionType"] = None, carnot_EventHandlerType182: set["carnot_EventActionType"] = None, carnot_EventHandlerType184: set["carnot_UnbindActionType"] = None, eventHandlers: "carnot_EventConditionTypeType" = None):
        self.autoBind = autoBind
        self.consumeOnMatch = consumeOnMatch
        self.logHandler = logHandler
        self.unbindOnMatch = unbindOnMatch
        self.carnot_EventHandlerType = carnot_EventHandlerType
        self.EventHandlerType = EventHandlerType
        self.carnot_EventHandlerType180 = carnot_EventHandlerType180 if carnot_EventHandlerType180 is not None else set()
        self.carnot_EventHandlerType182 = carnot_EventHandlerType182 if carnot_EventHandlerType182 is not None else set()
        self.carnot_EventHandlerType184 = carnot_EventHandlerType184 if carnot_EventHandlerType184 is not None else set()
        self.eventHandlers = eventHandlers
        
    @property
    def unbindOnMatch(self) -> str:
        return self.__unbindOnMatch

    @unbindOnMatch.setter
    def unbindOnMatch(self, unbindOnMatch: str):
        self.__unbindOnMatch = unbindOnMatch

    @property
    def logHandler(self) -> str:
        return self.__logHandler

    @logHandler.setter
    def logHandler(self, logHandler: str):
        self.__logHandler = logHandler

    @property
    def consumeOnMatch(self) -> str:
        return self.__consumeOnMatch

    @consumeOnMatch.setter
    def consumeOnMatch(self, consumeOnMatch: str):
        self.__consumeOnMatch = consumeOnMatch

    @property
    def autoBind(self) -> str:
        return self.__autoBind

    @autoBind.setter
    def autoBind(self, autoBind: str):
        self.__autoBind = autoBind

    @property
    def carnot_EventHandlerType184(self):
        return self.__carnot_EventHandlerType184

    @carnot_EventHandlerType184.setter
    def carnot_EventHandlerType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__carnot_EventHandlerType184", None)
        self.__carnot_EventHandlerType184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_UnbindActionType"):
                    opp_val = getattr(item, "carnot_UnbindActionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_UnbindActionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_UnbindActionType"):
                    opp_val = getattr(item, "carnot_UnbindActionType", None)
                    
                    setattr(item, "carnot_UnbindActionType", self)
                    

    @property
    def EventHandlerType(self):
        return self.__EventHandlerType

    @EventHandlerType.setter
    def EventHandlerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__EventHandlerType", None)
        self.__EventHandlerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type178"):
                opp_val = getattr(old_value, "type178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type178"):
                opp_val = getattr(value, "type178", None)
                if opp_val is None:
                    setattr(value, "type178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_EventHandlerType182(self):
        return self.__carnot_EventHandlerType182

    @carnot_EventHandlerType182.setter
    def carnot_EventHandlerType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__carnot_EventHandlerType182", None)
        self.__carnot_EventHandlerType182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EventActionType"):
                    opp_val = getattr(item, "carnot_EventActionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EventActionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EventActionType"):
                    opp_val = getattr(item, "carnot_EventActionType", None)
                    
                    setattr(item, "carnot_EventActionType", self)
                    

    @property
    def carnot_EventHandlerType(self):
        return self.__carnot_EventHandlerType

    @carnot_EventHandlerType.setter
    def carnot_EventHandlerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__carnot_EventHandlerType", None)
        self.__carnot_EventHandlerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IEventHandlerOwner"):
                opp_val = getattr(old_value, "carnot_IEventHandlerOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IEventHandlerOwner"):
                opp_val = getattr(value, "carnot_IEventHandlerOwner", None)
                if opp_val is None:
                    setattr(value, "carnot_IEventHandlerOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eventHandlers(self):
        return self.__eventHandlers

    @eventHandlers.setter
    def eventHandlers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__eventHandlers", None)
        self.__eventHandlers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventConditionTypeType"):
                opp_val = getattr(old_value, "EventConditionTypeType", None)
                if opp_val == self:
                    setattr(old_value, "EventConditionTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventConditionTypeType"):
                opp_val = getattr(value, "EventConditionTypeType", None)
                setattr(value, "EventConditionTypeType", self)

    @property
    def carnot_EventHandlerType180(self):
        return self.__carnot_EventHandlerType180

    @carnot_EventHandlerType180.setter
    def carnot_EventHandlerType180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_EventHandlerType__carnot_EventHandlerType180", None)
        self.__carnot_EventHandlerType180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_BindActionType"):
                    opp_val = getattr(item, "carnot_BindActionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_BindActionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_BindActionType"):
                    opp_val = getattr(item, "carnot_BindActionType", None)
                    
                    setattr(item, "carnot_BindActionType", self)
                    

class carnot_IEventHandlerOwner(ABC):

    pass
class carnot_DescriptionType:

    def __init__(self, mixed: str, carnot_DescriptionType: "carnot_IIdentifiableModelElement" = None, carnot_DescriptionType136: "carnot_ContextType" = None, carnot_DescriptionType210: "carnot_ModelType" = None, carnot_DescriptionType369: "carnot_ViewType" = None):
        self.mixed = mixed
        self.carnot_DescriptionType = carnot_DescriptionType
        self.carnot_DescriptionType136 = carnot_DescriptionType136
        self.carnot_DescriptionType210 = carnot_DescriptionType210
        self.carnot_DescriptionType369 = carnot_DescriptionType369
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def carnot_DescriptionType210(self):
        return self.__carnot_DescriptionType210

    @carnot_DescriptionType210.setter
    def carnot_DescriptionType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DescriptionType__carnot_DescriptionType210", None)
        self.__carnot_DescriptionType210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType209"):
                opp_val = getattr(old_value, "carnot_ModelType209", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ModelType209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType209"):
                opp_val = getattr(value, "carnot_ModelType209", None)
                setattr(value, "carnot_ModelType209", self)

    @property
    def carnot_DescriptionType369(self):
        return self.__carnot_DescriptionType369

    @carnot_DescriptionType369.setter
    def carnot_DescriptionType369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DescriptionType__carnot_DescriptionType369", None)
        self.__carnot_DescriptionType369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ViewType368"):
                opp_val = getattr(old_value, "carnot_ViewType368", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ViewType368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ViewType368"):
                opp_val = getattr(value, "carnot_ViewType368", None)
                setattr(value, "carnot_ViewType368", self)

    @property
    def carnot_DescriptionType136(self):
        return self.__carnot_DescriptionType136

    @carnot_DescriptionType136.setter
    def carnot_DescriptionType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DescriptionType__carnot_DescriptionType136", None)
        self.__carnot_DescriptionType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ContextType135"):
                opp_val = getattr(old_value, "carnot_ContextType135", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ContextType135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ContextType135"):
                opp_val = getattr(value, "carnot_ContextType135", None)
                setattr(value, "carnot_ContextType135", self)

    @property
    def carnot_DescriptionType(self):
        return self.__carnot_DescriptionType

    @carnot_DescriptionType.setter
    def carnot_DescriptionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DescriptionType__carnot_DescriptionType", None)
        self.__carnot_DescriptionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IIdentifiableModelElement"):
                opp_val = getattr(old_value, "carnot_IIdentifiableModelElement", None)
                if opp_val == self:
                    setattr(old_value, "carnot_IIdentifiableModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IIdentifiableModelElement"):
                opp_val = getattr(value, "carnot_IIdentifiableModelElement", None)
                setattr(value, "carnot_IIdentifiableModelElement", self)

class IExtensibleElement:

    pass
class carnot_LinkTypeType(IMetaType, IExtensibleElement):

    def __init__(self, sourceClass: str, sourceCardinality: str, sourceRole: str, targetCardinality: str, lineStyle: str, lineColor: str, targetRole: str, targetClass: str, sourceSymbol: str, targetSymbol: str, showRoleNames: str, showLinkTypeName: str, LinkTypeType: "carnot_GenericLinkConnectionType" = None, linkType: set["carnot_GenericLinkConnectionType"] = None, carnot_LinkTypeType: "carnot_ModelType" = None):
        self.sourceClass = sourceClass
        self.sourceCardinality = sourceCardinality
        self.sourceRole = sourceRole
        self.targetCardinality = targetCardinality
        self.lineStyle = lineStyle
        self.lineColor = lineColor
        self.targetRole = targetRole
        self.targetClass = targetClass
        self.sourceSymbol = sourceSymbol
        self.targetSymbol = targetSymbol
        self.showRoleNames = showRoleNames
        self.showLinkTypeName = showLinkTypeName
        self.LinkTypeType = LinkTypeType
        self.linkType = linkType if linkType is not None else set()
        self.carnot_LinkTypeType = carnot_LinkTypeType
        
    @property
    def targetCardinality(self) -> str:
        return self.__targetCardinality

    @targetCardinality.setter
    def targetCardinality(self, targetCardinality: str):
        self.__targetCardinality = targetCardinality

    @property
    def showLinkTypeName(self) -> str:
        return self.__showLinkTypeName

    @showLinkTypeName.setter
    def showLinkTypeName(self, showLinkTypeName: str):
        self.__showLinkTypeName = showLinkTypeName

    @property
    def sourceCardinality(self) -> str:
        return self.__sourceCardinality

    @sourceCardinality.setter
    def sourceCardinality(self, sourceCardinality: str):
        self.__sourceCardinality = sourceCardinality

    @property
    def targetClass(self) -> str:
        return self.__targetClass

    @targetClass.setter
    def targetClass(self, targetClass: str):
        self.__targetClass = targetClass

    @property
    def targetSymbol(self) -> str:
        return self.__targetSymbol

    @targetSymbol.setter
    def targetSymbol(self, targetSymbol: str):
        self.__targetSymbol = targetSymbol

    @property
    def sourceRole(self) -> str:
        return self.__sourceRole

    @sourceRole.setter
    def sourceRole(self, sourceRole: str):
        self.__sourceRole = sourceRole

    @property
    def sourceSymbol(self) -> str:
        return self.__sourceSymbol

    @sourceSymbol.setter
    def sourceSymbol(self, sourceSymbol: str):
        self.__sourceSymbol = sourceSymbol

    @property
    def showRoleNames(self) -> str:
        return self.__showRoleNames

    @showRoleNames.setter
    def showRoleNames(self, showRoleNames: str):
        self.__showRoleNames = showRoleNames

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def lineColor(self) -> str:
        return self.__lineColor

    @lineColor.setter
    def lineColor(self, lineColor: str):
        self.__lineColor = lineColor

    @property
    def sourceClass(self) -> str:
        return self.__sourceClass

    @sourceClass.setter
    def sourceClass(self, sourceClass: str):
        self.__sourceClass = sourceClass

    @property
    def targetRole(self) -> str:
        return self.__targetRole

    @targetRole.setter
    def targetRole(self, targetRole: str):
        self.__targetRole = targetRole

    @property
    def LinkTypeType(self):
        return self.__LinkTypeType

    @LinkTypeType.setter
    def LinkTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_LinkTypeType__LinkTypeType", None)
        self.__LinkTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkInstances"):
                opp_val = getattr(old_value, "linkInstances", None)
                if opp_val == self:
                    setattr(old_value, "linkInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkInstances"):
                opp_val = getattr(value, "linkInstances", None)
                setattr(value, "linkInstances", self)

    @property
    def carnot_LinkTypeType(self):
        return self.__carnot_LinkTypeType

    @carnot_LinkTypeType.setter
    def carnot_LinkTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_LinkTypeType__carnot_LinkTypeType", None)
        self.__carnot_LinkTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType251"):
                opp_val = getattr(old_value, "carnot_ModelType251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType251"):
                opp_val = getattr(value, "carnot_ModelType251", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linkType(self):
        return self.__linkType

    @linkType.setter
    def linkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_LinkTypeType__linkType", None)
        self.__linkType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GenericLinkConnectionType205"):
                    opp_val = getattr(item, "GenericLinkConnectionType205", None)
                    
                    if opp_val == self:
                        setattr(item, "GenericLinkConnectionType205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GenericLinkConnectionType205"):
                    opp_val = getattr(item, "GenericLinkConnectionType205", None)
                    
                    setattr(item, "GenericLinkConnectionType205", self)
                    

class carnot_ISymbolContainer(IExtensibleElement):

    def __init__(self, nodes: str, connections: str, carnot_ISymbolContainer: set["carnot_ActivitySymbolType"] = None, carnot_ISymbolContainer8: set["carnot_AnnotationSymbolType"] = None, carnot_ISymbolContainer10: set["carnot_ApplicationSymbolType"] = None, carnot_ISymbolContainer12: set["carnot_ConditionalPerformerSymbolType"] = None, carnot_ISymbolContainer14: set["carnot_DataSymbolType"] = None, carnot_ISymbolContainer16: set["carnot_EndEventSymbol"] = None, carnot_ISymbolContainer18: set["carnot_GatewaySymbol"] = None, carnot_ISymbolContainer20: set["carnot_GroupSymbolType"] = None, carnot_ISymbolContainer22: set["carnot_IntermediateEventSymbol"] = None, carnot_ISymbolContainer24: set["carnot_ModelerSymbolType"] = None, carnot_ISymbolContainer26: set["carnot_OrganizationSymbolType"] = None, carnot_ISymbolContainer28: set["carnot_ProcessSymbolType"] = None, carnot_ISymbolContainer30: set["carnot_PublicInterfaceSymbol"] = None, carnot_ISymbolContainer32: set["carnot_RoleSymbolType"] = None, carnot_ISymbolContainer34: set["carnot_StartEventSymbol"] = None, carnot_ISymbolContainer36: set["carnot_TextSymbolType"] = None, carnot_ISymbolContainer38: set["carnot_DataMappingConnectionType"] = None, carnot_ISymbolContainer40: set["carnot_ExecutedByConnectionType"] = None, carnot_ISymbolContainer42: set["carnot_GenericLinkConnectionType"] = None, carnot_ISymbolContainer44: set["carnot_PartOfConnectionType"] = None, carnot_ISymbolContainer46: set["carnot_PerformsConnectionType"] = None, carnot_ISymbolContainer48: set["carnot_TriggersConnectionType"] = None, carnot_ISymbolContainer50: set["carnot_RefersToConnectionType"] = None, carnot_ISymbolContainer52: set["carnot_SubProcessOfConnectionType"] = None, carnot_ISymbolContainer54: set["carnot_TransitionConnectionType"] = None, carnot_ISymbolContainer56: set["carnot_WorksForConnectionType"] = None, carnot_ISymbolContainer58: set["carnot_TeamLeadConnectionType"] = None):
        self.nodes = nodes
        self.connections = connections
        self.carnot_ISymbolContainer = carnot_ISymbolContainer if carnot_ISymbolContainer is not None else set()
        self.carnot_ISymbolContainer8 = carnot_ISymbolContainer8 if carnot_ISymbolContainer8 is not None else set()
        self.carnot_ISymbolContainer10 = carnot_ISymbolContainer10 if carnot_ISymbolContainer10 is not None else set()
        self.carnot_ISymbolContainer12 = carnot_ISymbolContainer12 if carnot_ISymbolContainer12 is not None else set()
        self.carnot_ISymbolContainer14 = carnot_ISymbolContainer14 if carnot_ISymbolContainer14 is not None else set()
        self.carnot_ISymbolContainer16 = carnot_ISymbolContainer16 if carnot_ISymbolContainer16 is not None else set()
        self.carnot_ISymbolContainer18 = carnot_ISymbolContainer18 if carnot_ISymbolContainer18 is not None else set()
        self.carnot_ISymbolContainer20 = carnot_ISymbolContainer20 if carnot_ISymbolContainer20 is not None else set()
        self.carnot_ISymbolContainer22 = carnot_ISymbolContainer22 if carnot_ISymbolContainer22 is not None else set()
        self.carnot_ISymbolContainer24 = carnot_ISymbolContainer24 if carnot_ISymbolContainer24 is not None else set()
        self.carnot_ISymbolContainer26 = carnot_ISymbolContainer26 if carnot_ISymbolContainer26 is not None else set()
        self.carnot_ISymbolContainer28 = carnot_ISymbolContainer28 if carnot_ISymbolContainer28 is not None else set()
        self.carnot_ISymbolContainer30 = carnot_ISymbolContainer30 if carnot_ISymbolContainer30 is not None else set()
        self.carnot_ISymbolContainer32 = carnot_ISymbolContainer32 if carnot_ISymbolContainer32 is not None else set()
        self.carnot_ISymbolContainer34 = carnot_ISymbolContainer34 if carnot_ISymbolContainer34 is not None else set()
        self.carnot_ISymbolContainer36 = carnot_ISymbolContainer36 if carnot_ISymbolContainer36 is not None else set()
        self.carnot_ISymbolContainer38 = carnot_ISymbolContainer38 if carnot_ISymbolContainer38 is not None else set()
        self.carnot_ISymbolContainer40 = carnot_ISymbolContainer40 if carnot_ISymbolContainer40 is not None else set()
        self.carnot_ISymbolContainer42 = carnot_ISymbolContainer42 if carnot_ISymbolContainer42 is not None else set()
        self.carnot_ISymbolContainer44 = carnot_ISymbolContainer44 if carnot_ISymbolContainer44 is not None else set()
        self.carnot_ISymbolContainer46 = carnot_ISymbolContainer46 if carnot_ISymbolContainer46 is not None else set()
        self.carnot_ISymbolContainer48 = carnot_ISymbolContainer48 if carnot_ISymbolContainer48 is not None else set()
        self.carnot_ISymbolContainer50 = carnot_ISymbolContainer50 if carnot_ISymbolContainer50 is not None else set()
        self.carnot_ISymbolContainer52 = carnot_ISymbolContainer52 if carnot_ISymbolContainer52 is not None else set()
        self.carnot_ISymbolContainer54 = carnot_ISymbolContainer54 if carnot_ISymbolContainer54 is not None else set()
        self.carnot_ISymbolContainer56 = carnot_ISymbolContainer56 if carnot_ISymbolContainer56 is not None else set()
        self.carnot_ISymbolContainer58 = carnot_ISymbolContainer58 if carnot_ISymbolContainer58 is not None else set()
        
    @property
    def nodes(self) -> str:
        return self.__nodes

    @nodes.setter
    def nodes(self, nodes: str):
        self.__nodes = nodes

    @property
    def connections(self) -> str:
        return self.__connections

    @connections.setter
    def connections(self, connections: str):
        self.__connections = connections

    @property
    def carnot_ISymbolContainer30(self):
        return self.__carnot_ISymbolContainer30

    @carnot_ISymbolContainer30.setter
    def carnot_ISymbolContainer30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer30", None)
        self.__carnot_ISymbolContainer30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_PublicInterfaceSymbol"):
                    opp_val = getattr(item, "carnot_PublicInterfaceSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_PublicInterfaceSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_PublicInterfaceSymbol"):
                    opp_val = getattr(item, "carnot_PublicInterfaceSymbol", None)
                    
                    setattr(item, "carnot_PublicInterfaceSymbol", self)
                    

    @property
    def carnot_ISymbolContainer58(self):
        return self.__carnot_ISymbolContainer58

    @carnot_ISymbolContainer58.setter
    def carnot_ISymbolContainer58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer58", None)
        self.__carnot_ISymbolContainer58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TeamLeadConnectionType"):
                    opp_val = getattr(item, "carnot_TeamLeadConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TeamLeadConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TeamLeadConnectionType"):
                    opp_val = getattr(item, "carnot_TeamLeadConnectionType", None)
                    
                    setattr(item, "carnot_TeamLeadConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer34(self):
        return self.__carnot_ISymbolContainer34

    @carnot_ISymbolContainer34.setter
    def carnot_ISymbolContainer34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer34", None)
        self.__carnot_ISymbolContainer34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_StartEventSymbol"):
                    opp_val = getattr(item, "carnot_StartEventSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_StartEventSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_StartEventSymbol"):
                    opp_val = getattr(item, "carnot_StartEventSymbol", None)
                    
                    setattr(item, "carnot_StartEventSymbol", self)
                    

    @property
    def carnot_ISymbolContainer40(self):
        return self.__carnot_ISymbolContainer40

    @carnot_ISymbolContainer40.setter
    def carnot_ISymbolContainer40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer40", None)
        self.__carnot_ISymbolContainer40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ExecutedByConnectionType"):
                    opp_val = getattr(item, "carnot_ExecutedByConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ExecutedByConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ExecutedByConnectionType"):
                    opp_val = getattr(item, "carnot_ExecutedByConnectionType", None)
                    
                    setattr(item, "carnot_ExecutedByConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer8(self):
        return self.__carnot_ISymbolContainer8

    @carnot_ISymbolContainer8.setter
    def carnot_ISymbolContainer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer8", None)
        self.__carnot_ISymbolContainer8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_AnnotationSymbolType"):
                    opp_val = getattr(item, "carnot_AnnotationSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_AnnotationSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_AnnotationSymbolType"):
                    opp_val = getattr(item, "carnot_AnnotationSymbolType", None)
                    
                    setattr(item, "carnot_AnnotationSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer48(self):
        return self.__carnot_ISymbolContainer48

    @carnot_ISymbolContainer48.setter
    def carnot_ISymbolContainer48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer48", None)
        self.__carnot_ISymbolContainer48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TriggersConnectionType"):
                    opp_val = getattr(item, "carnot_TriggersConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TriggersConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TriggersConnectionType"):
                    opp_val = getattr(item, "carnot_TriggersConnectionType", None)
                    
                    setattr(item, "carnot_TriggersConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer46(self):
        return self.__carnot_ISymbolContainer46

    @carnot_ISymbolContainer46.setter
    def carnot_ISymbolContainer46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer46", None)
        self.__carnot_ISymbolContainer46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_PerformsConnectionType"):
                    opp_val = getattr(item, "carnot_PerformsConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_PerformsConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_PerformsConnectionType"):
                    opp_val = getattr(item, "carnot_PerformsConnectionType", None)
                    
                    setattr(item, "carnot_PerformsConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer26(self):
        return self.__carnot_ISymbolContainer26

    @carnot_ISymbolContainer26.setter
    def carnot_ISymbolContainer26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer26", None)
        self.__carnot_ISymbolContainer26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_OrganizationSymbolType"):
                    opp_val = getattr(item, "carnot_OrganizationSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_OrganizationSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_OrganizationSymbolType"):
                    opp_val = getattr(item, "carnot_OrganizationSymbolType", None)
                    
                    setattr(item, "carnot_OrganizationSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer42(self):
        return self.__carnot_ISymbolContainer42

    @carnot_ISymbolContainer42.setter
    def carnot_ISymbolContainer42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer42", None)
        self.__carnot_ISymbolContainer42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_GenericLinkConnectionType"):
                    opp_val = getattr(item, "carnot_GenericLinkConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_GenericLinkConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_GenericLinkConnectionType"):
                    opp_val = getattr(item, "carnot_GenericLinkConnectionType", None)
                    
                    setattr(item, "carnot_GenericLinkConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer54(self):
        return self.__carnot_ISymbolContainer54

    @carnot_ISymbolContainer54.setter
    def carnot_ISymbolContainer54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer54", None)
        self.__carnot_ISymbolContainer54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TransitionConnectionType"):
                    opp_val = getattr(item, "carnot_TransitionConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TransitionConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TransitionConnectionType"):
                    opp_val = getattr(item, "carnot_TransitionConnectionType", None)
                    
                    setattr(item, "carnot_TransitionConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer38(self):
        return self.__carnot_ISymbolContainer38

    @carnot_ISymbolContainer38.setter
    def carnot_ISymbolContainer38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer38", None)
        self.__carnot_ISymbolContainer38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataMappingConnectionType"):
                    opp_val = getattr(item, "carnot_DataMappingConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataMappingConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataMappingConnectionType"):
                    opp_val = getattr(item, "carnot_DataMappingConnectionType", None)
                    
                    setattr(item, "carnot_DataMappingConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer(self):
        return self.__carnot_ISymbolContainer

    @carnot_ISymbolContainer.setter
    def carnot_ISymbolContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer", None)
        self.__carnot_ISymbolContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ActivitySymbolType"):
                    opp_val = getattr(item, "carnot_ActivitySymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ActivitySymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ActivitySymbolType"):
                    opp_val = getattr(item, "carnot_ActivitySymbolType", None)
                    
                    setattr(item, "carnot_ActivitySymbolType", self)
                    

    @property
    def carnot_ISymbolContainer16(self):
        return self.__carnot_ISymbolContainer16

    @carnot_ISymbolContainer16.setter
    def carnot_ISymbolContainer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer16", None)
        self.__carnot_ISymbolContainer16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EndEventSymbol"):
                    opp_val = getattr(item, "carnot_EndEventSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EndEventSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EndEventSymbol"):
                    opp_val = getattr(item, "carnot_EndEventSymbol", None)
                    
                    setattr(item, "carnot_EndEventSymbol", self)
                    

    @property
    def carnot_ISymbolContainer10(self):
        return self.__carnot_ISymbolContainer10

    @carnot_ISymbolContainer10.setter
    def carnot_ISymbolContainer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer10", None)
        self.__carnot_ISymbolContainer10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ApplicationSymbolType"):
                    opp_val = getattr(item, "carnot_ApplicationSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ApplicationSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ApplicationSymbolType"):
                    opp_val = getattr(item, "carnot_ApplicationSymbolType", None)
                    
                    setattr(item, "carnot_ApplicationSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer28(self):
        return self.__carnot_ISymbolContainer28

    @carnot_ISymbolContainer28.setter
    def carnot_ISymbolContainer28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer28", None)
        self.__carnot_ISymbolContainer28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ProcessSymbolType"):
                    opp_val = getattr(item, "carnot_ProcessSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ProcessSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ProcessSymbolType"):
                    opp_val = getattr(item, "carnot_ProcessSymbolType", None)
                    
                    setattr(item, "carnot_ProcessSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer20(self):
        return self.__carnot_ISymbolContainer20

    @carnot_ISymbolContainer20.setter
    def carnot_ISymbolContainer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer20", None)
        self.__carnot_ISymbolContainer20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_GroupSymbolType"):
                    opp_val = getattr(item, "carnot_GroupSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_GroupSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_GroupSymbolType"):
                    opp_val = getattr(item, "carnot_GroupSymbolType", None)
                    
                    setattr(item, "carnot_GroupSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer44(self):
        return self.__carnot_ISymbolContainer44

    @carnot_ISymbolContainer44.setter
    def carnot_ISymbolContainer44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer44", None)
        self.__carnot_ISymbolContainer44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_PartOfConnectionType"):
                    opp_val = getattr(item, "carnot_PartOfConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_PartOfConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_PartOfConnectionType"):
                    opp_val = getattr(item, "carnot_PartOfConnectionType", None)
                    
                    setattr(item, "carnot_PartOfConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer50(self):
        return self.__carnot_ISymbolContainer50

    @carnot_ISymbolContainer50.setter
    def carnot_ISymbolContainer50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer50", None)
        self.__carnot_ISymbolContainer50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_RefersToConnectionType"):
                    opp_val = getattr(item, "carnot_RefersToConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_RefersToConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_RefersToConnectionType"):
                    opp_val = getattr(item, "carnot_RefersToConnectionType", None)
                    
                    setattr(item, "carnot_RefersToConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer32(self):
        return self.__carnot_ISymbolContainer32

    @carnot_ISymbolContainer32.setter
    def carnot_ISymbolContainer32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer32", None)
        self.__carnot_ISymbolContainer32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_RoleSymbolType"):
                    opp_val = getattr(item, "carnot_RoleSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_RoleSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_RoleSymbolType"):
                    opp_val = getattr(item, "carnot_RoleSymbolType", None)
                    
                    setattr(item, "carnot_RoleSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer18(self):
        return self.__carnot_ISymbolContainer18

    @carnot_ISymbolContainer18.setter
    def carnot_ISymbolContainer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer18", None)
        self.__carnot_ISymbolContainer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_GatewaySymbol"):
                    opp_val = getattr(item, "carnot_GatewaySymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_GatewaySymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_GatewaySymbol"):
                    opp_val = getattr(item, "carnot_GatewaySymbol", None)
                    
                    setattr(item, "carnot_GatewaySymbol", self)
                    

    @property
    def carnot_ISymbolContainer36(self):
        return self.__carnot_ISymbolContainer36

    @carnot_ISymbolContainer36.setter
    def carnot_ISymbolContainer36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer36", None)
        self.__carnot_ISymbolContainer36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TextSymbolType"):
                    opp_val = getattr(item, "carnot_TextSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TextSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TextSymbolType"):
                    opp_val = getattr(item, "carnot_TextSymbolType", None)
                    
                    setattr(item, "carnot_TextSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer56(self):
        return self.__carnot_ISymbolContainer56

    @carnot_ISymbolContainer56.setter
    def carnot_ISymbolContainer56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer56", None)
        self.__carnot_ISymbolContainer56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_WorksForConnectionType"):
                    opp_val = getattr(item, "carnot_WorksForConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_WorksForConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_WorksForConnectionType"):
                    opp_val = getattr(item, "carnot_WorksForConnectionType", None)
                    
                    setattr(item, "carnot_WorksForConnectionType", self)
                    

    @property
    def carnot_ISymbolContainer14(self):
        return self.__carnot_ISymbolContainer14

    @carnot_ISymbolContainer14.setter
    def carnot_ISymbolContainer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer14", None)
        self.__carnot_ISymbolContainer14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataSymbolType"):
                    opp_val = getattr(item, "carnot_DataSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataSymbolType"):
                    opp_val = getattr(item, "carnot_DataSymbolType", None)
                    
                    setattr(item, "carnot_DataSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer24(self):
        return self.__carnot_ISymbolContainer24

    @carnot_ISymbolContainer24.setter
    def carnot_ISymbolContainer24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer24", None)
        self.__carnot_ISymbolContainer24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ModelerSymbolType"):
                    opp_val = getattr(item, "carnot_ModelerSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ModelerSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ModelerSymbolType"):
                    opp_val = getattr(item, "carnot_ModelerSymbolType", None)
                    
                    setattr(item, "carnot_ModelerSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer12(self):
        return self.__carnot_ISymbolContainer12

    @carnot_ISymbolContainer12.setter
    def carnot_ISymbolContainer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer12", None)
        self.__carnot_ISymbolContainer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ConditionalPerformerSymbolType"):
                    opp_val = getattr(item, "carnot_ConditionalPerformerSymbolType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ConditionalPerformerSymbolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ConditionalPerformerSymbolType"):
                    opp_val = getattr(item, "carnot_ConditionalPerformerSymbolType", None)
                    
                    setattr(item, "carnot_ConditionalPerformerSymbolType", self)
                    

    @property
    def carnot_ISymbolContainer22(self):
        return self.__carnot_ISymbolContainer22

    @carnot_ISymbolContainer22.setter
    def carnot_ISymbolContainer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer22", None)
        self.__carnot_ISymbolContainer22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_IntermediateEventSymbol"):
                    opp_val = getattr(item, "carnot_IntermediateEventSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_IntermediateEventSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_IntermediateEventSymbol"):
                    opp_val = getattr(item, "carnot_IntermediateEventSymbol", None)
                    
                    setattr(item, "carnot_IntermediateEventSymbol", self)
                    

    @property
    def carnot_ISymbolContainer52(self):
        return self.__carnot_ISymbolContainer52

    @carnot_ISymbolContainer52.setter
    def carnot_ISymbolContainer52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISymbolContainer__carnot_ISymbolContainer52", None)
        self.__carnot_ISymbolContainer52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_SubProcessOfConnectionType"):
                    opp_val = getattr(item, "carnot_SubProcessOfConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_SubProcessOfConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_SubProcessOfConnectionType"):
                    opp_val = getattr(item, "carnot_SubProcessOfConnectionType", None)
                    
                    setattr(item, "carnot_SubProcessOfConnectionType", self)
                    

    def getNodeContainingFeatures(self) -> str:
        # TODO: Implement getNodeContainingFeatures method
        pass

    def getConnectionContainingFeatures(self) -> str:
        # TODO: Implement getConnectionContainingFeatures method
        pass

class IIdentifiableElement:

    pass
class carnot_ModelType(IIdentifiableElement, IExtensibleElement):

    def __init__(self, modelOID: str, oid: str, vendor: str, author: str, carnotVersion: str, created: str, carnot_ModelType: "carnot_DocumentRoot" = None, carnot_ModelType223: set["carnot_EventActionTypeType"] = None, carnot_ModelType225: set["carnot_DataType"] = None, carnot_ModelType228: set["carnot_ApplicationType"] = None, carnot_ModelType231: set["carnot_ModelerType"] = None, carnot_ModelType209: "carnot_DescriptionType" = None, carnot_ModelType212: set["carnot_DataTypeType"] = None, carnot_ModelType215: set["carnot_ApplicationTypeType"] = None, carnot_ModelType217: set["carnot_ApplicationContextTypeType"] = None, carnot_ModelType219: set["carnot_TriggerTypeType"] = None, carnot_ModelType221: set["carnot_EventConditionTypeType"] = None, carnot_ModelType243: "carnot_ExternalPackages" = None, carnot_ModelType245: "carnot_ScriptType" = None, carnot_ModelType247: "carnot_TypeDeclarationsType" = None, carnot_ModelType233: "carnot_QualityControlType" = None, carnot_ModelType235: set["carnot_RoleType"] = None, carnot_ModelType237: set["carnot_OrganizationType"] = None, carnot_ModelType239: set["carnot_ConditionalPerformerType"] = None, carnot_ModelType241: set["carnot_ProcessDefinitionType"] = None, carnot_ModelType249: set["carnot_DiagramType"] = None, carnot_ModelType251: set["carnot_LinkTypeType"] = None, carnot_ModelType253: set["carnot_ViewType"] = None):
        self.modelOID = modelOID
        self.oid = oid
        self.vendor = vendor
        self.author = author
        self.carnotVersion = carnotVersion
        self.created = created
        self.carnot_ModelType = carnot_ModelType
        self.carnot_ModelType223 = carnot_ModelType223 if carnot_ModelType223 is not None else set()
        self.carnot_ModelType225 = carnot_ModelType225 if carnot_ModelType225 is not None else set()
        self.carnot_ModelType228 = carnot_ModelType228 if carnot_ModelType228 is not None else set()
        self.carnot_ModelType231 = carnot_ModelType231 if carnot_ModelType231 is not None else set()
        self.carnot_ModelType209 = carnot_ModelType209
        self.carnot_ModelType212 = carnot_ModelType212 if carnot_ModelType212 is not None else set()
        self.carnot_ModelType215 = carnot_ModelType215 if carnot_ModelType215 is not None else set()
        self.carnot_ModelType217 = carnot_ModelType217 if carnot_ModelType217 is not None else set()
        self.carnot_ModelType219 = carnot_ModelType219 if carnot_ModelType219 is not None else set()
        self.carnot_ModelType221 = carnot_ModelType221 if carnot_ModelType221 is not None else set()
        self.carnot_ModelType243 = carnot_ModelType243
        self.carnot_ModelType245 = carnot_ModelType245
        self.carnot_ModelType247 = carnot_ModelType247
        self.carnot_ModelType233 = carnot_ModelType233
        self.carnot_ModelType235 = carnot_ModelType235 if carnot_ModelType235 is not None else set()
        self.carnot_ModelType237 = carnot_ModelType237 if carnot_ModelType237 is not None else set()
        self.carnot_ModelType239 = carnot_ModelType239 if carnot_ModelType239 is not None else set()
        self.carnot_ModelType241 = carnot_ModelType241 if carnot_ModelType241 is not None else set()
        self.carnot_ModelType249 = carnot_ModelType249 if carnot_ModelType249 is not None else set()
        self.carnot_ModelType251 = carnot_ModelType251 if carnot_ModelType251 is not None else set()
        self.carnot_ModelType253 = carnot_ModelType253 if carnot_ModelType253 is not None else set()
        
    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def carnotVersion(self) -> str:
        return self.__carnotVersion

    @carnotVersion.setter
    def carnotVersion(self, carnotVersion: str):
        self.__carnotVersion = carnotVersion

    @property
    def modelOID(self) -> str:
        return self.__modelOID

    @modelOID.setter
    def modelOID(self, modelOID: str):
        self.__modelOID = modelOID

    @property
    def oid(self) -> str:
        return self.__oid

    @oid.setter
    def oid(self, oid: str):
        self.__oid = oid

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def carnot_ModelType(self):
        return self.__carnot_ModelType

    @carnot_ModelType.setter
    def carnot_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType", None)
        self.__carnot_ModelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_DocumentRoot174"):
                opp_val = getattr(old_value, "carnot_DocumentRoot174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_DocumentRoot174"):
                opp_val = getattr(value, "carnot_DocumentRoot174", None)
                if opp_val is None:
                    setattr(value, "carnot_DocumentRoot174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_ModelType237(self):
        return self.__carnot_ModelType237

    @carnot_ModelType237.setter
    def carnot_ModelType237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType237", None)
        self.__carnot_ModelType237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_OrganizationType"):
                    opp_val = getattr(item, "carnot_OrganizationType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_OrganizationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_OrganizationType"):
                    opp_val = getattr(item, "carnot_OrganizationType", None)
                    
                    setattr(item, "carnot_OrganizationType", self)
                    

    @property
    def carnot_ModelType233(self):
        return self.__carnot_ModelType233

    @carnot_ModelType233.setter
    def carnot_ModelType233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType233", None)
        self.__carnot_ModelType233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_QualityControlType"):
                opp_val = getattr(old_value, "carnot_QualityControlType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_QualityControlType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_QualityControlType"):
                opp_val = getattr(value, "carnot_QualityControlType", None)
                setattr(value, "carnot_QualityControlType", self)

    @property
    def carnot_ModelType223(self):
        return self.__carnot_ModelType223

    @carnot_ModelType223.setter
    def carnot_ModelType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType223", None)
        self.__carnot_ModelType223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EventActionTypeType"):
                    opp_val = getattr(item, "carnot_EventActionTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EventActionTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EventActionTypeType"):
                    opp_val = getattr(item, "carnot_EventActionTypeType", None)
                    
                    setattr(item, "carnot_EventActionTypeType", self)
                    

    @property
    def carnot_ModelType247(self):
        return self.__carnot_ModelType247

    @carnot_ModelType247.setter
    def carnot_ModelType247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType247", None)
        self.__carnot_ModelType247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_TypeDeclarationsType"):
                opp_val = getattr(old_value, "carnot_TypeDeclarationsType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_TypeDeclarationsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_TypeDeclarationsType"):
                opp_val = getattr(value, "carnot_TypeDeclarationsType", None)
                setattr(value, "carnot_TypeDeclarationsType", self)

    @property
    def carnot_ModelType231(self):
        return self.__carnot_ModelType231

    @carnot_ModelType231.setter
    def carnot_ModelType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType231", None)
        self.__carnot_ModelType231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ModelerType"):
                    opp_val = getattr(item, "carnot_ModelerType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ModelerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ModelerType"):
                    opp_val = getattr(item, "carnot_ModelerType", None)
                    
                    setattr(item, "carnot_ModelerType", self)
                    

    @property
    def carnot_ModelType239(self):
        return self.__carnot_ModelType239

    @carnot_ModelType239.setter
    def carnot_ModelType239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType239", None)
        self.__carnot_ModelType239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ConditionalPerformerType"):
                    opp_val = getattr(item, "carnot_ConditionalPerformerType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ConditionalPerformerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ConditionalPerformerType"):
                    opp_val = getattr(item, "carnot_ConditionalPerformerType", None)
                    
                    setattr(item, "carnot_ConditionalPerformerType", self)
                    

    @property
    def carnot_ModelType243(self):
        return self.__carnot_ModelType243

    @carnot_ModelType243.setter
    def carnot_ModelType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType243", None)
        self.__carnot_ModelType243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ExternalPackages"):
                opp_val = getattr(old_value, "carnot_ExternalPackages", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ExternalPackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ExternalPackages"):
                opp_val = getattr(value, "carnot_ExternalPackages", None)
                setattr(value, "carnot_ExternalPackages", self)

    @property
    def carnot_ModelType219(self):
        return self.__carnot_ModelType219

    @carnot_ModelType219.setter
    def carnot_ModelType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType219", None)
        self.__carnot_ModelType219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_TriggerTypeType"):
                    opp_val = getattr(item, "carnot_TriggerTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_TriggerTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_TriggerTypeType"):
                    opp_val = getattr(item, "carnot_TriggerTypeType", None)
                    
                    setattr(item, "carnot_TriggerTypeType", self)
                    

    @property
    def carnot_ModelType235(self):
        return self.__carnot_ModelType235

    @carnot_ModelType235.setter
    def carnot_ModelType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType235", None)
        self.__carnot_ModelType235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_RoleType"):
                    opp_val = getattr(item, "carnot_RoleType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_RoleType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_RoleType"):
                    opp_val = getattr(item, "carnot_RoleType", None)
                    
                    setattr(item, "carnot_RoleType", self)
                    

    @property
    def carnot_ModelType212(self):
        return self.__carnot_ModelType212

    @carnot_ModelType212.setter
    def carnot_ModelType212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType212", None)
        self.__carnot_ModelType212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataTypeType213"):
                    opp_val = getattr(item, "carnot_DataTypeType213", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataTypeType213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataTypeType213"):
                    opp_val = getattr(item, "carnot_DataTypeType213", None)
                    
                    setattr(item, "carnot_DataTypeType213", self)
                    

    @property
    def carnot_ModelType228(self):
        return self.__carnot_ModelType228

    @carnot_ModelType228.setter
    def carnot_ModelType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType228", None)
        self.__carnot_ModelType228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ApplicationType229"):
                    opp_val = getattr(item, "carnot_ApplicationType229", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ApplicationType229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ApplicationType229"):
                    opp_val = getattr(item, "carnot_ApplicationType229", None)
                    
                    setattr(item, "carnot_ApplicationType229", self)
                    

    @property
    def carnot_ModelType245(self):
        return self.__carnot_ModelType245

    @carnot_ModelType245.setter
    def carnot_ModelType245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType245", None)
        self.__carnot_ModelType245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ScriptType"):
                opp_val = getattr(old_value, "carnot_ScriptType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ScriptType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ScriptType"):
                opp_val = getattr(value, "carnot_ScriptType", None)
                setattr(value, "carnot_ScriptType", self)

    @property
    def carnot_ModelType249(self):
        return self.__carnot_ModelType249

    @carnot_ModelType249.setter
    def carnot_ModelType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType249", None)
        self.__carnot_ModelType249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DiagramType"):
                    opp_val = getattr(item, "carnot_DiagramType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DiagramType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DiagramType"):
                    opp_val = getattr(item, "carnot_DiagramType", None)
                    
                    setattr(item, "carnot_DiagramType", self)
                    

    @property
    def carnot_ModelType215(self):
        return self.__carnot_ModelType215

    @carnot_ModelType215.setter
    def carnot_ModelType215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType215", None)
        self.__carnot_ModelType215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ApplicationTypeType"):
                    opp_val = getattr(item, "carnot_ApplicationTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ApplicationTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ApplicationTypeType"):
                    opp_val = getattr(item, "carnot_ApplicationTypeType", None)
                    
                    setattr(item, "carnot_ApplicationTypeType", self)
                    

    @property
    def carnot_ModelType221(self):
        return self.__carnot_ModelType221

    @carnot_ModelType221.setter
    def carnot_ModelType221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType221", None)
        self.__carnot_ModelType221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_EventConditionTypeType"):
                    opp_val = getattr(item, "carnot_EventConditionTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_EventConditionTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_EventConditionTypeType"):
                    opp_val = getattr(item, "carnot_EventConditionTypeType", None)
                    
                    setattr(item, "carnot_EventConditionTypeType", self)
                    

    @property
    def carnot_ModelType217(self):
        return self.__carnot_ModelType217

    @carnot_ModelType217.setter
    def carnot_ModelType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType217", None)
        self.__carnot_ModelType217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ApplicationContextTypeType"):
                    opp_val = getattr(item, "carnot_ApplicationContextTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ApplicationContextTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ApplicationContextTypeType"):
                    opp_val = getattr(item, "carnot_ApplicationContextTypeType", None)
                    
                    setattr(item, "carnot_ApplicationContextTypeType", self)
                    

    @property
    def carnot_ModelType253(self):
        return self.__carnot_ModelType253

    @carnot_ModelType253.setter
    def carnot_ModelType253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType253", None)
        self.__carnot_ModelType253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ViewType"):
                    opp_val = getattr(item, "carnot_ViewType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ViewType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ViewType"):
                    opp_val = getattr(item, "carnot_ViewType", None)
                    
                    setattr(item, "carnot_ViewType", self)
                    

    @property
    def carnot_ModelType209(self):
        return self.__carnot_ModelType209

    @carnot_ModelType209.setter
    def carnot_ModelType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType209", None)
        self.__carnot_ModelType209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_DescriptionType210"):
                opp_val = getattr(old_value, "carnot_DescriptionType210", None)
                if opp_val == self:
                    setattr(old_value, "carnot_DescriptionType210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_DescriptionType210"):
                opp_val = getattr(value, "carnot_DescriptionType210", None)
                setattr(value, "carnot_DescriptionType210", self)

    @property
    def carnot_ModelType251(self):
        return self.__carnot_ModelType251

    @carnot_ModelType251.setter
    def carnot_ModelType251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType251", None)
        self.__carnot_ModelType251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_LinkTypeType"):
                    opp_val = getattr(item, "carnot_LinkTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_LinkTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_LinkTypeType"):
                    opp_val = getattr(item, "carnot_LinkTypeType", None)
                    
                    setattr(item, "carnot_LinkTypeType", self)
                    

    @property
    def carnot_ModelType241(self):
        return self.__carnot_ModelType241

    @carnot_ModelType241.setter
    def carnot_ModelType241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType241", None)
        self.__carnot_ModelType241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ProcessDefinitionType"):
                    opp_val = getattr(item, "carnot_ProcessDefinitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ProcessDefinitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ProcessDefinitionType"):
                    opp_val = getattr(item, "carnot_ProcessDefinitionType", None)
                    
                    setattr(item, "carnot_ProcessDefinitionType", self)
                    

    @property
    def carnot_ModelType225(self):
        return self.__carnot_ModelType225

    @carnot_ModelType225.setter
    def carnot_ModelType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ModelType__carnot_ModelType225", None)
        self.__carnot_ModelType225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_DataType226"):
                    opp_val = getattr(item, "carnot_DataType226", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_DataType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_DataType226"):
                    opp_val = getattr(item, "carnot_DataType226", None)
                    
                    setattr(item, "carnot_DataType226", self)
                    

class carnot_ISwimlaneSymbol(IIdentifiableElement, INodeSymbol):

    def __init__(self, orientation: str, collapsed: str, performedSwimlanes: "carnot_IModelParticipant" = None, parentLane: set["carnot_LaneSymbol"] = None, carnot_ISwimlaneSymbol: "carnot_IModelParticipant" = None, ISwimlaneSymbol: "carnot_IModelParticipant" = None, ISwimlaneSymbol203: "carnot_LaneSymbol" = None):
        self.orientation = orientation
        self.collapsed = collapsed
        self.performedSwimlanes = performedSwimlanes
        self.parentLane = parentLane if parentLane is not None else set()
        self.carnot_ISwimlaneSymbol = carnot_ISwimlaneSymbol
        self.ISwimlaneSymbol = ISwimlaneSymbol
        self.ISwimlaneSymbol203 = ISwimlaneSymbol203
        
    @property
    def collapsed(self) -> str:
        return self.__collapsed

    @collapsed.setter
    def collapsed(self, collapsed: str):
        self.__collapsed = collapsed

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def carnot_ISwimlaneSymbol(self):
        return self.__carnot_ISwimlaneSymbol

    @carnot_ISwimlaneSymbol.setter
    def carnot_ISwimlaneSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISwimlaneSymbol__carnot_ISwimlaneSymbol", None)
        self.__carnot_ISwimlaneSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IModelParticipant"):
                opp_val = getattr(old_value, "carnot_IModelParticipant", None)
                if opp_val == self:
                    setattr(old_value, "carnot_IModelParticipant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IModelParticipant"):
                opp_val = getattr(value, "carnot_IModelParticipant", None)
                setattr(value, "carnot_IModelParticipant", self)

    @property
    def ISwimlaneSymbol(self):
        return self.__ISwimlaneSymbol

    @ISwimlaneSymbol.setter
    def ISwimlaneSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISwimlaneSymbol__ISwimlaneSymbol", None)
        self.__ISwimlaneSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participant"):
                opp_val = getattr(old_value, "participant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participant"):
                opp_val = getattr(value, "participant", None)
                if opp_val is None:
                    setattr(value, "participant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentLane(self):
        return self.__parentLane

    @parentLane.setter
    def parentLane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISwimlaneSymbol__parentLane", None)
        self.__parentLane = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LaneSymbol"):
                    opp_val = getattr(item, "LaneSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "LaneSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LaneSymbol"):
                    opp_val = getattr(item, "LaneSymbol", None)
                    
                    setattr(item, "LaneSymbol", self)
                    

    @property
    def performedSwimlanes(self):
        return self.__performedSwimlanes

    @performedSwimlanes.setter
    def performedSwimlanes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISwimlaneSymbol__performedSwimlanes", None)
        self.__performedSwimlanes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IModelParticipant"):
                opp_val = getattr(old_value, "IModelParticipant", None)
                if opp_val == self:
                    setattr(old_value, "IModelParticipant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IModelParticipant"):
                opp_val = getattr(value, "IModelParticipant", None)
                setattr(value, "IModelParticipant", self)

    @property
    def ISwimlaneSymbol203(self):
        return self.__ISwimlaneSymbol203

    @ISwimlaneSymbol203.setter
    def ISwimlaneSymbol203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ISwimlaneSymbol__ISwimlaneSymbol203", None)
        self.__ISwimlaneSymbol203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childLanes"):
                opp_val = getattr(old_value, "childLanes", None)
                if opp_val == self:
                    setattr(old_value, "childLanes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childLanes"):
                opp_val = getattr(value, "childLanes", None)
                setattr(value, "childLanes", self)

class IModelElement:

    pass
class carnot_DataMappingType(IIdentifiableElement, IModelElement, IExtensibleElement):

    def __init__(self, applicationAccessPoint: str, applicationPath: str, context: str, dataPath: str, direction: str, carnot_DataMappingType: "carnot_ActivityType" = None, dataMappings143: "carnot_DataType" = None, DataMappingType: "carnot_DataType" = None):
        self.applicationAccessPoint = applicationAccessPoint
        self.applicationPath = applicationPath
        self.context = context
        self.dataPath = dataPath
        self.direction = direction
        self.carnot_DataMappingType = carnot_DataMappingType
        self.dataMappings143 = dataMappings143
        self.DataMappingType = DataMappingType
        
    @property
    def dataPath(self) -> str:
        return self.__dataPath

    @dataPath.setter
    def dataPath(self, dataPath: str):
        self.__dataPath = dataPath

    @property
    def applicationAccessPoint(self) -> str:
        return self.__applicationAccessPoint

    @applicationAccessPoint.setter
    def applicationAccessPoint(self, applicationAccessPoint: str):
        self.__applicationAccessPoint = applicationAccessPoint

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def applicationPath(self) -> str:
        return self.__applicationPath

    @applicationPath.setter
    def applicationPath(self, applicationPath: str):
        self.__applicationPath = applicationPath

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def DataMappingType(self):
        return self.__DataMappingType

    @DataMappingType.setter
    def DataMappingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataMappingType__DataMappingType", None)
        self.__DataMappingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data"):
                opp_val = getattr(old_value, "data", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data"):
                opp_val = getattr(value, "data", None)
                if opp_val is None:
                    setattr(value, "data", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_DataMappingType(self):
        return self.__carnot_DataMappingType

    @carnot_DataMappingType.setter
    def carnot_DataMappingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataMappingType__carnot_DataMappingType", None)
        self.__carnot_DataMappingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ActivityType"):
                opp_val = getattr(old_value, "carnot_ActivityType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ActivityType"):
                opp_val = getattr(value, "carnot_ActivityType", None)
                if opp_val is None:
                    setattr(value, "carnot_ActivityType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataMappings143(self):
        return self.__dataMappings143

    @dataMappings143.setter
    def dataMappings143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DataMappingType__dataMappings143", None)
        self.__dataMappings143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType144"):
                opp_val = getattr(old_value, "DataType144", None)
                if opp_val == self:
                    setattr(old_value, "DataType144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType144"):
                opp_val = getattr(value, "DataType144", None)
                setattr(value, "DataType144", self)

class carnot_DiagramType(ISymbolContainer, IModelElement, IExtensibleElement):

    def __init__(self, name: str, orientation: str, mode: str, diagram: set["carnot_PoolSymbol"] = None, carnot_DiagramType: "carnot_ModelType" = None, DiagramType: "carnot_PoolSymbol" = None, carnot_DiagramType293: "carnot_ProcessDefinitionType" = None):
        self.name = name
        self.orientation = orientation
        self.mode = mode
        self.diagram = diagram if diagram is not None else set()
        self.carnot_DiagramType = carnot_DiagramType
        self.DiagramType = DiagramType
        self.carnot_DiagramType293 = carnot_DiagramType293
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def carnot_DiagramType(self):
        return self.__carnot_DiagramType

    @carnot_DiagramType.setter
    def carnot_DiagramType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DiagramType__carnot_DiagramType", None)
        self.__carnot_DiagramType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType249"):
                opp_val = getattr(old_value, "carnot_ModelType249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType249"):
                opp_val = getattr(value, "carnot_ModelType249", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DiagramType__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PoolSymbol"):
                    opp_val = getattr(item, "PoolSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "PoolSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PoolSymbol"):
                    opp_val = getattr(item, "PoolSymbol", None)
                    
                    setattr(item, "PoolSymbol", self)
                    

    @property
    def DiagramType(self):
        return self.__DiagramType

    @DiagramType.setter
    def DiagramType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DiagramType__DiagramType", None)
        self.__DiagramType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poolSymbols"):
                opp_val = getattr(old_value, "poolSymbols", None)
                if opp_val == self:
                    setattr(old_value, "poolSymbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poolSymbols"):
                opp_val = getattr(value, "poolSymbols", None)
                setattr(value, "poolSymbols", self)

    @property
    def carnot_DiagramType293(self):
        return self.__carnot_DiagramType293

    @carnot_DiagramType293.setter
    def carnot_DiagramType293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_DiagramType__carnot_DiagramType293", None)
        self.__carnot_DiagramType293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ProcessDefinitionType292"):
                opp_val = getattr(old_value, "carnot_ProcessDefinitionType292", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ProcessDefinitionType292"):
                opp_val = getattr(value, "carnot_ProcessDefinitionType292", None)
                if opp_val is None:
                    setattr(value, "carnot_ProcessDefinitionType292", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_ContextType(IModelElement, IExtensibleElement, ITypedElement, IAccessPointOwner):

    pass
class carnot_ParameterMappingType(IModelElement):

    def __init__(self, dataPath: str, parameter: str, parameterPath: str, ParameterMappingType: "carnot_DataType" = None, parameterMappings: "carnot_DataType" = None, carnot_ParameterMappingType: "carnot_TriggerType" = None):
        self.dataPath = dataPath
        self.parameter = parameter
        self.parameterPath = parameterPath
        self.ParameterMappingType = ParameterMappingType
        self.parameterMappings = parameterMappings
        self.carnot_ParameterMappingType = carnot_ParameterMappingType
        
    @property
    def dataPath(self) -> str:
        return self.__dataPath

    @dataPath.setter
    def dataPath(self, dataPath: str):
        self.__dataPath = dataPath

    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def parameterPath(self) -> str:
        return self.__parameterPath

    @parameterPath.setter
    def parameterPath(self, parameterPath: str):
        self.__parameterPath = parameterPath

    @property
    def ParameterMappingType(self):
        return self.__ParameterMappingType

    @ParameterMappingType.setter
    def ParameterMappingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ParameterMappingType__ParameterMappingType", None)
        self.__ParameterMappingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data163"):
                opp_val = getattr(old_value, "data163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data163"):
                opp_val = getattr(value, "data163", None)
                if opp_val is None:
                    setattr(value, "data163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameterMappings(self):
        return self.__parameterMappings

    @parameterMappings.setter
    def parameterMappings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ParameterMappingType__parameterMappings", None)
        self.__parameterMappings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType266"):
                opp_val = getattr(old_value, "DataType266", None)
                if opp_val == self:
                    setattr(old_value, "DataType266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType266"):
                opp_val = getattr(value, "DataType266", None)
                setattr(value, "DataType266", self)

    @property
    def carnot_ParameterMappingType(self):
        return self.__carnot_ParameterMappingType

    @carnot_ParameterMappingType.setter
    def carnot_ParameterMappingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ParameterMappingType__carnot_ParameterMappingType", None)
        self.__carnot_ParameterMappingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_TriggerType359"):
                opp_val = getattr(old_value, "carnot_TriggerType359", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_TriggerType359"):
                opp_val = getattr(value, "carnot_TriggerType359", None)
                if opp_val is None:
                    setattr(value, "carnot_TriggerType359", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_ViewType(IModelElement, IExtensibleElement):

    def __init__(self, name: str, carnot_ViewType: "carnot_ModelType" = None, carnot_ViewType372: "carnot_ViewType" = None, carnot_ViewType370: set["carnot_ViewType"] = None, carnot_ViewType374: set["carnot_ViewableType"] = None, carnot_ViewType368: "carnot_DescriptionType" = None):
        self.name = name
        self.carnot_ViewType = carnot_ViewType
        self.carnot_ViewType372 = carnot_ViewType372
        self.carnot_ViewType370 = carnot_ViewType370 if carnot_ViewType370 is not None else set()
        self.carnot_ViewType374 = carnot_ViewType374 if carnot_ViewType374 is not None else set()
        self.carnot_ViewType368 = carnot_ViewType368
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def carnot_ViewType372(self):
        return self.__carnot_ViewType372

    @carnot_ViewType372.setter
    def carnot_ViewType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ViewType__carnot_ViewType372", None)
        self.__carnot_ViewType372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ViewType370"):
                opp_val = getattr(old_value, "carnot_ViewType370", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ViewType370"):
                opp_val = getattr(value, "carnot_ViewType370", None)
                if opp_val is None:
                    setattr(value, "carnot_ViewType370", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_ViewType370(self):
        return self.__carnot_ViewType370

    @carnot_ViewType370.setter
    def carnot_ViewType370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ViewType__carnot_ViewType370", None)
        self.__carnot_ViewType370 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ViewType372"):
                    opp_val = getattr(item, "carnot_ViewType372", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ViewType372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ViewType372"):
                    opp_val = getattr(item, "carnot_ViewType372", None)
                    
                    setattr(item, "carnot_ViewType372", self)
                    

    @property
    def carnot_ViewType368(self):
        return self.__carnot_ViewType368

    @carnot_ViewType368.setter
    def carnot_ViewType368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ViewType__carnot_ViewType368", None)
        self.__carnot_ViewType368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_DescriptionType369"):
                opp_val = getattr(old_value, "carnot_DescriptionType369", None)
                if opp_val == self:
                    setattr(old_value, "carnot_DescriptionType369", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_DescriptionType369"):
                opp_val = getattr(value, "carnot_DescriptionType369", None)
                setattr(value, "carnot_DescriptionType369", self)

    @property
    def carnot_ViewType374(self):
        return self.__carnot_ViewType374

    @carnot_ViewType374.setter
    def carnot_ViewType374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ViewType__carnot_ViewType374", None)
        self.__carnot_ViewType374 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "carnot_ViewableType375"):
                    opp_val = getattr(item, "carnot_ViewableType375", None)
                    
                    if opp_val == self:
                        setattr(item, "carnot_ViewableType375", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "carnot_ViewableType375"):
                    opp_val = getattr(item, "carnot_ViewableType375", None)
                    
                    setattr(item, "carnot_ViewableType375", self)
                    

    @property
    def carnot_ViewType(self):
        return self.__carnot_ViewType

    @carnot_ViewType.setter
    def carnot_ViewType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_ViewType__carnot_ViewType", None)
        self.__carnot_ViewType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ModelType253"):
                opp_val = getattr(old_value, "carnot_ModelType253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ModelType253"):
                opp_val = getattr(value, "carnot_ModelType253", None)
                if opp_val is None:
                    setattr(value, "carnot_ModelType253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class carnot_IGraphicalObject(IModelElement):

    def __init__(self, borderColor: str, fillColor: str, style: str, to: set["carnot_RefersToConnectionType"] = None, from: set["carnot_RefersToConnectionType"] = None, IGraphicalObject: "carnot_RefersToConnectionType" = None, IGraphicalObject311: "carnot_RefersToConnectionType" = None):
        self.borderColor = borderColor
        self.fillColor = fillColor
        self.style = style
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.IGraphicalObject = IGraphicalObject
        self.IGraphicalObject311 = IGraphicalObject311
        
    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

    @property
    def fillColor(self) -> str:
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IGraphicalObject__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefersToConnectionType61"):
                    opp_val = getattr(item, "RefersToConnectionType61", None)
                    
                    if opp_val == self:
                        setattr(item, "RefersToConnectionType61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefersToConnectionType61"):
                    opp_val = getattr(item, "RefersToConnectionType61", None)
                    
                    setattr(item, "RefersToConnectionType61", self)
                    

    @property
    def IGraphicalObject(self):
        return self.__IGraphicalObject

    @IGraphicalObject.setter
    def IGraphicalObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IGraphicalObject__IGraphicalObject", None)
        self.__IGraphicalObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referingFromConnections"):
                opp_val = getattr(old_value, "referingFromConnections", None)
                if opp_val == self:
                    setattr(old_value, "referingFromConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referingFromConnections"):
                opp_val = getattr(value, "referingFromConnections", None)
                setattr(value, "referingFromConnections", self)

    @property
    def IGraphicalObject311(self):
        return self.__IGraphicalObject311

    @IGraphicalObject311.setter
    def IGraphicalObject311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IGraphicalObject__IGraphicalObject311", None)
        self.__IGraphicalObject311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referingToConnections"):
                opp_val = getattr(old_value, "referingToConnections", None)
                if opp_val == self:
                    setattr(old_value, "referingToConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referingToConnections"):
                opp_val = getattr(value, "referingToConnections", None)
                setattr(value, "referingToConnections", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IGraphicalObject__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefersToConnectionType"):
                    opp_val = getattr(item, "RefersToConnectionType", None)
                    
                    if opp_val == self:
                        setattr(item, "RefersToConnectionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefersToConnectionType"):
                    opp_val = getattr(item, "RefersToConnectionType", None)
                    
                    setattr(item, "RefersToConnectionType", self)
                    

class carnot_IIdentifiableModelElement(IIdentifiableElement, IModelElement, IExtensibleElement):

    def __init__(self, carnot_IIdentifiableModelElement: "carnot_DescriptionType" = None):
        self.carnot_IIdentifiableModelElement = carnot_IIdentifiableModelElement
        
    @property
    def carnot_IIdentifiableModelElement(self):
        return self.__carnot_IIdentifiableModelElement

    @carnot_IIdentifiableModelElement.setter
    def carnot_IIdentifiableModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IIdentifiableModelElement__carnot_IIdentifiableModelElement", None)
        self.__carnot_IIdentifiableModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_DescriptionType"):
                opp_val = getattr(old_value, "carnot_DescriptionType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_DescriptionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_DescriptionType"):
                opp_val = getattr(value, "carnot_DescriptionType", None)
                setattr(value, "carnot_DescriptionType", self)

    def getSymbols(self):
        # TODO: Implement getSymbols method
        pass

class carnot_IModelElement(ABC):

    def __init__(self, elementOid: str, carnot_IModelElement: "carnot_ViewableType" = None):
        self.elementOid = elementOid
        self.carnot_IModelElement = carnot_IModelElement
        
    @property
    def elementOid(self) -> str:
        return self.__elementOid

    @elementOid.setter
    def elementOid(self, elementOid: str):
        self.__elementOid = elementOid

    @property
    def carnot_IModelElement(self):
        return self.__carnot_IModelElement

    @carnot_IModelElement.setter
    def carnot_IModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_IModelElement__carnot_IModelElement", None)
        self.__carnot_IModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_ViewableType"):
                opp_val = getattr(old_value, "carnot_ViewableType", None)
                if opp_val == self:
                    setattr(old_value, "carnot_ViewableType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_ViewableType"):
                opp_val = getattr(value, "carnot_ViewableType", None)
                setattr(value, "carnot_ViewableType", self)

class carnot_EObject:

    pass
class carnot_IdentifiableReference:

    pass
class carnot_AttributeType:

    def __init__(self, mixed: str, group: str, any: str, name: str, type: str, value: str, carnot_AttributeType: "carnot_IExtensibleElement" = None, AttributeType: "carnot_IdentifiableReference" = None, attribute: "carnot_IdentifiableReference" = None, carnot_AttributeType128: "carnot_XmlTextNode" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.name = name
        self.type = type
        self.value = value
        self.carnot_AttributeType = carnot_AttributeType
        self.AttributeType = AttributeType
        self.attribute = attribute
        self.carnot_AttributeType128 = carnot_AttributeType128
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AttributeType__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifiableReference"):
                opp_val = getattr(old_value, "IdentifiableReference", None)
                if opp_val == self:
                    setattr(old_value, "IdentifiableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifiableReference"):
                opp_val = getattr(value, "IdentifiableReference", None)
                setattr(value, "IdentifiableReference", self)

    @property
    def AttributeType(self):
        return self.__AttributeType

    @AttributeType.setter
    def AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AttributeType__AttributeType", None)
        self.__AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reference"):
                opp_val = getattr(old_value, "reference", None)
                if opp_val == self:
                    setattr(old_value, "reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reference"):
                opp_val = getattr(value, "reference", None)
                setattr(value, "reference", self)

    @property
    def carnot_AttributeType(self):
        return self.__carnot_AttributeType

    @carnot_AttributeType.setter
    def carnot_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AttributeType__carnot_AttributeType", None)
        self.__carnot_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IExtensibleElement"):
                opp_val = getattr(old_value, "carnot_IExtensibleElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IExtensibleElement"):
                opp_val = getattr(value, "carnot_IExtensibleElement", None)
                if opp_val is None:
                    setattr(value, "carnot_IExtensibleElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carnot_AttributeType128(self):
        return self.__carnot_AttributeType128

    @carnot_AttributeType128.setter
    def carnot_AttributeType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_AttributeType__carnot_AttributeType128", None)
        self.__carnot_AttributeType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_XmlTextNode"):
                opp_val = getattr(old_value, "carnot_XmlTextNode", None)
                if opp_val == self:
                    setattr(old_value, "carnot_XmlTextNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_XmlTextNode"):
                opp_val = getattr(value, "carnot_XmlTextNode", None)
                setattr(value, "carnot_XmlTextNode", self)

    def setAttributeValue(self, value: str, type: str):
        # TODO: Implement setAttributeValue method
        pass

    def getAttributeValue(self) -> str:
        # TODO: Implement getAttributeValue method
        pass

class carnot_IExtensibleElement:

    pass
class carnot_IIdentifiableElement(ABC):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class carnot_Coordinates:

    def __init__(self, xPos: str, yPos: str, carnot_Coordinates: "carnot_IConnectionSymbol" = None):
        self.xPos = xPos
        self.yPos = yPos
        self.carnot_Coordinates = carnot_Coordinates
        
    @property
    def xPos(self) -> str:
        return self.__xPos

    @xPos.setter
    def xPos(self, xPos: str):
        self.__xPos = xPos

    @property
    def yPos(self) -> str:
        return self.__yPos

    @yPos.setter
    def yPos(self, yPos: str):
        self.__yPos = yPos

    @property
    def carnot_Coordinates(self):
        return self.__carnot_Coordinates

    @carnot_Coordinates.setter
    def carnot_Coordinates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_carnot_Coordinates__carnot_Coordinates", None)
        self.__carnot_Coordinates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carnot_IConnectionSymbol"):
                opp_val = getattr(old_value, "carnot_IConnectionSymbol", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carnot_IConnectionSymbol"):
                opp_val = getattr(value, "carnot_IConnectionSymbol", None)
                if opp_val is None:
                    setattr(value, "carnot_IConnectionSymbol", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
