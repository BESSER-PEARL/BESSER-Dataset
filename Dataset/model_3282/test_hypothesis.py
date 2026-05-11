import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statediagram::Transition,
    statediagram::State,
    statediagram::StateDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statediagram::transition_is_not_abstract():
    assert not inspect.isabstract(statediagram::Transition)


def test_statediagram::transition_constructor_exists():
    assert callable(statediagram::Transition.__init__)


def test_statediagram::transition_constructor_args():
    sig = inspect.signature(statediagram::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statediagram::state_is_not_abstract():
    assert not inspect.isabstract(statediagram::State)


def test_statediagram::state_constructor_exists():
    assert callable(statediagram::State.__init__)


def test_statediagram::state_constructor_args():
    sig = inspect.signature(statediagram::State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "name" in params, "Missing parameter 'name'"

def test_statediagram::state_has_isInitial():
    assert hasattr(statediagram::State, "isInitial")
    descriptor = None
    for klass in statediagram::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_statediagram::state_has_name():
    assert hasattr(statediagram::State, "name")
    descriptor = None
    for klass in statediagram::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statediagram::statediagram_is_not_abstract():
    assert not inspect.isabstract(statediagram::StateDiagram)


def test_statediagram::statediagram_constructor_exists():
    assert callable(statediagram::StateDiagram.__init__)


def test_statediagram::statediagram_constructor_args():
    sig = inspect.signature(statediagram::StateDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statediagram::statediagram_has_name():
    assert hasattr(statediagram::StateDiagram, "name")
    descriptor = None
    for klass in statediagram::StateDiagram.__mro__:
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
statediagram::Transition_strategy = st.builds(
    statediagram::Transition,
)
statediagram::State_strategy = st.builds(
    statediagram::State,
    isInitial=
        st.booleans(),
    name=
        safe_text
)
statediagram::StateDiagram_strategy = st.builds(
    statediagram::StateDiagram,
    name=
        safe_text
)

@given(instance=statediagram::Transition_strategy)
@settings(max_examples=50)
def test_statediagram::transition_instantiation(instance):
    assert isinstance(instance, statediagram::Transition)

@given(instance=statediagram::State_strategy)
@settings(max_examples=50)
def test_statediagram::state_instantiation(instance):
    assert isinstance(instance, statediagram::State)

@given(instance=statediagram::State_strategy)
def test_statediagram::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=statediagram::State_strategy)
def test_statediagram::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=statediagram::State_strategy)
def test_statediagram::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statediagram::State_strategy)
def test_statediagram::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statediagram::StateDiagram_strategy)
@settings(max_examples=50)
def test_statediagram::statediagram_instantiation(instance):
    assert isinstance(instance, statediagram::StateDiagram)

@given(instance=statediagram::StateDiagram_strategy)
def test_statediagram::statediagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statediagram::StateDiagram_strategy)
def test_statediagram::statediagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
