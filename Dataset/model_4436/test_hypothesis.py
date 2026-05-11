import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SensorType,
    dsl::UltrasonicSensor,
    dsl::TouchSensor,
    dsl::ColorSensor,
    dsl::Ignorables,
    dsl::SensorType,
    dsl::Task,
    dsl::Mission,
    Directions,
    Colors,
    CompareOperator,
    Actions,
    TouchSensorSides,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sensortype_is_not_abstract():
    assert not inspect.isabstract(SensorType)


def test_sensortype_constructor_exists():
    assert callable(SensorType.__init__)


def test_sensortype_constructor_args():
    sig = inspect.signature(SensorType.__init__)
    params = list(sig.parameters.keys())



def test_dsl::ultrasonicsensor_is_not_abstract():
    assert not inspect.isabstract(dsl::UltrasonicSensor)


def test_dsl::ultrasonicsensor_constructor_exists():
    assert callable(dsl::UltrasonicSensor.__init__)


def test_dsl::ultrasonicsensor_constructor_args():
    sig = inspect.signature(dsl::UltrasonicSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "comparator" in params, "Missing parameter 'comparator'"

def test_dsl::ultrasonicsensor_has_distance():
    assert hasattr(dsl::UltrasonicSensor, "distance")
    descriptor = None
    for klass in dsl::UltrasonicSensor.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)

def test_dsl::ultrasonicsensor_has_comparator():
    assert hasattr(dsl::UltrasonicSensor, "comparator")
    descriptor = None
    for klass in dsl::UltrasonicSensor.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)



def test_dsl::touchsensor_is_not_abstract():
    assert not inspect.isabstract(dsl::TouchSensor)


def test_dsl::touchsensor_constructor_exists():
    assert callable(dsl::TouchSensor.__init__)


def test_dsl::touchsensor_constructor_args():
    sig = inspect.signature(dsl::TouchSensor.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_dsl::touchsensor_has_key():
    assert hasattr(dsl::TouchSensor, "key")
    descriptor = None
    for klass in dsl::TouchSensor.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_dsl::colorsensor_is_not_abstract():
    assert not inspect.isabstract(dsl::ColorSensor)


def test_dsl::colorsensor_constructor_exists():
    assert callable(dsl::ColorSensor.__init__)


def test_dsl::colorsensor_constructor_args():
    sig = inspect.signature(dsl::ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_dsl::colorsensor_has_key():
    assert hasattr(dsl::ColorSensor, "key")
    descriptor = None
    for klass in dsl::ColorSensor.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_dsl::ignorables_is_not_abstract():
    assert not inspect.isabstract(dsl::Ignorables)


def test_dsl::ignorables_constructor_exists():
    assert callable(dsl::Ignorables.__init__)


def test_dsl::ignorables_constructor_args():
    sig = inspect.signature(dsl::Ignorables.__init__)
    params = list(sig.parameters.keys())
    assert "AVOID_OBJECTS" in params, "Missing parameter 'AVOID_OBJECTS'"

def test_dsl::ignorables_has_AVOID_OBJECTS():
    assert hasattr(dsl::Ignorables, "AVOID_OBJECTS")
    descriptor = None
    for klass in dsl::Ignorables.__mro__:
        if "AVOID_OBJECTS" in klass.__dict__:
            descriptor = klass.__dict__["AVOID_OBJECTS"]
            break
    assert isinstance(descriptor, property)



def test_dsl::sensortype_is_not_abstract():
    assert not inspect.isabstract(dsl::SensorType)


def test_dsl::sensortype_constructor_exists():
    assert callable(dsl::SensorType.__init__)


def test_dsl::sensortype_constructor_args():
    sig = inspect.signature(dsl::SensorType.__init__)
    params = list(sig.parameters.keys())



def test_dsl::task_is_not_abstract():
    assert not inspect.isabstract(dsl::Task)


def test_dsl::task_constructor_exists():
    assert callable(dsl::Task.__init__)


def test_dsl::task_constructor_args():
    sig = inspect.signature(dsl::Task.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ignoreBehavior" in params, "Missing parameter 'ignoreBehavior'"

def test_dsl::task_has_action():
    assert hasattr(dsl::Task, "action")
    descriptor = None
    for klass in dsl::Task.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_dsl::task_has_name():
    assert hasattr(dsl::Task, "name")
    descriptor = None
    for klass in dsl::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::task_has_ignoreBehavior():
    assert hasattr(dsl::Task, "ignoreBehavior")
    descriptor = None
    for klass in dsl::Task.__mro__:
        if "ignoreBehavior" in klass.__dict__:
            descriptor = klass.__dict__["ignoreBehavior"]
            break
    assert isinstance(descriptor, property)



def test_dsl::mission_is_not_abstract():
    assert not inspect.isabstract(dsl::Mission)


def test_dsl::mission_constructor_exists():
    assert callable(dsl::Mission.__init__)


def test_dsl::mission_constructor_args():
    sig = inspect.signature(dsl::Mission.__init__)
    params = list(sig.parameters.keys())

def test_directions_exists():
    # Check that the Enumeration exists
    assert Directions is not None

def test_directions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Directions]
    expected_literals = [
        "N",
        "NE",
        "S",
        "SE",
        "NW",
        "SW",
        "E",
        "W",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Directions"

def test_colors_exists():
    # Check that the Enumeration exists
    assert Colors is not None

def test_colors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colors]
    expected_literals = [
        "LIGHT_GRAY",
        "RED",
        "CYAN",
        "WHITE",
        "BLACK",
        "GRAY",
        "PINK",
        "ORANGE",
        "GREEN",
        "BLUE",
        "MAGENTA",
        "DARK_GRAY",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colors"

def test_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "EQ",
        "L",
        "LEQ",
        "G",
        "GEQ",
        "NEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

def test_actions_exists():
    # Check that the Enumeration exists
    assert Actions is not None

def test_actions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Actions]
    expected_literals = [
        "ROTATE_R",
        "STOP_DRIVING",
        "DRIVETOEDGE",
        "TURN_AROUND",
        "BEEP",
        "DRIVE_FORWARD",
        "DRIVE_BACKWARD",
        "ROTATE_L",
        "MEASURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Actions"

def test_touchsensorsides_exists():
    # Check that the Enumeration exists
    assert TouchSensorSides is not None

def test_touchsensorsides_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchSensorSides]
    expected_literals = [
        "BOTH",
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchSensorSides"


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
SensorType_strategy = st.builds(
    SensorType,
)
dsl::UltrasonicSensor_strategy = st.builds(
    dsl::UltrasonicSensor,
    distance=
        safe_text,
    comparator=
        safe_text
)
dsl::TouchSensor_strategy = st.builds(
    dsl::TouchSensor,
    key=
        safe_text
)
dsl::ColorSensor_strategy = st.builds(
    dsl::ColorSensor,
    key=
        safe_text
)
dsl::Ignorables_strategy = st.builds(
    dsl::Ignorables,
    AVOID_OBJECTS=
        safe_text
)
dsl::SensorType_strategy = st.builds(
    dsl::SensorType,
)
dsl::Task_strategy = st.builds(
    dsl::Task,
    action=
        safe_text,
    name=
        safe_text,
    ignoreBehavior=
        st.booleans()
)
dsl::Mission_strategy = st.builds(
    dsl::Mission,
)

@given(instance=SensorType_strategy)
@settings(max_examples=50)
def test_sensortype_instantiation(instance):
    assert isinstance(instance, SensorType)

@given(instance=dsl::UltrasonicSensor_strategy)
@settings(max_examples=50)
def test_dsl::ultrasonicsensor_instantiation(instance):
    assert isinstance(instance, dsl::UltrasonicSensor)

@given(instance=dsl::UltrasonicSensor_strategy)
def test_dsl::ultrasonicsensor_distance_type(instance):
    assert isinstance(instance.distance, str)


@given(instance=dsl::UltrasonicSensor_strategy)
def test_dsl::ultrasonicsensor_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=dsl::UltrasonicSensor_strategy)
def test_dsl::ultrasonicsensor_comparator_type(instance):
    assert isinstance(instance.comparator, str)


@given(instance=dsl::UltrasonicSensor_strategy)
def test_dsl::ultrasonicsensor_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original

@given(instance=dsl::TouchSensor_strategy)
@settings(max_examples=50)
def test_dsl::touchsensor_instantiation(instance):
    assert isinstance(instance, dsl::TouchSensor)

@given(instance=dsl::TouchSensor_strategy)
def test_dsl::touchsensor_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dsl::TouchSensor_strategy)
def test_dsl::touchsensor_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dsl::ColorSensor_strategy)
@settings(max_examples=50)
def test_dsl::colorsensor_instantiation(instance):
    assert isinstance(instance, dsl::ColorSensor)

