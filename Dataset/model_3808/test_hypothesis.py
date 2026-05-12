import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    exercises_NamableElement,
    NamableElement,
    exercises_State,
    exercises_Transition,
    exercises_DFA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exercises_namableelement_is_not_abstract():
    assert not inspect.isabstract(exercises_NamableElement)


def test_exercises_namableelement_constructor_exists():
    assert callable(exercises_NamableElement.__init__)


def test_exercises_namableelement_constructor_args():
    sig = inspect.signature(exercises_NamableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_exercises_namableelement_has_name():
    assert hasattr(exercises_NamableElement, "name")
    descriptor = None
    for klass in exercises_NamableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namableelement_is_not_abstract():
    assert not inspect.isabstract(NamableElement)


def test_namableelement_constructor_exists():
    assert callable(NamableElement.__init__)


def test_namableelement_constructor_args():
    sig = inspect.signature(NamableElement.__init__)
    params = list(sig.parameters.keys())



def test_exercises_state_is_not_abstract():
    assert not inspect.isabstract(exercises_State)


def test_exercises_state_constructor_exists():
    assert callable(exercises_State.__init__)


def test_exercises_state_constructor_args():
    sig = inspect.signature(exercises_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_exercises_state_has_id():
    assert hasattr(exercises_State, "id")
    descriptor = None
    for klass in exercises_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_exercises_state_has_isEnd():
    assert hasattr(exercises_State, "isEnd")
    descriptor = None
    for klass in exercises_State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_exercises_state_has_isStart():
    assert hasattr(exercises_State, "isStart")
    descriptor = None
    for klass in exercises_State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)



def test_exercises_transition_is_not_abstract():
    assert not inspect.isabstract(exercises_Transition)


def test_exercises_transition_constructor_exists():
    assert callable(exercises_Transition.__init__)


def test_exercises_transition_constructor_args():
    sig = inspect.signature(exercises_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_exercises_transition_has_input():
    assert hasattr(exercises_Transition, "input")
    descriptor = None
    for klass in exercises_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_exercises_dfa_is_not_abstract():
    assert not inspect.isabstract(exercises_DFA)


def test_exercises_dfa_constructor_exists():
    assert callable(exercises_DFA.__init__)


def test_exercises_dfa_constructor_args():
    sig = inspect.signature(exercises_DFA.__init__)
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
exercises_NamableElement_strategy = st.builds(
    exercises_NamableElement,
    name=
        safe_text
)
NamableElement_strategy = st.builds(
    NamableElement,
)
exercises_State_strategy = st.builds(
    exercises_State,
    id=
        safe_text,
    isEnd=
        st.booleans(),
    isStart=
        st.booleans()
)
exercises_Transition_strategy = st.builds(
    exercises_Transition,
    input=
        safe_text
)
exercises_DFA_strategy = st.builds(
    exercises_DFA,
)

@given(instance=exercises_NamableElement_strategy)
@settings(max_examples=50)
def test_exercises_namableelement_instantiation(instance):
    assert isinstance(instance, exercises_NamableElement)



@given(instance=exercises_NamableElement_strategy)
def test_exercises_namableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamableElement_strategy)
@settings(max_examples=50)
def test_namableelement_instantiation(instance):
    assert isinstance(instance, NamableElement)

@given(instance=exercises_State_strategy)
@settings(max_examples=50)
def test_exercises_state_instantiation(instance):
    assert isinstance(instance, exercises_State)



@given(instance=exercises_State_strategy)
def test_exercises_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=exercises_State_strategy)
def test_exercises_state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original



@given(instance=exercises_State_strategy)
def test_exercises_state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=exercises_Transition_strategy)
@settings(max_examples=50)
def test_exercises_transition_instantiation(instance):
    assert isinstance(instance, exercises_Transition)



@given(instance=exercises_Transition_strategy)
def test_exercises_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=exercises_DFA_strategy)
@settings(max_examples=50)
def test_exercises_dfa_instantiation(instance):
    assert isinstance(instance, exercises_DFA)
