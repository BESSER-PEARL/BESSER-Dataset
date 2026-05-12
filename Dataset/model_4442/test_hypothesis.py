import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractDevice,
    raspduinoDSL_Actuator,
    raspduinoDSL_Sensor,
    raspduinoDSL_Timer,
    raspduinoDSL_SensorListener,
    raspduinoDSL_EventHandler,
    raspduinoDSL_AbstractDevice,
    raspduinoDSL_ChangeActuator,
    raspduinoDSL_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractdevice_is_not_abstract():
    assert not inspect.isabstract(AbstractDevice)


def test_abstractdevice_constructor_exists():
    assert callable(AbstractDevice.__init__)


def test_abstractdevice_constructor_args():
    sig = inspect.signature(AbstractDevice.__init__)
    params = list(sig.parameters.keys())



def test_raspduinodsl_actuator_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_Actuator)


def test_raspduinodsl_actuator_constructor_exists():
    assert callable(raspduinoDSL_Actuator.__init__)


def test_raspduinodsl_actuator_constructor_args():
    sig = inspect.signature(raspduinoDSL_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_raspduinodsl_sensor_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_Sensor)


def test_raspduinodsl_sensor_constructor_exists():
    assert callable(raspduinoDSL_Sensor.__init__)


def test_raspduinodsl_sensor_constructor_args():
    sig = inspect.signature(raspduinoDSL_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_raspduinodsl_timer_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_Timer)


def test_raspduinodsl_timer_constructor_exists():
    assert callable(raspduinoDSL_Timer.__init__)


def test_raspduinodsl_timer_constructor_args():
    sig = inspect.signature(raspduinoDSL_Timer.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "repeattype" in params, "Missing parameter 'repeattype'"
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "secs" in params, "Missing parameter 'secs'"

def test_raspduinodsl_timer_has_hours():
    assert hasattr(raspduinoDSL_Timer, "hours")
    descriptor = None
    for klass in raspduinoDSL_Timer.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_timer_has_repeattype():
    assert hasattr(raspduinoDSL_Timer, "repeattype")
    descriptor = None
    for klass in raspduinoDSL_Timer.__mro__:
        if "repeattype" in klass.__dict__:
            descriptor = klass.__dict__["repeattype"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_timer_has_minutes():
    assert hasattr(raspduinoDSL_Timer, "minutes")
    descriptor = None
    for klass in raspduinoDSL_Timer.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_timer_has_secs():
    assert hasattr(raspduinoDSL_Timer, "secs")
    descriptor = None
    for klass in raspduinoDSL_Timer.__mro__:
        if "secs" in klass.__dict__:
            descriptor = klass.__dict__["secs"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl_sensorlistener_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_SensorListener)


def test_raspduinodsl_sensorlistener_constructor_exists():
    assert callable(raspduinoDSL_SensorListener.__init__)


def test_raspduinodsl_sensorlistener_constructor_args():
    sig = inspect.signature(raspduinoDSL_SensorListener.__init__)
    params = list(sig.parameters.keys())
    assert "h" in params, "Missing parameter 'h'"
    assert "l" in params, "Missing parameter 'l'"
    assert "type" in params, "Missing parameter 'type'"

def test_raspduinodsl_sensorlistener_has_h():
    assert hasattr(raspduinoDSL_SensorListener, "h")
    descriptor = None
    for klass in raspduinoDSL_SensorListener.__mro__:
        if "h" in klass.__dict__:
            descriptor = klass.__dict__["h"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_sensorlistener_has_l():
    assert hasattr(raspduinoDSL_SensorListener, "l")
    descriptor = None
    for klass in raspduinoDSL_SensorListener.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_sensorlistener_has_type():
    assert hasattr(raspduinoDSL_SensorListener, "type")
    descriptor = None
    for klass in raspduinoDSL_SensorListener.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl_eventhandler_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_EventHandler)


def test_raspduinodsl_eventhandler_constructor_exists():
    assert callable(raspduinoDSL_EventHandler.__init__)


def test_raspduinodsl_eventhandler_constructor_args():
    sig = inspect.signature(raspduinoDSL_EventHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_raspduinodsl_eventhandler_has_name():
    assert hasattr(raspduinoDSL_EventHandler, "name")
    descriptor = None
    for klass in raspduinoDSL_EventHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl_abstractdevice_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_AbstractDevice)


def test_raspduinodsl_abstractdevice_constructor_exists():
    assert callable(raspduinoDSL_AbstractDevice.__init__)


def test_raspduinodsl_abstractdevice_constructor_args():
    sig = inspect.signature(raspduinoDSL_AbstractDevice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_raspduinodsl_abstractdevice_has_name():
    assert hasattr(raspduinoDSL_AbstractDevice, "name")
    descriptor = None
    for klass in raspduinoDSL_AbstractDevice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_abstractdevice_has_pin():
    assert hasattr(raspduinoDSL_AbstractDevice, "pin")
    descriptor = None
    for klass in raspduinoDSL_AbstractDevice.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl_changeactuator_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_ChangeActuator)


def test_raspduinodsl_changeactuator_constructor_exists():
    assert callable(raspduinoDSL_ChangeActuator.__init__)


def test_raspduinodsl_changeactuator_constructor_args():
    sig = inspect.signature(raspduinoDSL_ChangeActuator.__init__)
    params = list(sig.parameters.keys())
    assert "ActuatorState" in params, "Missing parameter 'ActuatorState'"

def test_raspduinodsl_changeactuator_has_ActuatorState():
    assert hasattr(raspduinoDSL_ChangeActuator, "ActuatorState")
    descriptor = None
    for klass in raspduinoDSL_ChangeActuator.__mro__:
        if "ActuatorState" in klass.__dict__:
            descriptor = klass.__dict__["ActuatorState"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl_model_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL_Model)


def test_raspduinodsl_model_constructor_exists():
    assert callable(raspduinoDSL_Model.__init__)


def test_raspduinodsl_model_constructor_args():
    sig = inspect.signature(raspduinoDSL_Model.__init__)
    params = list(sig.parameters.keys())
    assert "hardware" in params, "Missing parameter 'hardware'"
    assert "name" in params, "Missing parameter 'name'"

def test_raspduinodsl_model_has_hardware():
    assert hasattr(raspduinoDSL_Model, "hardware")
    descriptor = None
    for klass in raspduinoDSL_Model.__mro__:
        if "hardware" in klass.__dict__:
            descriptor = klass.__dict__["hardware"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl_model_has_name():
    assert hasattr(raspduinoDSL_Model, "name")
    descriptor = None
    for klass in raspduinoDSL_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
AbstractDevice_strategy = st.builds(
    AbstractDevice,
)
raspduinoDSL_Actuator_strategy = st.builds(
    raspduinoDSL_Actuator,
)
raspduinoDSL_Sensor_strategy = st.builds(
    raspduinoDSL_Sensor,
)
raspduinoDSL_Timer_strategy = st.builds(
    raspduinoDSL_Timer,
    hours=
        st.integers(),
    repeattype=
        safe_text,
    minutes=
        st.integers(),
    secs=
        st.integers()
)
raspduinoDSL_SensorListener_strategy = st.builds(
    raspduinoDSL_SensorListener,
    h=
        st.integers(),
    l=
        st.integers(),
    type=
        safe_text
)
raspduinoDSL_EventHandler_strategy = st.builds(
    raspduinoDSL_EventHandler,
    name=
        safe_text
)
raspduinoDSL_AbstractDevice_strategy = st.builds(
    raspduinoDSL_AbstractDevice,
    name=
        safe_text,
    pin=
        safe_text
)
raspduinoDSL_ChangeActuator_strategy = st.builds(
    raspduinoDSL_ChangeActuator,
    ActuatorState=
        safe_text
)
raspduinoDSL_Model_strategy = st.builds(
    raspduinoDSL_Model,
    hardware=
        safe_text,
    name=
        safe_text
)

@given(instance=AbstractDevice_strategy)
@settings(max_examples=50)
def test_abstractdevice_instantiation(instance):
    assert isinstance(instance, AbstractDevice)

@given(instance=raspduinoDSL_Actuator_strategy)
@settings(max_examples=50)
def test_raspduinodsl_actuator_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_Actuator)

@given(instance=raspduinoDSL_Sensor_strategy)
@settings(max_examples=50)
def test_raspduinodsl_sensor_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_Sensor)

@given(instance=raspduinoDSL_Timer_strategy)
@settings(max_examples=50)
def test_raspduinodsl_timer_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_Timer)



