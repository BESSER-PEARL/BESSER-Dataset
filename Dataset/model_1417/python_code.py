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

class SplitGate:

    pass
class AsynchronousGate:

    pass
class sam_MergeGate(AsynchronousGate):

    pass
class sam_SplitGate(AsynchronousGate):

    pass
class MergeGate:

    pass
class SynchronousGate:

    pass
class Gate:

    pass
class sam_SynchronousGate(Gate):

    pass
class sam_AsynchronousGate(Gate):

    pass
class sam_MessageMerge(MergeGate):

    pass
class MessagePort:

    pass
class ENamedElement:

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

class sam_Gate(IdentifiedItem):

    pass
class sam_EObject:

    pass
class sam_Model:

    pass
class sam_FlowGroup(ENamedElement):

    def __init__(self, globalComment: str, FlowGroup: "sam_Flow" = None, FlowGroup86: "sam_Model" = None, group: set["sam_Flow"] = None, flowGroups: "sam_Model" = None):
        self.globalComment = globalComment
        self.FlowGroup = FlowGroup
        self.FlowGroup86 = FlowGroup86
        self.group = group if group is not None else set()
        self.flowGroups = flowGroups
        
    @property
    def globalComment(self) -> str:
        return self.__globalComment

    @globalComment.setter
    def globalComment(self, globalComment: str):
        self.__globalComment = globalComment

    @property
    def flowGroups(self):
        return self.__flowGroups

    @flowGroups.setter
    def flowGroups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_FlowGroup__flowGroups", None)
        self.__flowGroups = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model115"):
                opp_val = getattr(old_value, "Model115", None)
                if opp_val == self:
                    setattr(old_value, "Model115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model115"):
                opp_val = getattr(value, "Model115", None)
                setattr(value, "Model115", self)

    @property
    def FlowGroup86(self):
        return self.__FlowGroup86

    @FlowGroup86.setter
    def FlowGroup86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_FlowGroup__FlowGroup86", None)
        self.__FlowGroup86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_FlowGroup__group", None)
        self.__group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flow113"):
                    opp_val = getattr(item, "Flow113", None)
                    
                    if opp_val == self:
                        setattr(item, "Flow113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flow113"):
                    opp_val = getattr(item, "Flow113", None)
                    
                    setattr(item, "Flow113", self)
                    

    @property
    def FlowGroup(self):
        return self.__FlowGroup

    @FlowGroup.setter
    def FlowGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_FlowGroup__FlowGroup", None)
        self.__FlowGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flows"):
                opp_val = getattr(old_value, "flows", None)
                if opp_val == self:
                    setattr(old_value, "flows", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flows"):
                opp_val = getattr(value, "flows", None)
                setattr(value, "flows", self)

class Flow:

    pass
class sam_DataFlow(Flow):

    def __init__(self, type: str, sam_DataFlow: "sam_DataPort" = None, sam_DataFlow60: set["sam_DataPort"] = None):
        self.type = type
        self.sam_DataFlow = sam_DataFlow
        self.sam_DataFlow60 = sam_DataFlow60 if sam_DataFlow60 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sam_DataFlow60(self):
        return self.__sam_DataFlow60

    @sam_DataFlow60.setter
    def sam_DataFlow60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_DataFlow__sam_DataFlow60", None)
        self.__sam_DataFlow60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sam_DataPort61"):
                    opp_val = getattr(item, "sam_DataPort61", None)
                    
                    if opp_val == self:
                        setattr(item, "sam_DataPort61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sam_DataPort61"):
                    opp_val = getattr(item, "sam_DataPort61", None)
                    
                    setattr(item, "sam_DataPort61", self)
                    

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

class sam_MessageFlow(Flow):

    pass
class sam_ControlFlow(Flow):

    pass
class DataSynchronisation:

    pass
class sam_DataDecomposition(DataSynchronisation):

    pass
class sam_DataComposition(DataSynchronisation):

    pass
class sam_DataMerge(MergeGate):

    pass
class sam_DataSynchronisation(SynchronousGate):

    pass
class DataPort:

    pass
class sam_MessageSplit(SplitGate):

    pass
class OutputPort:

    pass
class sam_OutMessagePort(OutputPort, MessagePort):

    pass
class sam_OutDataPort(OutputPort, DataPort):

    pass
class sam_ControlMerge(MergeGate):

    pass
class InputPort:

    pass
class sam_InDataPort(InputPort, DataPort):

    pass
class sam_InMessagePort(MessagePort, InputPort):

    pass
class ControlPort:

    pass
class sam_OutControlPort(OutputPort, ControlPort):

    pass
class sam_InControlPort(ControlPort, InputPort):

    pass
class Port:

    pass
class sam_MessagePort(Port):

    pass
class sam_InputPort(Port):

    pass
class sam_OutputPort(Port):

    pass
class sam_DataPort(Port):

    pass
class sam_ControlPort(Port):

    pass
class AbstractState:

    pass
class State:

    pass
class sam_InitialState(State):

    pass
class TraceableElement:

    pass
class sam_State(AbstractState):

    pass
class ModelContent:

    pass
class sam_System(TraceableElement, ModelContent):

    pass
class sam_MacroState(AbstractState):

    pass
class NamedItem:

    pass
class sam_ModelContent(NamedItem):

    pass
class sam_MultiPort(NamedItem):

    pass
class sam_Port(NamedItem):

    def __init__(self, Port: "sam_Automaton" = None, listPorts: "sam_System" = None, sam_Port: "sam_Flow" = None, sam_Port44: "sam_Flow" = None, listPorts47: "sam_Automaton" = None, sam_Port50: "sam_MultiPort" = None, sam_Port53: "sam_Port" = None, sam_Port51: "sam_Port" = None, Port71: "sam_System" = None, sam_Port94: "sam_MultiPort" = None):
        self.Port = Port
        self.listPorts = listPorts
        self.sam_Port = sam_Port
        self.sam_Port44 = sam_Port44
        self.listPorts47 = listPorts47
        self.sam_Port50 = sam_Port50
        self.sam_Port53 = sam_Port53
        self.sam_Port51 = sam_Port51
        self.Port71 = Port71
        self.sam_Port94 = sam_Port94
        
    @property
    def sam_Port50(self):
        return self.__sam_Port50

    @sam_Port50.setter
    def sam_Port50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port50", None)
        self.__sam_Port50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_MultiPort"):
                opp_val = getattr(old_value, "sam_MultiPort", None)
                if opp_val == self:
                    setattr(old_value, "sam_MultiPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_MultiPort"):
                opp_val = getattr(value, "sam_MultiPort", None)
                setattr(value, "sam_MultiPort", self)

    @property
    def listPorts(self):
        return self.__listPorts

    @listPorts.setter
    def listPorts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__listPorts", None)
        self.__listPorts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__Port", None)
        self.__Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAutomaton6"):
                opp_val = getattr(old_value, "parentAutomaton6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAutomaton6"):
                opp_val = getattr(value, "parentAutomaton6", None)
                if opp_val is None:
                    setattr(value, "parentAutomaton6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sam_Port(self):
        return self.__sam_Port

    @sam_Port.setter
    def sam_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port", None)
        self.__sam_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_Flow"):
                opp_val = getattr(old_value, "sam_Flow", None)
                if opp_val == self:
                    setattr(old_value, "sam_Flow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_Flow"):
                opp_val = getattr(value, "sam_Flow", None)
                setattr(value, "sam_Flow", self)

    @property
    def sam_Port53(self):
        return self.__sam_Port53

    @sam_Port53.setter
    def sam_Port53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port53", None)
        self.__sam_Port53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_Port51"):
                opp_val = getattr(old_value, "sam_Port51", None)
                if opp_val == self:
                    setattr(old_value, "sam_Port51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_Port51"):
                opp_val = getattr(value, "sam_Port51", None)
                setattr(value, "sam_Port51", self)

    @property
    def Port71(self):
        return self.__Port71

    @Port71.setter
    def Port71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__Port71", None)
        self.__Port71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentSystem"):
                opp_val = getattr(old_value, "parentSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentSystem"):
                opp_val = getattr(value, "parentSystem", None)
                if opp_val is None:
                    setattr(value, "parentSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def listPorts47(self):
        return self.__listPorts47

    @listPorts47.setter
    def listPorts47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__listPorts47", None)
        self.__listPorts47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Automaton48"):
                opp_val = getattr(old_value, "Automaton48", None)
                if opp_val == self:
                    setattr(old_value, "Automaton48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Automaton48"):
                opp_val = getattr(value, "Automaton48", None)
                setattr(value, "Automaton48", self)

    @property
    def sam_Port44(self):
        return self.__sam_Port44

    @sam_Port44.setter
    def sam_Port44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port44", None)
        self.__sam_Port44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_Flow45"):
                opp_val = getattr(old_value, "sam_Flow45", None)
                if opp_val == self:
                    setattr(old_value, "sam_Flow45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_Flow45"):
                opp_val = getattr(value, "sam_Flow45", None)
                setattr(value, "sam_Flow45", self)

    @property
    def sam_Port94(self):
        return self.__sam_Port94

    @sam_Port94.setter
    def sam_Port94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port94", None)
        self.__sam_Port94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_MultiPort93"):
                opp_val = getattr(old_value, "sam_MultiPort93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_MultiPort93"):
                opp_val = getattr(value, "sam_MultiPort93", None)
                if opp_val is None:
                    setattr(value, "sam_MultiPort93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sam_Port51(self):
        return self.__sam_Port51

    @sam_Port51.setter
    def sam_Port51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sam_Port__sam_Port51", None)
        self.__sam_Port51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sam_Port53"):
                opp_val = getattr(old_value, "sam_Port53", None)
                if opp_val == self:
                    setattr(old_value, "sam_Port53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sam_Port53"):
                opp_val = getattr(value, "sam_Port53", None)
                setattr(value, "sam_Port53", self)

    def isIn(self) -> bool:
        # TODO: Implement isIn method
        pass

    def isOut(self) -> bool:
        # TODO: Implement isOut method
        pass

class sam_TraceableElement(NamedItem):

    pass
class sam_Flow(NamedItem):

    pass
class sam_DataStore(NamedItem):

    pass
class sam_AbstractState(NamedItem):

    pass
class sam_Transition(TraceableElement):

    def __init__(self, condition: str, emission: str, priority: str, Transition: "sam_AbstractState" = None, Transition4: "sam_Automaton" = None, Transition14: "sam_State" = None, inlink: "sam_State" = None, listTransitions: "sam_Automaton" = None, outlink: "sam_AbstractState" = None):
        self.condition = condition
        self.emission = emission
        self.priority = priority
        self.Transition = Transition
        self.Transition4 = Transition4
        self.Transition14 = Transition14
        self.inlink = inlink
        self.listTransitions = listTransitions
        self.outlink = outlink
        
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
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

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

class sam_Automaton(ModelContent):

    pass