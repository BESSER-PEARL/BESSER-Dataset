import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Instruction,
    minidrone_Turn,
    minidrone_Jump,
    minidrone_Go,
    minidrone_Instruction,
    minidrone_MiniDroneProgram,
    JumpType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_minidrone_turn_is_not_abstract():
    assert not inspect.isabstract(minidrone_Turn)


def test_minidrone_turn_constructor_exists():
    assert callable(minidrone_Turn.__init__)


def test_minidrone_turn_constructor_args():
    sig = inspect.signature(minidrone_Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_minidrone_turn_has_angle():
    assert hasattr(minidrone_Turn, "angle")
    descriptor = None
    for klass in minidrone_Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_minidrone_jump_is_not_abstract():
    assert not inspect.isabstract(minidrone_Jump)


def test_minidrone_jump_constructor_exists():
    assert callable(minidrone_Jump.__init__)


def test_minidrone_jump_constructor_args():
    sig = inspect.signature(minidrone_Jump.__init__)
    params = list(sig.parameters.keys())
    assert "jumpType" in params, "Missing parameter 'jumpType'"

def test_minidrone_jump_has_jumpType():
    assert hasattr(minidrone_Jump, "jumpType")
    descriptor = None
    for klass in minidrone_Jump.__mro__:
        if "jumpType" in klass.__dict__:
            descriptor = klass.__dict__["jumpType"]
            break
    assert isinstance(descriptor, property)



def test_minidrone_go_is_not_abstract():
    assert not inspect.isabstract(minidrone_Go)


def test_minidrone_go_constructor_exists():
    assert callable(minidrone_Go.__init__)


def test_minidrone_go_constructor_args():
    sig = inspect.signature(minidrone_Go.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_minidrone_go_has_distance():
    assert hasattr(minidrone_Go, "distance")
    descriptor = None
    for klass in minidrone_Go.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_minidrone_instruction_is_not_abstract():
    assert not inspect.isabstract(minidrone_Instruction)


def test_minidrone_instruction_constructor_exists():
    assert callable(minidrone_Instruction.__init__)


def test_minidrone_instruction_constructor_args():
    sig = inspect.signature(minidrone_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_minidrone_minidroneprogram_is_not_abstract():
    assert not inspect.isabstract(minidrone_MiniDroneProgram)


def test_minidrone_minidroneprogram_constructor_exists():
    assert callable(minidrone_MiniDroneProgram.__init__)


def test_minidrone_minidroneprogram_constructor_args():
    sig = inspect.signature(minidrone_MiniDroneProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minidrone_minidroneprogram_has_name():
    assert hasattr(minidrone_MiniDroneProgram, "name")
    descriptor = None
    for klass in minidrone_MiniDroneProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jumptype_exists():
    # Check that the Enumeration exists
    assert JumpType is not None

def test_jumptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpType]
    expected_literals = [
        "JUMP_LONG",
        "JUMP_HIGH",
        "JUMP_MAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpType"


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
Instruction_strategy = st.builds(
    Instruction,
)
minidrone_Turn_strategy = st.builds(
    minidrone_Turn,
    angle=
        st.integers()
)
minidrone_Jump_strategy = st.builds(
    minidrone_Jump,
    jumpType=
        safe_text
)
minidrone_Go_strategy = st.builds(
    minidrone_Go,
    distance=
        st.integers()
)
minidrone_Instruction_strategy = st.builds(
    minidrone_Instruction,
)
minidrone_MiniDroneProgram_strategy = st.builds(
    minidrone_MiniDroneProgram,
    name=
        safe_text
)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=minidrone_Turn_strategy)
@settings(max_examples=50)
def test_minidrone_turn_instantiation(instance):
    assert isinstance(instance, minidrone_Turn)



@given(instance=minidrone_Turn_strategy)
def test_minidrone_turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=minidrone_Jump_strategy)
@settings(max_examples=50)
def test_minidrone_jump_instantiation(instance):
    assert isinstance(instance, minidrone_Jump)



@given(instance=minidrone_Jump_strategy)
def test_minidrone_jump_jumpType_setter(instance):
    original = instance.jumpType
    instance.jumpType = original
    assert instance.jumpType == original

@given(instance=minidrone_Go_strategy)
@settings(max_examples=50)
def test_minidrone_go_instantiation(instance):
    assert isinstance(instance, minidrone_Go)



@given(instance=minidrone_Go_strategy)
def test_minidrone_go_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=minidrone_Instruction_strategy)
@settings(max_examples=50)
def test_minidrone_instruction_instantiation(instance):
    assert isinstance(instance, minidrone_Instruction)

@given(instance=minidrone_MiniDroneProgram_strategy)
@settings(max_examples=50)
def test_minidrone_minidroneprogram_instantiation(instance):
    assert isinstance(instance, minidrone_MiniDroneProgram)



@given(instance=minidrone_MiniDroneProgram_strategy)
def test_minidrone_minidroneprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
