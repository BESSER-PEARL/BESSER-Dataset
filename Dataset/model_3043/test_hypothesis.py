import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ArgListsExpression,
    ActivityGraph,
    Partition,
    ActionState,
    behavioral_elements_activity_graphs_CallState,
    SimpleState,
    behavioral_elements_activity_graphs_ObjectFlowState,
    behavioral_elements_activity_graphs_ActionState,
    AssociationRole,
    BehavioralFeature,
    Reception,
    Link,
    Instance,
    behavioral_elements_common_behavior_Object,
    ComponentInstance,
    LinkEnd,
    AttributeLink,
    Classifier,
    behavioral_elements_activity_graphs_ClassifierInState,
    behavioral_elements_common_behavior_Signal,
    ObjectSetExpression,
    IterationExpression,
    SignalEvent,
    SendAction,
    ModelElement,
    behavioral_elements_collaborations_Interaction,
    behavioral_elements_collaborations_CollaborationInstanceSet,
    behavioral_elements_collaborations_InteractionInstanceSet,
    behavioral_elements_activity_graphs_Partition,
    behavioral_elements_common_behavior_Action,
    behavioral_elements_common_behavior_Link,
    behavioral_elements_common_behavior_Instance,
    behavioral_elements_collaborations_Message,
    Feature,
    ClassifierRole,
    Interaction,
    core_Namespace,
    core_GeneralizableElement,
    behavioral_elements_collaborations_Collaboration,
    Multiplicity_,
    behavioral_elements_collaborations_ClassifierRole,
    Collaboration,
    CollaborationInstanceSet,
    Guard,
    behavioral_elements_state_machines_Transition,
    behavioral_elements_state_machines_Guard,
    StateMachine,
    behavioral_elements_activity_graphs_ActivityGraph,
    StateVertex,
    behavioral_elements_state_machines_SynchState,
    behavioral_elements_state_machines_Pseudostate,
    behavioral_elements_state_machines_StubState,
    behavioral_elements_state_machines_State,
    CompositeState,
    behavioral_elements_state_machines_SubmachineState,
    behavioral_elements_state_machines_StateVertex,
    Parameter,
    behavioral_elements_state_machines_Event,
    SubmachineState,
    behavioral_elements_activity_graphs_SubactivityState,
    TimeExpression,
    Event,
    behavioral_elements_state_machines_SignalEvent,
    behavioral_elements_state_machines_CallEvent,
    behavioral_elements_state_machines_TimeEvent,
    behavioral_elements_state_machines_ChangeEvent,
    behavioral_elements_use_cases_ExtensionPoint,
    UseCase,
    BooleanExpression,
    Relationship,
    behavioral_elements_use_cases_Include,
    behavioral_elements_use_cases_Extend,
    behavioral_elements_use_cases_UseCaseInstance,
    behavioral_elements_use_cases_Actor,
    ExtensionPoint,
    State,
    behavioral_elements_state_machines_CompositeState,
    behavioral_elements_state_machines_FinalState,
    behavioral_elements_state_machines_SimpleState,
    behavioral_elements_state_machines_StateMachine,
    behavioral_elements_common_behavior_NodeInstance,
    NodeInstance,
    behavioral_elements_common_behavior_ComponentInstance,
    InteractionInstanceSet,
    Message,
    Include,
    Extend,
    behavioral_elements_use_cases_UseCase,
    behavioral_elements_common_behavior_SubsystemInstance,
    AssociationEnd,
    behavioral_elements_collaborations_AssociationEndRole,
    behavioral_elements_common_behavior_LinkEnd,
    behavioral_elements_common_behavior_Reception,
    Expression,
    behavioral_elements_common_behavior_Argument,
    behavioral_elements_common_behavior_Stimulus,
    Operation,
    behavioral_elements_common_behavior_DataValue,
    common_behavior_Link,
    common_behavior_Object,
    behavioral_elements_common_behavior_LinkObject,
    Signal,
    behavioral_elements_common_behavior_Exception,
    Attribute,
    behavioral_elements_common_behavior_AttributeLink,
    Action,
    behavioral_elements_common_behavior_SendAction,
    behavioral_elements_common_behavior_UninterpretedAction,
    behavioral_elements_common_behavior_ReturnAction,
    behavioral_elements_common_behavior_ActionSequence,
    behavioral_elements_common_behavior_DestroyAction,
    behavioral_elements_common_behavior_CallAction,
    behavioral_elements_common_behavior_TerminateAction,
    behavioral_elements_common_behavior_CreateAction,
    Transition,
    Stimulus,
    ActionSequence,
    Argument,
    ActionExpression,
    Association,
    behavioral_elements_collaborations_AssociationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arglistsexpression_is_not_abstract():
    assert not inspect.isabstract(ArgListsExpression)


def test_arglistsexpression_constructor_exists():
    assert callable(ArgListsExpression.__init__)


def test_arglistsexpression_constructor_args():
    sig = inspect.signature(ArgListsExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitygraph_is_not_abstract():
    assert not inspect.isabstract(ActivityGraph)


def test_activitygraph_constructor_exists():
    assert callable(ActivityGraph.__init__)


def test_activitygraph_constructor_args():
    sig = inspect.signature(ActivityGraph.__init__)
    params = list(sig.parameters.keys())



def test_partition_is_not_abstract():
    assert not inspect.isabstract(Partition)


def test_partition_constructor_exists():
    assert callable(Partition.__init__)


def test_partition_constructor_args():
    sig = inspect.signature(Partition.__init__)
    params = list(sig.parameters.keys())



def test_actionstate_is_not_abstract():
    assert not inspect.isabstract(ActionState)


def test_actionstate_constructor_exists():
    assert callable(ActionState.__init__)


def test_actionstate_constructor_args():
    sig = inspect.signature(ActionState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_callstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_CallState)


def test_behavioral_elements_activity_graphs_callstate_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_CallState.__init__)


def test_behavioral_elements_activity_graphs_callstate_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_CallState.__init__)
    params = list(sig.parameters.keys())



def test_simplestate_is_not_abstract():
    assert not inspect.isabstract(SimpleState)


def test_simplestate_constructor_exists():
    assert callable(SimpleState.__init__)


def test_simplestate_constructor_args():
    sig = inspect.signature(SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_objectflowstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_ObjectFlowState)


def test_behavioral_elements_activity_graphs_objectflowstate_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_ObjectFlowState.__init__)


def test_behavioral_elements_activity_graphs_objectflowstate_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_ObjectFlowState.__init__)
    params = list(sig.parameters.keys())
    assert "isSynch" in params, "Missing parameter 'isSynch'"

def test_behavioral_elements_activity_graphs_objectflowstate_has_isSynch():
    assert hasattr(behavioral_elements_activity_graphs_ObjectFlowState, "isSynch")
    descriptor = None
    for klass in behavioral_elements_activity_graphs_ObjectFlowState.__mro__:
        if "isSynch" in klass.__dict__:
            descriptor = klass.__dict__["isSynch"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_activity_graphs_actionstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_ActionState)


def test_behavioral_elements_activity_graphs_actionstate_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_ActionState.__init__)


def test_behavioral_elements_activity_graphs_actionstate_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_behavioral_elements_activity_graphs_actionstate_has_isDynamic():
    assert hasattr(behavioral_elements_activity_graphs_ActionState, "isDynamic")
    descriptor = None
    for klass in behavioral_elements_activity_graphs_ActionState.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_associationrole_is_not_abstract():
    assert not inspect.isabstract(AssociationRole)


