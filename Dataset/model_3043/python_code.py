from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArgListsExpression:

    pass
class ActivityGraph:

    pass
class Partition:

    pass
class ActionState:

    pass
class behavioral_elements_activity_graphs_CallState(ActionState):

    pass
class SimpleState:

    pass
class behavioral_elements_activity_graphs_ActionState(SimpleState):

    def __init__(self, isDynamic: str, behavioral_elements_activity_graphs_ActionState: "ArgListsExpression" = None, behavioral_elements_activity_graphs_ActionState260: "Multiplicity_" = None):
        self.isDynamic = isDynamic
        self.behavioral_elements_activity_graphs_ActionState = behavioral_elements_activity_graphs_ActionState
        self.behavioral_elements_activity_graphs_ActionState260 = behavioral_elements_activity_graphs_ActionState260
        
        pass
    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


    @property
    def behavioral_elements_activity_graphs_ActionState260(self):
        return self.__behavioral_elements_activity_graphs_ActionState260

    @behavioral_elements_activity_graphs_ActionState260.setter
    def behavioral_elements_activity_graphs_ActionState260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ActionState__behavioral_elements_activity_graphs_ActionState260", None)
        self.__behavioral_elements_activity_graphs_ActionState260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity261"):
                opp_val = getattr(old_value, "Multiplicity261", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity261"):
                opp_val = getattr(value, "Multiplicity261", None)
                setattr(value, "Multiplicity261", self)

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
            if hasattr(old_value, "ArgListsExpression258"):
                opp_val = getattr(old_value, "ArgListsExpression258", None)
                if opp_val == self:
                    setattr(old_value, "ArgListsExpression258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArgListsExpression258"):
                opp_val = getattr(value, "ArgListsExpression258", None)
                setattr(value, "ArgListsExpression258", self)

class behavioral_elements_activity_graphs_ObjectFlowState(SimpleState):

    def __init__(self, isSynch: str, behavioral_elements_activity_graphs_ObjectFlowState: set["Parameter"] = None, behavioral_elements_activity_graphs_ObjectFlowState265: "Classifier" = None):
        self.isSynch = isSynch
        self.behavioral_elements_activity_graphs_ObjectFlowState = behavioral_elements_activity_graphs_ObjectFlowState if behavioral_elements_activity_graphs_ObjectFlowState is not None else set()
        self.behavioral_elements_activity_graphs_ObjectFlowState265 = behavioral_elements_activity_graphs_ObjectFlowState265
        
        pass
    @property
    def isSynch(self):
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
                if hasattr(item, "Parameter263"):
                    opp_val = getattr(item, "Parameter263", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter263"):
                    opp_val = getattr(item, "Parameter263", None)
                    
                    setattr(item, "Parameter263", self)
                    

    @property
    def behavioral_elements_activity_graphs_ObjectFlowState265(self):
        return self.__behavioral_elements_activity_graphs_ObjectFlowState265

    @behavioral_elements_activity_graphs_ObjectFlowState265.setter
    def behavioral_elements_activity_graphs_ObjectFlowState265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_ObjectFlowState__behavioral_elements_activity_graphs_ObjectFlowState265", None)
        self.__behavioral_elements_activity_graphs_ObjectFlowState265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier266"):
                opp_val = getattr(old_value, "Classifier266", None)
                if opp_val == self:
                    setattr(old_value, "Classifier266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier266"):
                opp_val = getattr(value, "Classifier266", None)
                setattr(value, "Classifier266", self)

class AssociationRole:

    pass
class Feature:

    pass
class ClassifierRole:

    pass
class Interaction:

    pass
class core_Namespace:

    pass
class core_GeneralizableElement:

    pass
class behavioral_elements_collaborations_Collaboration(core_Namespace, core_GeneralizableElement):

    pass
class Multiplicity_:

    pass
class Collaboration:

    pass
class CollaborationInstanceSet:

    pass
class Guard:

    pass
class StateMachine:

    pass
class behavioral_elements_activity_graphs_ActivityGraph(StateMachine):

    pass
class StateVertex:

    pass
class behavioral_elements_state_machines_StubState(StateVertex):

    def __init__(self, referenceState: str, StateVertex148: "behavioral_elements_state_machines_Transition" = None, StateVertex: "behavioral_elements_state_machines_Transition" = None, StateVertex150: "behavioral_elements_state_machines_CompositeState" = None):
        self.referenceState = referenceState
        
        pass
    @property
    def referenceState(self):
        return self.__referenceState

    @referenceState.setter
    def referenceState(self, referenceState: str):
        self.__referenceState = referenceState


class behavioral_elements_state_machines_Pseudostate(StateVertex):

    def __init__(self, kind: str, StateVertex148: "behavioral_elements_state_machines_Transition" = None, StateVertex: "behavioral_elements_state_machines_Transition" = None, StateVertex150: "behavioral_elements_state_machines_CompositeState" = None):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class behavioral_elements_state_machines_SynchState(StateVertex):

    def __init__(self, bound: str, StateVertex148: "behavioral_elements_state_machines_Transition" = None, StateVertex: "behavioral_elements_state_machines_Transition" = None, StateVertex150: "behavioral_elements_state_machines_CompositeState" = None):
        self.bound = bound
        
        pass
    @property
    def bound(self):
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

    def __init__(self, isDynamic: str, behavioral_elements_activity_graphs_SubactivityState: "ArgListsExpression" = None, behavioral_elements_activity_graphs_SubactivityState255: "Multiplicity_" = None, SubmachineState: "behavioral_elements_state_machines_StateMachine" = None):
        self.isDynamic = isDynamic
        self.behavioral_elements_activity_graphs_SubactivityState = behavioral_elements_activity_graphs_SubactivityState
        self.behavioral_elements_activity_graphs_SubactivityState255 = behavioral_elements_activity_graphs_SubactivityState255
        
        pass
    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


    @property
    def behavioral_elements_activity_graphs_SubactivityState255(self):
        return self.__behavioral_elements_activity_graphs_SubactivityState255

    @behavioral_elements_activity_graphs_SubactivityState255.setter
    def behavioral_elements_activity_graphs_SubactivityState255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_activity_graphs_SubactivityState__behavioral_elements_activity_graphs_SubactivityState255", None)
        self.__behavioral_elements_activity_graphs_SubactivityState255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity256"):
                opp_val = getattr(old_value, "Multiplicity256", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity256"):
                opp_val = getattr(value, "Multiplicity256", None)
                setattr(value, "Multiplicity256", self)

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

class TimeExpression:

    pass
class Event:

    pass
class behavioral_elements_state_machines_TimeEvent(Event):

    pass
class behavioral_elements_state_machines_CallEvent(Event):

    pass
class behavioral_elements_state_machines_SignalEvent(Event):

    pass
class behavioral_elements_state_machines_ChangeEvent(Event):

    pass
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
class State:

    pass
class behavioral_elements_state_machines_CompositeState(State):

    def __init__(self, isConcurrent: str, container: set["StateVertex"] = None, State: "behavioral_elements_state_machines_StateMachine" = None, State140: "behavioral_elements_state_machines_Transition" = None, State271: "behavioral_elements_activity_graphs_ClassifierInState" = None):
        self.isConcurrent = isConcurrent
        self.container = container if container is not None else set()
        
        pass
    @property
    def isConcurrent(self):
        return self.__isConcurrent

    @isConcurrent.setter
    def isConcurrent(self, isConcurrent: str):
        self.__isConcurrent = isConcurrent


    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_state_machines_CompositeState__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex150"):
                    opp_val = getattr(item, "StateVertex150", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex150"):
                    opp_val = getattr(item, "StateVertex150", None)
                    
                    setattr(item, "StateVertex150", self)
                    

class behavioral_elements_state_machines_FinalState(State):

    pass
class behavioral_elements_state_machines_SimpleState(State):

    pass
class NodeInstance:

    pass
class InteractionInstanceSet:

    pass
class Message:

    pass
class Include:

    pass
class Extend:

    pass
class AssociationEnd:

    pass
class behavioral_elements_collaborations_AssociationEndRole(AssociationEnd):

    pass
class Expression:

    pass
class Operation:

    pass
class common_behavior_Link:

    pass
class common_behavior_Object:

    pass
class behavioral_elements_common_behavior_LinkObject(common_behavior_Link, common_behavior_Object):

    pass
class Signal:

    pass
class behavioral_elements_common_behavior_Exception(Signal):

    pass
class Attribute:

    pass
class Action:

    pass
class behavioral_elements_common_behavior_DestroyAction(Action):

    pass
class behavioral_elements_common_behavior_SendAction(Action):

    pass
class behavioral_elements_common_behavior_UninterpretedAction(Action):

    pass
class behavioral_elements_common_behavior_TerminateAction(Action):

    pass
class behavioral_elements_common_behavior_ActionSequence(Action):

    pass
class behavioral_elements_common_behavior_CallAction(Action):

    pass
class behavioral_elements_common_behavior_ReturnAction(Action):

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
class Association:

    pass
class behavioral_elements_collaborations_AssociationRole(Association):

    pass
class BehavioralFeature:

    pass
class behavioral_elements_common_behavior_Reception(BehavioralFeature):

    def __init__(self, specification: str, isRoot: str, isLeaf: str, isAbstract: str, reception: "Signal" = None, BehavioralFeature: "behavioral_elements_common_behavior_Signal" = None):
        self.specification = specification
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.reception = reception
        
        pass
    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


    @property
    def isRoot(self):
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


    @property
    def reception(self):
        return self.__reception

    @reception.setter
    def reception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Reception__reception", None)
        self.__reception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signal48"):
                opp_val = getattr(old_value, "Signal48", None)
                if opp_val == self:
                    setattr(old_value, "Signal48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signal48"):
                opp_val = getattr(value, "Signal48", None)
                setattr(value, "Signal48", self)

class Reception:

    pass
class Link:

    pass
class Instance:

    pass
class behavioral_elements_common_behavior_Object(Instance):

    pass
class behavioral_elements_common_behavior_ComponentInstance(Instance):

    pass
class behavioral_elements_use_cases_UseCaseInstance(Instance):

    pass
class behavioral_elements_common_behavior_DataValue(Instance):

    pass
class behavioral_elements_common_behavior_SubsystemInstance(Instance):

    pass
class behavioral_elements_common_behavior_NodeInstance(Instance):

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
class behavioral_elements_collaborations_ClassifierRole(Classifier):

    pass
class behavioral_elements_activity_graphs_ClassifierInState(Classifier):

    pass
class behavioral_elements_use_cases_UseCase(Classifier):

    pass
class behavioral_elements_use_cases_Actor(Classifier):

    pass
class ObjectSetExpression:

    pass
class IterationExpression:

    pass
class SignalEvent:

    pass
class SendAction:

    pass
class ModelElement:

    pass
class behavioral_elements_common_behavior_Stimulus(ModelElement):

    pass
class behavioral_elements_use_cases_ExtensionPoint(ModelElement):

    def __init__(self, location: str, extensionPoint: "UseCase" = None, extensionPoint100: set["Extend"] = None, ModelElement251: "behavioral_elements_activity_graphs_Partition" = None, ModelElement: "behavioral_elements_state_machines_StateMachine" = None, ModelElement179: "behavioral_elements_collaborations_ClassifierRole" = None, ModelElement248: "behavioral_elements_collaborations_CollaborationInstanceSet" = None, ModelElement163: "behavioral_elements_collaborations_Collaboration" = None):
        self.location = location
        self.extensionPoint = extensionPoint
        self.extensionPoint100 = extensionPoint100 if extensionPoint100 is not None else set()
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def extensionPoint100(self):
        return self.__extensionPoint100

    @extensionPoint100.setter
    def extensionPoint100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_use_cases_ExtensionPoint__extensionPoint100", None)
        self.__extensionPoint100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extend101"):
                    opp_val = getattr(item, "Extend101", None)
                    
                    if opp_val == self:
                        setattr(item, "Extend101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extend101"):
                    opp_val = getattr(item, "Extend101", None)
                    
                    setattr(item, "Extend101", self)
                    

    @property
    def extensionPoint(self):
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_use_cases_ExtensionPoint__extensionPoint", None)
        self.__extensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase98"):
                opp_val = getattr(old_value, "UseCase98", None)
                if opp_val == self:
                    setattr(old_value, "UseCase98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase98"):
                opp_val = getattr(value, "UseCase98", None)
                setattr(value, "UseCase98", self)

class behavioral_elements_state_machines_StateVertex(ModelElement):

    pass
class behavioral_elements_collaborations_InteractionInstanceSet(ModelElement):

    pass
class behavioral_elements_common_behavior_LinkEnd(ModelElement):

    pass
class behavioral_elements_common_behavior_AttributeLink(ModelElement):

    pass
class behavioral_elements_common_behavior_Action(ModelElement):

    def __init__(self, isAsynchronous: str, behavioral_elements_common_behavior_Action: "IterationExpression" = None, behavioral_elements_common_behavior_Action19: "ObjectSetExpression" = None, behavioral_elements_common_behavior_Action21: "ActionExpression" = None, action: set["Argument"] = None, action24: "ActionSequence" = None, dispatchAction: set["Stimulus"] = None, effect: "Transition" = None, ModelElement251: "behavioral_elements_activity_graphs_Partition" = None, ModelElement: "behavioral_elements_state_machines_StateMachine" = None, ModelElement179: "behavioral_elements_collaborations_ClassifierRole" = None, ModelElement248: "behavioral_elements_collaborations_CollaborationInstanceSet" = None, ModelElement163: "behavioral_elements_collaborations_Collaboration" = None):
        self.isAsynchronous = isAsynchronous
        self.behavioral_elements_common_behavior_Action = behavioral_elements_common_behavior_Action
        self.behavioral_elements_common_behavior_Action19 = behavioral_elements_common_behavior_Action19
        self.behavioral_elements_common_behavior_Action21 = behavioral_elements_common_behavior_Action21
        self.action = action if action is not None else set()
        self.action24 = action24
        self.dispatchAction = dispatchAction if dispatchAction is not None else set()
        self.effect = effect
        
        pass
    @property
    def isAsynchronous(self):
        return self.__isAsynchronous

    @isAsynchronous.setter
    def isAsynchronous(self, isAsynchronous: str):
        self.__isAsynchronous = isAsynchronous


    @property
    def dispatchAction(self):
        return self.__dispatchAction

    @dispatchAction.setter
    def dispatchAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__dispatchAction", None)
        self.__dispatchAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Stimulus"):
                    opp_val = getattr(item, "Stimulus", None)
                    
                    if opp_val == self:
                        setattr(item, "Stimulus", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Stimulus"):
                    opp_val = getattr(item, "Stimulus", None)
                    
                    setattr(item, "Stimulus", self)
                    

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__action", None)
        self.__action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    setattr(item, "Argument", self)
                    

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
            if hasattr(old_value, "ActionExpression"):
                opp_val = getattr(old_value, "ActionExpression", None)
                if opp_val == self:
                    setattr(old_value, "ActionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionExpression"):
                opp_val = getattr(value, "ActionExpression", None)
                setattr(value, "ActionExpression", self)

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
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__effect", None)
        self.__effect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def behavioral_elements_common_behavior_Action19(self):
        return self.__behavioral_elements_common_behavior_Action19

    @behavioral_elements_common_behavior_Action19.setter
    def behavioral_elements_common_behavior_Action19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__behavioral_elements_common_behavior_Action19", None)
        self.__behavioral_elements_common_behavior_Action19 = value
        
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
    def action24(self):
        return self.__action24

    @action24.setter
    def action24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_elements_common_behavior_Action__action24", None)
        self.__action24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionSequence"):
                opp_val = getattr(old_value, "ActionSequence", None)
                if opp_val == self:
                    setattr(old_value, "ActionSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionSequence"):
                opp_val = getattr(value, "ActionSequence", None)
                setattr(value, "ActionSequence", self)

class behavioral_elements_state_machines_StateMachine(ModelElement):

    pass
class behavioral_elements_collaborations_CollaborationInstanceSet(ModelElement):

    pass
class behavioral_elements_collaborations_Message(ModelElement):

    pass
class behavioral_elements_state_machines_Transition(ModelElement):

    pass
class behavioral_elements_common_behavior_Link(ModelElement):

    pass
class behavioral_elements_state_machines_Event(ModelElement):

    pass
class behavioral_elements_collaborations_Interaction(ModelElement):

    pass
class behavioral_elements_activity_graphs_Partition(ModelElement):

    pass
class behavioral_elements_state_machines_Guard(ModelElement):

    pass
class behavioral_elements_common_behavior_Argument(ModelElement):

    pass
class behavioral_elements_common_behavior_Instance(ModelElement):

    pass