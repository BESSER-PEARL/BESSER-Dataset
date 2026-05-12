import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IDElement,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_IDElement,
    stateMachine_Event,
    stateMachine_Transition,
    StateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idelement_is_not_abstract():
    assert not inspect.isabstract(IDElement)


def test_idelement_constructor_exists():
    assert callable(IDElement.__init__)


def test_idelement_constructor_args():
    sig = inspect.signature(IDElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine_state_has_kind():
    assert hasattr(stateMachine_State, "kind")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_idelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine_IDElement)


def test_statemachine_idelement_constructor_exists():
    assert callable(stateMachine_IDElement.__init__)


def test_statemachine_idelement_constructor_args():
    sig = inspect.signature(stateMachine_IDElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_idelement_has_id():
    assert hasattr(stateMachine_IDElement, "id")
    descriptor = None
    for klass in stateMachine_IDElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(stateMachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(stateMachine_Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(stateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(stateMachine_Transition.__init__)
    params = list(sig.parameters.keys())

def test_statekind_exists():
    # Check that the Enumeration exists
    assert StateKind is not None

def test_statekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateKind]
    expected_literals = [
        "INITIAL",
        "FINAL",
        "DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateKind"


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
IDElement_strategy = st.builds(
    IDElement,
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    kind=
        safe_text
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
)
stateMachine_IDElement_strategy = st.builds(
    stateMachine_IDElement,
    id=
        safe_text
)
stateMachine_Event_strategy = st.builds(
    stateMachine_Event,
)
stateMachine_Transition_strategy = st.builds(
    stateMachine_Transition,
)

@given(instance=IDElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IDElement)

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)

@given(instance=stateMachine_IDElement_strategy)
@settings(max_examples=50)
def test_statemachine_idelement_instantiation(instance):
    assert isinstance(instance, stateMachine_IDElement)



@given(instance=stateMachine_IDElement_strategy)
def test_statemachine_idelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=stateMachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, stateMachine_Event)

@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)