def test_associationrole_constructor_exists():
    assert callable(AssociationRole.__init__)


def test_associationrole_constructor_args():
    sig = inspect.signature(AssociationRole.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_reception_is_not_abstract():
    assert not inspect.isabstract(Reception)


def test_reception_constructor_exists():
    assert callable(Reception.__init__)


def test_reception_constructor_args():
    sig = inspect.signature(Reception.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_object_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Object)


def test_behavioral_elements_common_behavior_object_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Object.__init__)


def test_behavioral_elements_common_behavior_object_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Object.__init__)
    params = list(sig.parameters.keys())



def test_componentinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentInstance)


def test_componentinstance_constructor_exists():
    assert callable(ComponentInstance.__init__)


def test_componentinstance_constructor_args():
    sig = inspect.signature(ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_linkend_is_not_abstract():
    assert not inspect.isabstract(LinkEnd)


def test_linkend_constructor_exists():
    assert callable(LinkEnd.__init__)


def test_linkend_constructor_args():
    sig = inspect.signature(LinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_attributelink_is_not_abstract():
    assert not inspect.isabstract(AttributeLink)


def test_attributelink_constructor_exists():
    assert callable(AttributeLink.__init__)


def test_attributelink_constructor_args():
    sig = inspect.signature(AttributeLink.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_classifierinstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_ClassifierInState)


def test_behavioral_elements_activity_graphs_classifierinstate_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_ClassifierInState.__init__)


def test_behavioral_elements_activity_graphs_classifierinstate_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_ClassifierInState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_signal_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Signal)


def test_behavioral_elements_common_behavior_signal_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Signal.__init__)


def test_behavioral_elements_common_behavior_signal_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Signal.__init__)
    params = list(sig.parameters.keys())



def test_objectsetexpression_is_not_abstract():
    assert not inspect.isabstract(ObjectSetExpression)


def test_objectsetexpression_constructor_exists():
    assert callable(ObjectSetExpression.__init__)


def test_objectsetexpression_constructor_args():
    sig = inspect.signature(ObjectSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_iterationexpression_is_not_abstract():
    assert not inspect.isabstract(IterationExpression)


def test_iterationexpression_constructor_exists():
    assert callable(IterationExpression.__init__)


def test_iterationexpression_constructor_args():
    sig = inspect.signature(IterationExpression.__init__)
    params = list(sig.parameters.keys())



def test_signalevent_is_not_abstract():
    assert not inspect.isabstract(SignalEvent)


def test_signalevent_constructor_exists():
    assert callable(SignalEvent.__init__)


def test_signalevent_constructor_args():
    sig = inspect.signature(SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_sendaction_is_not_abstract():
    assert not inspect.isabstract(SendAction)


def test_sendaction_constructor_exists():
    assert callable(SendAction.__init__)


def test_sendaction_constructor_args():
    sig = inspect.signature(SendAction.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_interaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_Interaction)


def test_behavioral_elements_collaborations_interaction_constructor_exists():
    assert callable(behavioral_elements_collaborations_Interaction.__init__)


def test_behavioral_elements_collaborations_interaction_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_collaborationinstanceset_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_CollaborationInstanceSet)


def test_behavioral_elements_collaborations_collaborationinstanceset_constructor_exists():
    assert callable(behavioral_elements_collaborations_CollaborationInstanceSet.__init__)


def test_behavioral_elements_collaborations_collaborationinstanceset_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_CollaborationInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_interactioninstanceset_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_InteractionInstanceSet)


def test_behavioral_elements_collaborations_interactioninstanceset_constructor_exists():
    assert callable(behavioral_elements_collaborations_InteractionInstanceSet.__init__)


def test_behavioral_elements_collaborations_interactioninstanceset_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_InteractionInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_partition_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_Partition)


def test_behavioral_elements_activity_graphs_partition_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_Partition.__init__)


def test_behavioral_elements_activity_graphs_partition_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_Partition.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_action_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Action)


def test_behavioral_elements_common_behavior_action_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Action.__init__)


def test_behavioral_elements_common_behavior_action_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Action.__init__)
    params = list(sig.parameters.keys())
    assert "isAsynchronous" in params, "Missing parameter 'isAsynchronous'"

def test_behavioral_elements_common_behavior_action_has_isAsynchronous():
    assert hasattr(behavioral_elements_common_behavior_Action, "isAsynchronous")
    descriptor = None
    for klass in behavioral_elements_common_behavior_Action.__mro__:
        if "isAsynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isAsynchronous"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_common_behavior_link_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Link)


def test_behavioral_elements_common_behavior_link_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Link.__init__)


def test_behavioral_elements_common_behavior_link_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Link.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_instance_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Instance)


def test_behavioral_elements_common_behavior_instance_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Instance.__init__)


def test_behavioral_elements_common_behavior_instance_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Instance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_message_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_Message)


def test_behavioral_elements_collaborations_message_constructor_exists():
    assert callable(behavioral_elements_collaborations_Message.__init__)


def test_behavioral_elements_collaborations_message_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_Message.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_classifierrole_is_not_abstract():
    assert not inspect.isabstract(ClassifierRole)


def test_classifierrole_constructor_exists():
    assert callable(ClassifierRole.__init__)


def test_classifierrole_constructor_args():
    sig = inspect.signature(ClassifierRole.__init__)
    params = list(sig.parameters.keys())



def test_interaction_is_not_abstract():
    assert not inspect.isabstract(Interaction)


def test_interaction_constructor_exists():
    assert callable(Interaction.__init__)


def test_interaction_constructor_args():
    sig = inspect.signature(Interaction.__init__)
    params = list(sig.parameters.keys())



def test_core_namespace_is_not_abstract():
    assert not inspect.isabstract(core_Namespace)


def test_core_namespace_constructor_exists():
    assert callable(core_Namespace.__init__)


def test_core_namespace_constructor_args():
    sig = inspect.signature(core_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_core_generalizableelement_is_not_abstract():
    assert not inspect.isabstract(core_GeneralizableElement)


def test_core_generalizableelement_constructor_exists():
    assert callable(core_GeneralizableElement.__init__)


def test_core_generalizableelement_constructor_args():
    sig = inspect.signature(core_GeneralizableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_collaboration_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_Collaboration)


def test_behavioral_elements_collaborations_collaboration_constructor_exists():
    assert callable(behavioral_elements_collaborations_Collaboration.__init__)


def test_behavioral_elements_collaborations_collaboration_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_multiplicity__is_not_abstract():
    assert not inspect.isabstract(Multiplicity_)


def test_multiplicity__constructor_exists():
    assert callable(Multiplicity_.__init__)


def test_multiplicity__constructor_args():
    sig = inspect.signature(Multiplicity_.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_classifierrole_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_ClassifierRole)


def test_behavioral_elements_collaborations_classifierrole_constructor_exists():
    assert callable(behavioral_elements_collaborations_ClassifierRole.__init__)


def test_behavioral_elements_collaborations_classifierrole_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_ClassifierRole.__init__)
    params = list(sig.parameters.keys())



def test_collaboration_is_not_abstract():
    assert not inspect.isabstract(Collaboration)


def test_collaboration_constructor_exists():
    assert callable(Collaboration.__init__)


