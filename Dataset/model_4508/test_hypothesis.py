import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smartHome_SensorValue,
    smartHome_Location,
    smartHome_Duration,
    smartHome_Event,
    smartHome_Condition,
    smartHome_Rule,
    smartHome_SmartHome,
    smartHome_SensorType,
    smartHome_Sensor,
    DurationUnit,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smarthome_sensorvalue_is_not_abstract():
    assert not inspect.isabstract(smartHome_SensorValue)


def test_smarthome_sensorvalue_constructor_exists():
    assert callable(smartHome_SensorValue.__init__)


def test_smarthome_sensorvalue_constructor_args():
    sig = inspect.signature(smartHome_SensorValue.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_location_is_not_abstract():
    assert not inspect.isabstract(smartHome_Location)


def test_smarthome_location_constructor_exists():
    assert callable(smartHome_Location.__init__)


def test_smarthome_location_constructor_args():
    sig = inspect.signature(smartHome_Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome_location_has_name():
    assert hasattr(smartHome_Location, "name")
    descriptor = None
    for klass in smartHome_Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_duration_is_not_abstract():
    assert not inspect.isabstract(smartHome_Duration)


def test_smarthome_duration_constructor_exists():
    assert callable(smartHome_Duration.__init__)


def test_smarthome_duration_constructor_args():
    sig = inspect.signature(smartHome_Duration.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome_duration_has_unit():
    assert hasattr(smartHome_Duration, "unit")
    descriptor = None
    for klass in smartHome_Duration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_duration_has_value():
    assert hasattr(smartHome_Duration, "value")
    descriptor = None
    for klass in smartHome_Duration.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_event_is_not_abstract():
    assert not inspect.isabstract(smartHome_Event)


def test_smarthome_event_constructor_exists():
    assert callable(smartHome_Event.__init__)


def test_smarthome_event_constructor_args():
    sig = inspect.signature(smartHome_Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_smarthome_event_has_description():
    assert hasattr(smartHome_Event, "description")
    descriptor = None
    for klass in smartHome_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_condition_is_not_abstract():
    assert not inspect.isabstract(smartHome_Condition)


def test_smarthome_condition_constructor_exists():
    assert callable(smartHome_Condition.__init__)


def test_smarthome_condition_constructor_args():
    sig = inspect.signature(smartHome_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operand" in params, "Missing parameter 'operand'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome_condition_has_operand():
    assert hasattr(smartHome_Condition, "operand")
    descriptor = None
    for klass in smartHome_Condition.__mro__:
        if "operand" in klass.__dict__:
            descriptor = klass.__dict__["operand"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_condition_has_operator():
    assert hasattr(smartHome_Condition, "operator")
    descriptor = None
    for klass in smartHome_Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_rule_is_not_abstract():
    assert not inspect.isabstract(smartHome_Rule)


def test_smarthome_rule_constructor_exists():
    assert callable(smartHome_Rule.__init__)


def test_smarthome_rule_constructor_args():
    sig = inspect.signature(smartHome_Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_smarthome_is_not_abstract():
    assert not inspect.isabstract(smartHome_SmartHome)


def test_smarthome_smarthome_constructor_exists():
    assert callable(smartHome_SmartHome.__init__)


def test_smarthome_smarthome_constructor_args():
    sig = inspect.signature(smartHome_SmartHome.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_sensortype_is_not_abstract():
    assert not inspect.isabstract(smartHome_SensorType)


def test_smarthome_sensortype_constructor_exists():
    assert callable(smartHome_SensorType.__init__)


def test_smarthome_sensortype_constructor_args():
    sig = inspect.signature(smartHome_SensorType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome_sensortype_has_name():
    assert hasattr(smartHome_SensorType, "name")
    descriptor = None
    for klass in smartHome_SensorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_sensor_is_not_abstract():
    assert not inspect.isabstract(smartHome_Sensor)


def test_smarthome_sensor_constructor_exists():
    assert callable(smartHome_Sensor.__init__)


def test_smarthome_sensor_constructor_args():
    sig = inspect.signature(smartHome_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dataFile" in params, "Missing parameter 'dataFile'"

def test_smarthome_sensor_has_value():
    assert hasattr(smartHome_Sensor, "value")
    descriptor = None
    for klass in smartHome_Sensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_sensor_has_name():
    assert hasattr(smartHome_Sensor, "name")
    descriptor = None
    for klass in smartHome_Sensor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_sensor_has_dataFile():
    assert hasattr(smartHome_Sensor, "dataFile")
    descriptor = None
    for klass in smartHome_Sensor.__mro__:
        if "dataFile" in klass.__dict__:
            descriptor = klass.__dict__["dataFile"]
            break
    assert isinstance(descriptor, property)

def test_durationunit_exists():
    # Check that the Enumeration exists
    assert DurationUnit is not None

def test_durationunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationUnit]
    expected_literals = [
        "MINUTE",
        "SECOND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationUnit"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "SUPERIOR",
        "INFERIOR",
        "EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
smartHome_SensorValue_strategy = st.builds(
    smartHome_SensorValue,
)
smartHome_Location_strategy = st.builds(
    smartHome_Location,
    name=
        safe_text
)
smartHome_Duration_strategy = st.builds(
    smartHome_Duration,
    unit=
        safe_text,
    value=
        st.integers()
)
smartHome_Event_strategy = st.builds(
    smartHome_Event,
    description=
        safe_text
)
smartHome_Condition_strategy = st.builds(
    smartHome_Condition,
    operand=
        st.integers(),
    operator=
        safe_text
)
smartHome_Rule_strategy = st.builds(
    smartHome_Rule,
)
smartHome_SmartHome_strategy = st.builds(
    smartHome_SmartHome,
)
smartHome_SensorType_strategy = st.builds(
    smartHome_SensorType,
    name=
        safe_text
)
smartHome_Sensor_strategy = st.builds(
    smartHome_Sensor,
    value=
        st.integers(),
    name=
        safe_text,
    dataFile=
        safe_text
)

@given(instance=smartHome_SensorValue_strategy)
@settings(max_examples=50)
def test_smarthome_sensorvalue_instantiation(instance):
    assert isinstance(instance, smartHome_SensorValue)

@given(instance=smartHome_Location_strategy)
@settings(max_examples=50)
def test_smarthome_location_instantiation(instance):
    assert isinstance(instance, smartHome_Location)



@given(instance=smartHome_Location_strategy)
def test_smarthome_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome_Duration_strategy)
@settings(max_examples=50)
def test_smarthome_duration_instantiation(instance):
    assert isinstance(instance, smartHome_Duration)



@given(instance=smartHome_Duration_strategy)
def test_smarthome_duration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=smartHome_Duration_strategy)
def test_smarthome_duration_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smartHome_Event_strategy)
@settings(max_examples=50)
def test_smarthome_event_instantiation(instance):
    assert isinstance(instance, smartHome_Event)



@given(instance=smartHome_Event_strategy)
def test_smarthome_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=smartHome_Condition_strategy)
@settings(max_examples=50)
def test_smarthome_condition_instantiation(instance):
    assert isinstance(instance, smartHome_Condition)



@given(instance=smartHome_Condition_strategy)
def test_smarthome_condition_operand_setter(instance):
    original = instance.operand
    instance.operand = original
    assert instance.operand == original



@given(instance=smartHome_Condition_strategy)
def test_smarthome_condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=smartHome_Rule_strategy)
@settings(max_examples=50)
def test_smarthome_rule_instantiation(instance):
    assert isinstance(instance, smartHome_Rule)

@given(instance=smartHome_SmartHome_strategy)
@settings(max_examples=50)
def test_smarthome_smarthome_instantiation(instance):
    assert isinstance(instance, smartHome_SmartHome)

@given(instance=smartHome_SensorType_strategy)
@settings(max_examples=50)
def test_smarthome_sensortype_instantiation(instance):
    assert isinstance(instance, smartHome_SensorType)



@given(instance=smartHome_SensorType_strategy)
def test_smarthome_sensortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome_Sensor_strategy)
@settings(max_examples=50)
def test_smarthome_sensor_instantiation(instance):
    assert isinstance(instance, smartHome_Sensor)



@given(instance=smartHome_Sensor_strategy)
def test_smarthome_sensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smartHome_Sensor_strategy)
def test_smarthome_sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smartHome_Sensor_strategy)
def test_smarthome_sensor_dataFile_setter(instance):
    original = instance.dataFile
    instance.dataFile = original
    assert instance.dataFile == original
