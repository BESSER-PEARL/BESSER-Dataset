import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateMachines_ProtocolStateMachines_Operation,
    Operation,
    Classifier,
    StateMachines_ProtocolStateMachines_Interface,
    StateMachines_ProtocolStateMachines_Port,
    StateMachines_ProtocolStateMachines_DirectedRelationship,
    ProtocolStateMachine,
    DirectedRelationship,
    StateMachines_ProtocolStateMachines_ProtocolConformance,
    ProtocolConformance,
    ConnectionPointReference,
    BehaviorStateMachines_Vertex,
    StateMachines_BehaviorStateMachines_Trigger,
    StateMachines_BehaviorStateMachines_Constraint,
    StateMachines_BehaviorStateMachines_TimeEvent,
    StateMachines_BehaviorStateMachines_Classifier,
    StateMachines_BehaviorStateMachines_RedefinableElement,
    NamedElement,
    StateMachines_BehaviorStateMachines_Vertex,
    StateMachines_BehaviorStateMachines_NamedElement,
    Transition,
    StateMachines_ProtocolStateMachines_ProtocolTransition,
    Vertex,
    StateMachines_BehaviorStateMachines_Pseudostate,
    StateMachines_BehaviorStateMachines_ConnectionPointReference,
    BehaviorStateMachines_RedefinableElement,
    BehaviorStateMachines_Namespace,
    StateMachines_BehaviorStateMachines_State,
    StateMachines_BehaviorStateMachines_Region,
    StateMachines_BehaviorStateMachines_Namespace,
    StateMachine,
    StateMachines_ProtocolStateMachines_ProtocolStateMachine,
    State,
    StateMachines_BehaviorStateMachines_FinalState,
    Constraint,
    Trigger,
    StateMachines_BehaviorStateMachines_Transition,
    Pseudostate,
    Region,
    Behavior,
    StateMachines_BehaviorStateMachines_StateMachine,
    StateMachines_BehaviorStateMachines_Behavior,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines_protocolstatemachines_operation_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_Operation)


def test_statemachines_protocolstatemachines_operation_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_Operation.__init__)


def test_statemachines_protocolstatemachines_operation_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_Operation.__init__)
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



def test_statemachines_protocolstatemachines_interface_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_Interface)


def test_statemachines_protocolstatemachines_interface_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_Interface.__init__)


def test_statemachines_protocolstatemachines_interface_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_Interface.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_protocolstatemachines_port_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_Port)


def test_statemachines_protocolstatemachines_port_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_Port.__init__)


def test_statemachines_protocolstatemachines_port_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_Port.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_protocolstatemachines_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_DirectedRelationship)


def test_statemachines_protocolstatemachines_directedrelationship_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_DirectedRelationship.__init__)


def test_statemachines_protocolstatemachines_directedrelationship_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_DirectedRelationship.__init__)
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



def test_statemachines_protocolstatemachines_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_ProtocolConformance)


def test_statemachines_protocolstatemachines_protocolconformance_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_ProtocolConformance.__init__)


def test_statemachines_protocolstatemachines_protocolconformance_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_ProtocolConformance.__init__)
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



def test_behaviorstatemachines_vertex_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines_Vertex)


def test_behaviorstatemachines_vertex_constructor_exists():
    assert callable(BehaviorStateMachines_Vertex.__init__)


def test_behaviorstatemachines_vertex_constructor_args():
    sig = inspect.signature(BehaviorStateMachines_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Trigger)


def test_statemachines_behaviorstatemachines_trigger_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Trigger.__init__)


def test_statemachines_behaviorstatemachines_trigger_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_constraint_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Constraint)


def test_statemachines_behaviorstatemachines_constraint_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Constraint.__init__)


def test_statemachines_behaviorstatemachines_constraint_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_timeevent_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_TimeEvent)


def test_statemachines_behaviorstatemachines_timeevent_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_TimeEvent.__init__)


def test_statemachines_behaviorstatemachines_timeevent_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_classifier_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Classifier)


def test_statemachines_behaviorstatemachines_classifier_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Classifier.__init__)


def test_statemachines_behaviorstatemachines_classifier_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_RedefinableElement)


def test_statemachines_behaviorstatemachines_redefinableelement_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_RedefinableElement.__init__)