def test_collaboration_constructor_args():
    sig = inspect.signature(Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_collaborationinstanceset_is_not_abstract():
    assert not inspect.isabstract(CollaborationInstanceSet)


def test_collaborationinstanceset_constructor_exists():
    assert callable(CollaborationInstanceSet.__init__)


def test_collaborationinstanceset_constructor_args():
    sig = inspect.signature(CollaborationInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_transition_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_Transition)


def test_behavioral_elements_state_machines_transition_constructor_exists():
    assert callable(behavioral_elements_state_machines_Transition.__init__)


def test_behavioral_elements_state_machines_transition_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_Transition.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_guard_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_Guard)


def test_behavioral_elements_state_machines_guard_constructor_exists():
    assert callable(behavioral_elements_state_machines_Guard.__init__)


def test_behavioral_elements_state_machines_guard_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_activitygraph_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_ActivityGraph)


def test_behavioral_elements_activity_graphs_activitygraph_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_ActivityGraph.__init__)


def test_behavioral_elements_activity_graphs_activitygraph_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_ActivityGraph.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_synchstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_SynchState)


def test_behavioral_elements_state_machines_synchstate_constructor_exists():
    assert callable(behavioral_elements_state_machines_SynchState.__init__)


def test_behavioral_elements_state_machines_synchstate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_SynchState.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_behavioral_elements_state_machines_synchstate_has_bound():
    assert hasattr(behavioral_elements_state_machines_SynchState, "bound")
    descriptor = None
    for klass in behavioral_elements_state_machines_SynchState.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_state_machines_pseudostate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_Pseudostate)


def test_behavioral_elements_state_machines_pseudostate_constructor_exists():
    assert callable(behavioral_elements_state_machines_Pseudostate.__init__)


def test_behavioral_elements_state_machines_pseudostate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_behavioral_elements_state_machines_pseudostate_has_kind():
    assert hasattr(behavioral_elements_state_machines_Pseudostate, "kind")
    descriptor = None
    for klass in behavioral_elements_state_machines_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_state_machines_stubstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_StubState)


def test_behavioral_elements_state_machines_stubstate_constructor_exists():
    assert callable(behavioral_elements_state_machines_StubState.__init__)


def test_behavioral_elements_state_machines_stubstate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_StubState.__init__)
    params = list(sig.parameters.keys())
    assert "referenceState" in params, "Missing parameter 'referenceState'"

def test_behavioral_elements_state_machines_stubstate_has_referenceState():
    assert hasattr(behavioral_elements_state_machines_StubState, "referenceState")
    descriptor = None
    for klass in behavioral_elements_state_machines_StubState.__mro__:
        if "referenceState" in klass.__dict__:
            descriptor = klass.__dict__["referenceState"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_state_machines_state_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_State)


def test_behavioral_elements_state_machines_state_constructor_exists():
    assert callable(behavioral_elements_state_machines_State.__init__)


def test_behavioral_elements_state_machines_state_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_State.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_submachinestate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_SubmachineState)


def test_behavioral_elements_state_machines_submachinestate_constructor_exists():
    assert callable(behavioral_elements_state_machines_SubmachineState.__init__)


def test_behavioral_elements_state_machines_submachinestate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_SubmachineState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_statevertex_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_StateVertex)


def test_behavioral_elements_state_machines_statevertex_constructor_exists():
    assert callable(behavioral_elements_state_machines_StateVertex.__init__)


def test_behavioral_elements_state_machines_statevertex_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_event_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_Event)


def test_behavioral_elements_state_machines_event_constructor_exists():
    assert callable(behavioral_elements_state_machines_Event.__init__)


def test_behavioral_elements_state_machines_event_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_Event.__init__)
    params = list(sig.parameters.keys())



def test_submachinestate_is_not_abstract():
    assert not inspect.isabstract(SubmachineState)


def test_submachinestate_constructor_exists():
    assert callable(SubmachineState.__init__)


def test_submachinestate_constructor_args():
    sig = inspect.signature(SubmachineState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_activity_graphs_subactivitystate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_activity_graphs_SubactivityState)


def test_behavioral_elements_activity_graphs_subactivitystate_constructor_exists():
    assert callable(behavioral_elements_activity_graphs_SubactivityState.__init__)


def test_behavioral_elements_activity_graphs_subactivitystate_constructor_args():
    sig = inspect.signature(behavioral_elements_activity_graphs_SubactivityState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_behavioral_elements_activity_graphs_subactivitystate_has_isDynamic():
    assert hasattr(behavioral_elements_activity_graphs_SubactivityState, "isDynamic")
    descriptor = None
    for klass in behavioral_elements_activity_graphs_SubactivityState.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_timeexpression_is_not_abstract():
    assert not inspect.isabstract(TimeExpression)


def test_timeexpression_constructor_exists():
    assert callable(TimeExpression.__init__)


def test_timeexpression_constructor_args():
    sig = inspect.signature(TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_signalevent_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_SignalEvent)


def test_behavioral_elements_state_machines_signalevent_constructor_exists():
    assert callable(behavioral_elements_state_machines_SignalEvent.__init__)


def test_behavioral_elements_state_machines_signalevent_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_callevent_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_CallEvent)


def test_behavioral_elements_state_machines_callevent_constructor_exists():
    assert callable(behavioral_elements_state_machines_CallEvent.__init__)


def test_behavioral_elements_state_machines_callevent_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_timeevent_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_TimeEvent)


def test_behavioral_elements_state_machines_timeevent_constructor_exists():
    assert callable(behavioral_elements_state_machines_TimeEvent.__init__)


def test_behavioral_elements_state_machines_timeevent_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_changeevent_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_ChangeEvent)


def test_behavioral_elements_state_machines_changeevent_constructor_exists():
    assert callable(behavioral_elements_state_machines_ChangeEvent.__init__)


def test_behavioral_elements_state_machines_changeevent_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_ExtensionPoint)


def test_behavioral_elements_use_cases_extensionpoint_constructor_exists():
    assert callable(behavioral_elements_use_cases_ExtensionPoint.__init__)


def test_behavioral_elements_use_cases_extensionpoint_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_behavioral_elements_use_cases_extensionpoint_has_location():
    assert hasattr(behavioral_elements_use_cases_ExtensionPoint, "location")
    descriptor = None
    for klass in behavioral_elements_use_cases_ExtensionPoint.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase)


def test_usecase_constructor_exists():
    assert callable(UseCase.__init__)


def test_usecase_constructor_args():
    sig = inspect.signature(UseCase.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_include_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_Include)


def test_behavioral_elements_use_cases_include_constructor_exists():
    assert callable(behavioral_elements_use_cases_Include.__init__)


def test_behavioral_elements_use_cases_include_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_Include.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_extend_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_Extend)


def test_behavioral_elements_use_cases_extend_constructor_exists():
    assert callable(behavioral_elements_use_cases_Extend.__init__)


def test_behavioral_elements_use_cases_extend_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_Extend.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_usecaseinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_UseCaseInstance)


def test_behavioral_elements_use_cases_usecaseinstance_constructor_exists():
    assert callable(behavioral_elements_use_cases_UseCaseInstance.__init__)


def test_behavioral_elements_use_cases_usecaseinstance_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_UseCaseInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_actor_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_Actor)


def test_behavioral_elements_use_cases_actor_constructor_exists():
    assert callable(behavioral_elements_use_cases_Actor.__init__)


def test_behavioral_elements_use_cases_actor_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_Actor.__init__)
    params = list(sig.parameters.keys())



def test_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(ExtensionPoint)


def test_extensionpoint_constructor_exists():
    assert callable(ExtensionPoint.__init__)


def test_extensionpoint_constructor_args():
    sig = inspect.signature(ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_compositestate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_CompositeState)


