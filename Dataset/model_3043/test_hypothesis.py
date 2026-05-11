import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArgListsExpression,
    ActivityGraph,
    Partition,
    ActionState,
    behavioral::elements::activity::graphs::CallState,
    SimpleState,
    behavioral::elements::activity::graphs::ObjectFlowState,
    behavioral::elements::activity::graphs::ActionState,
    AssociationRole,
    Feature,
    ClassifierRole,
    Interaction,
    core::Namespace,
    core::GeneralizableElement,
    behavioral::elements::collaborations::Collaboration,
    Multiplicity_,
    Collaboration,
    CollaborationInstanceSet,
    Guard,
    StateMachine,
    behavioral::elements::activity::graphs::ActivityGraph,
    StateVertex,
    behavioral::elements::state::machines::StubState,
    behavioral::elements::state::machines::SynchState,
    behavioral::elements::state::machines::Pseudostate,
    behavioral::elements::state::machines::State,
    CompositeState,
    behavioral::elements::state::machines::SubmachineState,
    Parameter,
    SubmachineState,
    behavioral::elements::activity::graphs::SubactivityState,
    TimeExpression,
    Event,
    behavioral::elements::state::machines::SignalEvent,
    behavioral::elements::state::machines::CallEvent,
    behavioral::elements::state::machines::ChangeEvent,
    behavioral::elements::state::machines::TimeEvent,
    UseCase,
    BooleanExpression,
    Relationship,
    behavioral::elements::use::cases::Include,
    behavioral::elements::use::cases::Extend,
    ExtensionPoint,
    State,
    behavioral::elements::state::machines::FinalState,
    behavioral::elements::state::machines::CompositeState,
    behavioral::elements::state::machines::SimpleState,
    NodeInstance,
    InteractionInstanceSet,
    Message,
    Include,
    Extend,
    AssociationEnd,
    behavioral::elements::collaborations::AssociationEndRole,
    Expression,
    Operation,
    common::behavior::Link,
    common::behavior::Object,
    behavioral::elements::common::behavior::LinkObject,
    Signal,
    behavioral::elements::common::behavior::Exception,
    Attribute,
    Action,
    behavioral::elements::common::behavior::DestroyAction,
    behavioral::elements::common::behavior::SendAction,
    behavioral::elements::common::behavior::TerminateAction,
    behavioral::elements::common::behavior::ReturnAction,
    behavioral::elements::common::behavior::UninterpretedAction,
    behavioral::elements::common::behavior::ActionSequence,
    behavioral::elements::common::behavior::CallAction,
    behavioral::elements::common::behavior::CreateAction,
    Transition,
    Stimulus,
    ActionSequence,
    Argument,
    ActionExpression,
    Association,
    behavioral::elements::collaborations::AssociationRole,
    BehavioralFeature,
    behavioral::elements::common::behavior::Reception,
    Reception,
    Link,
    Instance,
    behavioral::elements::common::behavior::SubsystemInstance,
    behavioral::elements::common::behavior::DataValue,
    behavioral::elements::common::behavior::NodeInstance,
    behavioral::elements::use::cases::UseCaseInstance,
    behavioral::elements::common::behavior::ComponentInstance,
    behavioral::elements::common::behavior::Object,
    ComponentInstance,
    LinkEnd,
    AttributeLink,
    Classifier,
    behavioral::elements::common::behavior::Signal,
    behavioral::elements::collaborations::ClassifierRole,
    behavioral::elements::use::cases::Actor,
    behavioral::elements::activity::graphs::ClassifierInState,
    behavioral::elements::use::cases::UseCase,
    ObjectSetExpression,
    IterationExpression,
    SignalEvent,
    SendAction,
    ModelElement,
    behavioral::elements::state::machines::Event,
    behavioral::elements::common::behavior::Action,
    behavioral::elements::common::behavior::AttributeLink,
    behavioral::elements::use::cases::ExtensionPoint,
    behavioral::elements::collaborations::InteractionInstanceSet,
    behavioral::elements::collaborations::Interaction,
    behavioral::elements::common::behavior::LinkEnd,
    behavioral::elements::collaborations::CollaborationInstanceSet,
    behavioral::elements::common::behavior::Argument,
    behavioral::elements::collaborations::Message,
    behavioral::elements::common::behavior::Stimulus,
    behavioral::elements::state::machines::Transition,
    behavioral::elements::state::machines::Guard,
    behavioral::elements::common::behavior::Link,
    behavioral::elements::activity::graphs::Partition,
    behavioral::elements::state::machines::StateMachine,
    behavioral::elements::state::machines::StateVertex,
    behavioral::elements::common::behavior::Instance,
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



def test_behavioral::elements::activity::graphs::callstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::CallState)


def test_behavioral::elements::activity::graphs::callstate_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::CallState.__init__)


def test_behavioral::elements::activity::graphs::callstate_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::CallState.__init__)
    params = list(sig.parameters.keys())



def test_simplestate_is_not_abstract():
    assert not inspect.isabstract(SimpleState)


def test_simplestate_constructor_exists():
    assert callable(SimpleState.__init__)


def test_simplestate_constructor_args():
    sig = inspect.signature(SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::activity::graphs::objectflowstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::ObjectFlowState)


def test_behavioral::elements::activity::graphs::objectflowstate_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::ObjectFlowState.__init__)


def test_behavioral::elements::activity::graphs::objectflowstate_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::ObjectFlowState.__init__)
    params = list(sig.parameters.keys())
    assert "isSynch" in params, "Missing parameter 'isSynch'"

def test_behavioral::elements::activity::graphs::objectflowstate_has_isSynch():
    assert hasattr(behavioral::elements::activity::graphs::ObjectFlowState, "isSynch")
    descriptor = None
    for klass in behavioral::elements::activity::graphs::ObjectFlowState.__mro__:
        if "isSynch" in klass.__dict__:
            descriptor = klass.__dict__["isSynch"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::activity::graphs::actionstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::ActionState)


def test_behavioral::elements::activity::graphs::actionstate_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::ActionState.__init__)


