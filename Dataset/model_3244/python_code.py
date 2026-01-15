from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResourceTypes(Enum):
    cpu = "cpu"
    memory = "memory"
    bandwidth = "bandwidth"
    power = "power"
    port = "port"
class PrimitiveTypes(Enum):
    boolean = "boolean"
    integer = "integer"
    natural = "natural"
    clock = "clock"


############################################
# Definition of Classes
############################################

class remes_Resource:

    def __init__(self, expression: str, type: str, Resource: "remes_SubMode" = None, resources: "remes_SubMode" = None):
        self.expression = expression
        self.type = type
        self.Resource = Resource
        self.resources = resources
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Resource__resources", None)
        self.__resources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubMode41"):
                opp_val = getattr(old_value, "SubMode41", None)
                if opp_val == self:
                    setattr(old_value, "SubMode41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubMode41"):
                opp_val = getattr(value, "SubMode41", None)
                setattr(value, "SubMode41", self)

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Resource__Resource", None)
        self.__Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scope30"):
                opp_val = getattr(old_value, "scope30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scope30"):
                opp_val = getattr(value, "scope30", None)
                if opp_val is None:
                    setattr(value, "scope30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remes_Variable:

    def __init__(self, name: str, value: str, type: str, vectorSize: int, global: bool, readable: bool, writable: bool, Variable: "remes_Mode" = None, variables: "remes_Mode" = None):
        self.name = name
        self.value = value
        self.type = type
        self.vectorSize = vectorSize
        self.global = global
        self.readable = readable
        self.writable = writable
        self.Variable = Variable
        self.variables = variables
        
    @property
    def readable(self) -> bool:
        return self.__readable

    @readable.setter
    def readable(self, readable: bool):
        self.__readable = readable

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
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vectorSize(self) -> int:
        return self.__vectorSize

    @vectorSize.setter
    def vectorSize(self, vectorSize: int):
        self.__vectorSize = vectorSize

    @property
    def writable(self) -> bool:
        return self.__writable

    @writable.setter
    def writable(self, writable: bool):
        self.__writable = writable

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scope"):
                opp_val = getattr(old_value, "scope", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scope"):
                opp_val = getattr(value, "scope", None)
                if opp_val is None:
                    setattr(value, "scope", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Variable__variables", None)
        self.__variables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mode"):
                opp_val = getattr(old_value, "Mode", None)
                if opp_val == self:
                    setattr(old_value, "Mode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mode"):
                opp_val = getattr(value, "Mode", None)
                setattr(value, "Mode", self)

class remes_Mode(ABC):

    def __init__(self, name: str, initialization: str, remes_Mode: "remes_RemesDiagram" = None, scope: set["remes_Variable"] = None, Mode: "remes_Variable" = None):
        self.name = name
        self.initialization = initialization
        self.remes_Mode = remes_Mode
        self.scope = scope if scope is not None else set()
        self.Mode = Mode
        
    @property
    def initialization(self) -> str:
        return self.__initialization

    @initialization.setter
    def initialization(self, initialization: str):
        self.__initialization = initialization

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def remes_Mode(self):
        return self.__remes_Mode

    @remes_Mode.setter
    def remes_Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__remes_Mode", None)
        self.__remes_Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remes_RemesDiagram"):
                opp_val = getattr(old_value, "remes_RemesDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remes_RemesDiagram"):
                opp_val = getattr(value, "remes_RemesDiagram", None)
                if opp_val is None:
                    setattr(value, "remes_RemesDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Mode(self):
        return self.__Mode

    @Mode.setter
    def Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__Mode", None)
        self.__Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables"):
                opp_val = getattr(old_value, "variables", None)
                if opp_val == self:
                    setattr(old_value, "variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables"):
                opp_val = getattr(value, "variables", None)
                setattr(value, "variables", self)

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__scope", None)
        self.__scope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

class remes_InitEdge(ABC):

    def __init__(self, initialization: str):
        self.initialization = initialization
        
    @property
    def initialization(self) -> str:
        return self.__initialization

    @initialization.setter
    def initialization(self, initialization: str):
        self.__initialization = initialization

class remes_FromSubModeEdge(ABC):

    pass
class remes_ToSubModeEdge(ABC):

    pass
class remes_RemesDiagram:

    pass
class ToCompositeModeEdge:

    pass
class FromSubModeEdge:

    pass
class InitEdge:

    pass
class FromCompositeModeInitEdge:

    pass
class ToConditionalConnectorEdge:

    pass
class remes_EntryConditionalTopInitEdge(ToConditionalConnectorEdge, InitEdge, FromCompositeModeInitEdge):

    pass
class remes_ToConditionalConnectorEdge(ABC):

    pass
class remes_ConditionalConnector:

    def __init__(self, name: str, connectFrom10: set["remes_FromConditionalConnectorEdge"] = None, conditionalConnectors: "remes_CompositeMode" = None, ConditionalConnector: "remes_CompositeMode" = None, connectTo8: set["remes_ToConditionalConnectorEdge"] = None, ConditionalConnector17: "remes_FromConditionalConnectorEdge" = None, ConditionalConnector35: "remes_ToConditionalConnectorEdge" = None):
        self.name = name
        self.connectFrom10 = connectFrom10 if connectFrom10 is not None else set()
        self.conditionalConnectors = conditionalConnectors
        self.ConditionalConnector = ConditionalConnector
        self.connectTo8 = connectTo8 if connectTo8 is not None else set()
        self.ConditionalConnector17 = ConditionalConnector17
        self.ConditionalConnector35 = ConditionalConnector35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ConditionalConnector17(self):
        return self.__ConditionalConnector17

    @ConditionalConnector17.setter
    def ConditionalConnector17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__ConditionalConnector17", None)
        self.__ConditionalConnector17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exitEdges"):
                opp_val = getattr(old_value, "exitEdges", None)
                if opp_val == self:
                    setattr(old_value, "exitEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exitEdges"):
                opp_val = getattr(value, "exitEdges", None)
                setattr(value, "exitEdges", self)

    @property
    def connectTo8(self):
        return self.__connectTo8

    @connectTo8.setter
    def connectTo8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__connectTo8", None)
        self.__connectTo8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToConditionalConnectorEdge"):
                    opp_val = getattr(item, "ToConditionalConnectorEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ToConditionalConnectorEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToConditionalConnectorEdge"):
                    opp_val = getattr(item, "ToConditionalConnectorEdge", None)
                    
                    setattr(item, "ToConditionalConnectorEdge", self)
                    

    @property
    def conditionalConnectors(self):
        return self.__conditionalConnectors

    @conditionalConnectors.setter
    def conditionalConnectors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__conditionalConnectors", None)
        self.__conditionalConnectors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeMode"):
                opp_val = getattr(old_value, "CompositeMode", None)
                if opp_val == self:
                    setattr(old_value, "CompositeMode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeMode"):
                opp_val = getattr(value, "CompositeMode", None)
                setattr(value, "CompositeMode", self)

    @property
    def connectFrom10(self):
        return self.__connectFrom10

    @connectFrom10.setter
    def connectFrom10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__connectFrom10", None)
        self.__connectFrom10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FromConditionalConnectorEdge"):
                    opp_val = getattr(item, "FromConditionalConnectorEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "FromConditionalConnectorEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FromConditionalConnectorEdge"):
                    opp_val = getattr(item, "FromConditionalConnectorEdge", None)
                    
                    setattr(item, "FromConditionalConnectorEdge", self)
                    

    @property
    def ConditionalConnector(self):
        return self.__ConditionalConnector

    @ConditionalConnector.setter
    def ConditionalConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__ConditionalConnector", None)
        self.__ConditionalConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent6"):
                opp_val = getattr(old_value, "parent6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent6"):
                opp_val = getattr(value, "parent6", None)
                if opp_val is None:
                    setattr(value, "parent6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ConditionalConnector35(self):
        return self.__ConditionalConnector35

    @ConditionalConnector35.setter
    def ConditionalConnector35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__ConditionalConnector35", None)
        self.__ConditionalConnector35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryEdges"):
                opp_val = getattr(old_value, "entryEdges", None)
                if opp_val == self:
                    setattr(old_value, "entryEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryEdges"):
                opp_val = getattr(value, "entryEdges", None)
                setattr(value, "entryEdges", self)

class remes_FromCompositeModeEdge(ABC):

    pass
class FromCompositeModeEdge:

    pass
class Edge:

    pass
class remes_EntryConditionalTopEdge(Edge, ToConditionalConnectorEdge, FromCompositeModeEdge):

    pass
class remes_ExitConditionalSubEdge(Edge, ToConditionalConnectorEdge, FromSubModeEdge):

    pass
class remes_ExitEdge(ToCompositeModeEdge, Edge, FromSubModeEdge):

    pass
class ToSubModeEdge:

    pass
class remes_EntryEdge(ToSubModeEdge, Edge, FromCompositeModeEdge):

    pass
class remes_InternalEdge(ToSubModeEdge, Edge, FromSubModeEdge):

    pass
class remes_EntryInitEdge(ToSubModeEdge, InitEdge, FromCompositeModeInitEdge):

    pass
class FromConditionalConnectorEdge:

    pass
class remes_ExitConditionalTopEdge(ToCompositeModeEdge, FromConditionalConnectorEdge, Edge):

    pass
class remes_EntryConditionalSubEdge(FromConditionalConnectorEdge, ToSubModeEdge, Edge):

    pass
class remes_Edge(ABC):

    def __init__(self, actionGuard: str, actionBody: str):
        self.actionGuard = actionGuard
        self.actionBody = actionBody
        
    @property
    def actionBody(self) -> str:
        return self.__actionBody

    @actionBody.setter
    def actionBody(self, actionBody: str):
        self.__actionBody = actionBody

    @property
    def actionGuard(self) -> str:
        return self.__actionGuard

    @actionGuard.setter
    def actionGuard(self, actionGuard: str):
        self.__actionGuard = actionGuard

class remes_FromConditionalConnectorEdge(ABC):

    pass
class remes_FromCompositeModeInitEdge(ABC):

    pass
class remes_ToCompositeModeEdge(ABC):

    pass
class Mode:

    pass
class remes_SubMode(Mode):

    def __init__(self, invariant: str, isUrgent: bool, SubMode: "remes_CompositeMode" = None, connectTo24: set["remes_ToSubModeEdge"] = None, connectFrom26: set["remes_FromSubModeEdge"] = None, SubMode20: "remes_FromSubModeEdge" = None, subModes: "remes_CompositeMode" = None, scope30: set["remes_Resource"] = None, SubMode38: "remes_ToSubModeEdge" = None, SubMode41: "remes_Resource" = None):
        self.invariant = invariant
        self.isUrgent = isUrgent
        self.SubMode = SubMode
        self.connectTo24 = connectTo24 if connectTo24 is not None else set()
        self.connectFrom26 = connectFrom26 if connectFrom26 is not None else set()
        self.SubMode20 = SubMode20
        self.subModes = subModes
        self.scope30 = scope30 if scope30 is not None else set()
        self.SubMode38 = SubMode38
        self.SubMode41 = SubMode41
        
    @property
    def invariant(self) -> str:
        return self.__invariant

    @invariant.setter
    def invariant(self, invariant: str):
        self.__invariant = invariant

    @property
    def isUrgent(self) -> bool:
        return self.__isUrgent

    @isUrgent.setter
    def isUrgent(self, isUrgent: bool):
        self.__isUrgent = isUrgent

    @property
    def SubMode41(self):
        return self.__SubMode41

    @SubMode41.setter
    def SubMode41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__SubMode41", None)
        self.__SubMode41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources"):
                opp_val = getattr(old_value, "resources", None)
                if opp_val == self:
                    setattr(old_value, "resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources"):
                opp_val = getattr(value, "resources", None)
                setattr(value, "resources", self)

    @property
    def SubMode38(self):
        return self.__SubMode38

    @SubMode38.setter
    def SubMode38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__SubMode38", None)
        self.__SubMode38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryEdges37"):
                opp_val = getattr(old_value, "entryEdges37", None)
                if opp_val == self:
                    setattr(old_value, "entryEdges37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryEdges37"):
                opp_val = getattr(value, "entryEdges37", None)
                setattr(value, "entryEdges37", self)

    @property
    def subModes(self):
        return self.__subModes

    @subModes.setter
    def subModes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__subModes", None)
        self.__subModes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeMode28"):
                opp_val = getattr(old_value, "CompositeMode28", None)
                if opp_val == self:
                    setattr(old_value, "CompositeMode28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeMode28"):
                opp_val = getattr(value, "CompositeMode28", None)
                setattr(value, "CompositeMode28", self)

    @property
    def connectTo24(self):
        return self.__connectTo24

    @connectTo24.setter
    def connectTo24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__connectTo24", None)
        self.__connectTo24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToSubModeEdge"):
                    opp_val = getattr(item, "ToSubModeEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ToSubModeEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToSubModeEdge"):
                    opp_val = getattr(item, "ToSubModeEdge", None)
                    
                    setattr(item, "ToSubModeEdge", self)
                    

    @property
    def scope30(self):
        return self.__scope30

    @scope30.setter
    def scope30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__scope30", None)
        self.__scope30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    

    @property
    def SubMode(self):
        return self.__SubMode

    @SubMode.setter
    def SubMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__SubMode", None)
        self.__SubMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectFrom26(self):
        return self.__connectFrom26

    @connectFrom26.setter
    def connectFrom26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__connectFrom26", None)
        self.__connectFrom26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FromSubModeEdge"):
                    opp_val = getattr(item, "FromSubModeEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "FromSubModeEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FromSubModeEdge"):
                    opp_val = getattr(item, "FromSubModeEdge", None)
                    
                    setattr(item, "FromSubModeEdge", self)
                    

    @property
    def SubMode20(self):
        return self.__SubMode20

    @SubMode20.setter
    def SubMode20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__SubMode20", None)
        self.__SubMode20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exitEdges19"):
                opp_val = getattr(old_value, "exitEdges19", None)
                if opp_val == self:
                    setattr(old_value, "exitEdges19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exitEdges19"):
                opp_val = getattr(value, "exitEdges19", None)
                setattr(value, "exitEdges19", self)

class remes_CompositeMode(Mode):

    pass