def test_behavioral_elements_state_machines_compositestate_constructor_exists():
    assert callable(behavioral_elements_state_machines_CompositeState.__init__)


def test_behavioral_elements_state_machines_compositestate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_behavioral_elements_state_machines_compositestate_has_isConcurrent():
    assert hasattr(behavioral_elements_state_machines_CompositeState, "isConcurrent")
    descriptor = None
    for klass in behavioral_elements_state_machines_CompositeState.__mro__:
        if "isConcurrent" in klass.__dict__:
            descriptor = klass.__dict__["isConcurrent"]
            break
    assert isinstance(descriptor, property)



def test_behavioral_elements_state_machines_finalstate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_FinalState)


def test_behavioral_elements_state_machines_finalstate_constructor_exists():
    assert callable(behavioral_elements_state_machines_FinalState.__init__)


def test_behavioral_elements_state_machines_finalstate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_simplestate_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_SimpleState)


def test_behavioral_elements_state_machines_simplestate_constructor_exists():
    assert callable(behavioral_elements_state_machines_SimpleState.__init__)


def test_behavioral_elements_state_machines_simplestate_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_state_machines_statemachine_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_state_machines_StateMachine)


def test_behavioral_elements_state_machines_statemachine_constructor_exists():
    assert callable(behavioral_elements_state_machines_StateMachine.__init__)


def test_behavioral_elements_state_machines_statemachine_constructor_args():
    sig = inspect.signature(behavioral_elements_state_machines_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_NodeInstance)


def test_behavioral_elements_common_behavior_nodeinstance_constructor_exists():
    assert callable(behavioral_elements_common_behavior_NodeInstance.__init__)


def test_behavioral_elements_common_behavior_nodeinstance_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(NodeInstance)


def test_nodeinstance_constructor_exists():
    assert callable(NodeInstance.__init__)


def test_nodeinstance_constructor_args():
    sig = inspect.signature(NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_componentinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_ComponentInstance)


def test_behavioral_elements_common_behavior_componentinstance_constructor_exists():
    assert callable(behavioral_elements_common_behavior_ComponentInstance.__init__)


def test_behavioral_elements_common_behavior_componentinstance_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_interactioninstanceset_is_not_abstract():
    assert not inspect.isabstract(InteractionInstanceSet)


def test_interactioninstanceset_constructor_exists():
    assert callable(InteractionInstanceSet.__init__)


def test_interactioninstanceset_constructor_args():
    sig = inspect.signature(InteractionInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_include_is_not_abstract():
    assert not inspect.isabstract(Include)


def test_include_constructor_exists():
    assert callable(Include.__init__)


def test_include_constructor_args():
    sig = inspect.signature(Include.__init__)
    params = list(sig.parameters.keys())



def test_extend_is_not_abstract():
    assert not inspect.isabstract(Extend)


def test_extend_constructor_exists():
    assert callable(Extend.__init__)


def test_extend_constructor_args():
    sig = inspect.signature(Extend.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_use_cases_usecase_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_use_cases_UseCase)


def test_behavioral_elements_use_cases_usecase_constructor_exists():
    assert callable(behavioral_elements_use_cases_UseCase.__init__)


def test_behavioral_elements_use_cases_usecase_constructor_args():
    sig = inspect.signature(behavioral_elements_use_cases_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_subsysteminstance_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_SubsystemInstance)


def test_behavioral_elements_common_behavior_subsysteminstance_constructor_exists():
    assert callable(behavioral_elements_common_behavior_SubsystemInstance.__init__)


def test_behavioral_elements_common_behavior_subsysteminstance_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_SubsystemInstance.__init__)
    params = list(sig.parameters.keys())



def test_associationend_is_not_abstract():
    assert not inspect.isabstract(AssociationEnd)


def test_associationend_constructor_exists():
    assert callable(AssociationEnd.__init__)


def test_associationend_constructor_args():
    sig = inspect.signature(AssociationEnd.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_associationendrole_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_AssociationEndRole)


def test_behavioral_elements_collaborations_associationendrole_constructor_exists():
    assert callable(behavioral_elements_collaborations_AssociationEndRole.__init__)


def test_behavioral_elements_collaborations_associationendrole_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_AssociationEndRole.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_linkend_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_LinkEnd)


def test_behavioral_elements_common_behavior_linkend_constructor_exists():
    assert callable(behavioral_elements_common_behavior_LinkEnd.__init__)


def test_behavioral_elements_common_behavior_linkend_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_LinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_reception_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Reception)


def test_behavioral_elements_common_behavior_reception_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Reception.__init__)


def test_behavioral_elements_common_behavior_reception_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Reception.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"
    assert "isRoot" in params, "Missing parameter 'isRoot'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_behavioral_elements_common_behavior_reception_has_specification():
    assert hasattr(behavioral_elements_common_behavior_Reception, "specification")
    descriptor = None
    for klass in behavioral_elements_common_behavior_Reception.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_behavioral_elements_common_behavior_reception_has_isRoot():
    assert hasattr(behavioral_elements_common_behavior_Reception, "isRoot")
    descriptor = None
    for klass in behavioral_elements_common_behavior_Reception.__mro__:
        if "isRoot" in klass.__dict__:
            descriptor = klass.__dict__["isRoot"]
            break
    assert isinstance(descriptor, property)

def test_behavioral_elements_common_behavior_reception_has_isAbstract():
    assert hasattr(behavioral_elements_common_behavior_Reception, "isAbstract")
    descriptor = None
    for klass in behavioral_elements_common_behavior_Reception.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_behavioral_elements_common_behavior_reception_has_isLeaf():
    assert hasattr(behavioral_elements_common_behavior_Reception, "isLeaf")
    descriptor = None
    for klass in behavioral_elements_common_behavior_Reception.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_argument_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Argument)


def test_behavioral_elements_common_behavior_argument_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Argument.__init__)


def test_behavioral_elements_common_behavior_argument_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Argument.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_stimulus_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Stimulus)


def test_behavioral_elements_common_behavior_stimulus_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Stimulus.__init__)


def test_behavioral_elements_common_behavior_stimulus_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Stimulus.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_datavalue_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_DataValue)


def test_behavioral_elements_common_behavior_datavalue_constructor_exists():
    assert callable(behavioral_elements_common_behavior_DataValue.__init__)


def test_behavioral_elements_common_behavior_datavalue_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_DataValue.__init__)
    params = list(sig.parameters.keys())



def test_common_behavior_link_is_not_abstract():
    assert not inspect.isabstract(common_behavior_Link)


def test_common_behavior_link_constructor_exists():
    assert callable(common_behavior_Link.__init__)


def test_common_behavior_link_constructor_args():
    sig = inspect.signature(common_behavior_Link.__init__)
    params = list(sig.parameters.keys())



def test_common_behavior_object_is_not_abstract():
    assert not inspect.isabstract(common_behavior_Object)


def test_common_behavior_object_constructor_exists():
    assert callable(common_behavior_Object.__init__)


def test_common_behavior_object_constructor_args():
    sig = inspect.signature(common_behavior_Object.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_linkobject_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_LinkObject)


def test_behavioral_elements_common_behavior_linkobject_constructor_exists():
    assert callable(behavioral_elements_common_behavior_LinkObject.__init__)


def test_behavioral_elements_common_behavior_linkobject_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_LinkObject.__init__)
    params = list(sig.parameters.keys())



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_exception_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_Exception)


