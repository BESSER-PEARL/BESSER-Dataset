import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Home_Security,
    Temperature_sensor,
    Server,
    Lock_doors_sensors,
    Light_Sensor,
    Event_Log,
    Camera_sensor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_home_security_is_not_abstract():
    assert not inspect.isabstract(Home_Security)


def test_home_security_constructor_exists():
    assert callable(Home_Security.__init__)


def test_home_security_constructor_args():
    sig = inspect.signature(Home_Security.__init__)
    params = list(sig.parameters.keys())



def test_temperature_sensor_is_not_abstract():
    assert not inspect.isabstract(Temperature_sensor)


def test_temperature_sensor_constructor_exists():
    assert callable(Temperature_sensor.__init__)


def test_temperature_sensor_constructor_args():
    sig = inspect.signature(Temperature_sensor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_temperature_sensor_has_attribute():
    assert hasattr(Temperature_sensor, "attribute")
    descriptor = None
    for klass in Temperature_sensor.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_server_is_not_abstract():
    assert not inspect.isabstract(Server)


def test_server_constructor_exists():
    assert callable(Server.__init__)


def test_server_constructor_args():
    sig = inspect.signature(Server.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_server_has_attribute():
    assert hasattr(Server, "attribute")
    descriptor = None
    for klass in Server.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_lock_doors_sensors_is_not_abstract():
    assert not inspect.isabstract(Lock_doors_sensors)


def test_lock_doors_sensors_constructor_exists():
    assert callable(Lock_doors_sensors.__init__)


def test_lock_doors_sensors_constructor_args():
    sig = inspect.signature(Lock_doors_sensors.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_lock_doors_sensors_has_attribute():
    assert hasattr(Lock_doors_sensors, "attribute")
    descriptor = None
    for klass in Lock_doors_sensors.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_light_sensor_is_not_abstract():
    assert not inspect.isabstract(Light_Sensor)


def test_light_sensor_constructor_exists():
    assert callable(Light_Sensor.__init__)


def test_light_sensor_constructor_args():
    sig = inspect.signature(Light_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_light_sensor_has_attribute():
    assert hasattr(Light_Sensor, "attribute")
    descriptor = None
    for klass in Light_Sensor.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_event_log_is_not_abstract():
    assert not inspect.isabstract(Event_Log)


def test_event_log_constructor_exists():
    assert callable(Event_Log.__init__)


def test_event_log_constructor_args():
    sig = inspect.signature(Event_Log.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_event_log_has_attribute():
    assert hasattr(Event_Log, "attribute")
    descriptor = None
    for klass in Event_Log.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_camera_sensor_is_not_abstract():
    assert not inspect.isabstract(Camera_sensor)


def test_camera_sensor_constructor_exists():
    assert callable(Camera_sensor.__init__)


def test_camera_sensor_constructor_args():
    sig = inspect.signature(Camera_sensor.__init__)
    params = list(sig.parameters.keys())
    assert "Image_ID" in params, "Missing parameter 'Image_ID'"
    assert "Video_ID" in params, "Missing parameter 'Video_ID'"

def test_camera_sensor_has_Image_ID():
    assert hasattr(Camera_sensor, "Image_ID")
    descriptor = None
    for klass in Camera_sensor.__mro__:
        if "Image_ID" in klass.__dict__:
            descriptor = klass.__dict__["Image_ID"]
            break
    assert isinstance(descriptor, property)

def test_camera_sensor_has_Video_ID():
    assert hasattr(Camera_sensor, "Video_ID")
    descriptor = None
    for klass in Camera_sensor.__mro__:
        if "Video_ID" in klass.__dict__:
            descriptor = klass.__dict__["Video_ID"]
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
Home_Security_strategy = st.builds(
    Home_Security,
)
Temperature_sensor_strategy = st.builds(
    Temperature_sensor,
    attribute=
        safe_text
)
Server_strategy = st.builds(
    Server,
    attribute=
        safe_text
)
Lock_doors_sensors_strategy = st.builds(
    Lock_doors_sensors,
    attribute=
        safe_text
)
Light_Sensor_strategy = st.builds(
    Light_Sensor,
    attribute=
        safe_text
)
Event_Log_strategy = st.builds(
    Event_Log,
    attribute=
        safe_text
)
Camera_sensor_strategy = st.builds(
    Camera_sensor,
    Image_ID=
        st.integers(),
    Video_ID=
        st.integers()
)

@given(instance=Home_Security_strategy)
@settings(max_examples=50)
def test_home_security_instantiation(instance):
    assert isinstance(instance, Home_Security)

@given(instance=Temperature_sensor_strategy)
@settings(max_examples=50)
def test_temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_sensor)



@given(instance=Temperature_sensor_strategy)
def test_temperature_sensor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Server_strategy)
@settings(max_examples=50)
def test_server_instantiation(instance):
    assert isinstance(instance, Server)



@given(instance=Server_strategy)
def test_server_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Lock_doors_sensors_strategy)
@settings(max_examples=50)
def test_lock_doors_sensors_instantiation(instance):
    assert isinstance(instance, Lock_doors_sensors)



@given(instance=Lock_doors_sensors_strategy)
def test_lock_doors_sensors_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Light_Sensor_strategy)
@settings(max_examples=50)
def test_light_sensor_instantiation(instance):
    assert isinstance(instance, Light_Sensor)



@given(instance=Light_Sensor_strategy)
def test_light_sensor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Event_Log_strategy)
@settings(max_examples=50)
def test_event_log_instantiation(instance):
    assert isinstance(instance, Event_Log)



@given(instance=Event_Log_strategy)
def test_event_log_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Camera_sensor_strategy)
@settings(max_examples=50)
def test_camera_sensor_instantiation(instance):
    assert isinstance(instance, Camera_sensor)



@given(instance=Camera_sensor_strategy)
def test_camera_sensor_Image_ID_setter(instance):
    original = instance.Image_ID
    instance.Image_ID = original
    assert instance.Image_ID == original



@given(instance=Camera_sensor_strategy)
def test_camera_sensor_Video_ID_setter(instance):
    original = instance.Video_ID
    instance.Video_ID = original
    assert instance.Video_ID == original
