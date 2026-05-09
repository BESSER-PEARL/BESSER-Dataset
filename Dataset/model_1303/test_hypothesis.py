import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachines::Behavior,
    Vertex,
    StateMachines::State,
    StateMachines::Pseudostate,
    StateMachines::Trigger,
    StateMachines::Transition,
    StateMachines::Vertex,
    State,
    StateMachines::FinalState,
    StateMachines::ConnectionPointReference,
    StateMachines::Region,
    StateMachines::StateMachine,
    PseudoStateKind,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines::behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Behavior)


def test_statemachines::behavior_constructor_exists():
    assert callable(StateMachines::Behavior.__init__)


def test_statemachines::behavior_constructor_args():
    sig = inspect.signature(StateMachines::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::state_is_not_abstract():
    assert not inspect.isabstract(StateMachines::State)


def test_statemachines::state_constructor_exists():
    assert callable(StateMachines::State.__init__)


def test_statemachines::state_constructor_args():
    sig = inspect.signature(StateMachines::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Pseudostate)


def test_statemachines::pseudostate_constructor_exists():
    assert callable(StateMachines::Pseudostate.__init__)


def test_statemachines::pseudostate_constructor_args():
    sig = inspect.signature(StateMachines::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines::pseudostate_has_kind():
    assert hasattr(StateMachines::Pseudostate, "kind")
    descriptor = None
    for klass in StateMachines::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Trigger)


def test_statemachines::trigger_constructor_exists():
    assert callable(StateMachines::Trigger.__init__)


def test_statemachines::trigger_constructor_args():
    sig = inspect.signature(StateMachines::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Transition)


def test_statemachines::transition_constructor_exists():
    assert callable(StateMachines::Transition.__init__)


def test_statemachines::transition_constructor_args():
    sig = inspect.signature(StateMachines::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines::transition_has_kind():
    assert hasattr(StateMachines::Transition, "kind")
    descriptor = None
    for klass in StateMachines::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Vertex)


def test_statemachines::vertex_constructor_exists():
    assert callable(StateMachines::Vertex.__init__)


def test_statemachines::vertex_constructor_args():
    sig = inspect.signature(StateMachines::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachines::FinalState)


def test_statemachines::finalstate_constructor_exists():
    assert callable(StateMachines::FinalState.__init__)


def test_statemachines::finalstate_constructor_args():
    sig = inspect.signature(StateMachines::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(StateMachines::ConnectionPointReference)


def test_statemachines::connectionpointreference_constructor_exists():
    assert callable(StateMachines::ConnectionPointReference.__init__)


def test_statemachines::connectionpointreference_constructor_args():
    sig = inspect.signature(StateMachines::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::region_is_not_abstract():
    assert not inspect.isabstract(StateMachines::Region)


def test_statemachines::region_constructor_exists():
    assert callable(StateMachines::Region.__init__)


def test_statemachines::region_constructor_args():
    sig = inspect.signature(StateMachines::Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines::StateMachine)


def test_statemachines::statemachine_constructor_exists():
    assert callable(StateMachines::StateMachine.__init__)


def test_statemachines::statemachine_constructor_args():
    sig = inspect.signature(StateMachines::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "deepHistory",
        "join",
        "exitPoint",
        "junction",
        "initial",
        "entryPoint",
        "fork",
        "shallowHistory",
        "choice",
        "terminate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
        "local",
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
StateMachines::Behavior_strategy = st.builds(
    StateMachines::Behavior,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachines::State_strategy = st.builds(
    StateMachines::State,
)
StateMachines::Pseudostate_strategy = st.builds(
    StateMachines::Pseudostate,
    kind=
        safe_text
)
StateMachines::Trigger_strategy = st.builds(
    StateMachines::Trigger,
)
StateMachines::Transition_strategy = st.builds(
    StateMachines::Transition,
    kind=
        safe_text
)
StateMachines::Vertex_strategy = st.builds(
    StateMachines::Vertex,
)
State_strategy = st.builds(
    State,
)
StateMachines::FinalState_strategy = st.builds(
    StateMachines::FinalState,
)
StateMachines::ConnectionPointReference_strategy = st.builds(
    StateMachines::ConnectionPointReference,
)
StateMachines::Region_strategy = st.builds(
    StateMachines::Region,
)
StateMachines::StateMachine_strategy = st.builds(
    StateMachines::StateMachine,
)

@given(instance=StateMachines::Behavior_strategy)
@settings(max_examples=50)
def test_statemachines::behavior_instantiation(instance):
    assert isinstance(instance, StateMachines::Behavior)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachines::State_strategy)
@settings(max_examples=50)
def test_statemachines::state_instantiation(instance):
    assert isinstance(instance, StateMachines::State)

@given(instance=StateMachines::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachines::Pseudostate)

@given(instance=StateMachines::Pseudostate_strategy)
def test_statemachines::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=StateMachines::Pseudostate_strategy)
def test_statemachines::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=StateMachines::Trigger_strategy)
@settings(max_examples=50)
def test_statemachines::trigger_instantiation(instance):
    assert isinstance(instance, StateMachines::Trigger)

@given(instance=StateMachines::Transition_strategy)
@settings(max_examples=50)
def test_statemachines::transition_instantiation(instance):
    assert isinstance(instance, StateMachines::Transition)

@given(instance=StateMachines::Transition_strategy)
def test_statemachines::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=StateMachines::Transition_strategy)
def test_statemachines::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=StateMachines::Vertex_strategy)
@settings(max_examples=50)
def test_statemachines::vertex_instantiation(instance):
    assert isinstance(instance, StateMachines::Vertex)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachines::FinalState_strategy)
@settings(max_examples=50)
def test_statemachines::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachines::FinalState)

@given(instance=StateMachines::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_statemachines::connectionpointreference_instantiation(instance):
    assert isinstance(instance, StateMachines::ConnectionPointReference)

@given(instance=StateMachines::Region_strategy)
@settings(max_examples=50)
def test_statemachines::region_instantiation(instance):
    assert isinstance(instance, StateMachines::Region)

@given(instance=StateMachines::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachines::StateMachine)
