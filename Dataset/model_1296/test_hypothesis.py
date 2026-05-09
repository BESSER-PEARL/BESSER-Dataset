import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachines::ProtocolStateMachines::Operation,
    Operation,
    Classifier,
    StateMachines::ProtocolStateMachines::Interface,
    StateMachines::ProtocolStateMachines::Port,
    StateMachines::ProtocolStateMachines::DirectedRelationship,
    ProtocolStateMachine,
    DirectedRelationship,
    StateMachines::ProtocolStateMachines::ProtocolConformance,
    ProtocolConformance,
    ConnectionPointReference,
    BehaviorStateMachines::Vertex,
    StateMachines::BehaviorStateMachines::Trigger,
    StateMachines::BehaviorStateMachines::Constraint,
    StateMachines::BehaviorStateMachines::TimeEvent,
    StateMachines::BehaviorStateMachines::Classifier,
    StateMachines::BehaviorStateMachines::RedefinableElement,
    NamedElement,
    StateMachines::BehaviorStateMachines::Vertex,
    StateMachines::BehaviorStateMachines::NamedElement,
    Transition,
    StateMachines::ProtocolStateMachines::ProtocolTransition,
    Vertex,
    StateMachines::BehaviorStateMachines::ConnectionPointReference,
    StateMachines::BehaviorStateMachines::Pseudostate,
    BehaviorStateMachines::RedefinableElement,
    BehaviorStateMachines::Namespace,
    StateMachines::BehaviorStateMachines::State,
    StateMachines::BehaviorStateMachines::Region,
    StateMachines::BehaviorStateMachines::Namespace,
    StateMachine,
    StateMachines::ProtocolStateMachines::ProtocolStateMachine,
    State,
    StateMachines::BehaviorStateMachines::FinalState,
    Constraint,
    Trigger,
    StateMachines::BehaviorStateMachines::Transition,
    Pseudostate,
    Region,
    Behavior,
    StateMachines::BehaviorStateMachines::StateMachine,
    StateMachines::BehaviorStateMachines::Behavior,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines::protocolstatemachines::operation_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::Operation)


def test_statemachines::protocolstatemachines::operation_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::Operation.__init__)


def test_statemachines::protocolstatemachines::operation_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::Operation.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::interface_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::Interface)


def test_statemachines::protocolstatemachines::interface_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::Interface.__init__)


def test_statemachines::protocolstatemachines::interface_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::Interface.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::port_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::Port)


def test_statemachines::protocolstatemachines::port_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::Port.__init__)


def test_statemachines::protocolstatemachines::port_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::Port.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::DirectedRelationship)


def test_statemachines::protocolstatemachines::directedrelationship_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::DirectedRelationship.__init__)


def test_statemachines::protocolstatemachines::directedrelationship_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(ProtocolStateMachine)


def test_protocolstatemachine_constructor_exists():
    assert callable(ProtocolStateMachine.__init__)


def test_protocolstatemachine_constructor_args():
    sig = inspect.signature(ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::ProtocolConformance)


def test_statemachines::protocolstatemachines::protocolconformance_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::ProtocolConformance.__init__)


def test_statemachines::protocolstatemachines::protocolconformance_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(ProtocolConformance)


def test_protocolconformance_constructor_exists():
    assert callable(ProtocolConformance.__init__)


def test_protocolconformance_constructor_args():
    sig = inspect.signature(ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(ConnectionPointReference)


def test_connectionpointreference_constructor_exists():
    assert callable(ConnectionPointReference.__init__)


def test_connectionpointreference_constructor_args():
    sig = inspect.signature(ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_behaviorstatemachines::vertex_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines::Vertex)


def test_behaviorstatemachines::vertex_constructor_exists():
    assert callable(BehaviorStateMachines::Vertex.__init__)


def test_behaviorstatemachines::vertex_constructor_args():
    sig = inspect.signature(BehaviorStateMachines::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Trigger)


def test_statemachines::behaviorstatemachines::trigger_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Trigger.__init__)


def test_statemachines::behaviorstatemachines::trigger_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::constraint_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Constraint)


def test_statemachines::behaviorstatemachines::constraint_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Constraint.__init__)


def test_statemachines::behaviorstatemachines::constraint_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::timeevent_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::TimeEvent)


