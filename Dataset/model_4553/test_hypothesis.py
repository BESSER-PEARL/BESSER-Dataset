import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Command,
    logo_Turn,
    logo_WhileNoObstacle,
    logo_Move,
    logo_Command,
    logo_ProgramUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_logo_turn_is_not_abstract():
    assert not inspect.isabstract(logo_Turn)


def test_logo_turn_constructor_exists():
    assert callable(logo_Turn.__init__)


def test_logo_turn_constructor_args():
    sig = inspect.signature(logo_Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo_turn_has_angle():
    assert hasattr(logo_Turn, "angle")
    descriptor = None
    for klass in logo_Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo_whilenoobstacle_is_not_abstract():
    assert not inspect.isabstract(logo_WhileNoObstacle)


def test_logo_whilenoobstacle_constructor_exists():
    assert callable(logo_WhileNoObstacle.__init__)


def test_logo_whilenoobstacle_constructor_args():
    sig = inspect.signature(logo_WhileNoObstacle.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_logo_whilenoobstacle_has_distance():
    assert hasattr(logo_WhileNoObstacle, "distance")
    descriptor = None
    for klass in logo_WhileNoObstacle.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_logo_move_is_not_abstract():
    assert not inspect.isabstract(logo_Move)


def test_logo_move_constructor_exists():
    assert callable(logo_Move.__init__)


def test_logo_move_constructor_args():
    sig = inspect.signature(logo_Move.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_logo_move_has_distance():
    assert hasattr(logo_Move, "distance")
    descriptor = None
    for klass in logo_Move.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_logo_command_is_not_abstract():
    assert not inspect.isabstract(logo_Command)


def test_logo_command_constructor_exists():
    assert callable(logo_Command.__init__)


def test_logo_command_constructor_args():
    sig = inspect.signature(logo_Command.__init__)
    params = list(sig.parameters.keys())



def test_logo_programunit_is_not_abstract():
    assert not inspect.isabstract(logo_ProgramUnit)


def test_logo_programunit_constructor_exists():
    assert callable(logo_ProgramUnit.__init__)


def test_logo_programunit_constructor_args():
    sig = inspect.signature(logo_ProgramUnit.__init__)
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
Command_strategy = st.builds(
    Command,
)
logo_Turn_strategy = st.builds(
    logo_Turn,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_WhileNoObstacle_strategy = st.builds(
    logo_WhileNoObstacle,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_Move_strategy = st.builds(
    logo_Move,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_Command_strategy = st.builds(
    logo_Command,
)
logo_ProgramUnit_strategy = st.builds(
    logo_ProgramUnit,
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=logo_Turn_strategy)
@settings(max_examples=50)
def test_logo_turn_instantiation(instance):
    assert isinstance(instance, logo_Turn)



@given(instance=logo_Turn_strategy)
def test_logo_turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo_WhileNoObstacle_strategy)
@settings(max_examples=50)
def test_logo_whilenoobstacle_instantiation(instance):
    assert isinstance(instance, logo_WhileNoObstacle)



@given(instance=logo_WhileNoObstacle_strategy)
def test_logo_whilenoobstacle_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=logo_Move_strategy)
@settings(max_examples=50)
def test_logo_move_instantiation(instance):
    assert isinstance(instance, logo_Move)



@given(instance=logo_Move_strategy)
def test_logo_move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=logo_Command_strategy)
@settings(max_examples=50)
def test_logo_command_instantiation(instance):
    assert isinstance(instance, logo_Command)

@given(instance=logo_ProgramUnit_strategy)
@settings(max_examples=50)
def test_logo_programunit_instantiation(instance):
    assert isinstance(instance, logo_ProgramUnit)
