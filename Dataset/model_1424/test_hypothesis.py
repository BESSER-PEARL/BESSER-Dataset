import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Thing,
    statemachine::Transition,
    statemachine::Value,
    Guard,
    statemachine::RangeGuard,
    statemachine::ValueGuard,
    statemachine::Guard,
    statemachine::State,
    statemachine::Constant,
    statemachine::Command,
    statemachine::Event,
    statemachine::Statemachine,
    Value,
    statemachine::IntLiteral,
    statemachine::ConstantRef,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::thing_is_not_abstract():
    assert not inspect.isabstract(statemachine::Thing)


def test_statemachine::thing_constructor_exists():
    assert callable(statemachine::Thing.__init__)


def test_statemachine::thing_constructor_args():
    sig = inspect.signature(statemachine::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::thing_has_name():
    assert hasattr(statemachine::Thing, "name")
    descriptor = None
    for klass in statemachine::Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::value_is_not_abstract():
    assert not inspect.isabstract(statemachine::Value)


def test_statemachine::value_constructor_exists():
    assert callable(statemachine::Value.__init__)


def test_statemachine::value_constructor_args():
    sig = inspect.signature(statemachine::Value.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::rangeguard_is_not_abstract():
    assert not inspect.isabstract(statemachine::RangeGuard)


def test_statemachine::rangeguard_constructor_exists():
    assert callable(statemachine::RangeGuard.__init__)


def test_statemachine::rangeguard_constructor_args():
    sig = inspect.signature(statemachine::RangeGuard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::valueguard_is_not_abstract():
    assert not inspect.isabstract(statemachine::ValueGuard)


def test_statemachine::valueguard_constructor_exists():
    assert callable(statemachine::ValueGuard.__init__)


def test_statemachine::valueguard_constructor_args():
    sig = inspect.signature(statemachine::ValueGuard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::guard_is_not_abstract():
    assert not inspect.isabstract(statemachine::Guard)


def test_statemachine::guard_constructor_exists():
    assert callable(statemachine::Guard.__init__)


def test_statemachine::guard_constructor_args():
    sig = inspect.signature(statemachine::Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_description():
    assert hasattr(statemachine::State, "description")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_name():
    assert hasattr(statemachine::State, "name")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::constant_is_not_abstract():
    assert not inspect.isabstract(statemachine::Constant)


def test_statemachine::constant_constructor_exists():
    assert callable(statemachine::Constant.__init__)


def test_statemachine::constant_constructor_args():
    sig = inspect.signature(statemachine::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::constant_has_name():
    assert hasattr(statemachine::Constant, "name")
    descriptor = None
    for klass in statemachine::Constant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::command_is_not_abstract():
    assert not inspect.isabstract(statemachine::Command)


def test_statemachine::command_constructor_exists():
    assert callable(statemachine::Command.__init__)


def test_statemachine::command_constructor_args():
    sig = inspect.signature(statemachine::Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::command_has_code():
    assert hasattr(statemachine::Command, "code")
    descriptor = None
    for klass in statemachine::Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::command_has_name():
    assert hasattr(statemachine::Command, "name")
    descriptor = None
    for klass in statemachine::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::event_has_code():
    assert hasattr(statemachine::Event, "code")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::event_has_name():
    assert hasattr(statemachine::Event, "name")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statemachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::Statemachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(statemachine::Statemachine, "name")
    descriptor = None
    for klass in statemachine::Statemachine.__mro__:
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



def test_statemachine::intliteral_is_not_abstract():
    assert not inspect.isabstract(statemachine::IntLiteral)


def test_statemachine::intliteral_constructor_exists():
    assert callable(statemachine::IntLiteral.__init__)


def test_statemachine::intliteral_constructor_args():
    sig = inspect.signature(statemachine::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine::intliteral_has_value():
    assert hasattr(statemachine::IntLiteral, "value")
    descriptor = None
    for klass in statemachine::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::constantref_is_not_abstract():
    assert not inspect.isabstract(statemachine::ConstantRef)


def test_statemachine::constantref_constructor_exists():
    assert callable(statemachine::ConstantRef.__init__)


def test_statemachine::constantref_constructor_args():
    sig = inspect.signature(statemachine::ConstantRef.__init__)
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
statemachine::Thing_strategy = st.builds(
    statemachine::Thing,
    name=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::Value_strategy = st.builds(
    statemachine::Value,
)
Guard_strategy = st.builds(
    Guard,
)
statemachine::RangeGuard_strategy = st.builds(
    statemachine::RangeGuard,
)
statemachine::ValueGuard_strategy = st.builds(
    statemachine::ValueGuard,
)
statemachine::Guard_strategy = st.builds(
    statemachine::Guard,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    description=
        safe_text,
    name=
        safe_text
)
statemachine::Constant_strategy = st.builds(
    statemachine::Constant,
    name=
        safe_text
)
statemachine::Command_strategy = st.builds(
    statemachine::Command,
    code=
        st.integers(),
    name=
        safe_text
)
statemachine::Event_strategy = st.builds(
    statemachine::Event,
    code=
        st.integers(),
    name=
        safe_text
)
statemachine::Statemachine_strategy = st.builds(
    statemachine::Statemachine,
    name=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
statemachine::IntLiteral_strategy = st.builds(
    statemachine::IntLiteral,
    value=
        st.integers()
)
statemachine::ConstantRef_strategy = st.builds(
    statemachine::ConstantRef,
)

@given(instance=statemachine::Thing_strategy)
@settings(max_examples=50)
def test_statemachine::thing_instantiation(instance):
    assert isinstance(instance, statemachine::Thing)

@given(instance=statemachine::Thing_strategy)
def test_statemachine::thing_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Thing_strategy)
def test_statemachine::thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Value_strategy)
@settings(max_examples=50)
def test_statemachine::value_instantiation(instance):
    assert isinstance(instance, statemachine::Value)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=statemachine::RangeGuard_strategy)
@settings(max_examples=50)
def test_statemachine::rangeguard_instantiation(instance):
    assert isinstance(instance, statemachine::RangeGuard)

@given(instance=statemachine::ValueGuard_strategy)
@settings(max_examples=50)
def test_statemachine::valueguard_instantiation(instance):
    assert isinstance(instance, statemachine::ValueGuard)

@given(instance=statemachine::Guard_strategy)
@settings(max_examples=50)
def test_statemachine::guard_instantiation(instance):
    assert isinstance(instance, statemachine::Guard)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Constant_strategy)
@settings(max_examples=50)
def test_statemachine::constant_instantiation(instance):
    assert isinstance(instance, statemachine::Constant)

@given(instance=statemachine::Constant_strategy)
def test_statemachine::constant_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Constant_strategy)
def test_statemachine::constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Command_strategy)
@settings(max_examples=50)
def test_statemachine::command_instantiation(instance):
    assert isinstance(instance, statemachine::Command)

@given(instance=statemachine::Command_strategy)
def test_statemachine::command_code_type(instance):
    assert isinstance(instance.code, int)


@given(instance=statemachine::Command_strategy)
def test_statemachine::command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine::Command_strategy)
def test_statemachine::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Command_strategy)
def test_statemachine::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_code_type(instance):
    assert isinstance(instance.code, int)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::Statemachine)

@given(instance=statemachine::Statemachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Statemachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=statemachine::IntLiteral_strategy)
@settings(max_examples=50)
def test_statemachine::intliteral_instantiation(instance):
    assert isinstance(instance, statemachine::IntLiteral)

@given(instance=statemachine::IntLiteral_strategy)
def test_statemachine::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=statemachine::IntLiteral_strategy)
def test_statemachine::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine::ConstantRef_strategy)
@settings(max_examples=50)
def test_statemachine::constantref_instantiation(instance):
    assert isinstance(instance, statemachine::ConstantRef)
