import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserProfile,
    ROOM,
    TechSupport,
    Kitchen,
    HomeTheatre,
    End_Of_Day,
    Start_Of_Day,
    Light,
    PowerSystem,
    Speakers,
    Curtains,
    Alert,
    Security_System,
    MotionSensor,
    Sensor,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_userprofile_is_not_abstract():
    assert not inspect.isabstract(UserProfile)


def test_userprofile_constructor_exists():
    assert callable(UserProfile.__init__)


def test_userprofile_constructor_args():
    sig = inspect.signature(UserProfile.__init__)
    params = list(sig.parameters.keys())
    assert "ProfileID" in params, "Missing parameter 'ProfileID'"

def test_userprofile_has_ProfileID():
    assert hasattr(UserProfile, "ProfileID")
    descriptor = None
    for klass in UserProfile.__mro__:
        if "ProfileID" in klass.__dict__:
            descriptor = klass.__dict__["ProfileID"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(ROOM)


def test_room_constructor_exists():
    assert callable(ROOM.__init__)


def test_room_constructor_args():
    sig = inspect.signature(ROOM.__init__)
    params = list(sig.parameters.keys())
    assert "RoomID" in params, "Missing parameter 'RoomID'"

def test_room_has_RoomID():
    assert hasattr(ROOM, "RoomID")
    descriptor = None
    for klass in ROOM.__mro__:
        if "RoomID" in klass.__dict__:
            descriptor = klass.__dict__["RoomID"]
            break
    assert isinstance(descriptor, property)



def test_techsupport_is_not_abstract():
    assert not inspect.isabstract(TechSupport)


def test_techsupport_constructor_exists():
    assert callable(TechSupport.__init__)


def test_techsupport_constructor_args():
    sig = inspect.signature(TechSupport.__init__)
    params = list(sig.parameters.keys())
    assert "TechID" in params, "Missing parameter 'TechID'"

def test_techsupport_has_TechID():
    assert hasattr(TechSupport, "TechID")
    descriptor = None
    for klass in TechSupport.__mro__:
        if "TechID" in klass.__dict__:
            descriptor = klass.__dict__["TechID"]
            break
    assert isinstance(descriptor, property)



def test_kitchen_is_not_abstract():
    assert not inspect.isabstract(Kitchen)


def test_kitchen_constructor_exists():
    assert callable(Kitchen.__init__)


def test_kitchen_constructor_args():
    sig = inspect.signature(Kitchen.__init__)
    params = list(sig.parameters.keys())
    assert "TimeID" in params, "Missing parameter 'TimeID'"

def test_kitchen_has_TimeID():
    assert hasattr(Kitchen, "TimeID")
    descriptor = None
    for klass in Kitchen.__mro__:
        if "TimeID" in klass.__dict__:
            descriptor = klass.__dict__["TimeID"]
            break
    assert isinstance(descriptor, property)



def test_hometheatre_is_not_abstract():
    assert not inspect.isabstract(HomeTheatre)


def test_hometheatre_constructor_exists():
    assert callable(HomeTheatre.__init__)


def test_hometheatre_constructor_args():
    sig = inspect.signature(HomeTheatre.__init__)
    params = list(sig.parameters.keys())
    assert "SSID" in params, "Missing parameter 'SSID'"

def test_hometheatre_has_SSID():
    assert hasattr(HomeTheatre, "SSID")
    descriptor = None
    for klass in HomeTheatre.__mro__:
        if "SSID" in klass.__dict__:
            descriptor = klass.__dict__["SSID"]
            break
    assert isinstance(descriptor, property)



def test_end_of_day_is_not_abstract():
    assert not inspect.isabstract(End_Of_Day)


def test_end_of_day_constructor_exists():
    assert callable(End_Of_Day.__init__)


def test_end_of_day_constructor_args():
    sig = inspect.signature(End_Of_Day.__init__)
    params = list(sig.parameters.keys())
    assert "EOT" in params, "Missing parameter 'EOT'"

def test_end_of_day_has_EOT():
    assert hasattr(End_Of_Day, "EOT")
    descriptor = None
    for klass in End_Of_Day.__mro__:
        if "EOT" in klass.__dict__:
            descriptor = klass.__dict__["EOT"]
            break
    assert isinstance(descriptor, property)



def test_start_of_day_is_not_abstract():
    assert not inspect.isabstract(Start_Of_Day)


def test_start_of_day_constructor_exists():
    assert callable(Start_Of_Day.__init__)


def test_start_of_day_constructor_args():
    sig = inspect.signature(Start_Of_Day.__init__)
    params = list(sig.parameters.keys())
    assert "SOT" in params, "Missing parameter 'SOT'"

def test_start_of_day_has_SOT():
    assert hasattr(Start_Of_Day, "SOT")
    descriptor = None
    for klass in Start_Of_Day.__mro__:
        if "SOT" in klass.__dict__:
            descriptor = klass.__dict__["SOT"]
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



def test_powersystem_is_not_abstract():
    assert not inspect.isabstract(PowerSystem)


def test_powersystem_constructor_exists():
    assert callable(PowerSystem.__init__)


def test_powersystem_constructor_args():
    sig = inspect.signature(PowerSystem.__init__)
    params = list(sig.parameters.keys())
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"

def test_powersystem_has_DeviceID():
    assert hasattr(PowerSystem, "DeviceID")
    descriptor = None
    for klass in PowerSystem.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)



