import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    trialStatemachine::ComplexState,
    trialStatemachine::LabeledTransition,
    trialStatemachine::State,
    trialStatemachine::Action,
    Region,
    trialStatemachine::Statemachine,
    trialStatemachine::Region,
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



def test_trialstatemachine::complexstate_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::ComplexState)


def test_trialstatemachine::complexstate_constructor_exists():
    assert callable(trialStatemachine::ComplexState.__init__)


def test_trialstatemachine::complexstate_constructor_args():
    sig = inspect.signature(trialStatemachine::ComplexState.__init__)
    params = list(sig.parameters.keys())



def test_trialstatemachine::labeledtransition_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::LabeledTransition)


def test_trialstatemachine::labeledtransition_constructor_exists():
    assert callable(trialStatemachine::LabeledTransition.__init__)


def test_trialstatemachine::labeledtransition_constructor_args():
    sig = inspect.signature(trialStatemachine::LabeledTransition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_trialstatemachine::labeledtransition_has_id():
    assert hasattr(trialStatemachine::LabeledTransition, "id")
    descriptor = None
    for klass in trialStatemachine::LabeledTransition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine::state_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::State)


def test_trialstatemachine::state_constructor_exists():
    assert callable(trialStatemachine::State.__init__)


def test_trialstatemachine::state_constructor_args():
    sig = inspect.signature(trialStatemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine::state_has_name():
    assert hasattr(trialStatemachine::State, "name")
    descriptor = None
    for klass in trialStatemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine::action_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::Action)


def test_trialstatemachine::action_constructor_exists():
    assert callable(trialStatemachine::Action.__init__)


def test_trialstatemachine::action_constructor_args():
    sig = inspect.signature(trialStatemachine::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine::action_has_name():
    assert hasattr(trialStatemachine::Action, "name")
    descriptor = None
    for klass in trialStatemachine::Action.__mro__:
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



def test_trialstatemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::Statemachine)


def test_trialstatemachine::statemachine_constructor_exists():
    assert callable(trialStatemachine::Statemachine.__init__)


def test_trialstatemachine::statemachine_constructor_args():
    sig = inspect.signature(trialStatemachine::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trialstatemachine::statemachine_has_name():
    assert hasattr(trialStatemachine::Statemachine, "name")
    descriptor = None
    for klass in trialStatemachine::Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trialstatemachine::region_is_not_abstract():
    assert not inspect.isabstract(trialStatemachine::Region)


def test_trialstatemachine::region_constructor_exists():
    assert callable(trialStatemachine::Region.__init__)


def test_trialstatemachine::region_constructor_args():
    sig = inspect.signature(trialStatemachine::Region.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_trialstatemachine::region_has_history():
    assert hasattr(trialStatemachine::Region, "history")
    descriptor = None
    for klass in trialStatemachine::Region.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
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
trialStatemachine::ComplexState_strategy = st.builds(
    trialStatemachine::ComplexState,
)
trialStatemachine::LabeledTransition_strategy = st.builds(
    trialStatemachine::LabeledTransition,
    id=
        safe_text
)
trialStatemachine::State_strategy = st.builds(
    trialStatemachine::State,
    name=
        safe_text
)
trialStatemachine::Action_strategy = st.builds(
    trialStatemachine::Action,
    name=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
trialStatemachine::Statemachine_strategy = st.builds(
    trialStatemachine::Statemachine,
    name=
        safe_text
)
trialStatemachine::Region_strategy = st.builds(
    trialStatemachine::Region,
    history=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=trialStatemachine::ComplexState_strategy)
@settings(max_examples=50)
def test_trialstatemachine::complexstate_instantiation(instance):
    assert isinstance(instance, trialStatemachine::ComplexState)

@given(instance=trialStatemachine::LabeledTransition_strategy)
@settings(max_examples=50)
def test_trialstatemachine::labeledtransition_instantiation(instance):
    assert isinstance(instance, trialStatemachine::LabeledTransition)

@given(instance=trialStatemachine::LabeledTransition_strategy)
def test_trialstatemachine::labeledtransition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=trialStatemachine::LabeledTransition_strategy)
def test_trialstatemachine::labeledtransition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=trialStatemachine::State_strategy)
@settings(max_examples=50)
def test_trialstatemachine::state_instantiation(instance):
    assert isinstance(instance, trialStatemachine::State)

@given(instance=trialStatemachine::State_strategy)
def test_trialstatemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trialStatemachine::State_strategy)
def test_trialstatemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trialStatemachine::Action_strategy)
@settings(max_examples=50)
def test_trialstatemachine::action_instantiation(instance):
    assert isinstance(instance, trialStatemachine::Action)

@given(instance=trialStatemachine::Action_strategy)
def test_trialstatemachine::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trialStatemachine::Action_strategy)
def test_trialstatemachine::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=trialStatemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_trialstatemachine::statemachine_instantiation(instance):
    assert isinstance(instance, trialStatemachine::Statemachine)

@given(instance=trialStatemachine::Statemachine_strategy)
def test_trialstatemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trialStatemachine::Statemachine_strategy)
def test_trialstatemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trialStatemachine::Region_strategy)
@settings(max_examples=50)
def test_trialstatemachine::region_instantiation(instance):
    assert isinstance(instance, trialStatemachine::Region)

@given(instance=trialStatemachine::Region_strategy)
def test_trialstatemachine::region_history_type(instance):
    assert isinstance(instance.history, str)


@given(instance=trialStatemachine::Region_strategy)
def test_trialstatemachine::region_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original
