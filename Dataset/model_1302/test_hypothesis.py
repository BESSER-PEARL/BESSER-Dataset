import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IDElement,
    stateMachine::State,
    stateMachine::StateMachine,
    stateMachine::IDElement,
    stateMachine::Event,
    stateMachine::Transition,
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



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine::state_has_kind():
    assert hasattr(stateMachine::State, "kind")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::idelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine::IDElement)


def test_statemachine::idelement_constructor_exists():
    assert callable(stateMachine::IDElement.__init__)


def test_statemachine::idelement_constructor_args():
    sig = inspect.signature(stateMachine::IDElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::idelement_has_id():
    assert hasattr(stateMachine::IDElement, "id")
    descriptor = None
    for klass in stateMachine::IDElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(stateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(stateMachine::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())

def test_statekind_exists():
    # Check that the Enumeration exists
    assert StateKind is not None

def test_statekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateKind]
    expected_literals = [
        "DEFAULT",
        "INITIAL",
        "FINAL",
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
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    kind=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
)
stateMachine::IDElement_strategy = st.builds(
    stateMachine::IDElement,
    id=
        safe_text
)
stateMachine::Event_strategy = st.builds(
    stateMachine::Event,
)
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
)

@given(instance=IDElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IDElement)

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::IDElement_strategy)
@settings(max_examples=50)
def test_statemachine::idelement_instantiation(instance):
    assert isinstance(instance, stateMachine::IDElement)

@given(instance=stateMachine::IDElement_strategy)
def test_statemachine::idelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=stateMachine::IDElement_strategy)
def test_statemachine::idelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=stateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, stateMachine::Event)

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)
