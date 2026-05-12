import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Newsfeed,
    HomeAutomation,
    Light,
    Voice_control,
    Camera,
    Door_Sensor,
    Alert,
    Home_Security_System,
    Motion_Sensor,
    FireAlarm_Sensor,
    Sensor,
    Smart_mirror,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_newsfeed_is_not_abstract():
    assert not inspect.isabstract(Newsfeed)


def test_newsfeed_constructor_exists():
    assert callable(Newsfeed.__init__)


def test_newsfeed_constructor_args():
    sig = inspect.signature(Newsfeed.__init__)
    params = list(sig.parameters.keys())
    assert "Weather" in params, "Missing parameter 'Weather'"
    assert "News" in params, "Missing parameter 'News'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Calendar" in params, "Missing parameter 'Calendar'"
    assert "Phone" in params, "Missing parameter 'Phone'"

def test_newsfeed_has_Weather():
    assert hasattr(Newsfeed, "Weather")
    descriptor = None
    for klass in Newsfeed.__mro__:
        if "Weather" in klass.__dict__:
            descriptor = klass.__dict__["Weather"]
            break
    assert isinstance(descriptor, property)

def test_newsfeed_has_News():
    assert hasattr(Newsfeed, "News")
    descriptor = None
    for klass in Newsfeed.__mro__:
        if "News" in klass.__dict__:
            descriptor = klass.__dict__["News"]
            break
    assert isinstance(descriptor, property)

def test_newsfeed_has_Email():
    assert hasattr(Newsfeed, "Email")
    descriptor = None
    for klass in Newsfeed.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_newsfeed_has_Calendar():
    assert hasattr(Newsfeed, "Calendar")
    descriptor = None
    for klass in Newsfeed.__mro__:
        if "Calendar" in klass.__dict__:
            descriptor = klass.__dict__["Calendar"]
            break
    assert isinstance(descriptor, property)

def test_newsfeed_has_Phone():
    assert hasattr(Newsfeed, "Phone")
    descriptor = None
    for klass in Newsfeed.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)



def test_homeautomation_is_not_abstract():
    assert not inspect.isabstract(HomeAutomation)


def test_homeautomation_constructor_exists():
    assert callable(HomeAutomation.__init__)


def test_homeautomation_constructor_args():
    sig = inspect.signature(HomeAutomation.__init__)
    params = list(sig.parameters.keys())
    assert "Lights" in params, "Missing parameter 'Lights'"
    assert "Apllicances" in params, "Missing parameter 'Apllicances'"

def test_homeautomation_has_Lights():
    assert hasattr(HomeAutomation, "Lights")
    descriptor = None
    for klass in HomeAutomation.__mro__:
        if "Lights" in klass.__dict__:
            descriptor = klass.__dict__["Lights"]
            break
    assert isinstance(descriptor, property)

def test_homeautomation_has_Apllicances():
    assert hasattr(HomeAutomation, "Apllicances")
    descriptor = None
    for klass in HomeAutomation.__mro__:
        if "Apllicances" in klass.__dict__:
            descriptor = klass.__dict__["Apllicances"]
            break
    assert isinstance(descriptor, property)



def test_light_is_not_abstract():
    assert not inspect.isabstract(Light)


def test_light_constructor_exists():
    assert callable(Light.__init__)


def test_light_constructor_args():
    sig = inspect.signature(Light.__init__)
    params = list(sig.parameters.keys())
    assert "LightID" in params, "Missing parameter 'LightID'"

def test_light_has_LightID():
    assert hasattr(Light, "LightID")
    descriptor = None
    for klass in Light.__mro__:
        if "LightID" in klass.__dict__:
            descriptor = klass.__dict__["LightID"]
            break
    assert isinstance(descriptor, property)



def test_voice_control_is_not_abstract():
    assert not inspect.isabstract(Voice_control)


def test_voice_control_constructor_exists():
    assert callable(Voice_control.__init__)


