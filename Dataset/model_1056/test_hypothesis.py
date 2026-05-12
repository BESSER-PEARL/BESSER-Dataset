import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fSM_EnumerationLiteral,
    fSM_State,
    fSM_FSM,
    fSM_EnumerationType,
    fSM_Model,
    fSM_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(fSM_EnumerationLiteral)


def test_fsm_enumerationliteral_constructor_exists():
    assert callable(fSM_EnumerationLiteral.__init__)


def test_fsm_enumerationliteral_constructor_args():
    sig = inspect.signature(fSM_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_enumerationliteral_has_name():
    assert hasattr(fSM_EnumerationLiteral, "name")
    descriptor = None
    for klass in fSM_EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fSM_State)


def test_fsm_state_constructor_exists():
    assert callable(fSM_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fSM_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fSM_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fSM_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fSM_FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(fSM_EnumerationType)


def test_fsm_enumerationtype_constructor_exists():
    assert callable(fSM_EnumerationType.__init__)


def test_fsm_enumerationtype_constructor_args():
    sig = inspect.signature(fSM_EnumerationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_enumerationtype_has_name():
    assert hasattr(fSM_EnumerationType, "name")
    descriptor = None
    for klass in fSM_EnumerationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_model_is_not_abstract():
    assert not inspect.isabstract(fSM_Model)


def test_fsm_model_constructor_exists():
    assert callable(fSM_Model.__init__)


def test_fsm_model_constructor_args():
    sig = inspect.signature(fSM_Model.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fSM_Transition.__init__)
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
fSM_EnumerationLiteral_strategy = st.builds(
    fSM_EnumerationLiteral,
    name=
        safe_text
)
fSM_State_strategy = st.builds(
    fSM_State,
)
fSM_FSM_strategy = st.builds(
    fSM_FSM,
)
fSM_EnumerationType_strategy = st.builds(
    fSM_EnumerationType,
    name=
        safe_text
)
fSM_Model_strategy = st.builds(
    fSM_Model,
)
fSM_Transition_strategy = st.builds(
    fSM_Transition,
)

@given(instance=fSM_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_fsm_enumerationliteral_instantiation(instance):
    assert isinstance(instance, fSM_EnumerationLiteral)



@given(instance=fSM_EnumerationLiteral_strategy)
def test_fsm_enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fSM_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fSM_State)

@given(instance=fSM_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fSM_FSM)

@given(instance=fSM_EnumerationType_strategy)
@settings(max_examples=50)
def test_fsm_enumerationtype_instantiation(instance):
    assert isinstance(instance, fSM_EnumerationType)



@given(instance=fSM_EnumerationType_strategy)
def test_fsm_enumerationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fSM_Model_strategy)
@settings(max_examples=50)
def test_fsm_model_instantiation(instance):
    assert isinstance(instance, fSM_Model)

@given(instance=fSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fSM_Transition)
