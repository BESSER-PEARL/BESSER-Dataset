import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dfamodel::Transition,
    dfamodel::State,
    dfamodel::DFA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfamodel::transition_is_not_abstract():
    assert not inspect.isabstract(dfamodel::Transition)


def test_dfamodel::transition_constructor_exists():
    assert callable(dfamodel::Transition.__init__)


def test_dfamodel::transition_constructor_args():
    sig = inspect.signature(dfamodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_dfamodel::transition_has_input():
    assert hasattr(dfamodel::Transition, "input")
    descriptor = None
    for klass in dfamodel::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_dfamodel::state_is_not_abstract():
    assert not inspect.isabstract(dfamodel::State)


def test_dfamodel::state_constructor_exists():
    assert callable(dfamodel::State.__init__)


def test_dfamodel::state_constructor_args():
    sig = inspect.signature(dfamodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "id" in params, "Missing parameter 'id'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_dfamodel::state_has_isEnd():
    assert hasattr(dfamodel::State, "isEnd")
    descriptor = None
    for klass in dfamodel::State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_dfamodel::state_has_id():
    assert hasattr(dfamodel::State, "id")
    descriptor = None
    for klass in dfamodel::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dfamodel::state_has_isStart():
    assert hasattr(dfamodel::State, "isStart")
    descriptor = None
    for klass in dfamodel::State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)



def test_dfamodel::dfa_is_not_abstract():
    assert not inspect.isabstract(dfamodel::DFA)


def test_dfamodel::dfa_constructor_exists():
    assert callable(dfamodel::DFA.__init__)


def test_dfamodel::dfa_constructor_args():
    sig = inspect.signature(dfamodel::DFA.__init__)
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
dfamodel::Transition_strategy = st.builds(
    dfamodel::Transition,
    input=
        safe_text
)
dfamodel::State_strategy = st.builds(
    dfamodel::State,
    isEnd=
        st.booleans(),
    id=
        safe_text,
    isStart=
        st.booleans()
)
dfamodel::DFA_strategy = st.builds(
    dfamodel::DFA,
)

@given(instance=dfamodel::Transition_strategy)
@settings(max_examples=50)
def test_dfamodel::transition_instantiation(instance):
    assert isinstance(instance, dfamodel::Transition)

@given(instance=dfamodel::Transition_strategy)
def test_dfamodel::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=dfamodel::Transition_strategy)
def test_dfamodel::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=dfamodel::State_strategy)
@settings(max_examples=50)
def test_dfamodel::state_instantiation(instance):
    assert isinstance(instance, dfamodel::State)

@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_isEnd_type(instance):
    assert isinstance(instance.isEnd, bool)


@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_isStart_type(instance):
    assert isinstance(instance.isStart, bool)


@given(instance=dfamodel::State_strategy)
def test_dfamodel::state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=dfamodel::DFA_strategy)
@settings(max_examples=50)
def test_dfamodel::dfa_instantiation(instance):
    assert isinstance(instance, dfamodel::DFA)
