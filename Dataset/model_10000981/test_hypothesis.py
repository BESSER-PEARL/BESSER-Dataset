import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Lock_doors_sensors,
    Light_PIR_Sensor,
    Event_Log,
    Camera_sensor,
    Door_Security,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_light_pir_sensor_is_not_abstract():
    assert not inspect.isabstract(Light_PIR_Sensor)


def test_light_pir_sensor_constructor_exists():
    assert callable(Light_PIR_Sensor.__init__)


def test_light_pir_sensor_constructor_args():
    sig = inspect.signature(Light_PIR_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_light_pir_sensor_has_attribute():
    assert hasattr(Light_PIR_Sensor, "attribute")
    descriptor = None
    for klass in Light_PIR_Sensor.__mro__:
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
    assert "Video_ID" in params, "Missing parameter 'Video_ID'"
    assert "Image_ID" in params, "Missing parameter 'Image_ID'"

def test_camera_sensor_has_Video_ID():
    assert hasattr(Camera_sensor, "Video_ID")
    descriptor = None
    for klass in Camera_sensor.__mro__:
        if "Video_ID" in klass.__dict__:
            descriptor = klass.__dict__["Video_ID"]
            break
    assert isinstance(descriptor, property)

def test_camera_sensor_has_Image_ID():
    assert hasattr(Camera_sensor, "Image_ID")
    descriptor = None
    for klass in Camera_sensor.__mro__:
        if "Image_ID" in klass.__dict__:
            descriptor = klass.__dict__["Image_ID"]
            break
    assert isinstance(descriptor, property)



def test_door_security_is_not_abstract():
    assert not inspect.isabstract(Door_Security)


def test_door_security_constructor_exists():
    assert callable(Door_Security.__init__)


def test_door_security_constructor_args():
    sig = inspect.signature(Door_Security.__init__)
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
Lock_doors_sensors_strategy = st.builds(
    Lock_doors_sensors,
    attribute=
        safe_text
)
Light_PIR_Sensor_strategy = st.builds(
    Light_PIR_Sensor,
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
    Video_ID=
        st.integers(),
    Image_ID=
        st.integers()
)
Door_Security_strategy = st.builds(
    Door_Security,
)

@given(instance=Lock_doors_sensors_strategy)
@settings(max_examples=50)
def test_lock_doors_sensors_instantiation(instance):
    assert isinstance(instance, Lock_doors_sensors)



@given(instance=Lock_doors_sensors_strategy)
def test_lock_doors_sensors_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Light_PIR_Sensor_strategy)
@settings(max_examples=50)
def test_light_pir_sensor_instantiation(instance):
    assert isinstance(instance, Light_PIR_Sensor)



@given(instance=Light_PIR_Sensor_strategy)
def test_light_pir_sensor_attribute_setter(instance):
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
def test_camera_sensor_Video_ID_setter(instance):
    original = instance.Video_ID
    instance.Video_ID = original
    assert instance.Video_ID == original



@given(instance=Camera_sensor_strategy)
def test_camera_sensor_Image_ID_setter(instance):
    original = instance.Image_ID
    instance.Image_ID = original
    assert instance.Image_ID == original

@given(instance=Door_Security_strategy)
@settings(max_examples=50)
def test_door_security_instantiation(instance):
    assert isinstance(instance, Door_Security)
