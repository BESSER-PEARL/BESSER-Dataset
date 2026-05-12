import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Alert2,
    Web,
    Arduino,
    Count_people,
    Alert,
    Mobile_App,
    PressureSensor,
    Temperature_Sensor,
    Gas_Smoke_Sensor,
    Sensor,
    Firebase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alert2_is_not_abstract():
    assert not inspect.isabstract(Alert2)


def test_alert2_constructor_exists():
    assert callable(Alert2.__init__)


def test_alert2_constructor_args():
    sig = inspect.signature(Alert2.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"

def test_alert2_has_AlertID():
    assert hasattr(Alert2, "AlertID")
    descriptor = None
    for klass in Alert2.__mro__:
        if "AlertID" in klass.__dict__:
            descriptor = klass.__dict__["AlertID"]
            break
    assert isinstance(descriptor, property)



def test_web_is_not_abstract():
    assert not inspect.isabstract(Web)


def test_web_constructor_exists():
    assert callable(Web.__init__)


def test_web_constructor_args():
    sig = inspect.signature(Web.__init__)
    params = list(sig.parameters.keys())



def test_arduino_is_not_abstract():
    assert not inspect.isabstract(Arduino)


def test_arduino_constructor_exists():
    assert callable(Arduino.__init__)


def test_arduino_constructor_args():
    sig = inspect.signature(Arduino.__init__)
    params = list(sig.parameters.keys())
    assert "MicID" in params, "Missing parameter 'MicID'"

def test_arduino_has_MicID():
    assert hasattr(Arduino, "MicID")
    descriptor = None
    for klass in Arduino.__mro__:
        if "MicID" in klass.__dict__:
            descriptor = klass.__dict__["MicID"]
            break
    assert isinstance(descriptor, property)



def test_count_people_is_not_abstract():
    assert not inspect.isabstract(Count_people)


def test_count_people_constructor_exists():
    assert callable(Count_people.__init__)


def test_count_people_constructor_args():
    sig = inspect.signature(Count_people.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"

def test_count_people_has__attr():
    assert hasattr(Count_people, "_attr")
    descriptor = None
    for klass in Count_people.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)



def test_alert_is_not_abstract():
    assert not inspect.isabstract(Alert)


def test_alert_constructor_exists():
    assert callable(Alert.__init__)


def test_alert_constructor_args():
    sig = inspect.signature(Alert.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"

def test_alert_has_AlertID():
    assert hasattr(Alert, "AlertID")
    descriptor = None
    for klass in Alert.__mro__:
        if "AlertID" in klass.__dict__:
            descriptor = klass.__dict__["AlertID"]
            break
    assert isinstance(descriptor, property)



def test_mobile_app_is_not_abstract():
    assert not inspect.isabstract(Mobile_App)


def test_mobile_app_constructor_exists():
    assert callable(Mobile_App.__init__)


def test_mobile_app_constructor_args():
    sig = inspect.signature(Mobile_App.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"

def test_mobile_app_has_UserID():
    assert hasattr(Mobile_App, "UserID")
    descriptor = None
    for klass in Mobile_App.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)



def test_pressuresensor_is_not_abstract():
    assert not inspect.isabstract(PressureSensor)


def test_pressuresensor_constructor_exists():
    assert callable(PressureSensor.__init__)


def test_pressuresensor_constructor_args():
    sig = inspect.signature(PressureSensor.__init__)
    params = list(sig.parameters.keys())



def test_temperature_sensor_is_not_abstract():
    assert not inspect.isabstract(Temperature_Sensor)


def test_temperature_sensor_constructor_exists():
    assert callable(Temperature_Sensor.__init__)


def test_temperature_sensor_constructor_args():
    sig = inspect.signature(Temperature_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_gas_smoke_sensor_is_not_abstract():
    assert not inspect.isabstract(Gas_Smoke_Sensor)


def test_gas_smoke_sensor_constructor_exists():
    assert callable(Gas_Smoke_Sensor.__init__)


def test_gas_smoke_sensor_constructor_args():
    sig = inspect.signature(Gas_Smoke_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"
    assert "DispenseSprinkler" in params, "Missing parameter 'DispenseSprinkler'"

def test_gas_smoke_sensor_has_SmokeAlarm():
    assert hasattr(Gas_Smoke_Sensor, "SmokeAlarm")
    descriptor = None
    for klass in Gas_Smoke_Sensor.__mro__:
        if "SmokeAlarm" in klass.__dict__:
            descriptor = klass.__dict__["SmokeAlarm"]
            break
    assert isinstance(descriptor, property)

def test_gas_smoke_sensor_has_DispenseSprinkler():
    assert hasattr(Gas_Smoke_Sensor, "DispenseSprinkler")
    descriptor = None
    for klass in Gas_Smoke_Sensor.__mro__:
        if "DispenseSprinkler" in klass.__dict__:
            descriptor = klass.__dict__["DispenseSprinkler"]
            break
    assert isinstance(descriptor, property)



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SensorType" in params, "Missing parameter 'SensorType'"
    assert "SensorID" in params, "Missing parameter 'SensorID'"

def test_sensor_has_SensorType():
    assert hasattr(Sensor, "SensorType")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorType" in klass.__dict__:
            descriptor = klass.__dict__["SensorType"]
            break
    assert isinstance(descriptor, property)

def test_sensor_has_SensorID():
    assert hasattr(Sensor, "SensorID")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorID" in klass.__dict__:
            descriptor = klass.__dict__["SensorID"]
            break
    assert isinstance(descriptor, property)



def test_firebase_is_not_abstract():
    assert not inspect.isabstract(Firebase)


def test_firebase_constructor_exists():
    assert callable(Firebase.__init__)


def test_firebase_constructor_args():
    sig = inspect.signature(Firebase.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Update" in params, "Missing parameter 'Update'"

def test_firebase_has_Status():
    assert hasattr(Firebase, "Status")
    descriptor = None
    for klass in Firebase.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_firebase_has_Update():
    assert hasattr(Firebase, "Update")
    descriptor = None
    for klass in Firebase.__mro__:
        if "Update" in klass.__dict__:
            descriptor = klass.__dict__["Update"]
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
Alert2_strategy = st.builds(
    Alert2,
    AlertID=
        st.integers()
)
Web_strategy = st.builds(
    Web,
)
Arduino_strategy = st.builds(
    Arduino,
    MicID=
        safe_text
)
Count_people_strategy = st.builds(
    Count_people,
    _attr=
        st.integers()
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Mobile_App_strategy = st.builds(
    Mobile_App,
    UserID=
        st.integers()
)
PressureSensor_strategy = st.builds(
    PressureSensor,
)
Temperature_Sensor_strategy = st.builds(
    Temperature_Sensor,
)
Gas_Smoke_Sensor_strategy = st.builds(
    Gas_Smoke_Sensor,
    SmokeAlarm=
        st.booleans(),
    DispenseSprinkler=
        st.booleans()
)
Sensor_strategy = st.builds(
    Sensor,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
Firebase_strategy = st.builds(
    Firebase,
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Alert2_strategy)
@settings(max_examples=50)
def test_alert2_instantiation(instance):
    assert isinstance(instance, Alert2)



@given(instance=Alert2_strategy)
def test_alert2_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original

@given(instance=Web_strategy)
@settings(max_examples=50)
def test_web_instantiation(instance):
    assert isinstance(instance, Web)

@given(instance=Arduino_strategy)
@settings(max_examples=50)
def test_arduino_instantiation(instance):
    assert isinstance(instance, Arduino)



@given(instance=Arduino_strategy)
def test_arduino_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original

@given(instance=Count_people_strategy)
@settings(max_examples=50)
def test_count_people_instantiation(instance):
    assert isinstance(instance, Count_people)



@given(instance=Count_people_strategy)
def test_count_people__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original

@given(instance=Alert_strategy)
@settings(max_examples=50)
def test_alert_instantiation(instance):
    assert isinstance(instance, Alert)



@given(instance=Alert_strategy)
def test_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original

@given(instance=Mobile_App_strategy)
@settings(max_examples=50)
def test_mobile_app_instantiation(instance):
    assert isinstance(instance, Mobile_App)



@given(instance=Mobile_App_strategy)
def test_mobile_app_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=PressureSensor_strategy)
@settings(max_examples=50)
def test_pressuresensor_instantiation(instance):
    assert isinstance(instance, PressureSensor)

@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=50)
def test_temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)

@given(instance=Gas_Smoke_Sensor_strategy)
@settings(max_examples=50)
def test_gas_smoke_sensor_instantiation(instance):
    assert isinstance(instance, Gas_Smoke_Sensor)



@given(instance=Gas_Smoke_Sensor_strategy)
def test_gas_smoke_sensor_SmokeAlarm_setter(instance):
    original = instance.SmokeAlarm
    instance.SmokeAlarm = original
    assert instance.SmokeAlarm == original



@given(instance=Gas_Smoke_Sensor_strategy)
def test_gas_smoke_sensor_DispenseSprinkler_setter(instance):
    original = instance.DispenseSprinkler
    instance.DispenseSprinkler = original
    assert instance.DispenseSprinkler == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)



@given(instance=Sensor_strategy)
def test_sensor_SensorType_setter(instance):
    original = instance.SensorType
    instance.SensorType = original
    assert instance.SensorType == original



@given(instance=Sensor_strategy)
def test_sensor_SensorID_setter(instance):
    original = instance.SensorID
    instance.SensorID = original
    assert instance.SensorID == original

@given(instance=Firebase_strategy)
@settings(max_examples=50)
def test_firebase_instantiation(instance):
    assert isinstance(instance, Firebase)



@given(instance=Firebase_strategy)
def test_firebase_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Firebase_strategy)
def test_firebase_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original
