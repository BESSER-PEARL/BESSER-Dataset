import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractDevice,
    raspduinoDSL::Actuator,
    raspduinoDSL::Sensor,
    raspduinoDSL::Timer,
    raspduinoDSL::SensorListener,
    raspduinoDSL::EventHandler,
    raspduinoDSL::AbstractDevice,
    raspduinoDSL::ChangeActuator,
    raspduinoDSL::Model,
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



def test_raspduinodsl::actuator_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::Actuator)


def test_raspduinodsl::actuator_constructor_exists():
    assert callable(raspduinoDSL::Actuator.__init__)


def test_raspduinodsl::actuator_constructor_args():
    sig = inspect.signature(raspduinoDSL::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_raspduinodsl::sensor_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::Sensor)


def test_raspduinodsl::sensor_constructor_exists():
    assert callable(raspduinoDSL::Sensor.__init__)


def test_raspduinodsl::sensor_constructor_args():
    sig = inspect.signature(raspduinoDSL::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_raspduinodsl::timer_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::Timer)


def test_raspduinodsl::timer_constructor_exists():
    assert callable(raspduinoDSL::Timer.__init__)


def test_raspduinodsl::timer_constructor_args():
    sig = inspect.signature(raspduinoDSL::Timer.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "repeattype" in params, "Missing parameter 'repeattype'"
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "secs" in params, "Missing parameter 'secs'"

def test_raspduinodsl::timer_has_hours():
    assert hasattr(raspduinoDSL::Timer, "hours")
    descriptor = None
    for klass in raspduinoDSL::Timer.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::timer_has_repeattype():
    assert hasattr(raspduinoDSL::Timer, "repeattype")
    descriptor = None
    for klass in raspduinoDSL::Timer.__mro__:
        if "repeattype" in klass.__dict__:
            descriptor = klass.__dict__["repeattype"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::timer_has_minutes():
    assert hasattr(raspduinoDSL::Timer, "minutes")
    descriptor = None
    for klass in raspduinoDSL::Timer.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::timer_has_secs():
    assert hasattr(raspduinoDSL::Timer, "secs")
    descriptor = None
    for klass in raspduinoDSL::Timer.__mro__:
        if "secs" in klass.__dict__:
            descriptor = klass.__dict__["secs"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl::sensorlistener_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::SensorListener)


def test_raspduinodsl::sensorlistener_constructor_exists():
    assert callable(raspduinoDSL::SensorListener.__init__)


def test_raspduinodsl::sensorlistener_constructor_args():
    sig = inspect.signature(raspduinoDSL::SensorListener.__init__)
    params = list(sig.parameters.keys())
    assert "l" in params, "Missing parameter 'l'"
    assert "type" in params, "Missing parameter 'type'"
    assert "h" in params, "Missing parameter 'h'"

def test_raspduinodsl::sensorlistener_has_l():
    assert hasattr(raspduinoDSL::SensorListener, "l")
    descriptor = None
    for klass in raspduinoDSL::SensorListener.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::sensorlistener_has_type():
    assert hasattr(raspduinoDSL::SensorListener, "type")
    descriptor = None
    for klass in raspduinoDSL::SensorListener.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::sensorlistener_has_h():
    assert hasattr(raspduinoDSL::SensorListener, "h")
    descriptor = None
    for klass in raspduinoDSL::SensorListener.__mro__:
        if "h" in klass.__dict__:
            descriptor = klass.__dict__["h"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl::eventhandler_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::EventHandler)


def test_raspduinodsl::eventhandler_constructor_exists():
    assert callable(raspduinoDSL::EventHandler.__init__)


def test_raspduinodsl::eventhandler_constructor_args():
    sig = inspect.signature(raspduinoDSL::EventHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_raspduinodsl::eventhandler_has_name():
    assert hasattr(raspduinoDSL::EventHandler, "name")
    descriptor = None
    for klass in raspduinoDSL::EventHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl::abstractdevice_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::AbstractDevice)


def test_raspduinodsl::abstractdevice_constructor_exists():
    assert callable(raspduinoDSL::AbstractDevice.__init__)


def test_raspduinodsl::abstractdevice_constructor_args():
    sig = inspect.signature(raspduinoDSL::AbstractDevice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_raspduinodsl::abstractdevice_has_name():
    assert hasattr(raspduinoDSL::AbstractDevice, "name")
    descriptor = None
    for klass in raspduinoDSL::AbstractDevice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::abstractdevice_has_pin():
    assert hasattr(raspduinoDSL::AbstractDevice, "pin")
    descriptor = None
    for klass in raspduinoDSL::AbstractDevice.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl::changeactuator_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::ChangeActuator)


def test_raspduinodsl::changeactuator_constructor_exists():
    assert callable(raspduinoDSL::ChangeActuator.__init__)


def test_raspduinodsl::changeactuator_constructor_args():
    sig = inspect.signature(raspduinoDSL::ChangeActuator.__init__)
    params = list(sig.parameters.keys())
    assert "ActuatorState" in params, "Missing parameter 'ActuatorState'"

def test_raspduinodsl::changeactuator_has_ActuatorState():
    assert hasattr(raspduinoDSL::ChangeActuator, "ActuatorState")
    descriptor = None
    for klass in raspduinoDSL::ChangeActuator.__mro__:
        if "ActuatorState" in klass.__dict__:
            descriptor = klass.__dict__["ActuatorState"]
            break
    assert isinstance(descriptor, property)



def test_raspduinodsl::model_is_not_abstract():
    assert not inspect.isabstract(raspduinoDSL::Model)


def test_raspduinodsl::model_constructor_exists():
    assert callable(raspduinoDSL::Model.__init__)


def test_raspduinodsl::model_constructor_args():
    sig = inspect.signature(raspduinoDSL::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hardware" in params, "Missing parameter 'hardware'"

def test_raspduinodsl::model_has_name():
    assert hasattr(raspduinoDSL::Model, "name")
    descriptor = None
    for klass in raspduinoDSL::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_raspduinodsl::model_has_hardware():
    assert hasattr(raspduinoDSL::Model, "hardware")
    descriptor = None
    for klass in raspduinoDSL::Model.__mro__:
        if "hardware" in klass.__dict__:
            descriptor = klass.__dict__["hardware"]
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
raspduinoDSL::Actuator_strategy = st.builds(
    raspduinoDSL::Actuator,
)
raspduinoDSL::Sensor_strategy = st.builds(
    raspduinoDSL::Sensor,
)
raspduinoDSL::Timer_strategy = st.builds(
    raspduinoDSL::Timer,
    hours=
        st.integers(),
    repeattype=
        safe_text,
    minutes=
        st.integers(),
    secs=
        st.integers()
)
raspduinoDSL::SensorListener_strategy = st.builds(
    raspduinoDSL::SensorListener,
    l=
        st.integers(),
    type=
        safe_text,
    h=
        st.integers()
)
raspduinoDSL::EventHandler_strategy = st.builds(
    raspduinoDSL::EventHandler,
    name=
        safe_text
)
raspduinoDSL::AbstractDevice_strategy = st.builds(
    raspduinoDSL::AbstractDevice,
    name=
        safe_text,
    pin=
        safe_text
)
raspduinoDSL::ChangeActuator_strategy = st.builds(
    raspduinoDSL::ChangeActuator,
    ActuatorState=
        safe_text
)
raspduinoDSL::Model_strategy = st.builds(
    raspduinoDSL::Model,
    name=
        safe_text,
    hardware=
        safe_text
)

@given(instance=AbstractDevice_strategy)
@settings(max_examples=50)
def test_abstractdevice_instantiation(instance):
    assert isinstance(instance, AbstractDevice)

@given(instance=raspduinoDSL::Actuator_strategy)
@settings(max_examples=50)
def test_raspduinodsl::actuator_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::Actuator)

@given(instance=raspduinoDSL::Sensor_strategy)
@settings(max_examples=50)
def test_raspduinodsl::sensor_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::Sensor)

@given(instance=raspduinoDSL::Timer_strategy)
@settings(max_examples=50)
def test_raspduinodsl::timer_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::Timer)

