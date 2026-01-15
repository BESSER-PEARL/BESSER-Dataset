from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ActionState:

    pass
class behavioral_elements_activity_graphs_CallState(ActionState):

    pass
class SimpleState:

    pass
class behavioral_elements_activity_graphs_ObjectFlowState(SimpleState):

    def __init__(self, isSynch: str, behavioral_elements_activity_graphs_ObjectFlowState: set["Parameter"] = None, behavioral_elements_activity_graphs_ObjectFlowState325: "Classifier" = None):
        self.isSynch = isSynch
        self.behavioral_elements_activity_graphs_ObjectFlowState = behavioral_elements_activity_graphs_ObjectFlowState if behavioral_elements_activity_graphs_ObjectFlowState is not None else set()
        self.behavioral_elements_activity_graphs_ObjectFlowState325 = behavioral_elements_activity_graphs_ObjectFlowState325
        
    @property
    def isSynch(self) -> str:
        return self.__isSynch

    @isSynch.setter
    def isSynch(self, isSynch: str):
        self.__isSynch = isSynch

    @property
    def behavioral_elements_activity_graphs_ObjectFlowState(self):
        return self.__behavioral_elements_activity_graphs_ObjectFlowState

    @behavioral_elements_activity_graphs_ObjectFlowState.setter
    def behavioral_elements_activity_graphs_ObjectFlowState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ObjectFlowState__behavioral_elements_activity_graphs_ObjectFlowState", None)
        self.__behavioral_elements_activity_graphs_ObjectFlowState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter323"):
                    opp_val = getattr(item, "Parameter323", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter323"):
                    opp_val = getattr(item, "Parameter323", None)
                    
                    setattr(item, "Parameter323", self)
                    

    @property
    def behavioral_elements_activity_graphs_ObjectFlowState325(self):
        return self.__behavioral_elements_activity_graphs_ObjectFlowState325

    @behavioral_elements_activity_graphs_ObjectFlowState325.setter
    def behavioral_elements_activity_graphs_ObjectFlowState325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ObjectFlowState__behavioral_elements_activity_graphs_ObjectFlowState325", None)
        self.__behavioral_elements_activity_graphs_ObjectFlowState325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier326"):
                opp_val = getattr(old_value, "Classifier326", None)
                if opp_val == self:
                    setattr(old_value, "Classifier326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier326"):
                opp_val = getattr(value, "Classifier326", None)
                setattr(value, "Classifier326", self)

class behavioral_elements_activity_graphs_ActionState(SimpleState):

    def __init__(self, isDynamic: str, behavioral_elements_activity_graphs_ActionState: "ArgListsExpression" = None, behavioral_elements_activity_graphs_ActionState320: "Multiplicity" = None):
        self.isDynamic = isDynamic
        self.behavioral_elements_activity_graphs_ActionState = behavioral_elements_activity_graphs_ActionState
        self.behavioral_elements_activity_graphs_ActionState320 = behavioral_elements_activity_graphs_ActionState320
        
    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def behavioral_elements_activity_graphs_ActionState320(self):
        return self.__behavioral_elements_activity_graphs_ActionState320

    @behavioral_elements_activity_graphs_ActionState320.setter
    def behavioral_elements_activity_graphs_ActionState320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ActionState__behavioral_elements_activity_graphs_ActionState320", None)
        self.__behavioral_elements_activity_graphs_ActionState320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity321"):
                opp_val = getattr(old_value, "Multiplicity321", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity321"):
                opp_val = getattr(value, "Multiplicity321", None)
                setattr(value, "Multiplicity321", self)

    @property
    def behavioral_elements_activity_graphs_ActionState(self):
        return self.__behavioral_elements_activity_graphs_ActionState

    @behavioral_elements_activity_graphs_ActionState.setter
    def behavioral_elements_activity_graphs_ActionState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ActionState__behavioral_elements_activity_graphs_ActionState", None)
        self.__behavioral_elements_activity_graphs_ActionState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArgListsExpression318"):
                opp_val = getattr(old_value, "ArgListsExpression318", None)
                if opp_val == self:
                    setattr(old_value, "ArgListsExpression318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArgListsExpression318"):
                opp_val = getattr(value, "ArgListsExpression318", None)
                setattr(value, "ArgListsExpression318", self)

class ArgListsExpression:

    pass
class ActivityGraph:

    pass
class Partition:

    pass
class AssociationRole:

    pass
class ClassifierRole:

    pass
class Feature:

    pass
class Multiplicity:

    pass
class Collaboration:

    pass
class CollaborationInstanceSet:

    pass
class Interaction:

    pass
class core_Namespace:

    pass
class core_GeneralizableElement:

    pass
class behavioral_elements_collaborations_Collaboration(core_GeneralizableElement, core_Namespace):

    pass
class Guard:

    pass
class TimeExpression:

    pass
class Event:

    pass
class behavioral_elements_state_machines_CallEvent(Event):

    pass
class behavioral_elements_state_machines_TimeEvent(Event):

    pass
class behavioral_elements_state_machines_SignalEvent(Event):

    pass
class behavioral_elements_state_machines_ChangeEvent(Event):

    pass
class StateMachine:

    pass
class behavioral_elements_activity_graphs_ActivityGraph(StateMachine):

    pass
class StateVertex:

    pass
class behavioral_elements_state_machines_StubState(StateVertex):

    def __init__(self, referenceState: str, state_machines193: "behavioral_elements_state_machines_Transition", state_machines190: "behavioral_elements_state_machines_Transition", state_machines196: "behavioral_elements_state_machines_CompositeState"):
        self.referenceState = referenceState
        
    @property
    def referenceState(self) -> str:
        return self.__referenceState

    @referenceState.setter
    def referenceState(self, referenceState: str):
        self.__referenceState = referenceState

class behavioral_elements_state_machines_Pseudostate(StateVertex):

    def __init__(self, kind: str, state_machines193: "behavioral_elements_state_machines_Transition", state_machines190: "behavioral_elements_state_machines_Transition", state_machines196: "behavioral_elements_state_machines_CompositeState"):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class behavioral_elements_state_machines_SynchState(StateVertex):

    def __init__(self, bound: str, state_machines193: "behavioral_elements_state_machines_Transition", state_machines190: "behavioral_elements_state_machines_Transition", state_machines196: "behavioral_elements_state_machines_CompositeState"):
        self.bound = bound
        
    @property
    def bound(self) -> str:
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound

class behavioral_elements_state_machines_State(StateVertex):

    pass
class CompositeState:

    pass
class behavioral_elements_state_machines_SubmachineState(CompositeState):

    pass
class Parameter:

    pass
class SubmachineState:

    pass
class behavioral_elements_activity_graphs_SubactivityState(SubmachineState):

    def __init__(self, isDynamic: str, behavioral_elements_activity_graphs_SubactivityState: "ArgListsExpression" = None, behavioral_elements_activity_graphs_SubactivityState315: "Multiplicity" = None, state_machines140: "behavioral_elements_state_machines_StateMachine"):
        self.isDynamic = isDynamic
        self.behavioral_elements_activity_graphs_SubactivityState = behavioral_elements_activity_graphs_SubactivityState
        self.behavioral_elements_activity_graphs_SubactivityState315 = behavioral_elements_activity_graphs_SubactivityState315
        
    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def behavioral_elements_activity_graphs_SubactivityState315(self):
        return self.__behavioral_elements_activity_graphs_SubactivityState315

    @behavioral_elements_activity_graphs_SubactivityState315.setter
    def behavioral_elements_activity_graphs_SubactivityState315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_SubactivityState__behavioral_elements_activity_graphs_SubactivityState315", None)
        self.__behavioral_elements_activity_graphs_SubactivityState315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity316"):
                opp_val = getattr(old_value, "Multiplicity316", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity316"):
                opp_val = getattr(value, "Multiplicity316", None)
                setattr(value, "Multiplicity316", self)

    @property
    def behavioral_elements_activity_graphs_SubactivityState(self):
        return self.__behavioral_elements_activity_graphs_SubactivityState

    @behavioral_elements_activity_graphs_SubactivityState.setter
    def behavioral_elements_activity_graphs_SubactivityState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_SubactivityState__behavioral_elements_activity_graphs_SubactivityState", None)
        self.__behavioral_elements_activity_graphs_SubactivityState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArgListsExpression"):
                opp_val = getattr(old_value, "ArgListsExpression", None)
                if opp_val == self:
                    setattr(old_value, "ArgListsExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArgListsExpression"):
                opp_val = getattr(value, "ArgListsExpression", None)
                setattr(value, "ArgListsExpression", self)

class State:

    pass
class behavioral_elements_state_machines_SimpleState(State):

    pass
class behavioral_elements_state_machines_FinalState(State):

    pass
class behavioral_elements_state_machines_CompositeState(State):

    def __init__(self, isConcurrent: str, StateVertex195: set["StateVertex"] = None, state_machines182: "behavioral_elements_state_machines_Transition", state_machines135: "behavioral_elements_state_machines_StateMachine", State331: "behavioral_elements_activity_graphs_ClassifierInState"):
        self.isConcurrent = isConcurrent
        self.StateVertex195 = StateVertex195 if StateVertex195 is not None else set()
        
    @property
    def isConcurrent(self) -> str:
        return self.__isConcurrent

    @isConcurrent.setter
    def isConcurrent(self, isConcurrent: str):
        self.__isConcurrent = isConcurrent

    @property
    def StateVertex195(self):
        return self.__StateVertex195

    @StateVertex195.setter
    def StateVertex195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_state_machines_CompositeState__StateVertex195", None)
        self.__StateVertex195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "state_machines196"):
                    opp_val = getattr(item, "state_machines196", None)
                    
                    if opp_val == self:
                        setattr(item, "state_machines196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "state_machines196"):
                    opp_val = getattr(item, "state_machines196", None)
                    
                    setattr(item, "state_machines196", self)
                    

class UseCase:

    pass
class BooleanExpression:

    pass
class Relationship:

    pass
class behavioral_elements_use_cases_Include(Relationship):

    pass
class behavioral_elements_use_cases_Extend(Relationship):

    pass
class ExtensionPoint:

    pass
class Include:

    pass
class Extend:

    pass
class NodeInstance:

    pass
class InteractionInstanceSet:

    pass
class Message:

    pass
class AssociationEnd:

    pass
class behavioral_elements_collaborations_AssociationEndRole(AssociationEnd):

    pass
class Expression:

    pass
class Association:

    pass
class behavioral_elements_collaborations_AssociationRole(Association):

    pass
class Signal:

    pass
class behavioral_elements_common_behavior_Exception(Signal):

    pass
class Operation:

    pass
class common_behavior_Link:

    pass
class common_behavior_Object:

    pass
class behavioral_elements_common_behavior_LinkObject(common_behavior_Link, common_behavior_Object):

    pass
class Attribute:

    pass
class Action:

    pass
class behavioral_elements_common_behavior_SendAction(Action):

    pass
class behavioral_elements_common_behavior_TerminateAction(Action):

    pass
class behavioral_elements_common_behavior_ActionSequence(Action):

    pass
class behavioral_elements_common_behavior_ReturnAction(Action):

    pass
class behavioral_elements_common_behavior_DestroyAction(Action):

    pass
class behavioral_elements_common_behavior_CallAction(Action):

    pass
class behavioral_elements_common_behavior_UninterpretedAction(Action):

    pass
class behavioral_elements_common_behavior_CreateAction(Action):

    pass
class Transition:

    pass
class Stimulus:

    pass
class ActionSequence:

    pass
class Argument:

    pass
class ActionExpression:

    pass
class ObjectSetExpression:

    pass
class IterationExpression:

    pass
class SignalEvent:

    pass
class SendAction:

    pass
class BehavioralFeature:

    pass
class behavioral_elements_common_behavior_Reception(BehavioralFeature):

    def __init__(self, specification: str, isRoot: str, isLeaf: str, isAbstract: str, Signal63: "Signal" = None, foundation.ecorecore: "behavioral_elements_common_behavior_Signal"):
        self.specification = specification
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.Signal63 = Signal63
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def isRoot(self) -> str:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot

    @property
    def Signal63(self):
        return self.__Signal63

    @Signal63.setter
    def Signal63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Reception__Signal63", None)
        self.__Signal63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_behavior64"):
                opp_val = getattr(old_value, "common_behavior64", None)
                if opp_val == self:
                    setattr(old_value, "common_behavior64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_behavior64"):
                opp_val = getattr(value, "common_behavior64", None)
                setattr(value, "common_behavior64", self)

class Reception:

    pass
class Link:

    pass
class Instance:

    pass
class behavioral_elements_common_behavior_Object(Instance):

    pass
class behavioral_elements_use_cases_UseCaseInstance(Instance):

    pass
class behavioral_elements_common_behavior_ComponentInstance(Instance):

    pass
class behavioral_elements_common_behavior_NodeInstance(Instance):

    pass
class behavioral_elements_common_behavior_DataValue(Instance):

    pass
class behavioral_elements_common_behavior_SubsystemInstance(Instance):

    pass
class ComponentInstance:

    pass
class LinkEnd:

    pass
class AttributeLink:

    pass
class Classifier:

    pass
class behavioral_elements_common_behavior_Signal(Classifier):

    pass
class behavioral_elements_activity_graphs_ClassifierInState(Classifier):

    pass
class behavioral_elements_collaborations_ClassifierRole(Classifier):

    pass
class behavioral_elements_use_cases_Actor(Classifier):

    pass
class behavioral_elements_use_cases_UseCase(Classifier):

    pass
class ModelElement:

    pass
class behavioral_elements_collaborations_CollaborationInstanceSet(ModelElement):

    pass
class behavioral_elements_state_machines_Transition(ModelElement):

    pass
class behavioral_elements_common_behavior_Argument(ModelElement):

    pass
class behavioral_elements_common_behavior_AttributeLink(ModelElement):

    pass
class behavioral_elements_common_behavior_Action(ModelElement):

    def __init__(self, isAsynchronous: str, behavioral_elements_common_behavior_Action: "IterationExpression" = None, behavioral_elements_common_behavior_Action21: "ObjectSetExpression" = None, behavioral_elements_common_behavior_Action23: "ActionExpression" = None, Argument: set["Argument"] = None, ActionSequence: "ActionSequence" = None, Stimulus: set["Stimulus"] = None, Transition: "Transition" = None, foundation.ecorecore133: "behavioral_elements_state_machines_StateMachine", ModelElement310: "behavioral_elements_activity_graphs_Partition", ModelElement229: "behavioral_elements_collaborations_ClassifierRole", ModelElement307: "behavioral_elements_collaborations_CollaborationInstanceSet", ModelElement213: "behavioral_elements_collaborations_Collaboration"):
        self.isAsynchronous = isAsynchronous
        self.behavioral_elements_common_behavior_Action = behavioral_elements_common_behavior_Action
        self.behavioral_elements_common_behavior_Action21 = behavioral_elements_common_behavior_Action21
        self.behavioral_elements_common_behavior_Action23 = behavioral_elements_common_behavior_Action23
        self.Argument = Argument if Argument is not None else set()
        self.ActionSequence = ActionSequence
        self.Stimulus = Stimulus if Stimulus is not None else set()
        self.Transition = Transition
        
    @property
    def isAsynchronous(self) -> str:
        return self.__isAsynchronous

    @isAsynchronous.setter
    def isAsynchronous(self, isAsynchronous: str):
        self.__isAsynchronous = isAsynchronous

    @property
    def behavioral_elements_common_behavior_Action(self):
        return self.__behavioral_elements_common_behavior_Action

    @behavioral_elements_common_behavior_Action.setter
    def behavioral_elements_common_behavior_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__behavioral_elements_common_behavior_Action", None)
        self.__behavioral_elements_common_behavior_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IterationExpression"):
                opp_val = getattr(old_value, "IterationExpression", None)
                if opp_val == self:
                    setattr(old_value, "IterationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IterationExpression"):
                opp_val = getattr(value, "IterationExpression", None)
                setattr(value, "IterationExpression", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_machines31"):
                opp_val = getattr(old_value, "state_machines31", None)
                if opp_val == self:
                    setattr(old_value, "state_machines31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_machines31"):
                opp_val = getattr(value, "state_machines31", None)
                setattr(value, "state_machines31", self)

    @property
    def Stimulus(self):
        return self.__Stimulus

    @Stimulus.setter
    def Stimulus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__Stimulus", None)
        self.__Stimulus = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "common_behavior29"):
                    opp_val = getattr(item, "common_behavior29", None)
                    
                    if opp_val == self:
                        setattr(item, "common_behavior29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "common_behavior29"):
                    opp_val = getattr(item, "common_behavior29", None)
                    
                    setattr(item, "common_behavior29", self)
                    

    @property
    def ActionSequence(self):
        return self.__ActionSequence

    @ActionSequence.setter
    def ActionSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__ActionSequence", None)
        self.__ActionSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_behavior27"):
                opp_val = getattr(old_value, "common_behavior27", None)
                if opp_val == self:
                    setattr(old_value, "common_behavior27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_behavior27"):
                opp_val = getattr(value, "common_behavior27", None)
                setattr(value, "common_behavior27", self)

    @property
    def behavioral_elements_common_behavior_Action21(self):
        return self.__behavioral_elements_common_behavior_Action21

    @behavioral_elements_common_behavior_Action21.setter
    def behavioral_elements_common_behavior_Action21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__behavioral_elements_common_behavior_Action21", None)
        self.__behavioral_elements_common_behavior_Action21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjectSetExpression"):
                opp_val = getattr(old_value, "ObjectSetExpression", None)
                if opp_val == self:
                    setattr(old_value, "ObjectSetExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjectSetExpression"):
                opp_val = getattr(value, "ObjectSetExpression", None)
                setattr(value, "ObjectSetExpression", self)

    @property
    def Argument(self):
        return self.__Argument

    @Argument.setter
    def Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__Argument", None)
        self.__Argument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "common_behavior25"):
                    opp_val = getattr(item, "common_behavior25", None)
                    
                    if opp_val == self:
                        setattr(item, "common_behavior25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "common_behavior25"):
                    opp_val = getattr(item, "common_behavior25", None)
                    
                    setattr(item, "common_behavior25", self)
                    

    @property
    def behavioral_elements_common_behavior_Action23(self):
        return self.__behavioral_elements_common_behavior_Action23

    @behavioral_elements_common_behavior_Action23.setter
    def behavioral_elements_common_behavior_Action23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__behavioral_elements_common_behavior_Action23", None)
        self.__behavioral_elements_common_behavior_Action23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionExpression"):
                opp_val = getattr(old_value, "ActionExpression", None)
                if opp_val == self:
                    setattr(old_value, "ActionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionExpression"):
                opp_val = getattr(value, "ActionExpression", None)
                setattr(value, "ActionExpression", self)

class behavioral_elements_common_behavior_LinkEnd(ModelElement):

    pass
class behavioral_elements_activity_graphs_Partition(ModelElement):

    pass
class behavioral_elements_collaborations_InteractionInstanceSet(ModelElement):

    pass
class behavioral_elements_common_behavior_Link(ModelElement):

    pass
class behavioral_elements_state_machines_StateMachine(ModelElement):

    pass
class behavioral_elements_state_machines_Event(ModelElement):

    pass
class behavioral_elements_state_machines_StateVertex(ModelElement):

    pass
class behavioral_elements_state_machines_Guard(ModelElement):

    pass
class behavioral_elements_collaborations_Interaction(ModelElement):

    pass
class behavioral_elements_collaborations_Message(ModelElement):

    pass
class behavioral_elements_use_cases_ExtensionPoint(ModelElement):

    def __init__(self, location: str, UseCase127: "UseCase" = None, Extend130: set["Extend"] = None, foundation.ecorecore133: "behavioral_elements_state_machines_StateMachine", ModelElement310: "behavioral_elements_activity_graphs_Partition", ModelElement229: "behavioral_elements_collaborations_ClassifierRole", ModelElement307: "behavioral_elements_collaborations_CollaborationInstanceSet", ModelElement213: "behavioral_elements_collaborations_Collaboration"):
        self.location = location
        self.UseCase127 = UseCase127
        self.Extend130 = Extend130 if Extend130 is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def UseCase127(self):
        return self.__UseCase127

    @UseCase127.setter
    def UseCase127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_use_cases_ExtensionPoint__UseCase127", None)
        self.__UseCase127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "use_cases128"):
                opp_val = getattr(old_value, "use_cases128", None)
                if opp_val == self:
                    setattr(old_value, "use_cases128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "use_cases128"):
                opp_val = getattr(value, "use_cases128", None)
                setattr(value, "use_cases128", self)

    @property
    def Extend130(self):
        return self.__Extend130

    @Extend130.setter
    def Extend130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_use_cases_ExtensionPoint__Extend130", None)
        self.__Extend130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "use_cases131"):
                    opp_val = getattr(item, "use_cases131", None)
                    
                    if opp_val == self:
                        setattr(item, "use_cases131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "use_cases131"):
                    opp_val = getattr(item, "use_cases131", None)
                    
                    setattr(item, "use_cases131", self)
                    

class behavioral_elements_common_behavior_Stimulus(ModelElement):

    pass
class behavioral_elements_common_behavior_Instance(ModelElement):

    pass