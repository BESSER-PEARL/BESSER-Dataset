import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Condition,
    smartHome_IntegerCondition,
    smartHome_BooleanCondition,
    smartHome_Rule,
    smartHome_SmartHome,
    SensorType,
    smartHome_BooleanSensorType,
    smartHome_AnalogSensorType,
    smartHome_Location,
    Sensor,
    smartHome_BooleanSensor,
    smartHome_IntegerSensor,
    smartHome_SensorType,
    smartHome_Sensor,
    smartHome_Duration,
    smartHome_Event,
    smartHome_Condition,
    BooleanOperator,
    DurationUnit,
    IntegerOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_integercondition_is_not_abstract():
    assert not inspect.isabstract(smartHome_IntegerCondition)


def test_smarthome_integercondition_constructor_exists():
    assert callable(smartHome_IntegerCondition.__init__)


def test_smarthome_integercondition_constructor_args():
    sig = inspect.signature(smartHome_IntegerCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operand" in params, "Missing parameter 'operand'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome_integercondition_has_operand():
    assert hasattr(smartHome_IntegerCondition, "operand")
    descriptor = None
    for klass in smartHome_IntegerCondition.__mro__:
        if "operand" in klass.__dict__:
            descriptor = klass.__dict__["operand"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_integercondition_has_operator():
    assert hasattr(smartHome_IntegerCondition, "operator")
    descriptor = None
    for klass in smartHome_IntegerCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_booleancondition_is_not_abstract():
    assert not inspect.isabstract(smartHome_BooleanCondition)


def test_smarthome_booleancondition_constructor_exists():
    assert callable(smartHome_BooleanCondition.__init__)


def test_smarthome_booleancondition_constructor_args():
    sig = inspect.signature(smartHome_BooleanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "operand" in params, "Missing parameter 'operand'"

def test_smarthome_booleancondition_has_operator():
    assert hasattr(smartHome_BooleanCondition, "operator")
    descriptor = None
    for klass in smartHome_BooleanCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_booleancondition_has_operand():
    assert hasattr(smartHome_BooleanCondition, "operand")
    descriptor = None
    for klass in smartHome_BooleanCondition.__mro__:
        if "operand" in klass.__dict__:
            descriptor = klass.__dict__["operand"]
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



def test_sensortype_is_not_abstract():
    assert not inspect.isabstract(SensorType)


def test_sensortype_constructor_exists():
    assert callable(SensorType.__init__)


def test_sensortype_constructor_args():
    sig = inspect.signature(SensorType.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_booleansensortype_is_not_abstract():
    assert not inspect.isabstract(smartHome_BooleanSensorType)


def test_smarthome_booleansensortype_constructor_exists():
    assert callable(smartHome_BooleanSensorType.__init__)


def test_smarthome_booleansensortype_constructor_args():
    sig = inspect.signature(smartHome_BooleanSensorType.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_analogsensortype_is_not_abstract():
    assert not inspect.isabstract(smartHome_AnalogSensorType)


def test_smarthome_analogsensortype_constructor_exists():
    assert callable(smartHome_AnalogSensorType.__init__)


def test_smarthome_analogsensortype_constructor_args():
    sig = inspect.signature(smartHome_AnalogSensorType.__init__)
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



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_booleansensor_is_not_abstract():
    assert not inspect.isabstract(smartHome_BooleanSensor)


def test_smarthome_booleansensor_constructor_exists():
    assert callable(smartHome_BooleanSensor.__init__)


def test_smarthome_booleansensor_constructor_args():
    sig = inspect.signature(smartHome_BooleanSensor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome_booleansensor_has_value():
    assert hasattr(smartHome_BooleanSensor, "value")
    descriptor = None
    for klass in smartHome_BooleanSensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_integersensor_is_not_abstract():
    assert not inspect.isabstract(smartHome_IntegerSensor)


def test_smarthome_integersensor_constructor_exists():
    assert callable(smartHome_IntegerSensor.__init__)


def test_smarthome_integersensor_constructor_args():
    sig = inspect.signature(smartHome_IntegerSensor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome_integersensor_has_value():
    assert hasattr(smartHome_IntegerSensor, "value")
    descriptor = None
    for klass in smartHome_IntegerSensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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
    assert "dataFile" in params, "Missing parameter 'dataFile'"
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome_sensor_has_dataFile():
    assert hasattr(smartHome_Sensor, "dataFile")
    descriptor = None
    for klass in smartHome_Sensor.__mro__:
        if "dataFile" in klass.__dict__:
            descriptor = klass.__dict__["dataFile"]
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



def test_smarthome_duration_is_not_abstract():
    assert not inspect.isabstract(smartHome_Duration)


def test_smarthome_duration_constructor_exists():
    assert callable(smartHome_Duration.__init__)


def test_smarthome_duration_constructor_args():
    sig = inspect.signature(smartHome_Duration.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_smarthome_duration_has_value():
    assert hasattr(smartHome_Duration, "value")
    descriptor = None
    for klass in smartHome_Duration.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_duration_has_unit():
    assert hasattr(smartHome_Duration, "unit")
    descriptor = None
    for klass in smartHome_Duration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
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

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "IS",
        "IS_NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

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

def test_integeroperator_exists():
    # Check that the Enumeration exists
    assert IntegerOperator is not None

def test_integeroperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerOperator]
    expected_literals = [
        "EQUALS",
        "INFERIOR",
        "SUPERIOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerOperator"


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
Condition_strategy = st.builds(
    Condition,
)
smartHome_IntegerCondition_strategy = st.builds(
    smartHome_IntegerCondition,
    operand=
        st.integers(),
    operator=
        safe_text
)
smartHome_BooleanCondition_strategy = st.builds(
    smartHome_BooleanCondition,
    operator=
        safe_text,
    operand=
        st.booleans()
)
smartHome_Rule_strategy = st.builds(
    smartHome_Rule,
)
smartHome_SmartHome_strategy = st.builds(
    smartHome_SmartHome,
)
SensorType_strategy = st.builds(
    SensorType,
)
smartHome_BooleanSensorType_strategy = st.builds(
    smartHome_BooleanSensorType,
)
smartHome_AnalogSensorType_strategy = st.builds(
    smartHome_AnalogSensorType,
)
smartHome_Location_strategy = st.builds(
    smartHome_Location,
    name=
        safe_text
)
Sensor_strategy = st.builds(
    Sensor,
)
smartHome_BooleanSensor_strategy = st.builds(
    smartHome_BooleanSensor,
    value=
        st.booleans()
)
smartHome_IntegerSensor_strategy = st.builds(
    smartHome_IntegerSensor,
    value=
        st.integers()
)
smartHome_SensorType_strategy = st.builds(
    smartHome_SensorType,
    name=
        safe_text
)
smartHome_Sensor_strategy = st.builds(
    smartHome_Sensor,
    dataFile=
        safe_text,
    name=
        safe_text
)
smartHome_Duration_strategy = st.builds(
    smartHome_Duration,
    value=
        st.integers(),
    unit=
        safe_text
)
smartHome_Event_strategy = st.builds(
    smartHome_Event,
    description=
        safe_text
)
smartHome_Condition_strategy = st.builds(
    smartHome_Condition,
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=smartHome_IntegerCondition_strategy)
@settings(max_examples=50)
def test_smarthome_integercondition_instantiation(instance):
    assert isinstance(instance, smartHome_IntegerCondition)



@given(instance=smartHome_IntegerCondition_strategy)
def test_smarthome_integercondition_operand_setter(instance):
    original = instance.operand
    instance.operand = original
    assert instance.operand == original



@given(instance=smartHome_IntegerCondition_strategy)
def test_smarthome_integercondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=smartHome_BooleanCondition_strategy)
@settings(max_examples=50)
def test_smarthome_booleancondition_instantiation(instance):
    assert isinstance(instance, smartHome_BooleanCondition)



@given(instance=smartHome_BooleanCondition_strategy)
def test_smarthome_booleancondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=smartHome_BooleanCondition_strategy)
def test_smarthome_booleancondition_operand_setter(instance):
    original = instance.operand
    instance.operand = original
    assert instance.operand == original

@given(instance=smartHome_Rule_strategy)
@settings(max_examples=50)
def test_smarthome_rule_instantiation(instance):
    assert isinstance(instance, smartHome_Rule)

@given(instance=smartHome_SmartHome_strategy)
@settings(max_examples=50)
def test_smarthome_smarthome_instantiation(instance):
    assert isinstance(instance, smartHome_SmartHome)

@given(instance=SensorType_strategy)
@settings(max_examples=50)
def test_sensortype_instantiation(instance):
    assert isinstance(instance, SensorType)

@given(instance=smartHome_BooleanSensorType_strategy)
@settings(max_examples=50)
def test_smarthome_booleansensortype_instantiation(instance):
    assert isinstance(instance, smartHome_BooleanSensorType)

@given(instance=smartHome_AnalogSensorType_strategy)
@settings(max_examples=50)
def test_smarthome_analogsensortype_instantiation(instance):
    assert isinstance(instance, smartHome_AnalogSensorType)

@given(instance=smartHome_Location_strategy)
@settings(max_examples=50)
def test_smarthome_location_instantiation(instance):
    assert isinstance(instance, smartHome_Location)



@given(instance=smartHome_Location_strategy)
def test_smarthome_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=smartHome_BooleanSensor_strategy)
@settings(max_examples=50)
def test_smarthome_booleansensor_instantiation(instance):
    assert isinstance(instance, smartHome_BooleanSensor)



@given(instance=smartHome_BooleanSensor_strategy)
def test_smarthome_booleansensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smartHome_IntegerSensor_strategy)
@settings(max_examples=50)
def test_smarthome_integersensor_instantiation(instance):
    assert isinstance(instance, smartHome_IntegerSensor)



@given(instance=smartHome_IntegerSensor_strategy)
def test_smarthome_integersensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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
def test_smarthome_sensor_dataFile_setter(instance):
    original = instance.dataFile
    instance.dataFile = original
    assert instance.dataFile == original



@given(instance=smartHome_Sensor_strategy)
def test_smarthome_sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smartHome_Duration_strategy)
@settings(max_examples=50)
def test_smarthome_duration_instantiation(instance):
    assert isinstance(instance, smartHome_Duration)



@given(instance=smartHome_Duration_strategy)
def test_smarthome_duration_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smartHome_Duration_strategy)
def test_smarthome_duration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

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