def test_statemachines::behaviorstatemachines::timeevent_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::TimeEvent.__init__)


def test_statemachines::behaviorstatemachines::timeevent_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::classifier_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Classifier)


def test_statemachines::behaviorstatemachines::classifier_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Classifier.__init__)


def test_statemachines::behaviorstatemachines::classifier_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::RedefinableElement)


def test_statemachines::behaviorstatemachines::redefinableelement_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::RedefinableElement.__init__)


def test_statemachines::behaviorstatemachines::redefinableelement_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Vertex)


def test_statemachines::behaviorstatemachines::vertex_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Vertex.__init__)


def test_statemachines::behaviorstatemachines::vertex_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::namedelement_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::NamedElement)


def test_statemachines::behaviorstatemachines::namedelement_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::NamedElement.__init__)


def test_statemachines::behaviorstatemachines::namedelement_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::ProtocolTransition)


def test_statemachines::protocolstatemachines::protocoltransition_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::ProtocolTransition.__init__)


def test_statemachines::protocolstatemachines::protocoltransition_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::ConnectionPointReference)


def test_statemachines::behaviorstatemachines::connectionpointreference_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::ConnectionPointReference.__init__)


def test_statemachines::behaviorstatemachines::connectionpointreference_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Pseudostate)


def test_statemachines::behaviorstatemachines::pseudostate_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Pseudostate.__init__)


def test_statemachines::behaviorstatemachines::pseudostate_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_behaviorstatemachines::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines::RedefinableElement)


def test_behaviorstatemachines::redefinableelement_constructor_exists():
    assert callable(BehaviorStateMachines::RedefinableElement.__init__)


def test_behaviorstatemachines::redefinableelement_constructor_args():
    sig = inspect.signature(BehaviorStateMachines::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviorstatemachines::namespace_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines::Namespace)


def test_behaviorstatemachines::namespace_constructor_exists():
    assert callable(BehaviorStateMachines::Namespace.__init__)


def test_behaviorstatemachines::namespace_constructor_args():
    sig = inspect.signature(BehaviorStateMachines::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::state_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::State)


def test_statemachines::behaviorstatemachines::state_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::State.__init__)


def test_statemachines::behaviorstatemachines::state_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"

def test_statemachines::behaviorstatemachines::state_has_isComposite():
    assert hasattr(StateMachines::BehaviorStateMachines::State, "isComposite")
    descriptor = None
    for klass in StateMachines::BehaviorStateMachines::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_statemachines::behaviorstatemachines::state_has_isSubmachineState():
    assert hasattr(StateMachines::BehaviorStateMachines::State, "isSubmachineState")
    descriptor = None
    for klass in StateMachines::BehaviorStateMachines::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_statemachines::behaviorstatemachines::state_has_isOrthogonal():
    assert hasattr(StateMachines::BehaviorStateMachines::State, "isOrthogonal")
    descriptor = None
    for klass in StateMachines::BehaviorStateMachines::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_statemachines::behaviorstatemachines::state_has_isSimple():
    assert hasattr(StateMachines::BehaviorStateMachines::State, "isSimple")
    descriptor = None
    for klass in StateMachines::BehaviorStateMachines::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::behaviorstatemachines::region_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Region)


def test_statemachines::behaviorstatemachines::region_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Region.__init__)


def test_statemachines::behaviorstatemachines::region_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::namespace_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Namespace)


def test_statemachines::behaviorstatemachines::namespace_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Namespace.__init__)


def test_statemachines::behaviorstatemachines::namespace_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::protocolstatemachines::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ProtocolStateMachines::ProtocolStateMachine)


def test_statemachines::protocolstatemachines::protocolstatemachine_constructor_exists():
    assert callable(StateMachines::ProtocolStateMachines::ProtocolStateMachine.__init__)


def test_statemachines::protocolstatemachines::protocolstatemachine_constructor_args():
    sig = inspect.signature(StateMachines::ProtocolStateMachines::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::FinalState)


def test_statemachines::behaviorstatemachines::finalstate_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::FinalState.__init__)


def test_statemachines::behaviorstatemachines::finalstate_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Transition)


def test_statemachines::behaviorstatemachines::transition_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Transition.__init__)


