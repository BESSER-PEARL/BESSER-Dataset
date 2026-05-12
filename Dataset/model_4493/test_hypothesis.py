import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    robotDSL_Distance,
    robotDSL_Color,
    robotDSL_Sensor,
    robotDSL_Negation,
    robotDSL_Bool,
    robotDSL_Sound,
    robotDSL_ArmOp,
    robotDSL_Direction,
    robotDSL_Action,
    robotDSL_Time,
    robotDSL_Trigger,
    robotDSL_Goal,
    robotDSL_Task,
    robotDSL_Flag,
    robotDSL_Speed,
    robotDSL_Mission,
    robotDSL_Missions,
    SoundName,
    ColorName,
    SensorType,
    DirectionVal,
    ArmOpType,
    BoolType,
    SpeedVal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_robotdsl_distance_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Distance)


def test_robotdsl_distance_constructor_exists():
    assert callable(robotDSL_Distance.__init__)


def test_robotdsl_distance_constructor_args():
    sig = inspect.signature(robotDSL_Distance.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_robotdsl_distance_has_distance():
    assert hasattr(robotDSL_Distance, "distance")
    descriptor = None
    for klass in robotDSL_Distance.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_color_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Color)


def test_robotdsl_color_constructor_exists():
    assert callable(robotDSL_Color.__init__)


def test_robotdsl_color_constructor_args():
    sig = inspect.signature(robotDSL_Color.__init__)
    params = list(sig.parameters.keys())
    assert "colorName" in params, "Missing parameter 'colorName'"

def test_robotdsl_color_has_colorName():
    assert hasattr(robotDSL_Color, "colorName")
    descriptor = None
    for klass in robotDSL_Color.__mro__:
        if "colorName" in klass.__dict__:
            descriptor = klass.__dict__["colorName"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_sensor_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Sensor)


def test_robotdsl_sensor_constructor_exists():
    assert callable(robotDSL_Sensor.__init__)