def test_behavioral::elements::activity::graphs::actionstate_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_behavioral::elements::activity::graphs::actionstate_has_isDynamic():
    assert hasattr(behavioral::elements::activity::graphs::ActionState, "isDynamic")
    descriptor = None
    for klass in behavioral::elements::activity::graphs::ActionState.__mro__:
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



def test_core::namespace_is_not_abstract():
    assert not inspect.isabstract(core::Namespace)


def test_core::namespace_constructor_exists():
    assert callable(core::Namespace.__init__)


def test_core::namespace_constructor_args():
    sig = inspect.signature(core::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_core::generalizableelement_is_not_abstract():
    assert not inspect.isabstract(core::GeneralizableElement)


def test_core::generalizableelement_constructor_exists():
    assert callable(core::GeneralizableElement.__init__)


def test_core::generalizableelement_constructor_args():
    sig = inspect.signature(core::GeneralizableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::collaboration_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::Collaboration)


def test_behavioral::elements::collaborations::collaboration_constructor_exists():
    assert callable(behavioral::elements::collaborations::Collaboration.__init__)


def test_behavioral::elements::collaborations::collaboration_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_multiplicity__is_not_abstract():
    assert not inspect.isabstract(Multiplicity_)


def test_multiplicity__constructor_exists():
    assert callable(Multiplicity_.__init__)


def test_multiplicity__constructor_args():
    sig = inspect.signature(Multiplicity_.__init__)
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



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::activity::graphs::activitygraph_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::ActivityGraph)


def test_behavioral::elements::activity::graphs::activitygraph_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::ActivityGraph.__init__)


def test_behavioral::elements::activity::graphs::activitygraph_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::ActivityGraph.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::stubstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::StubState)


def test_behavioral::elements::state::machines::stubstate_constructor_exists():
    assert callable(behavioral::elements::state::machines::StubState.__init__)


def test_behavioral::elements::state::machines::stubstate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::StubState.__init__)
    params = list(sig.parameters.keys())
    assert "referenceState" in params, "Missing parameter 'referenceState'"

def test_behavioral::elements::state::machines::stubstate_has_referenceState():
    assert hasattr(behavioral::elements::state::machines::StubState, "referenceState")
    descriptor = None
    for klass in behavioral::elements::state::machines::StubState.__mro__:
        if "referenceState" in klass.__dict__:
            descriptor = klass.__dict__["referenceState"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::state::machines::synchstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::SynchState)


def test_behavioral::elements::state::machines::synchstate_constructor_exists():
    assert callable(behavioral::elements::state::machines::SynchState.__init__)


def test_behavioral::elements::state::machines::synchstate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::SynchState.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_behavioral::elements::state::machines::synchstate_has_bound():
    assert hasattr(behavioral::elements::state::machines::SynchState, "bound")
    descriptor = None
    for klass in behavioral::elements::state::machines::SynchState.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::state::machines::pseudostate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::Pseudostate)


def test_behavioral::elements::state::machines::pseudostate_constructor_exists():
    assert callable(behavioral::elements::state::machines::Pseudostate.__init__)


def test_behavioral::elements::state::machines::pseudostate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_behavioral::elements::state::machines::pseudostate_has_kind():
    assert hasattr(behavioral::elements::state::machines::Pseudostate, "kind")
    descriptor = None
    for klass in behavioral::elements::state::machines::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::state::machines::state_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::State)


def test_behavioral::elements::state::machines::state_constructor_exists():
    assert callable(behavioral::elements::state::machines::State.__init__)


def test_behavioral::elements::state::machines::state_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::State.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::submachinestate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::SubmachineState)


def test_behavioral::elements::state::machines::submachinestate_constructor_exists():
    assert callable(behavioral::elements::state::machines::SubmachineState.__init__)


def test_behavioral::elements::state::machines::submachinestate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::SubmachineState.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_submachinestate_is_not_abstract():
    assert not inspect.isabstract(SubmachineState)


def test_submachinestate_constructor_exists():
    assert callable(SubmachineState.__init__)


def test_submachinestate_constructor_args():
    sig = inspect.signature(SubmachineState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::activity::graphs::subactivitystate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::SubactivityState)


def test_behavioral::elements::activity::graphs::subactivitystate_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::SubactivityState.__init__)


def test_behavioral::elements::activity::graphs::subactivitystate_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::SubactivityState.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_behavioral::elements::activity::graphs::subactivitystate_has_isDynamic():
    assert hasattr(behavioral::elements::activity::graphs::SubactivityState, "isDynamic")
    descriptor = None
    for klass in behavioral::elements::activity::graphs::SubactivityState.__mro__:
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



def test_behavioral::elements::state::machines::signalevent_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::SignalEvent)


def test_behavioral::elements::state::machines::signalevent_constructor_exists():
    assert callable(behavioral::elements::state::machines::SignalEvent.__init__)


def test_behavioral::elements::state::machines::signalevent_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::callevent_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::CallEvent)


def test_behavioral::elements::state::machines::callevent_constructor_exists():
    assert callable(behavioral::elements::state::machines::CallEvent.__init__)


def test_behavioral::elements::state::machines::callevent_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::changeevent_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::ChangeEvent)


def test_behavioral::elements::state::machines::changeevent_constructor_exists():
    assert callable(behavioral::elements::state::machines::ChangeEvent.__init__)


def test_behavioral::elements::state::machines::changeevent_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::timeevent_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::TimeEvent)


def test_behavioral::elements::state::machines::timeevent_constructor_exists():
    assert callable(behavioral::elements::state::machines::TimeEvent.__init__)


def test_behavioral::elements::state::machines::timeevent_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::TimeEvent.__init__)
    params = list(sig.parameters.keys())



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



def test_behavioral::elements::use::cases::include_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::Include)


def test_behavioral::elements::use::cases::include_constructor_exists():
    assert callable(behavioral::elements::use::cases::Include.__init__)


def test_behavioral::elements::use::cases::include_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::Include.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::use::cases::extend_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::Extend)


def test_behavioral::elements::use::cases::extend_constructor_exists():
    assert callable(behavioral::elements::use::cases::Extend.__init__)


def test_behavioral::elements::use::cases::extend_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::Extend.__init__)
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



def test_behavioral::elements::state::machines::finalstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::FinalState)