@given(instance=dsl::ColorSensor_strategy)
def test_dsl::colorsensor_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dsl::ColorSensor_strategy)
def test_dsl::colorsensor_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dsl::Ignorables_strategy)
@settings(max_examples=50)
def test_dsl::ignorables_instantiation(instance):
    assert isinstance(instance, dsl::Ignorables)

@given(instance=dsl::Ignorables_strategy)
def test_dsl::ignorables_AVOID_OBJECTS_type(instance):
    assert isinstance(instance.AVOID_OBJECTS, str)


@given(instance=dsl::Ignorables_strategy)
def test_dsl::ignorables_AVOID_OBJECTS_setter(instance):
    original = instance.AVOID_OBJECTS
    instance.AVOID_OBJECTS = original
    assert instance.AVOID_OBJECTS == original

@given(instance=dsl::SensorType_strategy)
@settings(max_examples=50)
def test_dsl::sensortype_instantiation(instance):
    assert isinstance(instance, dsl::SensorType)

@given(instance=dsl::Task_strategy)
@settings(max_examples=50)
def test_dsl::task_instantiation(instance):
    assert isinstance(instance, dsl::Task)

@given(instance=dsl::Task_strategy)
def test_dsl::task_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=dsl::Task_strategy)
def test_dsl::task_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=dsl::Task_strategy)
def test_dsl::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Task_strategy)
def test_dsl::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Task_strategy)
def test_dsl::task_ignoreBehavior_type(instance):
    assert isinstance(instance.ignoreBehavior, bool)


@given(instance=dsl::Task_strategy)
def test_dsl::task_ignoreBehavior_setter(instance):
    original = instance.ignoreBehavior
    instance.ignoreBehavior = original
    assert instance.ignoreBehavior == original

@given(instance=dsl::Mission_strategy)
@settings(max_examples=50)
def test_dsl::mission_instantiation(instance):
    assert isinstance(instance, dsl::Mission)
