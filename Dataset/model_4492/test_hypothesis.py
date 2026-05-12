import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DriveAction,
    taskDSL_TurnLeft,
    taskDSL_TurnRight,
    taskDSL_MoveBack,
    taskDSL_DriveAction,
    Action,
    taskDSL_Speak,
    taskDSL_FollowLine,
    taskDSL_Investigate,
    taskDSL_DriveUntil,
    taskDSL_Avoid,
    taskDSL_Task,
    taskDSL_Mission,
    taskDSL_DSL,
    taskDSL_Detector,
    taskDSL_Action,
    Speed,
    Color,
    Object,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_driveaction_is_not_abstract():
    assert not inspect.isabstract(DriveAction)


def test_driveaction_constructor_exists():
    assert callable(DriveAction.__init__)


def test_driveaction_constructor_args():
    sig = inspect.signature(DriveAction.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl_turnleft_is_not_abstract():
    assert not inspect.isabstract(taskDSL_TurnLeft)


def test_taskdsl_turnleft_constructor_exists():
    assert callable(taskDSL_TurnLeft.__init__)


def test_taskdsl_turnleft_constructor_args():
    sig = inspect.signature(taskDSL_TurnLeft.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_taskdsl_turnleft_has_degrees():
    assert hasattr(taskDSL_TurnLeft, "degrees")
    descriptor = None
    for klass in taskDSL_TurnLeft.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_turnright_is_not_abstract():
    assert not inspect.isabstract(taskDSL_TurnRight)


def test_taskdsl_turnright_constructor_exists():
    assert callable(taskDSL_TurnRight.__init__)


def test_taskdsl_turnright_constructor_args():
    sig = inspect.signature(taskDSL_TurnRight.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_taskdsl_turnright_has_degrees():
    assert hasattr(taskDSL_TurnRight, "degrees")
    descriptor = None
    for klass in taskDSL_TurnRight.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_moveback_is_not_abstract():
    assert not inspect.isabstract(taskDSL_MoveBack)


def test_taskdsl_moveback_constructor_exists():
    assert callable(taskDSL_MoveBack.__init__)


def test_taskdsl_moveback_constructor_args():
    sig = inspect.signature(taskDSL_MoveBack.__init__)
    params = list(sig.parameters.keys())
    assert "meters" in params, "Missing parameter 'meters'"

def test_taskdsl_moveback_has_meters():
    assert hasattr(taskDSL_MoveBack, "meters")
    descriptor = None
    for klass in taskDSL_MoveBack.__mro__:
        if "meters" in klass.__dict__:
            descriptor = klass.__dict__["meters"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_driveaction_is_not_abstract():
    assert not inspect.isabstract(taskDSL_DriveAction)


def test_taskdsl_driveaction_constructor_exists():
    assert callable(taskDSL_DriveAction.__init__)


def test_taskdsl_driveaction_constructor_args():
    sig = inspect.signature(taskDSL_DriveAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl_speak_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Speak)


def test_taskdsl_speak_constructor_exists():
    assert callable(taskDSL_Speak.__init__)


def test_taskdsl_speak_constructor_args():
    sig = inspect.signature(taskDSL_Speak.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_taskdsl_speak_has_text():
    assert hasattr(taskDSL_Speak, "text")
    descriptor = None
    for klass in taskDSL_Speak.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_followline_is_not_abstract():
    assert not inspect.isabstract(taskDSL_FollowLine)


def test_taskdsl_followline_constructor_exists():
    assert callable(taskDSL_FollowLine.__init__)


def test_taskdsl_followline_constructor_args():
    sig = inspect.signature(taskDSL_FollowLine.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_taskdsl_followline_has_distance():
    assert hasattr(taskDSL_FollowLine, "distance")
    descriptor = None
    for klass in taskDSL_FollowLine.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_investigate_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Investigate)


def test_taskdsl_investigate_constructor_exists():
    assert callable(taskDSL_Investigate.__init__)


def test_taskdsl_investigate_constructor_args():
    sig = inspect.signature(taskDSL_Investigate.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_taskdsl_investigate_has_speed():
    assert hasattr(taskDSL_Investigate, "speed")
    descriptor = None
    for klass in taskDSL_Investigate.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_driveuntil_is_not_abstract():
    assert not inspect.isabstract(taskDSL_DriveUntil)


def test_taskdsl_driveuntil_constructor_exists():
    assert callable(taskDSL_DriveUntil.__init__)


def test_taskdsl_driveuntil_constructor_args():
    sig = inspect.signature(taskDSL_DriveUntil.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "object" in params, "Missing parameter 'object'"
    assert "color" in params, "Missing parameter 'color'"

def test_taskdsl_driveuntil_has_speed():
    assert hasattr(taskDSL_DriveUntil, "speed")
    descriptor = None
    for klass in taskDSL_DriveUntil.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl_driveuntil_has_object():
    assert hasattr(taskDSL_DriveUntil, "object")
    descriptor = None
    for klass in taskDSL_DriveUntil.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl_driveuntil_has_color():
    assert hasattr(taskDSL_DriveUntil, "color")
    descriptor = None
    for klass in taskDSL_DriveUntil.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_avoid_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Avoid)


def test_taskdsl_avoid_constructor_exists():
    assert callable(taskDSL_Avoid.__init__)


def test_taskdsl_avoid_constructor_args():
    sig = inspect.signature(taskDSL_Avoid.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"
    assert "color" in params, "Missing parameter 'color'"

def test_taskdsl_avoid_has_object():
    assert hasattr(taskDSL_Avoid, "object")
    descriptor = None
    for klass in taskDSL_Avoid.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl_avoid_has_color():
    assert hasattr(taskDSL_Avoid, "color")
    descriptor = None
    for klass in taskDSL_Avoid.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_task_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Task)


def test_taskdsl_task_constructor_exists():
    assert callable(taskDSL_Task.__init__)


def test_taskdsl_task_constructor_args():
    sig = inspect.signature(taskDSL_Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_taskdsl_task_has_name():
    assert hasattr(taskDSL_Task, "name")
    descriptor = None
    for klass in taskDSL_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_mission_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Mission)


def test_taskdsl_mission_constructor_exists():
    assert callable(taskDSL_Mission.__init__)


def test_taskdsl_mission_constructor_args():
    sig = inspect.signature(taskDSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_taskdsl_mission_has_name():
    assert hasattr(taskDSL_Mission, "name")
    descriptor = None
    for klass in taskDSL_Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl_dsl_is_not_abstract():
    assert not inspect.isabstract(taskDSL_DSL)


def test_taskdsl_dsl_constructor_exists():
    assert callable(taskDSL_DSL.__init__)


def test_taskdsl_dsl_constructor_args():
    sig = inspect.signature(taskDSL_DSL.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl_detector_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Detector)


def test_taskdsl_detector_constructor_exists():
    assert callable(taskDSL_Detector.__init__)


def test_taskdsl_detector_constructor_args():
    sig = inspect.signature(taskDSL_Detector.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl_action_is_not_abstract():
    assert not inspect.isabstract(taskDSL_Action)


def test_taskdsl_action_constructor_exists():
    assert callable(taskDSL_Action.__init__)


def test_taskdsl_action_constructor_args():
    sig = inspect.signature(taskDSL_Action.__init__)
    params = list(sig.parameters.keys())

def test_speed_exists():
    # Check that the Enumeration exists
    assert Speed is not None

def test_speed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Speed]
    expected_literals = [
        "SLOW",
        "NORMAL",
        "FAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Speed"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "GREEN",
        "BLUE",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_object_exists():
    # Check that the Enumeration exists
    assert Object is not None

def test_object_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Object]
    expected_literals = [
        "ROCK",
        "LAKE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Object"


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
DriveAction_strategy = st.builds(
    DriveAction,
)
taskDSL_TurnLeft_strategy = st.builds(
    taskDSL_TurnLeft,
    degrees=
        st.integers()
)
taskDSL_TurnRight_strategy = st.builds(
    taskDSL_TurnRight,
    degrees=
        st.integers()
)
taskDSL_MoveBack_strategy = st.builds(
    taskDSL_MoveBack,
    meters=
        st.integers()
)
taskDSL_DriveAction_strategy = st.builds(
    taskDSL_DriveAction,
)
Action_strategy = st.builds(
    Action,
)
taskDSL_Speak_strategy = st.builds(
    taskDSL_Speak,
    text=
        safe_text
)
taskDSL_FollowLine_strategy = st.builds(
    taskDSL_FollowLine,
    distance=
        st.integers()
)
taskDSL_Investigate_strategy = st.builds(
    taskDSL_Investigate,
    speed=
        safe_text
)
taskDSL_DriveUntil_strategy = st.builds(
    taskDSL_DriveUntil,
    speed=
        safe_text,
    object=
        safe_text,
    color=
        safe_text
)
taskDSL_Avoid_strategy = st.builds(
    taskDSL_Avoid,
    object=
        safe_text,
    color=
        safe_text
)
taskDSL_Task_strategy = st.builds(
    taskDSL_Task,
    name=
        safe_text
)
taskDSL_Mission_strategy = st.builds(
    taskDSL_Mission,
    name=
        safe_text
)
taskDSL_DSL_strategy = st.builds(
    taskDSL_DSL,
)
taskDSL_Detector_strategy = st.builds(
    taskDSL_Detector,
)
taskDSL_Action_strategy = st.builds(
    taskDSL_Action,
)

@given(instance=DriveAction_strategy)
@settings(max_examples=50)
def test_driveaction_instantiation(instance):
    assert isinstance(instance, DriveAction)

@given(instance=taskDSL_TurnLeft_strategy)
@settings(max_examples=50)
def test_taskdsl_turnleft_instantiation(instance):
    assert isinstance(instance, taskDSL_TurnLeft)



@given(instance=taskDSL_TurnLeft_strategy)
def test_taskdsl_turnleft_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=taskDSL_TurnRight_strategy)
@settings(max_examples=50)
def test_taskdsl_turnright_instantiation(instance):
    assert isinstance(instance, taskDSL_TurnRight)



@given(instance=taskDSL_TurnRight_strategy)
def test_taskdsl_turnright_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=taskDSL_MoveBack_strategy)
@settings(max_examples=50)
def test_taskdsl_moveback_instantiation(instance):
    assert isinstance(instance, taskDSL_MoveBack)



@given(instance=taskDSL_MoveBack_strategy)
def test_taskdsl_moveback_meters_setter(instance):
    original = instance.meters
    instance.meters = original
    assert instance.meters == original

@given(instance=taskDSL_DriveAction_strategy)
@settings(max_examples=50)
def test_taskdsl_driveaction_instantiation(instance):
    assert isinstance(instance, taskDSL_DriveAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=taskDSL_Speak_strategy)
@settings(max_examples=50)
def test_taskdsl_speak_instantiation(instance):
    assert isinstance(instance, taskDSL_Speak)



@given(instance=taskDSL_Speak_strategy)
def test_taskdsl_speak_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=taskDSL_FollowLine_strategy)
@settings(max_examples=50)
def test_taskdsl_followline_instantiation(instance):
    assert isinstance(instance, taskDSL_FollowLine)



@given(instance=taskDSL_FollowLine_strategy)
def test_taskdsl_followline_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=taskDSL_Investigate_strategy)
@settings(max_examples=50)
def test_taskdsl_investigate_instantiation(instance):
    assert isinstance(instance, taskDSL_Investigate)



@given(instance=taskDSL_Investigate_strategy)
def test_taskdsl_investigate_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=taskDSL_DriveUntil_strategy)
@settings(max_examples=50)
def test_taskdsl_driveuntil_instantiation(instance):
    assert isinstance(instance, taskDSL_DriveUntil)



@given(instance=taskDSL_DriveUntil_strategy)
def test_taskdsl_driveuntil_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=taskDSL_DriveUntil_strategy)
def test_taskdsl_driveuntil_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original



@given(instance=taskDSL_DriveUntil_strategy)
def test_taskdsl_driveuntil_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=taskDSL_Avoid_strategy)
@settings(max_examples=50)
def test_taskdsl_avoid_instantiation(instance):
    assert isinstance(instance, taskDSL_Avoid)



@given(instance=taskDSL_Avoid_strategy)
def test_taskdsl_avoid_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original



@given(instance=taskDSL_Avoid_strategy)
def test_taskdsl_avoid_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=taskDSL_Task_strategy)
@settings(max_examples=50)
def test_taskdsl_task_instantiation(instance):
    assert isinstance(instance, taskDSL_Task)



@given(instance=taskDSL_Task_strategy)
def test_taskdsl_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=taskDSL_Mission_strategy)
@settings(max_examples=50)
def test_taskdsl_mission_instantiation(instance):
    assert isinstance(instance, taskDSL_Mission)



@given(instance=taskDSL_Mission_strategy)
def test_taskdsl_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=taskDSL_DSL_strategy)
@settings(max_examples=50)
def test_taskdsl_dsl_instantiation(instance):
    assert isinstance(instance, taskDSL_DSL)

@given(instance=taskDSL_Detector_strategy)
@settings(max_examples=50)
def test_taskdsl_detector_instantiation(instance):
    assert isinstance(instance, taskDSL_Detector)

@given(instance=taskDSL_Action_strategy)
@settings(max_examples=50)
def test_taskdsl_action_instantiation(instance):
    assert isinstance(instance, taskDSL_Action)