def test_statemachines_behaviorstatemachines_redefinableelement_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Vertex)


def test_statemachines_behaviorstatemachines_vertex_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Vertex.__init__)


def test_statemachines_behaviorstatemachines_vertex_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_namedelement_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_NamedElement)


def test_statemachines_behaviorstatemachines_namedelement_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_NamedElement.__init__)


def test_statemachines_behaviorstatemachines_namedelement_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_protocolstatemachines_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_ProtocolTransition)


def test_statemachines_protocolstatemachines_protocoltransition_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_ProtocolTransition.__init__)


def test_statemachines_protocolstatemachines_protocoltransition_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Pseudostate)


def test_statemachines_behaviorstatemachines_pseudostate_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Pseudostate.__init__)


def test_statemachines_behaviorstatemachines_pseudostate_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_ConnectionPointReference)


def test_statemachines_behaviorstatemachines_connectionpointreference_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_ConnectionPointReference.__init__)


def test_statemachines_behaviorstatemachines_connectionpointreference_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_behaviorstatemachines_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines_RedefinableElement)


def test_behaviorstatemachines_redefinableelement_constructor_exists():
    assert callable(BehaviorStateMachines_RedefinableElement.__init__)


def test_behaviorstatemachines_redefinableelement_constructor_args():
    sig = inspect.signature(BehaviorStateMachines_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviorstatemachines_namespace_is_not_abstract():
    assert not inspect.isabstract(BehaviorStateMachines_Namespace)


def test_behaviorstatemachines_namespace_constructor_exists():
    assert callable(BehaviorStateMachines_Namespace.__init__)


def test_behaviorstatemachines_namespace_constructor_args():
    sig = inspect.signature(BehaviorStateMachines_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_state_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_State)


def test_statemachines_behaviorstatemachines_state_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_State.__init__)


def test_statemachines_behaviorstatemachines_state_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"

def test_statemachines_behaviorstatemachines_state_has_isComposite():
    assert hasattr(StateMachines_BehaviorStateMachines_State, "isComposite")
    descriptor = None
    for klass in StateMachines_BehaviorStateMachines_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_behaviorstatemachines_state_has_isOrthogonal():
    assert hasattr(StateMachines_BehaviorStateMachines_State, "isOrthogonal")
    descriptor = None
    for klass in StateMachines_BehaviorStateMachines_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_behaviorstatemachines_state_has_isSubmachineState():
    assert hasattr(StateMachines_BehaviorStateMachines_State, "isSubmachineState")
    descriptor = None
    for klass in StateMachines_BehaviorStateMachines_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_behaviorstatemachines_state_has_isSimple():
    assert hasattr(StateMachines_BehaviorStateMachines_State, "isSimple")
    descriptor = None
    for klass in StateMachines_BehaviorStateMachines_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_behaviorstatemachines_region_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Region)


def test_statemachines_behaviorstatemachines_region_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Region.__init__)


def test_statemachines_behaviorstatemachines_region_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_namespace_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Namespace)


def test_statemachines_behaviorstatemachines_namespace_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Namespace.__init__)


def test_statemachines_behaviorstatemachines_namespace_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_protocolstatemachines_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ProtocolStateMachines_ProtocolStateMachine)


def test_statemachines_protocolstatemachines_protocolstatemachine_constructor_exists():
    assert callable(StateMachines_ProtocolStateMachines_ProtocolStateMachine.__init__)


def test_statemachines_protocolstatemachines_protocolstatemachine_constructor_args():
    sig = inspect.signature(StateMachines_ProtocolStateMachines_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_FinalState)


def test_statemachines_behaviorstatemachines_finalstate_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_FinalState.__init__)


def test_statemachines_behaviorstatemachines_finalstate_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_FinalState.__init__)
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



def test_statemachines_behaviorstatemachines_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Transition)


def test_statemachines_behaviorstatemachines_transition_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Transition.__init__)


def test_statemachines_behaviorstatemachines_transition_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines_behaviorstatemachines_transition_has_kind():
    assert hasattr(StateMachines_BehaviorStateMachines_Transition, "kind")
    descriptor = None
    for klass in StateMachines_BehaviorStateMachines_Transition.__mro__:
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



def test_statemachines_behaviorstatemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_StateMachine)


