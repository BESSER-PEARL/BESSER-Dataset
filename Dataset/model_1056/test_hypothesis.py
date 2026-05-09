import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fSM::EnumerationLiteral,
    fSM::State,
    fSM::FSM,
    fSM::EnumerationType,
    fSM::Model,
    fSM::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(fSM::EnumerationLiteral)


def test_fsm::enumerationliteral_constructor_exists():
    assert callable(fSM::EnumerationLiteral.__init__)


def test_fsm::enumerationliteral_constructor_args():
    sig = inspect.signature(fSM::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::enumerationliteral_has_name():
    assert hasattr(fSM::EnumerationLiteral, "name")
    descriptor = None
    for klass in fSM::EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fSM::State)


def test_fsm::state_constructor_exists():
    assert callable(fSM::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fSM::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fSM::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fSM::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fSM::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(fSM::EnumerationType)


def test_fsm::enumerationtype_constructor_exists():
    assert callable(fSM::EnumerationType.__init__)


def test_fsm::enumerationtype_constructor_args():
    sig = inspect.signature(fSM::EnumerationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::enumerationtype_has_name():
    assert hasattr(fSM::EnumerationType, "name")
    descriptor = None
    for klass in fSM::EnumerationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::model_is_not_abstract():
    assert not inspect.isabstract(fSM::Model)


def test_fsm::model_constructor_exists():
    assert callable(fSM::Model.__init__)


def test_fsm::model_constructor_args():
    sig = inspect.signature(fSM::Model.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fSM::Transition.__init__)
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
fSM::EnumerationLiteral_strategy = st.builds(
    fSM::EnumerationLiteral,
    name=
        safe_text
)
fSM::State_strategy = st.builds(
    fSM::State,
)
fSM::FSM_strategy = st.builds(
    fSM::FSM,
)
fSM::EnumerationType_strategy = st.builds(
    fSM::EnumerationType,
    name=
        safe_text
)
fSM::Model_strategy = st.builds(
    fSM::Model,
)
fSM::Transition_strategy = st.builds(
    fSM::Transition,
)

@given(instance=fSM::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_fsm::enumerationliteral_instantiation(instance):
    assert isinstance(instance, fSM::EnumerationLiteral)

@given(instance=fSM::EnumerationLiteral_strategy)
def test_fsm::enumerationliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fSM::EnumerationLiteral_strategy)
def test_fsm::enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fSM::State)

@given(instance=fSM::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fSM::FSM)

@given(instance=fSM::EnumerationType_strategy)
@settings(max_examples=50)
def test_fsm::enumerationtype_instantiation(instance):
    assert isinstance(instance, fSM::EnumerationType)

@given(instance=fSM::EnumerationType_strategy)
def test_fsm::enumerationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fSM::EnumerationType_strategy)
def test_fsm::enumerationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fSM::Model_strategy)
@settings(max_examples=50)
def test_fsm::model_instantiation(instance):
    assert isinstance(instance, fSM::Model)

@given(instance=fSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fSM::Transition)
