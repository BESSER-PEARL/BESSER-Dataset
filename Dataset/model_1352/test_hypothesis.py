import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_State,
    statemachine_FiringElement,
    statemachine_AbstractState,
    statemachine_StateMachine,
    FiringElement,
    statemachine_Transition,
    statemachine_StateAction,
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



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_firingelement_is_not_abstract():
    assert not inspect.isabstract(statemachine_FiringElement)


def test_statemachine_firingelement_constructor_exists():
    assert callable(statemachine_FiringElement.__init__)


def test_statemachine_firingelement_constructor_args():
    sig = inspect.signature(statemachine_FiringElement.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachine_firingelement_has_action():
    assert hasattr(statemachine_FiringElement, "action")
    descriptor = None
    for klass in statemachine_FiringElement.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_firingelement_has_trigger():
    assert hasattr(statemachine_FiringElement, "trigger")
    descriptor = None
    for klass in statemachine_FiringElement.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractState)


def test_statemachine_abstractstate_constructor_exists():
    assert callable(statemachine_AbstractState.__init__)


def test_statemachine_abstractstate_constructor_args():
    sig = inspect.signature(statemachine_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_abstractstate_has_name():
    assert hasattr(statemachine_AbstractState, "name")
    descriptor = None
    for klass in statemachine_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_firingelement_is_not_abstract():
    assert not inspect.isabstract(FiringElement)


def test_firingelement_constructor_exists():
    assert callable(FiringElement.__init__)


def test_firingelement_constructor_args():
    sig = inspect.signature(FiringElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_stateaction_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateAction)


def test_statemachine_stateaction_constructor_exists():
    assert callable(statemachine_StateAction.__init__)


def test_statemachine_stateaction_constructor_args():
    sig = inspect.signature(statemachine_StateAction.__init__)
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
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
statemachine_FiringElement_strategy = st.builds(
    statemachine_FiringElement,
    action=
        safe_text,
    trigger=
        safe_text
)
statemachine_AbstractState_strategy = st.builds(
    statemachine_AbstractState,
    name=
        safe_text
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)
FiringElement_strategy = st.builds(
    FiringElement,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_StateAction_strategy = st.builds(
    statemachine_StateAction,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)

@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)

@given(instance=statemachine_FiringElement_strategy)
@settings(max_examples=50)
def test_statemachine_firingelement_instantiation(instance):
    assert isinstance(instance, statemachine_FiringElement)



@given(instance=statemachine_FiringElement_strategy)
def test_statemachine_firingelement_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=statemachine_FiringElement_strategy)
def test_statemachine_firingelement_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine_abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)



@given(instance=statemachine_AbstractState_strategy)
def test_statemachine_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)

@given(instance=FiringElement_strategy)
@settings(max_examples=50)
def test_firingelement_instantiation(instance):
    assert isinstance(instance, FiringElement)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_StateAction_strategy)
@settings(max_examples=50)
def test_statemachine_stateaction_instantiation(instance):
    assert isinstance(instance, statemachine_StateAction)
