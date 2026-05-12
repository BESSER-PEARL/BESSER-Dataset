import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Thing,
    statemachine_Transition,
    statemachine_Value,
    Guard,
    statemachine_RangeGuard,
    statemachine_ValueGuard,
    statemachine_Guard,
    statemachine_State,
    statemachine_Constant,
    statemachine_Command,
    statemachine_Event,
    statemachine_Statemachine,
    Value,
    statemachine_IntLiteral,
    statemachine_ConstantRef,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_thing_is_not_abstract():
    assert not inspect.isabstract(statemachine_Thing)


def test_statemachine_thing_constructor_exists():
    assert callable(statemachine_Thing.__init__)


def test_statemachine_thing_constructor_args():
    sig = inspect.signature(statemachine_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_thing_has_name():
    assert hasattr(statemachine_Thing, "name")
    descriptor = None
    for klass in statemachine_Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_value_is_not_abstract():
    assert not inspect.isabstract(statemachine_Value)


def test_statemachine_value_constructor_exists():
    assert callable(statemachine_Value.__init__)


def test_statemachine_value_constructor_args():
    sig = inspect.signature(statemachine_Value.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_rangeguard_is_not_abstract():
    assert not inspect.isabstract(statemachine_RangeGuard)


def test_statemachine_rangeguard_constructor_exists():
    assert callable(statemachine_RangeGuard.__init__)


def test_statemachine_rangeguard_constructor_args():
    sig = inspect.signature(statemachine_RangeGuard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_valueguard_is_not_abstract():
    assert not inspect.isabstract(statemachine_ValueGuard)


def test_statemachine_valueguard_constructor_exists():
    assert callable(statemachine_ValueGuard.__init__)


def test_statemachine_valueguard_constructor_args():
    sig = inspect.signature(statemachine_ValueGuard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_guard_is_not_abstract():
    assert not inspect.isabstract(statemachine_Guard)


def test_statemachine_guard_constructor_exists():
    assert callable(statemachine_Guard.__init__)


def test_statemachine_guard_constructor_args():
    sig = inspect.signature(statemachine_Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_description():
    assert hasattr(statemachine_State, "description")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_constant_is_not_abstract():
    assert not inspect.isabstract(statemachine_Constant)


def test_statemachine_constant_constructor_exists():
    assert callable(statemachine_Constant.__init__)


def test_statemachine_constant_constructor_args():
    sig = inspect.signature(statemachine_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_constant_has_name():
    assert hasattr(statemachine_Constant, "name")
    descriptor = None
    for klass in statemachine_Constant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(statemachine_Command)


def test_statemachine_command_constructor_exists():
    assert callable(statemachine_Command.__init__)


def test_statemachine_command_constructor_args():
    sig = inspect.signature(statemachine_Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_command_has_code():
    assert hasattr(statemachine_Command, "code")
    descriptor = None
    for klass in statemachine_Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_command_has_name():
    assert hasattr(statemachine_Command, "name")
    descriptor = None
    for klass in statemachine_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_event_has_code():
    assert hasattr(statemachine_Event, "code")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_event_has_name():
    assert hasattr(statemachine_Event, "name")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(statemachine_Statemachine, "name")
    descriptor = None
    for klass in statemachine_Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_intliteral_is_not_abstract():
    assert not inspect.isabstract(statemachine_IntLiteral)


def test_statemachine_intliteral_constructor_exists():
    assert callable(statemachine_IntLiteral.__init__)


def test_statemachine_intliteral_constructor_args():
    sig = inspect.signature(statemachine_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine_intliteral_has_value():
    assert hasattr(statemachine_IntLiteral, "value")
    descriptor = None
    for klass in statemachine_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_constantref_is_not_abstract():
    assert not inspect.isabstract(statemachine_ConstantRef)


def test_statemachine_constantref_constructor_exists():
    assert callable(statemachine_ConstantRef.__init__)


def test_statemachine_constantref_constructor_args():
    sig = inspect.signature(statemachine_ConstantRef.__init__)
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
statemachine_Thing_strategy = st.builds(
    statemachine_Thing,
    name=
        safe_text
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_Value_strategy = st.builds(
    statemachine_Value,
)
Guard_strategy = st.builds(
    Guard,
)
statemachine_RangeGuard_strategy = st.builds(
    statemachine_RangeGuard,
)
statemachine_ValueGuard_strategy = st.builds(
    statemachine_ValueGuard,
)
statemachine_Guard_strategy = st.builds(
    statemachine_Guard,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text,
    description=
        safe_text
)
statemachine_Constant_strategy = st.builds(
    statemachine_Constant,
    name=
        safe_text
)
statemachine_Command_strategy = st.builds(
    statemachine_Command,
    code=
        st.integers(),
    name=
        safe_text
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    code=
        st.integers(),
    name=
        safe_text
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
    name=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
statemachine_IntLiteral_strategy = st.builds(
    statemachine_IntLiteral,
    value=
        st.integers()
)
statemachine_ConstantRef_strategy = st.builds(
    statemachine_ConstantRef,
)

@given(instance=statemachine_Thing_strategy)
@settings(max_examples=50)
def test_statemachine_thing_instantiation(instance):
    assert isinstance(instance, statemachine_Thing)



@given(instance=statemachine_Thing_strategy)
def test_statemachine_thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_Value_strategy)
@settings(max_examples=50)
def test_statemachine_value_instantiation(instance):
    assert isinstance(instance, statemachine_Value)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=statemachine_RangeGuard_strategy)
@settings(max_examples=50)
def test_statemachine_rangeguard_instantiation(instance):
    assert isinstance(instance, statemachine_RangeGuard)

@given(instance=statemachine_ValueGuard_strategy)
@settings(max_examples=50)
def test_statemachine_valueguard_instantiation(instance):
    assert isinstance(instance, statemachine_ValueGuard)

@given(instance=statemachine_Guard_strategy)
@settings(max_examples=50)
def test_statemachine_guard_instantiation(instance):
    assert isinstance(instance, statemachine_Guard)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachine_State_strategy)
def test_statemachine_state_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statemachine_Constant_strategy)
@settings(max_examples=50)
def test_statemachine_constant_instantiation(instance):
    assert isinstance(instance, statemachine_Constant)



@given(instance=statemachine_Constant_strategy)
def test_statemachine_constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Command_strategy)
@settings(max_examples=50)
def test_statemachine_command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)



@given(instance=statemachine_Command_strategy)
def test_statemachine_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=statemachine_Command_strategy)
def test_statemachine_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)



@given(instance=statemachine_Statemachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=statemachine_IntLiteral_strategy)
@settings(max_examples=50)
def test_statemachine_intliteral_instantiation(instance):
    assert isinstance(instance, statemachine_IntLiteral)



@given(instance=statemachine_IntLiteral_strategy)
def test_statemachine_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine_ConstantRef_strategy)
@settings(max_examples=50)
def test_statemachine_constantref_instantiation(instance):
    assert isinstance(instance, statemachine_ConstantRef)
