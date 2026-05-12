from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TranslationKind(Enum):
    SINGLEVAR = "SINGLEVAR"
    REFINEDVAR = "REFINEDVAR"
    MULTIVAR = "MULTIVAR"


############################################
# Definition of Classes
############################################

class StatemachineOwner:

    pass
class EventBNamed:

    pass
class AbstractNode:

    pass
class statemachines_Initial(AbstractNode):

    pass
class statemachines_Fork(AbstractNode):

    def __init__(self):
        
        pass
    def isJoin(self) :
        # TODO: Implement isJoin method
        pass

    def isFork(self) :
        # TODO: Implement isFork method
        pass

class statemachines_Final(AbstractNode):

    pass
class statemachines_Any(AbstractNode):

    pass
class statemachines_Junction(AbstractNode):

    pass
class statemachines_State(EventBNamed, StatemachineOwner, AbstractNode):

    def __init__(self, active: bool, statemachines_State24: set["Invariant"] = None, statemachines_State: "statemachines_State" = None, statemachines_State21: "statemachines_State" = None):
        self.active = active
        self.statemachines_State24 = statemachines_State24 if statemachines_State24 is not None else set()
        self.statemachines_State = statemachines_State
        self.statemachines_State21 = statemachines_State21
        
        pass
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def statemachines_State(self):
        return self.__statemachines_State

    @statemachines_State.setter
    def statemachines_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State", None)
        self.__statemachines_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_State21"):
                opp_val = getattr(old_value, "statemachines_State21", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_State21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_State21"):
                opp_val = getattr(value, "statemachines_State21", None)
                setattr(value, "statemachines_State21", self)

    @property
    def statemachines_State24(self):
        return self.__statemachines_State24

    @statemachines_State24.setter
    def statemachines_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State24", None)
        self.__statemachines_State24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invariant"):
                    opp_val = getattr(item, "Invariant", None)
                    
                    if opp_val == self:
                        setattr(item, "Invariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invariant"):
                    opp_val = getattr(item, "Invariant", None)
                    
                    setattr(item, "Invariant", self)
                    

    @property
    def statemachines_State21(self):
        return self.__statemachines_State21

    @statemachines_State21.setter
    def statemachines_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_State__statemachines_State21", None)
        self.__statemachines_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_State"):
                opp_val = getattr(old_value, "statemachines_State", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_State"):
                opp_val = getattr(value, "statemachines_State", None)
                setattr(value, "statemachines_State", self)

class EventBElement:

    pass
class Invariant:

    pass
class statemachines_EventBElement:

    pass
class EventBCommentedLabeledEventGroupElement:

    pass
class statemachines_StatemachineOwner(ABC):

    pass
class statemachines_EventBNamedCommentedElement:

    pass
class statemachines_Transition(EventBCommentedLabeledEventGroupElement):

    def __init__(self, operations: str, statemachines_Transition: "statemachines_Statemachine" = None, statemachines_Transition16: "statemachines_EventBElement" = None, incoming: "statemachines_AbstractNode" = None, outgoing: "statemachines_AbstractNode" = None, statemachines_Transition14: "statemachines_EventBElement" = None, Transition: "statemachines_AbstractNode" = None, Transition20: "statemachines_AbstractNode" = None):
        self.operations = operations
        self.statemachines_Transition = statemachines_Transition
        self.statemachines_Transition16 = statemachines_Transition16
        self.incoming = incoming
        self.outgoing = outgoing
        self.statemachines_Transition14 = statemachines_Transition14
        self.Transition = Transition
        self.Transition20 = Transition20
        
        pass
    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, operations: str):
        self.__operations = operations


    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractNode"):
                opp_val = getattr(old_value, "AbstractNode", None)
                if opp_val == self:
                    setattr(old_value, "AbstractNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractNode"):
                opp_val = getattr(value, "AbstractNode", None)
                setattr(value, "AbstractNode", self)

    @property
    def Transition20(self):
        return self.__Transition20

    @Transition20.setter
    def Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition20", None)
        self.__Transition20 = value
        
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
    def statemachines_Transition16(self):
        return self.__statemachines_Transition16

    @statemachines_Transition16.setter
    def statemachines_Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition16", None)
        self.__statemachines_Transition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_EventBElement17"):
                opp_val = getattr(old_value, "statemachines_EventBElement17", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_EventBElement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_EventBElement17"):
                opp_val = getattr(value, "statemachines_EventBElement17", None)
                setattr(value, "statemachines_EventBElement17", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__Transition", None)
        self.__Transition = value
        
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
    def statemachines_Transition(self):
        return self.__statemachines_Transition

    @statemachines_Transition.setter
    def statemachines_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition", None)
        self.__statemachines_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Statemachine5"):
                opp_val = getattr(old_value, "statemachines_Statemachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Statemachine5"):
                opp_val = getattr(value, "statemachines_Statemachine5", None)
                if opp_val is None:
                    setattr(value, "statemachines_Statemachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Transition14(self):
        return self.__statemachines_Transition14

    @statemachines_Transition14.setter
    def statemachines_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__statemachines_Transition14", None)
        self.__statemachines_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_EventBElement"):
                opp_val = getattr(old_value, "statemachines_EventBElement", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_EventBElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_EventBElement"):
                opp_val = getattr(value, "statemachines_EventBElement", None)
                setattr(value, "statemachines_EventBElement", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractNode12"):
                opp_val = getattr(old_value, "AbstractNode12", None)
                if opp_val == self:
                    setattr(old_value, "AbstractNode12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractNode12"):
                opp_val = getattr(value, "AbstractNode12", None)
                setattr(value, "AbstractNode12", self)

class statemachines_AbstractNode(EventBElement):

    pass
class Diagram:

    pass
class AbstractExtension:

    pass
class EventBNamedCommentedDataElaborationElement:

    pass
class statemachines_Statemachine(EventBNamedCommentedDataElaborationElement, AbstractExtension, Diagram):

    def __init__(self, selfName: str, translation: str, statemachines_Statemachine: "statemachines_Statemachine" = None, statemachines_Statemachine0: "statemachines_Statemachine" = None, statemachines_Statemachine7: "statemachines_EventBNamedCommentedElement" = None, statemachines_Statemachine3: set["statemachines_AbstractNode"] = None, statemachines_Statemachine5: set["statemachines_Transition"] = None, statemachines_Statemachine9: "statemachines_StatemachineOwner" = None):
        self.selfName = selfName
        self.translation = translation
        self.statemachines_Statemachine = statemachines_Statemachine
        self.statemachines_Statemachine0 = statemachines_Statemachine0
        self.statemachines_Statemachine7 = statemachines_Statemachine7
        self.statemachines_Statemachine3 = statemachines_Statemachine3 if statemachines_Statemachine3 is not None else set()
        self.statemachines_Statemachine5 = statemachines_Statemachine5 if statemachines_Statemachine5 is not None else set()
        self.statemachines_Statemachine9 = statemachines_Statemachine9
        
        pass
    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, translation: str):
        self.__translation = translation


    @property
    def selfName(self):
        return self.__selfName

    @selfName.setter
    def selfName(self, selfName: str):
        self.__selfName = selfName


    @property
    def statemachines_Statemachine7(self):
        return self.__statemachines_Statemachine7

    @statemachines_Statemachine7.setter
    def statemachines_Statemachine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine7", None)
        self.__statemachines_Statemachine7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_EventBNamedCommentedElement"):
                opp_val = getattr(old_value, "statemachines_EventBNamedCommentedElement", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_EventBNamedCommentedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_EventBNamedCommentedElement"):
                opp_val = getattr(value, "statemachines_EventBNamedCommentedElement", None)
                setattr(value, "statemachines_EventBNamedCommentedElement", self)

    @property
    def statemachines_Statemachine(self):
        return self.__statemachines_Statemachine

    @statemachines_Statemachine.setter
    def statemachines_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine", None)
        self.__statemachines_Statemachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Statemachine0"):
                opp_val = getattr(old_value, "statemachines_Statemachine0", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Statemachine0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Statemachine0"):
                opp_val = getattr(value, "statemachines_Statemachine0", None)
                setattr(value, "statemachines_Statemachine0", self)

    @property
    def statemachines_Statemachine0(self):
        return self.__statemachines_Statemachine0

    @statemachines_Statemachine0.setter
    def statemachines_Statemachine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine0", None)
        self.__statemachines_Statemachine0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_Statemachine"):
                opp_val = getattr(old_value, "statemachines_Statemachine", None)
                if opp_val == self:
                    setattr(old_value, "statemachines_Statemachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_Statemachine"):
                opp_val = getattr(value, "statemachines_Statemachine", None)
                setattr(value, "statemachines_Statemachine", self)

    @property
    def statemachines_Statemachine5(self):
        return self.__statemachines_Statemachine5

    @statemachines_Statemachine5.setter
    def statemachines_Statemachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine5", None)
        self.__statemachines_Statemachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_Transition"):
                    opp_val = getattr(item, "statemachines_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_Transition"):
                    opp_val = getattr(item, "statemachines_Transition", None)
                    
                    setattr(item, "statemachines_Transition", self)
                    

    @property
    def statemachines_Statemachine9(self):
        return self.__statemachines_Statemachine9

    @statemachines_Statemachine9.setter
    def statemachines_Statemachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine9", None)
        self.__statemachines_Statemachine9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachines_StatemachineOwner"):
                opp_val = getattr(old_value, "statemachines_StatemachineOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachines_StatemachineOwner"):
                opp_val = getattr(value, "statemachines_StatemachineOwner", None)
                if opp_val is None:
                    setattr(value, "statemachines_StatemachineOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachines_Statemachine3(self):
        return self.__statemachines_Statemachine3

    @statemachines_Statemachine3.setter
    def statemachines_Statemachine3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_Statemachine__statemachines_Statemachine3", None)
        self.__statemachines_Statemachine3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_AbstractNode"):
                    opp_val = getattr(item, "statemachines_AbstractNode", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_AbstractNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_AbstractNode"):
                    opp_val = getattr(item, "statemachines_AbstractNode", None)
                    
                    setattr(item, "statemachines_AbstractNode", self)
                    
