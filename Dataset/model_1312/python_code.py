from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateKind(Enum):
    initial = "initial"
    deep = "deep"
    join = "join"
    fork = "fork"
    choice = "choice"
    terminate = "terminate"
    shallow = "shallow"
    none = "none"
class TransitionKind(Enum):
    external = "external"
    internal = "internal"
    local = "local"


############################################
# Definition of Classes
############################################

class state_Constraint:

    pass
class state_StateModel:

    pass
class state_Event:

    def __init__(self, body: str, state_Event: "state_Trigger" = None):
        self.body = body
        self.state_Event = state_Event
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def state_Event(self):
        return self.__state_Event

    @state_Event.setter
    def state_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Event__state_Event", None)
        self.__state_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Trigger40"):
                opp_val = getattr(old_value, "state_Trigger40", None)
                if opp_val == self:
                    setattr(old_value, "state_Trigger40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Trigger40"):
                opp_val = getattr(value, "state_Trigger40", None)
                setattr(value, "state_Trigger40", self)

class state_OpaqueExpression:

    def __init__(self, body: str, state_OpaqueExpression: "state_Constraint" = None):
        self.body = body
        self.state_OpaqueExpression = state_OpaqueExpression
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def state_OpaqueExpression(self):
        return self.__state_OpaqueExpression

    @state_OpaqueExpression.setter
    def state_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_OpaqueExpression__state_OpaqueExpression", None)
        self.__state_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Constraint38"):
                opp_val = getattr(old_value, "state_Constraint38", None)
                if opp_val == self:
                    setattr(old_value, "state_Constraint38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Constraint38"):
                opp_val = getattr(value, "state_Constraint38", None)
                setattr(value, "state_Constraint38", self)

class State:

    pass
class state_FinalState(State):

    pass
class state_Behaviour:

    def __init__(self, body: str, language: str, state_Behaviour: "state_State" = None, state_Behaviour7: "state_State" = None, state_Behaviour10: "state_State" = None, state_Behaviour36: "state_Transition" = None):
        self.body = body
        self.language = language
        self.state_Behaviour = state_Behaviour
        self.state_Behaviour7 = state_Behaviour7
        self.state_Behaviour10 = state_Behaviour10
        self.state_Behaviour36 = state_Behaviour36
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def state_Behaviour36(self):
        return self.__state_Behaviour36

    @state_Behaviour36.setter
    def state_Behaviour36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Behaviour__state_Behaviour36", None)
        self.__state_Behaviour36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Transition35"):
                opp_val = getattr(old_value, "state_Transition35", None)
                if opp_val == self:
                    setattr(old_value, "state_Transition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Transition35"):
                opp_val = getattr(value, "state_Transition35", None)
                setattr(value, "state_Transition35", self)

    @property
    def state_Behaviour7(self):
        return self.__state_Behaviour7

    @state_Behaviour7.setter
    def state_Behaviour7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Behaviour__state_Behaviour7", None)
        self.__state_Behaviour7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_State6"):
                opp_val = getattr(old_value, "state_State6", None)
                if opp_val == self:
                    setattr(old_value, "state_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_State6"):
                opp_val = getattr(value, "state_State6", None)
                setattr(value, "state_State6", self)

    @property
    def state_Behaviour(self):
        return self.__state_Behaviour

    @state_Behaviour.setter
    def state_Behaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Behaviour__state_Behaviour", None)
        self.__state_Behaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_State4"):
                opp_val = getattr(old_value, "state_State4", None)
                if opp_val == self:
                    setattr(old_value, "state_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_State4"):
                opp_val = getattr(value, "state_State4", None)
                setattr(value, "state_State4", self)

    @property
    def state_Behaviour10(self):
        return self.__state_Behaviour10

    @state_Behaviour10.setter
    def state_Behaviour10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Behaviour__state_Behaviour10", None)
        self.__state_Behaviour10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_State9"):
                opp_val = getattr(old_value, "state_State9", None)
                if opp_val == self:
                    setattr(old_value, "state_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_State9"):
                opp_val = getattr(value, "state_State9", None)
                setattr(value, "state_State9", self)

class state_NamedElement(ABC):

    def __init__(self, name: str, id: str, state_NamedElement: "state_StateModel" = None):
        self.name = name
        self.id = id
        self.state_NamedElement = state_NamedElement
        
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

    @property
    def state_NamedElement(self):
        return self.__state_NamedElement

    @state_NamedElement.setter
    def state_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_NamedElement__state_NamedElement", None)
        self.__state_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_StateModel"):
                opp_val = getattr(old_value, "state_StateModel", None)
                if opp_val == self:
                    setattr(old_value, "state_StateModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_StateModel"):
                opp_val = getattr(value, "state_StateModel", None)
                setattr(value, "state_StateModel", self)

class NamedElement:

    pass
