import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DriveAction,
    taskDSL::TurnRight,
    taskDSL::TurnLeft,
    taskDSL::MoveBack,
    taskDSL::DriveAction,
    Action,
    taskDSL::FollowLine,
    taskDSL::Speak,
    taskDSL::Investigate,
    taskDSL::DriveUntil,
    taskDSL::Avoid,
    taskDSL::Task,
    taskDSL::Mission,
    taskDSL::DSL,
    taskDSL::Detector,
    taskDSL::Action,
    Object,
    Speed,
    Color,
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



def test_taskdsl::turnright_is_not_abstract():
    assert not inspect.isabstract(taskDSL::TurnRight)


def test_taskdsl::turnright_constructor_exists():
    assert callable(taskDSL::TurnRight.__init__)


def test_taskdsl::turnright_constructor_args():
    sig = inspect.signature(taskDSL::TurnRight.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_taskdsl::turnright_has_degrees():
    assert hasattr(taskDSL::TurnRight, "degrees")
    descriptor = None
    for klass in taskDSL::TurnRight.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::turnleft_is_not_abstract():
    assert not inspect.isabstract(taskDSL::TurnLeft)


def test_taskdsl::turnleft_constructor_exists():
    assert callable(taskDSL::TurnLeft.__init__)


def test_taskdsl::turnleft_constructor_args():
    sig = inspect.signature(taskDSL::TurnLeft.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_taskdsl::turnleft_has_degrees():
    assert hasattr(taskDSL::TurnLeft, "degrees")
    descriptor = None
    for klass in taskDSL::TurnLeft.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::moveback_is_not_abstract():
    assert not inspect.isabstract(taskDSL::MoveBack)


def test_taskdsl::moveback_constructor_exists():
    assert callable(taskDSL::MoveBack.__init__)


def test_taskdsl::moveback_constructor_args():
    sig = inspect.signature(taskDSL::MoveBack.__init__)
    params = list(sig.parameters.keys())
    assert "meters" in params, "Missing parameter 'meters'"

def test_taskdsl::moveback_has_meters():
    assert hasattr(taskDSL::MoveBack, "meters")
    descriptor = None
    for klass in taskDSL::MoveBack.__mro__:
        if "meters" in klass.__dict__:
            descriptor = klass.__dict__["meters"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::driveaction_is_not_abstract():
    assert not inspect.isabstract(taskDSL::DriveAction)


def test_taskdsl::driveaction_constructor_exists():
    assert callable(taskDSL::DriveAction.__init__)


def test_taskdsl::driveaction_constructor_args():
    sig = inspect.signature(taskDSL::DriveAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl::followline_is_not_abstract():
    assert not inspect.isabstract(taskDSL::FollowLine)


def test_taskdsl::followline_constructor_exists():
    assert callable(taskDSL::FollowLine.__init__)


def test_taskdsl::followline_constructor_args():
    sig = inspect.signature(taskDSL::FollowLine.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_taskdsl::followline_has_distance():
    assert hasattr(taskDSL::FollowLine, "distance")
    descriptor = None
    for klass in taskDSL::FollowLine.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::speak_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Speak)


def test_taskdsl::speak_constructor_exists():
    assert callable(taskDSL::Speak.__init__)


def test_taskdsl::speak_constructor_args():
    sig = inspect.signature(taskDSL::Speak.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_taskdsl::speak_has_text():
    assert hasattr(taskDSL::Speak, "text")
    descriptor = None
    for klass in taskDSL::Speak.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::investigate_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Investigate)


def test_taskdsl::investigate_constructor_exists():
    assert callable(taskDSL::Investigate.__init__)


def test_taskdsl::investigate_constructor_args():
    sig = inspect.signature(taskDSL::Investigate.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_taskdsl::investigate_has_speed():
    assert hasattr(taskDSL::Investigate, "speed")
    descriptor = None
    for klass in taskDSL::Investigate.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::driveuntil_is_not_abstract():
    assert not inspect.isabstract(taskDSL::DriveUntil)


def test_taskdsl::driveuntil_constructor_exists():
    assert callable(taskDSL::DriveUntil.__init__)


def test_taskdsl::driveuntil_constructor_args():
    sig = inspect.signature(taskDSL::DriveUntil.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "color" in params, "Missing parameter 'color'"

def test_taskdsl::driveuntil_has_object():
    assert hasattr(taskDSL::DriveUntil, "object")
    descriptor = None
    for klass in taskDSL::DriveUntil.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl::driveuntil_has_speed():
    assert hasattr(taskDSL::DriveUntil, "speed")
    descriptor = None
    for klass in taskDSL::DriveUntil.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl::driveuntil_has_color():
    assert hasattr(taskDSL::DriveUntil, "color")
    descriptor = None
    for klass in taskDSL::DriveUntil.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::avoid_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Avoid)


def test_taskdsl::avoid_constructor_exists():
    assert callable(taskDSL::Avoid.__init__)


def test_taskdsl::avoid_constructor_args():
    sig = inspect.signature(taskDSL::Avoid.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"
    assert "color" in params, "Missing parameter 'color'"

def test_taskdsl::avoid_has_object():
    assert hasattr(taskDSL::Avoid, "object")
    descriptor = None
    for klass in taskDSL::Avoid.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)

def test_taskdsl::avoid_has_color():
    assert hasattr(taskDSL::Avoid, "color")
    descriptor = None
    for klass in taskDSL::Avoid.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::task_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Task)


def test_taskdsl::task_constructor_exists():
    assert callable(taskDSL::Task.__init__)


def test_taskdsl::task_constructor_args():
    sig = inspect.signature(taskDSL::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_taskdsl::task_has_name():
    assert hasattr(taskDSL::Task, "name")
    descriptor = None
    for klass in taskDSL::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::mission_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Mission)


def test_taskdsl::mission_constructor_exists():
    assert callable(taskDSL::Mission.__init__)


def test_taskdsl::mission_constructor_args():
    sig = inspect.signature(taskDSL::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_taskdsl::mission_has_name():
    assert hasattr(taskDSL::Mission, "name")
    descriptor = None
    for klass in taskDSL::Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_taskdsl::dsl_is_not_abstract():
    assert not inspect.isabstract(taskDSL::DSL)


def test_taskdsl::dsl_constructor_exists():
    assert callable(taskDSL::DSL.__init__)


def test_taskdsl::dsl_constructor_args():
    sig = inspect.signature(taskDSL::DSL.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl::detector_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Detector)


def test_taskdsl::detector_constructor_exists():
    assert callable(taskDSL::Detector.__init__)


def test_taskdsl::detector_constructor_args():
    sig = inspect.signature(taskDSL::Detector.__init__)
    params = list(sig.parameters.keys())



def test_taskdsl::action_is_not_abstract():
    assert not inspect.isabstract(taskDSL::Action)


def test_taskdsl::action_constructor_exists():
    assert callable(taskDSL::Action.__init__)


def test_taskdsl::action_constructor_args():
    sig = inspect.signature(taskDSL::Action.__init__)
    params = list(sig.parameters.keys())

def test_object_exists():
    # Check that the Enumeration exists
    assert Object is not None

def test_object_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Object]
    expected_literals = [
        "LAKE",
        "ROCK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Object"

def test_speed_exists():
    # Check that the Enumeration exists
    assert Speed is not None

def test_speed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Speed]
    expected_literals = [
        "FAST",
        "SLOW",
        "NORMAL",
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
        "RED",
        "GREEN",
        "BLUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
taskDSL::TurnRight_strategy = st.builds(
    taskDSL::TurnRight,
    degrees=
        st.integers()
)
taskDSL::TurnLeft_strategy = st.builds(
    taskDSL::TurnLeft,
    degrees=
        st.integers()
)
taskDSL::MoveBack_strategy = st.builds(
    taskDSL::MoveBack,
    meters=
        st.integers()
)
taskDSL::DriveAction_strategy = st.builds(
    taskDSL::DriveAction,
)
Action_strategy = st.builds(
    Action,
)
taskDSL::FollowLine_strategy = st.builds(
    taskDSL::FollowLine,
    distance=
        st.integers()
)
taskDSL::Speak_strategy = st.builds(
    taskDSL::Speak,
    text=
        safe_text
)
taskDSL::Investigate_strategy = st.builds(
    taskDSL::Investigate,
    speed=
        safe_text
)
taskDSL::DriveUntil_strategy = st.builds(
    taskDSL::DriveUntil,
    object=
        safe_text,
    speed=
        safe_text,
    color=
        safe_text
)
taskDSL::Avoid_strategy = st.builds(
    taskDSL::Avoid,
    object=
        safe_text,
    color=
        safe_text
)
taskDSL::Task_strategy = st.builds(
    taskDSL::Task,
    name=
        safe_text
)
taskDSL::Mission_strategy = st.builds(
    taskDSL::Mission,
    name=
        safe_text
)
taskDSL::DSL_strategy = st.builds(
    taskDSL::DSL,
)
taskDSL::Detector_strategy = st.builds(
    taskDSL::Detector,
)
taskDSL::Action_strategy = st.builds(
    taskDSL::Action,
)

@given(instance=DriveAction_strategy)
@settings(max_examples=50)
def test_driveaction_instantiation(instance):
    assert isinstance(instance, DriveAction)

@given(instance=taskDSL::TurnRight_strategy)
@settings(max_examples=50)
def test_taskdsl::turnright_instantiation(instance):
    assert isinstance(instance, taskDSL::TurnRight)

@given(instance=taskDSL::TurnRight_strategy)
def test_taskdsl::turnright_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=taskDSL::TurnRight_strategy)
def test_taskdsl::turnright_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=taskDSL::TurnLeft_strategy)
@settings(max_examples=50)
def test_taskdsl::turnleft_instantiation(instance):
    assert isinstance(instance, taskDSL::TurnLeft)

@given(instance=taskDSL::TurnLeft_strategy)
def test_taskdsl::turnleft_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=taskDSL::TurnLeft_strategy)
def test_taskdsl::turnleft_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=taskDSL::MoveBack_strategy)
@settings(max_examples=50)
def test_taskdsl::moveback_instantiation(instance):
    assert isinstance(instance, taskDSL::MoveBack)

@given(instance=taskDSL::MoveBack_strategy)
def test_taskdsl::moveback_meters_type(instance):
    assert isinstance(instance.meters, int)


@given(instance=taskDSL::MoveBack_strategy)
def test_taskdsl::moveback_meters_setter(instance):
    original = instance.meters
    instance.meters = original
    assert instance.meters == original

@given(instance=taskDSL::DriveAction_strategy)
@settings(max_examples=50)
def test_taskdsl::driveaction_instantiation(instance):
    assert isinstance(instance, taskDSL::DriveAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=taskDSL::FollowLine_strategy)
@settings(max_examples=50)
def test_taskdsl::followline_instantiation(instance):
    assert isinstance(instance, taskDSL::FollowLine)

@given(instance=taskDSL::FollowLine_strategy)
def test_taskdsl::followline_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=taskDSL::FollowLine_strategy)
def test_taskdsl::followline_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=taskDSL::Speak_strategy)
@settings(max_examples=50)
def test_taskdsl::speak_instantiation(instance):
    assert isinstance(instance, taskDSL::Speak)

