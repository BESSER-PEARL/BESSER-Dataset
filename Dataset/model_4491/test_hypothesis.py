import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    missionsDSL_Value,
    missionsDSL_NewMissions,
    missionsDSL_Action,
    missionsDSL_Condition,
    missionsDSL_Mission,
    missionsDSL_Robot,
    Sensor,
    Relation,
    MissionType,
    EV3_ACTION,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_missionsdsl_value_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_Value)


def test_missionsdsl_value_constructor_exists():
    assert callable(missionsDSL_Value.__init__)


def test_missionsdsl_value_constructor_args():
    sig = inspect.signature(missionsDSL_Value.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"
    assert "bool" in params, "Missing parameter 'bool'"
    assert "color" in params, "Missing parameter 'color'"

def test_missionsdsl_value_has_integer():
    assert hasattr(missionsDSL_Value, "integer")
    descriptor = None
    for klass in missionsDSL_Value.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_value_has_bool():
    assert hasattr(missionsDSL_Value, "bool")
    descriptor = None
    for klass in missionsDSL_Value.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_value_has_color():
    assert hasattr(missionsDSL_Value, "color")
    descriptor = None
    for klass in missionsDSL_Value.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl_newmissions_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_NewMissions)


def test_missionsdsl_newmissions_constructor_exists():
    assert callable(missionsDSL_NewMissions.__init__)


def test_missionsdsl_newmissions_constructor_args():
    sig = inspect.signature(missionsDSL_NewMissions.__init__)
    params = list(sig.parameters.keys())



def test_missionsdsl_action_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_Action)


def test_missionsdsl_action_constructor_exists():
    assert callable(missionsDSL_Action.__init__)


def test_missionsdsl_action_constructor_args():
    sig = inspect.signature(missionsDSL_Action.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "value" in params, "Missing parameter 'value'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_missionsdsl_action_has_action():
    assert hasattr(missionsDSL_Action, "action")
    descriptor = None
    for klass in missionsDSL_Action.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_action_has_value():
    assert hasattr(missionsDSL_Action, "value")
    descriptor = None
    for klass in missionsDSL_Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_action_has_duration():
    assert hasattr(missionsDSL_Action, "duration")
    descriptor = None
    for klass in missionsDSL_Action.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl_condition_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_Condition)


def test_missionsdsl_condition_constructor_exists():
    assert callable(missionsDSL_Condition.__init__)


def test_missionsdsl_condition_constructor_args():
    sig = inspect.signature(missionsDSL_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "sensor" in params, "Missing parameter 'sensor'"
    assert "relation" in params, "Missing parameter 'relation'"

def test_missionsdsl_condition_has_sensor():
    assert hasattr(missionsDSL_Condition, "sensor")
    descriptor = None
    for klass in missionsDSL_Condition.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_condition_has_relation():
    assert hasattr(missionsDSL_Condition, "relation")
    descriptor = None
    for klass in missionsDSL_Condition.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl_mission_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_Mission)


def test_missionsdsl_mission_constructor_exists():
    assert callable(missionsDSL_Mission.__init__)