def test_behavioral::elements::state::machines::finalstate_constructor_exists():
    assert callable(behavioral::elements::state::machines::FinalState.__init__)


def test_behavioral::elements::state::machines::finalstate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::compositestate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::CompositeState)


def test_behavioral::elements::state::machines::compositestate_constructor_exists():
    assert callable(behavioral::elements::state::machines::CompositeState.__init__)


def test_behavioral::elements::state::machines::compositestate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "isConcurrent" in params, "Missing parameter 'isConcurrent'"

def test_behavioral::elements::state::machines::compositestate_has_isConcurrent():
    assert hasattr(behavioral::elements::state::machines::CompositeState, "isConcurrent")
    descriptor = None
    for klass in behavioral::elements::state::machines::CompositeState.__mro__:
        if "isConcurrent" in klass.__dict__:
            descriptor = klass.__dict__["isConcurrent"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::state::machines::simplestate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::SimpleState)


def test_behavioral::elements::state::machines::simplestate_constructor_exists():
    assert callable(behavioral::elements::state::machines::SimpleState.__init__)


def test_behavioral::elements::state::machines::simplestate_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(NodeInstance)


def test_nodeinstance_constructor_exists():
    assert callable(NodeInstance.__init__)


def test_nodeinstance_constructor_args():
    sig = inspect.signature(NodeInstance.__init__)
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



def test_associationend_is_not_abstract():
    assert not inspect.isabstract(AssociationEnd)


def test_associationend_constructor_exists():
    assert callable(AssociationEnd.__init__)


def test_associationend_constructor_args():
    sig = inspect.signature(AssociationEnd.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::associationendrole_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::AssociationEndRole)


def test_behavioral::elements::collaborations::associationendrole_constructor_exists():
    assert callable(behavioral::elements::collaborations::AssociationEndRole.__init__)


def test_behavioral::elements::collaborations::associationendrole_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::AssociationEndRole.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_common::behavior::link_is_not_abstract():
    assert not inspect.isabstract(common::behavior::Link)


def test_common::behavior::link_constructor_exists():
    assert callable(common::behavior::Link.__init__)


def test_common::behavior::link_constructor_args():
    sig = inspect.signature(common::behavior::Link.__init__)
    params = list(sig.parameters.keys())



def test_common::behavior::object_is_not_abstract():
    assert not inspect.isabstract(common::behavior::Object)


def test_common::behavior::object_constructor_exists():
    assert callable(common::behavior::Object.__init__)


def test_common::behavior::object_constructor_args():
    sig = inspect.signature(common::behavior::Object.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::linkobject_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::LinkObject)


def test_behavioral::elements::common::behavior::linkobject_constructor_exists():
    assert callable(behavioral::elements::common::behavior::LinkObject.__init__)


def test_behavioral::elements::common::behavior::linkobject_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::LinkObject.__init__)
    params = list(sig.parameters.keys())



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::exception_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Exception)


def test_behavioral::elements::common::behavior::exception_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Exception.__init__)


def test_behavioral::elements::common::behavior::exception_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Exception.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::destroyaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::DestroyAction)


def test_behavioral::elements::common::behavior::destroyaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::DestroyAction.__init__)


def test_behavioral::elements::common::behavior::destroyaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::DestroyAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::sendaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::SendAction)


def test_behavioral::elements::common::behavior::sendaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::SendAction.__init__)


def test_behavioral::elements::common::behavior::sendaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::SendAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::terminateaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::TerminateAction)


def test_behavioral::elements::common::behavior::terminateaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::TerminateAction.__init__)


def test_behavioral::elements::common::behavior::terminateaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::TerminateAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::returnaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::ReturnAction)


def test_behavioral::elements::common::behavior::returnaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::ReturnAction.__init__)


def test_behavioral::elements::common::behavior::returnaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::uninterpretedaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::UninterpretedAction)


def test_behavioral::elements::common::behavior::uninterpretedaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::UninterpretedAction.__init__)


def test_behavioral::elements::common::behavior::uninterpretedaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::UninterpretedAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::actionsequence_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::ActionSequence)


def test_behavioral::elements::common::behavior::actionsequence_constructor_exists():
    assert callable(behavioral::elements::common::behavior::ActionSequence.__init__)


def test_behavioral::elements::common::behavior::actionsequence_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::ActionSequence.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::callaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::CallAction)


def test_behavioral::elements::common::behavior::callaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::CallAction.__init__)


def test_behavioral::elements::common::behavior::callaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::CallAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::createaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::CreateAction)


def test_behavioral::elements::common::behavior::createaction_constructor_exists():
    assert callable(behavioral::elements::common::behavior::CreateAction.__init__)


def test_behavioral::elements::common::behavior::createaction_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::CreateAction.__init__)
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



def test_behavioral::elements::collaborations::associationrole_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::AssociationRole)


def test_behavioral::elements::collaborations::associationrole_constructor_exists():
    assert callable(behavioral::elements::collaborations::AssociationRole.__init__)


def test_behavioral::elements::collaborations::associationrole_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::AssociationRole.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::reception_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Reception)


def test_behavioral::elements::common::behavior::reception_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Reception.__init__)


def test_behavioral::elements::common::behavior::reception_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Reception.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"
    assert "isRoot" in params, "Missing parameter 'isRoot'"
    assert "specification" in params, "Missing parameter 'specification'"

def test_behavioral::elements::common::behavior::reception_has_isAbstract():
    assert hasattr(behavioral::elements::common::behavior::Reception, "isAbstract")
    descriptor = None
    for klass in behavioral::elements::common::behavior::Reception.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::elements::common::behavior::reception_has_isLeaf():
    assert hasattr(behavioral::elements::common::behavior::Reception, "isLeaf")
    descriptor = None
    for klass in behavioral::elements::common::behavior::Reception.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::elements::common::behavior::reception_has_isRoot():
    assert hasattr(behavioral::elements::common::behavior::Reception, "isRoot")
    descriptor = None
    for klass in behavioral::elements::common::behavior::Reception.__mro__:
        if "isRoot" in klass.__dict__:
            descriptor = klass.__dict__["isRoot"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::elements::common::behavior::reception_has_specification():
    assert hasattr(behavioral::elements::common::behavior::Reception, "specification")
    descriptor = None
    for klass in behavioral::elements::common::behavior::Reception.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



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



def test_behavioral::elements::common::behavior::subsysteminstance_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::SubsystemInstance)


