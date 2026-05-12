import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateMachines_Behavior,
    Vertex,
    StateMachines_State,
    StateMachines_Pseudostate,
    StateMachines_Trigger,
    StateMachines_Transition,
    StateMachines_Vertex,
    State,
    StateMachines_FinalState,
    StateMachines_ConnectionPointReference,
    StateMachines_Region,
    StateMachines_StateMachine,
    TransitionKind,
    PseudoStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines_behavior_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Behavior)


def test_statemachines_behavior_constructor_exists():
    assert callable(StateMachines_Behavior.__init__)


def test_statemachines_behavior_constructor_args():
    sig = inspect.signature(StateMachines_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_state_is_not_abstract():
    assert not inspect.isabstract(StateMachines_State)


def test_statemachines_state_constructor_exists():
    assert callable(StateMachines_State.__init__)


def test_statemachines_state_constructor_args():
    sig = inspect.signature(StateMachines_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Pseudostate)


def test_statemachines_pseudostate_constructor_exists():
    assert callable(StateMachines_Pseudostate.__init__)


def test_statemachines_pseudostate_constructor_args():
    sig = inspect.signature(StateMachines_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines_pseudostate_has_kind():
    assert hasattr(StateMachines_Pseudostate, "kind")
    descriptor = None
    for klass in StateMachines_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Trigger)


def test_statemachines_trigger_constructor_exists():
    assert callable(StateMachines_Trigger.__init__)


def test_statemachines_trigger_constructor_args():
    sig = inspect.signature(StateMachines_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Transition)


def test_statemachines_transition_constructor_exists():
    assert callable(StateMachines_Transition.__init__)


def test_statemachines_transition_constructor_args():
    sig = inspect.signature(StateMachines_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines_transition_has_kind():
    assert hasattr(StateMachines_Transition, "kind")
    descriptor = None
    for klass in StateMachines_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Vertex)


def test_statemachines_vertex_constructor_exists():
    assert callable(StateMachines_Vertex.__init__)


def test_statemachines_vertex_constructor_args():
    sig = inspect.signature(StateMachines_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachines_FinalState)


def test_statemachines_finalstate_constructor_exists():
    assert callable(StateMachines_FinalState.__init__)


def test_statemachines_finalstate_constructor_args():
    sig = inspect.signature(StateMachines_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(StateMachines_ConnectionPointReference)


def test_statemachines_connectionpointreference_constructor_exists():
    assert callable(StateMachines_ConnectionPointReference.__init__)


def test_statemachines_connectionpointreference_constructor_args():
    sig = inspect.signature(StateMachines_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_region_is_not_abstract():
    assert not inspect.isabstract(StateMachines_Region)


def test_statemachines_region_constructor_exists():
    assert callable(StateMachines_Region.__init__)


def test_statemachines_region_constructor_args():
    sig = inspect.signature(StateMachines_Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachines_StateMachine)


def test_statemachines_statemachine_constructor_exists():
    assert callable(StateMachines_StateMachine.__init__)


def test_statemachines_statemachine_constructor_args():
    sig = inspect.signature(StateMachines_StateMachine.__init__)
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
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "choice",
        "initial",
        "junction",
        "terminate",
        "fork",
        "entryPoint",
        "join",
        "exitPoint",
        "shallowHistory",
        "deepHistory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"


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
StateMachines_Behavior_strategy = st.builds(
    StateMachines_Behavior,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachines_State_strategy = st.builds(
    StateMachines_State,
)
StateMachines_Pseudostate_strategy = st.builds(
    StateMachines_Pseudostate,
    kind=
        safe_text
)
StateMachines_Trigger_strategy = st.builds(
    StateMachines_Trigger,
)
StateMachines_Transition_strategy = st.builds(
    StateMachines_Transition,
    kind=
        safe_text
)
StateMachines_Vertex_strategy = st.builds(
    StateMachines_Vertex,
)
State_strategy = st.builds(
    State,
)
StateMachines_FinalState_strategy = st.builds(
    StateMachines_FinalState,
)
StateMachines_ConnectionPointReference_strategy = st.builds(
    StateMachines_ConnectionPointReference,
)
StateMachines_Region_strategy = st.builds(
    StateMachines_Region,
)
StateMachines_StateMachine_strategy = st.builds(
    StateMachines_StateMachine,
)

@given(instance=StateMachines_Behavior_strategy)
@settings(max_examples=50)
def test_statemachines_behavior_instantiation(instance):
    assert isinstance(instance, StateMachines_Behavior)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachines_State_strategy)
@settings(max_examples=50)
def test_statemachines_state_instantiation(instance):
    assert isinstance(instance, StateMachines_State)

@given(instance=StateMachines_Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines_pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachines_Pseudostate)



@given(instance=StateMachines_Pseudostate_strategy)
def test_statemachines_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=StateMachines_Trigger_strategy)
@settings(max_examples=50)
def test_statemachines_trigger_instantiation(instance):
    assert isinstance(instance, StateMachines_Trigger)

@given(instance=StateMachines_Transition_strategy)
@settings(max_examples=50)
def test_statemachines_transition_instantiation(instance):
    assert isinstance(instance, StateMachines_Transition)



@given(instance=StateMachines_Transition_strategy)
def test_statemachines_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=StateMachines_Vertex_strategy)
@settings(max_examples=50)
def test_statemachines_vertex_instantiation(instance):
    assert isinstance(instance, StateMachines_Vertex)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachines_FinalState_strategy)
@settings(max_examples=50)
def test_statemachines_finalstate_instantiation(instance):
    assert isinstance(instance, StateMachines_FinalState)

@given(instance=StateMachines_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_statemachines_connectionpointreference_instantiation(instance):
    assert isinstance(instance, StateMachines_ConnectionPointReference)

@given(instance=StateMachines_Region_strategy)
@settings(max_examples=50)
def test_statemachines_region_instantiation(instance):
    assert isinstance(instance, StateMachines_Region)

@given(instance=StateMachines_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachines_StateMachine)
