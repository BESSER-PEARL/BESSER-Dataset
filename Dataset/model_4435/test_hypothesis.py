import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dsl_ColorValue,
    SensorType,
    dsl_ColorSensor,
    dsl_timeUnitValue,
    dsl_UltrasonicSensor,
    dsl_TouchSensor,
    dsl_Ignorables,
    dsl_SensorType,
    dsl_Task,
    dsl_Mission,
    Colors,
    TouchSensorSides,
    CompareOperator,
    timeUnit,
    Actions,
    Directions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_colorvalue_is_not_abstract():
    assert not inspect.isabstract(dsl_ColorValue)


def test_dsl_colorvalue_constructor_exists():
    assert callable(dsl_ColorValue.__init__)


def test_dsl_colorvalue_constructor_args():
    sig = inspect.signature(dsl_ColorValue.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_dsl_colorvalue_has_color():
    assert hasattr(dsl_ColorValue, "color")
    descriptor = None
    for klass in dsl_ColorValue.__mro__:
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



def test_dsl_colorsensor_is_not_abstract():
    assert not inspect.isabstract(dsl_ColorSensor)


def test_dsl_colorsensor_constructor_exists():
    assert callable(dsl_ColorSensor.__init__)


def test_dsl_colorsensor_constructor_args():
    sig = inspect.signature(dsl_ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_dsl_colorsensor_has_distinct():
    assert hasattr(dsl_ColorSensor, "distinct")
    descriptor = None
    for klass in dsl_ColorSensor.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_dsl_timeunitvalue_is_not_abstract():
    assert not inspect.isabstract(dsl_timeUnitValue)


def test_dsl_timeunitvalue_constructor_exists():
    assert callable(dsl_timeUnitValue.__init__)


def test_dsl_timeunitvalue_constructor_args():
    sig = inspect.signature(dsl_timeUnitValue.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_dsl_timeunitvalue_has_unit():
    assert hasattr(dsl_timeUnitValue, "unit")
    descriptor = None
    for klass in dsl_timeUnitValue.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_dsl_ultrasonicsensor_is_not_abstract():
    assert not inspect.isabstract(dsl_UltrasonicSensor)


def test_dsl_ultrasonicsensor_constructor_exists():
    assert callable(dsl_UltrasonicSensor.__init__)


def test_dsl_ultrasonicsensor_constructor_args():
    sig = inspect.signature(dsl_UltrasonicSensor.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_dsl_ultrasonicsensor_has_comparator():
    assert hasattr(dsl_UltrasonicSensor, "comparator")
    descriptor = None
    for klass in dsl_UltrasonicSensor.__mro__:
        if "comparator" in klass.__dict__:
            descriptor = klass.__dict__["comparator"]
            break
    assert isinstance(descriptor, property)

def test_dsl_ultrasonicsensor_has_distance():
    assert hasattr(dsl_UltrasonicSensor, "distance")
    descriptor = None
    for klass in dsl_UltrasonicSensor.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_dsl_touchsensor_is_not_abstract():
    assert not inspect.isabstract(dsl_TouchSensor)


def test_dsl_touchsensor_constructor_exists():
    assert callable(dsl_TouchSensor.__init__)


def test_dsl_touchsensor_constructor_args():
    sig = inspect.signature(dsl_TouchSensor.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_dsl_touchsensor_has_key():
    assert hasattr(dsl_TouchSensor, "key")
    descriptor = None
    for klass in dsl_TouchSensor.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_dsl_ignorables_is_not_abstract():
    assert not inspect.isabstract(dsl_Ignorables)


def test_dsl_ignorables_constructor_exists():
    assert callable(dsl_Ignorables.__init__)


def test_dsl_ignorables_constructor_args():
    sig = inspect.signature(dsl_Ignorables.__init__)
    params = list(sig.parameters.keys())
    assert "AVOID_OBJECTS" in params, "Missing parameter 'AVOID_OBJECTS'"

def test_dsl_ignorables_has_AVOID_OBJECTS():
    assert hasattr(dsl_Ignorables, "AVOID_OBJECTS")
    descriptor = None
    for klass in dsl_Ignorables.__mro__:
        if "AVOID_OBJECTS" in klass.__dict__:
            descriptor = klass.__dict__["AVOID_OBJECTS"]
            break
    assert isinstance(descriptor, property)



def test_dsl_sensortype_is_not_abstract():
    assert not inspect.isabstract(dsl_SensorType)


def test_dsl_sensortype_constructor_exists():
    assert callable(dsl_SensorType.__init__)


def test_dsl_sensortype_constructor_args():
    sig = inspect.signature(dsl_SensorType.__init__)
    params = list(sig.parameters.keys())



def test_dsl_task_is_not_abstract():
    assert not inspect.isabstract(dsl_Task)


def test_dsl_task_constructor_exists():
    assert callable(dsl_Task.__init__)


def test_dsl_task_constructor_args():
    sig = inspect.signature(dsl_Task.__init__)
    params = list(sig.parameters.keys())
    assert "nrOfTimes" in params, "Missing parameter 'nrOfTimes'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"

def test_dsl_task_has_nrOfTimes():
    assert hasattr(dsl_Task, "nrOfTimes")
    descriptor = None
    for klass in dsl_Task.__mro__:
        if "nrOfTimes" in klass.__dict__:
            descriptor = klass.__dict__["nrOfTimes"]
            break
    assert isinstance(descriptor, property)

def test_dsl_task_has_action():
    assert hasattr(dsl_Task, "action")
    descriptor = None
    for klass in dsl_Task.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_dsl_task_has_name():
    assert hasattr(dsl_Task, "name")
    descriptor = None
    for klass in dsl_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_task_has_time():
    assert hasattr(dsl_Task, "time")
    descriptor = None
    for klass in dsl_Task.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_dsl_mission_is_not_abstract():
    assert not inspect.isabstract(dsl_Mission)


def test_dsl_mission_constructor_exists():
    assert callable(dsl_Mission.__init__)


def test_dsl_mission_constructor_args():
    sig = inspect.signature(dsl_Mission.__init__)
    params = list(sig.parameters.keys())

def test_colors_exists():
    # Check that the Enumeration exists
    assert Colors is not None

def test_colors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colors]
    expected_literals = [
        "BLACK",
        "LIGHT_GRAY",
        "PINK",
        "CYAN",
        "BLUE",
        "GREEN",
        "YELLOW",
        "GRAY",
        "RED",
        "WHITE",
        "MAGENTA",
        "DARK_GRAY",
        "ORANGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colors"

def test_touchsensorsides_exists():
    # Check that the Enumeration exists
    assert TouchSensorSides is not None

def test_touchsensorsides_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchSensorSides]
    expected_literals = [
        "ANY",
        "LEFT",
        "RIGHT",
        "BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchSensorSides"

def test_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "GEQ",
        "G",
        "EQ",
        "L",
        "NEQ",
        "LEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

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

def test_actions_exists():
    # Check that the Enumeration exists
    assert Actions is not None

def test_actions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Actions]
    expected_literals = [
        "ROTATE_L",
        "ROTATE_R",
        "STOP_DRIVING",
        "MEASURE",
        "DRIVE_BACKWARD",
        "DRIVETOEDGE",
        "DRIVE_FORWARD",
        "BEEP",
        "TURN_AROUND",
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
        "S",
        "NW",
        "E",
        "SW",
        "W",
        "SE",
        "NE",
        "N",
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
dsl_ColorValue_strategy = st.builds(
    dsl_ColorValue,
    color=
        safe_text
)
SensorType_strategy = st.builds(
    SensorType,
)
dsl_ColorSensor_strategy = st.builds(
    dsl_ColorSensor,
    distinct=
        st.booleans()
)
dsl_timeUnitValue_strategy = st.builds(
    dsl_timeUnitValue,
    unit=
        safe_text
)
dsl_UltrasonicSensor_strategy = st.builds(
    dsl_UltrasonicSensor,
    comparator=
        safe_text,
    distance=
        safe_text
)
dsl_TouchSensor_strategy = st.builds(
    dsl_TouchSensor,
    key=
        safe_text
)
dsl_Ignorables_strategy = st.builds(
    dsl_Ignorables,
    AVOID_OBJECTS=
        safe_text
)
dsl_SensorType_strategy = st.builds(
    dsl_SensorType,
)
dsl_Task_strategy = st.builds(
    dsl_Task,
    nrOfTimes=
        st.integers(),
    action=
        safe_text,
    name=
        safe_text,
    time=
        st.integers()
)
dsl_Mission_strategy = st.builds(
    dsl_Mission,
)

@given(instance=dsl_ColorValue_strategy)
@settings(max_examples=50)
def test_dsl_colorvalue_instantiation(instance):
    assert isinstance(instance, dsl_ColorValue)



@given(instance=dsl_ColorValue_strategy)
def test_dsl_colorvalue_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=SensorType_strategy)
@settings(max_examples=50)
def test_sensortype_instantiation(instance):
    assert isinstance(instance, SensorType)

@given(instance=dsl_ColorSensor_strategy)
@settings(max_examples=50)
def test_dsl_colorsensor_instantiation(instance):
    assert isinstance(instance, dsl_ColorSensor)



@given(instance=dsl_ColorSensor_strategy)
def test_dsl_colorsensor_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=dsl_timeUnitValue_strategy)
@settings(max_examples=50)
def test_dsl_timeunitvalue_instantiation(instance):
    assert isinstance(instance, dsl_timeUnitValue)



@given(instance=dsl_timeUnitValue_strategy)
def test_dsl_timeunitvalue_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=dsl_UltrasonicSensor_strategy)
@settings(max_examples=50)
def test_dsl_ultrasonicsensor_instantiation(instance):
    assert isinstance(instance, dsl_UltrasonicSensor)



@given(instance=dsl_UltrasonicSensor_strategy)
def test_dsl_ultrasonicsensor_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original



@given(instance=dsl_UltrasonicSensor_strategy)
def test_dsl_ultrasonicsensor_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=dsl_TouchSensor_strategy)
@settings(max_examples=50)
def test_dsl_touchsensor_instantiation(instance):
    assert isinstance(instance, dsl_TouchSensor)



@given(instance=dsl_TouchSensor_strategy)
def test_dsl_touchsensor_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dsl_Ignorables_strategy)
@settings(max_examples=50)
def test_dsl_ignorables_instantiation(instance):
    assert isinstance(instance, dsl_Ignorables)



@given(instance=dsl_Ignorables_strategy)
def test_dsl_ignorables_AVOID_OBJECTS_setter(instance):
    original = instance.AVOID_OBJECTS
    instance.AVOID_OBJECTS = original
    assert instance.AVOID_OBJECTS == original

@given(instance=dsl_SensorType_strategy)
@settings(max_examples=50)
def test_dsl_sensortype_instantiation(instance):
    assert isinstance(instance, dsl_SensorType)

@given(instance=dsl_Task_strategy)
@settings(max_examples=50)
def test_dsl_task_instantiation(instance):
    assert isinstance(instance, dsl_Task)



@given(instance=dsl_Task_strategy)
def test_dsl_task_nrOfTimes_setter(instance):
    original = instance.nrOfTimes
    instance.nrOfTimes = original
    assert instance.nrOfTimes == original



@given(instance=dsl_Task_strategy)
def test_dsl_task_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=dsl_Task_strategy)
def test_dsl_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Task_strategy)
def test_dsl_task_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=dsl_Mission_strategy)
@settings(max_examples=50)
def test_dsl_mission_instantiation(instance):
    assert isinstance(instance, dsl_Mission)
