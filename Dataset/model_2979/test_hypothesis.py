import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    machine_TuringMachine,
    machine_Symbol,
    machine_Tape,
    machine_Head,
    machine_Current,
    machine_Final,
    machine_Initial,
    machine_Machine,
    machine_Transition,
    machine_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_machine_turingmachine_is_not_abstract():
    assert not inspect.isabstract(machine_TuringMachine)


def test_machine_turingmachine_constructor_exists():
    assert callable(machine_TuringMachine.__init__)


def test_machine_turingmachine_constructor_args():
    sig = inspect.signature(machine_TuringMachine.__init__)
    params = list(sig.parameters.keys())



def test_machine_symbol_is_not_abstract():
    assert not inspect.isabstract(machine_Symbol)


def test_machine_symbol_constructor_exists():
    assert callable(machine_Symbol.__init__)


def test_machine_symbol_constructor_args():
    sig = inspect.signature(machine_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_machine_symbol_has_position():
    assert hasattr(machine_Symbol, "position")
    descriptor = None
    for klass in machine_Symbol.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_machine_symbol_has_name():
    assert hasattr(machine_Symbol, "name")
    descriptor = None
    for klass in machine_Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_machine_symbol_has_value():
    assert hasattr(machine_Symbol, "value")
    descriptor = None
    for klass in machine_Symbol.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_machine_tape_is_not_abstract():
    assert not inspect.isabstract(machine_Tape)


def test_machine_tape_constructor_exists():
    assert callable(machine_Tape.__init__)


def test_machine_tape_constructor_args():
    sig = inspect.signature(machine_Tape.__init__)
    params = list(sig.parameters.keys())



def test_machine_head_is_not_abstract():
    assert not inspect.isabstract(machine_Head)


def test_machine_head_constructor_exists():
    assert callable(machine_Head.__init__)


def test_machine_head_constructor_args():
    sig = inspect.signature(machine_Head.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine_head_has_name():
    assert hasattr(machine_Head, "name")
    descriptor = None
    for klass in machine_Head.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine_current_is_not_abstract():
    assert not inspect.isabstract(machine_Current)


def test_machine_current_constructor_exists():
    assert callable(machine_Current.__init__)


def test_machine_current_constructor_args():
    sig = inspect.signature(machine_Current.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine_current_has_name():
    assert hasattr(machine_Current, "name")
    descriptor = None
    for klass in machine_Current.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine_final_is_not_abstract():
    assert not inspect.isabstract(machine_Final)


def test_machine_final_constructor_exists():
    assert callable(machine_Final.__init__)


def test_machine_final_constructor_args():
    sig = inspect.signature(machine_Final.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine_final_has_name():
    assert hasattr(machine_Final, "name")
    descriptor = None
    for klass in machine_Final.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine_initial_is_not_abstract():
    assert not inspect.isabstract(machine_Initial)


def test_machine_initial_constructor_exists():
    assert callable(machine_Initial.__init__)


def test_machine_initial_constructor_args():
    sig = inspect.signature(machine_Initial.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine_initial_has_name():
    assert hasattr(machine_Initial, "name")
    descriptor = None
    for klass in machine_Initial.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine_machine_is_not_abstract():
    assert not inspect.isabstract(machine_Machine)


def test_machine_machine_constructor_exists():
    assert callable(machine_Machine.__init__)


def test_machine_machine_constructor_args():
    sig = inspect.signature(machine_Machine.__init__)
    params = list(sig.parameters.keys())



def test_machine_transition_is_not_abstract():
    assert not inspect.isabstract(machine_Transition)


def test_machine_transition_constructor_exists():
    assert callable(machine_Transition.__init__)


def test_machine_transition_constructor_args():
    sig = inspect.signature(machine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "read" in params, "Missing parameter 'read'"
    assert "name" in params, "Missing parameter 'name'"
    assert "write" in params, "Missing parameter 'write'"
    assert "moveTo" in params, "Missing parameter 'moveTo'"

def test_machine_transition_has_read():
    assert hasattr(machine_Transition, "read")
    descriptor = None
    for klass in machine_Transition.__mro__:
        if "read" in klass.__dict__:
            descriptor = klass.__dict__["read"]
            break
    assert isinstance(descriptor, property)

def test_machine_transition_has_name():
    assert hasattr(machine_Transition, "name")
    descriptor = None
    for klass in machine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_machine_transition_has_write():
    assert hasattr(machine_Transition, "write")
    descriptor = None
    for klass in machine_Transition.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)

def test_machine_transition_has_moveTo():
    assert hasattr(machine_Transition, "moveTo")
    descriptor = None
    for klass in machine_Transition.__mro__:
        if "moveTo" in klass.__dict__:
            descriptor = klass.__dict__["moveTo"]
            break
    assert isinstance(descriptor, property)



def test_machine_state_is_not_abstract():
    assert not inspect.isabstract(machine_State)


def test_machine_state_constructor_exists():
    assert callable(machine_State.__init__)


def test_machine_state_constructor_args():
    sig = inspect.signature(machine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machine_state_has_name():
    assert hasattr(machine_State, "name")
    descriptor = None
    for klass in machine_State.__mro__:
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
machine_TuringMachine_strategy = st.builds(
    machine_TuringMachine,
)
machine_Symbol_strategy = st.builds(
    machine_Symbol,
    position=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
machine_Tape_strategy = st.builds(
    machine_Tape,
)
machine_Head_strategy = st.builds(
    machine_Head,
    name=
        safe_text
)
machine_Current_strategy = st.builds(
    machine_Current,
    name=
        safe_text
)
machine_Final_strategy = st.builds(
    machine_Final,
    name=
        safe_text
)
machine_Initial_strategy = st.builds(
    machine_Initial,
    name=
        safe_text
)
machine_Machine_strategy = st.builds(
    machine_Machine,
)
machine_Transition_strategy = st.builds(
    machine_Transition,
    read=
        safe_text,
    name=
        safe_text,
    write=
        safe_text,
    moveTo=
        safe_text
)
machine_State_strategy = st.builds(
    machine_State,
    name=
        safe_text
)

@given(instance=machine_TuringMachine_strategy)
@settings(max_examples=50)
def test_machine_turingmachine_instantiation(instance):
    assert isinstance(instance, machine_TuringMachine)

@given(instance=machine_Symbol_strategy)
@settings(max_examples=50)
def test_machine_symbol_instantiation(instance):
    assert isinstance(instance, machine_Symbol)



@given(instance=machine_Symbol_strategy)
def test_machine_symbol_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=machine_Symbol_strategy)
def test_machine_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=machine_Symbol_strategy)
def test_machine_symbol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=machine_Tape_strategy)
@settings(max_examples=50)
def test_machine_tape_instantiation(instance):
    assert isinstance(instance, machine_Tape)

@given(instance=machine_Head_strategy)
@settings(max_examples=50)
def test_machine_head_instantiation(instance):
    assert isinstance(instance, machine_Head)



@given(instance=machine_Head_strategy)
def test_machine_head_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine_Current_strategy)
@settings(max_examples=50)
def test_machine_current_instantiation(instance):
    assert isinstance(instance, machine_Current)



@given(instance=machine_Current_strategy)
def test_machine_current_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine_Final_strategy)
@settings(max_examples=50)
def test_machine_final_instantiation(instance):
    assert isinstance(instance, machine_Final)



@given(instance=machine_Final_strategy)
def test_machine_final_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine_Initial_strategy)
@settings(max_examples=50)
def test_machine_initial_instantiation(instance):
    assert isinstance(instance, machine_Initial)



@given(instance=machine_Initial_strategy)
def test_machine_initial_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=machine_Machine_strategy)
@settings(max_examples=50)
def test_machine_machine_instantiation(instance):
    assert isinstance(instance, machine_Machine)

@given(instance=machine_Transition_strategy)
@settings(max_examples=50)
def test_machine_transition_instantiation(instance):
    assert isinstance(instance, machine_Transition)



@given(instance=machine_Transition_strategy)
def test_machine_transition_read_setter(instance):
    original = instance.read
    instance.read = original
    assert instance.read == original



@given(instance=machine_Transition_strategy)
def test_machine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=machine_Transition_strategy)
def test_machine_transition_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original



@given(instance=machine_Transition_strategy)
def test_machine_transition_moveTo_setter(instance):
    original = instance.moveTo
    instance.moveTo = original
    assert instance.moveTo == original

@given(instance=machine_State_strategy)
@settings(max_examples=50)
def test_machine_state_instantiation(instance):
    assert isinstance(instance, machine_State)



@given(instance=machine_State_strategy)
def test_machine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
