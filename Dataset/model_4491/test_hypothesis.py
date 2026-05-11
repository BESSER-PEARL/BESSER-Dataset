import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    missionsDSL::Value,
    missionsDSL::NewMissions,
    missionsDSL::Action,
    missionsDSL::Condition,
    missionsDSL::Mission,
    missionsDSL::Robot,
    Color,
    MissionType,
    Relation,
    EV3_ACTION,
    Sensor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_missionsdsl::value_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::Value)


def test_missionsdsl::value_constructor_exists():
    assert callable(missionsDSL::Value.__init__)


def test_missionsdsl::value_constructor_args():
    sig = inspect.signature(missionsDSL::Value.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"
    assert "color" in params, "Missing parameter 'color'"
    assert "bool" in params, "Missing parameter 'bool'"

def test_missionsdsl::value_has_integer():
    assert hasattr(missionsDSL::Value, "integer")
    descriptor = None
    for klass in missionsDSL::Value.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::value_has_color():
    assert hasattr(missionsDSL::Value, "color")
    descriptor = None
    for klass in missionsDSL::Value.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::value_has_bool():
    assert hasattr(missionsDSL::Value, "bool")
    descriptor = None
    for klass in missionsDSL::Value.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl::newmissions_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::NewMissions)


def test_missionsdsl::newmissions_constructor_exists():
    assert callable(missionsDSL::NewMissions.__init__)


def test_missionsdsl::newmissions_constructor_args():
    sig = inspect.signature(missionsDSL::NewMissions.__init__)
    params = list(sig.parameters.keys())



def test_missionsdsl::action_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::Action)


def test_missionsdsl::action_constructor_exists():
    assert callable(missionsDSL::Action.__init__)


def test_missionsdsl::action_constructor_args():
    sig = inspect.signature(missionsDSL::Action.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "action" in params, "Missing parameter 'action'"
    assert "value" in params, "Missing parameter 'value'"

def test_missionsdsl::action_has_duration():
    assert hasattr(missionsDSL::Action, "duration")
    descriptor = None
    for klass in missionsDSL::Action.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::action_has_action():
    assert hasattr(missionsDSL::Action, "action")
    descriptor = None
    for klass in missionsDSL::Action.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::action_has_value():
    assert hasattr(missionsDSL::Action, "value")
    descriptor = None
    for klass in missionsDSL::Action.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl::condition_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::Condition)


def test_missionsdsl::condition_constructor_exists():
    assert callable(missionsDSL::Condition.__init__)


def test_missionsdsl::condition_constructor_args():
    sig = inspect.signature(missionsDSL::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "sensor" in params, "Missing parameter 'sensor'"
    assert "relation" in params, "Missing parameter 'relation'"

def test_missionsdsl::condition_has_sensor():
    assert hasattr(missionsDSL::Condition, "sensor")
    descriptor = None
    for klass in missionsDSL::Condition.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::condition_has_relation():
    assert hasattr(missionsDSL::Condition, "relation")
    descriptor = None
    for klass in missionsDSL::Condition.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl::mission_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::Mission)


def test_missionsdsl::mission_constructor_exists():
    assert callable(missionsDSL::Mission.__init__)