def test_speakers_is_not_abstract():
    assert not inspect.isabstract(Speakers)


def test_speakers_constructor_exists():
    assert callable(Speakers.__init__)


def test_speakers_constructor_args():
    sig = inspect.signature(Speakers.__init__)
    params = list(sig.parameters.keys())
    assert "SpeakerID" in params, "Missing parameter 'SpeakerID'"

def test_speakers_has_SpeakerID():
    assert hasattr(Speakers, "SpeakerID")
    descriptor = None
    for klass in Speakers.__mro__:
        if "SpeakerID" in klass.__dict__:
            descriptor = klass.__dict__["SpeakerID"]
            break
    assert isinstance(descriptor, property)



def test_curtains_is_not_abstract():
    assert not inspect.isabstract(Curtains)


def test_curtains_constructor_exists():
    assert callable(Curtains.__init__)


def test_curtains_constructor_args():
    sig = inspect.signature(Curtains.__init__)
    params = list(sig.parameters.keys())
    assert "CurtaiunID" in params, "Missing parameter 'CurtaiunID'"

def test_curtains_has_CurtaiunID():
    assert hasattr(Curtains, "CurtaiunID")
    descriptor = None
    for klass in Curtains.__mro__:
        if "CurtaiunID" in klass.__dict__:
            descriptor = klass.__dict__["CurtaiunID"]
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



def test_security_system_is_not_abstract():
    assert not inspect.isabstract(Security_System)


def test_security_system_constructor_exists():
    assert callable(Security_System.__init__)


def test_security_system_constructor_args():
    sig = inspect.signature(Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"

def test_security_system_has_UserID():
    assert hasattr(Security_System, "UserID")
    descriptor = None
    for klass in Security_System.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)



def test_motionsensor_is_not_abstract():
    assert not inspect.isabstract(MotionSensor)


def test_motionsensor_constructor_exists():
    assert callable(MotionSensor.__init__)


def test_motionsensor_constructor_args():
    sig = inspect.signature(MotionSensor.__init__)
    params = list(sig.parameters.keys())



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



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Update" in params, "Missing parameter 'Update'"