def test_behavioral_elements_common_behavior_exception_constructor_exists():
    assert callable(behavioral_elements_common_behavior_Exception.__init__)


def test_behavioral_elements_common_behavior_exception_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_Exception.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_attributelink_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_AttributeLink)


def test_behavioral_elements_common_behavior_attributelink_constructor_exists():
    assert callable(behavioral_elements_common_behavior_AttributeLink.__init__)


def test_behavioral_elements_common_behavior_attributelink_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_AttributeLink.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_sendaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_SendAction)


def test_behavioral_elements_common_behavior_sendaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_SendAction.__init__)


def test_behavioral_elements_common_behavior_sendaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_SendAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_uninterpretedaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_UninterpretedAction)


def test_behavioral_elements_common_behavior_uninterpretedaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_UninterpretedAction.__init__)


def test_behavioral_elements_common_behavior_uninterpretedaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_UninterpretedAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_returnaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_ReturnAction)


def test_behavioral_elements_common_behavior_returnaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_ReturnAction.__init__)


def test_behavioral_elements_common_behavior_returnaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_actionsequence_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_ActionSequence)


def test_behavioral_elements_common_behavior_actionsequence_constructor_exists():
    assert callable(behavioral_elements_common_behavior_ActionSequence.__init__)


def test_behavioral_elements_common_behavior_actionsequence_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_ActionSequence.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_destroyaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_DestroyAction)


def test_behavioral_elements_common_behavior_destroyaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_DestroyAction.__init__)


def test_behavioral_elements_common_behavior_destroyaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_DestroyAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_callaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_CallAction)


def test_behavioral_elements_common_behavior_callaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_CallAction.__init__)


def test_behavioral_elements_common_behavior_callaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_CallAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_terminateaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_TerminateAction)


def test_behavioral_elements_common_behavior_terminateaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_TerminateAction.__init__)


def test_behavioral_elements_common_behavior_terminateaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_TerminateAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_common_behavior_createaction_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_common_behavior_CreateAction)


def test_behavioral_elements_common_behavior_createaction_constructor_exists():
    assert callable(behavioral_elements_common_behavior_CreateAction.__init__)


