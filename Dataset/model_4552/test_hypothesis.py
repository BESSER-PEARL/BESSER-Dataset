import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Instruction,
    polybot::TakeDropObject,
    polybot::IfObjectDetected,
    polybot::IfObstacleDetected,
    polybot::While,
    polybot::Move,
    Move,
    polybot::Reverse,
    polybot::Left,
    polybot::Forward,
    polybot::GoTo,
    polybot::Right,
    polybot::Instruction,
    polybot::Point,
    polybot::Bot,
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



def test_polybot::takedropobject_is_not_abstract():
    assert not inspect.isabstract(polybot::TakeDropObject)


def test_polybot::takedropobject_constructor_exists():
    assert callable(polybot::TakeDropObject.__init__)


def test_polybot::takedropobject_constructor_args():
    sig = inspect.signature(polybot::TakeDropObject.__init__)
    params = list(sig.parameters.keys())



def test_polybot::ifobjectdetected_is_not_abstract():
    assert not inspect.isabstract(polybot::IfObjectDetected)


def test_polybot::ifobjectdetected_constructor_exists():
    assert callable(polybot::IfObjectDetected.__init__)


def test_polybot::ifobjectdetected_constructor_args():
    sig = inspect.signature(polybot::IfObjectDetected.__init__)
    params = list(sig.parameters.keys())



def test_polybot::ifobstacledetected_is_not_abstract():
    assert not inspect.isabstract(polybot::IfObstacleDetected)


def test_polybot::ifobstacledetected_constructor_exists():
    assert callable(polybot::IfObstacleDetected.__init__)


def test_polybot::ifobstacledetected_constructor_args():
    sig = inspect.signature(polybot::IfObstacleDetected.__init__)
    params = list(sig.parameters.keys())



def test_polybot::while_is_not_abstract():
    assert not inspect.isabstract(polybot::While)


def test_polybot::while_constructor_exists():
    assert callable(polybot::While.__init__)


def test_polybot::while_constructor_args():
    sig = inspect.signature(polybot::While.__init__)
    params = list(sig.parameters.keys())
    assert "nb" in params, "Missing parameter 'nb'"

def test_polybot::while_has_nb():
    assert hasattr(polybot::While, "nb")
    descriptor = None
    for klass in polybot::While.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)



def test_polybot::move_is_not_abstract():
    assert not inspect.isabstract(polybot::Move)


def test_polybot::move_constructor_exists():
    assert callable(polybot::Move.__init__)


