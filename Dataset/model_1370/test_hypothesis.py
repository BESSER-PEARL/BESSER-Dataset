import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HSM_AbstractState,
    HSM_Transition,
    HSM_StateMachine,
    AbstractState,
    HSM_CompositeState,
    HSM_RegularState,
    HSM_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(HSM_AbstractState)


def test_hsm_abstractstate_constructor_exists():
    assert callable(HSM_AbstractState.__init__)


def test_hsm_abstractstate_constructor_args():
    sig = inspect.signature(HSM_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_abstractstate_has_name():
    assert hasattr(HSM_AbstractState, "name")
    descriptor = None
    for klass in HSM_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm_transition_is_not_abstract():
    assert not inspect.isabstract(HSM_Transition)


def test_hsm_transition_constructor_exists():
    assert callable(HSM_Transition.__init__)


def test_hsm_transition_constructor_args():
    sig = inspect.signature(HSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hsm_transition_has_label():
    assert hasattr(HSM_Transition, "label")
    descriptor = None
    for klass in HSM_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM_StateMachine)


def test_hsm_statemachine_constructor_exists():
    assert callable(HSM_StateMachine.__init__)


def test_hsm_statemachine_constructor_args():
    sig = inspect.signature(HSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_statemachine_has_name():
    assert hasattr(HSM_StateMachine, "name")
    descriptor = None
    for klass in HSM_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM_CompositeState)


def test_hsm_compositestate_constructor_exists():
    assert callable(HSM_CompositeState.__init__)


def test_hsm_compositestate_constructor_args():
    sig = inspect.signature(HSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_regularstate_is_not_abstract():
    assert not inspect.isabstract(HSM_RegularState)


def test_hsm_regularstate_constructor_exists():
    assert callable(HSM_RegularState.__init__)


def test_hsm_regularstate_constructor_args():
    sig = inspect.signature(HSM_RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(HSM_InitialState)


def test_hsm_initialstate_constructor_exists():
    assert callable(HSM_InitialState.__init__)


def test_hsm_initialstate_constructor_args():
    sig = inspect.signature(HSM_InitialState.__init__)
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
HSM_AbstractState_strategy = st.builds(
    HSM_AbstractState,
    name=
        safe_text
)
HSM_Transition_strategy = st.builds(
    HSM_Transition,
    label=
        safe_text
)
HSM_StateMachine_strategy = st.builds(
    HSM_StateMachine,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
HSM_CompositeState_strategy = st.builds(
    HSM_CompositeState,
)
HSM_RegularState_strategy = st.builds(
    HSM_RegularState,
)
HSM_InitialState_strategy = st.builds(
    HSM_InitialState,
)

@given(instance=HSM_AbstractState_strategy)
@settings(max_examples=50)
def test_hsm_abstractstate_instantiation(instance):
    assert isinstance(instance, HSM_AbstractState)



@given(instance=HSM_AbstractState_strategy)
def test_hsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM_Transition_strategy)
@settings(max_examples=50)
def test_hsm_transition_instantiation(instance):
    assert isinstance(instance, HSM_Transition)



@given(instance=HSM_Transition_strategy)
def test_hsm_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=50)
def test_hsm_statemachine_instantiation(instance):
    assert isinstance(instance, HSM_StateMachine)



@given(instance=HSM_StateMachine_strategy)
def test_hsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=HSM_CompositeState_strategy)
@settings(max_examples=50)
def test_hsm_compositestate_instantiation(instance):
    assert isinstance(instance, HSM_CompositeState)

@given(instance=HSM_RegularState_strategy)
@settings(max_examples=50)
def test_hsm_regularstate_instantiation(instance):
    assert isinstance(instance, HSM_RegularState)

@given(instance=HSM_InitialState_strategy)
@settings(max_examples=50)
def test_hsm_initialstate_instantiation(instance):
    assert isinstance(instance, HSM_InitialState)