def test_voice_control_constructor_args():
    sig = inspect.signature(Voice_control.__init__)
    params = list(sig.parameters.keys())
    assert "MicID" in params, "Missing parameter 'MicID'"

def test_voice_control_has_MicID():
    assert hasattr(Voice_control, "MicID")
    descriptor = None
    for klass in Voice_control.__mro__:
        if "MicID" in klass.__dict__:
            descriptor = klass.__dict__["MicID"]
            break
    assert isinstance(descriptor, property)



def test_camera_is_not_abstract():
    assert not inspect.isabstract(Camera)


def test_camera_constructor_exists():
    assert callable(Camera.__init__)


def test_camera_constructor_args():
    sig = inspect.signature(Camera.__init__)
    params = list(sig.parameters.keys())
    assert "CameraID" in params, "Missing parameter 'CameraID'"

def test_camera_has_CameraID():
    assert hasattr(Camera, "CameraID")
    descriptor = None
    for klass in Camera.__mro__:
        if "CameraID" in klass.__dict__:
            descriptor = klass.__dict__["CameraID"]
            break
    assert isinstance(descriptor, property)



def test_door_sensor_is_not_abstract():
    assert not inspect.isabstract(Door_Sensor)


def test_door_sensor_constructor_exists():
    assert callable(Door_Sensor.__init__)


