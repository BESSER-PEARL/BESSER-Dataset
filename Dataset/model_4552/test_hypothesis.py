import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Instruction,
    polybot_IfObstacleDetected,
    polybot_While,
    polybot_IfObjectDetected,
    polybot_TakeDropObject,
    polybot_Move,
    Move,
    polybot_Left,
    polybot_Reverse,
    polybot_Right,
    polybot_GoTo,
    polybot_Forward,
    polybot_Instruction,
    polybot_Point,
    polybot_Bot,
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



def test_polybot_ifobstacledetected_is_not_abstract():
    assert not inspect.isabstract(polybot_IfObstacleDetected)


def test_polybot_ifobstacledetected_constructor_exists():
    assert callable(polybot_IfObstacleDetected.__init__)


def test_polybot_ifobstacledetected_constructor_args():
    sig = inspect.signature(polybot_IfObstacleDetected.__init__)
    params = list(sig.parameters.keys())



def test_polybot_while_is_not_abstract():
    assert not inspect.isabstract(polybot_While)


def test_polybot_while_constructor_exists():
    assert callable(polybot_While.__init__)


def test_polybot_while_constructor_args():
    sig = inspect.signature(polybot_While.__init__)
    params = list(sig.parameters.keys())
    assert "nb" in params, "Missing parameter 'nb'"

def test_polybot_while_has_nb():
    assert hasattr(polybot_While, "nb")
    descriptor = None
    for klass in polybot_While.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)



def test_polybot_ifobjectdetected_is_not_abstract():
    assert not inspect.isabstract(polybot_IfObjectDetected)


def test_polybot_ifobjectdetected_constructor_exists():
    assert callable(polybot_IfObjectDetected.__init__)


def test_polybot_ifobjectdetected_constructor_args():
    sig = inspect.signature(polybot_IfObjectDetected.__init__)
    params = list(sig.parameters.keys())



def test_polybot_takedropobject_is_not_abstract():
    assert not inspect.isabstract(polybot_TakeDropObject)


def test_polybot_takedropobject_constructor_exists():
    assert callable(polybot_TakeDropObject.__init__)


def test_polybot_takedropobject_constructor_args():
    sig = inspect.signature(polybot_TakeDropObject.__init__)
    params = list(sig.parameters.keys())



def test_polybot_move_is_not_abstract():
    assert not inspect.isabstract(polybot_Move)


def test_polybot_move_constructor_exists():
    assert callable(polybot_Move.__init__)