def test_statemachines_behaviorstatemachines_statemachine_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_StateMachine.__init__)


def test_statemachines_behaviorstatemachines_statemachine_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_behaviorstatemachines_behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachines_BehaviorStateMachines_Behavior)


def test_statemachines_behaviorstatemachines_behavior_constructor_exists():
    assert callable(StateMachines_BehaviorStateMachines_Behavior.__init__)


def test_statemachines_behaviorstatemachines_behavior_constructor_args():
    sig = inspect.signature(StateMachines_BehaviorStateMachines_Behavior.__init__)
    params = list(sig.parameters.keys())

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "internal",
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
StateMachines_ProtocolStateMachines_Operation_strategy = st.builds(
    StateMachines_ProtocolStateMachines_Operation,
)
Operation_strategy = st.builds(
    Operation,
)
Classifier_strategy = st.builds(
    Classifier,
)
StateMachines_ProtocolStateMachines_Interface_strategy = st.builds(
    StateMachines_ProtocolStateMachines_Interface,
)
StateMachines_ProtocolStateMachines_Port_strategy = st.builds(
    StateMachines_ProtocolStateMachines_Port,
)
StateMachines_ProtocolStateMachines_DirectedRelationship_strategy = st.builds(
    StateMachines_ProtocolStateMachines_DirectedRelationship,
)
ProtocolStateMachine_strategy = st.builds(
    ProtocolStateMachine,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
StateMachines_ProtocolStateMachines_ProtocolConformance_strategy = st.builds(
    StateMachines_ProtocolStateMachines_ProtocolConformance,
)
ProtocolConformance_strategy = st.builds(
    ProtocolConformance,
)
ConnectionPointReference_strategy = st.builds(
    ConnectionPointReference,
)
BehaviorStateMachines_Vertex_strategy = st.builds(
    BehaviorStateMachines_Vertex,
)
StateMachines_BehaviorStateMachines_Trigger_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Trigger,
)
StateMachines_BehaviorStateMachines_Constraint_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Constraint,
)
StateMachines_BehaviorStateMachines_TimeEvent_strategy = st.builds(
    StateMachines_BehaviorStateMachines_TimeEvent,
)
StateMachines_BehaviorStateMachines_Classifier_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Classifier,
)
StateMachines_BehaviorStateMachines_RedefinableElement_strategy = st.builds(
    StateMachines_BehaviorStateMachines_RedefinableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StateMachines_BehaviorStateMachines_Vertex_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Vertex,
)
StateMachines_BehaviorStateMachines_NamedElement_strategy = st.builds(
    StateMachines_BehaviorStateMachines_NamedElement,
)
Transition_strategy = st.builds(
    Transition,
)
StateMachines_ProtocolStateMachines_ProtocolTransition_strategy = st.builds(
    StateMachines_ProtocolStateMachines_ProtocolTransition,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachines_BehaviorStateMachines_Pseudostate_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Pseudostate,
)
StateMachines_BehaviorStateMachines_ConnectionPointReference_strategy = st.builds(
    StateMachines_BehaviorStateMachines_ConnectionPointReference,
)
BehaviorStateMachines_RedefinableElement_strategy = st.builds(
    BehaviorStateMachines_RedefinableElement,
)
BehaviorStateMachines_Namespace_strategy = st.builds(
    BehaviorStateMachines_Namespace,
)
StateMachines_BehaviorStateMachines_State_strategy = st.builds(
    StateMachines_BehaviorStateMachines_State,
    isComposite=
        st.booleans(),
    isOrthogonal=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isSimple=
        st.booleans()
)
StateMachines_BehaviorStateMachines_Region_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Region,
)
StateMachines_BehaviorStateMachines_Namespace_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Namespace,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
StateMachines_ProtocolStateMachines_ProtocolStateMachine_strategy = st.builds(
    StateMachines_ProtocolStateMachines_ProtocolStateMachine,
)
State_strategy = st.builds(
    State,
)
StateMachines_BehaviorStateMachines_FinalState_strategy = st.builds(
    StateMachines_BehaviorStateMachines_FinalState,
)
Constraint_strategy = st.builds(
    Constraint,
)
Trigger_strategy = st.builds(
    Trigger,
)
StateMachines_BehaviorStateMachines_Transition_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Transition,
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
StateMachines_BehaviorStateMachines_StateMachine_strategy = st.builds(
    StateMachines_BehaviorStateMachines_StateMachine,
)
StateMachines_BehaviorStateMachines_Behavior_strategy = st.builds(
    StateMachines_BehaviorStateMachines_Behavior,
)