def test_behavioral_elements_common_behavior_createaction_constructor_args():
    sig = inspect.signature(behavioral_elements_common_behavior_CreateAction.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_stimulus_is_not_abstract():
    assert not inspect.isabstract(Stimulus)


def test_stimulus_constructor_exists():
    assert callable(Stimulus.__init__)


def test_stimulus_constructor_args():
    sig = inspect.signature(Stimulus.__init__)
    params = list(sig.parameters.keys())



def test_actionsequence_is_not_abstract():
    assert not inspect.isabstract(ActionSequence)


def test_actionsequence_constructor_exists():
    assert callable(ActionSequence.__init__)


def test_actionsequence_constructor_args():
    sig = inspect.signature(ActionSequence.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_actionexpression_is_not_abstract():
    assert not inspect.isabstract(ActionExpression)


def test_actionexpression_constructor_exists():
    assert callable(ActionExpression.__init__)


def test_actionexpression_constructor_args():
    sig = inspect.signature(ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_behavioral_elements_collaborations_associationrole_is_not_abstract():
    assert not inspect.isabstract(behavioral_elements_collaborations_AssociationRole)


def test_behavioral_elements_collaborations_associationrole_constructor_exists():
    assert callable(behavioral_elements_collaborations_AssociationRole.__init__)


def test_behavioral_elements_collaborations_associationrole_constructor_args():
    sig = inspect.signature(behavioral_elements_collaborations_AssociationRole.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ArgListsExpression_strategy = st.builds(
    ArgListsExpression,
)
ActivityGraph_strategy = st.builds(
    ActivityGraph,
)
Partition_strategy = st.builds(
    Partition,
)
ActionState_strategy = st.builds(
    ActionState,
)
behavioral_elements_activity_graphs_CallState_strategy = st.builds(
    behavioral_elements_activity_graphs_CallState,
)
SimpleState_strategy = st.builds(
    SimpleState,
)
behavioral_elements_activity_graphs_ObjectFlowState_strategy = st.builds(
    behavioral_elements_activity_graphs_ObjectFlowState,
    isSynch=
        safe_text
)
behavioral_elements_activity_graphs_ActionState_strategy = st.builds(
    behavioral_elements_activity_graphs_ActionState,
    isDynamic=
        safe_text
)
AssociationRole_strategy = st.builds(
    AssociationRole,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
Reception_strategy = st.builds(
    Reception,
)
Link_strategy = st.builds(
    Link,
)
Instance_strategy = st.builds(
    Instance,
)
behavioral_elements_common_behavior_Object_strategy = st.builds(
    behavioral_elements_common_behavior_Object,
)
ComponentInstance_strategy = st.builds(
    ComponentInstance,
)
LinkEnd_strategy = st.builds(
    LinkEnd,
)
AttributeLink_strategy = st.builds(
    AttributeLink,
)
Classifier_strategy = st.builds(
    Classifier,
)
behavioral_elements_activity_graphs_ClassifierInState_strategy = st.builds(
    behavioral_elements_activity_graphs_ClassifierInState,
)
behavioral_elements_common_behavior_Signal_strategy = st.builds(
    behavioral_elements_common_behavior_Signal,
)
ObjectSetExpression_strategy = st.builds(
    ObjectSetExpression,
)
IterationExpression_strategy = st.builds(
    IterationExpression,
)
SignalEvent_strategy = st.builds(
    SignalEvent,
)
SendAction_strategy = st.builds(
    SendAction,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
behavioral_elements_collaborations_Interaction_strategy = st.builds(
    behavioral_elements_collaborations_Interaction,
)
behavioral_elements_collaborations_CollaborationInstanceSet_strategy = st.builds(
    behavioral_elements_collaborations_CollaborationInstanceSet,
)
behavioral_elements_collaborations_InteractionInstanceSet_strategy = st.builds(
    behavioral_elements_collaborations_InteractionInstanceSet,
)
behavioral_elements_activity_graphs_Partition_strategy = st.builds(
    behavioral_elements_activity_graphs_Partition,
)
behavioral_elements_common_behavior_Action_strategy = st.builds(
    behavioral_elements_common_behavior_Action,
    isAsynchronous=
        safe_text
)
behavioral_elements_common_behavior_Link_strategy = st.builds(
    behavioral_elements_common_behavior_Link,
)
behavioral_elements_common_behavior_Instance_strategy = st.builds(
    behavioral_elements_common_behavior_Instance,
)
behavioral_elements_collaborations_Message_strategy = st.builds(
    behavioral_elements_collaborations_Message,
)
Feature_strategy = st.builds(
    Feature,
)
ClassifierRole_strategy = st.builds(
    ClassifierRole,
)
Interaction_strategy = st.builds(
    Interaction,
)
core_Namespace_strategy = st.builds(
    core_Namespace,
)
core_GeneralizableElement_strategy = st.builds(
    core_GeneralizableElement,
)
behavioral_elements_collaborations_Collaboration_strategy = st.builds(
    behavioral_elements_collaborations_Collaboration,
)
Multiplicity__strategy = st.builds(
    Multiplicity_,
)
behavioral_elements_collaborations_ClassifierRole_strategy = st.builds(
    behavioral_elements_collaborations_ClassifierRole,
)
Collaboration_strategy = st.builds(
    Collaboration,
)
CollaborationInstanceSet_strategy = st.builds(
    CollaborationInstanceSet,
)
Guard_strategy = st.builds(
    Guard,
)
behavioral_elements_state_machines_Transition_strategy = st.builds(
    behavioral_elements_state_machines_Transition,
)
behavioral_elements_state_machines_Guard_strategy = st.builds(
    behavioral_elements_state_machines_Guard,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
behavioral_elements_activity_graphs_ActivityGraph_strategy = st.builds(
    behavioral_elements_activity_graphs_ActivityGraph,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
behavioral_elements_state_machines_SynchState_strategy = st.builds(
    behavioral_elements_state_machines_SynchState,
    bound=
        safe_text
)
behavioral_elements_state_machines_Pseudostate_strategy = st.builds(
    behavioral_elements_state_machines_Pseudostate,
    kind=
        safe_text
)
behavioral_elements_state_machines_StubState_strategy = st.builds(
    behavioral_elements_state_machines_StubState,
    referenceState=
        safe_text
)
behavioral_elements_state_machines_State_strategy = st.builds(
    behavioral_elements_state_machines_State,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
behavioral_elements_state_machines_SubmachineState_strategy = st.builds(
    behavioral_elements_state_machines_SubmachineState,
)
behavioral_elements_state_machines_StateVertex_strategy = st.builds(
    behavioral_elements_state_machines_StateVertex,
)
Parameter_strategy = st.builds(
    Parameter,
)
behavioral_elements_state_machines_Event_strategy = st.builds(
    behavioral_elements_state_machines_Event,
)
SubmachineState_strategy = st.builds(
    SubmachineState,
)
behavioral_elements_activity_graphs_SubactivityState_strategy = st.builds(
    behavioral_elements_activity_graphs_SubactivityState,
    isDynamic=
        safe_text
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
Event_strategy = st.builds(
    Event,
)
behavioral_elements_state_machines_SignalEvent_strategy = st.builds(
    behavioral_elements_state_machines_SignalEvent,
)
behavioral_elements_state_machines_CallEvent_strategy = st.builds(
    behavioral_elements_state_machines_CallEvent,
)
behavioral_elements_state_machines_TimeEvent_strategy = st.builds(
    behavioral_elements_state_machines_TimeEvent,
)
behavioral_elements_state_machines_ChangeEvent_strategy = st.builds(
    behavioral_elements_state_machines_ChangeEvent,
)
behavioral_elements_use_cases_ExtensionPoint_strategy = st.builds(
    behavioral_elements_use_cases_ExtensionPoint,
    location=
        safe_text
)
UseCase_strategy = st.builds(
    UseCase,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
Relationship_strategy = st.builds(
    Relationship,
)
behavioral_elements_use_cases_Include_strategy = st.builds(
    behavioral_elements_use_cases_Include,
)
behavioral_elements_use_cases_Extend_strategy = st.builds(
    behavioral_elements_use_cases_Extend,
)
behavioral_elements_use_cases_UseCaseInstance_strategy = st.builds(
    behavioral_elements_use_cases_UseCaseInstance,
)
behavioral_elements_use_cases_Actor_strategy = st.builds(
    behavioral_elements_use_cases_Actor,
)
ExtensionPoint_strategy = st.builds(
    ExtensionPoint,
)
State_strategy = st.builds(
    State,
)
behavioral_elements_state_machines_CompositeState_strategy = st.builds(
    behavioral_elements_state_machines_CompositeState,
    isConcurrent=
        safe_text
)
behavioral_elements_state_machines_FinalState_strategy = st.builds(
    behavioral_elements_state_machines_FinalState,
)
behavioral_elements_state_machines_SimpleState_strategy = st.builds(
    behavioral_elements_state_machines_SimpleState,
)
behavioral_elements_state_machines_StateMachine_strategy = st.builds(
    behavioral_elements_state_machines_StateMachine,
)
behavioral_elements_common_behavior_NodeInstance_strategy = st.builds(
    behavioral_elements_common_behavior_NodeInstance,
)
NodeInstance_strategy = st.builds(
    NodeInstance,
)
behavioral_elements_common_behavior_ComponentInstance_strategy = st.builds(
    behavioral_elements_common_behavior_ComponentInstance,
)
InteractionInstanceSet_strategy = st.builds(
    InteractionInstanceSet,
)
Message_strategy = st.builds(
    Message,
)
Include_strategy = st.builds(
    Include,
)
Extend_strategy = st.builds(
    Extend,
)
behavioral_elements_use_cases_UseCase_strategy = st.builds(
    behavioral_elements_use_cases_UseCase,
)
behavioral_elements_common_behavior_SubsystemInstance_strategy = st.builds(
    behavioral_elements_common_behavior_SubsystemInstance,
)
AssociationEnd_strategy = st.builds(
    AssociationEnd,
)
behavioral_elements_collaborations_AssociationEndRole_strategy = st.builds(
    behavioral_elements_collaborations_AssociationEndRole,
)
behavioral_elements_common_behavior_LinkEnd_strategy = st.builds(
    behavioral_elements_common_behavior_LinkEnd,
)
behavioral_elements_common_behavior_Reception_strategy = st.builds(
    behavioral_elements_common_behavior_Reception,
    specification=
        safe_text,
    isRoot=
        safe_text,
    isAbstract=
        safe_text,
    isLeaf=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
behavioral_elements_common_behavior_Argument_strategy = st.builds(
    behavioral_elements_common_behavior_Argument,
)
behavioral_elements_common_behavior_Stimulus_strategy = st.builds(
    behavioral_elements_common_behavior_Stimulus,
)
Operation_strategy = st.builds(
    Operation,
)
behavioral_elements_common_behavior_DataValue_strategy = st.builds(
    behavioral_elements_common_behavior_DataValue,
)
common_behavior_Link_strategy = st.builds(
    common_behavior_Link,
)
common_behavior_Object_strategy = st.builds(
    common_behavior_Object,
)
behavioral_elements_common_behavior_LinkObject_strategy = st.builds(
    behavioral_elements_common_behavior_LinkObject,
)
Signal_strategy = st.builds(
    Signal,
)
behavioral_elements_common_behavior_Exception_strategy = st.builds(
    behavioral_elements_common_behavior_Exception,
)
Attribute_strategy = st.builds(
    Attribute,
)
behavioral_elements_common_behavior_AttributeLink_strategy = st.builds(
    behavioral_elements_common_behavior_AttributeLink,
)
Action_strategy = st.builds(
    Action,
)
behavioral_elements_common_behavior_SendAction_strategy = st.builds(
    behavioral_elements_common_behavior_SendAction,
)
behavioral_elements_common_behavior_UninterpretedAction_strategy = st.builds(
    behavioral_elements_common_behavior_UninterpretedAction,
)
behavioral_elements_common_behavior_ReturnAction_strategy = st.builds(
    behavioral_elements_common_behavior_ReturnAction,
)
behavioral_elements_common_behavior_ActionSequence_strategy = st.builds(
    behavioral_elements_common_behavior_ActionSequence,
)
behavioral_elements_common_behavior_DestroyAction_strategy = st.builds(
    behavioral_elements_common_behavior_DestroyAction,
)
behavioral_elements_common_behavior_CallAction_strategy = st.builds(
    behavioral_elements_common_behavior_CallAction,
)
behavioral_elements_common_behavior_TerminateAction_strategy = st.builds(
    behavioral_elements_common_behavior_TerminateAction,
)
behavioral_elements_common_behavior_CreateAction_strategy = st.builds(
    behavioral_elements_common_behavior_CreateAction,
)
Transition_strategy = st.builds(
    Transition,
)
Stimulus_strategy = st.builds(
    Stimulus,
)
ActionSequence_strategy = st.builds(
    ActionSequence,
)
Argument_strategy = st.builds(
    Argument,
)
ActionExpression_strategy = st.builds(
    ActionExpression,
)
Association_strategy = st.builds(
    Association,
)
behavioral_elements_collaborations_AssociationRole_strategy = st.builds(
    behavioral_elements_collaborations_AssociationRole,
)

@given(instance=ArgListsExpression_strategy)
@settings(max_examples=50)
def test_arglistsexpression_instantiation(instance):
    assert isinstance(instance, ArgListsExpression)

@given(instance=ActivityGraph_strategy)
@settings(max_examples=50)
def test_activitygraph_instantiation(instance):
    assert isinstance(instance, ActivityGraph)

@given(instance=Partition_strategy)
@settings(max_examples=50)
def test_partition_instantiation(instance):
    assert isinstance(instance, Partition)

@given(instance=ActionState_strategy)
@settings(max_examples=50)
def test_actionstate_instantiation(instance):
    assert isinstance(instance, ActionState)

@given(instance=behavioral_elements_activity_graphs_CallState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_callstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_CallState)

@given(instance=SimpleState_strategy)
@settings(max_examples=50)
def test_simplestate_instantiation(instance):
    assert isinstance(instance, SimpleState)

@given(instance=behavioral_elements_activity_graphs_ObjectFlowState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_objectflowstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_ObjectFlowState)



@given(instance=behavioral_elements_activity_graphs_ObjectFlowState_strategy)
def test_behavioral_elements_activity_graphs_objectflowstate_isSynch_setter(instance):
    original = instance.isSynch
    instance.isSynch = original
    assert instance.isSynch == original

@given(instance=behavioral_elements_activity_graphs_ActionState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_actionstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_ActionState)



@given(instance=behavioral_elements_activity_graphs_ActionState_strategy)
def test_behavioral_elements_activity_graphs_actionstate_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=AssociationRole_strategy)
@settings(max_examples=50)
def test_associationrole_instantiation(instance):
    assert isinstance(instance, AssociationRole)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=Reception_strategy)
@settings(max_examples=50)
def test_reception_instantiation(instance):
    assert isinstance(instance, Reception)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=behavioral_elements_common_behavior_Object_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_object_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Object)

@given(instance=ComponentInstance_strategy)
@settings(max_examples=50)
def test_componentinstance_instantiation(instance):
    assert isinstance(instance, ComponentInstance)

@given(instance=LinkEnd_strategy)
@settings(max_examples=50)
def test_linkend_instantiation(instance):
    assert isinstance(instance, LinkEnd)

@given(instance=AttributeLink_strategy)
@settings(max_examples=50)
def test_attributelink_instantiation(instance):
    assert isinstance(instance, AttributeLink)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=behavioral_elements_activity_graphs_ClassifierInState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_classifierinstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_ClassifierInState)

@given(instance=behavioral_elements_common_behavior_Signal_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_signal_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Signal)

@given(instance=ObjectSetExpression_strategy)
@settings(max_examples=50)
def test_objectsetexpression_instantiation(instance):
    assert isinstance(instance, ObjectSetExpression)

@given(instance=IterationExpression_strategy)
@settings(max_examples=50)
def test_iterationexpression_instantiation(instance):
    assert isinstance(instance, IterationExpression)

@given(instance=SignalEvent_strategy)
@settings(max_examples=50)
def test_signalevent_instantiation(instance):
    assert isinstance(instance, SignalEvent)

@given(instance=SendAction_strategy)
@settings(max_examples=50)
def test_sendaction_instantiation(instance):
    assert isinstance(instance, SendAction)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=behavioral_elements_collaborations_Interaction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_interaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_Interaction)

@given(instance=behavioral_elements_collaborations_CollaborationInstanceSet_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_collaborationinstanceset_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_CollaborationInstanceSet)

@given(instance=behavioral_elements_collaborations_InteractionInstanceSet_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_interactioninstanceset_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_InteractionInstanceSet)

@given(instance=behavioral_elements_activity_graphs_Partition_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_partition_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_Partition)

@given(instance=behavioral_elements_common_behavior_Action_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_action_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Action)



@given(instance=behavioral_elements_common_behavior_Action_strategy)
def test_behavioral_elements_common_behavior_action_isAsynchronous_setter(instance):
    original = instance.isAsynchronous
    instance.isAsynchronous = original
    assert instance.isAsynchronous == original

@given(instance=behavioral_elements_common_behavior_Link_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_link_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Link)

@given(instance=behavioral_elements_common_behavior_Instance_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_instance_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Instance)

@given(instance=behavioral_elements_collaborations_Message_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_message_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_Message)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ClassifierRole_strategy)
@settings(max_examples=50)
def test_classifierrole_instantiation(instance):
    assert isinstance(instance, ClassifierRole)

@given(instance=Interaction_strategy)
@settings(max_examples=50)
def test_interaction_instantiation(instance):
    assert isinstance(instance, Interaction)

@given(instance=core_Namespace_strategy)
@settings(max_examples=50)
def test_core_namespace_instantiation(instance):
    assert isinstance(instance, core_Namespace)

@given(instance=core_GeneralizableElement_strategy)
@settings(max_examples=50)
def test_core_generalizableelement_instantiation(instance):
    assert isinstance(instance, core_GeneralizableElement)

@given(instance=behavioral_elements_collaborations_Collaboration_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_collaboration_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_Collaboration)

@given(instance=Multiplicity__strategy)
@settings(max_examples=50)
def test_multiplicity__instantiation(instance):
    assert isinstance(instance, Multiplicity_)

@given(instance=behavioral_elements_collaborations_ClassifierRole_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_classifierrole_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_ClassifierRole)

@given(instance=Collaboration_strategy)
@settings(max_examples=50)
def test_collaboration_instantiation(instance):
    assert isinstance(instance, Collaboration)

@given(instance=CollaborationInstanceSet_strategy)
@settings(max_examples=50)
def test_collaborationinstanceset_instantiation(instance):
    assert isinstance(instance, CollaborationInstanceSet)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=behavioral_elements_state_machines_Transition_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_transition_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_Transition)

@given(instance=behavioral_elements_state_machines_Guard_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_guard_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_Guard)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=behavioral_elements_activity_graphs_ActivityGraph_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_activitygraph_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_ActivityGraph)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=behavioral_elements_state_machines_SynchState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_synchstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_SynchState)



@given(instance=behavioral_elements_state_machines_SynchState_strategy)
def test_behavioral_elements_state_machines_synchstate_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=behavioral_elements_state_machines_Pseudostate_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_pseudostate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_Pseudostate)



@given(instance=behavioral_elements_state_machines_Pseudostate_strategy)
def test_behavioral_elements_state_machines_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=behavioral_elements_state_machines_StubState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_stubstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_StubState)



@given(instance=behavioral_elements_state_machines_StubState_strategy)
def test_behavioral_elements_state_machines_stubstate_referenceState_setter(instance):
    original = instance.referenceState
    instance.referenceState = original
    assert instance.referenceState == original

@given(instance=behavioral_elements_state_machines_State_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_state_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_State)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=behavioral_elements_state_machines_SubmachineState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_submachinestate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_SubmachineState)