def test_behavioral::elements::common::behavior::subsysteminstance_constructor_exists():
    assert callable(behavioral::elements::common::behavior::SubsystemInstance.__init__)


def test_behavioral::elements::common::behavior::subsysteminstance_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::SubsystemInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::datavalue_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::DataValue)


def test_behavioral::elements::common::behavior::datavalue_constructor_exists():
    assert callable(behavioral::elements::common::behavior::DataValue.__init__)


def test_behavioral::elements::common::behavior::datavalue_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::DataValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::nodeinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::NodeInstance)


def test_behavioral::elements::common::behavior::nodeinstance_constructor_exists():
    assert callable(behavioral::elements::common::behavior::NodeInstance.__init__)


def test_behavioral::elements::common::behavior::nodeinstance_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::use::cases::usecaseinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::UseCaseInstance)


def test_behavioral::elements::use::cases::usecaseinstance_constructor_exists():
    assert callable(behavioral::elements::use::cases::UseCaseInstance.__init__)


def test_behavioral::elements::use::cases::usecaseinstance_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::UseCaseInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::componentinstance_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::ComponentInstance)


def test_behavioral::elements::common::behavior::componentinstance_constructor_exists():
    assert callable(behavioral::elements::common::behavior::ComponentInstance.__init__)


def test_behavioral::elements::common::behavior::componentinstance_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::object_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Object)


def test_behavioral::elements::common::behavior::object_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Object.__init__)


def test_behavioral::elements::common::behavior::object_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Object.__init__)
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



def test_behavioral::elements::common::behavior::signal_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Signal)


def test_behavioral::elements::common::behavior::signal_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Signal.__init__)


def test_behavioral::elements::common::behavior::signal_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Signal.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::classifierrole_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::ClassifierRole)


def test_behavioral::elements::collaborations::classifierrole_constructor_exists():
    assert callable(behavioral::elements::collaborations::ClassifierRole.__init__)


def test_behavioral::elements::collaborations::classifierrole_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::ClassifierRole.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::use::cases::actor_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::Actor)


def test_behavioral::elements::use::cases::actor_constructor_exists():
    assert callable(behavioral::elements::use::cases::Actor.__init__)


def test_behavioral::elements::use::cases::actor_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::Actor.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::activity::graphs::classifierinstate_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::ClassifierInState)


def test_behavioral::elements::activity::graphs::classifierinstate_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::ClassifierInState.__init__)


def test_behavioral::elements::activity::graphs::classifierinstate_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::ClassifierInState.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::use::cases::usecase_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::UseCase)


def test_behavioral::elements::use::cases::usecase_constructor_exists():
    assert callable(behavioral::elements::use::cases::UseCase.__init__)


def test_behavioral::elements::use::cases::usecase_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::UseCase.__init__)
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



def test_behavioral::elements::state::machines::event_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::Event)


def test_behavioral::elements::state::machines::event_constructor_exists():
    assert callable(behavioral::elements::state::machines::Event.__init__)


def test_behavioral::elements::state::machines::event_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::Event.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::action_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Action)


def test_behavioral::elements::common::behavior::action_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Action.__init__)


def test_behavioral::elements::common::behavior::action_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Action.__init__)
    params = list(sig.parameters.keys())
    assert "isAsynchronous" in params, "Missing parameter 'isAsynchronous'"

def test_behavioral::elements::common::behavior::action_has_isAsynchronous():
    assert hasattr(behavioral::elements::common::behavior::Action, "isAsynchronous")
    descriptor = None
    for klass in behavioral::elements::common::behavior::Action.__mro__:
        if "isAsynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isAsynchronous"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::common::behavior::attributelink_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::AttributeLink)


def test_behavioral::elements::common::behavior::attributelink_constructor_exists():
    assert callable(behavioral::elements::common::behavior::AttributeLink.__init__)


def test_behavioral::elements::common::behavior::attributelink_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::AttributeLink.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::use::cases::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::use::cases::ExtensionPoint)


def test_behavioral::elements::use::cases::extensionpoint_constructor_exists():
    assert callable(behavioral::elements::use::cases::ExtensionPoint.__init__)


def test_behavioral::elements::use::cases::extensionpoint_constructor_args():
    sig = inspect.signature(behavioral::elements::use::cases::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_behavioral::elements::use::cases::extensionpoint_has_location():
    assert hasattr(behavioral::elements::use::cases::ExtensionPoint, "location")
    descriptor = None
    for klass in behavioral::elements::use::cases::ExtensionPoint.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::elements::collaborations::interactioninstanceset_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::InteractionInstanceSet)


def test_behavioral::elements::collaborations::interactioninstanceset_constructor_exists():
    assert callable(behavioral::elements::collaborations::InteractionInstanceSet.__init__)


def test_behavioral::elements::collaborations::interactioninstanceset_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::InteractionInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::interaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::Interaction)


def test_behavioral::elements::collaborations::interaction_constructor_exists():
    assert callable(behavioral::elements::collaborations::Interaction.__init__)


def test_behavioral::elements::collaborations::interaction_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::linkend_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::LinkEnd)


def test_behavioral::elements::common::behavior::linkend_constructor_exists():
    assert callable(behavioral::elements::common::behavior::LinkEnd.__init__)


def test_behavioral::elements::common::behavior::linkend_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::LinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::collaborationinstanceset_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::CollaborationInstanceSet)


def test_behavioral::elements::collaborations::collaborationinstanceset_constructor_exists():
    assert callable(behavioral::elements::collaborations::CollaborationInstanceSet.__init__)


def test_behavioral::elements::collaborations::collaborationinstanceset_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::CollaborationInstanceSet.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::argument_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Argument)


def test_behavioral::elements::common::behavior::argument_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Argument.__init__)


def test_behavioral::elements::common::behavior::argument_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Argument.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::collaborations::message_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::collaborations::Message)


def test_behavioral::elements::collaborations::message_constructor_exists():
    assert callable(behavioral::elements::collaborations::Message.__init__)


