import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ioT_FetchDataExpression,
    ioT_FetchDataCondition,
    ioT_Condition,
    ioT_Time,
    ioT_Device,
    ioT_DeviceTypes,
    ioT_DeviceType,
    Condition,
    ioT_LiteralNumber,
    ioT_OrCondition,
    ioT_LiteralBool,
    ioT_AndCondition,
    ioT_ComparisonCondition,
    ioT_FetchData,
    ioT_Destination,
    ioT_DestinationTypes,
    ioT_DestinationType,
    ioT_Portnumber,
    ioT_Ip,
    ioT_Server,
    ioT_ServerTypes,
    ioT_ServerType,
    ioT_Method,
    ioT_SensorGetMethod,
    ioT_SensorGroup,
    ioT_Sensor,
    ioT_SensorTypes,
    ioT_SensorType,
    ioT_EObject,
    ioT_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot_fetchdataexpression_is_not_abstract():
    assert not inspect.isabstract(ioT_FetchDataExpression)


def test_iot_fetchdataexpression_constructor_exists():
    assert callable(ioT_FetchDataExpression.__init__)


def test_iot_fetchdataexpression_constructor_args():
    sig = inspect.signature(ioT_FetchDataExpression.__init__)
    params = list(sig.parameters.keys())
    assert "timeUnit" in params, "Missing parameter 'timeUnit'"

def test_iot_fetchdataexpression_has_timeUnit():
    assert hasattr(ioT_FetchDataExpression, "timeUnit")
    descriptor = None
    for klass in ioT_FetchDataExpression.__mro__:
        if "timeUnit" in klass.__dict__:
            descriptor = klass.__dict__["timeUnit"]
            break
    assert isinstance(descriptor, property)



def test_iot_fetchdatacondition_is_not_abstract():
    assert not inspect.isabstract(ioT_FetchDataCondition)


def test_iot_fetchdatacondition_constructor_exists():
    assert callable(ioT_FetchDataCondition.__init__)


def test_iot_fetchdatacondition_constructor_args():
    sig = inspect.signature(ioT_FetchDataCondition.__init__)
    params = list(sig.parameters.keys())



def test_iot_condition_is_not_abstract():
    assert not inspect.isabstract(ioT_Condition)


def test_iot_condition_constructor_exists():
    assert callable(ioT_Condition.__init__)


def test_iot_condition_constructor_args():
    sig = inspect.signature(ioT_Condition.__init__)
    params = list(sig.parameters.keys())



def test_iot_time_is_not_abstract():
    assert not inspect.isabstract(ioT_Time)


def test_iot_time_constructor_exists():
    assert callable(ioT_Time.__init__)


