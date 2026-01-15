from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    Integer = "Integer"
    Real = "Real"
    Float = "Float"
    Double = "Double"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class sam_Model:

    pass
class EModelElement:

    pass
class sam_IdentifiedItem(EModelElement):

    def __init__(self, comment: str, requirements: str):
        self.comment = comment
        self.requirements = requirements
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def requirements(self) -> str:
        return self.__requirements

    @requirements.setter
    def requirements(self, requirements: str):
        self.__requirements = requirements

class Flow:

    pass
class sam_DataFlow(Flow):

    def __init__(self, type: str, sam_DataFlow: "sam_DataPort" = None, sam_DataFlow47: set["sam_DataPort"] = None):
        self.type = type
        self.sam_DataFlow = sam_DataFlow
        self.sam_DataFlow47 = sam_DataFlow47 if sam_DataFlow47 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sam_DataFlow47(self):
        return self.__sam_DataFlow47

    @sam_DataFlow47.setter
    def sam_DataFlow47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_DataFlow__sam_DataFlow47", None)
        self.__sam_DataFlow47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sam_DataPort48"):
                    opp_val = getattr(item, "sam_DataPort48", None)
                    
                    if opp_val == self:
                        setattr(item, "sam_DataPort48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sam_DataPort48"):
                    opp_val = getattr(item, "sam_DataPort48", None)
                    
                    setattr(item, "sam_DataPort48", self)
                    

    @property
    def sam_DataFlow(self):
        return self.__sam_DataFlow

    @sam_DataFlow.setter
    def sam_DataFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_DataFlow__sam_DataFlow", None)
        self.__sam_DataFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_DataPort"):
                opp_val = getattr(old_value, "sam_DataPort", None)
                if opp_val == self:
                    setattr(old_value, "sam_DataPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_DataPort"):
                opp_val = getattr(value, "sam_DataPort", None)
                setattr(value, "sam_DataPort", self)

class sam_ControlFlow(Flow):

    pass
class SynchronisationGate:

    pass
class sam_Decomposition(SynchronisationGate):

    pass
class sam_Composition(SynchronisationGate):

    pass
class DataPort:

    pass
class InputPort:

    pass
class sam_InDataPort(DataPort, InputPort):

    pass
class ControlPort:

    pass
class sam_InControlPort(ControlPort, InputPort):

    pass
class OutputPort:

    pass
class sam_OutDataPort(OutputPort, DataPort):

    pass
class sam_OutControlPort(OutputPort, ControlPort):

    pass
class IdentifiedItem:

    pass
class sam_NamedItem(IdentifiedItem):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class sam_SynchronisationGate(IdentifiedItem):

    pass
class AbstractState:

    pass
class sam_State(AbstractState):

    pass
class Port:

    pass
class sam_OutputPort(Port):

    pass
class sam_InputPort(Port):

    pass
class sam_DataPort(Port):

    pass
class sam_ControlPort(Port):

    pass
class ModelContent:

    pass
class sam_System(ModelContent):

    pass
class sam_Transition(IdentifiedItem):

    def __init__(self, condition: str, emission: str, priority: str, Transition: "sam_AbstractState" = None, Transition4: "sam_Automaton" = None, inlink: "sam_State" = None, listTransitions: "sam_Automaton" = None, outlink: "sam_AbstractState" = None, Transition14: "sam_State" = None):
        self.condition = condition
        self.emission = emission
        self.priority = priority
        self.Transition = Transition
        self.Transition4 = Transition4
        self.inlink = inlink
        self.listTransitions = listTransitions
        self.outlink = outlink
        self.Transition14 = Transition14
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def emission(self) -> str:
        return self.__emission

    @emission.setter
    def emission(self, emission: str):
        self.__emission = emission

    @property
    def inlink(self):
        return self.__inlink

    @inlink.setter
    def inlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__inlink", None)
        self.__inlink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__Transition", None)
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
    def listTransitions(self):
        return self.__listTransitions

    @listTransitions.setter
    def listTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__listTransitions", None)
        self.__listTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Automaton17"):
                opp_val = getattr(old_value, "Automaton17", None)
                if opp_val == self:
                    setattr(old_value, "Automaton17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Automaton17"):
                opp_val = getattr(value, "Automaton17", None)
                setattr(value, "Automaton17", self)

    @property
    def outlink(self):
        return self.__outlink

    @outlink.setter
    def outlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__outlink", None)
        self.__outlink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState19"):
                opp_val = getattr(old_value, "AbstractState19", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState19"):
                opp_val = getattr(value, "AbstractState19", None)
                setattr(value, "AbstractState19", self)

    @property
    def Transition14(self):
        return self.__Transition14

    @Transition14.setter
    def Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__Transition14", None)
        self.__Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dest"):
                opp_val = getattr(old_value, "dest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dest"):
                opp_val = getattr(value, "dest", None)
                if opp_val is None:
                    setattr(value, "dest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition4(self):
        return self.__Transition4

    @Transition4.setter
    def Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Transition__Transition4", None)
        self.__Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAutomaton"):
                opp_val = getattr(old_value, "parentAutomaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAutomaton"):
                opp_val = getattr(value, "parentAutomaton", None)
                if opp_val is None:
                    setattr(value, "parentAutomaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sam_Automaton(ModelContent):

    pass
class sam_MacroState(AbstractState):

    pass
class State:

    pass
class sam_InitialState(State):

    pass
class NamedItem:

    pass
class sam_MultiPort(NamedItem):

    pass
class sam_ModelContent(NamedItem):

    pass
class sam_DataStore(NamedItem):

    pass
class sam_Flow(NamedItem):

    pass
class sam_AbstractState(NamedItem):

    pass
class sam_Port(NamedItem):

    pass