@given(instance=taskDSL::Speak_strategy)
def test_taskdsl::speak_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=taskDSL::Speak_strategy)
def test_taskdsl::speak_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=taskDSL::Investigate_strategy)
@settings(max_examples=50)
def test_taskdsl::investigate_instantiation(instance):
    assert isinstance(instance, taskDSL::Investigate)

@given(instance=taskDSL::Investigate_strategy)
def test_taskdsl::investigate_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=taskDSL::Investigate_strategy)
def test_taskdsl::investigate_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=taskDSL::DriveUntil_strategy)
@settings(max_examples=50)
def test_taskdsl::driveuntil_instantiation(instance):
    assert isinstance(instance, taskDSL::DriveUntil)

@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=taskDSL::DriveUntil_strategy)
def test_taskdsl::driveuntil_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=taskDSL::Avoid_strategy)
@settings(max_examples=50)
def test_taskdsl::avoid_instantiation(instance):
    assert isinstance(instance, taskDSL::Avoid)

@given(instance=taskDSL::Avoid_strategy)
def test_taskdsl::avoid_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=taskDSL::Avoid_strategy)
def test_taskdsl::avoid_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=taskDSL::Avoid_strategy)
def test_taskdsl::avoid_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=taskDSL::Avoid_strategy)
def test_taskdsl::avoid_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=taskDSL::Task_strategy)
@settings(max_examples=50)
def test_taskdsl::task_instantiation(instance):
    assert isinstance(instance, taskDSL::Task)

@given(instance=taskDSL::Task_strategy)
def test_taskdsl::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=taskDSL::Task_strategy)
def test_taskdsl::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=taskDSL::Mission_strategy)
@settings(max_examples=50)
def test_taskdsl::mission_instantiation(instance):
    assert isinstance(instance, taskDSL::Mission)

@given(instance=taskDSL::Mission_strategy)
def test_taskdsl::mission_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=taskDSL::Mission_strategy)
def test_taskdsl::mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=taskDSL::DSL_strategy)
@settings(max_examples=50)
def test_taskdsl::dsl_instantiation(instance):
    assert isinstance(instance, taskDSL::DSL)

@given(instance=taskDSL::Detector_strategy)
@settings(max_examples=50)
def test_taskdsl::detector_instantiation(instance):
    assert isinstance(instance, taskDSL::Detector)

@given(instance=taskDSL::Action_strategy)
@settings(max_examples=50)
def test_taskdsl::action_instantiation(instance):
    assert isinstance(instance, taskDSL::Action)
