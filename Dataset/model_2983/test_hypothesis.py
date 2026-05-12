import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    turingmodel_Transition,
    turingmodel_State,
    turingmodel_TuringMachine,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_turingmodel_transition_is_not_abstract():
    assert not inspect.isabstract(turingmodel_Transition)


def test_turingmodel_transition_constructor_exists():
    assert callable(turingmodel_Transition.__init__)


def test_turingmodel_transition_constructor_args():
    sig = inspect.signature(turingmodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "dir" in params, "Missing parameter 'dir'"
    assert "write" in params, "Missing parameter 'write'"

def test_turingmodel_transition_has_condition():
    assert hasattr(turingmodel_Transition, "condition")
    descriptor = None
    for klass in turingmodel_Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel_transition_has_dir():
    assert hasattr(turingmodel_Transition, "dir")
    descriptor = None
    for klass in turingmodel_Transition.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel_transition_has_write():
    assert hasattr(turingmodel_Transition, "write")
    descriptor = None
    for klass in turingmodel_Transition.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)



def test_turingmodel_state_is_not_abstract():
    assert not inspect.isabstract(turingmodel_State)


def test_turingmodel_state_constructor_exists():
    assert callable(turingmodel_State.__init__)


def test_turingmodel_state_constructor_args():
    sig = inspect.signature(turingmodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isEndState" in params, "Missing parameter 'isEndState'"

def test_turingmodel_state_has_name():
    assert hasattr(turingmodel_State, "name")
    descriptor = None
    for klass in turingmodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_turingmodel_state_has_isEndState():
    assert hasattr(turingmodel_State, "isEndState")
    descriptor = None
    for klass in turingmodel_State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)



def test_turingmodel_turingmachine_is_not_abstract():
    assert not inspect.isabstract(turingmodel_TuringMachine)


def test_turingmodel_turingmachine_constructor_exists():
    assert callable(turingmodel_TuringMachine.__init__)


def test_turingmodel_turingmachine_constructor_args():
    sig = inspect.signature(turingmodel_TuringMachine.__init__)
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
turingmodel_Transition_strategy = st.builds(
    turingmodel_Transition,
    condition=
        safe_text,
    dir=
        safe_text,
    write=
        safe_text
)
turingmodel_State_strategy = st.builds(
    turingmodel_State,
    name=
        safe_text,
    isEndState=
        st.booleans()
)
turingmodel_TuringMachine_strategy = st.builds(
    turingmodel_TuringMachine,
)

@given(instance=turingmodel_Transition_strategy)
@settings(max_examples=50)
def test_turingmodel_transition_instantiation(instance):
    assert isinstance(instance, turingmodel_Transition)



@given(instance=turingmodel_Transition_strategy)
def test_turingmodel_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original



@given(instance=turingmodel_Transition_strategy)
def test_turingmodel_transition_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original



@given(instance=turingmodel_Transition_strategy)
def test_turingmodel_transition_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=turingmodel_State_strategy)
@settings(max_examples=50)
def test_turingmodel_state_instantiation(instance):
    assert isinstance(instance, turingmodel_State)



@given(instance=turingmodel_State_strategy)
def test_turingmodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=turingmodel_State_strategy)
def test_turingmodel_state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original

@given(instance=turingmodel_TuringMachine_strategy)
@settings(max_examples=50)
def test_turingmodel_turingmachine_instantiation(instance):
    assert isinstance(instance, turingmodel_TuringMachine)