def test_missionsdsl_mission_constructor_args():
    sig = inspect.signature(missionsDSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_missionsdsl_mission_has_type():
    assert hasattr(missionsDSL_Mission, "type")
    descriptor = None
    for klass in missionsDSL_Mission.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_mission_has_priority():
    assert hasattr(missionsDSL_Mission, "priority")
    descriptor = None
    for klass in missionsDSL_Mission.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_mission_has_name():
    assert hasattr(missionsDSL_Mission, "name")
    descriptor = None
    for klass in missionsDSL_Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl_robot_is_not_abstract():
    assert not inspect.isabstract(missionsDSL_Robot)


def test_missionsdsl_robot_constructor_exists():
    assert callable(missionsDSL_Robot.__init__)


def test_missionsdsl_robot_constructor_args():
    sig = inspect.signature(missionsDSL_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "refreshRate" in params, "Missing parameter 'refreshRate'"
    assert "slaveAddress" in params, "Missing parameter 'slaveAddress'"
    assert "maxAngle" in params, "Missing parameter 'maxAngle'"
    assert "slowSpeed" in params, "Missing parameter 'slowSpeed'"
    assert "minAngle" in params, "Missing parameter 'minAngle'"
    assert "defaultSpeed" in params, "Missing parameter 'defaultSpeed'"

def test_missionsdsl_robot_has_refreshRate():
    assert hasattr(missionsDSL_Robot, "refreshRate")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "refreshRate" in klass.__dict__:
            descriptor = klass.__dict__["refreshRate"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_robot_has_slaveAddress():
    assert hasattr(missionsDSL_Robot, "slaveAddress")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "slaveAddress" in klass.__dict__:
            descriptor = klass.__dict__["slaveAddress"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_robot_has_maxAngle():
    assert hasattr(missionsDSL_Robot, "maxAngle")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "maxAngle" in klass.__dict__:
            descriptor = klass.__dict__["maxAngle"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_robot_has_slowSpeed():
    assert hasattr(missionsDSL_Robot, "slowSpeed")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "slowSpeed" in klass.__dict__:
            descriptor = klass.__dict__["slowSpeed"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_robot_has_minAngle():
    assert hasattr(missionsDSL_Robot, "minAngle")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "minAngle" in klass.__dict__:
            descriptor = klass.__dict__["minAngle"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl_robot_has_defaultSpeed():
    assert hasattr(missionsDSL_Robot, "defaultSpeed")
    descriptor = None
    for klass in missionsDSL_Robot.__mro__:
        if "defaultSpeed" in klass.__dict__:
            descriptor = klass.__dict__["defaultSpeed"]
            break
    assert isinstance(descriptor, property)

def test_sensor_exists():
    # Check that the Enumeration exists
    assert Sensor is not None

def test_sensor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sensor]
    expected_literals = [
        "proximity",
        "touch",
        "color",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sensor"

def test_relation_exists():
    # Check that the Enumeration exists
    assert Relation is not None

def test_relation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Relation]
    expected_literals = [
        "EQ",
        "GT",
        "GE",
        "LE",
        "LT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Relation"

def test_missiontype_exists():
    # Check that the Enumeration exists
    assert MissionType is not None

def test_missiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MissionType]
    expected_literals = [
        "FINDINORDER",
        "AVOID",
        "FINDSIMULTANEOUS",
        "FIND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MissionType"

def test_ev3_action_exists():
    # Check that the Enumeration exists
    assert EV3_ACTION is not None

def test_ev3_action_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EV3_ACTION]
    expected_literals = [
        "HALT",
        "STOP",
        "ROTATE",
        "PLAY",
        "REVERSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EV3_ACTION"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "RED",
        "BROWN",
        "WHITE",
        "BLUE",
        "BLACK",
        "GREEN",
        "YELLOW",
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
missionsDSL_Value_strategy = st.builds(
    missionsDSL_Value,
    integer=
        st.integers(),
    bool=
        safe_text,
    color=
        safe_text
)
missionsDSL_NewMissions_strategy = st.builds(
    missionsDSL_NewMissions,
)
missionsDSL_Action_strategy = st.builds(
    missionsDSL_Action,
    action=
        safe_text,
    value=
        st.integers(),
    duration=
        st.integers()
)
missionsDSL_Condition_strategy = st.builds(
    missionsDSL_Condition,
    sensor=
        safe_text,
    relation=
        safe_text
)
missionsDSL_Mission_strategy = st.builds(
    missionsDSL_Mission,
    type=
        safe_text,
    priority=
        st.integers(),
    name=
        safe_text
)
missionsDSL_Robot_strategy = st.builds(
    missionsDSL_Robot,
    refreshRate=
        st.integers(),
    slaveAddress=
        safe_text,
    maxAngle=
        st.integers(),
    slowSpeed=
        st.integers(),
    minAngle=
        st.integers(),
    defaultSpeed=
        st.integers()
)

@given(instance=missionsDSL_Value_strategy)
@settings(max_examples=50)
def test_missionsdsl_value_instantiation(instance):
    assert isinstance(instance, missionsDSL_Value)



@given(instance=missionsDSL_Value_strategy)
def test_missionsdsl_value_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original



@given(instance=missionsDSL_Value_strategy)
def test_missionsdsl_value_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original



@given(instance=missionsDSL_Value_strategy)
def test_missionsdsl_value_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=missionsDSL_NewMissions_strategy)
@settings(max_examples=50)
def test_missionsdsl_newmissions_instantiation(instance):
    assert isinstance(instance, missionsDSL_NewMissions)

@given(instance=missionsDSL_Action_strategy)
@settings(max_examples=50)
def test_missionsdsl_action_instantiation(instance):
    assert isinstance(instance, missionsDSL_Action)



@given(instance=missionsDSL_Action_strategy)
def test_missionsdsl_action_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=missionsDSL_Action_strategy)
def test_missionsdsl_action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=missionsDSL_Action_strategy)
def test_missionsdsl_action_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=missionsDSL_Condition_strategy)
@settings(max_examples=50)
def test_missionsdsl_condition_instantiation(instance):
    assert isinstance(instance, missionsDSL_Condition)



@given(instance=missionsDSL_Condition_strategy)
def test_missionsdsl_condition_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original



@given(instance=missionsDSL_Condition_strategy)
def test_missionsdsl_condition_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=missionsDSL_Mission_strategy)
@settings(max_examples=50)
def test_missionsdsl_mission_instantiation(instance):
    assert isinstance(instance, missionsDSL_Mission)



@given(instance=missionsDSL_Mission_strategy)
def test_missionsdsl_mission_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=missionsDSL_Mission_strategy)
def test_missionsdsl_mission_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=missionsDSL_Mission_strategy)
def test_missionsdsl_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=missionsDSL_Robot_strategy)
@settings(max_examples=50)
def test_missionsdsl_robot_instantiation(instance):
    assert isinstance(instance, missionsDSL_Robot)



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_refreshRate_setter(instance):
    original = instance.refreshRate
    instance.refreshRate = original
    assert instance.refreshRate == original



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_slaveAddress_setter(instance):
    original = instance.slaveAddress
    instance.slaveAddress = original
    assert instance.slaveAddress == original



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_maxAngle_setter(instance):
    original = instance.maxAngle
    instance.maxAngle = original
    assert instance.maxAngle == original



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_slowSpeed_setter(instance):
    original = instance.slowSpeed
    instance.slowSpeed = original
    assert instance.slowSpeed == original



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_minAngle_setter(instance):
    original = instance.minAngle
    instance.minAngle = original
    assert instance.minAngle == original



@given(instance=missionsDSL_Robot_strategy)
def test_missionsdsl_robot_defaultSpeed_setter(instance):
    original = instance.defaultSpeed
    instance.defaultSpeed = original
    assert instance.defaultSpeed == original
