import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Instruction,
    minidrone::Turn,
    minidrone::Jump,
    minidrone::Go,
    minidrone::Instruction,
    minidrone::MiniDroneProgram,
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



def test_minidrone::turn_is_not_abstract():
    assert not inspect.isabstract(minidrone::Turn)


def test_minidrone::turn_constructor_exists():
    assert callable(minidrone::Turn.__init__)


def test_minidrone::turn_constructor_args():
    sig = inspect.signature(minidrone::Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_minidrone::turn_has_angle():
    assert hasattr(minidrone::Turn, "angle")
    descriptor = None
    for klass in minidrone::Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_minidrone::jump_is_not_abstract():
    assert not inspect.isabstract(minidrone::Jump)


def test_minidrone::jump_constructor_exists():
    assert callable(minidrone::Jump.__init__)


def test_minidrone::jump_constructor_args():
    sig = inspect.signature(minidrone::Jump.__init__)
    params = list(sig.parameters.keys())
    assert "jumpType" in params, "Missing parameter 'jumpType'"

def test_minidrone::jump_has_jumpType():
    assert hasattr(minidrone::Jump, "jumpType")
    descriptor = None
    for klass in minidrone::Jump.__mro__:
        if "jumpType" in klass.__dict__:
            descriptor = klass.__dict__["jumpType"]
            break
    assert isinstance(descriptor, property)



def test_minidrone::go_is_not_abstract():
    assert not inspect.isabstract(minidrone::Go)


def test_minidrone::go_constructor_exists():
    assert callable(minidrone::Go.__init__)


def test_minidrone::go_constructor_args():
    sig = inspect.signature(minidrone::Go.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_minidrone::go_has_distance():
    assert hasattr(minidrone::Go, "distance")
    descriptor = None
    for klass in minidrone::Go.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_minidrone::instruction_is_not_abstract():
    assert not inspect.isabstract(minidrone::Instruction)


def test_minidrone::instruction_constructor_exists():
    assert callable(minidrone::Instruction.__init__)


def test_minidrone::instruction_constructor_args():
    sig = inspect.signature(minidrone::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_minidrone::minidroneprogram_is_not_abstract():
    assert not inspect.isabstract(minidrone::MiniDroneProgram)


def test_minidrone::minidroneprogram_constructor_exists():
    assert callable(minidrone::MiniDroneProgram.__init__)


def test_minidrone::minidroneprogram_constructor_args():
    sig = inspect.signature(minidrone::MiniDroneProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minidrone::minidroneprogram_has_name():
    assert hasattr(minidrone::MiniDroneProgram, "name")
    descriptor = None
    for klass in minidrone::MiniDroneProgram.__mro__:
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
        "JUMP_MAX",
        "JUMP_LONG",
        "JUMP_HIGH",
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
minidrone::Turn_strategy = st.builds(
    minidrone::Turn,
    angle=
        st.integers()
)
minidrone::Jump_strategy = st.builds(
    minidrone::Jump,
    jumpType=
        safe_text
)
minidrone::Go_strategy = st.builds(
    minidrone::Go,
    distance=
        st.integers()
)
minidrone::Instruction_strategy = st.builds(
    minidrone::Instruction,
)
minidrone::MiniDroneProgram_strategy = st.builds(
    minidrone::MiniDroneProgram,
    name=
        safe_text
)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=minidrone::Turn_strategy)
@settings(max_examples=50)
def test_minidrone::turn_instantiation(instance):
    assert isinstance(instance, minidrone::Turn)

@given(instance=minidrone::Turn_strategy)
def test_minidrone::turn_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=minidrone::Turn_strategy)
def test_minidrone::turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=minidrone::Jump_strategy)
@settings(max_examples=50)
def test_minidrone::jump_instantiation(instance):
    assert isinstance(instance, minidrone::Jump)

@given(instance=minidrone::Jump_strategy)
def test_minidrone::jump_jumpType_type(instance):
    assert isinstance(instance.jumpType, str)


@given(instance=minidrone::Jump_strategy)
def test_minidrone::jump_jumpType_setter(instance):
    original = instance.jumpType
    instance.jumpType = original
    assert instance.jumpType == original

@given(instance=minidrone::Go_strategy)
@settings(max_examples=50)
def test_minidrone::go_instantiation(instance):
    assert isinstance(instance, minidrone::Go)

@given(instance=minidrone::Go_strategy)
def test_minidrone::go_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=minidrone::Go_strategy)
def test_minidrone::go_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=minidrone::Instruction_strategy)
@settings(max_examples=50)
def test_minidrone::instruction_instantiation(instance):
    assert isinstance(instance, minidrone::Instruction)

@given(instance=minidrone::MiniDroneProgram_strategy)
@settings(max_examples=50)
def test_minidrone::minidroneprogram_instantiation(instance):
    assert isinstance(instance, minidrone::MiniDroneProgram)

@given(instance=minidrone::MiniDroneProgram_strategy)
def test_minidrone::minidroneprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minidrone::MiniDroneProgram_strategy)
def test_minidrone::minidroneprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