@given(instance=behavioral_elements_state_machines_StateVertex_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_statevertex_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_StateVertex)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=behavioral_elements_state_machines_Event_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_event_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_Event)

@given(instance=SubmachineState_strategy)
@settings(max_examples=50)
def test_submachinestate_instantiation(instance):
    assert isinstance(instance, SubmachineState)

@given(instance=behavioral_elements_activity_graphs_SubactivityState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_activity_graphs_subactivitystate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_activity_graphs_SubactivityState)



@given(instance=behavioral_elements_activity_graphs_SubactivityState_strategy)
def test_behavioral_elements_activity_graphs_subactivitystate_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=TimeExpression_strategy)
@settings(max_examples=50)
def test_timeexpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=behavioral_elements_state_machines_SignalEvent_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_signalevent_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_SignalEvent)

@given(instance=behavioral_elements_state_machines_CallEvent_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_callevent_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_CallEvent)

@given(instance=behavioral_elements_state_machines_TimeEvent_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_timeevent_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_TimeEvent)

@given(instance=behavioral_elements_state_machines_ChangeEvent_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_changeevent_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_ChangeEvent)

@given(instance=behavioral_elements_use_cases_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_extensionpoint_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_ExtensionPoint)



@given(instance=behavioral_elements_use_cases_ExtensionPoint_strategy)
def test_behavioral_elements_use_cases_extensionpoint_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=UseCase_strategy)
@settings(max_examples=50)
def test_usecase_instantiation(instance):
    assert isinstance(instance, UseCase)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=behavioral_elements_use_cases_Include_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_include_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_Include)

