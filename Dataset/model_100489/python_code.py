from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    pk_choice = "pk_choice"
    pk_deepHistory = "pk_deepHistory"
    pk_fork = "pk_fork"
    pk_initial = "pk_initial"
    pk_join = "pk_join"
    pk_junction = "pk_junction"
    pk_shallowHistory = "pk_shallowHistory"
class CallConcurrencyKind(Enum):
    cck_sequential = "cck_sequential"
    cck_guarded = "cck_guarded"
    cck_concurrent = "cck_concurrent"
class ParameterDirectionKind(Enum):
    pdk_in = "pdk_in"
    pdk_inout = "pdk_inout"
    pdk_out = "pdk_out"
    pdk_return = "pdk_return"
class VisibilityKind(Enum):
    vk_public = "vk_public"
    vk_protected = "vk_protected"
    vk_private = "vk_private"
    vk_package = "vk_package"
class ScopeKind(Enum):
    sk_instance = "sk_instance"
    sk_classifier = "sk_classifier"


############################################
# Definition of Classes
############################################

class Relationship:

    pass
class Core_Generalization_(Relationship):

    def __init__(self, discriminator: str, Core_Generalization: "GeneralizableElement" = None, powertypeRange: "Classifier" = None, generalization: "GeneralizableElement" = None):
        self.discriminator = discriminator
        self.Core_Generalization = Core_Generalization
        self.powertypeRange = powertypeRange
        self.generalization = generalization
        
        pass
    @property
    def discriminator(self):
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator


    @property
    def Core_Generalization(self):
        return self.__Core_Generalization

    @Core_Generalization.setter
    def Core_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___Core_Generalization", None)
        self.__Core_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralizableElement"):
                opp_val = getattr(old_value, "GeneralizableElement", None)
                if opp_val == self:
                    setattr(old_value, "GeneralizableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralizableElement"):
                opp_val = getattr(value, "GeneralizableElement", None)
                setattr(value, "GeneralizableElement", self)

    @property
    def powertypeRange(self):
        return self.__powertypeRange

    @powertypeRange.setter
    def powertypeRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___powertypeRange", None)
        self.__powertypeRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier86"):
                opp_val = getattr(old_value, "Classifier86", None)
                if opp_val == self:
                    setattr(old_value, "Classifier86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier86"):
                opp_val = getattr(value, "Classifier86", None)
                setattr(value, "Classifier86", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralizableElement88"):
                opp_val = getattr(old_value, "GeneralizableElement88", None)
                if opp_val == self:
                    setattr(old_value, "GeneralizableElement88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralizableElement88"):
                opp_val = getattr(value, "GeneralizableElement88", None)
                setattr(value, "GeneralizableElement88", self)

class Feature:

    pass
class Core_BehavioralFeature(Feature):

    def __init__(self, isQuery: str, behavioralFeature: set["Parameter"] = None, Feature: "Core_Classifier" = None):
        self.isQuery = isQuery
        self.behavioralFeature = behavioralFeature if behavioralFeature is not None else set()
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery


    @property
    def behavioralFeature(self):
        return self.__behavioralFeature

    @behavioralFeature.setter
    def behavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_BehavioralFeature__behavioralFeature", None)
        self.__behavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter77"):
                    opp_val = getattr(item, "Parameter77", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter77"):
                    opp_val = getattr(item, "Parameter77", None)
                    
                    setattr(item, "Parameter77", self)
                    

class GeneralizableElement:

    pass
class BooleanExpression:

    pass
class Generalization_:

    pass
class Guard:

    pass
class Namespace:

    pass
class Core_Classifier(GeneralizableElement, Namespace):

    pass
class Element:

    pass
class Core_ModelElement(Element):

    def __init__(self, name: str, visibility: str, isSpecification: str, ownedElement: "Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.isSpecification = isSpecification
        self.ownedElement = ownedElement
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def isSpecification(self):
        return self.__isSpecification

    @isSpecification.setter
    def isSpecification(self, isSpecification: str):
        self.__isSpecification = isSpecification


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ModelElement__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

class Core_Element(ABC):

    pass
class Event:

    pass
class State_Machines_ChangeEvent(Event):

    pass
class StateVertex:

    pass
class State_Machines_StubState(StateVertex):

    def __init__(self, referenceState: str, StateVertex53: "State_Machines_Transition" = None, StateVertex59: "State_Machines_CompositeState" = None, StateVertex: "State_Machines_Transition" = None):
        self.referenceState = referenceState
        
        pass
    @property
    def referenceState(self):
        return self.__referenceState

    @referenceState.setter
    def referenceState(self, referenceState: str):
        self.__referenceState = referenceState


class State_Machines_SynchState(StateVertex):

    def __init__(self, bound: str, StateVertex53: "State_Machines_Transition" = None, StateVertex59: "State_Machines_CompositeState" = None, StateVertex: "State_Machines_Transition" = None):
        self.bound = bound
        
        pass
    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound


class State_Machines_Pseudostate(StateVertex):

    def __init__(self, kind: str, StateVertex53: "State_Machines_Transition" = None, StateVertex59: "State_Machines_CompositeState" = None, StateVertex: "State_Machines_Transition" = None):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class State_Machines_State(StateVertex):

    pass
class State_Machines_SignalEvent(Event):

    pass
class State_Machines_CallEvent(Event):

    pass
class TimeExpression:

    pass
class State_Machines_TimeEvent(Event):

    pass
class StateMachine:

    pass
class Data_Types_Expression:

    def __init__(self, language: str, body: str):
        self.language = language
        self.body = body
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class CompositeState:

    pass
class State_Machines_SubmachineState(CompositeState):

    pass
class Parameter:

    pass
class Transition:

    pass
class State:

    pass
class State_Machines_SimpleState(State):

    pass
class State_Machines_FinalState(State):

    pass
class State_Machines_CompositeState(State):

    def __init__(self, isConcurrent: str, container: set["StateVertex"] = None, State: "State_Machines_StateMachine" = None):
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
        old_value = getattr(self, f"_State_Machines_CompositeState__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex59"):
                    opp_val = getattr(item, "StateVertex59", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex59"):
                    opp_val = getattr(item, "StateVertex59", None)
                    
                    setattr(item, "StateVertex59", self)
                    

class SubmachineState:

    pass
class Operation:

    pass
class Action:

    pass
class Common_Behavior_DestroyAction(Action):

    pass
class Common_Behavior_SendAction(Action):

    pass
class Common_Behavior_CallAction(Action):

    pass
class Common_Behavior_UninterpretedAction(Action):

    pass
class Common_Behavior_CreateAction(Action):

    pass
class ActionExpression:

    pass
class Common_Behavior_TerminateAction(Action):

    pass
class Common_Behavior_ReturnAction(Action):

    pass
class BehavioralFeature:

    pass
class Core_Operation(BehavioralFeature):

    def __init__(self, concurrency: str, isRoot: str, isLeaf: str, isAbstract: str, specification: str, BehavioralFeature: "Core_Parameter" = None):
        self.concurrency = concurrency
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


    @property
    def concurrency(self):
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency


    @property
    def isRoot(self):
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot


    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


class Common_Behavior_Reception(BehavioralFeature):

    def __init__(self, specification: str, isRoot: str, isLeaf: str, isAbstract: str, Common_Behavior_Reception: "Signal" = None, BehavioralFeature: "Core_Parameter" = None):
        self.specification = specification
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.Common_Behavior_Reception = Common_Behavior_Reception
        
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
    def Common_Behavior_Reception(self):
        return self.__Common_Behavior_Reception

    @Common_Behavior_Reception.setter
    def Common_Behavior_Reception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Reception__Common_Behavior_Reception", None)
        self.__Common_Behavior_Reception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signal16"):
                opp_val = getattr(old_value, "Signal16", None)
                if opp_val == self:
                    setattr(old_value, "Signal16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signal16"):
                opp_val = getattr(value, "Signal16", None)
                setattr(value, "Signal16", self)

class Expression:

    pass
class Data_Types_ObjectSetExpression(Expression):

    pass
class Data_Types_BooleanExpression(Expression):

    pass
class Data_Types_ActionExpression(Expression):

    pass
class Data_Types_TimeExpression(Expression):

    pass
class Data_Types_IterationExpression(Expression):

    pass
class Common_Behavior_ActionSequence(Action):

    pass
class Signal:

    pass
class Common_Behavior_Exception(Signal):

    pass
class ObjectSetExpression:

    pass
class IterationExpression:

    pass
class ActionSequence:

    pass
class Argument:

    pass
class ModelElement:

    pass
class Core_Namespace(ModelElement):

    pass
class Core_Parameter(ModelElement):

    def __init__(self, kind: str, Core_Parameter: "Classifier" = None, parameter: "BehavioralFeature" = None, Core_Parameter82: "Expression" = None, ModelElement: "State_Machines_StateMachine" = None, ModelElement70: "Core_Namespace" = None):
        self.kind = kind
        self.Core_Parameter = Core_Parameter
        self.parameter = parameter
        self.Core_Parameter82 = Core_Parameter82
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Parameter__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioralFeature"):
                opp_val = getattr(old_value, "BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioralFeature"):
                opp_val = getattr(value, "BehavioralFeature", None)
                setattr(value, "BehavioralFeature", self)

    @property
    def Core_Parameter(self):
        return self.__Core_Parameter

    @Core_Parameter.setter
    def Core_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Parameter__Core_Parameter", None)
        self.__Core_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier79"):
                opp_val = getattr(old_value, "Classifier79", None)
                if opp_val == self:
                    setattr(old_value, "Classifier79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier79"):
                opp_val = getattr(value, "Classifier79", None)
                setattr(value, "Classifier79", self)

    @property
    def Core_Parameter82(self):
        return self.__Core_Parameter82

    @Core_Parameter82.setter
    def Core_Parameter82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Parameter__Core_Parameter82", None)
        self.__Core_Parameter82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression83"):
                opp_val = getattr(old_value, "Expression83", None)
                if opp_val == self:
                    setattr(old_value, "Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression83"):
                opp_val = getattr(value, "Expression83", None)
                setattr(value, "Expression83", self)

class Core_GeneralizableElement(ModelElement):

    def __init__(self, isRoot: str, isLeaf: str, isAbstract: str, child: set["Generalization_"] = None, ModelElement: "State_Machines_StateMachine" = None, ModelElement70: "Core_Namespace" = None):
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.child = child if child is not None else set()
        
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
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_GeneralizableElement__child", None)
        self.__child = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization_", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    setattr(item, "Generalization_", self)
                    

class Common_Behavior_Argument(ModelElement):

    pass
class Core_Relationship(ModelElement):

    pass
class Core_Feature(ModelElement):

    def __init__(self, ownerScope: str, feature: "Classifier" = None, ModelElement: "State_Machines_StateMachine" = None, ModelElement70: "Core_Namespace" = None):
        self.ownerScope = ownerScope
        self.feature = feature
        
        pass
    @property
    def ownerScope(self):
        return self.__ownerScope

    @ownerScope.setter
    def ownerScope(self, ownerScope: str):
        self.__ownerScope = ownerScope


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Feature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier75"):
                opp_val = getattr(old_value, "Classifier75", None)
                if opp_val == self:
                    setattr(old_value, "Classifier75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier75"):
                opp_val = getattr(value, "Classifier75", None)
                setattr(value, "Classifier75", self)

class State_Machines_Event(ModelElement):

    pass
class State_Machines_StateMachine(ModelElement):

    pass
class State_Machines_Transition(ModelElement):

    pass
class State_Machines_Guard(ModelElement):

    pass
class State_Machines_StateVertex(ModelElement):

    pass
class Common_Behavior_Action(ModelElement):

    def __init__(self, isAsynchronous: str, action: set["Argument"] = None, action2: "ActionSequence" = None, Common_Behavior_Action: "IterationExpression" = None, Common_Behavior_Action5: "ObjectSetExpression" = None, Common_Behavior_Action7: "ActionExpression" = None, ModelElement: "State_Machines_StateMachine" = None, ModelElement70: "Core_Namespace" = None):
        self.isAsynchronous = isAsynchronous
        self.action = action if action is not None else set()
        self.action2 = action2
        self.Common_Behavior_Action = Common_Behavior_Action
        self.Common_Behavior_Action5 = Common_Behavior_Action5
        self.Common_Behavior_Action7 = Common_Behavior_Action7
        
        pass
    @property
    def isAsynchronous(self):
        return self.__isAsynchronous

    @isAsynchronous.setter
    def isAsynchronous(self, isAsynchronous: str):
        self.__isAsynchronous = isAsynchronous


    @property
    def action2(self):
        return self.__action2

    @action2.setter
    def action2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Action__action2", None)
        self.__action2 = value
        
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

    @property
    def Common_Behavior_Action5(self):
        return self.__Common_Behavior_Action5

    @Common_Behavior_Action5.setter
    def Common_Behavior_Action5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Action__Common_Behavior_Action5", None)
        self.__Common_Behavior_Action5 = value
        
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
    def Common_Behavior_Action7(self):
        return self.__Common_Behavior_Action7

    @Common_Behavior_Action7.setter
    def Common_Behavior_Action7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Action__Common_Behavior_Action7", None)
        self.__Common_Behavior_Action7 = value
        
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
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Action__action", None)
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
    def Common_Behavior_Action(self):
        return self.__Common_Behavior_Action

    @Common_Behavior_Action.setter
    def Common_Behavior_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Common_Behavior_Action__Common_Behavior_Action", None)
        self.__Common_Behavior_Action = value
        
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

class Classifier:

    pass
class Common_Behavior_Signal(Classifier):

    pass