@given(instance=raspduinoDSL_Timer_strategy)
def test_raspduinodsl_timer_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original



@given(instance=raspduinoDSL_Timer_strategy)
def test_raspduinodsl_timer_repeattype_setter(instance):
    original = instance.repeattype
    instance.repeattype = original
    assert instance.repeattype == original



@given(instance=raspduinoDSL_Timer_strategy)
def test_raspduinodsl_timer_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=raspduinoDSL_Timer_strategy)
def test_raspduinodsl_timer_secs_setter(instance):
    original = instance.secs
    instance.secs = original
    assert instance.secs == original

@given(instance=raspduinoDSL_SensorListener_strategy)
@settings(max_examples=50)
def test_raspduinodsl_sensorlistener_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_SensorListener)



@given(instance=raspduinoDSL_SensorListener_strategy)
def test_raspduinodsl_sensorlistener_h_setter(instance):
    original = instance.h
    instance.h = original
    assert instance.h == original



@given(instance=raspduinoDSL_SensorListener_strategy)
def test_raspduinodsl_sensorlistener_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original



@given(instance=raspduinoDSL_SensorListener_strategy)
def test_raspduinodsl_sensorlistener_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=raspduinoDSL_EventHandler_strategy)
@settings(max_examples=50)
def test_raspduinodsl_eventhandler_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_EventHandler)



@given(instance=raspduinoDSL_EventHandler_strategy)
def test_raspduinodsl_eventhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=raspduinoDSL_AbstractDevice_strategy)
@settings(max_examples=50)
def test_raspduinodsl_abstractdevice_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_AbstractDevice)



@given(instance=raspduinoDSL_AbstractDevice_strategy)
def test_raspduinodsl_abstractdevice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=raspduinoDSL_AbstractDevice_strategy)
def test_raspduinodsl_abstractdevice_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=raspduinoDSL_ChangeActuator_strategy)
@settings(max_examples=50)
def test_raspduinodsl_changeactuator_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_ChangeActuator)



@given(instance=raspduinoDSL_ChangeActuator_strategy)
def test_raspduinodsl_changeactuator_ActuatorState_setter(instance):
    original = instance.ActuatorState
    instance.ActuatorState = original
    assert instance.ActuatorState == original

@given(instance=raspduinoDSL_Model_strategy)
@settings(max_examples=50)
def test_raspduinodsl_model_instantiation(instance):
    assert isinstance(instance, raspduinoDSL_Model)



@given(instance=raspduinoDSL_Model_strategy)
def test_raspduinodsl_model_hardware_setter(instance):
    original = instance.hardware
    instance.hardware = original
    assert instance.hardware == original



@given(instance=raspduinoDSL_Model_strategy)
def test_raspduinodsl_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
