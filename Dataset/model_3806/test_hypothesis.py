import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachineEditRules::DFA,
    stateMachineEditRules::State,
    stateMachineEditRules::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachineeditrules::dfa_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules::DFA)


def test_statemachineeditrules::dfa_constructor_exists():
    assert callable(stateMachineEditRules::DFA.__init__)


def test_statemachineeditrules::dfa_constructor_args():
    sig = inspect.signature(stateMachineEditRules::DFA.__init__)
    params = list(sig.parameters.keys())



def test_statemachineeditrules::state_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules::State)


def test_statemachineeditrules::state_constructor_exists():
    assert callable(stateMachineEditRules::State.__init__)


def test_statemachineeditrules::state_constructor_args():
    sig = inspect.signature(stateMachineEditRules::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_statemachineeditrules::state_has_id():
    assert hasattr(stateMachineEditRules::State, "id")
    descriptor = None
    for klass in stateMachineEditRules::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachineeditrules::state_has_isEnd():
    assert hasattr(stateMachineEditRules::State, "isEnd")
    descriptor = None
    for klass in stateMachineEditRules::State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_statemachineeditrules::state_has_isStart():
    assert hasattr(stateMachineEditRules::State, "isStart")
    descriptor = None
    for klass in stateMachineEditRules::State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)



def test_statemachineeditrules::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules::Transition)


def test_statemachineeditrules::transition_constructor_exists():
    assert callable(stateMachineEditRules::Transition.__init__)


def test_statemachineeditrules::transition_constructor_args():
    sig = inspect.signature(stateMachineEditRules::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_statemachineeditrules::transition_has_input():
    assert hasattr(stateMachineEditRules::Transition, "input")
    descriptor = None
    for klass in stateMachineEditRules::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)


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
stateMachineEditRules::DFA_strategy = st.builds(
    stateMachineEditRules::DFA,
)
stateMachineEditRules::State_strategy = st.builds(
    stateMachineEditRules::State,
    id=
        safe_text,
    isEnd=
        st.booleans(),
    isStart=
        st.booleans()
)
stateMachineEditRules::Transition_strategy = st.builds(
    stateMachineEditRules::Transition,
    input=
        safe_text
)

@given(instance=stateMachineEditRules::DFA_strategy)
@settings(max_examples=50)
def test_statemachineeditrules::dfa_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules::DFA)

@given(instance=stateMachineEditRules::State_strategy)
@settings(max_examples=50)
def test_statemachineeditrules::state_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules::State)

@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_isEnd_type(instance):
    assert isinstance(instance.isEnd, bool)


@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_isStart_type(instance):
    assert isinstance(instance.isStart, bool)


@given(instance=stateMachineEditRules::State_strategy)
def test_statemachineeditrules::state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=stateMachineEditRules::Transition_strategy)
@settings(max_examples=50)
def test_statemachineeditrules::transition_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules::Transition)

@given(instance=stateMachineEditRules::Transition_strategy)
def test_statemachineeditrules::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=stateMachineEditRules::Transition_strategy)
def test_statemachineeditrules::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original