def test_system_has_Status():
    assert hasattr(System, "Status")
    descriptor = None
    for klass in System.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_system_has_Update():
    assert hasattr(System, "Update")
    descriptor = None
    for klass in System.__mro__:
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
UserProfile_strategy = st.builds(
    UserProfile,
    ProfileID=
        st.integers()
)
ROOM_strategy = st.builds(
    ROOM,
    RoomID=
        safe_text
)
TechSupport_strategy = st.builds(
    TechSupport,
    TechID=
        st.integers()
)
Kitchen_strategy = st.builds(
    Kitchen,
    TimeID=
        safe_text
)
HomeTheatre_strategy = st.builds(
    HomeTheatre,
    SSID=
        safe_text
)
End_Of_Day_strategy = st.builds(
    End_Of_Day,
    EOT=
        st.integers()
)
Start_Of_Day_strategy = st.builds(
    Start_Of_Day,
    SOT=
        st.integers()
)
Light_strategy = st.builds(
    Light,
    LightID=
        st.integers()
)
PowerSystem_strategy = st.builds(
    PowerSystem,
    DeviceID=
        st.integers()
)
Speakers_strategy = st.builds(
    Speakers,
    SpeakerID=
        st.integers()
)
Curtains_strategy = st.builds(
    Curtains,
    CurtaiunID=
        st.integers()
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Security_System_strategy = st.builds(
    Security_System,
    UserID=
        st.integers()
)
MotionSensor_strategy = st.builds(
    MotionSensor,
)
Sensor_strategy = st.builds(
    Sensor,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
System_strategy = st.builds(
    System,
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=UserProfile_strategy)
@settings(max_examples=50)
def test_userprofile_instantiation(instance):
    assert isinstance(instance, UserProfile)



@given(instance=UserProfile_strategy)
def test_userprofile_ProfileID_setter(instance):
    original = instance.ProfileID
    instance.ProfileID = original
    assert instance.ProfileID == original

@given(instance=ROOM_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, ROOM)



@given(instance=ROOM_strategy)
def test_room_RoomID_setter(instance):
    original = instance.RoomID
    instance.RoomID = original
    assert instance.RoomID == original

@given(instance=TechSupport_strategy)
@settings(max_examples=50)
def test_techsupport_instantiation(instance):
    assert isinstance(instance, TechSupport)



@given(instance=TechSupport_strategy)
def test_techsupport_TechID_setter(instance):
    original = instance.TechID
    instance.TechID = original
    assert instance.TechID == original

@given(instance=Kitchen_strategy)
@settings(max_examples=50)
def test_kitchen_instantiation(instance):
    assert isinstance(instance, Kitchen)



@given(instance=Kitchen_strategy)
def test_kitchen_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original

@given(instance=HomeTheatre_strategy)
@settings(max_examples=50)
def test_hometheatre_instantiation(instance):
    assert isinstance(instance, HomeTheatre)



@given(instance=HomeTheatre_strategy)
def test_hometheatre_SSID_setter(instance):
    original = instance.SSID
    instance.SSID = original
    assert instance.SSID == original

@given(instance=End_Of_Day_strategy)
@settings(max_examples=50)
def test_end_of_day_instantiation(instance):
    assert isinstance(instance, End_Of_Day)



@given(instance=End_Of_Day_strategy)
def test_end_of_day_EOT_setter(instance):
    original = instance.EOT
    instance.EOT = original
    assert instance.EOT == original

@given(instance=Start_Of_Day_strategy)
@settings(max_examples=50)
def test_start_of_day_instantiation(instance):
    assert isinstance(instance, Start_Of_Day)



@given(instance=Start_Of_Day_strategy)
def test_start_of_day_SOT_setter(instance):
    original = instance.SOT
    instance.SOT = original
    assert instance.SOT == original

@given(instance=Light_strategy)
@settings(max_examples=50)
def test_light_instantiation(instance):
    assert isinstance(instance, Light)



@given(instance=Light_strategy)
def test_light_LightID_setter(instance):
    original = instance.LightID
    instance.LightID = original
    assert instance.LightID == original

@given(instance=PowerSystem_strategy)
@settings(max_examples=50)
def test_powersystem_instantiation(instance):
    assert isinstance(instance, PowerSystem)



@given(instance=PowerSystem_strategy)
def test_powersystem_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original

@given(instance=Speakers_strategy)
@settings(max_examples=50)
def test_speakers_instantiation(instance):
    assert isinstance(instance, Speakers)



@given(instance=Speakers_strategy)
def test_speakers_SpeakerID_setter(instance):
    original = instance.SpeakerID
    instance.SpeakerID = original
    assert instance.SpeakerID == original

@given(instance=Curtains_strategy)
@settings(max_examples=50)
def test_curtains_instantiation(instance):
    assert isinstance(instance, Curtains)



@given(instance=Curtains_strategy)
def test_curtains_CurtaiunID_setter(instance):
    original = instance.CurtaiunID
    instance.CurtaiunID = original
    assert instance.CurtaiunID == original

@given(instance=Alert_strategy)
@settings(max_examples=50)
def test_alert_instantiation(instance):
    assert isinstance(instance, Alert)



@given(instance=Alert_strategy)
def test_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original

@given(instance=Security_System_strategy)
@settings(max_examples=50)
def test_security_system_instantiation(instance):
    assert isinstance(instance, Security_System)



@given(instance=Security_System_strategy)
def test_security_system_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=MotionSensor_strategy)
@settings(max_examples=50)
def test_motionsensor_instantiation(instance):
    assert isinstance(instance, MotionSensor)

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

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)



@given(instance=System_strategy)
def test_system_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=System_strategy)
def test_system_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original
