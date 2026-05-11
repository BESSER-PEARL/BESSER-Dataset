import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Command,
    logo::WhileNoObstacle,
    logo::Turn,
    logo::Move,
    logo::Command,
    logo::ProgramUnit,
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



def test_logo::whilenoobstacle_is_not_abstract():
    assert not inspect.isabstract(logo::WhileNoObstacle)


def test_logo::whilenoobstacle_constructor_exists():
    assert callable(logo::WhileNoObstacle.__init__)


def test_logo::whilenoobstacle_constructor_args():
    sig = inspect.signature(logo::WhileNoObstacle.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_logo::whilenoobstacle_has_distance():
    assert hasattr(logo::WhileNoObstacle, "distance")
    descriptor = None
    for klass in logo::WhileNoObstacle.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_logo::turn_is_not_abstract():
    assert not inspect.isabstract(logo::Turn)


def test_logo::turn_constructor_exists():
    assert callable(logo::Turn.__init__)


def test_logo::turn_constructor_args():
    sig = inspect.signature(logo::Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_logo::turn_has_angle():
    assert hasattr(logo::Turn, "angle")
    descriptor = None
    for klass in logo::Turn.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_logo::move_is_not_abstract():
    assert not inspect.isabstract(logo::Move)


def test_logo::move_constructor_exists():
    assert callable(logo::Move.__init__)


def test_logo::move_constructor_args():
    sig = inspect.signature(logo::Move.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_logo::move_has_distance():
    assert hasattr(logo::Move, "distance")
    descriptor = None
    for klass in logo::Move.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_logo::command_is_not_abstract():
    assert not inspect.isabstract(logo::Command)


def test_logo::command_constructor_exists():
    assert callable(logo::Command.__init__)


def test_logo::command_constructor_args():
    sig = inspect.signature(logo::Command.__init__)
    params = list(sig.parameters.keys())



def test_logo::programunit_is_not_abstract():
    assert not inspect.isabstract(logo::ProgramUnit)


def test_logo::programunit_constructor_exists():
    assert callable(logo::ProgramUnit.__init__)


def test_logo::programunit_constructor_args():
    sig = inspect.signature(logo::ProgramUnit.__init__)
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
logo::WhileNoObstacle_strategy = st.builds(
    logo::WhileNoObstacle,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo::Turn_strategy = st.builds(
    logo::Turn,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo::Move_strategy = st.builds(
    logo::Move,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo::Command_strategy = st.builds(
    logo::Command,
)
logo::ProgramUnit_strategy = st.builds(
    logo::ProgramUnit,
)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=logo::WhileNoObstacle_strategy)
@settings(max_examples=50)
def test_logo::whilenoobstacle_instantiation(instance):
    assert isinstance(instance, logo::WhileNoObstacle)

@given(instance=logo::WhileNoObstacle_strategy)
def test_logo::whilenoobstacle_distance_type(instance):
    assert isinstance(instance.distance, float)


@given(instance=logo::WhileNoObstacle_strategy)
def test_logo::whilenoobstacle_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=logo::Turn_strategy)
@settings(max_examples=50)
def test_logo::turn_instantiation(instance):
    assert isinstance(instance, logo::Turn)

@given(instance=logo::Turn_strategy)
def test_logo::turn_angle_type(instance):
    assert isinstance(instance.angle, float)


@given(instance=logo::Turn_strategy)
def test_logo::turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=logo::Move_strategy)
@settings(max_examples=50)
def test_logo::move_instantiation(instance):
    assert isinstance(instance, logo::Move)

@given(instance=logo::Move_strategy)
def test_logo::move_distance_type(instance):
    assert isinstance(instance.distance, float)


@given(instance=logo::Move_strategy)
def test_logo::move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=logo::Command_strategy)
@settings(max_examples=50)
def test_logo::command_instantiation(instance):
    assert isinstance(instance, logo::Command)

@given(instance=logo::ProgramUnit_strategy)
@settings(max_examples=50)
def test_logo::programunit_instantiation(instance):
    assert isinstance(instance, logo::ProgramUnit)
