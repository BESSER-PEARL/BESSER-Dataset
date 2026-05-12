import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    efsm_AbstractState,
    efsm_ContextVariable,
    efsm_State,
    efsm_InitialState,
    efsm_Transition,
    efsm_EFSM,
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



def test_efsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(efsm_AbstractState)


def test_efsm_abstractstate_constructor_exists():
    assert callable(efsm_AbstractState.__init__)


def test_efsm_abstractstate_constructor_args():
    sig = inspect.signature(efsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_abstractstate_has_name():
    assert hasattr(efsm_AbstractState, "name")
    descriptor = None
    for klass in efsm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm_contextvariable_is_not_abstract():
    assert not inspect.isabstract(efsm_ContextVariable)


def test_efsm_contextvariable_constructor_exists():
    assert callable(efsm_ContextVariable.__init__)


def test_efsm_contextvariable_constructor_args():
    sig = inspect.signature(efsm_ContextVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_contextvariable_has_type():
    assert hasattr(efsm_ContextVariable, "type")
    descriptor = None
    for klass in efsm_ContextVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_efsm_contextvariable_has_name():
    assert hasattr(efsm_ContextVariable, "name")
    descriptor = None
    for klass in efsm_ContextVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_efsm_state_is_not_abstract():
    assert not inspect.isabstract(efsm_State)


def test_efsm_state_constructor_exists():
    assert callable(efsm_State.__init__)


def test_efsm_state_constructor_args():
    sig = inspect.signature(efsm_State.__init__)
    params = list(sig.parameters.keys())



def test_efsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(efsm_InitialState)


def test_efsm_initialstate_constructor_exists():
    assert callable(efsm_InitialState.__init__)


def test_efsm_initialstate_constructor_args():
    sig = inspect.signature(efsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_efsm_transition_is_not_abstract():
    assert not inspect.isabstract(efsm_Transition)


def test_efsm_transition_constructor_exists():
    assert callable(efsm_Transition.__init__)


def test_efsm_transition_constructor_args():
    sig = inspect.signature(efsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "event" in params, "Missing parameter 'event'"
    assert "input" in params, "Missing parameter 'input'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "action" in params, "Missing parameter 'action'"
    assert "output" in params, "Missing parameter 'output'"

def test_efsm_transition_has_name():
    assert hasattr(efsm_Transition, "name")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_event():
    assert hasattr(efsm_Transition, "event")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_input():
    assert hasattr(efsm_Transition, "input")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_guard():
    assert hasattr(efsm_Transition, "guard")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_action():
    assert hasattr(efsm_Transition, "action")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_efsm_transition_has_output():
    assert hasattr(efsm_Transition, "output")
    descriptor = None
    for klass in efsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_efsm_efsm_is_not_abstract():
    assert not inspect.isabstract(efsm_EFSM)


def test_efsm_efsm_constructor_exists():
    assert callable(efsm_EFSM.__init__)


def test_efsm_efsm_constructor_args():
    sig = inspect.signature(efsm_EFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_efsm_efsm_has_name():
    assert hasattr(efsm_EFSM, "name")
    descriptor = None
    for klass in efsm_EFSM.__mro__:
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
efsm_AbstractState_strategy = st.builds(
    efsm_AbstractState,
    name=
        safe_text
)
efsm_ContextVariable_strategy = st.builds(
    efsm_ContextVariable,
    type=
        safe_text,
    name=
        safe_text
)
efsm_State_strategy = st.builds(
    efsm_State,
)
efsm_InitialState_strategy = st.builds(
    efsm_InitialState,
)
efsm_Transition_strategy = st.builds(
    efsm_Transition,
    name=
        safe_text,
    event=
        safe_text,
    input=
        safe_text,
    guard=
        safe_text,
    action=
        safe_text,
    output=
        safe_text
)
efsm_EFSM_strategy = st.builds(
    efsm_EFSM,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=efsm_AbstractState_strategy)
@settings(max_examples=50)
def test_efsm_abstractstate_instantiation(instance):
    assert isinstance(instance, efsm_AbstractState)



@given(instance=efsm_AbstractState_strategy)
def test_efsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm_ContextVariable_strategy)
@settings(max_examples=50)
def test_efsm_contextvariable_instantiation(instance):
    assert isinstance(instance, efsm_ContextVariable)



@given(instance=efsm_ContextVariable_strategy)
def test_efsm_contextvariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=efsm_ContextVariable_strategy)
def test_efsm_contextvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=efsm_State_strategy)
@settings(max_examples=50)
def test_efsm_state_instantiation(instance):
    assert isinstance(instance, efsm_State)

@given(instance=efsm_InitialState_strategy)
@settings(max_examples=50)
def test_efsm_initialstate_instantiation(instance):
    assert isinstance(instance, efsm_InitialState)

@given(instance=efsm_Transition_strategy)
@settings(max_examples=50)
def test_efsm_transition_instantiation(instance):
    assert isinstance(instance, efsm_Transition)



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=efsm_Transition_strategy)
def test_efsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=efsm_EFSM_strategy)
@settings(max_examples=50)
def test_efsm_efsm_instantiation(instance):
    assert isinstance(instance, efsm_EFSM)



@given(instance=efsm_EFSM_strategy)
def test_efsm_efsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