def test_behavioral::elements::collaborations::message_constructor_args():
    sig = inspect.signature(behavioral::elements::collaborations::Message.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::stimulus_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Stimulus)


def test_behavioral::elements::common::behavior::stimulus_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Stimulus.__init__)


def test_behavioral::elements::common::behavior::stimulus_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Stimulus.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::transition_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::Transition)


def test_behavioral::elements::state::machines::transition_constructor_exists():
    assert callable(behavioral::elements::state::machines::Transition.__init__)


def test_behavioral::elements::state::machines::transition_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::Transition.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::guard_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::Guard)


def test_behavioral::elements::state::machines::guard_constructor_exists():
    assert callable(behavioral::elements::state::machines::Guard.__init__)


def test_behavioral::elements::state::machines::guard_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::Guard.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::link_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Link)


def test_behavioral::elements::common::behavior::link_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Link.__init__)


def test_behavioral::elements::common::behavior::link_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Link.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::activity::graphs::partition_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::activity::graphs::Partition)


def test_behavioral::elements::activity::graphs::partition_constructor_exists():
    assert callable(behavioral::elements::activity::graphs::Partition.__init__)


def test_behavioral::elements::activity::graphs::partition_constructor_args():
    sig = inspect.signature(behavioral::elements::activity::graphs::Partition.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::statemachine_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::StateMachine)


def test_behavioral::elements::state::machines::statemachine_constructor_exists():
    assert callable(behavioral::elements::state::machines::StateMachine.__init__)


def test_behavioral::elements::state::machines::statemachine_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::state::machines::statevertex_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::state::machines::StateVertex)


def test_behavioral::elements::state::machines::statevertex_constructor_exists():
    assert callable(behavioral::elements::state::machines::StateVertex.__init__)


