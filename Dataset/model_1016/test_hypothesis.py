import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    fsm_InitialState,
    fsm_CompositeState,
    fsm_AbstractState,
    fsm_Transition,
    fsm_StateMachine,
    fsm_Root,
    fsm_RegularState,
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



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(fsm_CompositeState)


def test_fsm_compositestate_constructor_exists():
    assert callable(fsm_CompositeState.__init__)


def test_fsm_compositestate_constructor_args():
    sig = inspect.signature(fsm_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_abstractstate_has_name():
    assert hasattr(fsm_AbstractState, "name")
    descriptor = None
    for klass in fsm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_fsm_transition_has_label():
    assert hasattr(fsm_Transition, "label")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_statemachine_has_name():
    assert hasattr(fsm_StateMachine, "name")
    descriptor = None
    for klass in fsm_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_root_is_not_abstract():
    assert not inspect.isabstract(fsm_Root)


def test_fsm_root_constructor_exists():
    assert callable(fsm_Root.__init__)


def test_fsm_root_constructor_args():
    sig = inspect.signature(fsm_Root.__init__)
    params = list(sig.parameters.keys())



def test_fsm_regularstate_is_not_abstract():
    assert not inspect.isabstract(fsm_RegularState)


def test_fsm_regularstate_constructor_exists():
    assert callable(fsm_RegularState.__init__)


def test_fsm_regularstate_constructor_args():
    sig = inspect.signature(fsm_RegularState.__init__)
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
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_CompositeState_strategy = st.builds(
    fsm_CompositeState,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
    name=
        safe_text
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    label=
        safe_text
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
    name=
        safe_text
)
fsm_Root_strategy = st.builds(
    fsm_Root,
)
fsm_RegularState_strategy = st.builds(
    fsm_RegularState,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)

@given(instance=fsm_CompositeState_strategy)
@settings(max_examples=50)
def test_fsm_compositestate_instantiation(instance):
    assert isinstance(instance, fsm_CompositeState)

@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)



@given(instance=fsm_AbstractState_strategy)
def test_fsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)



@given(instance=fsm_StateMachine_strategy)
def test_fsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Root_strategy)
@settings(max_examples=50)
def test_fsm_root_instantiation(instance):
    assert isinstance(instance, fsm_Root)

@given(instance=fsm_RegularState_strategy)
@settings(max_examples=50)
def test_fsm_regularstate_instantiation(instance):
    assert isinstance(instance, fsm_RegularState)