@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_hours_type(instance):
    assert isinstance(instance.hours, int)


@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_repeattype_type(instance):
    assert isinstance(instance.repeattype, str)


@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_repeattype_setter(instance):
    original = instance.repeattype
    instance.repeattype = original
    assert instance.repeattype == original

@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_minutes_type(instance):
    assert isinstance(instance.minutes, int)


@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original

@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_secs_type(instance):
    assert isinstance(instance.secs, int)


@given(instance=raspduinoDSL::Timer_strategy)
def test_raspduinodsl::timer_secs_setter(instance):
    original = instance.secs
    instance.secs = original
    assert instance.secs == original

@given(instance=raspduinoDSL::SensorListener_strategy)
@settings(max_examples=50)
def test_raspduinodsl::sensorlistener_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::SensorListener)

@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_l_type(instance):
    assert isinstance(instance.l, int)


@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_h_type(instance):
    assert isinstance(instance.h, int)


@given(instance=raspduinoDSL::SensorListener_strategy)
def test_raspduinodsl::sensorlistener_h_setter(instance):
    original = instance.h
    instance.h = original
    assert instance.h == original

@given(instance=raspduinoDSL::EventHandler_strategy)
@settings(max_examples=50)
def test_raspduinodsl::eventhandler_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::EventHandler)

