import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::ColorValue,
    SensorType,
    dsl::ColorSensor,
    dsl::timeUnitValue,
    dsl::UltrasonicSensor,
    dsl::TouchSensor,
    dsl::Ignorables,
    dsl::SensorType,
    dsl::Task,
    dsl::Mission,
    TouchSensorSides,
    timeUnit,
    Colors,
    CompareOperator,
    Actions,
    Directions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::colorvalue_is_not_abstract():
    assert not inspect.isabstract(dsl::ColorValue)


def test_dsl::colorvalue_constructor_exists():
    assert callable(dsl::ColorValue.__init__)


def test_dsl::colorvalue_constructor_args():
    sig = inspect.signature(dsl::ColorValue.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_dsl::colorvalue_has_color():
    assert hasattr(dsl::ColorValue, "color")
    descriptor = None
    for klass in dsl::ColorValue.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_sensortype_is_not_abstract():
    assert not inspect.isabstract(SensorType)


def test_sensortype_constructor_exists():
    assert callable(SensorType.__init__)


def test_sensortype_constructor_args():
    sig = inspect.signature(SensorType.__init__)
    params = list(sig.parameters.keys())



def test_dsl::colorsensor_is_not_abstract():
    assert not inspect.isabstract(dsl::ColorSensor)


def test_dsl::colorsensor_constructor_exists():
    assert callable(dsl::ColorSensor.__init__)


def test_dsl::colorsensor_constructor_args():
    sig = inspect.signature(dsl::ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_dsl::colorsensor_has_distinct():
    assert hasattr(dsl::ColorSensor, "distinct")
    descriptor = None
    for klass in dsl::ColorSensor.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_dsl::timeunitvalue_is_not_abstract():
    assert not inspect.isabstract(dsl::timeUnitValue)


def test_dsl::timeunitvalue_constructor_exists():
    assert callable(dsl::timeUnitValue.__init__)


def test_dsl::timeunitvalue_constructor_args():
    sig = inspect.signature(dsl::timeUnitValue.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_dsl::timeunitvalue_has_unit():
    assert hasattr(dsl::timeUnitValue, "unit")
    descriptor = None
    for klass in dsl::timeUnitValue.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



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
    assert "time" in params, "Missing parameter 'time'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nrOfTimes" in params, "Missing parameter 'nrOfTimes'"

def test_dsl::task_has_time():
    assert hasattr(dsl::Task, "time")
    descriptor = None
    for klass in dsl::Task.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

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

def test_dsl::task_has_nrOfTimes():
    assert hasattr(dsl::Task, "nrOfTimes")
    descriptor = None
    for klass in dsl::Task.__mro__:
        if "nrOfTimes" in klass.__dict__:
            descriptor = klass.__dict__["nrOfTimes"]
            break
    assert isinstance(descriptor, property)



def test_dsl::mission_is_not_abstract():
    assert not inspect.isabstract(dsl::Mission)


def test_dsl::mission_constructor_exists():
    assert callable(dsl::Mission.__init__)


def test_dsl::mission_constructor_args():
    sig = inspect.signature(dsl::Mission.__init__)
    params = list(sig.parameters.keys())

def test_touchsensorsides_exists():
    # Check that the Enumeration exists
    assert TouchSensorSides is not None

def test_touchsensorsides_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchSensorSides]
    expected_literals = [
        "BOTH",
        "RIGHT",
        "ANY",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchSensorSides"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert timeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in timeUnit]
    expected_literals = [
        "SECONDS",
        "MILISECONDS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in timeUnit"

def test_colors_exists():
    # Check that the Enumeration exists
    assert Colors is not None

def test_colors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colors]
    expected_literals = [
        "LIGHT_GRAY",
        "GRAY",
        "ORANGE",
        "PINK",
        "GREEN",
        "BLUE",
        "BLACK",
        "MAGENTA",
        "CYAN",
        "YELLOW",
        "WHITE",
        "RED",
        "DARK_GRAY",
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
        "NEQ",
        "LEQ",
        "G",
        "GEQ",
        "L",
        "EQ",
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
        "BEEP",
        "ROTATE_L",
        "ROTATE_R",
        "MEASURE",
        "STOP_DRIVING",
        "TURN_AROUND",
        "DRIVE_FORWARD",
        "DRIVE_BACKWARD",
        "DRIVETOEDGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Actions"

def test_directions_exists():
    # Check that the Enumeration exists
    assert Directions is not None

def test_directions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Directions]
    expected_literals = [
        "E",
        "NE",
        "SE",
        "SW",
        "S",
        "NW",
        "N",
        "W",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Directions"


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
dsl::ColorValue_strategy = st.builds(
    dsl::ColorValue,
    color=
        safe_text
)
SensorType_strategy = st.builds(
    SensorType,
)
dsl::ColorSensor_strategy = st.builds(
    dsl::ColorSensor,
    distinct=
        st.booleans()
)
dsl::timeUnitValue_strategy = st.builds(
    dsl::timeUnitValue,
    unit=
        safe_text
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
    time=
        st.integers(),
    action=
        safe_text,
    name=
        safe_text,
    nrOfTimes=
        st.integers()
)
dsl::Mission_strategy = st.builds(
    dsl::Mission,
)

@given(instance=dsl::ColorValue_strategy)
@settings(max_examples=50)
def test_dsl::colorvalue_instantiation(instance):
    assert isinstance(instance, dsl::ColorValue)

@given(instance=dsl::ColorValue_strategy)
def test_dsl::colorvalue_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=dsl::ColorValue_strategy)
def test_dsl::colorvalue_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=SensorType_strategy)
@settings(max_examples=50)
def test_sensortype_instantiation(instance):
    assert isinstance(instance, SensorType)

@given(instance=dsl::ColorSensor_strategy)
@settings(max_examples=50)
def test_dsl::colorsensor_instantiation(instance):
    assert isinstance(instance, dsl::ColorSensor)

@given(instance=dsl::ColorSensor_strategy)
def test_dsl::colorsensor_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=dsl::ColorSensor_strategy)
def test_dsl::colorsensor_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=dsl::timeUnitValue_strategy)
@settings(max_examples=50)
def test_dsl::timeunitvalue_instantiation(instance):
    assert isinstance(instance, dsl::timeUnitValue)

@given(instance=dsl::timeUnitValue_strategy)
def test_dsl::timeunitvalue_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=dsl::timeUnitValue_strategy)
def test_dsl::timeunitvalue_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

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
def test_dsl::task_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=dsl::Task_strategy)
def test_dsl::task_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

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
def test_dsl::task_nrOfTimes_type(instance):
    assert isinstance(instance.nrOfTimes, int)


@given(instance=dsl::Task_strategy)
def test_dsl::task_nrOfTimes_setter(instance):
    original = instance.nrOfTimes
    instance.nrOfTimes = original
    assert instance.nrOfTimes == original

@given(instance=dsl::Mission_strategy)
@settings(max_examples=50)
def test_dsl::mission_instantiation(instance):
    assert isinstance(instance, dsl::Mission)