def test_missionsdsl::mission_constructor_args():
    sig = inspect.signature(missionsDSL::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_missionsdsl::mission_has_priority():
    assert hasattr(missionsDSL::Mission, "priority")
    descriptor = None
    for klass in missionsDSL::Mission.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::mission_has_type():
    assert hasattr(missionsDSL::Mission, "type")
    descriptor = None
    for klass in missionsDSL::Mission.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::mission_has_name():
    assert hasattr(missionsDSL::Mission, "name")
    descriptor = None
    for klass in missionsDSL::Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_missionsdsl::robot_is_not_abstract():
    assert not inspect.isabstract(missionsDSL::Robot)


def test_missionsdsl::robot_constructor_exists():
    assert callable(missionsDSL::Robot.__init__)


def test_missionsdsl::robot_constructor_args():
    sig = inspect.signature(missionsDSL::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "slowSpeed" in params, "Missing parameter 'slowSpeed'"
    assert "slaveAddress" in params, "Missing parameter 'slaveAddress'"
    assert "minAngle" in params, "Missing parameter 'minAngle'"
    assert "refreshRate" in params, "Missing parameter 'refreshRate'"
    assert "defaultSpeed" in params, "Missing parameter 'defaultSpeed'"
    assert "maxAngle" in params, "Missing parameter 'maxAngle'"

def test_missionsdsl::robot_has_slowSpeed():
    assert hasattr(missionsDSL::Robot, "slowSpeed")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "slowSpeed" in klass.__dict__:
            descriptor = klass.__dict__["slowSpeed"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::robot_has_slaveAddress():
    assert hasattr(missionsDSL::Robot, "slaveAddress")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "slaveAddress" in klass.__dict__:
            descriptor = klass.__dict__["slaveAddress"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::robot_has_minAngle():
    assert hasattr(missionsDSL::Robot, "minAngle")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "minAngle" in klass.__dict__:
            descriptor = klass.__dict__["minAngle"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::robot_has_refreshRate():
    assert hasattr(missionsDSL::Robot, "refreshRate")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "refreshRate" in klass.__dict__:
            descriptor = klass.__dict__["refreshRate"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::robot_has_defaultSpeed():
    assert hasattr(missionsDSL::Robot, "defaultSpeed")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "defaultSpeed" in klass.__dict__:
            descriptor = klass.__dict__["defaultSpeed"]
            break
    assert isinstance(descriptor, property)

def test_missionsdsl::robot_has_maxAngle():
    assert hasattr(missionsDSL::Robot, "maxAngle")
    descriptor = None
    for klass in missionsDSL::Robot.__mro__:
        if "maxAngle" in klass.__dict__:
            descriptor = klass.__dict__["maxAngle"]
            break
    assert isinstance(descriptor, property)

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "GREEN",
        "RED",
        "WHITE",
        "BLUE",
        "YELLOW",
        "BROWN",
        "BLACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_missiontype_exists():
    # Check that the Enumeration exists
    assert MissionType is not None

def test_missiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MissionType]
    expected_literals = [
        "FIND",
        "FINDINORDER",
        "AVOID",
        "FINDSIMULTANEOUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MissionType"

def test_relation_exists():
    # Check that the Enumeration exists
    assert Relation is not None

def test_relation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Relation]
    expected_literals = [
        "LE",
        "GE",
        "LT",
        "GT",
        "EQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Relation"

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

def test_sensor_exists():
    # Check that the Enumeration exists
    assert Sensor is not None

def test_sensor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sensor]
    expected_literals = [
        "touch",
        "color",
        "proximity",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sensor"


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
missionsDSL::Value_strategy = st.builds(
    missionsDSL::Value,
    integer=
        st.integers(),
    color=
        safe_text,
    bool=
        safe_text
)
missionsDSL::NewMissions_strategy = st.builds(
    missionsDSL::NewMissions,
)
missionsDSL::Action_strategy = st.builds(
    missionsDSL::Action,
    duration=
        st.integers(),
    action=
        safe_text,
    value=
        st.integers()
)
missionsDSL::Condition_strategy = st.builds(
    missionsDSL::Condition,
    sensor=
        safe_text,
    relation=
        safe_text
)
missionsDSL::Mission_strategy = st.builds(
    missionsDSL::Mission,
    priority=
        st.integers(),
    type=
        safe_text,
    name=
        safe_text
)
missionsDSL::Robot_strategy = st.builds(
    missionsDSL::Robot,
    slowSpeed=
        st.integers(),
    slaveAddress=
        safe_text,
    minAngle=
        st.integers(),
    refreshRate=
        st.integers(),
    defaultSpeed=
        st.integers(),
    maxAngle=
        st.integers()
)

@given(instance=missionsDSL::Value_strategy)
@settings(max_examples=50)
def test_missionsdsl::value_instantiation(instance):
    assert isinstance(instance, missionsDSL::Value)

@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_integer_type(instance):
    assert isinstance(instance.integer, int)


@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_bool_type(instance):
    assert isinstance(instance.bool, str)


@given(instance=missionsDSL::Value_strategy)
def test_missionsdsl::value_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=missionsDSL::NewMissions_strategy)
@settings(max_examples=50)
def test_missionsdsl::newmissions_instantiation(instance):
    assert isinstance(instance, missionsDSL::NewMissions)

@given(instance=missionsDSL::Action_strategy)
@settings(max_examples=50)
def test_missionsdsl::action_instantiation(instance):
    assert isinstance(instance, missionsDSL::Action)

@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=missionsDSL::Action_strategy)
def test_missionsdsl::action_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=missionsDSL::Condition_strategy)
@settings(max_examples=50)
def test_missionsdsl::condition_instantiation(instance):
    assert isinstance(instance, missionsDSL::Condition)

@given(instance=missionsDSL::Condition_strategy)
def test_missionsdsl::condition_sensor_type(instance):
    assert isinstance(instance.sensor, str)


@given(instance=missionsDSL::Condition_strategy)
def test_missionsdsl::condition_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=missionsDSL::Condition_strategy)
def test_missionsdsl::condition_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=missionsDSL::Condition_strategy)
def test_missionsdsl::condition_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=missionsDSL::Mission_strategy)
@settings(max_examples=50)
def test_missionsdsl::mission_instantiation(instance):
    assert isinstance(instance, missionsDSL::Mission)

@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=missionsDSL::Mission_strategy)
def test_missionsdsl::mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=missionsDSL::Robot_strategy)
@settings(max_examples=50)
def test_missionsdsl::robot_instantiation(instance):
    assert isinstance(instance, missionsDSL::Robot)

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_slowSpeed_type(instance):
    assert isinstance(instance.slowSpeed, int)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_slowSpeed_setter(instance):
    original = instance.slowSpeed
    instance.slowSpeed = original
    assert instance.slowSpeed == original

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_slaveAddress_type(instance):
    assert isinstance(instance.slaveAddress, str)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_slaveAddress_setter(instance):
    original = instance.slaveAddress
    instance.slaveAddress = original
    assert instance.slaveAddress == original

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_minAngle_type(instance):
    assert isinstance(instance.minAngle, int)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_minAngle_setter(instance):
    original = instance.minAngle
    instance.minAngle = original
    assert instance.minAngle == original

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_refreshRate_type(instance):
    assert isinstance(instance.refreshRate, int)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_refreshRate_setter(instance):
    original = instance.refreshRate
    instance.refreshRate = original
    assert instance.refreshRate == original

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_defaultSpeed_type(instance):
    assert isinstance(instance.defaultSpeed, int)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_defaultSpeed_setter(instance):
    original = instance.defaultSpeed
    instance.defaultSpeed = original
    assert instance.defaultSpeed == original

@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_maxAngle_type(instance):
    assert isinstance(instance.maxAngle, int)


@given(instance=missionsDSL::Robot_strategy)
def test_missionsdsl::robot_maxAngle_setter(instance):
    original = instance.maxAngle
    instance.maxAngle = original
    assert instance.maxAngle == original