def test_behavioral::elements::state::machines::statevertex_constructor_args():
    sig = inspect.signature(behavioral::elements::state::machines::StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::elements::common::behavior::instance_is_not_abstract():
    assert not inspect.isabstract(behavioral::elements::common::behavior::Instance)


def test_behavioral::elements::common::behavior::instance_constructor_exists():
    assert callable(behavioral::elements::common::behavior::Instance.__init__)


def test_behavioral::elements::common::behavior::instance_constructor_args():
    sig = inspect.signature(behavioral::elements::common::behavior::Instance.__init__)
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
behavioral::elements::activity::graphs::CallState_strategy = st.builds(
    behavioral::elements::activity::graphs::CallState,
)
SimpleState_strategy = st.builds(
    SimpleState,
)
behavioral::elements::activity::graphs::ObjectFlowState_strategy = st.builds(
    behavioral::elements::activity::graphs::ObjectFlowState,
    isSynch=
        safe_text
)
behavioral::elements::activity::graphs::ActionState_strategy = st.builds(
    behavioral::elements::activity::graphs::ActionState,
    isDynamic=
        safe_text
)
AssociationRole_strategy = st.builds(
    AssociationRole,
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
core::Namespace_strategy = st.builds(
    core::Namespace,
)
core::GeneralizableElement_strategy = st.builds(
    core::GeneralizableElement,
)
behavioral::elements::collaborations::Collaboration_strategy = st.builds(
    behavioral::elements::collaborations::Collaboration,
)
Multiplicity__strategy = st.builds(
    Multiplicity_,
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
StateMachine_strategy = st.builds(
    StateMachine,
)
behavioral::elements::activity::graphs::ActivityGraph_strategy = st.builds(
    behavioral::elements::activity::graphs::ActivityGraph,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
behavioral::elements::state::machines::StubState_strategy = st.builds(
    behavioral::elements::state::machines::StubState,
    referenceState=
        safe_text
)
behavioral::elements::state::machines::SynchState_strategy = st.builds(
    behavioral::elements::state::machines::SynchState,
    bound=
        safe_text
)
behavioral::elements::state::machines::Pseudostate_strategy = st.builds(
    behavioral::elements::state::machines::Pseudostate,
    kind=
        safe_text
)
behavioral::elements::state::machines::State_strategy = st.builds(
    behavioral::elements::state::machines::State,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
behavioral::elements::state::machines::SubmachineState_strategy = st.builds(
    behavioral::elements::state::machines::SubmachineState,
)
Parameter_strategy = st.builds(
    Parameter,
)
SubmachineState_strategy = st.builds(
    SubmachineState,
)
behavioral::elements::activity::graphs::SubactivityState_strategy = st.builds(
    behavioral::elements::activity::graphs::SubactivityState,
    isDynamic=
        safe_text
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
Event_strategy = st.builds(
    Event,
)
behavioral::elements::state::machines::SignalEvent_strategy = st.builds(
    behavioral::elements::state::machines::SignalEvent,
)
behavioral::elements::state::machines::CallEvent_strategy = st.builds(
    behavioral::elements::state::machines::CallEvent,
)
behavioral::elements::state::machines::ChangeEvent_strategy = st.builds(
    behavioral::elements::state::machines::ChangeEvent,
)
behavioral::elements::state::machines::TimeEvent_strategy = st.builds(
    behavioral::elements::state::machines::TimeEvent,
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
behavioral::elements::use::cases::Include_strategy = st.builds(
    behavioral::elements::use::cases::Include,
)
behavioral::elements::use::cases::Extend_strategy = st.builds(
    behavioral::elements::use::cases::Extend,
)
ExtensionPoint_strategy = st.builds(
    ExtensionPoint,
)
State_strategy = st.builds(
    State,
)
behavioral::elements::state::machines::FinalState_strategy = st.builds(
    behavioral::elements::state::machines::FinalState,
)
behavioral::elements::state::machines::CompositeState_strategy = st.builds(
    behavioral::elements::state::machines::CompositeState,
    isConcurrent=
        safe_text
)
behavioral::elements::state::machines::SimpleState_strategy = st.builds(
    behavioral::elements::state::machines::SimpleState,
)
NodeInstance_strategy = st.builds(
    NodeInstance,
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
AssociationEnd_strategy = st.builds(
    AssociationEnd,
)
behavioral::elements::collaborations::AssociationEndRole_strategy = st.builds(
    behavioral::elements::collaborations::AssociationEndRole,
)
Expression_strategy = st.builds(
    Expression,
)
Operation_strategy = st.builds(
    Operation,
)
common::behavior::Link_strategy = st.builds(
    common::behavior::Link,
)
common::behavior::Object_strategy = st.builds(
    common::behavior::Object,
)
behavioral::elements::common::behavior::LinkObject_strategy = st.builds(
    behavioral::elements::common::behavior::LinkObject,
)
Signal_strategy = st.builds(
    Signal,
)
behavioral::elements::common::behavior::Exception_strategy = st.builds(
    behavioral::elements::common::behavior::Exception,
)
Attribute_strategy = st.builds(
    Attribute,
)
Action_strategy = st.builds(
    Action,
)
behavioral::elements::common::behavior::DestroyAction_strategy = st.builds(
    behavioral::elements::common::behavior::DestroyAction,
)
behavioral::elements::common::behavior::SendAction_strategy = st.builds(
    behavioral::elements::common::behavior::SendAction,
)
behavioral::elements::common::behavior::TerminateAction_strategy = st.builds(
    behavioral::elements::common::behavior::TerminateAction,
)
behavioral::elements::common::behavior::ReturnAction_strategy = st.builds(
    behavioral::elements::common::behavior::ReturnAction,
)
behavioral::elements::common::behavior::UninterpretedAction_strategy = st.builds(
    behavioral::elements::common::behavior::UninterpretedAction,
)
behavioral::elements::common::behavior::ActionSequence_strategy = st.builds(
    behavioral::elements::common::behavior::ActionSequence,
)
behavioral::elements::common::behavior::CallAction_strategy = st.builds(
    behavioral::elements::common::behavior::CallAction,
)
behavioral::elements::common::behavior::CreateAction_strategy = st.builds(
    behavioral::elements::common::behavior::CreateAction,
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
behavioral::elements::collaborations::AssociationRole_strategy = st.builds(
    behavioral::elements::collaborations::AssociationRole,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
behavioral::elements::common::behavior::Reception_strategy = st.builds(
    behavioral::elements::common::behavior::Reception,
    isAbstract=
        safe_text,
    isLeaf=
        safe_text,
    isRoot=
        safe_text,
    specification=
        safe_text
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
behavioral::elements::common::behavior::SubsystemInstance_strategy = st.builds(
    behavioral::elements::common::behavior::SubsystemInstance,
)
behavioral::elements::common::behavior::DataValue_strategy = st.builds(
    behavioral::elements::common::behavior::DataValue,
)
behavioral::elements::common::behavior::NodeInstance_strategy = st.builds(
    behavioral::elements::common::behavior::NodeInstance,
)
behavioral::elements::use::cases::UseCaseInstance_strategy = st.builds(
    behavioral::elements::use::cases::UseCaseInstance,
)
behavioral::elements::common::behavior::ComponentInstance_strategy = st.builds(
    behavioral::elements::common::behavior::ComponentInstance,
)
behavioral::elements::common::behavior::Object_strategy = st.builds(
    behavioral::elements::common::behavior::Object,
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
behavioral::elements::common::behavior::Signal_strategy = st.builds(
    behavioral::elements::common::behavior::Signal,
)
behavioral::elements::collaborations::ClassifierRole_strategy = st.builds(
    behavioral::elements::collaborations::ClassifierRole,
)
behavioral::elements::use::cases::Actor_strategy = st.builds(
    behavioral::elements::use::cases::Actor,
)
behavioral::elements::activity::graphs::ClassifierInState_strategy = st.builds(
    behavioral::elements::activity::graphs::ClassifierInState,
)
behavioral::elements::use::cases::UseCase_strategy = st.builds(
    behavioral::elements::use::cases::UseCase,
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
behavioral::elements::state::machines::Event_strategy = st.builds(
    behavioral::elements::state::machines::Event,
)
behavioral::elements::common::behavior::Action_strategy = st.builds(
    behavioral::elements::common::behavior::Action,
    isAsynchronous=
        safe_text
)
behavioral::elements::common::behavior::AttributeLink_strategy = st.builds(
    behavioral::elements::common::behavior::AttributeLink,
)
behavioral::elements::use::cases::ExtensionPoint_strategy = st.builds(
    behavioral::elements::use::cases::ExtensionPoint,
    location=
        safe_text
)
behavioral::elements::collaborations::InteractionInstanceSet_strategy = st.builds(
    behavioral::elements::collaborations::InteractionInstanceSet,
)
behavioral::elements::collaborations::Interaction_strategy = st.builds(
    behavioral::elements::collaborations::Interaction,
)
behavioral::elements::common::behavior::LinkEnd_strategy = st.builds(
    behavioral::elements::common::behavior::LinkEnd,
)
behavioral::elements::collaborations::CollaborationInstanceSet_strategy = st.builds(
    behavioral::elements::collaborations::CollaborationInstanceSet,
)
behavioral::elements::common::behavior::Argument_strategy = st.builds(
    behavioral::elements::common::behavior::Argument,
)
behavioral::elements::collaborations::Message_strategy = st.builds(
    behavioral::elements::collaborations::Message,
)
behavioral::elements::common::behavior::Stimulus_strategy = st.builds(
    behavioral::elements::common::behavior::Stimulus,
)
behavioral::elements::state::machines::Transition_strategy = st.builds(
    behavioral::elements::state::machines::Transition,
)
behavioral::elements::state::machines::Guard_strategy = st.builds(
    behavioral::elements::state::machines::Guard,
)
behavioral::elements::common::behavior::Link_strategy = st.builds(
    behavioral::elements::common::behavior::Link,
)
behavioral::elements::activity::graphs::Partition_strategy = st.builds(
    behavioral::elements::activity::graphs::Partition,
)
behavioral::elements::state::machines::StateMachine_strategy = st.builds(
    behavioral::elements::state::machines::StateMachine,
)
behavioral::elements::state::machines::StateVertex_strategy = st.builds(
    behavioral::elements::state::machines::StateVertex,
)
behavioral::elements::common::behavior::Instance_strategy = st.builds(
    behavioral::elements::common::behavior::Instance,
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

@given(instance=behavioral::elements::activity::graphs::CallState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::callstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::CallState)

@given(instance=SimpleState_strategy)
@settings(max_examples=50)
def test_simplestate_instantiation(instance):
    assert isinstance(instance, SimpleState)

@given(instance=behavioral::elements::activity::graphs::ObjectFlowState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::objectflowstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::ObjectFlowState)

@given(instance=behavioral::elements::activity::graphs::ObjectFlowState_strategy)
def test_behavioral::elements::activity::graphs::objectflowstate_isSynch_type(instance):
    assert isinstance(instance.isSynch, str)


@given(instance=behavioral::elements::activity::graphs::ObjectFlowState_strategy)
def test_behavioral::elements::activity::graphs::objectflowstate_isSynch_setter(instance):
    original = instance.isSynch
    instance.isSynch = original
    assert instance.isSynch == original

@given(instance=behavioral::elements::activity::graphs::ActionState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::actionstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::ActionState)

@given(instance=behavioral::elements::activity::graphs::ActionState_strategy)
def test_behavioral::elements::activity::graphs::actionstate_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=behavioral::elements::activity::graphs::ActionState_strategy)
def test_behavioral::elements::activity::graphs::actionstate_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=AssociationRole_strategy)
@settings(max_examples=50)
def test_associationrole_instantiation(instance):
    assert isinstance(instance, AssociationRole)

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

@given(instance=core::Namespace_strategy)
@settings(max_examples=50)
def test_core::namespace_instantiation(instance):
    assert isinstance(instance, core::Namespace)

@given(instance=core::GeneralizableElement_strategy)
@settings(max_examples=50)
def test_core::generalizableelement_instantiation(instance):
    assert isinstance(instance, core::GeneralizableElement)

@given(instance=behavioral::elements::collaborations::Collaboration_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::collaboration_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::Collaboration)

@given(instance=Multiplicity__strategy)
@settings(max_examples=50)
def test_multiplicity__instantiation(instance):
    assert isinstance(instance, Multiplicity_)

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

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=behavioral::elements::activity::graphs::ActivityGraph_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::activitygraph_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::ActivityGraph)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=behavioral::elements::state::machines::StubState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::stubstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::StubState)

@given(instance=behavioral::elements::state::machines::StubState_strategy)
def test_behavioral::elements::state::machines::stubstate_referenceState_type(instance):
    assert isinstance(instance.referenceState, str)


@given(instance=behavioral::elements::state::machines::StubState_strategy)
def test_behavioral::elements::state::machines::stubstate_referenceState_setter(instance):
    original = instance.referenceState
    instance.referenceState = original
    assert instance.referenceState == original

@given(instance=behavioral::elements::state::machines::SynchState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::synchstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::SynchState)

@given(instance=behavioral::elements::state::machines::SynchState_strategy)
def test_behavioral::elements::state::machines::synchstate_bound_type(instance):
    assert isinstance(instance.bound, str)


@given(instance=behavioral::elements::state::machines::SynchState_strategy)
def test_behavioral::elements::state::machines::synchstate_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=behavioral::elements::state::machines::Pseudostate_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::pseudostate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::Pseudostate)

@given(instance=behavioral::elements::state::machines::Pseudostate_strategy)
def test_behavioral::elements::state::machines::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=behavioral::elements::state::machines::Pseudostate_strategy)
def test_behavioral::elements::state::machines::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=behavioral::elements::state::machines::State_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::state_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::State)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=behavioral::elements::state::machines::SubmachineState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::submachinestate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::SubmachineState)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=SubmachineState_strategy)
@settings(max_examples=50)
def test_submachinestate_instantiation(instance):
    assert isinstance(instance, SubmachineState)

@given(instance=behavioral::elements::activity::graphs::SubactivityState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::subactivitystate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::SubactivityState)

@given(instance=behavioral::elements::activity::graphs::SubactivityState_strategy)
def test_behavioral::elements::activity::graphs::subactivitystate_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=behavioral::elements::activity::graphs::SubactivityState_strategy)
def test_behavioral::elements::activity::graphs::subactivitystate_isDynamic_setter(instance):
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

@given(instance=behavioral::elements::state::machines::SignalEvent_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::signalevent_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::SignalEvent)

@given(instance=behavioral::elements::state::machines::CallEvent_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::callevent_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::CallEvent)

@given(instance=behavioral::elements::state::machines::ChangeEvent_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::changeevent_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::ChangeEvent)

@given(instance=behavioral::elements::state::machines::TimeEvent_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::timeevent_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::TimeEvent)

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

@given(instance=behavioral::elements::use::cases::Include_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::include_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::Include)

@given(instance=behavioral::elements::use::cases::Extend_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::extend_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::Extend)

@given(instance=ExtensionPoint_strategy)
@settings(max_examples=50)
def test_extensionpoint_instantiation(instance):
    assert isinstance(instance, ExtensionPoint)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=behavioral::elements::state::machines::FinalState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::finalstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::FinalState)

@given(instance=behavioral::elements::state::machines::CompositeState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::compositestate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::CompositeState)

@given(instance=behavioral::elements::state::machines::CompositeState_strategy)
def test_behavioral::elements::state::machines::compositestate_isConcurrent_type(instance):
    assert isinstance(instance.isConcurrent, str)


@given(instance=behavioral::elements::state::machines::CompositeState_strategy)
def test_behavioral::elements::state::machines::compositestate_isConcurrent_setter(instance):
    original = instance.isConcurrent
    instance.isConcurrent = original
    assert instance.isConcurrent == original

@given(instance=behavioral::elements::state::machines::SimpleState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::simplestate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::SimpleState)

@given(instance=NodeInstance_strategy)
@settings(max_examples=50)
def test_nodeinstance_instantiation(instance):
    assert isinstance(instance, NodeInstance)

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

@given(instance=AssociationEnd_strategy)
@settings(max_examples=50)
def test_associationend_instantiation(instance):
    assert isinstance(instance, AssociationEnd)

@given(instance=behavioral::elements::collaborations::AssociationEndRole_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::associationendrole_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::AssociationEndRole)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=common::behavior::Link_strategy)
@settings(max_examples=50)
def test_common::behavior::link_instantiation(instance):
    assert isinstance(instance, common::behavior::Link)

@given(instance=common::behavior::Object_strategy)
@settings(max_examples=50)
def test_common::behavior::object_instantiation(instance):
    assert isinstance(instance, common::behavior::Object)

@given(instance=behavioral::elements::common::behavior::LinkObject_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::linkobject_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::LinkObject)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=behavioral::elements::common::behavior::Exception_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::exception_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Exception)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=behavioral::elements::common::behavior::DestroyAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::destroyaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::DestroyAction)

