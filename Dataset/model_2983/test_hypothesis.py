import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    turingmodel::Transition,
    turingmodel::State,
    turingmodel::TuringMachine,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_turingmodel::transition_is_not_abstract():
    assert not inspect.isabstract(turingmodel::Transition)


def test_turingmodel::transition_constructor_exists():
    assert callable(turingmodel::Transition.__init__)


def test_turingmodel::transition_constructor_args():
    sig = inspect.signature(turingmodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "write" in params, "Missing parameter 'write'"
    assert "dir" in params, "Missing parameter 'dir'"

def test_turingmodel::transition_has_condition():
    assert hasattr(turingmodel::Transition, "condition")
    descriptor = None
    for klass in turingmodel::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel::transition_has_write():
    assert hasattr(turingmodel::Transition, "write")
    descriptor = None
    for klass in turingmodel::Transition.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel::transition_has_dir():
    assert hasattr(turingmodel::Transition, "dir")
    descriptor = None
    for klass in turingmodel::Transition.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_turingmodel::state_is_not_abstract():
    assert not inspect.isabstract(turingmodel::State)


def test_turingmodel::state_constructor_exists():
    assert callable(turingmodel::State.__init__)


def test_turingmodel::state_constructor_args():
    sig = inspect.signature(turingmodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "isEndState" in params, "Missing parameter 'isEndState'"
    assert "name" in params, "Missing parameter 'name'"

def test_turingmodel::state_has_isEndState():
    assert hasattr(turingmodel::State, "isEndState")
    descriptor = None
    for klass in turingmodel::State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel::state_has_name():
    assert hasattr(turingmodel::State, "name")
    descriptor = None
    for klass in turingmodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_turingmodel::turingmachine_is_not_abstract():
    assert not inspect.isabstract(turingmodel::TuringMachine)


def test_turingmodel::turingmachine_constructor_exists():
    assert callable(turingmodel::TuringMachine.__init__)


def test_turingmodel::turingmachine_constructor_args():
    sig = inspect.signature(turingmodel::TuringMachine.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "LEFT",
        "RIGHT",
        "HOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
turingmodel::Transition_strategy = st.builds(
    turingmodel::Transition,
    condition=
        safe_text,
    write=
        safe_text,
    dir=
        safe_text
)
turingmodel::State_strategy = st.builds(
    turingmodel::State,
    isEndState=
        st.booleans(),
    name=
        safe_text
)
turingmodel::TuringMachine_strategy = st.builds(
    turingmodel::TuringMachine,
)

@given(instance=turingmodel::Transition_strategy)
@settings(max_examples=50)
def test_turingmodel::transition_instantiation(instance):
    assert isinstance(instance, turingmodel::Transition)

@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_write_type(instance):
    assert isinstance(instance.write, str)


@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=turingmodel::Transition_strategy)
def test_turingmodel::transition_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=turingmodel::State_strategy)
@settings(max_examples=50)
def test_turingmodel::state_instantiation(instance):
    assert isinstance(instance, turingmodel::State)

@given(instance=turingmodel::State_strategy)
def test_turingmodel::state_isEndState_type(instance):
    assert isinstance(instance.isEndState, bool)


@given(instance=turingmodel::State_strategy)
def test_turingmodel::state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original

@given(instance=turingmodel::State_strategy)
def test_turingmodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=turingmodel::State_strategy)
def test_turingmodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=turingmodel::TuringMachine_strategy)
@settings(max_examples=50)
def test_turingmodel::turingmachine_instantiation(instance):
    assert isinstance(instance, turingmodel::TuringMachine)