@given(instance=behavioral_elements_use_cases_Extend_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_extend_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_Extend)

@given(instance=behavioral_elements_use_cases_UseCaseInstance_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_usecaseinstance_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_UseCaseInstance)

@given(instance=behavioral_elements_use_cases_Actor_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_actor_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_Actor)

@given(instance=ExtensionPoint_strategy)
@settings(max_examples=50)
def test_extensionpoint_instantiation(instance):
    assert isinstance(instance, ExtensionPoint)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=behavioral_elements_state_machines_CompositeState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_compositestate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_CompositeState)



@given(instance=behavioral_elements_state_machines_CompositeState_strategy)
def test_behavioral_elements_state_machines_compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=behavioral_elements_state_machines_FinalState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_finalstate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_FinalState)

@given(instance=behavioral_elements_state_machines_SimpleState_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_simplestate_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_SimpleState)

@given(instance=behavioral_elements_state_machines_StateMachine_strategy)
@settings(max_examples=50)
def test_behavioral_elements_state_machines_statemachine_instantiation(instance):
    assert isinstance(instance, behavioral_elements_state_machines_StateMachine)

@given(instance=behavioral_elements_common_behavior_NodeInstance_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_nodeinstance_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_NodeInstance)

@given(instance=NodeInstance_strategy)
@settings(max_examples=50)
def test_nodeinstance_instantiation(instance):
    assert isinstance(instance, NodeInstance)

@given(instance=behavioral_elements_common_behavior_ComponentInstance_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_componentinstance_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_ComponentInstance)

@given(instance=InteractionInstanceSet_strategy)
@settings(max_examples=50)
def test_interactioninstanceset_instantiation(instance):
    assert isinstance(instance, InteractionInstanceSet)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=Include_strategy)
@settings(max_examples=50)
def test_include_instantiation(instance):
    assert isinstance(instance, Include)

@given(instance=Extend_strategy)
@settings(max_examples=50)
def test_extend_instantiation(instance):
    assert isinstance(instance, Extend)

@given(instance=behavioral_elements_use_cases_UseCase_strategy)
@settings(max_examples=50)
def test_behavioral_elements_use_cases_usecase_instantiation(instance):
    assert isinstance(instance, behavioral_elements_use_cases_UseCase)

@given(instance=behavioral_elements_common_behavior_SubsystemInstance_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_subsysteminstance_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_SubsystemInstance)

@given(instance=AssociationEnd_strategy)
@settings(max_examples=50)
def test_associationend_instantiation(instance):
    assert isinstance(instance, AssociationEnd)

@given(instance=behavioral_elements_collaborations_AssociationEndRole_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_associationendrole_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_AssociationEndRole)

@given(instance=behavioral_elements_common_behavior_LinkEnd_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_linkend_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_LinkEnd)

@given(instance=behavioral_elements_common_behavior_Reception_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_reception_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Reception)



@given(instance=behavioral_elements_common_behavior_Reception_strategy)
def test_behavioral_elements_common_behavior_reception_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original



@given(instance=behavioral_elements_common_behavior_Reception_strategy)
def test_behavioral_elements_common_behavior_reception_isRoot_setter(instance):
    original = instance.isRoot
    instance.isRoot = original
    assert instance.isRoot == original



@given(instance=behavioral_elements_common_behavior_Reception_strategy)
def test_behavioral_elements_common_behavior_reception_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=behavioral_elements_common_behavior_Reception_strategy)
def test_behavioral_elements_common_behavior_reception_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behavioral_elements_common_behavior_Argument_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_argument_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Argument)

@given(instance=behavioral_elements_common_behavior_Stimulus_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_stimulus_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Stimulus)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=behavioral_elements_common_behavior_DataValue_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_datavalue_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_DataValue)

@given(instance=common_behavior_Link_strategy)
@settings(max_examples=50)
def test_common_behavior_link_instantiation(instance):
    assert isinstance(instance, common_behavior_Link)

@given(instance=common_behavior_Object_strategy)
@settings(max_examples=50)
def test_common_behavior_object_instantiation(instance):
    assert isinstance(instance, common_behavior_Object)

@given(instance=behavioral_elements_common_behavior_LinkObject_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_linkobject_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_LinkObject)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=behavioral_elements_common_behavior_Exception_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_exception_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_Exception)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=behavioral_elements_common_behavior_AttributeLink_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_attributelink_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_AttributeLink)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=behavioral_elements_common_behavior_SendAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_sendaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_SendAction)

@given(instance=behavioral_elements_common_behavior_UninterpretedAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_uninterpretedaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_UninterpretedAction)

@given(instance=behavioral_elements_common_behavior_ReturnAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_returnaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_ReturnAction)

@given(instance=behavioral_elements_common_behavior_ActionSequence_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_actionsequence_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_ActionSequence)

@given(instance=behavioral_elements_common_behavior_DestroyAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_destroyaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_DestroyAction)

@given(instance=behavioral_elements_common_behavior_CallAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_callaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_CallAction)

@given(instance=behavioral_elements_common_behavior_TerminateAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_terminateaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_TerminateAction)

@given(instance=behavioral_elements_common_behavior_CreateAction_strategy)
@settings(max_examples=50)
def test_behavioral_elements_common_behavior_createaction_instantiation(instance):
    assert isinstance(instance, behavioral_elements_common_behavior_CreateAction)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Stimulus_strategy)
@settings(max_examples=50)
def test_stimulus_instantiation(instance):
    assert isinstance(instance, Stimulus)

@given(instance=ActionSequence_strategy)
@settings(max_examples=50)
def test_actionsequence_instantiation(instance):
    assert isinstance(instance, ActionSequence)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=ActionExpression_strategy)
@settings(max_examples=50)
def test_actionexpression_instantiation(instance):
    assert isinstance(instance, ActionExpression)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=behavioral_elements_collaborations_AssociationRole_strategy)
@settings(max_examples=50)
def test_behavioral_elements_collaborations_associationrole_instantiation(instance):
    assert isinstance(instance, behavioral_elements_collaborations_AssociationRole)
