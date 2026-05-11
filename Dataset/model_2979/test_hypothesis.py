import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    machine::TuringMachine,
    machine::Symbol,
    machine::Tape,
    machine::Head,
    machine::Current,
    machine::Final,
    machine::Initial,
    machine::Machine,
    machine::Transition,
    machine::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_machine::turingmachine_is_not_abstract():
    assert not inspect.isabstract(machine::TuringMachine)


def test_machine::turingmachine_constructor_exists():
    assert callable(machine::TuringMachine.__init__)


def test_machine::turingmachine_constructor_args():
    sig = inspect.signature(machine::TuringMachine.__init__)
    params = list(sig.parameters.keys())



def test_machine::symbol_is_not_abstract():
    assert not inspect.isabstract(machine::Symbol)


def test_machine::symbol_constructor_exists():
    assert callable(machine::Symbol.__init__)


def test_machine::symbol_constructor_args():
    sig = inspect.signature(machine::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "position" in params, "Missing parameter 'position'"
    assert "value" in params, "Missing parameter 'value'"

def test_machine::symbol_has_name():
    assert hasattr(machine::Symbol, "name")
    descriptor = None
    for klass in machine::Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_machine::symbol_has_position():
    assert hasattr(machine::Symbol, "position")
    descriptor = None
    for klass in machine::Symbol.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_machine::symbol_has_value():
    assert hasattr(machine::Symbol, "value")
    descriptor = None
    for klass in machine::Symbol.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_machine::tape_is_not_abstract():
    assert not inspect.isabstract(machine::Tape)


def test_machine::tape_constructor_exists():
    assert callable(machine::Tape.__init__)


def test_machine::tape_constructor_args():
    sig = inspect.signature(machine::Tape.__init__)
    params = list(sig.parameters.keys())



def test_machine::head_is_not_abstract():
    assert not inspect.isabstract(machine::Head)


def test_machine::head_constructor_exists():
    assert callable(machine::Head.__init__)


def test_machine::head_constructor_args():
    sig = inspect.signature(machine::Head.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine::head_has_name():
    assert hasattr(machine::Head, "name")
    descriptor = None
    for klass in machine::Head.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine::current_is_not_abstract():
    assert not inspect.isabstract(machine::Current)


def test_machine::current_constructor_exists():
    assert callable(machine::Current.__init__)


def test_machine::current_constructor_args():
    sig = inspect.signature(machine::Current.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine::current_has_name():
    assert hasattr(machine::Current, "name")
    descriptor = None
    for klass in machine::Current.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine::final_is_not_abstract():
    assert not inspect.isabstract(machine::Final)


def test_machine::final_constructor_exists():
    assert callable(machine::Final.__init__)


def test_machine::final_constructor_args():
    sig = inspect.signature(machine::Final.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine::final_has_name():
    assert hasattr(machine::Final, "name")
    descriptor = None
    for klass in machine::Final.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine::initial_is_not_abstract():
    assert not inspect.isabstract(machine::Initial)


def test_machine::initial_constructor_exists():
    assert callable(machine::Initial.__init__)


def test_machine::initial_constructor_args():
    sig = inspect.signature(machine::Initial.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine::initial_has_name():
    assert hasattr(machine::Initial, "name")
    descriptor = None
    for klass in machine::Initial.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine::machine_is_not_abstract():
    assert not inspect.isabstract(machine::Machine)


def test_machine::machine_constructor_exists():
    assert callable(machine::Machine.__init__)


def test_machine::machine_constructor_args():
    sig = inspect.signature(machine::Machine.__init__)
    params = list(sig.parameters.keys())



def test_machine::transition_is_not_abstract():
    assert not inspect.isabstract(machine::Transition)


def test_machine::transition_constructor_exists():
    assert callable(machine::Transition.__init__)


def test_machine::transition_constructor_args():
    sig = inspect.signature(machine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "moveTo" in params, "Missing parameter 'moveTo'"
    assert "read" in params, "Missing parameter 'read'"
    assert "write" in params, "Missing parameter 'write'"
    assert "name" in params, "Missing parameter 'name'"

def test_machine::transition_has_moveTo():
    assert hasattr(machine::Transition, "moveTo")
    descriptor = None
    for klass in machine::Transition.__mro__:
        if "moveTo" in klass.__dict__:
            descriptor = klass.__dict__["moveTo"]
            break
    assert isinstance(descriptor, property)

def test_machine::transition_has_read():
    assert hasattr(machine::Transition, "read")
    descriptor = None
    for klass in machine::Transition.__mro__:
        if "read" in klass.__dict__:
            descriptor = klass.__dict__["read"]
            break
    assert isinstance(descriptor, property)

def test_machine::transition_has_write():
    assert hasattr(machine::Transition, "write")
    descriptor = None
    for klass in machine::Transition.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)

def test_machine::transition_has_name():
    assert hasattr(machine::Transition, "name")
    descriptor = None
    for klass in machine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine::state_is_not_abstract():
    assert not inspect.isabstract(machine::State)


def test_machine::state_constructor_exists():
    assert callable(machine::State.__init__)


def test_machine::state_constructor_args():
    sig = inspect.signature(machine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine::state_has_name():
    assert hasattr(machine::State, "name")
    descriptor = None
    for klass in machine::State.__mro__:
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
machine::TuringMachine_strategy = st.builds(
    machine::TuringMachine,
)
machine::Symbol_strategy = st.builds(
    machine::Symbol,
    name=
        safe_text,
    position=
        safe_text,
    value=
        safe_text
)
machine::Tape_strategy = st.builds(
    machine::Tape,
)
machine::Head_strategy = st.builds(
    machine::Head,
    name=
        safe_text
)
machine::Current_strategy = st.builds(
    machine::Current,
    name=
        safe_text
)
machine::Final_strategy = st.builds(
    machine::Final,
    name=
        safe_text
)
machine::Initial_strategy = st.builds(
    machine::Initial,
    name=
        safe_text
)
machine::Machine_strategy = st.builds(
    machine::Machine,
)
machine::Transition_strategy = st.builds(
    machine::Transition,
    moveTo=
        safe_text,
    read=
        safe_text,
    write=
        safe_text,
    name=
        safe_text
)
machine::State_strategy = st.builds(
    machine::State,
    name=
        safe_text
)

@given(instance=machine::TuringMachine_strategy)
@settings(max_examples=50)
def test_machine::turingmachine_instantiation(instance):
    assert isinstance(instance, machine::TuringMachine)

@given(instance=machine::Symbol_strategy)
@settings(max_examples=50)
def test_machine::symbol_instantiation(instance):
    assert isinstance(instance, machine::Symbol)

@given(instance=machine::Symbol_strategy)
def test_machine::symbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Symbol_strategy)
def test_machine::symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::Symbol_strategy)
def test_machine::symbol_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=machine::Symbol_strategy)
def test_machine::symbol_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=machine::Symbol_strategy)
def test_machine::symbol_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=machine::Symbol_strategy)
def test_machine::symbol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=machine::Tape_strategy)
@settings(max_examples=50)
def test_machine::tape_instantiation(instance):
    assert isinstance(instance, machine::Tape)

