import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Named,
    AbstractState,
    statemachine_State,
    statemachine_Initial,
    Named,
    statemachine_Transition,
    statemachine_AbstractState,
    statemachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_named_is_not_abstract():
    assert not inspect.isabstract(statemachine_Named)


def test_statemachine_named_constructor_exists():
    assert callable(statemachine_Named.__init__)


def test_statemachine_named_constructor_args():
    sig = inspect.signature(statemachine_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_named_has_name():
    assert hasattr(statemachine_Named, "name")
    descriptor = None
    for klass in statemachine_Named.__mro__:
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



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initial_is_not_abstract():
    assert not inspect.isabstract(statemachine_Initial)


def test_statemachine_initial_constructor_exists():
    assert callable(statemachine_Initial.__init__)


def test_statemachine_initial_constructor_args():
    sig = inspect.signature(statemachine_Initial.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractState)


def test_statemachine_abstractstate_constructor_exists():
    assert callable(statemachine_AbstractState.__init__)


def test_statemachine_abstractstate_constructor_args():
    sig = inspect.signature(statemachine_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
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
statemachine_Named_strategy = st.builds(
    statemachine_Named,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
statemachine_Initial_strategy = st.builds(
    statemachine_Initial,
)
Named_strategy = st.builds(
    Named,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_AbstractState_strategy = st.builds(
    statemachine_AbstractState,
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)

@given(instance=statemachine_Named_strategy)
@settings(max_examples=50)
def test_statemachine_named_instantiation(instance):
    assert isinstance(instance, statemachine_Named)



@given(instance=statemachine_Named_strategy)
def test_statemachine_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)

@given(instance=statemachine_Initial_strategy)
@settings(max_examples=50)
def test_statemachine_initial_instantiation(instance):
    assert isinstance(instance, statemachine_Initial)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine_abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)