def test_statemachines::behaviorstatemachines::transition_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines::behaviorstatemachines::transition_has_kind():
    assert hasattr(StateMachines::BehaviorStateMachines::Transition, "kind")
    descriptor = None
    for klass in StateMachines::BehaviorStateMachines::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::StateMachine)


def test_statemachines::behaviorstatemachines::statemachine_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::StateMachine.__init__)


def test_statemachines::behaviorstatemachines::statemachine_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::behaviorstatemachines::behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachines::BehaviorStateMachines::Behavior)


def test_statemachines::behaviorstatemachines::behavior_constructor_exists():
    assert callable(StateMachines::BehaviorStateMachines::Behavior.__init__)


def test_statemachines::behaviorstatemachines::behavior_constructor_args():
    sig = inspect.signature(StateMachines::BehaviorStateMachines::Behavior.__init__)
    params = list(sig.parameters.keys())

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"


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
StateMachines::ProtocolStateMachines::Operation_strategy = st.builds(
    StateMachines::ProtocolStateMachines::Operation,
)
Operation_strategy = st.builds(
    Operation,
)
Classifier_strategy = st.builds(
    Classifier,
)
StateMachines::ProtocolStateMachines::Interface_strategy = st.builds(
    StateMachines::ProtocolStateMachines::Interface,
)
StateMachines::ProtocolStateMachines::Port_strategy = st.builds(
    StateMachines::ProtocolStateMachines::Port,
)
StateMachines::ProtocolStateMachines::DirectedRelationship_strategy = st.builds(
    StateMachines::ProtocolStateMachines::DirectedRelationship,
)
ProtocolStateMachine_strategy = st.builds(
    ProtocolStateMachine,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
StateMachines::ProtocolStateMachines::ProtocolConformance_strategy = st.builds(
    StateMachines::ProtocolStateMachines::ProtocolConformance,
)
ProtocolConformance_strategy = st.builds(
    ProtocolConformance,
)
ConnectionPointReference_strategy = st.builds(
    ConnectionPointReference,
)
BehaviorStateMachines::Vertex_strategy = st.builds(
    BehaviorStateMachines::Vertex,
)
StateMachines::BehaviorStateMachines::Trigger_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Trigger,
)
StateMachines::BehaviorStateMachines::Constraint_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Constraint,
)
StateMachines::BehaviorStateMachines::TimeEvent_strategy = st.builds(
    StateMachines::BehaviorStateMachines::TimeEvent,
)
StateMachines::BehaviorStateMachines::Classifier_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Classifier,
)
StateMachines::BehaviorStateMachines::RedefinableElement_strategy = st.builds(
    StateMachines::BehaviorStateMachines::RedefinableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StateMachines::BehaviorStateMachines::Vertex_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Vertex,
)
StateMachines::BehaviorStateMachines::NamedElement_strategy = st.builds(
    StateMachines::BehaviorStateMachines::NamedElement,
)
Transition_strategy = st.builds(
    Transition,
)
StateMachines::ProtocolStateMachines::ProtocolTransition_strategy = st.builds(
    StateMachines::ProtocolStateMachines::ProtocolTransition,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachines::BehaviorStateMachines::ConnectionPointReference_strategy = st.builds(
    StateMachines::BehaviorStateMachines::ConnectionPointReference,
)
StateMachines::BehaviorStateMachines::Pseudostate_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Pseudostate,
)
BehaviorStateMachines::RedefinableElement_strategy = st.builds(
    BehaviorStateMachines::RedefinableElement,
)
BehaviorStateMachines::Namespace_strategy = st.builds(
    BehaviorStateMachines::Namespace,
)
StateMachines::BehaviorStateMachines::State_strategy = st.builds(
    StateMachines::BehaviorStateMachines::State,
    isComposite=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isOrthogonal=
        st.booleans(),
    isSimple=
        st.booleans()
)
StateMachines::BehaviorStateMachines::Region_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Region,
)
StateMachines::BehaviorStateMachines::Namespace_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Namespace,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
StateMachines::ProtocolStateMachines::ProtocolStateMachine_strategy = st.builds(
    StateMachines::ProtocolStateMachines::ProtocolStateMachine,
)
State_strategy = st.builds(
    State,
)
StateMachines::BehaviorStateMachines::FinalState_strategy = st.builds(
    StateMachines::BehaviorStateMachines::FinalState,
)
Constraint_strategy = st.builds(
    Constraint,
)
Trigger_strategy = st.builds(
    Trigger,
)
StateMachines::BehaviorStateMachines::Transition_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Transition,
    kind=
        safe_text
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
Region_strategy = st.builds(
    Region,
)
Behavior_strategy = st.builds(
    Behavior,
)
StateMachines::BehaviorStateMachines::StateMachine_strategy = st.builds(
    StateMachines::BehaviorStateMachines::StateMachine,
)
StateMachines::BehaviorStateMachines::Behavior_strategy = st.builds(
    StateMachines::BehaviorStateMachines::Behavior,
)

