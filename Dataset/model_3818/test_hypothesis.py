import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dfamodel_Transition,
    dfamodel_State,
    dfamodel_DFA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfamodel_transition_is_not_abstract():
    assert not inspect.isabstract(dfamodel_Transition)


def test_dfamodel_transition_constructor_exists():
    assert callable(dfamodel_Transition.__init__)


def test_dfamodel_transition_constructor_args():
    sig = inspect.signature(dfamodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_dfamodel_transition_has_input():
    assert hasattr(dfamodel_Transition, "input")
    descriptor = None
    for klass in dfamodel_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_dfamodel_state_is_not_abstract():
    assert not inspect.isabstract(dfamodel_State)


def test_dfamodel_state_constructor_exists():
    assert callable(dfamodel_State.__init__)


def test_dfamodel_state_constructor_args():
    sig = inspect.signature(dfamodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "isStart" in params, "Missing parameter 'isStart'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "id" in params, "Missing parameter 'id'"

def test_dfamodel_state_has_isStart():
    assert hasattr(dfamodel_State, "isStart")
    descriptor = None
    for klass in dfamodel_State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)

def test_dfamodel_state_has_isEnd():
    assert hasattr(dfamodel_State, "isEnd")
    descriptor = None
    for klass in dfamodel_State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_dfamodel_state_has_id():
    assert hasattr(dfamodel_State, "id")
    descriptor = None
    for klass in dfamodel_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dfamodel_dfa_is_not_abstract():
    assert not inspect.isabstract(dfamodel_DFA)


def test_dfamodel_dfa_constructor_exists():
    assert callable(dfamodel_DFA.__init__)


def test_dfamodel_dfa_constructor_args():
    sig = inspect.signature(dfamodel_DFA.__init__)
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
dfamodel_Transition_strategy = st.builds(
    dfamodel_Transition,
    input=
        safe_text
)
dfamodel_State_strategy = st.builds(
    dfamodel_State,
    isStart=
        st.booleans(),
    isEnd=
        st.booleans(),
    id=
        safe_text
)
dfamodel_DFA_strategy = st.builds(
    dfamodel_DFA,
)

@given(instance=dfamodel_Transition_strategy)
@settings(max_examples=50)
def test_dfamodel_transition_instantiation(instance):
    assert isinstance(instance, dfamodel_Transition)



@given(instance=dfamodel_Transition_strategy)
def test_dfamodel_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=dfamodel_State_strategy)
@settings(max_examples=50)
def test_dfamodel_state_instantiation(instance):
    assert isinstance(instance, dfamodel_State)



@given(instance=dfamodel_State_strategy)
def test_dfamodel_state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original



@given(instance=dfamodel_State_strategy)
def test_dfamodel_state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original



@given(instance=dfamodel_State_strategy)
def test_dfamodel_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dfamodel_DFA_strategy)
@settings(max_examples=50)
def test_dfamodel_dfa_instantiation(instance):
    assert isinstance(instance, dfamodel_DFA)
