import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    oclstates_CompoundState,
    oclstates_SimpleState,
    oclstates_Transition,
    oclstates_State,
    oclstates_Event,
    oclstates_Statemachine,
    oclstates_Module,
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



def test_oclstates_compoundstate_is_not_abstract():
    assert not inspect.isabstract(oclstates_CompoundState)


def test_oclstates_compoundstate_constructor_exists():
    assert callable(oclstates_CompoundState.__init__)


def test_oclstates_compoundstate_constructor_args():
    sig = inspect.signature(oclstates_CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_oclstates_simplestate_is_not_abstract():
    assert not inspect.isabstract(oclstates_SimpleState)


def test_oclstates_simplestate_constructor_exists():
    assert callable(oclstates_SimpleState.__init__)


def test_oclstates_simplestate_constructor_args():
    sig = inspect.signature(oclstates_SimpleState.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oclstates_simplestate_has_value():
    assert hasattr(oclstates_SimpleState, "value")
    descriptor = None
    for klass in oclstates_SimpleState.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclstates_transition_is_not_abstract():
    assert not inspect.isabstract(oclstates_Transition)


def test_oclstates_transition_constructor_exists():
    assert callable(oclstates_Transition.__init__)


def test_oclstates_transition_constructor_args():
    sig = inspect.signature(oclstates_Transition.__init__)
    params = list(sig.parameters.keys())



def test_oclstates_state_is_not_abstract():
    assert not inspect.isabstract(oclstates_State)


def test_oclstates_state_constructor_exists():
    assert callable(oclstates_State.__init__)


def test_oclstates_state_constructor_args():
    sig = inspect.signature(oclstates_State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates_state_has_initial():
    assert hasattr(oclstates_State, "initial")
    descriptor = None
    for klass in oclstates_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_oclstates_state_has_name():
    assert hasattr(oclstates_State, "name")
    descriptor = None
    for klass in oclstates_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstates_event_is_not_abstract():
    assert not inspect.isabstract(oclstates_Event)


def test_oclstates_event_constructor_exists():
    assert callable(oclstates_Event.__init__)


def test_oclstates_event_constructor_args():
    sig = inspect.signature(oclstates_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates_event_has_name():
    assert hasattr(oclstates_Event, "name")
    descriptor = None
    for klass in oclstates_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstates_statemachine_is_not_abstract():
    assert not inspect.isabstract(oclstates_Statemachine)


def test_oclstates_statemachine_constructor_exists():
    assert callable(oclstates_Statemachine.__init__)


def test_oclstates_statemachine_constructor_args():
    sig = inspect.signature(oclstates_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_oclstates_statemachine_has_initial():
    assert hasattr(oclstates_Statemachine, "initial")
    descriptor = None
    for klass in oclstates_Statemachine.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_oclstates_statemachine_has_name():
    assert hasattr(oclstates_Statemachine, "name")
    descriptor = None
    for klass in oclstates_Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oclstates_statemachine_has_value():
    assert hasattr(oclstates_Statemachine, "value")
    descriptor = None
    for klass in oclstates_Statemachine.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclstates_module_is_not_abstract():
    assert not inspect.isabstract(oclstates_Module)


def test_oclstates_module_constructor_exists():
    assert callable(oclstates_Module.__init__)


def test_oclstates_module_constructor_args():
    sig = inspect.signature(oclstates_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates_module_has_name():
    assert hasattr(oclstates_Module, "name")
    descriptor = None
    for klass in oclstates_Module.__mro__:
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
oclstates_CompoundState_strategy = st.builds(
    oclstates_CompoundState,
)
oclstates_SimpleState_strategy = st.builds(
    oclstates_SimpleState,
    value=
        st.integers()
)
oclstates_Transition_strategy = st.builds(
    oclstates_Transition,
)
oclstates_State_strategy = st.builds(
    oclstates_State,
    initial=
        st.booleans(),
    name=
        safe_text
)
oclstates_Event_strategy = st.builds(
    oclstates_Event,
    name=
        safe_text
)
oclstates_Statemachine_strategy = st.builds(
    oclstates_Statemachine,
    initial=
        st.booleans(),
    name=
        safe_text,
    value=
        st.integers()
)
oclstates_Module_strategy = st.builds(
    oclstates_Module,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=oclstates_CompoundState_strategy)
@settings(max_examples=50)
def test_oclstates_compoundstate_instantiation(instance):
    assert isinstance(instance, oclstates_CompoundState)

@given(instance=oclstates_SimpleState_strategy)
@settings(max_examples=50)
def test_oclstates_simplestate_instantiation(instance):
    assert isinstance(instance, oclstates_SimpleState)



@given(instance=oclstates_SimpleState_strategy)
def test_oclstates_simplestate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclstates_Transition_strategy)
@settings(max_examples=50)
def test_oclstates_transition_instantiation(instance):
    assert isinstance(instance, oclstates_Transition)

@given(instance=oclstates_State_strategy)
@settings(max_examples=50)
def test_oclstates_state_instantiation(instance):
    assert isinstance(instance, oclstates_State)



@given(instance=oclstates_State_strategy)
def test_oclstates_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=oclstates_State_strategy)
def test_oclstates_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstates_Event_strategy)
@settings(max_examples=50)
def test_oclstates_event_instantiation(instance):
    assert isinstance(instance, oclstates_Event)



@given(instance=oclstates_Event_strategy)
def test_oclstates_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstates_Statemachine_strategy)
@settings(max_examples=50)
def test_oclstates_statemachine_instantiation(instance):
    assert isinstance(instance, oclstates_Statemachine)



@given(instance=oclstates_Statemachine_strategy)
def test_oclstates_statemachine_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=oclstates_Statemachine_strategy)
def test_oclstates_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oclstates_Statemachine_strategy)
def test_oclstates_statemachine_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclstates_Module_strategy)
@settings(max_examples=50)
def test_oclstates_module_instantiation(instance):
    assert isinstance(instance, oclstates_Module)



@given(instance=oclstates_Module_strategy)
def test_oclstates_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
