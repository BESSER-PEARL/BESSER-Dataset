import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachineEditRules_DFA,
    stateMachineEditRules_State,
    stateMachineEditRules_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachineeditrules_dfa_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_DFA)


def test_statemachineeditrules_dfa_constructor_exists():
    assert callable(stateMachineEditRules_DFA.__init__)


def test_statemachineeditrules_dfa_constructor_args():
    sig = inspect.signature(stateMachineEditRules_DFA.__init__)
    params = list(sig.parameters.keys())



def test_statemachineeditrules_state_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_State)


def test_statemachineeditrules_state_constructor_exists():
    assert callable(stateMachineEditRules_State.__init__)


def test_statemachineeditrules_state_constructor_args():
    sig = inspect.signature(stateMachineEditRules_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isStart" in params, "Missing parameter 'isStart'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"

def test_statemachineeditrules_state_has_id():
    assert hasattr(stateMachineEditRules_State, "id")
    descriptor = None
    for klass in stateMachineEditRules_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachineeditrules_state_has_isStart():
    assert hasattr(stateMachineEditRules_State, "isStart")
    descriptor = None
    for klass in stateMachineEditRules_State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)

def test_statemachineeditrules_state_has_isEnd():
    assert hasattr(stateMachineEditRules_State, "isEnd")
    descriptor = None
    for klass in stateMachineEditRules_State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)



def test_statemachineeditrules_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachineEditRules_Transition)


def test_statemachineeditrules_transition_constructor_exists():
    assert callable(stateMachineEditRules_Transition.__init__)


def test_statemachineeditrules_transition_constructor_args():
    sig = inspect.signature(stateMachineEditRules_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_statemachineeditrules_transition_has_input():
    assert hasattr(stateMachineEditRules_Transition, "input")
    descriptor = None
    for klass in stateMachineEditRules_Transition.__mro__:
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
stateMachineEditRules_DFA_strategy = st.builds(
    stateMachineEditRules_DFA,
)
stateMachineEditRules_State_strategy = st.builds(
    stateMachineEditRules_State,
    id=
        safe_text,
    isStart=
        st.booleans(),
    isEnd=
        st.booleans()
)
stateMachineEditRules_Transition_strategy = st.builds(
    stateMachineEditRules_Transition,
    input=
        safe_text
)

@given(instance=stateMachineEditRules_DFA_strategy)
@settings(max_examples=50)
def test_statemachineeditrules_dfa_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_DFA)

@given(instance=stateMachineEditRules_State_strategy)
@settings(max_examples=50)
def test_statemachineeditrules_state_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_State)



@given(instance=stateMachineEditRules_State_strategy)
def test_statemachineeditrules_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=stateMachineEditRules_State_strategy)
def test_statemachineeditrules_state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original



@given(instance=stateMachineEditRules_State_strategy)
def test_statemachineeditrules_state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=stateMachineEditRules_Transition_strategy)
@settings(max_examples=50)
def test_statemachineeditrules_transition_instantiation(instance):
    assert isinstance(instance, stateMachineEditRules_Transition)



@given(instance=stateMachineEditRules_Transition_strategy)
def test_statemachineeditrules_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original
