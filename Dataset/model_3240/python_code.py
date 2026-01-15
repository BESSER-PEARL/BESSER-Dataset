from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypes(Enum):
    boolean = "boolean"
    natural = "natural"
    clock = "clock"
    float = "float"
    integer = "integer"
class ResourceTypes(Enum):
    cpu = "cpu"
    memory = "memory"
    bandwidth = "bandwidth"
    power = "power"
    port = "port"


############################################
# Definition of Classes
############################################

class remes_WriteEdge:

    pass
class ResourceRoot:

    pass
class ActionRoot:

    pass
class Referable:

    pass
class remes_Referable(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EntryPoint:

    pass
class ExitPoint:

    pass
class remes_Edge:

    def __init__(self, actionGuard: str, actionBody: str, Edge: "remes_EntryPoint" = None, Edge30: "remes_ExitPoint" = None, remes_Edge: "LogicalRoot" = None, exitEdges: "remes_ExitPoint" = None, entryEdges: "remes_EntryPoint" = None, remes_Edge44: "ActionRoot" = None):
        self.actionGuard = actionGuard
        self.actionBody = actionBody
        self.Edge = Edge
        self.Edge30 = Edge30
        self.remes_Edge = remes_Edge
        self.exitEdges = exitEdges
        self.entryEdges = entryEdges
        self.remes_Edge44 = remes_Edge44
        
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

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectTo"):
                opp_val = getattr(old_value, "connectTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectTo"):
                opp_val = getattr(value, "connectTo", None)
                if opp_val is None:
                    setattr(value, "connectTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def remes_Edge(self):
        return self.__remes_Edge

    @remes_Edge.setter
    def remes_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__remes_Edge", None)
        self.__remes_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalRoot38"):
                opp_val = getattr(old_value, "LogicalRoot38", None)
                if opp_val == self:
                    setattr(old_value, "LogicalRoot38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalRoot38"):
                opp_val = getattr(value, "LogicalRoot38", None)
                setattr(value, "LogicalRoot38", self)

    @property
    def remes_Edge44(self):
        return self.__remes_Edge44

    @remes_Edge44.setter
    def remes_Edge44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__remes_Edge44", None)
        self.__remes_Edge44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionRoot"):
                opp_val = getattr(old_value, "ActionRoot", None)
                if opp_val == self:
                    setattr(old_value, "ActionRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionRoot"):
                opp_val = getattr(value, "ActionRoot", None)
                setattr(value, "ActionRoot", self)

    @property
    def exitEdges(self):
        return self.__exitEdges

    @exitEdges.setter
    def exitEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__exitEdges", None)
        self.__exitEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExitPoint40"):
                opp_val = getattr(old_value, "ExitPoint40", None)
                if opp_val == self:
                    setattr(old_value, "ExitPoint40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExitPoint40"):
                opp_val = getattr(value, "ExitPoint40", None)
                setattr(value, "ExitPoint40", self)

    @property
    def entryEdges(self):
        return self.__entryEdges

    @entryEdges.setter
    def entryEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__entryEdges", None)
        self.__entryEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntryPoint42"):
                opp_val = getattr(old_value, "EntryPoint42", None)
                if opp_val == self:
                    setattr(old_value, "EntryPoint42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntryPoint42"):
                opp_val = getattr(value, "EntryPoint42", None)
                setattr(value, "EntryPoint42", self)

    @property
    def Edge30(self):
        return self.__Edge30

    @Edge30.setter
    def Edge30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Edge__Edge30", None)
        self.__Edge30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectFrom29"):
                opp_val = getattr(old_value, "connectFrom29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectFrom29"):
                opp_val = getattr(value, "connectFrom29", None)
                if opp_val is None:
                    setattr(value, "connectFrom29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remes_InitEdge:

    def __init__(self, initialization: str, InitEdge: "remes_InitPoint" = None, remes_InitEdge49: "ActionRoot" = None, initEdge: "remes_InitPoint" = None, remes_InitEdge: "remes_EntryPoint" = None):
        self.initialization = initialization
        self.InitEdge = InitEdge
        self.remes_InitEdge49 = remes_InitEdge49
        self.initEdge = initEdge
        self.remes_InitEdge = remes_InitEdge
        
    @property
    def initialization(self) -> str:
        return self.__initialization

    @initialization.setter
    def initialization(self, initialization: str):
        self.__initialization = initialization

    @property
    def remes_InitEdge(self):
        return self.__remes_InitEdge

    @remes_InitEdge.setter
    def remes_InitEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_InitEdge__remes_InitEdge", None)
        self.__remes_InitEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "remes_EntryPoint"):
                opp_val = getattr(old_value, "remes_EntryPoint", None)
                if opp_val == self:
                    setattr(old_value, "remes_EntryPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "remes_EntryPoint"):
                opp_val = getattr(value, "remes_EntryPoint", None)
                setattr(value, "remes_EntryPoint", self)

    @property
    def initEdge(self):
        return self.__initEdge

    @initEdge.setter
    def initEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_InitEdge__initEdge", None)
        self.__initEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InitPoint46"):
                opp_val = getattr(old_value, "InitPoint46", None)
                if opp_val == self:
                    setattr(old_value, "InitPoint46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InitPoint46"):
                opp_val = getattr(value, "InitPoint46", None)
                setattr(value, "InitPoint46", self)

    @property
    def remes_InitEdge49(self):
        return self.__remes_InitEdge49

    @remes_InitEdge49.setter
    def remes_InitEdge49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_InitEdge__remes_InitEdge49", None)
        self.__remes_InitEdge49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionRoot50"):
                opp_val = getattr(old_value, "ActionRoot50", None)
                if opp_val == self:
                    setattr(old_value, "ActionRoot50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionRoot50"):
                opp_val = getattr(value, "ActionRoot50", None)
                setattr(value, "ActionRoot50", self)

    @property
    def InitEdge(self):
        return self.__InitEdge

    @InitEdge.setter
    def InitEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_InitEdge__InitEdge", None)
        self.__InitEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectFrom"):
                opp_val = getattr(old_value, "connectFrom", None)
                if opp_val == self:
                    setattr(old_value, "connectFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectFrom"):
                opp_val = getattr(value, "connectFrom", None)
                setattr(value, "connectFrom", self)

class Point:

    pass
class remes_Point(ABC):

    pass
class LogicalRoot:

    pass
class remes_WritePoint(Point):

    pass
class remes_CompositeExitPoint(EntryPoint):

    pass
class remes_CompositeEntryPoint(ExitPoint):

    pass
class Mode:

    pass
class remes_SubMode(Mode):

    def __init__(self, invariant: str, isUrgent: bool, SubMode: "remes_CompositeMode" = None, subModes: "remes_CompositeMode" = None, remes_SubMode: "LogicalRoot" = None):
        self.invariant = invariant
        self.isUrgent = isUrgent
        self.SubMode = SubMode
        self.subModes = subModes
        self.remes_SubMode = remes_SubMode
        
    @property
    def isUrgent(self) -> bool:
        return self.__isUrgent

    @isUrgent.setter
    def isUrgent(self, isUrgent: bool):
        self.__isUrgent = isUrgent

    @property
    def invariant(self) -> str:
        return self.__invariant

    @invariant.setter
    def invariant(self, invariant: str):
        self.__invariant = invariant

    @property
    def remes_SubMode(self):
        return self.__remes_SubMode

    @remes_SubMode.setter
    def remes_SubMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__remes_SubMode", None)
        self.__remes_SubMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalRoot"):
                opp_val = getattr(old_value, "LogicalRoot", None)
                if opp_val == self:
                    setattr(old_value, "LogicalRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalRoot"):
                opp_val = getattr(value, "LogicalRoot", None)
                setattr(value, "LogicalRoot", self)

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

class remes_CompositeMode(Mode):

    pass
class remes_Constant(Referable):

    def __init__(self, type: str, value: str, global: bool, Constant: "remes_Mode" = None, constants: "remes_Mode" = None):
        self.type = type
        self.value = value
        self.global = global
        self.Constant = Constant
        self.constants = constants
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def constants(self):
        return self.__constants

    @constants.setter
    def constants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Constant__constants", None)
        self.__constants = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mode56"):
                opp_val = getattr(old_value, "Mode56", None)
                if opp_val == self:
                    setattr(old_value, "Mode56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mode56"):
                opp_val = getattr(value, "Mode56", None)
                setattr(value, "Mode56", self)

    @property
    def Constant(self):
        return self.__Constant

    @Constant.setter
    def Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Constant__Constant", None)
        self.__Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scope8"):
                opp_val = getattr(old_value, "scope8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scope8"):
                opp_val = getattr(value, "scope8", None)
                if opp_val is None:
                    setattr(value, "scope8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class remes_Resource(Referable):

    def __init__(self, expression: str, type: str, Resource: "remes_Mode" = None, resources: "remes_Mode" = None, remes_Resource: "ResourceRoot" = None):
        self.expression = expression
        self.type = type
        self.Resource = Resource
        self.resources = resources
        self.remes_Resource = remes_Resource
        
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
    def remes_Resource(self):
        return self.__remes_Resource

    @remes_Resource.setter
    def remes_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Resource__remes_Resource", None)
        self.__remes_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceRoot"):
                opp_val = getattr(old_value, "ResourceRoot", None)
                if opp_val == self:
                    setattr(old_value, "ResourceRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceRoot"):
                opp_val = getattr(value, "ResourceRoot", None)
                setattr(value, "ResourceRoot", self)

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
            if hasattr(old_value, "scope6"):
                opp_val = getattr(old_value, "scope6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scope6"):
                opp_val = getattr(value, "scope6", None)
                if opp_val is None:
                    setattr(value, "scope6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Mode53"):
                opp_val = getattr(old_value, "Mode53", None)
                if opp_val == self:
                    setattr(old_value, "Mode53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mode53"):
                opp_val = getattr(value, "Mode53", None)
                setattr(value, "Mode53", self)

class remes_Variable(Referable):

    def __init__(self, value: str, type: str, vectorSize: int, global: bool, readable: bool, writable: bool, Variable: "remes_Mode" = None, variables: "remes_Mode" = None):
        self.value = value
        self.type = type
        self.vectorSize = vectorSize
        self.global = global
        self.readable = readable
        self.writable = writable
        self.Variable = Variable
        self.variables = variables
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def vectorSize(self) -> int:
        return self.__vectorSize

    @vectorSize.setter
    def vectorSize(self, vectorSize: int):
        self.__vectorSize = vectorSize

    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def writable(self) -> bool:
        return self.__writable

    @writable.setter
    def writable(self, writable: bool):
        self.__writable = writable

    @property
    def readable(self) -> bool:
        return self.__readable

    @readable.setter
    def readable(self, readable: bool):
        self.__readable = readable

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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

class ControlPath:

    pass
class remes_ExitPoint(Point):

    pass
class remes_EntryPoint(Point):

    pass
class remes_ControlPath(ABC):

    def __init__(self, name: str, container: "remes_EntryPoint" = None, container3: "remes_ExitPoint" = None, ControlPath: "remes_EntryPoint" = None, ControlPath32: "remes_ExitPoint" = None):
        self.name = name
        self.container = container
        self.container3 = container3
        self.ControlPath = ControlPath
        self.ControlPath32 = ControlPath32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def container3(self):
        return self.__container3

    @container3.setter
    def container3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ControlPath__container3", None)
        self.__container3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExitPoint"):
                opp_val = getattr(old_value, "ExitPoint", None)
                if opp_val == self:
                    setattr(old_value, "ExitPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExitPoint"):
                opp_val = getattr(value, "ExitPoint", None)
                setattr(value, "ExitPoint", self)

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ControlPath__container", None)
        self.__container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntryPoint"):
                opp_val = getattr(old_value, "EntryPoint", None)
                if opp_val == self:
                    setattr(old_value, "EntryPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntryPoint"):
                opp_val = getattr(value, "EntryPoint", None)
                setattr(value, "EntryPoint", self)

    @property
    def ControlPath(self):
        return self.__ControlPath

    @ControlPath.setter
    def ControlPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ControlPath__ControlPath", None)
        self.__ControlPath = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryPoint"):
                opp_val = getattr(old_value, "entryPoint", None)
                if opp_val == self:
                    setattr(old_value, "entryPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryPoint"):
                opp_val = getattr(value, "entryPoint", None)
                setattr(value, "entryPoint", self)

    @property
    def ControlPath32(self):
        return self.__ControlPath32

    @ControlPath32.setter
    def ControlPath32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ControlPath__ControlPath32", None)
        self.__ControlPath32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exitPoint"):
                opp_val = getattr(old_value, "exitPoint", None)
                if opp_val == self:
                    setattr(old_value, "exitPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exitPoint"):
                opp_val = getattr(value, "exitPoint", None)
                setattr(value, "exitPoint", self)

class remes_Mode(ControlPath):

    def __init__(self, initialization: str, remes_Mode: "remes_RemesDiagram" = None, scope: set["remes_Variable"] = None, scope6: set["remes_Resource"] = None, scope8: set["remes_Constant"] = None, Mode: "remes_Variable" = None, Mode53: "remes_Resource" = None, Mode56: "remes_Constant" = None):
        self.initialization = initialization
        self.remes_Mode = remes_Mode
        self.scope = scope if scope is not None else set()
        self.scope6 = scope6 if scope6 is not None else set()
        self.scope8 = scope8 if scope8 is not None else set()
        self.Mode = Mode
        self.Mode53 = Mode53
        self.Mode56 = Mode56
        
    @property
    def initialization(self) -> str:
        return self.__initialization

    @initialization.setter
    def initialization(self, initialization: str):
        self.__initialization = initialization

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
    def scope8(self):
        return self.__scope8

    @scope8.setter
    def scope8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__scope8", None)
        self.__scope8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constant"):
                    opp_val = getattr(item, "Constant", None)
                    
                    if opp_val == self:
                        setattr(item, "Constant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constant"):
                    opp_val = getattr(item, "Constant", None)
                    
                    setattr(item, "Constant", self)
                    

    @property
    def scope6(self):
        return self.__scope6

    @scope6.setter
    def scope6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__scope6", None)
        self.__scope6 = value if value is not None else set()
        
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
    def Mode53(self):
        return self.__Mode53

    @Mode53.setter
    def Mode53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__Mode53", None)
        self.__Mode53 = value
        
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
                    

    @property
    def Mode56(self):
        return self.__Mode56

    @Mode56.setter
    def Mode56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_Mode__Mode56", None)
        self.__Mode56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constants"):
                opp_val = getattr(old_value, "constants", None)
                if opp_val == self:
                    setattr(old_value, "constants", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constants"):
                opp_val = getattr(value, "constants", None)
                setattr(value, "constants", self)

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

    def findVariableByName(self, name: str) -> str:
        # TODO: Implement findVariableByName method
        pass

    def findResourceByName(self, name: str) -> str:
        # TODO: Implement findResourceByName method
        pass

    def findConstantByName(self, name: str) -> str:
        # TODO: Implement findConstantByName method
        pass

class remes_RemesDiagram:

    pass
class remes_InitPoint(Point):

    pass
class remes_ConditionalConnector(ControlPath):

    pass