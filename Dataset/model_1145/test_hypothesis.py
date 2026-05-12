import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hsm_Root,
    hsm_AbstractState,
    hsm_Transition,
    hsm_StateMachine,
    AbstractState,
    hsm_RegularState,
    hsm_InitialState,
    hsm_CompositeState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm_root_is_not_abstract():
    assert not inspect.isabstract(hsm_Root)


def test_hsm_root_constructor_exists():
    assert callable(hsm_Root.__init__)


def test_hsm_root_constructor_args():
    sig = inspect.signature(hsm_Root.__init__)
    params = list(sig.parameters.keys())



def test_hsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(hsm_AbstractState)


def test_hsm_abstractstate_constructor_exists():
    assert callable(hsm_AbstractState.__init__)


def test_hsm_abstractstate_constructor_args():
    sig = inspect.signature(hsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_abstractstate_has_name():
    assert hasattr(hsm_AbstractState, "name")
    descriptor = None
    for klass in hsm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm_transition_is_not_abstract():
    assert not inspect.isabstract(hsm_Transition)


def test_hsm_transition_constructor_exists():
    assert callable(hsm_Transition.__init__)


def test_hsm_transition_constructor_args():
    sig = inspect.signature(hsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hsm_transition_has_label():
    assert hasattr(hsm_Transition, "label")
    descriptor = None
    for klass in hsm_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(hsm_StateMachine)


def test_hsm_statemachine_constructor_exists():
    assert callable(hsm_StateMachine.__init__)


def test_hsm_statemachine_constructor_args():
    sig = inspect.signature(hsm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_statemachine_has_name():
    assert hasattr(hsm_StateMachine, "name")
    descriptor = None
    for klass in hsm_StateMachine.__mro__:
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



def test_hsm_regularstate_is_not_abstract():
    assert not inspect.isabstract(hsm_RegularState)


def test_hsm_regularstate_constructor_exists():
    assert callable(hsm_RegularState.__init__)


def test_hsm_regularstate_constructor_args():
    sig = inspect.signature(hsm_RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(hsm_InitialState)


def test_hsm_initialstate_constructor_exists():
    assert callable(hsm_InitialState.__init__)


def test_hsm_initialstate_constructor_args():
    sig = inspect.signature(hsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(hsm_CompositeState)


def test_hsm_compositestate_constructor_exists():
    assert callable(hsm_CompositeState.__init__)


def test_hsm_compositestate_constructor_args():
    sig = inspect.signature(hsm_CompositeState.__init__)
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
hsm_Root_strategy = st.builds(
    hsm_Root,
)
hsm_AbstractState_strategy = st.builds(
    hsm_AbstractState,
    name=
        safe_text
)
hsm_Transition_strategy = st.builds(
    hsm_Transition,
    label=
        safe_text
)
hsm_StateMachine_strategy = st.builds(
    hsm_StateMachine,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hsm_RegularState_strategy = st.builds(
    hsm_RegularState,
)
hsm_InitialState_strategy = st.builds(
    hsm_InitialState,
)
hsm_CompositeState_strategy = st.builds(
    hsm_CompositeState,
)

@given(instance=hsm_Root_strategy)
@settings(max_examples=50)
def test_hsm_root_instantiation(instance):
    assert isinstance(instance, hsm_Root)

@given(instance=hsm_AbstractState_strategy)
@settings(max_examples=50)
def test_hsm_abstractstate_instantiation(instance):
    assert isinstance(instance, hsm_AbstractState)



@given(instance=hsm_AbstractState_strategy)
def test_hsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hsm_Transition_strategy)
@settings(max_examples=50)
def test_hsm_transition_instantiation(instance):
    assert isinstance(instance, hsm_Transition)



@given(instance=hsm_Transition_strategy)
def test_hsm_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=hsm_StateMachine_strategy)
@settings(max_examples=50)
def test_hsm_statemachine_instantiation(instance):
    assert isinstance(instance, hsm_StateMachine)



@given(instance=hsm_StateMachine_strategy)
def test_hsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hsm_RegularState_strategy)
@settings(max_examples=50)
def test_hsm_regularstate_instantiation(instance):
    assert isinstance(instance, hsm_RegularState)

@given(instance=hsm_InitialState_strategy)
@settings(max_examples=50)
def test_hsm_initialstate_instantiation(instance):
    assert isinstance(instance, hsm_InitialState)

@given(instance=hsm_CompositeState_strategy)
@settings(max_examples=50)
def test_hsm_compositestate_instantiation(instance):
    assert isinstance(instance, hsm_CompositeState)
