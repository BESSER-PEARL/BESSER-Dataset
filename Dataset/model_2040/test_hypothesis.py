import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iDM::Test::Transition,
    iDM::Test::State,
    iDM::Test::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idm::test::transition_is_not_abstract():
    assert not inspect.isabstract(iDM::Test::Transition)


def test_idm::test::transition_constructor_exists():
    assert callable(iDM::Test::Transition.__init__)


def test_idm::test::transition_constructor_args():
    sig = inspect.signature(iDM::Test::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::test::transition_has_name():
    assert hasattr(iDM::Test::Transition, "name")
    descriptor = None
    for klass in iDM::Test::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm::test::state_is_not_abstract():
    assert not inspect.isabstract(iDM::Test::State)


def test_idm::test::state_constructor_exists():
    assert callable(iDM::Test::State.__init__)


def test_idm::test::state_constructor_args():
    sig = inspect.signature(iDM::Test::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::test::state_has_name():
    assert hasattr(iDM::Test::State, "name")
    descriptor = None
    for klass in iDM::Test::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm::test::statemachine_is_not_abstract():
    assert not inspect.isabstract(iDM::Test::StateMachine)


def test_idm::test::statemachine_constructor_exists():
    assert callable(iDM::Test::StateMachine.__init__)


def test_idm::test::statemachine_constructor_args():
    sig = inspect.signature(iDM::Test::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::test::statemachine_has_name():
    assert hasattr(iDM::Test::StateMachine, "name")
    descriptor = None
    for klass in iDM::Test::StateMachine.__mro__:
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
iDM::Test::Transition_strategy = st.builds(
    iDM::Test::Transition,
    name=
        safe_text
)
iDM::Test::State_strategy = st.builds(
    iDM::Test::State,
    name=
        safe_text
)
iDM::Test::StateMachine_strategy = st.builds(
    iDM::Test::StateMachine,
    name=
        safe_text
)

@given(instance=iDM::Test::Transition_strategy)
@settings(max_examples=50)
def test_idm::test::transition_instantiation(instance):
    assert isinstance(instance, iDM::Test::Transition)

@given(instance=iDM::Test::Transition_strategy)
def test_idm::test::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iDM::Test::Transition_strategy)
def test_idm::test::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iDM::Test::State_strategy)
@settings(max_examples=50)
def test_idm::test::state_instantiation(instance):
    assert isinstance(instance, iDM::Test::State)

@given(instance=iDM::Test::State_strategy)
def test_idm::test::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iDM::Test::State_strategy)
def test_idm::test::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iDM::Test::StateMachine_strategy)
@settings(max_examples=50)
def test_idm::test::statemachine_instantiation(instance):
    assert isinstance(instance, iDM::Test::StateMachine)

@given(instance=iDM::Test::StateMachine_strategy)
def test_idm::test::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iDM::Test::StateMachine_strategy)
def test_idm::test::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