@given(instance=StateMachines_ProtocolStateMachines_Operation_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_operation_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=StateMachines_ProtocolStateMachines_Interface_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_interface_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_Interface)

@given(instance=StateMachines_ProtocolStateMachines_Port_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_port_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_Port)

@given(instance=StateMachines_ProtocolStateMachines_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_directedrelationship_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_DirectedRelationship)

@given(instance=ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, ProtocolStateMachine)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=StateMachines_ProtocolStateMachines_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_protocolconformance_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_ProtocolConformance)

@given(instance=ProtocolConformance_strategy)
@settings(max_examples=50)
def test_protocolconformance_instantiation(instance):
    assert isinstance(instance, ProtocolConformance)

@given(instance=ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_connectionpointreference_instantiation(instance):
    assert isinstance(instance, ConnectionPointReference)

@given(instance=BehaviorStateMachines_Vertex_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines_vertex_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines_Vertex)

@given(instance=StateMachines_BehaviorStateMachines_Trigger_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_trigger_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Trigger)

@given(instance=StateMachines_BehaviorStateMachines_Constraint_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_constraint_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Constraint)

@given(instance=StateMachines_BehaviorStateMachines_TimeEvent_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_timeevent_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_TimeEvent)

@given(instance=StateMachines_BehaviorStateMachines_Classifier_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_classifier_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Classifier)

@given(instance=StateMachines_BehaviorStateMachines_RedefinableElement_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_redefinableelement_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_RedefinableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StateMachines_BehaviorStateMachines_Vertex_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_vertex_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Vertex)

@given(instance=StateMachines_BehaviorStateMachines_NamedElement_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_namedelement_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_NamedElement)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=StateMachines_ProtocolStateMachines_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_protocoltransition_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_ProtocolTransition)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachines_BehaviorStateMachines_Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Pseudostate)

@given(instance=StateMachines_BehaviorStateMachines_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_connectionpointreference_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_ConnectionPointReference)

@given(instance=BehaviorStateMachines_RedefinableElement_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines_redefinableelement_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines_RedefinableElement)

@given(instance=BehaviorStateMachines_Namespace_strategy)
@settings(max_examples=50)
def test_behaviorstatemachines_namespace_instantiation(instance):
    assert isinstance(instance, BehaviorStateMachines_Namespace)

@given(instance=StateMachines_BehaviorStateMachines_State_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_state_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_State)



@given(instance=StateMachines_BehaviorStateMachines_State_strategy)
def test_statemachines_behaviorstatemachines_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=StateMachines_BehaviorStateMachines_State_strategy)
def test_statemachines_behaviorstatemachines_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=StateMachines_BehaviorStateMachines_State_strategy)
def test_statemachines_behaviorstatemachines_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original



@given(instance=StateMachines_BehaviorStateMachines_State_strategy)
def test_statemachines_behaviorstatemachines_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=StateMachines_BehaviorStateMachines_Region_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_region_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Region)

@given(instance=StateMachines_BehaviorStateMachines_Namespace_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_namespace_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Namespace)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=StateMachines_ProtocolStateMachines_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_statemachines_protocolstatemachines_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, StateMachines_ProtocolStateMachines_ProtocolStateMachine)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachines_BehaviorStateMachines_FinalState_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_finalstate_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_FinalState)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=StateMachines_BehaviorStateMachines_Transition_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_transition_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Transition)



@given(instance=StateMachines_BehaviorStateMachines_Transition_strategy)
def test_statemachines_behaviorstatemachines_transition_kind_setter(instance):
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

@given(instance=StateMachines_BehaviorStateMachines_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_StateMachine)

@given(instance=StateMachines_BehaviorStateMachines_Behavior_strategy)
@settings(max_examples=50)
def test_statemachines_behaviorstatemachines_behavior_instantiation(instance):
    assert isinstance(instance, StateMachines_BehaviorStateMachines_Behavior)
