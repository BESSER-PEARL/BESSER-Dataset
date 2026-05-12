import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statediagram_Transition,
    statediagram_State,
    statediagram_StateDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statediagram_transition_is_not_abstract():
    assert not inspect.isabstract(statediagram_Transition)


def test_statediagram_transition_constructor_exists():
    assert callable(statediagram_Transition.__init__)


def test_statediagram_transition_constructor_args():
    sig = inspect.signature(statediagram_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statediagram_state_is_not_abstract():
    assert not inspect.isabstract(statediagram_State)


def test_statediagram_state_constructor_exists():
    assert callable(statediagram_State.__init__)


def test_statediagram_state_constructor_args():
    sig = inspect.signature(statediagram_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "name" in params, "Missing parameter 'name'"

def test_statediagram_state_has_isInitial():
    assert hasattr(statediagram_State, "isInitial")
    descriptor = None
    for klass in statediagram_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_statediagram_state_has_name():
    assert hasattr(statediagram_State, "name")
    descriptor = None
    for klass in statediagram_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statediagram_statediagram_is_not_abstract():
    assert not inspect.isabstract(statediagram_StateDiagram)


def test_statediagram_statediagram_constructor_exists():
    assert callable(statediagram_StateDiagram.__init__)


def test_statediagram_statediagram_constructor_args():
    sig = inspect.signature(statediagram_StateDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statediagram_statediagram_has_name():
    assert hasattr(statediagram_StateDiagram, "name")
    descriptor = None
    for klass in statediagram_StateDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
statediagram_Transition_strategy = st.builds(
    statediagram_Transition,
)
statediagram_State_strategy = st.builds(
    statediagram_State,
    isInitial=
        st.booleans(),
    name=
        safe_text
)
statediagram_StateDiagram_strategy = st.builds(
    statediagram_StateDiagram,
    name=
        safe_text
)

@given(instance=statediagram_Transition_strategy)
@settings(max_examples=50)
def test_statediagram_transition_instantiation(instance):
    assert isinstance(instance, statediagram_Transition)

@given(instance=statediagram_State_strategy)
@settings(max_examples=50)
def test_statediagram_state_instantiation(instance):
    assert isinstance(instance, statediagram_State)



@given(instance=statediagram_State_strategy)
def test_statediagram_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=statediagram_State_strategy)
def test_statediagram_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statediagram_StateDiagram_strategy)
@settings(max_examples=50)
def test_statediagram_statediagram_instantiation(instance):
    assert isinstance(instance, statediagram_StateDiagram)



@given(instance=statediagram_StateDiagram_strategy)
def test_statediagram_statediagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
