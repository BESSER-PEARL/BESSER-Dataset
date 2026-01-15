from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    NORMAL = "NORMAL"
    CONDITIONAL = "CONDITIONAL"
    REFERENCE = "REFERENCE"
    TEXTUAL = "TEXTUAL"
class TransitionType(Enum):
    WEAKABORT = "WEAKABORT"
    STRONGABORT = "STRONGABORT"
    NORMALTERMINATION = "NORMALTERMINATION"


############################################
# Definition of Classes
############################################

class TextualCode:

    pass
class synccharts_TextualCode:

    pass
class synccharts_EObject:

    pass
class Action:

    pass
class synccharts_Substitution:

    def __init__(self, formal: str, actual: str, renamings: "synccharts_Scope" = None, Substitution: "synccharts_Scope" = None):
        self.formal = formal
        self.actual = actual
        self.renamings = renamings
        self.Substitution = Substitution
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, actual: str):
        self.__actual = actual

    @property
    def renamings(self):
        return self.__renamings

    @renamings.setter
    def renamings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Substitution__renamings", None)
        self.__renamings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope"):
                opp_val = getattr(old_value, "Scope", None)
                if opp_val == self:
                    setattr(old_value, "Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope"):
                opp_val = getattr(value, "Scope", None)
                setattr(value, "Scope", self)

    @property
    def Substitution(self):
        return self.__Substitution

    @Substitution.setter
    def Substitution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Substitution__Substitution", None)
        self.__Substitution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentScope"):
                opp_val = getattr(old_value, "parentScope", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentScope"):
                opp_val = getattr(value, "parentScope", None)
                if opp_val is None:
                    setattr(value, "parentScope", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Scope:

    pass
class synccharts_State(Scope):

    def __init__(self, type: str, isInitial: bool, isFinal: bool, sourceState: set["synccharts_Transition"] = None, State: "synccharts_Region" = None, State13: "synccharts_Region" = None, parentState: set["synccharts_Region"] = None, states: "synccharts_Region" = None, targetState: set["synccharts_Transition"] = None, State22: "synccharts_Transition" = None, State24: "synccharts_Transition" = None):
        self.type = type
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.sourceState = sourceState if sourceState is not None else set()
        self.State = State
        self.State13 = State13
        self.parentState = parentState if parentState is not None else set()
        self.states = states
        self.targetState = targetState if targetState is not None else set()
        self.State22 = State22
        self.State24 = State24
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentRegion"):
                opp_val = getattr(old_value, "parentRegion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentRegion"):
                opp_val = getattr(value, "parentRegion", None)
                if opp_val is None:
                    setattr(value, "parentRegion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentState(self):
        return self.__parentState

    @parentState.setter
    def parentState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__parentState", None)
        self.__parentState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    if opp_val == self:
                        setattr(item, "Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    setattr(item, "Region", self)
                    

    @property
    def State24(self):
        return self.__State24

    @State24.setter
    def State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__State24", None)
        self.__State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region17"):
                opp_val = getattr(old_value, "Region17", None)
                if opp_val == self:
                    setattr(old_value, "Region17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region17"):
                opp_val = getattr(value, "Region17", None)
                setattr(value, "Region17", self)

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__State13", None)
        self.__State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "regions"):
                opp_val = getattr(old_value, "regions", None)
                if opp_val == self:
                    setattr(old_value, "regions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "regions"):
                opp_val = getattr(value, "regions", None)
                setattr(value, "regions", self)

    @property
    def State22(self):
        return self.__State22

    @State22.setter
    def State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__State22", None)
        self.__State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def targetState(self):
        return self.__targetState

    @targetState.setter
    def targetState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__targetState", None)
        self.__targetState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition20"):
                    opp_val = getattr(item, "Transition20", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition20"):
                    opp_val = getattr(item, "Transition20", None)
                    
                    setattr(item, "Transition20", self)
                    

    @property
    def sourceState(self):
        return self.__sourceState

    @sourceState.setter
    def sourceState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_State__sourceState", None)
        self.__sourceState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

class synccharts_Region(Scope):

    pass
class synccharts_Signal:

    pass
class synccharts_Variable:

    pass
class synccharts_Transition(Action):

    def __init__(self, priority: int, type: str, isHistory: bool, Transition: "synccharts_State" = None, Transition20: "synccharts_State" = None, incomingTransitions: "synccharts_State" = None, outgoingTransitions: "synccharts_State" = None):
        self.priority = priority
        self.type = type
        self.isHistory = isHistory
        self.Transition = Transition
        self.Transition20 = Transition20
        self.incomingTransitions = incomingTransitions
        self.outgoingTransitions = outgoingTransitions
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isHistory(self) -> bool:
        return self.__isHistory

    @isHistory.setter
    def isHistory(self, isHistory: bool):
        self.__isHistory = isHistory

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def Transition20(self):
        return self.__Transition20

    @Transition20.setter
    def Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Transition__Transition20", None)
        self.__Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetState"):
                opp_val = getattr(old_value, "targetState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetState"):
                opp_val = getattr(value, "targetState", None)
                if opp_val is None:
                    setattr(value, "targetState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceState"):
                opp_val = getattr(old_value, "sourceState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceState"):
                opp_val = getattr(value, "sourceState", None)
                if opp_val is None:
                    setattr(value, "sourceState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State22"):
                opp_val = getattr(old_value, "State22", None)
                if opp_val == self:
                    setattr(old_value, "State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State22"):
                opp_val = getattr(value, "State22", None)
                setattr(value, "State22", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State24"):
                opp_val = getattr(old_value, "State24", None)
                if opp_val == self:
                    setattr(old_value, "State24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State24"):
                opp_val = getattr(value, "State24", None)
                setattr(value, "State24", self)

class synccharts_Expression:

    pass
class synccharts_Effect(ABC):

    pass
class Annotatable:

    pass
class synccharts_Scope(Annotatable):

    def __init__(self, id: str, label: str, interfaceDeclaration: str, Scope: "synccharts_Substitution" = None, synccharts_Scope31: "synccharts_Action" = None, synccharts_Scope34: set["synccharts_Action"] = None, synccharts_Scope: set["synccharts_Signal"] = None, synccharts_Scope28: set["synccharts_Variable"] = None, synccharts_Scope37: set["synccharts_Action"] = None, synccharts_Scope40: set["synccharts_Action"] = None, synccharts_Scope43: "synccharts_EObject" = None, synccharts_Scope45: "synccharts_EObject" = None, synccharts_Scope48: set["synccharts_TextualCode"] = None, parentScope: set["synccharts_Substitution"] = None):
        self.id = id
        self.label = label
        self.interfaceDeclaration = interfaceDeclaration
        self.Scope = Scope
        self.synccharts_Scope31 = synccharts_Scope31
        self.synccharts_Scope34 = synccharts_Scope34 if synccharts_Scope34 is not None else set()
        self.synccharts_Scope = synccharts_Scope if synccharts_Scope is not None else set()
        self.synccharts_Scope28 = synccharts_Scope28 if synccharts_Scope28 is not None else set()
        self.synccharts_Scope37 = synccharts_Scope37 if synccharts_Scope37 is not None else set()
        self.synccharts_Scope40 = synccharts_Scope40 if synccharts_Scope40 is not None else set()
        self.synccharts_Scope43 = synccharts_Scope43
        self.synccharts_Scope45 = synccharts_Scope45
        self.synccharts_Scope48 = synccharts_Scope48 if synccharts_Scope48 is not None else set()
        self.parentScope = parentScope if parentScope is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def interfaceDeclaration(self) -> str:
        return self.__interfaceDeclaration

    @interfaceDeclaration.setter
    def interfaceDeclaration(self, interfaceDeclaration: str):
        self.__interfaceDeclaration = interfaceDeclaration

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def synccharts_Scope40(self):
        return self.__synccharts_Scope40

    @synccharts_Scope40.setter
    def synccharts_Scope40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope40", None)
        self.__synccharts_Scope40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Action41"):
                    opp_val = getattr(item, "synccharts_Action41", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Action41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Action41"):
                    opp_val = getattr(item, "synccharts_Action41", None)
                    
                    setattr(item, "synccharts_Action41", self)
                    

    @property
    def parentScope(self):
        return self.__parentScope

    @parentScope.setter
    def parentScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__parentScope", None)
        self.__parentScope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    setattr(item, "Substitution", self)
                    

    @property
    def Scope(self):
        return self.__Scope

    @Scope.setter
    def Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__Scope", None)
        self.__Scope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "renamings"):
                opp_val = getattr(old_value, "renamings", None)
                if opp_val == self:
                    setattr(old_value, "renamings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "renamings"):
                opp_val = getattr(value, "renamings", None)
                setattr(value, "renamings", self)

    @property
    def synccharts_Scope48(self):
        return self.__synccharts_Scope48

    @synccharts_Scope48.setter
    def synccharts_Scope48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope48", None)
        self.__synccharts_Scope48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_TextualCode"):
                    opp_val = getattr(item, "synccharts_TextualCode", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_TextualCode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_TextualCode"):
                    opp_val = getattr(item, "synccharts_TextualCode", None)
                    
                    setattr(item, "synccharts_TextualCode", self)
                    

    @property
    def synccharts_Scope43(self):
        return self.__synccharts_Scope43

    @synccharts_Scope43.setter
    def synccharts_Scope43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope43", None)
        self.__synccharts_Scope43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_EObject"):
                opp_val = getattr(old_value, "synccharts_EObject", None)
                if opp_val == self:
                    setattr(old_value, "synccharts_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_EObject"):
                opp_val = getattr(value, "synccharts_EObject", None)
                setattr(value, "synccharts_EObject", self)

    @property
    def synccharts_Scope37(self):
        return self.__synccharts_Scope37

    @synccharts_Scope37.setter
    def synccharts_Scope37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope37", None)
        self.__synccharts_Scope37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Action38"):
                    opp_val = getattr(item, "synccharts_Action38", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Action38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Action38"):
                    opp_val = getattr(item, "synccharts_Action38", None)
                    
                    setattr(item, "synccharts_Action38", self)
                    

    @property
    def synccharts_Scope34(self):
        return self.__synccharts_Scope34

    @synccharts_Scope34.setter
    def synccharts_Scope34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope34", None)
        self.__synccharts_Scope34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Action35"):
                    opp_val = getattr(item, "synccharts_Action35", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Action35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Action35"):
                    opp_val = getattr(item, "synccharts_Action35", None)
                    
                    setattr(item, "synccharts_Action35", self)
                    

    @property
    def synccharts_Scope28(self):
        return self.__synccharts_Scope28

    @synccharts_Scope28.setter
    def synccharts_Scope28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope28", None)
        self.__synccharts_Scope28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Variable29"):
                    opp_val = getattr(item, "synccharts_Variable29", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Variable29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Variable29"):
                    opp_val = getattr(item, "synccharts_Variable29", None)
                    
                    setattr(item, "synccharts_Variable29", self)
                    

    @property
    def synccharts_Scope45(self):
        return self.__synccharts_Scope45

    @synccharts_Scope45.setter
    def synccharts_Scope45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope45", None)
        self.__synccharts_Scope45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_EObject46"):
                opp_val = getattr(old_value, "synccharts_EObject46", None)
                if opp_val == self:
                    setattr(old_value, "synccharts_EObject46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_EObject46"):
                opp_val = getattr(value, "synccharts_EObject46", None)
                setattr(value, "synccharts_EObject46", self)

    @property
    def synccharts_Scope31(self):
        return self.__synccharts_Scope31

    @synccharts_Scope31.setter
    def synccharts_Scope31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope31", None)
        self.__synccharts_Scope31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Action32"):
                opp_val = getattr(old_value, "synccharts_Action32", None)
                if opp_val == self:
                    setattr(old_value, "synccharts_Action32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Action32"):
                opp_val = getattr(value, "synccharts_Action32", None)
                setattr(value, "synccharts_Action32", self)

    @property
    def synccharts_Scope(self):
        return self.__synccharts_Scope

    @synccharts_Scope.setter
    def synccharts_Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Scope__synccharts_Scope", None)
        self.__synccharts_Scope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Signal26"):
                    opp_val = getattr(item, "synccharts_Signal26", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Signal26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Signal26"):
                    opp_val = getattr(item, "synccharts_Signal26", None)
                    
                    setattr(item, "synccharts_Signal26", self)
                    

class synccharts_Action(Annotatable):

    def __init__(self, delay: int, isImmediate: bool, label: str, synccharts_Action: set["synccharts_Effect"] = None, synccharts_Action2: "synccharts_Expression" = None, synccharts_Action32: "synccharts_Scope" = None, synccharts_Action35: "synccharts_Scope" = None, synccharts_Action38: "synccharts_Scope" = None, synccharts_Action41: "synccharts_Scope" = None):
        self.delay = delay
        self.isImmediate = isImmediate
        self.label = label
        self.synccharts_Action = synccharts_Action if synccharts_Action is not None else set()
        self.synccharts_Action2 = synccharts_Action2
        self.synccharts_Action32 = synccharts_Action32
        self.synccharts_Action35 = synccharts_Action35
        self.synccharts_Action38 = synccharts_Action38
        self.synccharts_Action41 = synccharts_Action41
        
    @property
    def delay(self) -> int:
        return self.__delay

    @delay.setter
    def delay(self, delay: int):
        self.__delay = delay

    @property
    def isImmediate(self) -> bool:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: bool):
        self.__isImmediate = isImmediate

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def synccharts_Action2(self):
        return self.__synccharts_Action2

    @synccharts_Action2.setter
    def synccharts_Action2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action2", None)
        self.__synccharts_Action2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Expression"):
                opp_val = getattr(old_value, "synccharts_Expression", None)
                if opp_val == self:
                    setattr(old_value, "synccharts_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Expression"):
                opp_val = getattr(value, "synccharts_Expression", None)
                setattr(value, "synccharts_Expression", self)

    @property
    def synccharts_Action35(self):
        return self.__synccharts_Action35

    @synccharts_Action35.setter
    def synccharts_Action35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action35", None)
        self.__synccharts_Action35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Scope34"):
                opp_val = getattr(old_value, "synccharts_Scope34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Scope34"):
                opp_val = getattr(value, "synccharts_Scope34", None)
                if opp_val is None:
                    setattr(value, "synccharts_Scope34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def synccharts_Action38(self):
        return self.__synccharts_Action38

    @synccharts_Action38.setter
    def synccharts_Action38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action38", None)
        self.__synccharts_Action38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Scope37"):
                opp_val = getattr(old_value, "synccharts_Scope37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Scope37"):
                opp_val = getattr(value, "synccharts_Scope37", None)
                if opp_val is None:
                    setattr(value, "synccharts_Scope37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def synccharts_Action41(self):
        return self.__synccharts_Action41

    @synccharts_Action41.setter
    def synccharts_Action41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action41", None)
        self.__synccharts_Action41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Scope40"):
                opp_val = getattr(old_value, "synccharts_Scope40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Scope40"):
                opp_val = getattr(value, "synccharts_Scope40", None)
                if opp_val is None:
                    setattr(value, "synccharts_Scope40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def synccharts_Action(self):
        return self.__synccharts_Action

    @synccharts_Action.setter
    def synccharts_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action", None)
        self.__synccharts_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "synccharts_Effect"):
                    opp_val = getattr(item, "synccharts_Effect", None)
                    
                    if opp_val == self:
                        setattr(item, "synccharts_Effect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "synccharts_Effect"):
                    opp_val = getattr(item, "synccharts_Effect", None)
                    
                    setattr(item, "synccharts_Effect", self)
                    

    @property
    def synccharts_Action32(self):
        return self.__synccharts_Action32

    @synccharts_Action32.setter
    def synccharts_Action32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_synccharts_Action__synccharts_Action32", None)
        self.__synccharts_Action32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synccharts_Scope31"):
                opp_val = getattr(old_value, "synccharts_Scope31", None)
                if opp_val == self:
                    setattr(old_value, "synccharts_Scope31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synccharts_Scope31"):
                opp_val = getattr(value, "synccharts_Scope31", None)
                setattr(value, "synccharts_Scope31", self)

class Effect:

    pass
class synccharts_Emission(Effect):

    pass
class synccharts_TextEffect(Effect, TextualCode):

    pass
class synccharts_Assignment(Effect):

    pass