def test_robotdsl_sensor_constructor_args():
    sig = inspect.signature(robotDSL_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "sensorType" in params, "Missing parameter 'sensorType'"

def test_robotdsl_sensor_has_sensorType():
    assert hasattr(robotDSL_Sensor, "sensorType")
    descriptor = None
    for klass in robotDSL_Sensor.__mro__:
        if "sensorType" in klass.__dict__:
            descriptor = klass.__dict__["sensorType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_negation_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Negation)


def test_robotdsl_negation_constructor_exists():
    assert callable(robotDSL_Negation.__init__)


def test_robotdsl_negation_constructor_args():
    sig = inspect.signature(robotDSL_Negation.__init__)
    params = list(sig.parameters.keys())
    assert "NOT" in params, "Missing parameter 'NOT'"

def test_robotdsl_negation_has_NOT():
    assert hasattr(robotDSL_Negation, "NOT")
    descriptor = None
    for klass in robotDSL_Negation.__mro__:
        if "NOT" in klass.__dict__:
            descriptor = klass.__dict__["NOT"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_bool_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Bool)


def test_robotdsl_bool_constructor_exists():
    assert callable(robotDSL_Bool.__init__)


def test_robotdsl_bool_constructor_args():
    sig = inspect.signature(robotDSL_Bool.__init__)
    params = list(sig.parameters.keys())
    assert "boolType" in params, "Missing parameter 'boolType'"

def test_robotdsl_bool_has_boolType():
    assert hasattr(robotDSL_Bool, "boolType")
    descriptor = None
    for klass in robotDSL_Bool.__mro__:
        if "boolType" in klass.__dict__:
            descriptor = klass.__dict__["boolType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_sound_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Sound)


def test_robotdsl_sound_constructor_exists():
    assert callable(robotDSL_Sound.__init__)


def test_robotdsl_sound_constructor_args():
    sig = inspect.signature(robotDSL_Sound.__init__)
    params = list(sig.parameters.keys())
    assert "soundName" in params, "Missing parameter 'soundName'"

def test_robotdsl_sound_has_soundName():
    assert hasattr(robotDSL_Sound, "soundName")
    descriptor = None
    for klass in robotDSL_Sound.__mro__:
        if "soundName" in klass.__dict__:
            descriptor = klass.__dict__["soundName"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_armop_is_not_abstract():
    assert not inspect.isabstract(robotDSL_ArmOp)


def test_robotdsl_armop_constructor_exists():
    assert callable(robotDSL_ArmOp.__init__)


def test_robotdsl_armop_constructor_args():
    sig = inspect.signature(robotDSL_ArmOp.__init__)
    params = list(sig.parameters.keys())
    assert "opType" in params, "Missing parameter 'opType'"

def test_robotdsl_armop_has_opType():
    assert hasattr(robotDSL_ArmOp, "opType")
    descriptor = None
    for klass in robotDSL_ArmOp.__mro__:
        if "opType" in klass.__dict__:
            descriptor = klass.__dict__["opType"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_direction_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Direction)


def test_robotdsl_direction_constructor_exists():
    assert callable(robotDSL_Direction.__init__)


def test_robotdsl_direction_constructor_args():
    sig = inspect.signature(robotDSL_Direction.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_robotdsl_direction_has_dir():
    assert hasattr(robotDSL_Direction, "dir")
    descriptor = None
    for klass in robotDSL_Direction.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_action_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Action)


def test_robotdsl_action_constructor_exists():
    assert callable(robotDSL_Action.__init__)


def test_robotdsl_action_constructor_args():
    sig = inspect.signature(robotDSL_Action.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "degr" in params, "Missing parameter 'degr'"
    assert "cent" in params, "Missing parameter 'cent'"

def test_robotdsl_action_has_duration():
    assert hasattr(robotDSL_Action, "duration")
    descriptor = None
    for klass in robotDSL_Action.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl_action_has_degr():
    assert hasattr(robotDSL_Action, "degr")
    descriptor = None
    for klass in robotDSL_Action.__mro__:
        if "degr" in klass.__dict__:
            descriptor = klass.__dict__["degr"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl_action_has_cent():
    assert hasattr(robotDSL_Action, "cent")
    descriptor = None
    for klass in robotDSL_Action.__mro__:
        if "cent" in klass.__dict__:
            descriptor = klass.__dict__["cent"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_time_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Time)


def test_robotdsl_time_constructor_exists():
    assert callable(robotDSL_Time.__init__)


def test_robotdsl_time_constructor_args():
    sig = inspect.signature(robotDSL_Time.__init__)
    params = list(sig.parameters.keys())
    assert "sec" in params, "Missing parameter 'sec'"

def test_robotdsl_time_has_sec():
    assert hasattr(robotDSL_Time, "sec")
    descriptor = None
    for klass in robotDSL_Time.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_trigger_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Trigger)


def test_robotdsl_trigger_constructor_exists():
    assert callable(robotDSL_Trigger.__init__)


def test_robotdsl_trigger_constructor_args():
    sig = inspect.signature(robotDSL_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "touching" in params, "Missing parameter 'touching'"

def test_robotdsl_trigger_has_degrees():
    assert hasattr(robotDSL_Trigger, "degrees")
    descriptor = None
    for klass in robotDSL_Trigger.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl_trigger_has_touching():
    assert hasattr(robotDSL_Trigger, "touching")
    descriptor = None
    for klass in robotDSL_Trigger.__mro__:
        if "touching" in klass.__dict__:
            descriptor = klass.__dict__["touching"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_goal_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Goal)


def test_robotdsl_goal_constructor_exists():
    assert callable(robotDSL_Goal.__init__)


def test_robotdsl_goal_constructor_args():
    sig = inspect.signature(robotDSL_Goal.__init__)
    params = list(sig.parameters.keys())



def test_robotdsl_task_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Task)


def test_robotdsl_task_constructor_exists():
    assert callable(robotDSL_Task.__init__)


def test_robotdsl_task_constructor_args():
    sig = inspect.signature(robotDSL_Task.__init__)
    params = list(sig.parameters.keys())
    assert "prio" in params, "Missing parameter 'prio'"
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl_task_has_prio():
    assert hasattr(robotDSL_Task, "prio")
    descriptor = None
    for klass in robotDSL_Task.__mro__:
        if "prio" in klass.__dict__:
            descriptor = klass.__dict__["prio"]
            break
    assert isinstance(descriptor, property)

def test_robotdsl_task_has_name():
    assert hasattr(robotDSL_Task, "name")
    descriptor = None
    for klass in robotDSL_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_flag_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Flag)


def test_robotdsl_flag_constructor_exists():
    assert callable(robotDSL_Flag.__init__)


def test_robotdsl_flag_constructor_args():
    sig = inspect.signature(robotDSL_Flag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl_flag_has_name():
    assert hasattr(robotDSL_Flag, "name")
    descriptor = None
    for klass in robotDSL_Flag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_speed_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Speed)


def test_robotdsl_speed_constructor_exists():
    assert callable(robotDSL_Speed.__init__)


def test_robotdsl_speed_constructor_args():
    sig = inspect.signature(robotDSL_Speed.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"

def test_robotdsl_speed_has_speed():
    assert hasattr(robotDSL_Speed, "speed")
    descriptor = None
    for klass in robotDSL_Speed.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_mission_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Mission)


def test_robotdsl_mission_constructor_exists():
    assert callable(robotDSL_Mission.__init__)


def test_robotdsl_mission_constructor_args():
    sig = inspect.signature(robotDSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl_mission_has_name():
    assert hasattr(robotDSL_Mission, "name")
    descriptor = None
    for klass in robotDSL_Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_robotdsl_missions_is_not_abstract():
    assert not inspect.isabstract(robotDSL_Missions)


def test_robotdsl_missions_constructor_exists():
    assert callable(robotDSL_Missions.__init__)


def test_robotdsl_missions_constructor_args():
    sig = inspect.signature(robotDSL_Missions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_robotdsl_missions_has_name():
    assert hasattr(robotDSL_Missions, "name")
    descriptor = None
    for klass in robotDSL_Missions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_soundname_exists():
    # Check that the Enumeration exists
    assert SoundName is not None

def test_soundname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SoundName]
    expected_literals = [
        "FANFARE",
        "BUZZ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SoundName"

def test_colorname_exists():
    # Check that the Enumeration exists
    assert ColorName is not None

def test_colorname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorName]
    expected_literals = [
        "BLUE",
        "GREEN",
        "RED",
        "BLACK",
        "WHITE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorName"

def test_sensortype_exists():
    # Check that the Enumeration exists
    assert SensorType is not None

def test_sensortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SensorType]
    expected_literals = [
        "GYRO",
        "LEFTTOUCH",
        "FRONTUS",
        "RIGHTLIGHT",
        "LEFTLIGHT",
        "RIGHTTOUCH",
        "BACKUS",
        "COLOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SensorType"

def test_directionval_exists():
    # Check that the Enumeration exists
    assert DirectionVal is not None

def test_directionval_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionVal]
    expected_literals = [
        "BACKWARD",
        "RIGHT",
        "LEFT",
        "FORWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionVal"

def test_armoptype_exists():
    # Check that the Enumeration exists
    assert ArmOpType is not None

def test_armoptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArmOpType]
    expected_literals = [
        "DOWN",
        "UP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArmOpType"

def test_booltype_exists():
    # Check that the Enumeration exists
    assert BoolType is not None

def test_booltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoolType]
    expected_literals = [
        "TRUE",
        "L",
        "OR",
        "G",
        "AND",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoolType"

def test_speedval_exists():
    # Check that the Enumeration exists
    assert SpeedVal is not None

def test_speedval_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpeedVal]
    expected_literals = [
        "HIGH",
        "MED",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpeedVal"


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
robotDSL_Distance_strategy = st.builds(
    robotDSL_Distance,
    distance=
        st.integers()
)
robotDSL_Color_strategy = st.builds(
    robotDSL_Color,
    colorName=
        safe_text
)
robotDSL_Sensor_strategy = st.builds(
    robotDSL_Sensor,
    sensorType=
        safe_text
)
robotDSL_Negation_strategy = st.builds(
    robotDSL_Negation,
    NOT=
        safe_text
)
robotDSL_Bool_strategy = st.builds(
    robotDSL_Bool,
    boolType=
        safe_text
)
robotDSL_Sound_strategy = st.builds(
    robotDSL_Sound,
    soundName=
        safe_text
)
robotDSL_ArmOp_strategy = st.builds(
    robotDSL_ArmOp,
    opType=
        safe_text
)
robotDSL_Direction_strategy = st.builds(
    robotDSL_Direction,
    dir=
        safe_text
)
robotDSL_Action_strategy = st.builds(
    robotDSL_Action,
    duration=
        st.integers(),
    degr=
        st.integers(),
    cent=
        safe_text
)
robotDSL_Time_strategy = st.builds(
    robotDSL_Time,
    sec=
        st.integers()
)
robotDSL_Trigger_strategy = st.builds(
    robotDSL_Trigger,
    degrees=
        st.integers(),
    touching=
        safe_text
)
robotDSL_Goal_strategy = st.builds(
    robotDSL_Goal,
)
robotDSL_Task_strategy = st.builds(
    robotDSL_Task,
    prio=
        st.integers(),
    name=
        safe_text
)
robotDSL_Flag_strategy = st.builds(
    robotDSL_Flag,
    name=
        safe_text
)
robotDSL_Speed_strategy = st.builds(
    robotDSL_Speed,
    speed=
        safe_text
)
robotDSL_Mission_strategy = st.builds(
    robotDSL_Mission,
    name=
        safe_text
)
robotDSL_Missions_strategy = st.builds(
    robotDSL_Missions,
    name=
        safe_text
)

@given(instance=robotDSL_Distance_strategy)
@settings(max_examples=50)
def test_robotdsl_distance_instantiation(instance):
    assert isinstance(instance, robotDSL_Distance)



@given(instance=robotDSL_Distance_strategy)
def test_robotdsl_distance_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=robotDSL_Color_strategy)
@settings(max_examples=50)
def test_robotdsl_color_instantiation(instance):
    assert isinstance(instance, robotDSL_Color)



@given(instance=robotDSL_Color_strategy)
def test_robotdsl_color_colorName_setter(instance):
    original = instance.colorName
    instance.colorName = original
    assert instance.colorName == original

@given(instance=robotDSL_Sensor_strategy)
@settings(max_examples=50)
def test_robotdsl_sensor_instantiation(instance):
    assert isinstance(instance, robotDSL_Sensor)



@given(instance=robotDSL_Sensor_strategy)
def test_robotdsl_sensor_sensorType_setter(instance):
    original = instance.sensorType
    instance.sensorType = original
    assert instance.sensorType == original

@given(instance=robotDSL_Negation_strategy)
@settings(max_examples=50)
def test_robotdsl_negation_instantiation(instance):
    assert isinstance(instance, robotDSL_Negation)



@given(instance=robotDSL_Negation_strategy)
def test_robotdsl_negation_NOT_setter(instance):
    original = instance.NOT
    instance.NOT = original
    assert instance.NOT == original

@given(instance=robotDSL_Bool_strategy)
@settings(max_examples=50)
def test_robotdsl_bool_instantiation(instance):
    assert isinstance(instance, robotDSL_Bool)



@given(instance=robotDSL_Bool_strategy)
def test_robotdsl_bool_boolType_setter(instance):
    original = instance.boolType
    instance.boolType = original
    assert instance.boolType == original

@given(instance=robotDSL_Sound_strategy)
@settings(max_examples=50)
def test_robotdsl_sound_instantiation(instance):
    assert isinstance(instance, robotDSL_Sound)



@given(instance=robotDSL_Sound_strategy)
def test_robotdsl_sound_soundName_setter(instance):
    original = instance.soundName
    instance.soundName = original
    assert instance.soundName == original

@given(instance=robotDSL_ArmOp_strategy)
@settings(max_examples=50)
def test_robotdsl_armop_instantiation(instance):
    assert isinstance(instance, robotDSL_ArmOp)



@given(instance=robotDSL_ArmOp_strategy)
def test_robotdsl_armop_opType_setter(instance):
    original = instance.opType
    instance.opType = original
    assert instance.opType == original

@given(instance=robotDSL_Direction_strategy)
@settings(max_examples=50)
def test_robotdsl_direction_instantiation(instance):
    assert isinstance(instance, robotDSL_Direction)



@given(instance=robotDSL_Direction_strategy)
def test_robotdsl_direction_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=robotDSL_Action_strategy)
@settings(max_examples=50)
def test_robotdsl_action_instantiation(instance):
    assert isinstance(instance, robotDSL_Action)



@given(instance=robotDSL_Action_strategy)
def test_robotdsl_action_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=robotDSL_Action_strategy)
def test_robotdsl_action_degr_setter(instance):
    original = instance.degr
    instance.degr = original
    assert instance.degr == original



@given(instance=robotDSL_Action_strategy)
def test_robotdsl_action_cent_setter(instance):
    original = instance.cent
    instance.cent = original
    assert instance.cent == original

@given(instance=robotDSL_Time_strategy)
@settings(max_examples=50)
def test_robotdsl_time_instantiation(instance):
    assert isinstance(instance, robotDSL_Time)



@given(instance=robotDSL_Time_strategy)
def test_robotdsl_time_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original

@given(instance=robotDSL_Trigger_strategy)
@settings(max_examples=50)
def test_robotdsl_trigger_instantiation(instance):
    assert isinstance(instance, robotDSL_Trigger)



@given(instance=robotDSL_Trigger_strategy)
def test_robotdsl_trigger_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original



@given(instance=robotDSL_Trigger_strategy)
def test_robotdsl_trigger_touching_setter(instance):
    original = instance.touching
    instance.touching = original
    assert instance.touching == original

@given(instance=robotDSL_Goal_strategy)
@settings(max_examples=50)
def test_robotdsl_goal_instantiation(instance):
    assert isinstance(instance, robotDSL_Goal)

@given(instance=robotDSL_Task_strategy)
@settings(max_examples=50)
def test_robotdsl_task_instantiation(instance):
    assert isinstance(instance, robotDSL_Task)



@given(instance=robotDSL_Task_strategy)
def test_robotdsl_task_prio_setter(instance):
    original = instance.prio
    instance.prio = original
    assert instance.prio == original



@given(instance=robotDSL_Task_strategy)
def test_robotdsl_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL_Flag_strategy)
@settings(max_examples=50)
def test_robotdsl_flag_instantiation(instance):
    assert isinstance(instance, robotDSL_Flag)



@given(instance=robotDSL_Flag_strategy)
def test_robotdsl_flag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL_Speed_strategy)
@settings(max_examples=50)
def test_robotdsl_speed_instantiation(instance):
    assert isinstance(instance, robotDSL_Speed)



@given(instance=robotDSL_Speed_strategy)
def test_robotdsl_speed_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=robotDSL_Mission_strategy)
@settings(max_examples=50)
def test_robotdsl_mission_instantiation(instance):
    assert isinstance(instance, robotDSL_Mission)



@given(instance=robotDSL_Mission_strategy)
def test_robotdsl_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=robotDSL_Missions_strategy)
@settings(max_examples=50)
def test_robotdsl_missions_instantiation(instance):
    assert isinstance(instance, robotDSL_Missions)



@given(instance=robotDSL_Missions_strategy)
def test_robotdsl_missions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
