import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    model_State,
    model_Transition,
    model_FiniteStateMachine,
    model_AbstractState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_model_state_is_not_abstract():
    assert not inspect.isabstract(model_State)


def test_model_state_constructor_exists():
    assert callable(model_State.__init__)


def test_model_state_constructor_args():
    sig = inspect.signature(model_State.__init__)
    params = list(sig.parameters.keys())



def test_model_transition_is_not_abstract():
    assert not inspect.isabstract(model_Transition)


def test_model_transition_constructor_exists():
    assert callable(model_Transition.__init__)


def test_model_transition_constructor_args():
    sig = inspect.signature(model_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_model_transition_has_name():
    assert hasattr(model_Transition, "name")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_transition_has_trigger():
    assert hasattr(model_Transition, "trigger")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_model_finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(model_FiniteStateMachine)


def test_model_finitestatemachine_constructor_exists():
    assert callable(model_FiniteStateMachine.__init__)


def test_model_finitestatemachine_constructor_args():
    sig = inspect.signature(model_FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_model_abstractstate_is_not_abstract():
    assert not inspect.isabstract(model_AbstractState)


def test_model_abstractstate_constructor_exists():
    assert callable(model_AbstractState.__init__)


def test_model_abstractstate_constructor_args():
    sig = inspect.signature(model_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_abstractstate_has_name():
    assert hasattr(model_AbstractState, "name")
    descriptor = None
    for klass in model_AbstractState.__mro__:
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
AbstractState_strategy = st.builds(
    AbstractState,
)
model_State_strategy = st.builds(
    model_State,
)
model_Transition_strategy = st.builds(
    model_Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
model_FiniteStateMachine_strategy = st.builds(
    model_FiniteStateMachine,
)
model_AbstractState_strategy = st.builds(
    model_AbstractState,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=model_State_strategy)
@settings(max_examples=50)
def test_model_state_instantiation(instance):
    assert isinstance(instance, model_State)

@given(instance=model_Transition_strategy)
@settings(max_examples=50)
def test_model_transition_instantiation(instance):
    assert isinstance(instance, model_Transition)



@given(instance=model_Transition_strategy)
def test_model_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Transition_strategy)
def test_model_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=model_FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_model_finitestatemachine_instantiation(instance):
    assert isinstance(instance, model_FiniteStateMachine)

@given(instance=model_AbstractState_strategy)
@settings(max_examples=50)
def test_model_abstractstate_instantiation(instance):
    assert isinstance(instance, model_AbstractState)



@given(instance=model_AbstractState_strategy)
def test_model_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
