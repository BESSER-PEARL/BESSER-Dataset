import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stm_GuardCall,
    stm_Parameter,
    stm_State,
    stm_Transition,
    stm_SelfEvent,
    stm_Guard,
    stm_Command,
    stm_Event,
    stm_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stm_guardcall_is_not_abstract():
    assert not inspect.isabstract(stm_GuardCall)


def test_stm_guardcall_constructor_exists():
    assert callable(stm_GuardCall.__init__)


def test_stm_guardcall_constructor_args():
    sig = inspect.signature(stm_GuardCall.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_stm_guardcall_has_parameters():
    assert hasattr(stm_GuardCall, "parameters")
    descriptor = None
    for klass in stm_GuardCall.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_stm_parameter_is_not_abstract():
    assert not inspect.isabstract(stm_Parameter)


def test_stm_parameter_constructor_exists():
    assert callable(stm_Parameter.__init__)


def test_stm_parameter_constructor_args():
    sig = inspect.signature(stm_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_stm_parameter_has_type():
    assert hasattr(stm_Parameter, "type")
    descriptor = None
    for klass in stm_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stm_parameter_has_name():
    assert hasattr(stm_Parameter, "name")
    descriptor = None
    for klass in stm_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm_state_is_not_abstract():
    assert not inspect.isabstract(stm_State)


def test_stm_state_constructor_exists():
    assert callable(stm_State.__init__)


def test_stm_state_constructor_args():
    sig = inspect.signature(stm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm_state_has_name():
    assert hasattr(stm_State, "name")
    descriptor = None
    for klass in stm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm_transition_is_not_abstract():
    assert not inspect.isabstract(stm_Transition)


def test_stm_transition_constructor_exists():
    assert callable(stm_Transition.__init__)


def test_stm_transition_constructor_args():
    sig = inspect.signature(stm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_stm_selfevent_is_not_abstract():
    assert not inspect.isabstract(stm_SelfEvent)


def test_stm_selfevent_constructor_exists():
    assert callable(stm_SelfEvent.__init__)


def test_stm_selfevent_constructor_args():
    sig = inspect.signature(stm_SelfEvent.__init__)
    params = list(sig.parameters.keys())



def test_stm_guard_is_not_abstract():
    assert not inspect.isabstract(stm_Guard)


def test_stm_guard_constructor_exists():
    assert callable(stm_Guard.__init__)


def test_stm_guard_constructor_args():
    sig = inspect.signature(stm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm_guard_has_name():
    assert hasattr(stm_Guard, "name")
    descriptor = None
    for klass in stm_Guard.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm_command_is_not_abstract():
    assert not inspect.isabstract(stm_Command)


def test_stm_command_constructor_exists():
    assert callable(stm_Command.__init__)


def test_stm_command_constructor_args():
    sig = inspect.signature(stm_Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm_command_has_name():
    assert hasattr(stm_Command, "name")
    descriptor = None
    for klass in stm_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm_event_is_not_abstract():
    assert not inspect.isabstract(stm_Event)


def test_stm_event_constructor_exists():
    assert callable(stm_Event.__init__)


def test_stm_event_constructor_args():
    sig = inspect.signature(stm_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stm_event_has_name():
    assert hasattr(stm_Event, "name")
    descriptor = None
    for klass in stm_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stm_statemachine_is_not_abstract():
    assert not inspect.isabstract(stm_Statemachine)


def test_stm_statemachine_constructor_exists():
    assert callable(stm_Statemachine.__init__)


def test_stm_statemachine_constructor_args():
    sig = inspect.signature(stm_Statemachine.__init__)
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
stm_GuardCall_strategy = st.builds(
    stm_GuardCall,
    parameters=
        safe_text
)
stm_Parameter_strategy = st.builds(
    stm_Parameter,
    type=
        safe_text,
    name=
        safe_text
)
stm_State_strategy = st.builds(
    stm_State,
    name=
        safe_text
)
stm_Transition_strategy = st.builds(
    stm_Transition,
)
stm_SelfEvent_strategy = st.builds(
    stm_SelfEvent,
)
stm_Guard_strategy = st.builds(
    stm_Guard,
    name=
        safe_text
)
stm_Command_strategy = st.builds(
    stm_Command,
    name=
        safe_text
)
stm_Event_strategy = st.builds(
    stm_Event,
    name=
        safe_text
)
stm_Statemachine_strategy = st.builds(
    stm_Statemachine,
)

@given(instance=stm_GuardCall_strategy)
@settings(max_examples=50)
def test_stm_guardcall_instantiation(instance):
    assert isinstance(instance, stm_GuardCall)



@given(instance=stm_GuardCall_strategy)
def test_stm_guardcall_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=stm_Parameter_strategy)
@settings(max_examples=50)
def test_stm_parameter_instantiation(instance):
    assert isinstance(instance, stm_Parameter)



@given(instance=stm_Parameter_strategy)
def test_stm_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stm_Parameter_strategy)
def test_stm_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm_State_strategy)
@settings(max_examples=50)
def test_stm_state_instantiation(instance):
    assert isinstance(instance, stm_State)



@given(instance=stm_State_strategy)
def test_stm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm_Transition_strategy)
@settings(max_examples=50)
def test_stm_transition_instantiation(instance):
    assert isinstance(instance, stm_Transition)

@given(instance=stm_SelfEvent_strategy)
@settings(max_examples=50)
def test_stm_selfevent_instantiation(instance):
    assert isinstance(instance, stm_SelfEvent)

@given(instance=stm_Guard_strategy)
@settings(max_examples=50)
def test_stm_guard_instantiation(instance):
    assert isinstance(instance, stm_Guard)



@given(instance=stm_Guard_strategy)
def test_stm_guard_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm_Command_strategy)
@settings(max_examples=50)
def test_stm_command_instantiation(instance):
    assert isinstance(instance, stm_Command)



@given(instance=stm_Command_strategy)
def test_stm_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm_Event_strategy)
@settings(max_examples=50)
def test_stm_event_instantiation(instance):
    assert isinstance(instance, stm_Event)



@given(instance=stm_Event_strategy)
def test_stm_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stm_Statemachine_strategy)
@settings(max_examples=50)
def test_stm_statemachine_instantiation(instance):
    assert isinstance(instance, stm_Statemachine)
