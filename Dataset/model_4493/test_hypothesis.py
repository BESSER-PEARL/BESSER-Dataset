import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    robotDSL::Distance,
    robotDSL::Color,
    robotDSL::Sensor,
    robotDSL::Negation,
    robotDSL::Bool,
    robotDSL::Sound,
    robotDSL::ArmOp,
    robotDSL::Direction,
    robotDSL::Action,
    robotDSL::Time,
    robotDSL::Trigger,
    robotDSL::Goal,
    robotDSL::Task,
    robotDSL::Flag,
    robotDSL::Speed,
    robotDSL::Mission,
    robotDSL::Missions,
    SensorType,
    SoundName,
    SpeedVal,
    DirectionVal,
    BoolType,
    ColorName,
    ArmOpType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robotdsl::distance_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Distance)


def test_robotdsl::distance_constructor_exists():
    assert callable(robotDSL::Distance.__init__)


def test_robotdsl::distance_constructor_args():
    sig = inspect.signature(robotDSL::Distance.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_robotdsl::distance_has_distance():
    assert hasattr(robotDSL::Distance, "distance")
    descriptor = None
    for klass in robotDSL::Distance.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::color_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Color)


def test_robotdsl::color_constructor_exists():
    assert callable(robotDSL::Color.__init__)


def test_robotdsl::color_constructor_args():
    sig = inspect.signature(robotDSL::Color.__init__)
    params = list(sig.parameters.keys())
    assert "colorName" in params, "Missing parameter 'colorName'"

def test_robotdsl::color_has_colorName():
    assert hasattr(robotDSL::Color, "colorName")
    descriptor = None
    for klass in robotDSL::Color.__mro__:
        if "colorName" in klass.__dict__:
            descriptor = klass.__dict__["colorName"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::sensor_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Sensor)


def test_robotdsl::sensor_constructor_exists():
    assert callable(robotDSL::Sensor.__init__)