@given(instance=raspduinoDSL::EventHandler_strategy)
def test_raspduinodsl::eventhandler_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=raspduinoDSL::EventHandler_strategy)
def test_raspduinodsl::eventhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=raspduinoDSL::AbstractDevice_strategy)
@settings(max_examples=50)
def test_raspduinodsl::abstractdevice_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::AbstractDevice)

@given(instance=raspduinoDSL::AbstractDevice_strategy)
def test_raspduinodsl::abstractdevice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=raspduinoDSL::AbstractDevice_strategy)
def test_raspduinodsl::abstractdevice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=raspduinoDSL::AbstractDevice_strategy)
def test_raspduinodsl::abstractdevice_pin_type(instance):
    assert isinstance(instance.pin, str)


@given(instance=raspduinoDSL::AbstractDevice_strategy)
def test_raspduinodsl::abstractdevice_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=raspduinoDSL::ChangeActuator_strategy)
@settings(max_examples=50)
def test_raspduinodsl::changeactuator_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::ChangeActuator)

@given(instance=raspduinoDSL::ChangeActuator_strategy)
def test_raspduinodsl::changeactuator_ActuatorState_type(instance):
    assert isinstance(instance.ActuatorState, str)


@given(instance=raspduinoDSL::ChangeActuator_strategy)
def test_raspduinodsl::changeactuator_ActuatorState_setter(instance):
    original = instance.ActuatorState
    instance.ActuatorState = original
    assert instance.ActuatorState == original

@given(instance=raspduinoDSL::Model_strategy)
@settings(max_examples=50)
def test_raspduinodsl::model_instantiation(instance):
    assert isinstance(instance, raspduinoDSL::Model)

@given(instance=raspduinoDSL::Model_strategy)
def test_raspduinodsl::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=raspduinoDSL::Model_strategy)
def test_raspduinodsl::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=raspduinoDSL::Model_strategy)
def test_raspduinodsl::model_hardware_type(instance):
    assert isinstance(instance.hardware, str)


@given(instance=raspduinoDSL::Model_strategy)
def test_raspduinodsl::model_hardware_setter(instance):
    original = instance.hardware
    instance.hardware = original
    assert instance.hardware == original