@given(instance=behavioral::elements::common::behavior::SendAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::sendaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::SendAction)

@given(instance=behavioral::elements::common::behavior::TerminateAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::terminateaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::TerminateAction)

@given(instance=behavioral::elements::common::behavior::ReturnAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::returnaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::ReturnAction)

@given(instance=behavioral::elements::common::behavior::UninterpretedAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::uninterpretedaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::UninterpretedAction)

@given(instance=behavioral::elements::common::behavior::ActionSequence_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::actionsequence_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::ActionSequence)

@given(instance=behavioral::elements::common::behavior::CallAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::callaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::CallAction)

@given(instance=behavioral::elements::common::behavior::CreateAction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::createaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::CreateAction)

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

@given(instance=behavioral::elements::collaborations::AssociationRole_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::associationrole_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::AssociationRole)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=behavioral::elements::common::behavior::Reception_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::reception_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Reception)

@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, str)


@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isRoot_type(instance):
    assert isinstance(instance.isRoot, str)


@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_isRoot_setter(instance):
    original = instance.isRoot
    instance.isRoot = original
    assert instance.isRoot == original

@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=behavioral::elements::common::behavior::Reception_strategy)
def test_behavioral::elements::common::behavior::reception_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

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

@given(instance=behavioral::elements::common::behavior::SubsystemInstance_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::subsysteminstance_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::SubsystemInstance)

