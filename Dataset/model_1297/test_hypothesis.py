import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Vertex,
    Transition,
    StateMachinesProv::ProtocolTransition,
    StateMachinesProv::ProtocolConformance,
    StateMachine,
    StateMachinesProv::ProtocolStateMachine,
    StateMachinesProv::TimeEvent,
    State,
    StateMachinesProv::FinalState,
    StateMachinesProv::ConnectionPointReference,
    StateMachinesProv::Transition,
    StateMachinesProv::Vertex,
    StateMachinesProv::State,
    StateMachinesProv::Pseudostate,
    StateMachinesProv::Region,
    StateMachinesProv::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::ProtocolTransition)


def test_statemachinesprov::protocoltransition_constructor_exists():
    assert callable(StateMachinesProv::ProtocolTransition.__init__)


def test_statemachinesprov::protocoltransition_constructor_args():
    sig = inspect.signature(StateMachinesProv::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::ProtocolConformance)


def test_statemachinesprov::protocolconformance_constructor_exists():
    assert callable(StateMachinesProv::ProtocolConformance.__init__)


def test_statemachinesprov::protocolconformance_constructor_args():
    sig = inspect.signature(StateMachinesProv::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::ProtocolStateMachine)


def test_statemachinesprov::protocolstatemachine_constructor_exists():
    assert callable(StateMachinesProv::ProtocolStateMachine.__init__)


def test_statemachinesprov::protocolstatemachine_constructor_args():
    sig = inspect.signature(StateMachinesProv::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::timeevent_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::TimeEvent)


def test_statemachinesprov::timeevent_constructor_exists():
    assert callable(StateMachinesProv::TimeEvent.__init__)


def test_statemachinesprov::timeevent_constructor_args():
    sig = inspect.signature(StateMachinesProv::TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::FinalState)


def test_statemachinesprov::finalstate_constructor_exists():
    assert callable(StateMachinesProv::FinalState.__init__)


def test_statemachinesprov::finalstate_constructor_args():
    sig = inspect.signature(StateMachinesProv::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::ConnectionPointReference)


def test_statemachinesprov::connectionpointreference_constructor_exists():
    assert callable(StateMachinesProv::ConnectionPointReference.__init__)


def test_statemachinesprov::connectionpointreference_constructor_args():
    sig = inspect.signature(StateMachinesProv::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::Transition)


def test_statemachinesprov::transition_constructor_exists():
    assert callable(StateMachinesProv::Transition.__init__)


def test_statemachinesprov::transition_constructor_args():
    sig = inspect.signature(StateMachinesProv::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::Vertex)


def test_statemachinesprov::vertex_constructor_exists():
    assert callable(StateMachinesProv::Vertex.__init__)


def test_statemachinesprov::vertex_constructor_args():
    sig = inspect.signature(StateMachinesProv::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::state_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::State)


def test_statemachinesprov::state_constructor_exists():
    assert callable(StateMachinesProv::State.__init__)


def test_statemachinesprov::state_constructor_args():
    sig = inspect.signature(StateMachinesProv::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"

def test_statemachinesprov::state_has_isComposite():
    assert hasattr(StateMachinesProv::State, "isComposite")
    descriptor = None
    for klass in StateMachinesProv::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_statemachinesprov::state_has_isOrthogonal():
    assert hasattr(StateMachinesProv::State, "isOrthogonal")
    descriptor = None
    for klass in StateMachinesProv::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_statemachinesprov::state_has_isSimple():
    assert hasattr(StateMachinesProv::State, "isSimple")
    descriptor = None
    for klass in StateMachinesProv::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_statemachinesprov::state_has_isSubmachineState():
    assert hasattr(StateMachinesProv::State, "isSubmachineState")
    descriptor = None
    for klass in StateMachinesProv::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)



def test_statemachinesprov::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::Pseudostate)


def test_statemachinesprov::pseudostate_constructor_exists():
    assert callable(StateMachinesProv::Pseudostate.__init__)


