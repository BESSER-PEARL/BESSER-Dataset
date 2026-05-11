import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smartHome::SensorValue,
    smartHome::Location,
    smartHome::Duration,
    smartHome::Event,
    smartHome::Condition,
    smartHome::Rule,
    smartHome::SmartHome,
    smartHome::SensorType,
    smartHome::Sensor,
    Operator,
    DurationUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smarthome::sensorvalue_is_not_abstract():
    assert not inspect.isabstract(smartHome::SensorValue)


def test_smarthome::sensorvalue_constructor_exists():
    assert callable(smartHome::SensorValue.__init__)


def test_smarthome::sensorvalue_constructor_args():
    sig = inspect.signature(smartHome::SensorValue.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::location_is_not_abstract():
    assert not inspect.isabstract(smartHome::Location)


def test_smarthome::location_constructor_exists():
    assert callable(smartHome::Location.__init__)


def test_smarthome::location_constructor_args():
    sig = inspect.signature(smartHome::Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome::location_has_name():
    assert hasattr(smartHome::Location, "name")
    descriptor = None
    for klass in smartHome::Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::duration_is_not_abstract():
    assert not inspect.isabstract(smartHome::Duration)


def test_smarthome::duration_constructor_exists():
    assert callable(smartHome::Duration.__init__)


def test_smarthome::duration_constructor_args():
    sig = inspect.signature(smartHome::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_smarthome::duration_has_value():
    assert hasattr(smartHome::Duration, "value")
    descriptor = None
    for klass in smartHome::Duration.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::duration_has_unit():
    assert hasattr(smartHome::Duration, "unit")
    descriptor = None
    for klass in smartHome::Duration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::event_is_not_abstract():
    assert not inspect.isabstract(smartHome::Event)


def test_smarthome::event_constructor_exists():
    assert callable(smartHome::Event.__init__)


def test_smarthome::event_constructor_args():
    sig = inspect.signature(smartHome::Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_smarthome::event_has_description():
    assert hasattr(smartHome::Event, "description")
    descriptor = None
    for klass in smartHome::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::condition_is_not_abstract():
    assert not inspect.isabstract(smartHome::Condition)


def test_smarthome::condition_constructor_exists():
    assert callable(smartHome::Condition.__init__)


def test_smarthome::condition_constructor_args():
    sig = inspect.signature(smartHome::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operand" in params, "Missing parameter 'operand'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome::condition_has_operand():
    assert hasattr(smartHome::Condition, "operand")
    descriptor = None
    for klass in smartHome::Condition.__mro__:
        if "operand" in klass.__dict__:
            descriptor = klass.__dict__["operand"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::condition_has_operator():
    assert hasattr(smartHome::Condition, "operator")
    descriptor = None
    for klass in smartHome::Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::rule_is_not_abstract():
    assert not inspect.isabstract(smartHome::Rule)


def test_smarthome::rule_constructor_exists():
    assert callable(smartHome::Rule.__init__)


def test_smarthome::rule_constructor_args():
    sig = inspect.signature(smartHome::Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::smarthome_is_not_abstract():
    assert not inspect.isabstract(smartHome::SmartHome)


def test_smarthome::smarthome_constructor_exists():
    assert callable(smartHome::SmartHome.__init__)


def test_smarthome::smarthome_constructor_args():
    sig = inspect.signature(smartHome::SmartHome.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::sensortype_is_not_abstract():
    assert not inspect.isabstract(smartHome::SensorType)


def test_smarthome::sensortype_constructor_exists():
    assert callable(smartHome::SensorType.__init__)


def test_smarthome::sensortype_constructor_args():
    sig = inspect.signature(smartHome::SensorType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome::sensortype_has_name():
    assert hasattr(smartHome::SensorType, "name")
    descriptor = None
    for klass in smartHome::SensorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::sensor_is_not_abstract():
    assert not inspect.isabstract(smartHome::Sensor)


def test_smarthome::sensor_constructor_exists():
    assert callable(smartHome::Sensor.__init__)


def test_smarthome::sensor_constructor_args():
    sig = inspect.signature(smartHome::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataFile" in params, "Missing parameter 'dataFile'"
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome::sensor_has_name():
    assert hasattr(smartHome::Sensor, "name")
    descriptor = None
    for klass in smartHome::Sensor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::sensor_has_dataFile():
    assert hasattr(smartHome::Sensor, "dataFile")
    descriptor = None
    for klass in smartHome::Sensor.__mro__:
        if "dataFile" in klass.__dict__:
            descriptor = klass.__dict__["dataFile"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::sensor_has_value():
    assert hasattr(smartHome::Sensor, "value")
    descriptor = None
    for klass in smartHome::Sensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "INFERIOR",
        "EQUALS",
        "SUPERIOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_durationunit_exists():
    # Check that the Enumeration exists
    assert DurationUnit is not None

def test_durationunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationUnit]
    expected_literals = [
        "SECOND",
        "MINUTE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationUnit"


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
smartHome::SensorValue_strategy = st.builds(
    smartHome::SensorValue,
)
smartHome::Location_strategy = st.builds(
    smartHome::Location,
    name=
        safe_text
)
smartHome::Duration_strategy = st.builds(
    smartHome::Duration,
    value=
        st.integers(),
    unit=
        safe_text
)
smartHome::Event_strategy = st.builds(
    smartHome::Event,
    description=
        safe_text
)
smartHome::Condition_strategy = st.builds(
    smartHome::Condition,
    operand=
        st.integers(),
    operator=
        safe_text
)
smartHome::Rule_strategy = st.builds(
    smartHome::Rule,
)
smartHome::SmartHome_strategy = st.builds(
    smartHome::SmartHome,
)
smartHome::SensorType_strategy = st.builds(
    smartHome::SensorType,
    name=
        safe_text
)
smartHome::Sensor_strategy = st.builds(
    smartHome::Sensor,
    name=
        safe_text,
    dataFile=
        safe_text,
    value=
        st.integers()
)

@given(instance=smartHome::SensorValue_strategy)
@settings(max_examples=50)
def test_smarthome::sensorvalue_instantiation(instance):
    assert isinstance(instance, smartHome::SensorValue)

@given(instance=smartHome::Location_strategy)
@settings(max_examples=50)
def test_smarthome::location_instantiation(instance):
    assert isinstance(instance, smartHome::Location)

@given(instance=smartHome::Location_strategy)
def test_smarthome::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smartHome::Location_strategy)
def test_smarthome::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome::Duration_strategy)
@settings(max_examples=50)
def test_smarthome::duration_instantiation(instance):
    assert isinstance(instance, smartHome::Duration)

@given(instance=smartHome::Duration_strategy)
def test_smarthome::duration_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=smartHome::Duration_strategy)
def test_smarthome::duration_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smartHome::Duration_strategy)
def test_smarthome::duration_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=smartHome::Duration_strategy)
def test_smarthome::duration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=smartHome::Event_strategy)
@settings(max_examples=50)
def test_smarthome::event_instantiation(instance):
    assert isinstance(instance, smartHome::Event)

@given(instance=smartHome::Event_strategy)
def test_smarthome::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=smartHome::Event_strategy)
def test_smarthome::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=smartHome::Condition_strategy)
@settings(max_examples=50)
def test_smarthome::condition_instantiation(instance):
    assert isinstance(instance, smartHome::Condition)

@given(instance=smartHome::Condition_strategy)
def test_smarthome::condition_operand_type(instance):
    assert isinstance(instance.operand, int)


@given(instance=smartHome::Condition_strategy)
def test_smarthome::condition_operand_setter(instance):
    original = instance.operand
    instance.operand = original
    assert instance.operand == original

@given(instance=smartHome::Condition_strategy)
def test_smarthome::condition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=smartHome::Condition_strategy)
def test_smarthome::condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=smartHome::Rule_strategy)
@settings(max_examples=50)
def test_smarthome::rule_instantiation(instance):
    assert isinstance(instance, smartHome::Rule)

@given(instance=smartHome::SmartHome_strategy)
@settings(max_examples=50)
def test_smarthome::smarthome_instantiation(instance):
    assert isinstance(instance, smartHome::SmartHome)

@given(instance=smartHome::SensorType_strategy)
@settings(max_examples=50)
def test_smarthome::sensortype_instantiation(instance):
    assert isinstance(instance, smartHome::SensorType)

@given(instance=smartHome::SensorType_strategy)
def test_smarthome::sensortype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smartHome::SensorType_strategy)
def test_smarthome::sensortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome::Sensor_strategy)
@settings(max_examples=50)
def test_smarthome::sensor_instantiation(instance):
    assert isinstance(instance, smartHome::Sensor)

@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_dataFile_type(instance):
    assert isinstance(instance.dataFile, str)


@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_dataFile_setter(instance):
    original = instance.dataFile
    instance.dataFile = original
    assert instance.dataFile == original

@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=smartHome::Sensor_strategy)
def test_smarthome::sensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