@given(instance=behavioral::elements::common::behavior::DataValue_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::datavalue_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::DataValue)

@given(instance=behavioral::elements::common::behavior::NodeInstance_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::nodeinstance_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::NodeInstance)

@given(instance=behavioral::elements::use::cases::UseCaseInstance_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::usecaseinstance_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::UseCaseInstance)

@given(instance=behavioral::elements::common::behavior::ComponentInstance_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::componentinstance_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::ComponentInstance)

@given(instance=behavioral::elements::common::behavior::Object_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::object_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Object)

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

@given(instance=behavioral::elements::common::behavior::Signal_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::signal_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Signal)

@given(instance=behavioral::elements::collaborations::ClassifierRole_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::classifierrole_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::ClassifierRole)

@given(instance=behavioral::elements::use::cases::Actor_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::actor_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::Actor)

@given(instance=behavioral::elements::activity::graphs::ClassifierInState_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::classifierinstate_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::ClassifierInState)

@given(instance=behavioral::elements::use::cases::UseCase_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::usecase_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::UseCase)

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

@given(instance=behavioral::elements::state::machines::Event_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::event_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::Event)

@given(instance=behavioral::elements::common::behavior::Action_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::action_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Action)

@given(instance=behavioral::elements::common::behavior::Action_strategy)
def test_behavioral::elements::common::behavior::action_isAsynchronous_type(instance):
    assert isinstance(instance.isAsynchronous, str)


@given(instance=behavioral::elements::common::behavior::Action_strategy)
def test_behavioral::elements::common::behavior::action_isAsynchronous_setter(instance):
    original = instance.isAsynchronous
    instance.isAsynchronous = original
    assert instance.isAsynchronous == original

@given(instance=behavioral::elements::common::behavior::AttributeLink_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::attributelink_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::AttributeLink)

@given(instance=behavioral::elements::use::cases::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_behavioral::elements::use::cases::extensionpoint_instantiation(instance):
    assert isinstance(instance, behavioral::elements::use::cases::ExtensionPoint)

@given(instance=behavioral::elements::use::cases::ExtensionPoint_strategy)
def test_behavioral::elements::use::cases::extensionpoint_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=behavioral::elements::use::cases::ExtensionPoint_strategy)
def test_behavioral::elements::use::cases::extensionpoint_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=behavioral::elements::collaborations::InteractionInstanceSet_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::interactioninstanceset_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::InteractionInstanceSet)

@given(instance=behavioral::elements::collaborations::Interaction_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::interaction_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::Interaction)

@given(instance=behavioral::elements::common::behavior::LinkEnd_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::linkend_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::LinkEnd)

@given(instance=behavioral::elements::collaborations::CollaborationInstanceSet_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::collaborationinstanceset_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::CollaborationInstanceSet)

@given(instance=behavioral::elements::common::behavior::Argument_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::argument_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Argument)

@given(instance=behavioral::elements::collaborations::Message_strategy)
@settings(max_examples=50)
def test_behavioral::elements::collaborations::message_instantiation(instance):
    assert isinstance(instance, behavioral::elements::collaborations::Message)

@given(instance=behavioral::elements::common::behavior::Stimulus_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::stimulus_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Stimulus)

@given(instance=behavioral::elements::state::machines::Transition_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::transition_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::Transition)

@given(instance=behavioral::elements::state::machines::Guard_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::guard_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::Guard)

@given(instance=behavioral::elements::common::behavior::Link_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::link_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Link)

@given(instance=behavioral::elements::activity::graphs::Partition_strategy)
@settings(max_examples=50)
def test_behavioral::elements::activity::graphs::partition_instantiation(instance):
    assert isinstance(instance, behavioral::elements::activity::graphs::Partition)

@given(instance=behavioral::elements::state::machines::StateMachine_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::statemachine_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::StateMachine)

@given(instance=behavioral::elements::state::machines::StateVertex_strategy)
@settings(max_examples=50)
def test_behavioral::elements::state::machines::statevertex_instantiation(instance):
    assert isinstance(instance, behavioral::elements::state::machines::StateVertex)

@given(instance=behavioral::elements::common::behavior::Instance_strategy)
@settings(max_examples=50)
def test_behavioral::elements::common::behavior::instance_instantiation(instance):
    assert isinstance(instance, behavioral::elements::common::behavior::Instance)
