import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    states_CompoundState,
    states_SimpleState,
    states_Transition,
    states_State,
    states_Event,
    states_Statemachine,
    states_Module,
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



def test_states_compoundstate_is_not_abstract():
    assert not inspect.isabstract(states_CompoundState)


def test_states_compoundstate_constructor_exists():
    assert callable(states_CompoundState.__init__)


def test_states_compoundstate_constructor_args():
    sig = inspect.signature(states_CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_states_simplestate_is_not_abstract():
    assert not inspect.isabstract(states_SimpleState)


def test_states_simplestate_constructor_exists():
    assert callable(states_SimpleState.__init__)


def test_states_simplestate_constructor_args():
    sig = inspect.signature(states_SimpleState.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_states_simplestate_has_value():
    assert hasattr(states_SimpleState, "value")
    descriptor = None
    for klass in states_SimpleState.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_states_transition_is_not_abstract():
    assert not inspect.isabstract(states_Transition)


def test_states_transition_constructor_exists():
    assert callable(states_Transition.__init__)


def test_states_transition_constructor_args():
    sig = inspect.signature(states_Transition.__init__)
    params = list(sig.parameters.keys())



def test_states_state_is_not_abstract():
    assert not inspect.isabstract(states_State)


def test_states_state_constructor_exists():
    assert callable(states_State.__init__)


def test_states_state_constructor_args():
    sig = inspect.signature(states_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_states_state_has_name():
    assert hasattr(states_State, "name")
    descriptor = None
    for klass in states_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_states_state_has_initial():
    assert hasattr(states_State, "initial")
    descriptor = None
    for klass in states_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_states_event_is_not_abstract():
    assert not inspect.isabstract(states_Event)


def test_states_event_constructor_exists():
    assert callable(states_Event.__init__)


def test_states_event_constructor_args():
    sig = inspect.signature(states_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_states_event_has_name():
    assert hasattr(states_Event, "name")
    descriptor = None
    for klass in states_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_states_statemachine_is_not_abstract():
    assert not inspect.isabstract(states_Statemachine)


def test_states_statemachine_constructor_exists():
    assert callable(states_Statemachine.__init__)


def test_states_statemachine_constructor_args():
    sig = inspect.signature(states_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_states_statemachine_has_name():
    assert hasattr(states_Statemachine, "name")
    descriptor = None
    for klass in states_Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_states_statemachine_has_value():
    assert hasattr(states_Statemachine, "value")
    descriptor = None
    for klass in states_Statemachine.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_states_statemachine_has_initial():
    assert hasattr(states_Statemachine, "initial")
    descriptor = None
    for klass in states_Statemachine.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_states_module_is_not_abstract():
    assert not inspect.isabstract(states_Module)


def test_states_module_constructor_exists():
    assert callable(states_Module.__init__)


def test_states_module_constructor_args():
    sig = inspect.signature(states_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_states_module_has_name():
    assert hasattr(states_Module, "name")
    descriptor = None
    for klass in states_Module.__mro__:
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
states_CompoundState_strategy = st.builds(
    states_CompoundState,
)
states_SimpleState_strategy = st.builds(
    states_SimpleState,
    value=
        st.integers()
)
states_Transition_strategy = st.builds(
    states_Transition,
)
states_State_strategy = st.builds(
    states_State,
    name=
        safe_text,
    initial=
        st.booleans()
)
states_Event_strategy = st.builds(
    states_Event,
    name=
        safe_text
)
states_Statemachine_strategy = st.builds(
    states_Statemachine,
    name=
        safe_text,
    value=
        st.integers(),
    initial=
        st.booleans()
)
states_Module_strategy = st.builds(
    states_Module,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=states_CompoundState_strategy)
@settings(max_examples=50)
def test_states_compoundstate_instantiation(instance):
    assert isinstance(instance, states_CompoundState)

@given(instance=states_SimpleState_strategy)
@settings(max_examples=50)
def test_states_simplestate_instantiation(instance):
    assert isinstance(instance, states_SimpleState)



@given(instance=states_SimpleState_strategy)
def test_states_simplestate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=states_Transition_strategy)
@settings(max_examples=50)
def test_states_transition_instantiation(instance):
    assert isinstance(instance, states_Transition)

@given(instance=states_State_strategy)
@settings(max_examples=50)
def test_states_state_instantiation(instance):
    assert isinstance(instance, states_State)



@given(instance=states_State_strategy)
def test_states_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=states_State_strategy)
def test_states_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=states_Event_strategy)
@settings(max_examples=50)
def test_states_event_instantiation(instance):
    assert isinstance(instance, states_Event)



@given(instance=states_Event_strategy)
def test_states_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=states_Statemachine_strategy)
@settings(max_examples=50)
def test_states_statemachine_instantiation(instance):
    assert isinstance(instance, states_Statemachine)



@given(instance=states_Statemachine_strategy)
def test_states_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=states_Statemachine_strategy)
def test_states_statemachine_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=states_Statemachine_strategy)
def test_states_statemachine_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=states_Module_strategy)
@settings(max_examples=50)
def test_states_module_instantiation(instance):
    assert isinstance(instance, states_Module)



@given(instance=states_Module_strategy)
def test_states_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