def test_door_sensor_constructor_args():
    sig = inspect.signature(Door_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "DoorID" in params, "Missing parameter 'DoorID'"

def test_door_sensor_has_DoorID():
    assert hasattr(Door_Sensor, "DoorID")
    descriptor = None
    for klass in Door_Sensor.__mro__:
        if "DoorID" in klass.__dict__:
            descriptor = klass.__dict__["DoorID"]
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



def test_home_security_system_is_not_abstract():
    assert not inspect.isabstract(Home_Security_System)


def test_home_security_system_constructor_exists():
    assert callable(Home_Security_System.__init__)


def test_home_security_system_constructor_args():
    sig = inspect.signature(Home_Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"

def test_home_security_system_has_UserID():
    assert hasattr(Home_Security_System, "UserID")
    descriptor = None
    for klass in Home_Security_System.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)



def test_motion_sensor_is_not_abstract():
    assert not inspect.isabstract(Motion_Sensor)


def test_motion_sensor_constructor_exists():
    assert callable(Motion_Sensor.__init__)


def test_motion_sensor_constructor_args():
    sig = inspect.signature(Motion_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_firealarm_sensor_is_not_abstract():
    assert not inspect.isabstract(FireAlarm_Sensor)


def test_firealarm_sensor_constructor_exists():
    assert callable(FireAlarm_Sensor.__init__)


def test_firealarm_sensor_constructor_args():
    sig = inspect.signature(FireAlarm_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"

def test_firealarm_sensor_has_SmokeAlarm():
    assert hasattr(FireAlarm_Sensor, "SmokeAlarm")
    descriptor = None
    for klass in FireAlarm_Sensor.__mro__:
        if "SmokeAlarm" in klass.__dict__:
            descriptor = klass.__dict__["SmokeAlarm"]
            break
    assert isinstance(descriptor, property)



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SensorID" in params, "Missing parameter 'SensorID'"
    assert "SensorName" in params, "Missing parameter 'SensorName'"

def test_sensor_has_SensorID():
    assert hasattr(Sensor, "SensorID")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorID" in klass.__dict__:
            descriptor = klass.__dict__["SensorID"]
            break
    assert isinstance(descriptor, property)

def test_sensor_has_SensorName():
    assert hasattr(Sensor, "SensorName")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorName" in klass.__dict__:
            descriptor = klass.__dict__["SensorName"]
            break
    assert isinstance(descriptor, property)



def test_smart_mirror_is_not_abstract():
    assert not inspect.isabstract(Smart_mirror)


def test_smart_mirror_constructor_exists():
    assert callable(Smart_mirror.__init__)


def test_smart_mirror_constructor_args():
    sig = inspect.signature(Smart_mirror.__init__)
    params = list(sig.parameters.keys())
    assert "Display_newsfeed" in params, "Missing parameter 'Display_newsfeed'"
    assert "PhoneConnect" in params, "Missing parameter 'PhoneConnect'"
    assert "security" in params, "Missing parameter 'security'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Update" in params, "Missing parameter 'Update'"

def test_smart_mirror_has_Display_newsfeed():
    assert hasattr(Smart_mirror, "Display_newsfeed")
    descriptor = None
    for klass in Smart_mirror.__mro__:
        if "Display_newsfeed" in klass.__dict__:
            descriptor = klass.__dict__["Display_newsfeed"]
            break
    assert isinstance(descriptor, property)

def test_smart_mirror_has_PhoneConnect():
    assert hasattr(Smart_mirror, "PhoneConnect")
    descriptor = None
    for klass in Smart_mirror.__mro__:
        if "PhoneConnect" in klass.__dict__:
            descriptor = klass.__dict__["PhoneConnect"]
            break
    assert isinstance(descriptor, property)

def test_smart_mirror_has_security():
    assert hasattr(Smart_mirror, "security")
    descriptor = None
    for klass in Smart_mirror.__mro__:
        if "security" in klass.__dict__:
            descriptor = klass.__dict__["security"]
            break
    assert isinstance(descriptor, property)

def test_smart_mirror_has_Status():
    assert hasattr(Smart_mirror, "Status")
    descriptor = None
    for klass in Smart_mirror.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_smart_mirror_has_Update():
    assert hasattr(Smart_mirror, "Update")
    descriptor = None
    for klass in Smart_mirror.__mro__:
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
Newsfeed_strategy = st.builds(
    Newsfeed,
    Weather=
        safe_text,
    News=
        safe_text,
    Email=
        safe_text,
    Calendar=
        safe_text,
    Phone=
        safe_text
)
HomeAutomation_strategy = st.builds(
    HomeAutomation,
    Lights=
        safe_text,
    Apllicances=
        safe_text
)
Light_strategy = st.builds(
    Light,
    LightID=
        safe_text
)
Voice_control_strategy = st.builds(
    Voice_control,
    MicID=
        safe_text
)
Camera_strategy = st.builds(
    Camera,
    CameraID=
        st.integers()
)
Door_Sensor_strategy = st.builds(
    Door_Sensor,
    DoorID=
        st.integers()
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Home_Security_System_strategy = st.builds(
    Home_Security_System,
    UserID=
        st.integers()
)
Motion_Sensor_strategy = st.builds(
    Motion_Sensor,
)
FireAlarm_Sensor_strategy = st.builds(
    FireAlarm_Sensor,
    SmokeAlarm=
        st.booleans()
)
Sensor_strategy = st.builds(
    Sensor,
    SensorID=
        st.integers(),
    SensorName=
        st.integers()
)
Smart_mirror_strategy = st.builds(
    Smart_mirror,
    Display_newsfeed=
        st.none(),
    PhoneConnect=
        st.booleans(),
    security=
        st.none(),
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Newsfeed_strategy)
@settings(max_examples=50)
def test_newsfeed_instantiation(instance):
    assert isinstance(instance, Newsfeed)



@given(instance=Newsfeed_strategy)
def test_newsfeed_Weather_setter(instance):
    original = instance.Weather
    instance.Weather = original
    assert instance.Weather == original



@given(instance=Newsfeed_strategy)
def test_newsfeed_News_setter(instance):
    original = instance.News
    instance.News = original
    assert instance.News == original



@given(instance=Newsfeed_strategy)
def test_newsfeed_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Newsfeed_strategy)
def test_newsfeed_Calendar_setter(instance):
    original = instance.Calendar
    instance.Calendar = original
    assert instance.Calendar == original



@given(instance=Newsfeed_strategy)
def test_newsfeed_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original

@given(instance=HomeAutomation_strategy)
@settings(max_examples=50)
def test_homeautomation_instantiation(instance):
    assert isinstance(instance, HomeAutomation)



@given(instance=HomeAutomation_strategy)
def test_homeautomation_Lights_setter(instance):
    original = instance.Lights
    instance.Lights = original
    assert instance.Lights == original



@given(instance=HomeAutomation_strategy)
def test_homeautomation_Apllicances_setter(instance):
    original = instance.Apllicances
    instance.Apllicances = original
    assert instance.Apllicances == original

@given(instance=Light_strategy)
@settings(max_examples=50)
def test_light_instantiation(instance):
    assert isinstance(instance, Light)



@given(instance=Light_strategy)
def test_light_LightID_setter(instance):
    original = instance.LightID
    instance.LightID = original
    assert instance.LightID == original

@given(instance=Voice_control_strategy)
@settings(max_examples=50)
def test_voice_control_instantiation(instance):
    assert isinstance(instance, Voice_control)



@given(instance=Voice_control_strategy)
def test_voice_control_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original

@given(instance=Camera_strategy)
@settings(max_examples=50)
def test_camera_instantiation(instance):
    assert isinstance(instance, Camera)



@given(instance=Camera_strategy)
def test_camera_CameraID_setter(instance):
    original = instance.CameraID
    instance.CameraID = original
    assert instance.CameraID == original

@given(instance=Door_Sensor_strategy)
@settings(max_examples=50)
def test_door_sensor_instantiation(instance):
    assert isinstance(instance, Door_Sensor)



@given(instance=Door_Sensor_strategy)
def test_door_sensor_DoorID_setter(instance):
    original = instance.DoorID
    instance.DoorID = original
    assert instance.DoorID == original

@given(instance=Alert_strategy)
@settings(max_examples=50)
def test_alert_instantiation(instance):
    assert isinstance(instance, Alert)



@given(instance=Alert_strategy)
def test_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original

@given(instance=Home_Security_System_strategy)
@settings(max_examples=50)
def test_home_security_system_instantiation(instance):
    assert isinstance(instance, Home_Security_System)



@given(instance=Home_Security_System_strategy)
def test_home_security_system_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=Motion_Sensor_strategy)
@settings(max_examples=50)
def test_motion_sensor_instantiation(instance):
    assert isinstance(instance, Motion_Sensor)

@given(instance=FireAlarm_Sensor_strategy)
@settings(max_examples=50)
def test_firealarm_sensor_instantiation(instance):
    assert isinstance(instance, FireAlarm_Sensor)



@given(instance=FireAlarm_Sensor_strategy)
def test_firealarm_sensor_SmokeAlarm_setter(instance):
    original = instance.SmokeAlarm
    instance.SmokeAlarm = original
    assert instance.SmokeAlarm == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)



@given(instance=Sensor_strategy)
def test_sensor_SensorID_setter(instance):
    original = instance.SensorID
    instance.SensorID = original
    assert instance.SensorID == original



@given(instance=Sensor_strategy)
def test_sensor_SensorName_setter(instance):
    original = instance.SensorName
    instance.SensorName = original
    assert instance.SensorName == original

@given(instance=Smart_mirror_strategy)
@settings(max_examples=50)
def test_smart_mirror_instantiation(instance):
    assert isinstance(instance, Smart_mirror)



@given(instance=Smart_mirror_strategy)
def test_smart_mirror_Display_newsfeed_setter(instance):
    original = instance.Display_newsfeed
    instance.Display_newsfeed = original
    assert instance.Display_newsfeed == original



@given(instance=Smart_mirror_strategy)
def test_smart_mirror_PhoneConnect_setter(instance):
    original = instance.PhoneConnect
    instance.PhoneConnect = original
    assert instance.PhoneConnect == original



@given(instance=Smart_mirror_strategy)
def test_smart_mirror_security_setter(instance):
    original = instance.security
    instance.security = original
    assert instance.security == original



@given(instance=Smart_mirror_strategy)
def test_smart_mirror_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Smart_mirror_strategy)
def test_smart_mirror_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original
