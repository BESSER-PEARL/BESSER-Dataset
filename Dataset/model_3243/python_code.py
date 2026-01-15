from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class remes_ToSubModeEdge(ABC):

    pass
class ToCompositeModeEdge:

    pass
class remes_RemesDiagram:

    pass
class remes_Mode(ABC):

    def __init__(self, name: str, initialization: str, remes_Mode: "remes_RemesDiagram" = None):
        self.name = name
        self.initialization = initialization
        self.remes_Mode = remes_Mode
        
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
class remes_ToCompositeModeEdge(ABC):

    pass
class Mode:

    pass
class remes_CompositeMode(Mode):

    pass
class FromSubModeEdge:

    pass
class InitEdge:

    pass
class FromCompositeModeInitEdge:

    pass
class ToConditionalConnectorEdge:

    pass
class remes_EntryConditionalTopInitEdge(FromCompositeModeInitEdge, InitEdge, ToConditionalConnectorEdge):

    pass
class FromCompositeModeEdge:

    pass
class Edge:

    pass
class remes_EntryConditionalTopEdge(Edge, ToConditionalConnectorEdge, FromCompositeModeEdge):

    pass
class remes_ExitEdge(FromSubModeEdge, ToCompositeModeEdge, Edge):

    pass
class remes_ExitConditionalSubEdge(FromSubModeEdge, ToConditionalConnectorEdge, Edge):

    pass
class ToSubModeEdge:

    pass
class remes_EntryInitEdge(FromCompositeModeInitEdge, InitEdge, ToSubModeEdge):

    pass
class remes_EntryEdge(ToSubModeEdge, Edge, FromCompositeModeEdge):

    pass
class remes_InternalEdge(FromSubModeEdge, ToSubModeEdge, Edge):

    pass
class FromConditionalConnectorEdge:

    pass
class remes_ExitConditionalTopEdge(FromConditionalConnectorEdge, ToCompositeModeEdge, Edge):

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
class remes_ToConditionalConnectorEdge(ABC):

    pass
class remes_ConditionalConnector:

    def __init__(self, name: str, ConditionalConnector: "remes_CompositeMode" = None, connectTo8: set["remes_ToConditionalConnectorEdge"] = None, connectFrom10: set["remes_FromConditionalConnectorEdge"] = None, conditionalConnectors: "remes_CompositeMode" = None, ConditionalConnector17: "remes_FromConditionalConnectorEdge" = None, ConditionalConnector32: "remes_ToConditionalConnectorEdge" = None):
        self.name = name
        self.ConditionalConnector = ConditionalConnector
        self.connectTo8 = connectTo8 if connectTo8 is not None else set()
        self.connectFrom10 = connectFrom10 if connectFrom10 is not None else set()
        self.conditionalConnectors = conditionalConnectors
        self.ConditionalConnector17 = ConditionalConnector17
        self.ConditionalConnector32 = ConditionalConnector32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def ConditionalConnector32(self):
        return self.__ConditionalConnector32

    @ConditionalConnector32.setter
    def ConditionalConnector32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_ConditionalConnector__ConditionalConnector32", None)
        self.__ConditionalConnector32 = value
        
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

class remes_SubMode(Mode):

    def __init__(self, resourceClassA: str, resourceClassB: str, resourceClassC: str, invariant: str, isUrgent: str, SubMode: "remes_CompositeMode" = None, SubMode20: "remes_FromSubModeEdge" = None, connectFrom25: set["remes_FromSubModeEdge"] = None, subModes: "remes_CompositeMode" = None, SubMode35: "remes_ToSubModeEdge" = None, connectTo23: set["remes_ToSubModeEdge"] = None):
        self.resourceClassA = resourceClassA
        self.resourceClassB = resourceClassB
        self.resourceClassC = resourceClassC
        self.invariant = invariant
        self.isUrgent = isUrgent
        self.SubMode = SubMode
        self.SubMode20 = SubMode20
        self.connectFrom25 = connectFrom25 if connectFrom25 is not None else set()
        self.subModes = subModes
        self.SubMode35 = SubMode35
        self.connectTo23 = connectTo23 if connectTo23 is not None else set()
        
    @property
    def invariant(self) -> str:
        return self.__invariant

    @invariant.setter
    def invariant(self, invariant: str):
        self.__invariant = invariant

    @property
    def resourceClassC(self) -> str:
        return self.__resourceClassC

    @resourceClassC.setter
    def resourceClassC(self, resourceClassC: str):
        self.__resourceClassC = resourceClassC

    @property
    def resourceClassB(self) -> str:
        return self.__resourceClassB

    @resourceClassB.setter
    def resourceClassB(self, resourceClassB: str):
        self.__resourceClassB = resourceClassB

    @property
    def resourceClassA(self) -> str:
        return self.__resourceClassA

    @resourceClassA.setter
    def resourceClassA(self, resourceClassA: str):
        self.__resourceClassA = resourceClassA

    @property
    def isUrgent(self) -> str:
        return self.__isUrgent

    @isUrgent.setter
    def isUrgent(self, isUrgent: str):
        self.__isUrgent = isUrgent

    @property
    def connectTo23(self):
        return self.__connectTo23

    @connectTo23.setter
    def connectTo23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__connectTo23", None)
        self.__connectTo23 = value if value is not None else set()
        
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
    def SubMode35(self):
        return self.__SubMode35

    @SubMode35.setter
    def SubMode35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__SubMode35", None)
        self.__SubMode35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryEdges34"):
                opp_val = getattr(old_value, "entryEdges34", None)
                if opp_val == self:
                    setattr(old_value, "entryEdges34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryEdges34"):
                opp_val = getattr(value, "entryEdges34", None)
                setattr(value, "entryEdges34", self)

    @property
    def connectFrom25(self):
        return self.__connectFrom25

    @connectFrom25.setter
    def connectFrom25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__connectFrom25", None)
        self.__connectFrom25 = value if value is not None else set()
        
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
    def subModes(self):
        return self.__subModes

    @subModes.setter
    def subModes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_remes_SubMode__subModes", None)
        self.__subModes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeMode27"):
                opp_val = getattr(old_value, "CompositeMode27", None)
                if opp_val == self:
                    setattr(old_value, "CompositeMode27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeMode27"):
                opp_val = getattr(value, "CompositeMode27", None)
                setattr(value, "CompositeMode27", self)

class remes_FromCompositeModeEdge(ABC):

    pass
class remes_FromCompositeModeInitEdge(ABC):

    pass