@given(instance=StateMachines::ProtocolStateMachines::Operation_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::operation_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=StateMachines::ProtocolStateMachines::Interface_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::interface_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::Interface)

@given(instance=StateMachines::ProtocolStateMachines::Port_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::port_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::Port)

@given(instance=StateMachines::ProtocolStateMachines::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::directedrelationship_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::DirectedRelationship)

@given(instance=ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, ProtocolStateMachine)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=StateMachines::ProtocolStateMachines::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::protocolconformance_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::ProtocolConformance)

@given(instance=ProtocolConformance_strategy)
@settings(max_examples=50)
def test_protocolconformance_instantiation(instance):
    assert isinstance(instance, ProtocolConformance)

@given(instance=ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_connectionpointreference_instantiation(instance):
    assert isinstance(instance, ConnectionPointReference)

@given(instance=BehaviorStateMachines::Vertex_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines::vertex_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines::Vertex)

@given(instance=StateMachines::BehaviorStateMachines::Trigger_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::trigger_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Trigger)

@given(instance=StateMachines::BehaviorStateMachines::Constraint_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::constraint_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Constraint)

@given(instance=StateMachines::BehaviorStateMachines::TimeEvent_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::timeevent_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::TimeEvent)

@given(instance=StateMachines::BehaviorStateMachines::Classifier_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::classifier_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Classifier)

@given(instance=StateMachines::BehaviorStateMachines::RedefinableElement_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::redefinableelement_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::RedefinableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StateMachines::BehaviorStateMachines::Vertex_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::vertex_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Vertex)

@given(instance=StateMachines::BehaviorStateMachines::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::namedelement_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::NamedElement)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=StateMachines::ProtocolStateMachines::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::protocoltransition_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::ProtocolTransition)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachines::BehaviorStateMachines::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::connectionpointreference_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::ConnectionPointReference)

@given(instance=StateMachines::BehaviorStateMachines::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Pseudostate)

@given(instance=BehaviorStateMachines::RedefinableElement_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines::redefinableelement_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines::RedefinableElement)

@given(instance=BehaviorStateMachines::Namespace_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines::namespace_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines::Namespace)

@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::state_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::State)

@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, bool)


@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, bool)


@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=StateMachines::BehaviorStateMachines::State_strategy)
def test_statemachines::behaviorstatemachines::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=StateMachines::BehaviorStateMachines::Region_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::region_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Region)

@given(instance=StateMachines::BehaviorStateMachines::Namespace_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::namespace_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Namespace)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=StateMachines::ProtocolStateMachines::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_statemachines::protocolstatemachines::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, StateMachines::ProtocolStateMachines::ProtocolStateMachine)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachines::BehaviorStateMachines::FinalState_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::FinalState)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=StateMachines::BehaviorStateMachines::Transition_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::transition_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Transition)

@given(instance=StateMachines::BehaviorStateMachines::Transition_strategy)
def test_statemachines::behaviorstatemachines::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=StateMachines::BehaviorStateMachines::Transition_strategy)
def test_statemachines::behaviorstatemachines::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=StateMachines::BehaviorStateMachines::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::StateMachine)

@given(instance=StateMachines::BehaviorStateMachines::Behavior_strategy)
@settings(max_examples=50)
def test_statemachines::behaviorstatemachines::behavior_instantiation(instance):
    assert isinstance(instance, StateMachines::BehaviorStateMachines::Behavior)
