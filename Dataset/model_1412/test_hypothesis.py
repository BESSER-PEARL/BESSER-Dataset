import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    trialStatemachine_ComplexState,
    trialStatemachine_Region,
    trialStatemachine_LabeledTransition,
    trialStatemachine_State,
    trialStatemachine_Action,
    Region,
    trialStatemachine_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_trialstatemachine_complexstate_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_ComplexState)


def test_trialstatemachine_complexstate_constructor_exists():
    assert callable(trialStatemachine_ComplexState.__init__)


def test_trialstatemachine_complexstate_constructor_args():
    sig = inspect.signature(trialStatemachine_ComplexState.__init__)
    params = list(sig.parameters.keys())



def test_trialstatemachine_region_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_Region)


def test_trialstatemachine_region_constructor_exists():
    assert callable(trialStatemachine_Region.__init__)


def test_trialstatemachine_region_constructor_args():
    sig = inspect.signature(trialStatemachine_Region.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_trialstatemachine_region_has_history():
    assert hasattr(trialStatemachine_Region, "history")
    descriptor = None
    for klass in trialStatemachine_Region.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine_labeledtransition_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_LabeledTransition)


def test_trialstatemachine_labeledtransition_constructor_exists():
    assert callable(trialStatemachine_LabeledTransition.__init__)


def test_trialstatemachine_labeledtransition_constructor_args():
    sig = inspect.signature(trialStatemachine_LabeledTransition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_trialstatemachine_labeledtransition_has_id():
    assert hasattr(trialStatemachine_LabeledTransition, "id")
    descriptor = None
    for klass in trialStatemachine_LabeledTransition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine_state_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_State)


def test_trialstatemachine_state_constructor_exists():
    assert callable(trialStatemachine_State.__init__)


def test_trialstatemachine_state_constructor_args():
    sig = inspect.signature(trialStatemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "initialState" in params, "Missing parameter 'initialState'"
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine_state_has_initialState():
    assert hasattr(trialStatemachine_State, "initialState")
    descriptor = None
    for klass in trialStatemachine_State.__mro__:
        if "initialState" in klass.__dict__:
            descriptor = klass.__dict__["initialState"]
            break
    assert isinstance(descriptor, property)

def test_trialstatemachine_state_has_name():
    assert hasattr(trialStatemachine_State, "name")
    descriptor = None
    for klass in trialStatemachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine_action_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_Action)


def test_trialstatemachine_action_constructor_exists():
    assert callable(trialStatemachine_Action.__init__)


def test_trialstatemachine_action_constructor_args():
    sig = inspect.signature(trialStatemachine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine_action_has_name():
    assert hasattr(trialStatemachine_Action, "name")
    descriptor = None
    for klass in trialStatemachine_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_trialstatemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine_Statemachine)


def test_trialstatemachine_statemachine_constructor_exists():
    assert callable(trialStatemachine_Statemachine.__init__)


def test_trialstatemachine_statemachine_constructor_args():
    sig = inspect.signature(trialStatemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine_statemachine_has_name():
    assert hasattr(trialStatemachine_Statemachine, "name")
    descriptor = None
    for klass in trialStatemachine_Statemachine.__mro__:
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
State_strategy = st.builds(
    State,
)
trialStatemachine_ComplexState_strategy = st.builds(
    trialStatemachine_ComplexState,
)
trialStatemachine_Region_strategy = st.builds(
    trialStatemachine_Region,
    history=
        safe_text
)
trialStatemachine_LabeledTransition_strategy = st.builds(
    trialStatemachine_LabeledTransition,
    id=
        safe_text
)
trialStatemachine_State_strategy = st.builds(
    trialStatemachine_State,
    initialState=
        safe_text,
    name=
        safe_text
)
trialStatemachine_Action_strategy = st.builds(
    trialStatemachine_Action,
    name=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
trialStatemachine_Statemachine_strategy = st.builds(
    trialStatemachine_Statemachine,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=trialStatemachine_ComplexState_strategy)
@settings(max_examples=50)
def test_trialstatemachine_complexstate_instantiation(instance):
    assert isinstance(instance, trialStatemachine_ComplexState)

@given(instance=trialStatemachine_Region_strategy)
@settings(max_examples=50)
def test_trialstatemachine_region_instantiation(instance):
    assert isinstance(instance, trialStatemachine_Region)



@given(instance=trialStatemachine_Region_strategy)
def test_trialstatemachine_region_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=trialStatemachine_LabeledTransition_strategy)
@settings(max_examples=50)
def test_trialstatemachine_labeledtransition_instantiation(instance):
    assert isinstance(instance, trialStatemachine_LabeledTransition)



@given(instance=trialStatemachine_LabeledTransition_strategy)
def test_trialstatemachine_labeledtransition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=trialStatemachine_State_strategy)
@settings(max_examples=50)
def test_trialstatemachine_state_instantiation(instance):
    assert isinstance(instance, trialStatemachine_State)



@given(instance=trialStatemachine_State_strategy)
def test_trialstatemachine_state_initialState_setter(instance):
    original = instance.initialState
    instance.initialState = original
    assert instance.initialState == original



@given(instance=trialStatemachine_State_strategy)
def test_trialstatemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trialStatemachine_Action_strategy)
@settings(max_examples=50)
def test_trialstatemachine_action_instantiation(instance):
    assert isinstance(instance, trialStatemachine_Action)



@given(instance=trialStatemachine_Action_strategy)
def test_trialstatemachine_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=trialStatemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_trialstatemachine_statemachine_instantiation(instance):
    assert isinstance(instance, trialStatemachine_Statemachine)



@given(instance=trialStatemachine_Statemachine_strategy)
def test_trialstatemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
