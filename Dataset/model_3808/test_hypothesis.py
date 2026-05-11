import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    exercises::NamableElement,
    NamableElement,
    exercises::Transition,
    exercises::State,
    exercises::DFA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exercises::namableelement_is_not_abstract():
    assert not inspect.isabstract(exercises::NamableElement)


def test_exercises::namableelement_constructor_exists():
    assert callable(exercises::NamableElement.__init__)


def test_exercises::namableelement_constructor_args():
    sig = inspect.signature(exercises::NamableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_exercises::namableelement_has_name():
    assert hasattr(exercises::NamableElement, "name")
    descriptor = None
    for klass in exercises::NamableElement.__mro__:
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



def test_exercises::transition_is_not_abstract():
    assert not inspect.isabstract(exercises::Transition)


def test_exercises::transition_constructor_exists():
    assert callable(exercises::Transition.__init__)


def test_exercises::transition_constructor_args():
    sig = inspect.signature(exercises::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_exercises::transition_has_input():
    assert hasattr(exercises::Transition, "input")
    descriptor = None
    for klass in exercises::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_exercises::state_is_not_abstract():
    assert not inspect.isabstract(exercises::State)


def test_exercises::state_constructor_exists():
    assert callable(exercises::State.__init__)


def test_exercises::state_constructor_args():
    sig = inspect.signature(exercises::State.__init__)
    params = list(sig.parameters.keys())
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"
    assert "id" in params, "Missing parameter 'id'"

def test_exercises::state_has_isEnd():
    assert hasattr(exercises::State, "isEnd")
    descriptor = None
    for klass in exercises::State.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_exercises::state_has_isStart():
    assert hasattr(exercises::State, "isStart")
    descriptor = None
    for klass in exercises::State.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)

def test_exercises::state_has_id():
    assert hasattr(exercises::State, "id")
    descriptor = None
    for klass in exercises::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_exercises::dfa_is_not_abstract():
    assert not inspect.isabstract(exercises::DFA)


def test_exercises::dfa_constructor_exists():
    assert callable(exercises::DFA.__init__)


def test_exercises::dfa_constructor_args():
    sig = inspect.signature(exercises::DFA.__init__)
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
exercises::NamableElement_strategy = st.builds(
    exercises::NamableElement,
    name=
        safe_text
)
NamableElement_strategy = st.builds(
    NamableElement,
)
exercises::Transition_strategy = st.builds(
    exercises::Transition,
    input=
        safe_text
)
exercises::State_strategy = st.builds(
    exercises::State,
    isEnd=
        st.booleans(),
    isStart=
        st.booleans(),
    id=
        safe_text
)
exercises::DFA_strategy = st.builds(
    exercises::DFA,
)

@given(instance=exercises::NamableElement_strategy)
@settings(max_examples=50)
def test_exercises::namableelement_instantiation(instance):
    assert isinstance(instance, exercises::NamableElement)

@given(instance=exercises::NamableElement_strategy)
def test_exercises::namableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=exercises::NamableElement_strategy)
def test_exercises::namableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamableElement_strategy)
@settings(max_examples=50)
def test_namableelement_instantiation(instance):
    assert isinstance(instance, NamableElement)

@given(instance=exercises::Transition_strategy)
@settings(max_examples=50)
def test_exercises::transition_instantiation(instance):
    assert isinstance(instance, exercises::Transition)

@given(instance=exercises::Transition_strategy)
def test_exercises::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=exercises::Transition_strategy)
def test_exercises::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=exercises::State_strategy)
@settings(max_examples=50)
def test_exercises::state_instantiation(instance):
    assert isinstance(instance, exercises::State)

@given(instance=exercises::State_strategy)
def test_exercises::state_isEnd_type(instance):
    assert isinstance(instance.isEnd, bool)


@given(instance=exercises::State_strategy)
def test_exercises::state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=exercises::State_strategy)
def test_exercises::state_isStart_type(instance):
    assert isinstance(instance.isStart, bool)


@given(instance=exercises::State_strategy)
def test_exercises::state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=exercises::State_strategy)
def test_exercises::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=exercises::State_strategy)
def test_exercises::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=exercises::DFA_strategy)
@settings(max_examples=50)
def test_exercises::dfa_instantiation(instance):
    assert isinstance(instance, exercises::DFA)