def test_statemachinesprov::pseudostate_constructor_args():
    sig = inspect.signature(StateMachinesProv::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::region_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::Region)


def test_statemachinesprov::region_constructor_exists():
    assert callable(StateMachinesProv::Region.__init__)


def test_statemachinesprov::region_constructor_args():
    sig = inspect.signature(StateMachinesProv::Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesprov::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachinesProv::StateMachine)


def test_statemachinesprov::statemachine_constructor_exists():
    assert callable(StateMachinesProv::StateMachine.__init__)


def test_statemachinesprov::statemachine_constructor_args():
    sig = inspect.signature(StateMachinesProv::StateMachine.__init__)
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
Vertex_strategy = st.builds(
    Vertex,
)
Transition_strategy = st.builds(
    Transition,
)
StateMachinesProv::ProtocolTransition_strategy = st.builds(
    StateMachinesProv::ProtocolTransition,
)
StateMachinesProv::ProtocolConformance_strategy = st.builds(
    StateMachinesProv::ProtocolConformance,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
StateMachinesProv::ProtocolStateMachine_strategy = st.builds(
    StateMachinesProv::ProtocolStateMachine,
)
StateMachinesProv::TimeEvent_strategy = st.builds(
    StateMachinesProv::TimeEvent,
)
State_strategy = st.builds(
    State,
)
StateMachinesProv::FinalState_strategy = st.builds(
    StateMachinesProv::FinalState,
)
StateMachinesProv::ConnectionPointReference_strategy = st.builds(
    StateMachinesProv::ConnectionPointReference,
)
StateMachinesProv::Transition_strategy = st.builds(
    StateMachinesProv::Transition,
)
StateMachinesProv::Vertex_strategy = st.builds(
    StateMachinesProv::Vertex,
)
StateMachinesProv::State_strategy = st.builds(
    StateMachinesProv::State,
    isComposite=
        st.booleans(),
    isOrthogonal=
        st.booleans(),
    isSimple=
        st.booleans(),
    isSubmachineState=
        st.booleans()
)
StateMachinesProv::Pseudostate_strategy = st.builds(
    StateMachinesProv::Pseudostate,
)
StateMachinesProv::Region_strategy = st.builds(
    StateMachinesProv::Region,
)
StateMachinesProv::StateMachine_strategy = st.builds(
    StateMachinesProv::StateMachine,
)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=StateMachinesProv::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_statemachinesprov::protocoltransition_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::ProtocolTransition)

@given(instance=StateMachinesProv::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_statemachinesprov::protocolconformance_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::ProtocolConformance)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=StateMachinesProv::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_statemachinesprov::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::ProtocolStateMachine)

@given(instance=StateMachinesProv::TimeEvent_strategy)
@settings(max_examples=50)
def test_statemachinesprov::timeevent_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::TimeEvent)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachinesProv::FinalState_strategy)
@settings(max_examples=50)
def test_statemachinesprov::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::FinalState)

@given(instance=StateMachinesProv::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_statemachinesprov::connectionpointreference_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::ConnectionPointReference)

@given(instance=StateMachinesProv::Transition_strategy)
@settings(max_examples=50)
def test_statemachinesprov::transition_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::Transition)

@given(instance=StateMachinesProv::Vertex_strategy)
@settings(max_examples=50)
def test_statemachinesprov::vertex_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::Vertex)

@given(instance=StateMachinesProv::State_strategy)
@settings(max_examples=50)
def test_statemachinesprov::state_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::State)

@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, bool)


@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, bool)


@given(instance=StateMachinesProv::State_strategy)
def test_statemachinesprov::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=StateMachinesProv::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachinesprov::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::Pseudostate)

@given(instance=StateMachinesProv::Region_strategy)
@settings(max_examples=50)
def test_statemachinesprov::region_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::Region)

@given(instance=StateMachinesProv::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinesprov::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachinesProv::StateMachine)