@given(instance=machine::Head_strategy)
@settings(max_examples=50)
def test_machine::head_instantiation(instance):
    assert isinstance(instance, machine::Head)

@given(instance=machine::Head_strategy)
def test_machine::head_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Head_strategy)
def test_machine::head_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::Current_strategy)
@settings(max_examples=50)
def test_machine::current_instantiation(instance):
    assert isinstance(instance, machine::Current)

@given(instance=machine::Current_strategy)
def test_machine::current_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Current_strategy)
def test_machine::current_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::Final_strategy)
@settings(max_examples=50)
def test_machine::final_instantiation(instance):
    assert isinstance(instance, machine::Final)

@given(instance=machine::Final_strategy)
def test_machine::final_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Final_strategy)
def test_machine::final_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::Initial_strategy)
@settings(max_examples=50)
def test_machine::initial_instantiation(instance):
    assert isinstance(instance, machine::Initial)

@given(instance=machine::Initial_strategy)
def test_machine::initial_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Initial_strategy)
def test_machine::initial_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::Machine_strategy)
@settings(max_examples=50)
def test_machine::machine_instantiation(instance):
    assert isinstance(instance, machine::Machine)

@given(instance=machine::Transition_strategy)
@settings(max_examples=50)
def test_machine::transition_instantiation(instance):
    assert isinstance(instance, machine::Transition)

@given(instance=machine::Transition_strategy)
def test_machine::transition_moveTo_type(instance):
    assert isinstance(instance.moveTo, str)


@given(instance=machine::Transition_strategy)
def test_machine::transition_moveTo_setter(instance):
    original = instance.moveTo
    instance.moveTo = original
    assert instance.moveTo == original

@given(instance=machine::Transition_strategy)
def test_machine::transition_read_type(instance):
    assert isinstance(instance.read, str)


@given(instance=machine::Transition_strategy)
def test_machine::transition_read_setter(instance):
    original = instance.read
    instance.read = original
    assert instance.read == original

@given(instance=machine::Transition_strategy)
def test_machine::transition_write_type(instance):
    assert isinstance(instance.write, str)


@given(instance=machine::Transition_strategy)
def test_machine::transition_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=machine::Transition_strategy)
def test_machine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::Transition_strategy)
def test_machine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine::State_strategy)
@settings(max_examples=50)
def test_machine::state_instantiation(instance):
    assert isinstance(instance, machine::State)

@given(instance=machine::State_strategy)
def test_machine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=machine::State_strategy)
def test_machine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