def test_polybot_move_constructor_args():
    sig = inspect.signature(polybot_Move.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_polybot_move_has_speed():
    assert hasattr(polybot_Move, "speed")
    descriptor = None
    for klass in polybot_Move.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_polybot_move_has_duration():
    assert hasattr(polybot_Move, "duration")
    descriptor = None
    for klass in polybot_Move.__mro__:
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



def test_polybot_left_is_not_abstract():
    assert not inspect.isabstract(polybot_Left)


def test_polybot_left_constructor_exists():
    assert callable(polybot_Left.__init__)


def test_polybot_left_constructor_args():
    sig = inspect.signature(polybot_Left.__init__)
    params = list(sig.parameters.keys())



def test_polybot_reverse_is_not_abstract():
    assert not inspect.isabstract(polybot_Reverse)


def test_polybot_reverse_constructor_exists():
    assert callable(polybot_Reverse.__init__)


def test_polybot_reverse_constructor_args():
    sig = inspect.signature(polybot_Reverse.__init__)
    params = list(sig.parameters.keys())



def test_polybot_right_is_not_abstract():
    assert not inspect.isabstract(polybot_Right)


def test_polybot_right_constructor_exists():
    assert callable(polybot_Right.__init__)


def test_polybot_right_constructor_args():
    sig = inspect.signature(polybot_Right.__init__)
    params = list(sig.parameters.keys())



def test_polybot_goto_is_not_abstract():
    assert not inspect.isabstract(polybot_GoTo)


def test_polybot_goto_constructor_exists():
    assert callable(polybot_GoTo.__init__)


def test_polybot_goto_constructor_args():
    sig = inspect.signature(polybot_GoTo.__init__)
    params = list(sig.parameters.keys())



def test_polybot_forward_is_not_abstract():
    assert not inspect.isabstract(polybot_Forward)


def test_polybot_forward_constructor_exists():
    assert callable(polybot_Forward.__init__)


def test_polybot_forward_constructor_args():
    sig = inspect.signature(polybot_Forward.__init__)
    params = list(sig.parameters.keys())



def test_polybot_instruction_is_not_abstract():
    assert not inspect.isabstract(polybot_Instruction)


def test_polybot_instruction_constructor_exists():
    assert callable(polybot_Instruction.__init__)


def test_polybot_instruction_constructor_args():
    sig = inspect.signature(polybot_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_polybot_point_is_not_abstract():
    assert not inspect.isabstract(polybot_Point)


def test_polybot_point_constructor_exists():
    assert callable(polybot_Point.__init__)


def test_polybot_point_constructor_args():
    sig = inspect.signature(polybot_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_polybot_point_has_x():
    assert hasattr(polybot_Point, "x")
    descriptor = None
    for klass in polybot_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_polybot_point_has_y():
    assert hasattr(polybot_Point, "y")
    descriptor = None
    for klass in polybot_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_polybot_bot_is_not_abstract():
    assert not inspect.isabstract(polybot_Bot)


def test_polybot_bot_constructor_exists():
    assert callable(polybot_Bot.__init__)


def test_polybot_bot_constructor_args():
    sig = inspect.signature(polybot_Bot.__init__)
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
polybot_IfObstacleDetected_strategy = st.builds(
    polybot_IfObstacleDetected,
)
polybot_While_strategy = st.builds(
    polybot_While,
    nb=
        st.integers()
)
polybot_IfObjectDetected_strategy = st.builds(
    polybot_IfObjectDetected,
)
polybot_TakeDropObject_strategy = st.builds(
    polybot_TakeDropObject,
)
polybot_Move_strategy = st.builds(
    polybot_Move,
    speed=
        st.integers(),
    duration=
        st.integers()
)
Move_strategy = st.builds(
    Move,
)
polybot_Left_strategy = st.builds(
    polybot_Left,
)
polybot_Reverse_strategy = st.builds(
    polybot_Reverse,
)
polybot_Right_strategy = st.builds(
    polybot_Right,
)
polybot_GoTo_strategy = st.builds(
    polybot_GoTo,
)
polybot_Forward_strategy = st.builds(
    polybot_Forward,
)
polybot_Instruction_strategy = st.builds(
    polybot_Instruction,
)
polybot_Point_strategy = st.builds(
    polybot_Point,
    x=
        st.integers(),
    y=
        st.integers()
)
polybot_Bot_strategy = st.builds(
    polybot_Bot,
)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=polybot_IfObstacleDetected_strategy)
@settings(max_examples=50)
def test_polybot_ifobstacledetected_instantiation(instance):
    assert isinstance(instance, polybot_IfObstacleDetected)

@given(instance=polybot_While_strategy)
@settings(max_examples=50)
def test_polybot_while_instantiation(instance):
    assert isinstance(instance, polybot_While)



@given(instance=polybot_While_strategy)
def test_polybot_while_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original

@given(instance=polybot_IfObjectDetected_strategy)
@settings(max_examples=50)
def test_polybot_ifobjectdetected_instantiation(instance):
    assert isinstance(instance, polybot_IfObjectDetected)

@given(instance=polybot_TakeDropObject_strategy)
@settings(max_examples=50)
def test_polybot_takedropobject_instantiation(instance):
    assert isinstance(instance, polybot_TakeDropObject)

@given(instance=polybot_Move_strategy)
@settings(max_examples=50)
def test_polybot_move_instantiation(instance):
    assert isinstance(instance, polybot_Move)



@given(instance=polybot_Move_strategy)
def test_polybot_move_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=polybot_Move_strategy)
def test_polybot_move_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Move_strategy)
@settings(max_examples=50)
def test_move_instantiation(instance):
    assert isinstance(instance, Move)

@given(instance=polybot_Left_strategy)
@settings(max_examples=50)
def test_polybot_left_instantiation(instance):
    assert isinstance(instance, polybot_Left)

@given(instance=polybot_Reverse_strategy)
@settings(max_examples=50)
def test_polybot_reverse_instantiation(instance):
    assert isinstance(instance, polybot_Reverse)

@given(instance=polybot_Right_strategy)
@settings(max_examples=50)
def test_polybot_right_instantiation(instance):
    assert isinstance(instance, polybot_Right)

@given(instance=polybot_GoTo_strategy)
@settings(max_examples=50)
def test_polybot_goto_instantiation(instance):
    assert isinstance(instance, polybot_GoTo)

@given(instance=polybot_Forward_strategy)
@settings(max_examples=50)
def test_polybot_forward_instantiation(instance):
    assert isinstance(instance, polybot_Forward)

@given(instance=polybot_Instruction_strategy)
@settings(max_examples=50)
def test_polybot_instruction_instantiation(instance):
    assert isinstance(instance, polybot_Instruction)

@given(instance=polybot_Point_strategy)
@settings(max_examples=50)
def test_polybot_point_instantiation(instance):
    assert isinstance(instance, polybot_Point)



@given(instance=polybot_Point_strategy)
def test_polybot_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=polybot_Point_strategy)
def test_polybot_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=polybot_Bot_strategy)
@settings(max_examples=50)
def test_polybot_bot_instantiation(instance):
    assert isinstance(instance, polybot_Bot)