def test_polybot::move_constructor_args():
    sig = inspect.signature(polybot::Move.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_polybot::move_has_speed():
    assert hasattr(polybot::Move, "speed")
    descriptor = None
    for klass in polybot::Move.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_polybot::move_has_duration():
    assert hasattr(polybot::Move, "duration")
    descriptor = None
    for klass in polybot::Move.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_move_is_not_abstract():
    assert not inspect.isabstract(Move)


def test_move_constructor_exists():
    assert callable(Move.__init__)


def test_move_constructor_args():
    sig = inspect.signature(Move.__init__)
    params = list(sig.parameters.keys())



def test_polybot::reverse_is_not_abstract():
    assert not inspect.isabstract(polybot::Reverse)


def test_polybot::reverse_constructor_exists():
    assert callable(polybot::Reverse.__init__)


def test_polybot::reverse_constructor_args():
    sig = inspect.signature(polybot::Reverse.__init__)
    params = list(sig.parameters.keys())



def test_polybot::left_is_not_abstract():
    assert not inspect.isabstract(polybot::Left)


def test_polybot::left_constructor_exists():
    assert callable(polybot::Left.__init__)


def test_polybot::left_constructor_args():
    sig = inspect.signature(polybot::Left.__init__)
    params = list(sig.parameters.keys())



def test_polybot::forward_is_not_abstract():
    assert not inspect.isabstract(polybot::Forward)


def test_polybot::forward_constructor_exists():
    assert callable(polybot::Forward.__init__)


def test_polybot::forward_constructor_args():
    sig = inspect.signature(polybot::Forward.__init__)
    params = list(sig.parameters.keys())



def test_polybot::goto_is_not_abstract():
    assert not inspect.isabstract(polybot::GoTo)


def test_polybot::goto_constructor_exists():
    assert callable(polybot::GoTo.__init__)


def test_polybot::goto_constructor_args():
    sig = inspect.signature(polybot::GoTo.__init__)
    params = list(sig.parameters.keys())



def test_polybot::right_is_not_abstract():
    assert not inspect.isabstract(polybot::Right)


def test_polybot::right_constructor_exists():
    assert callable(polybot::Right.__init__)


def test_polybot::right_constructor_args():
    sig = inspect.signature(polybot::Right.__init__)
    params = list(sig.parameters.keys())



def test_polybot::instruction_is_not_abstract():
    assert not inspect.isabstract(polybot::Instruction)


def test_polybot::instruction_constructor_exists():
    assert callable(polybot::Instruction.__init__)


def test_polybot::instruction_constructor_args():
    sig = inspect.signature(polybot::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_polybot::point_is_not_abstract():
    assert not inspect.isabstract(polybot::Point)


def test_polybot::point_constructor_exists():
    assert callable(polybot::Point.__init__)


def test_polybot::point_constructor_args():
    sig = inspect.signature(polybot::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_polybot::point_has_y():
    assert hasattr(polybot::Point, "y")
    descriptor = None
    for klass in polybot::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_polybot::point_has_x():
    assert hasattr(polybot::Point, "x")
    descriptor = None
    for klass in polybot::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_polybot::bot_is_not_abstract():
    assert not inspect.isabstract(polybot::Bot)


def test_polybot::bot_constructor_exists():
    assert callable(polybot::Bot.__init__)


def test_polybot::bot_constructor_args():
    sig = inspect.signature(polybot::Bot.__init__)
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
Instruction_strategy = st.builds(
    Instruction,
)
polybot::TakeDropObject_strategy = st.builds(
    polybot::TakeDropObject,
)
polybot::IfObjectDetected_strategy = st.builds(
    polybot::IfObjectDetected,
)
polybot::IfObstacleDetected_strategy = st.builds(
    polybot::IfObstacleDetected,
)
polybot::While_strategy = st.builds(
    polybot::While,
    nb=
        st.integers()
)
polybot::Move_strategy = st.builds(
    polybot::Move,
    speed=
        st.integers(),
    duration=
        st.integers()
)
Move_strategy = st.builds(
    Move,
)
polybot::Reverse_strategy = st.builds(
    polybot::Reverse,
)
polybot::Left_strategy = st.builds(
    polybot::Left,
)
polybot::Forward_strategy = st.builds(
    polybot::Forward,
)
polybot::GoTo_strategy = st.builds(
    polybot::GoTo,
)
polybot::Right_strategy = st.builds(
    polybot::Right,
)
polybot::Instruction_strategy = st.builds(
    polybot::Instruction,
)
polybot::Point_strategy = st.builds(
    polybot::Point,
    y=
        st.integers(),
    x=
        st.integers()
)
polybot::Bot_strategy = st.builds(
    polybot::Bot,
)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=polybot::TakeDropObject_strategy)
@settings(max_examples=50)
def test_polybot::takedropobject_instantiation(instance):
    assert isinstance(instance, polybot::TakeDropObject)

@given(instance=polybot::IfObjectDetected_strategy)
@settings(max_examples=50)
def test_polybot::ifobjectdetected_instantiation(instance):
    assert isinstance(instance, polybot::IfObjectDetected)

@given(instance=polybot::IfObstacleDetected_strategy)
@settings(max_examples=50)
def test_polybot::ifobstacledetected_instantiation(instance):
    assert isinstance(instance, polybot::IfObstacleDetected)

@given(instance=polybot::While_strategy)
@settings(max_examples=50)
def test_polybot::while_instantiation(instance):
    assert isinstance(instance, polybot::While)

@given(instance=polybot::While_strategy)
def test_polybot::while_nb_type(instance):
    assert isinstance(instance.nb, int)


@given(instance=polybot::While_strategy)
def test_polybot::while_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original

@given(instance=polybot::Move_strategy)
@settings(max_examples=50)
def test_polybot::move_instantiation(instance):
    assert isinstance(instance, polybot::Move)

@given(instance=polybot::Move_strategy)
def test_polybot::move_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=polybot::Move_strategy)
def test_polybot::move_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=polybot::Move_strategy)
def test_polybot::move_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=polybot::Move_strategy)
def test_polybot::move_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Move_strategy)
@settings(max_examples=50)
def test_move_instantiation(instance):
    assert isinstance(instance, Move)

@given(instance=polybot::Reverse_strategy)
@settings(max_examples=50)
def test_polybot::reverse_instantiation(instance):
    assert isinstance(instance, polybot::Reverse)

@given(instance=polybot::Left_strategy)
@settings(max_examples=50)
def test_polybot::left_instantiation(instance):
    assert isinstance(instance, polybot::Left)

@given(instance=polybot::Forward_strategy)
@settings(max_examples=50)
def test_polybot::forward_instantiation(instance):
    assert isinstance(instance, polybot::Forward)

@given(instance=polybot::GoTo_strategy)
@settings(max_examples=50)
def test_polybot::goto_instantiation(instance):
    assert isinstance(instance, polybot::GoTo)

@given(instance=polybot::Right_strategy)
@settings(max_examples=50)
def test_polybot::right_instantiation(instance):
    assert isinstance(instance, polybot::Right)

@given(instance=polybot::Instruction_strategy)
@settings(max_examples=50)
def test_polybot::instruction_instantiation(instance):
    assert isinstance(instance, polybot::Instruction)

@given(instance=polybot::Point_strategy)
@settings(max_examples=50)
def test_polybot::point_instantiation(instance):
    assert isinstance(instance, polybot::Point)

@given(instance=polybot::Point_strategy)
def test_polybot::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=polybot::Point_strategy)
def test_polybot::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=polybot::Point_strategy)
def test_polybot::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=polybot::Point_strategy)
def test_polybot::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=polybot::Bot_strategy)
@settings(max_examples=50)
def test_polybot::bot_instantiation(instance):
    assert isinstance(instance, polybot::Bot)