class state_Transition(NamedElement):

    def __init__(self, kind: str, state_Transition: "state_Region" = None, Transition: "state_Vertex" = None, Transition25: "state_Vertex" = None, outgoing: "state_Vertex" = None, incoming: "state_Vertex" = None, state_Transition30: "state_Trigger" = None, state_Transition33: "state_Constraint" = None, state_Transition35: "state_Behaviour" = None):
        self.kind = kind
        self.state_Transition = state_Transition
        self.Transition = Transition
        self.Transition25 = Transition25
        self.outgoing = outgoing
        self.incoming = incoming
        self.state_Transition30 = state_Transition30
        self.state_Transition33 = state_Transition33
        self.state_Transition35 = state_Transition35
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex28"):
                opp_val = getattr(old_value, "Vertex28", None)
                if opp_val == self:
                    setattr(old_value, "Vertex28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex28"):
                opp_val = getattr(value, "Vertex28", None)
                setattr(value, "Vertex28", self)

    @property
    def state_Transition33(self):
        return self.__state_Transition33

    @state_Transition33.setter
    def state_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition33", None)
        self.__state_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Constraint"):
                opp_val = getattr(old_value, "state_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "state_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Constraint"):
                opp_val = getattr(value, "state_Constraint", None)
                setattr(value, "state_Constraint", self)

    @property
    def state_Transition35(self):
        return self.__state_Transition35

    @state_Transition35.setter
    def state_Transition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition35", None)
        self.__state_Transition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Behaviour36"):
                opp_val = getattr(old_value, "state_Behaviour36", None)
                if opp_val == self:
                    setattr(old_value, "state_Behaviour36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Behaviour36"):
                opp_val = getattr(value, "state_Behaviour36", None)
                setattr(value, "state_Behaviour36", self)

    @property
    def state_Transition(self):
        return self.__state_Transition

    @state_Transition.setter
    def state_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition", None)
        self.__state_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Region19"):
                opp_val = getattr(old_value, "state_Region19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Region19"):
                opp_val = getattr(value, "state_Region19", None)
                if opp_val is None:
                    setattr(value, "state_Region19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex"):
                opp_val = getattr(old_value, "Vertex", None)
                if opp_val == self:
                    setattr(old_value, "Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex"):
                opp_val = getattr(value, "Vertex", None)
                setattr(value, "Vertex", self)

    @property
    def Transition25(self):
        return self.__Transition25

    @Transition25.setter
    def Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__Transition25", None)
        self.__Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def state_Transition30(self):
        return self.__state_Transition30

    @state_Transition30.setter
    def state_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition30", None)
        self.__state_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Trigger31"):
                opp_val = getattr(old_value, "state_Trigger31", None)
                if opp_val == self:
                    setattr(old_value, "state_Trigger31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Trigger31"):
                opp_val = getattr(value, "state_Trigger31", None)
                setattr(value, "state_Trigger31", self)

class state_StateMachine(NamedElement):

    pass
class state_Vertex(NamedElement):

    pass
class state_Region(NamedElement):

    pass
class state_Trigger(NamedElement):

    pass
class Vertex:

    pass
class state_PseudoState(Vertex):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class state_State(NamedElement, Vertex):

    def __init__(self, isSimple: bool, isComposite: bool, state_State: set["state_Region"] = None, state_State2: set["state_Trigger"] = None, state_State13: "state_Region" = None, state_State4: "state_Behaviour" = None, state_State6: "state_Behaviour" = None, state_State9: "state_Behaviour" = None):
        self.isSimple = isSimple
        self.isComposite = isComposite
        self.state_State = state_State if state_State is not None else set()
        self.state_State2 = state_State2 if state_State2 is not None else set()
        self.state_State13 = state_State13
        self.state_State4 = state_State4
        self.state_State6 = state_State6
        self.state_State9 = state_State9
        
    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def state_State6(self):
        return self.__state_State6

    @state_State6.setter
    def state_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State6", None)
        self.__state_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Behaviour7"):
                opp_val = getattr(old_value, "state_Behaviour7", None)
                if opp_val == self:
                    setattr(old_value, "state_Behaviour7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Behaviour7"):
                opp_val = getattr(value, "state_Behaviour7", None)
                setattr(value, "state_Behaviour7", self)

    @property
    def state_State(self):
        return self.__state_State

    @state_State.setter
    def state_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State", None)
        self.__state_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "state_Region"):
                    opp_val = getattr(item, "state_Region", None)
                    
                    if opp_val == self:
                        setattr(item, "state_Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "state_Region"):
                    opp_val = getattr(item, "state_Region", None)
                    
                    setattr(item, "state_Region", self)
                    

    @property
    def state_State4(self):
        return self.__state_State4

    @state_State4.setter
    def state_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State4", None)
        self.__state_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Behaviour"):
                opp_val = getattr(old_value, "state_Behaviour", None)
                if opp_val == self:
                    setattr(old_value, "state_Behaviour", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Behaviour"):
                opp_val = getattr(value, "state_Behaviour", None)
                setattr(value, "state_Behaviour", self)

    @property
    def state_State13(self):
        return self.__state_State13

    @state_State13.setter
    def state_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State13", None)
        self.__state_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Region12"):
                opp_val = getattr(old_value, "state_Region12", None)
                if opp_val == self:
                    setattr(old_value, "state_Region12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Region12"):
                opp_val = getattr(value, "state_Region12", None)
                setattr(value, "state_Region12", self)

    @property
    def state_State2(self):
        return self.__state_State2

    @state_State2.setter
    def state_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State2", None)
        self.__state_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "state_Trigger"):
                    opp_val = getattr(item, "state_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "state_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "state_Trigger"):
                    opp_val = getattr(item, "state_Trigger", None)
                    
                    setattr(item, "state_Trigger", self)
                    

    @property
    def state_State9(self):
        return self.__state_State9

    @state_State9.setter
    def state_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_State__state_State9", None)
        self.__state_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Behaviour10"):
                opp_val = getattr(old_value, "state_Behaviour10", None)
                if opp_val == self:
                    setattr(old_value, "state_Behaviour10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Behaviour10"):
                opp_val = getattr(value, "state_Behaviour10", None)
                setattr(value, "state_Behaviour10", self)