def test_iot_time_constructor_args():
    sig = inspect.signature(ioT_Time.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_iot_time_has_time():
    assert hasattr(ioT_Time, "time")
    descriptor = None
    for klass in ioT_Time.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_iot_device_is_not_abstract():
    assert not inspect.isabstract(ioT_Device)


def test_iot_device_constructor_exists():
    assert callable(ioT_Device.__init__)


def test_iot_device_constructor_args():
    sig = inspect.signature(ioT_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_device_has_name():
    assert hasattr(ioT_Device, "name")
    descriptor = None
    for klass in ioT_Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_devicetypes_is_not_abstract():
    assert not inspect.isabstract(ioT_DeviceTypes)


def test_iot_devicetypes_constructor_exists():
    assert callable(ioT_DeviceTypes.__init__)


def test_iot_devicetypes_constructor_args():
    sig = inspect.signature(ioT_DeviceTypes.__init__)
    params = list(sig.parameters.keys())



def test_iot_devicetype_is_not_abstract():
    assert not inspect.isabstract(ioT_DeviceType)


def test_iot_devicetype_constructor_exists():
    assert callable(ioT_DeviceType.__init__)


def test_iot_devicetype_constructor_args():
    sig = inspect.signature(ioT_DeviceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_devicetype_has_name():
    assert hasattr(ioT_DeviceType, "name")
    descriptor = None
    for klass in ioT_DeviceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_iot_literalnumber_is_not_abstract():
    assert not inspect.isabstract(ioT_LiteralNumber)


def test_iot_literalnumber_constructor_exists():
    assert callable(ioT_LiteralNumber.__init__)


def test_iot_literalnumber_constructor_args():
    sig = inspect.signature(ioT_LiteralNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot_literalnumber_has_value():
    assert hasattr(ioT_LiteralNumber, "value")
    descriptor = None
    for klass in ioT_LiteralNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot_orcondition_is_not_abstract():
    assert not inspect.isabstract(ioT_OrCondition)


def test_iot_orcondition_constructor_exists():
    assert callable(ioT_OrCondition.__init__)


def test_iot_orcondition_constructor_args():
    sig = inspect.signature(ioT_OrCondition.__init__)
    params = list(sig.parameters.keys())



def test_iot_literalbool_is_not_abstract():
    assert not inspect.isabstract(ioT_LiteralBool)


def test_iot_literalbool_constructor_exists():
    assert callable(ioT_LiteralBool.__init__)


def test_iot_literalbool_constructor_args():
    sig = inspect.signature(ioT_LiteralBool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot_literalbool_has_value():
    assert hasattr(ioT_LiteralBool, "value")
    descriptor = None
    for klass in ioT_LiteralBool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot_andcondition_is_not_abstract():
    assert not inspect.isabstract(ioT_AndCondition)


def test_iot_andcondition_constructor_exists():
    assert callable(ioT_AndCondition.__init__)


def test_iot_andcondition_constructor_args():
    sig = inspect.signature(ioT_AndCondition.__init__)
    params = list(sig.parameters.keys())



def test_iot_comparisoncondition_is_not_abstract():
    assert not inspect.isabstract(ioT_ComparisonCondition)


def test_iot_comparisoncondition_constructor_exists():
    assert callable(ioT_ComparisonCondition.__init__)


def test_iot_comparisoncondition_constructor_args():
    sig = inspect.signature(ioT_ComparisonCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot_comparisoncondition_has_operator():
    assert hasattr(ioT_ComparisonCondition, "operator")
    descriptor = None
    for klass in ioT_ComparisonCondition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot_fetchdata_is_not_abstract():
    assert not inspect.isabstract(ioT_FetchData)


def test_iot_fetchdata_constructor_exists():
    assert callable(ioT_FetchData.__init__)


def test_iot_fetchdata_constructor_args():
    sig = inspect.signature(ioT_FetchData.__init__)
    params = list(sig.parameters.keys())



def test_iot_destination_is_not_abstract():
    assert not inspect.isabstract(ioT_Destination)


def test_iot_destination_constructor_exists():
    assert callable(ioT_Destination.__init__)


def test_iot_destination_constructor_args():
    sig = inspect.signature(ioT_Destination.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_destination_has_name():
    assert hasattr(ioT_Destination, "name")
    descriptor = None
    for klass in ioT_Destination.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_destinationtypes_is_not_abstract():
    assert not inspect.isabstract(ioT_DestinationTypes)


def test_iot_destinationtypes_constructor_exists():
    assert callable(ioT_DestinationTypes.__init__)


def test_iot_destinationtypes_constructor_args():
    sig = inspect.signature(ioT_DestinationTypes.__init__)
    params = list(sig.parameters.keys())



def test_iot_destinationtype_is_not_abstract():
    assert not inspect.isabstract(ioT_DestinationType)


def test_iot_destinationtype_constructor_exists():
    assert callable(ioT_DestinationType.__init__)


def test_iot_destinationtype_constructor_args():
    sig = inspect.signature(ioT_DestinationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_destinationtype_has_name():
    assert hasattr(ioT_DestinationType, "name")
    descriptor = None
    for klass in ioT_DestinationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_portnumber_is_not_abstract():
    assert not inspect.isabstract(ioT_Portnumber)


def test_iot_portnumber_constructor_exists():
    assert callable(ioT_Portnumber.__init__)


def test_iot_portnumber_constructor_args():
    sig = inspect.signature(ioT_Portnumber.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_iot_portnumber_has_number():
    assert hasattr(ioT_Portnumber, "number")
    descriptor = None
    for klass in ioT_Portnumber.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_iot_ip_is_not_abstract():
    assert not inspect.isabstract(ioT_Ip)


def test_iot_ip_constructor_exists():
    assert callable(ioT_Ip.__init__)


def test_iot_ip_constructor_args():
    sig = inspect.signature(ioT_Ip.__init__)
    params = list(sig.parameters.keys())
    assert "ip" in params, "Missing parameter 'ip'"

def test_iot_ip_has_ip():
    assert hasattr(ioT_Ip, "ip")
    descriptor = None
    for klass in ioT_Ip.__mro__:
        if "ip" in klass.__dict__:
            descriptor = klass.__dict__["ip"]
            break
    assert isinstance(descriptor, property)



def test_iot_server_is_not_abstract():
    assert not inspect.isabstract(ioT_Server)


def test_iot_server_constructor_exists():
    assert callable(ioT_Server.__init__)


def test_iot_server_constructor_args():
    sig = inspect.signature(ioT_Server.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_server_has_name():
    assert hasattr(ioT_Server, "name")
    descriptor = None
    for klass in ioT_Server.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_servertypes_is_not_abstract():
    assert not inspect.isabstract(ioT_ServerTypes)


def test_iot_servertypes_constructor_exists():
    assert callable(ioT_ServerTypes.__init__)


def test_iot_servertypes_constructor_args():
    sig = inspect.signature(ioT_ServerTypes.__init__)
    params = list(sig.parameters.keys())



def test_iot_servertype_is_not_abstract():
    assert not inspect.isabstract(ioT_ServerType)


def test_iot_servertype_constructor_exists():
    assert callable(ioT_ServerType.__init__)


def test_iot_servertype_constructor_args():
    sig = inspect.signature(ioT_ServerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_servertype_has_name():
    assert hasattr(ioT_ServerType, "name")
    descriptor = None
    for klass in ioT_ServerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_method_is_not_abstract():
    assert not inspect.isabstract(ioT_Method)


def test_iot_method_constructor_exists():
    assert callable(ioT_Method.__init__)


def test_iot_method_constructor_args():
    sig = inspect.signature(ioT_Method.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot_method_has_parameters():
    assert hasattr(ioT_Method, "parameters")
    descriptor = None
    for klass in ioT_Method.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_iot_method_has_name():
    assert hasattr(ioT_Method, "name")
    descriptor = None
    for klass in ioT_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_sensorgetmethod_is_not_abstract():
    assert not inspect.isabstract(ioT_SensorGetMethod)


def test_iot_sensorgetmethod_constructor_exists():
    assert callable(ioT_SensorGetMethod.__init__)


def test_iot_sensorgetmethod_constructor_args():
    sig = inspect.signature(ioT_SensorGetMethod.__init__)
    params = list(sig.parameters.keys())



def test_iot_sensorgroup_is_not_abstract():
    assert not inspect.isabstract(ioT_SensorGroup)


def test_iot_sensorgroup_constructor_exists():
    assert callable(ioT_SensorGroup.__init__)


def test_iot_sensorgroup_constructor_args():
    sig = inspect.signature(ioT_SensorGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_sensorgroup_has_name():
    assert hasattr(ioT_SensorGroup, "name")
    descriptor = None
    for klass in ioT_SensorGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_sensor_is_not_abstract():
    assert not inspect.isabstract(ioT_Sensor)


def test_iot_sensor_constructor_exists():
    assert callable(ioT_Sensor.__init__)


def test_iot_sensor_constructor_args():
    sig = inspect.signature(ioT_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_sensor_has_name():
    assert hasattr(ioT_Sensor, "name")
    descriptor = None
    for klass in ioT_Sensor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_sensortypes_is_not_abstract():
    assert not inspect.isabstract(ioT_SensorTypes)


def test_iot_sensortypes_constructor_exists():
    assert callable(ioT_SensorTypes.__init__)


def test_iot_sensortypes_constructor_args():
    sig = inspect.signature(ioT_SensorTypes.__init__)
    params = list(sig.parameters.keys())



def test_iot_sensortype_is_not_abstract():
    assert not inspect.isabstract(ioT_SensorType)


def test_iot_sensortype_constructor_exists():
    assert callable(ioT_SensorType.__init__)


def test_iot_sensortype_constructor_args():
    sig = inspect.signature(ioT_SensorType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_sensortype_has_name():
    assert hasattr(ioT_SensorType, "name")
    descriptor = None
    for klass in ioT_SensorType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_eobject_is_not_abstract():
    assert not inspect.isabstract(ioT_EObject)


def test_iot_eobject_constructor_exists():
    assert callable(ioT_EObject.__init__)


def test_iot_eobject_constructor_args():
    sig = inspect.signature(ioT_EObject.__init__)
    params = list(sig.parameters.keys())



def test_iot_system_is_not_abstract():
    assert not inspect.isabstract(ioT_System)


def test_iot_system_constructor_exists():
    assert callable(ioT_System.__init__)


def test_iot_system_constructor_args():
    sig = inspect.signature(ioT_System.__init__)
    params = list(sig.parameters.keys())


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
ioT_FetchDataExpression_strategy = st.builds(
    ioT_FetchDataExpression,
    timeUnit=
        safe_text
)
ioT_FetchDataCondition_strategy = st.builds(
    ioT_FetchDataCondition,
)
ioT_Condition_strategy = st.builds(
    ioT_Condition,
)
ioT_Time_strategy = st.builds(
    ioT_Time,
    time=
        st.integers()
)
ioT_Device_strategy = st.builds(
    ioT_Device,
    name=
        safe_text
)
ioT_DeviceTypes_strategy = st.builds(
    ioT_DeviceTypes,
)
ioT_DeviceType_strategy = st.builds(
    ioT_DeviceType,
    name=
        safe_text
)
Condition_strategy = st.builds(
    Condition,
)
ioT_LiteralNumber_strategy = st.builds(
    ioT_LiteralNumber,
    value=
        st.integers()
)
ioT_OrCondition_strategy = st.builds(
    ioT_OrCondition,
)
ioT_LiteralBool_strategy = st.builds(
    ioT_LiteralBool,
    value=
        safe_text
)
ioT_AndCondition_strategy = st.builds(
    ioT_AndCondition,
)
ioT_ComparisonCondition_strategy = st.builds(
    ioT_ComparisonCondition,
    operator=
        safe_text
)
ioT_FetchData_strategy = st.builds(
    ioT_FetchData,
)
ioT_Destination_strategy = st.builds(
    ioT_Destination,
    name=
        safe_text
)
ioT_DestinationTypes_strategy = st.builds(
    ioT_DestinationTypes,
)
ioT_DestinationType_strategy = st.builds(
    ioT_DestinationType,
    name=
        safe_text
)
ioT_Portnumber_strategy = st.builds(
    ioT_Portnumber,
    number=
        st.integers()
)
ioT_Ip_strategy = st.builds(
    ioT_Ip,
    ip=
        st.integers()
)
ioT_Server_strategy = st.builds(
    ioT_Server,
    name=
        safe_text
)
ioT_ServerTypes_strategy = st.builds(
    ioT_ServerTypes,
)
ioT_ServerType_strategy = st.builds(
    ioT_ServerType,
    name=
        safe_text
)
ioT_Method_strategy = st.builds(
    ioT_Method,
    parameters=
        safe_text,
    name=
        safe_text
)
ioT_SensorGetMethod_strategy = st.builds(
    ioT_SensorGetMethod,
)
ioT_SensorGroup_strategy = st.builds(
    ioT_SensorGroup,
    name=
        safe_text
)
ioT_Sensor_strategy = st.builds(
    ioT_Sensor,
    name=
        safe_text
)
ioT_SensorTypes_strategy = st.builds(
    ioT_SensorTypes,
)
ioT_SensorType_strategy = st.builds(
    ioT_SensorType,
    name=
        safe_text
)
ioT_EObject_strategy = st.builds(
    ioT_EObject,
)
ioT_System_strategy = st.builds(
    ioT_System,
)

@given(instance=ioT_FetchDataExpression_strategy)
@settings(max_examples=50)
def test_iot_fetchdataexpression_instantiation(instance):
    assert isinstance(instance, ioT_FetchDataExpression)



@given(instance=ioT_FetchDataExpression_strategy)
def test_iot_fetchdataexpression_timeUnit_setter(instance):
    original = instance.timeUnit
    instance.timeUnit = original
    assert instance.timeUnit == original

@given(instance=ioT_FetchDataCondition_strategy)
@settings(max_examples=50)
def test_iot_fetchdatacondition_instantiation(instance):
    assert isinstance(instance, ioT_FetchDataCondition)

@given(instance=ioT_Condition_strategy)
@settings(max_examples=50)
def test_iot_condition_instantiation(instance):
    assert isinstance(instance, ioT_Condition)

@given(instance=ioT_Time_strategy)
@settings(max_examples=50)
def test_iot_time_instantiation(instance):
    assert isinstance(instance, ioT_Time)



@given(instance=ioT_Time_strategy)
def test_iot_time_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=ioT_Device_strategy)
@settings(max_examples=50)
def test_iot_device_instantiation(instance):
    assert isinstance(instance, ioT_Device)



@given(instance=ioT_Device_strategy)
def test_iot_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_DeviceTypes_strategy)
@settings(max_examples=50)
def test_iot_devicetypes_instantiation(instance):
    assert isinstance(instance, ioT_DeviceTypes)

@given(instance=ioT_DeviceType_strategy)
@settings(max_examples=50)
def test_iot_devicetype_instantiation(instance):
    assert isinstance(instance, ioT_DeviceType)



@given(instance=ioT_DeviceType_strategy)
def test_iot_devicetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=ioT_LiteralNumber_strategy)
@settings(max_examples=50)
def test_iot_literalnumber_instantiation(instance):
    assert isinstance(instance, ioT_LiteralNumber)



@given(instance=ioT_LiteralNumber_strategy)
def test_iot_literalnumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ioT_OrCondition_strategy)
@settings(max_examples=50)
def test_iot_orcondition_instantiation(instance):
    assert isinstance(instance, ioT_OrCondition)

@given(instance=ioT_LiteralBool_strategy)
@settings(max_examples=50)
def test_iot_literalbool_instantiation(instance):
    assert isinstance(instance, ioT_LiteralBool)



@given(instance=ioT_LiteralBool_strategy)
def test_iot_literalbool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ioT_AndCondition_strategy)
@settings(max_examples=50)
def test_iot_andcondition_instantiation(instance):
    assert isinstance(instance, ioT_AndCondition)

@given(instance=ioT_ComparisonCondition_strategy)
@settings(max_examples=50)
def test_iot_comparisoncondition_instantiation(instance):
    assert isinstance(instance, ioT_ComparisonCondition)



@given(instance=ioT_ComparisonCondition_strategy)
def test_iot_comparisoncondition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ioT_FetchData_strategy)
@settings(max_examples=50)
def test_iot_fetchdata_instantiation(instance):
    assert isinstance(instance, ioT_FetchData)

@given(instance=ioT_Destination_strategy)
@settings(max_examples=50)
def test_iot_destination_instantiation(instance):
    assert isinstance(instance, ioT_Destination)



@given(instance=ioT_Destination_strategy)
def test_iot_destination_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_DestinationTypes_strategy)
@settings(max_examples=50)
def test_iot_destinationtypes_instantiation(instance):
    assert isinstance(instance, ioT_DestinationTypes)

@given(instance=ioT_DestinationType_strategy)
@settings(max_examples=50)
def test_iot_destinationtype_instantiation(instance):
    assert isinstance(instance, ioT_DestinationType)



@given(instance=ioT_DestinationType_strategy)
def test_iot_destinationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_Portnumber_strategy)
@settings(max_examples=50)
def test_iot_portnumber_instantiation(instance):
    assert isinstance(instance, ioT_Portnumber)



@given(instance=ioT_Portnumber_strategy)
def test_iot_portnumber_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=ioT_Ip_strategy)
@settings(max_examples=50)
def test_iot_ip_instantiation(instance):
    assert isinstance(instance, ioT_Ip)



@given(instance=ioT_Ip_strategy)
def test_iot_ip_ip_setter(instance):
    original = instance.ip
    instance.ip = original
    assert instance.ip == original

@given(instance=ioT_Server_strategy)
@settings(max_examples=50)
def test_iot_server_instantiation(instance):
    assert isinstance(instance, ioT_Server)



@given(instance=ioT_Server_strategy)
def test_iot_server_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_ServerTypes_strategy)
@settings(max_examples=50)
def test_iot_servertypes_instantiation(instance):
    assert isinstance(instance, ioT_ServerTypes)

@given(instance=ioT_ServerType_strategy)
@settings(max_examples=50)
def test_iot_servertype_instantiation(instance):
    assert isinstance(instance, ioT_ServerType)



@given(instance=ioT_ServerType_strategy)
def test_iot_servertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_Method_strategy)
@settings(max_examples=50)
def test_iot_method_instantiation(instance):
    assert isinstance(instance, ioT_Method)



@given(instance=ioT_Method_strategy)
def test_iot_method_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original



@given(instance=ioT_Method_strategy)
def test_iot_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_SensorGetMethod_strategy)
@settings(max_examples=50)
def test_iot_sensorgetmethod_instantiation(instance):
    assert isinstance(instance, ioT_SensorGetMethod)

@given(instance=ioT_SensorGroup_strategy)
@settings(max_examples=50)
def test_iot_sensorgroup_instantiation(instance):
    assert isinstance(instance, ioT_SensorGroup)



@given(instance=ioT_SensorGroup_strategy)
def test_iot_sensorgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_Sensor_strategy)
@settings(max_examples=50)
def test_iot_sensor_instantiation(instance):
    assert isinstance(instance, ioT_Sensor)



@given(instance=ioT_Sensor_strategy)
def test_iot_sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_SensorTypes_strategy)
@settings(max_examples=50)
def test_iot_sensortypes_instantiation(instance):
    assert isinstance(instance, ioT_SensorTypes)

@given(instance=ioT_SensorType_strategy)
@settings(max_examples=50)
def test_iot_sensortype_instantiation(instance):
    assert isinstance(instance, ioT_SensorType)



@given(instance=ioT_SensorType_strategy)
def test_iot_sensortype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_EObject_strategy)
@settings(max_examples=50)
def test_iot_eobject_instantiation(instance):
    assert isinstance(instance, ioT_EObject)

@given(instance=ioT_System_strategy)
@settings(max_examples=50)
def test_iot_system_instantiation(instance):
    assert isinstance(instance, ioT_System)