def test_robotdsl::sensor_constructor_args():
    sig = inspect.signature(robotDSL::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "sensorType" in params, "Missing parameter 'sensorType'"

def test_robotdsl::sensor_has_sensorType():
    assert hasattr(robotDSL::Sensor, "sensorType")
    descriptor = None
    for klass in robotDSL::Sensor.__mro__:
        if "sensorType" in klass.__dict__:
            descriptor = klass.__dict__["sensorType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::negation_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Negation)


def test_robotdsl::negation_constructor_exists():
    assert callable(robotDSL::Negation.__init__)


def test_robotdsl::negation_constructor_args():
    sig = inspect.signature(robotDSL::Negation.__init__)
    params = list(sig.parameters.keys())
    assert "NOT" in params, "Missing parameter 'NOT'"

def test_robotdsl::negation_has_NOT():
    assert hasattr(robotDSL::Negation, "NOT")
    descriptor = None
    for klass in robotDSL::Negation.__mro__:
        if "NOT" in klass.__dict__:
            descriptor = klass.__dict__["NOT"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::bool_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Bool)


def test_robotdsl::bool_constructor_exists():
    assert callable(robotDSL::Bool.__init__)


def test_robotdsl::bool_constructor_args():
    sig = inspect.signature(robotDSL::Bool.__init__)
    params = list(sig.parameters.keys())
    assert "boolType" in params, "Missing parameter 'boolType'"

def test_robotdsl::bool_has_boolType():
    assert hasattr(robotDSL::Bool, "boolType")
    descriptor = None
    for klass in robotDSL::Bool.__mro__:
        if "boolType" in klass.__dict__:
            descriptor = klass.__dict__["boolType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::sound_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Sound)


def test_robotdsl::sound_constructor_exists():
    assert callable(robotDSL::Sound.__init__)


def test_robotdsl::sound_constructor_args():
    sig = inspect.signature(robotDSL::Sound.__init__)
    params = list(sig.parameters.keys())
    assert "soundName" in params, "Missing parameter 'soundName'"

def test_robotdsl::sound_has_soundName():
    assert hasattr(robotDSL::Sound, "soundName")
    descriptor = None
    for klass in robotDSL::Sound.__mro__:
        if "soundName" in klass.__dict__:
            descriptor = klass.__dict__["soundName"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::armop_is_not_abstract():
    assert not inspect.isabstract(robotDSL::ArmOp)


def test_robotdsl::armop_constructor_exists():
    assert callable(robotDSL::ArmOp.__init__)


def test_robotdsl::armop_constructor_args():
    sig = inspect.signature(robotDSL::ArmOp.__init__)
    params = list(sig.parameters.keys())
    assert "opType" in params, "Missing parameter 'opType'"

def test_robotdsl::armop_has_opType():
    assert hasattr(robotDSL::ArmOp, "opType")
    descriptor = None
    for klass in robotDSL::ArmOp.__mro__:
        if "opType" in klass.__dict__:
            descriptor = klass.__dict__["opType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::direction_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Direction)


def test_robotdsl::direction_constructor_exists():
    assert callable(robotDSL::Direction.__init__)


def test_robotdsl::direction_constructor_args():
    sig = inspect.signature(robotDSL::Direction.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_robotdsl::direction_has_dir():
    assert hasattr(robotDSL::Direction, "dir")
    descriptor = None
    for klass in robotDSL::Direction.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::action_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Action)


def test_robotdsl::action_constructor_exists():
    assert callable(robotDSL::Action.__init__)


def test_robotdsl::action_constructor_args():
    sig = inspect.signature(robotDSL::Action.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "degr" in params, "Missing parameter 'degr'"
    assert "cent" in params, "Missing parameter 'cent'"

def test_robotdsl::action_has_duration():
    assert hasattr(robotDSL::Action, "duration")
    descriptor = None
    for klass in robotDSL::Action.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl::action_has_degr():
    assert hasattr(robotDSL::Action, "degr")
    descriptor = None
    for klass in robotDSL::Action.__mro__:
        if "degr" in klass.__dict__:
            descriptor = klass.__dict__["degr"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl::action_has_cent():
    assert hasattr(robotDSL::Action, "cent")
    descriptor = None
    for klass in robotDSL::Action.__mro__:
        if "cent" in klass.__dict__:
            descriptor = klass.__dict__["cent"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::time_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Time)


def test_robotdsl::time_constructor_exists():
    assert callable(robotDSL::Time.__init__)


def test_robotdsl::time_constructor_args():
    sig = inspect.signature(robotDSL::Time.__init__)
    params = list(sig.parameters.keys())
    assert "sec" in params, "Missing parameter 'sec'"

def test_robotdsl::time_has_sec():
    assert hasattr(robotDSL::Time, "sec")
    descriptor = None
    for klass in robotDSL::Time.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::trigger_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Trigger)


def test_robotdsl::trigger_constructor_exists():
    assert callable(robotDSL::Trigger.__init__)


def test_robotdsl::trigger_constructor_args():
    sig = inspect.signature(robotDSL::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "touching" in params, "Missing parameter 'touching'"

def test_robotdsl::trigger_has_degrees():
    assert hasattr(robotDSL::Trigger, "degrees")
    descriptor = None
    for klass in robotDSL::Trigger.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl::trigger_has_touching():
    assert hasattr(robotDSL::Trigger, "touching")
    descriptor = None
    for klass in robotDSL::Trigger.__mro__:
        if "touching" in klass.__dict__:
            descriptor = klass.__dict__["touching"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::goal_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Goal)


def test_robotdsl::goal_constructor_exists():
    assert callable(robotDSL::Goal.__init__)


def test_robotdsl::goal_constructor_args():
    sig = inspect.signature(robotDSL::Goal.__init__)
    params = list(sig.parameters.keys())



def test_robotdsl::task_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Task)


def test_robotdsl::task_constructor_exists():
    assert callable(robotDSL::Task.__init__)


def test_robotdsl::task_constructor_args():
    sig = inspect.signature(robotDSL::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "prio" in params, "Missing parameter 'prio'"

def test_robotdsl::task_has_name():
    assert hasattr(robotDSL::Task, "name")
    descriptor = None
    for klass in robotDSL::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl::task_has_prio():
    assert hasattr(robotDSL::Task, "prio")
    descriptor = None
    for klass in robotDSL::Task.__mro__:
        if "prio" in klass.__dict__:
            descriptor = klass.__dict__["prio"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::flag_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Flag)


def test_robotdsl::flag_constructor_exists():
    assert callable(robotDSL::Flag.__init__)


def test_robotdsl::flag_constructor_args():
    sig = inspect.signature(robotDSL::Flag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl::flag_has_name():
    assert hasattr(robotDSL::Flag, "name")
    descriptor = None
    for klass in robotDSL::Flag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::speed_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Speed)


def test_robotdsl::speed_constructor_exists():
    assert callable(robotDSL::Speed.__init__)


def test_robotdsl::speed_constructor_args():
    sig = inspect.signature(robotDSL::Speed.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_robotdsl::speed_has_speed():
    assert hasattr(robotDSL::Speed, "speed")
    descriptor = None
    for klass in robotDSL::Speed.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::mission_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Mission)


def test_robotdsl::mission_constructor_exists():
    assert callable(robotDSL::Mission.__init__)


def test_robotdsl::mission_constructor_args():
    sig = inspect.signature(robotDSL::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl::mission_has_name():
    assert hasattr(robotDSL::Mission, "name")
    descriptor = None
    for klass in robotDSL::Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl::missions_is_not_abstract():
    assert not inspect.isabstract(robotDSL::Missions)


def test_robotdsl::missions_constructor_exists():
    assert callable(robotDSL::Missions.__init__)


def test_robotdsl::missions_constructor_args():
    sig = inspect.signature(robotDSL::Missions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl::missions_has_name():
    assert hasattr(robotDSL::Missions, "name")
    descriptor = None
    for klass in robotDSL::Missions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sensortype_exists():
    # Check that the Enumeration exists
    assert SensorType is not None

def test_sensortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SensorType]
    expected_literals = [
        "FRONTUS",
        "RIGHTTOUCH",
        "RIGHTLIGHT",
        "LEFTLIGHT",
        "BACKUS",
        "LEFTTOUCH",
        "COLOR",
        "GYRO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SensorType"

def test_soundname_exists():
    # Check that the Enumeration exists
    assert SoundName is not None

def test_soundname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SoundName]
    expected_literals = [
        "BUZZ",
        "FANFARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SoundName"

def test_speedval_exists():
    # Check that the Enumeration exists
    assert SpeedVal is not None

def test_speedval_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeedVal]
    expected_literals = [
        "MED",
        "HIGH",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeedVal"

def test_directionval_exists():
    # Check that the Enumeration exists
    assert DirectionVal is not None

def test_directionval_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionVal]
    expected_literals = [
        "FORWARD",
        "BACKWARD",
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionVal"

def test_booltype_exists():
    # Check that the Enumeration exists
    assert BoolType is not None

def test_booltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoolType]
    expected_literals = [
        "TRUE",
        "FALSE",
        "L",
        "G",
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoolType"

def test_colorname_exists():
    # Check that the Enumeration exists
    assert ColorName is not None

def test_colorname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorName]
    expected_literals = [
        "BLACK",
        "BLUE",
        "RED",
        "WHITE",
        "GREEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorName"

def test_armoptype_exists():
    # Check that the Enumeration exists
    assert ArmOpType is not None

def test_armoptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArmOpType]
    expected_literals = [
        "UP",
        "DOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArmOpType"


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
robotDSL::Distance_strategy = st.builds(
    robotDSL::Distance,
    distance=
        st.integers()
)
robotDSL::Color_strategy = st.builds(
    robotDSL::Color,
    colorName=
        safe_text
)
robotDSL::Sensor_strategy = st.builds(
    robotDSL::Sensor,
    sensorType=
        safe_text
)
robotDSL::Negation_strategy = st.builds(
    robotDSL::Negation,
    NOT=
        safe_text
)
robotDSL::Bool_strategy = st.builds(
    robotDSL::Bool,
    boolType=
        safe_text
)
robotDSL::Sound_strategy = st.builds(
    robotDSL::Sound,
    soundName=
        safe_text
)
robotDSL::ArmOp_strategy = st.builds(
    robotDSL::ArmOp,
    opType=
        safe_text
)
robotDSL::Direction_strategy = st.builds(
    robotDSL::Direction,
    dir=
        safe_text
)
robotDSL::Action_strategy = st.builds(
    robotDSL::Action,
    duration=
        st.integers(),
    degr=
        st.integers(),
    cent=
        safe_text
)
robotDSL::Time_strategy = st.builds(
    robotDSL::Time,
    sec=
        st.integers()
)
robotDSL::Trigger_strategy = st.builds(
    robotDSL::Trigger,
    degrees=
        st.integers(),
    touching=
        safe_text
)
robotDSL::Goal_strategy = st.builds(
    robotDSL::Goal,
)
robotDSL::Task_strategy = st.builds(
    robotDSL::Task,
    name=
        safe_text,
    prio=
        st.integers()
)
robotDSL::Flag_strategy = st.builds(
    robotDSL::Flag,
    name=
        safe_text
)
robotDSL::Speed_strategy = st.builds(
    robotDSL::Speed,
    speed=
        safe_text
)
robotDSL::Mission_strategy = st.builds(
    robotDSL::Mission,
    name=
        safe_text
)
robotDSL::Missions_strategy = st.builds(
    robotDSL::Missions,
    name=
        safe_text
)

@given(instance=robotDSL::Distance_strategy)
@settings(max_examples=50)
def test_robotdsl::distance_instantiation(instance):
    assert isinstance(instance, robotDSL::Distance)

@given(instance=robotDSL::Distance_strategy)
def test_robotdsl::distance_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=robotDSL::Distance_strategy)
def test_robotdsl::distance_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=robotDSL::Color_strategy)
@settings(max_examples=50)
def test_robotdsl::color_instantiation(instance):
    assert isinstance(instance, robotDSL::Color)

@given(instance=robotDSL::Color_strategy)
def test_robotdsl::color_colorName_type(instance):
    assert isinstance(instance.colorName, str)


@given(instance=robotDSL::Color_strategy)
def test_robotdsl::color_colorName_setter(instance):
    original = instance.colorName
    instance.colorName = original
    assert instance.colorName == original

@given(instance=robotDSL::Sensor_strategy)
@settings(max_examples=50)
def test_robotdsl::sensor_instantiation(instance):
    assert isinstance(instance, robotDSL::Sensor)

@given(instance=robotDSL::Sensor_strategy)
def test_robotdsl::sensor_sensorType_type(instance):
    assert isinstance(instance.sensorType, str)


@given(instance=robotDSL::Sensor_strategy)
def test_robotdsl::sensor_sensorType_setter(instance):
    original = instance.sensorType
    instance.sensorType = original
    assert instance.sensorType == original

@given(instance=robotDSL::Negation_strategy)
@settings(max_examples=50)
def test_robotdsl::negation_instantiation(instance):
    assert isinstance(instance, robotDSL::Negation)

@given(instance=robotDSL::Negation_strategy)
def test_robotdsl::negation_NOT_type(instance):
    assert isinstance(instance.NOT, str)


@given(instance=robotDSL::Negation_strategy)
def test_robotdsl::negation_NOT_setter(instance):
    original = instance.NOT
    instance.NOT = original
    assert instance.NOT == original

@given(instance=robotDSL::Bool_strategy)
@settings(max_examples=50)
def test_robotdsl::bool_instantiation(instance):
    assert isinstance(instance, robotDSL::Bool)

@given(instance=robotDSL::Bool_strategy)
def test_robotdsl::bool_boolType_type(instance):
    assert isinstance(instance.boolType, str)


@given(instance=robotDSL::Bool_strategy)
def test_robotdsl::bool_boolType_setter(instance):
    original = instance.boolType
    instance.boolType = original
    assert instance.boolType == original

@given(instance=robotDSL::Sound_strategy)
@settings(max_examples=50)
def test_robotdsl::sound_instantiation(instance):
    assert isinstance(instance, robotDSL::Sound)

@given(instance=robotDSL::Sound_strategy)
def test_robotdsl::sound_soundName_type(instance):
    assert isinstance(instance.soundName, str)


@given(instance=robotDSL::Sound_strategy)
def test_robotdsl::sound_soundName_setter(instance):
    original = instance.soundName
    instance.soundName = original
    assert instance.soundName == original

@given(instance=robotDSL::ArmOp_strategy)
@settings(max_examples=50)
def test_robotdsl::armop_instantiation(instance):
    assert isinstance(instance, robotDSL::ArmOp)

@given(instance=robotDSL::ArmOp_strategy)
def test_robotdsl::armop_opType_type(instance):
    assert isinstance(instance.opType, str)


@given(instance=robotDSL::ArmOp_strategy)
def test_robotdsl::armop_opType_setter(instance):
    original = instance.opType
    instance.opType = original
    assert instance.opType == original

@given(instance=robotDSL::Direction_strategy)
@settings(max_examples=50)
def test_robotdsl::direction_instantiation(instance):
    assert isinstance(instance, robotDSL::Direction)

@given(instance=robotDSL::Direction_strategy)
def test_robotdsl::direction_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=robotDSL::Direction_strategy)
def test_robotdsl::direction_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=robotDSL::Action_strategy)
@settings(max_examples=50)
def test_robotdsl::action_instantiation(instance):
    assert isinstance(instance, robotDSL::Action)

@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_degr_type(instance):
    assert isinstance(instance.degr, int)


@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_degr_setter(instance):
    original = instance.degr
    instance.degr = original
    assert instance.degr == original

@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_cent_type(instance):
    assert isinstance(instance.cent, str)


@given(instance=robotDSL::Action_strategy)
def test_robotdsl::action_cent_setter(instance):
    original = instance.cent
    instance.cent = original
    assert instance.cent == original

@given(instance=robotDSL::Time_strategy)
@settings(max_examples=50)
def test_robotdsl::time_instantiation(instance):
    assert isinstance(instance, robotDSL::Time)

@given(instance=robotDSL::Time_strategy)
def test_robotdsl::time_sec_type(instance):
    assert isinstance(instance.sec, int)


@given(instance=robotDSL::Time_strategy)
def test_robotdsl::time_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original

@given(instance=robotDSL::Trigger_strategy)
@settings(max_examples=50)
def test_robotdsl::trigger_instantiation(instance):
    assert isinstance(instance, robotDSL::Trigger)

@given(instance=robotDSL::Trigger_strategy)
def test_robotdsl::trigger_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=robotDSL::Trigger_strategy)
def test_robotdsl::trigger_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=robotDSL::Trigger_strategy)
def test_robotdsl::trigger_touching_type(instance):
    assert isinstance(instance.touching, str)


@given(instance=robotDSL::Trigger_strategy)
def test_robotdsl::trigger_touching_setter(instance):
    original = instance.touching
    instance.touching = original
    assert instance.touching == original

@given(instance=robotDSL::Goal_strategy)
@settings(max_examples=50)
def test_robotdsl::goal_instantiation(instance):
    assert isinstance(instance, robotDSL::Goal)

@given(instance=robotDSL::Task_strategy)
@settings(max_examples=50)
def test_robotdsl::task_instantiation(instance):
    assert isinstance(instance, robotDSL::Task)

@given(instance=robotDSL::Task_strategy)
def test_robotdsl::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robotDSL::Task_strategy)
def test_robotdsl::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL::Task_strategy)
def test_robotdsl::task_prio_type(instance):
    assert isinstance(instance.prio, int)


@given(instance=robotDSL::Task_strategy)
def test_robotdsl::task_prio_setter(instance):
    original = instance.prio
    instance.prio = original
    assert instance.prio == original

@given(instance=robotDSL::Flag_strategy)
@settings(max_examples=50)
def test_robotdsl::flag_instantiation(instance):
    assert isinstance(instance, robotDSL::Flag)

@given(instance=robotDSL::Flag_strategy)
def test_robotdsl::flag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robotDSL::Flag_strategy)
def test_robotdsl::flag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL::Speed_strategy)
@settings(max_examples=50)
def test_robotdsl::speed_instantiation(instance):
    assert isinstance(instance, robotDSL::Speed)

@given(instance=robotDSL::Speed_strategy)
def test_robotdsl::speed_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=robotDSL::Speed_strategy)
def test_robotdsl::speed_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=robotDSL::Mission_strategy)
@settings(max_examples=50)
def test_robotdsl::mission_instantiation(instance):
    assert isinstance(instance, robotDSL::Mission)

@given(instance=robotDSL::Mission_strategy)
def test_robotdsl::mission_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robotDSL::Mission_strategy)
def test_robotdsl::mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL::Missions_strategy)
@settings(max_examples=50)
def test_robotdsl::missions_instantiation(instance):
    assert isinstance(instance, robotDSL::Missions)

@given(instance=robotDSL::Missions_strategy)
def test_robotdsl::missions_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=robotDSL::Missions_strategy)
def test_robotdsl::missions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
