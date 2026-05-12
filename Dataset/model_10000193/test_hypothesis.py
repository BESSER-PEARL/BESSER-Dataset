import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entertainment,
    HouseHolds,
    HomeTheatre,
    TV,
    End_Of_Day,
    Start_Of_Day,
    Light,
    MicroPhone,
    Speakers,
    Camera,
    Door,
    Alert,
    Home_Security_System,
    PressureSensor,
    Motion_Sensor,
    FireAlarm_Sensor,
    Sensor,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entertainment_is_not_abstract():
    assert not inspect.isabstract(Entertainment)


def test_entertainment_constructor_exists():
    assert callable(Entertainment.__init__)


def test_entertainment_constructor_args():
    sig = inspect.signature(Entertainment.__init__)
    params = list(sig.parameters.keys())
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"

def test_entertainment_has_DeviceID():
    assert hasattr(Entertainment, "DeviceID")
    descriptor = None
    for klass in Entertainment.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)



def test_households_is_not_abstract():
    assert not inspect.isabstract(HouseHolds)


def test_households_constructor_exists():
    assert callable(HouseHolds.__init__)


def test_households_constructor_args():
    sig = inspect.signature(HouseHolds.__init__)
    params = list(sig.parameters.keys())
    assert "TimeID" in params, "Missing parameter 'TimeID'"
    assert "DishWasher" in params, "Missing parameter 'DishWasher'"
    assert "WashingMachine" in params, "Missing parameter 'WashingMachine'"
    assert "Coffee" in params, "Missing parameter 'Coffee'"
    assert "Alarm" in params, "Missing parameter 'Alarm'"

def test_households_has_TimeID():
    assert hasattr(HouseHolds, "TimeID")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "TimeID" in klass.__dict__:
            descriptor = klass.__dict__["TimeID"]
            break
    assert isinstance(descriptor, property)

def test_households_has_DishWasher():
    assert hasattr(HouseHolds, "DishWasher")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "DishWasher" in klass.__dict__:
            descriptor = klass.__dict__["DishWasher"]
            break
    assert isinstance(descriptor, property)

def test_households_has_WashingMachine():
    assert hasattr(HouseHolds, "WashingMachine")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "WashingMachine" in klass.__dict__:
            descriptor = klass.__dict__["WashingMachine"]
            break
    assert isinstance(descriptor, property)

def test_households_has_Coffee():
    assert hasattr(HouseHolds, "Coffee")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "Coffee" in klass.__dict__:
            descriptor = klass.__dict__["Coffee"]
            break
    assert isinstance(descriptor, property)

def test_households_has_Alarm():
    assert hasattr(HouseHolds, "Alarm")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "Alarm" in klass.__dict__:
            descriptor = klass.__dict__["Alarm"]
            break
    assert isinstance(descriptor, property)



def test_hometheatre_is_not_abstract():
    assert not inspect.isabstract(HomeTheatre)


def test_hometheatre_constructor_exists():
    assert callable(HomeTheatre.__init__)


def test_hometheatre_constructor_args():
    sig = inspect.signature(HomeTheatre.__init__)
    params = list(sig.parameters.keys())
    assert "HTID" in params, "Missing parameter 'HTID'"

def test_hometheatre_has_HTID():
    assert hasattr(HomeTheatre, "HTID")
    descriptor = None
    for klass in HomeTheatre.__mro__:
        if "HTID" in klass.__dict__:
            descriptor = klass.__dict__["HTID"]
            break
    assert isinstance(descriptor, property)



def test_tv_is_not_abstract():
    assert not inspect.isabstract(TV)


def test_tv_constructor_exists():
    assert callable(TV.__init__)


def test_tv_constructor_args():
    sig = inspect.signature(TV.__init__)
    params = list(sig.parameters.keys())
    assert "TVID" in params, "Missing parameter 'TVID'"

def test_tv_has_TVID():
    assert hasattr(TV, "TVID")
    descriptor = None
    for klass in TV.__mro__:
        if "TVID" in klass.__dict__:
            descriptor = klass.__dict__["TVID"]
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



def test_microphone_is_not_abstract():
    assert not inspect.isabstract(MicroPhone)


def test_microphone_constructor_exists():
    assert callable(MicroPhone.__init__)


def test_microphone_constructor_args():
    sig = inspect.signature(MicroPhone.__init__)
    params = list(sig.parameters.keys())
    assert "MicID" in params, "Missing parameter 'MicID'"

def test_microphone_has_MicID():
    assert hasattr(MicroPhone, "MicID")
    descriptor = None
    for klass in MicroPhone.__mro__:
        if "MicID" in klass.__dict__:
            descriptor = klass.__dict__["MicID"]
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



def test_door_is_not_abstract():
    assert not inspect.isabstract(Door)


def test_door_constructor_exists():
    assert callable(Door.__init__)


def test_door_constructor_args():
    sig = inspect.signature(Door.__init__)
    params = list(sig.parameters.keys())
    assert "DoorID" in params, "Missing parameter 'DoorID'"

def test_door_has_DoorID():
    assert hasattr(Door, "DoorID")
    descriptor = None
    for klass in Door.__mro__:
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



def test_pressuresensor_is_not_abstract():
    assert not inspect.isabstract(PressureSensor)


def test_pressuresensor_constructor_exists():
    assert callable(PressureSensor.__init__)


def test_pressuresensor_constructor_args():
    sig = inspect.signature(PressureSensor.__init__)
    params = list(sig.parameters.keys())



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
    assert "DispenseSprinkler" in params, "Missing parameter 'DispenseSprinkler'"
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"

def test_firealarm_sensor_has_DispenseSprinkler():
    assert hasattr(FireAlarm_Sensor, "DispenseSprinkler")
    descriptor = None
    for klass in FireAlarm_Sensor.__mro__:
        if "DispenseSprinkler" in klass.__dict__:
            descriptor = klass.__dict__["DispenseSprinkler"]
            break
    assert isinstance(descriptor, property)

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
    assert "SensorType" in params, "Missing parameter 'SensorType'"

def test_sensor_has_SensorID():
    assert hasattr(Sensor, "SensorID")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorID" in klass.__dict__:
            descriptor = klass.__dict__["SensorID"]
            break
    assert isinstance(descriptor, property)

def test_sensor_has_SensorType():
    assert hasattr(Sensor, "SensorType")
    descriptor = None
    for klass in Sensor.__mro__:
        if "SensorType" in klass.__dict__:
            descriptor = klass.__dict__["SensorType"]
            break
    assert isinstance(descriptor, property)



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "Update" in params, "Missing parameter 'Update'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_system_has_Update():
    assert hasattr(System, "Update")
    descriptor = None
    for klass in System.__mro__:
        if "Update" in klass.__dict__:
            descriptor = klass.__dict__["Update"]
            break
    assert isinstance(descriptor, property)

def test_system_has_Status():
    assert hasattr(System, "Status")
    descriptor = None
    for klass in System.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
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
Entertainment_strategy = st.builds(
    Entertainment,
    DeviceID=
        st.integers()
)
HouseHolds_strategy = st.builds(
    HouseHolds,
    TimeID=
        safe_text,
    DishWasher=
        safe_text,
    WashingMachine=
        safe_text,
    Coffee=
        safe_text,
    Alarm=
        safe_text
)
HomeTheatre_strategy = st.builds(
    HomeTheatre,
    HTID=
        safe_text
)
TV_strategy = st.builds(
    TV,
    TVID=
        st.integers()
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
        safe_text
)
MicroPhone_strategy = st.builds(
    MicroPhone,
    MicID=
        safe_text
)
Speakers_strategy = st.builds(
    Speakers,
    SpeakerID=
        st.integers()
)
Camera_strategy = st.builds(
    Camera,
    CameraID=
        st.integers()
)
Door_strategy = st.builds(
    Door,
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
PressureSensor_strategy = st.builds(
    PressureSensor,
)
Motion_Sensor_strategy = st.builds(
    Motion_Sensor,
)
FireAlarm_Sensor_strategy = st.builds(
    FireAlarm_Sensor,
    DispenseSprinkler=
        st.booleans(),
    SmokeAlarm=
        st.booleans()
)
Sensor_strategy = st.builds(
    Sensor,
    SensorID=
        st.integers(),
    SensorType=
        st.integers()
)
System_strategy = st.builds(
    System,
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Status=
        st.booleans()
)

@given(instance=Entertainment_strategy)
@settings(max_examples=50)
def test_entertainment_instantiation(instance):
    assert isinstance(instance, Entertainment)



@given(instance=Entertainment_strategy)
def test_entertainment_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original

@given(instance=HouseHolds_strategy)
@settings(max_examples=50)
def test_households_instantiation(instance):
    assert isinstance(instance, HouseHolds)



@given(instance=HouseHolds_strategy)
def test_households_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original



@given(instance=HouseHolds_strategy)
def test_households_DishWasher_setter(instance):
    original = instance.DishWasher
    instance.DishWasher = original
    assert instance.DishWasher == original



@given(instance=HouseHolds_strategy)
def test_households_WashingMachine_setter(instance):
    original = instance.WashingMachine
    instance.WashingMachine = original
    assert instance.WashingMachine == original



@given(instance=HouseHolds_strategy)
def test_households_Coffee_setter(instance):
    original = instance.Coffee
    instance.Coffee = original
    assert instance.Coffee == original



@given(instance=HouseHolds_strategy)
def test_households_Alarm_setter(instance):
    original = instance.Alarm
    instance.Alarm = original
    assert instance.Alarm == original

@given(instance=HomeTheatre_strategy)
@settings(max_examples=50)
def test_hometheatre_instantiation(instance):
    assert isinstance(instance, HomeTheatre)



@given(instance=HomeTheatre_strategy)
def test_hometheatre_HTID_setter(instance):
    original = instance.HTID
    instance.HTID = original
    assert instance.HTID == original

@given(instance=TV_strategy)
@settings(max_examples=50)
def test_tv_instantiation(instance):
    assert isinstance(instance, TV)



@given(instance=TV_strategy)
def test_tv_TVID_setter(instance):
    original = instance.TVID
    instance.TVID = original
    assert instance.TVID == original

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

@given(instance=MicroPhone_strategy)
@settings(max_examples=50)
def test_microphone_instantiation(instance):
    assert isinstance(instance, MicroPhone)



@given(instance=MicroPhone_strategy)
def test_microphone_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original

@given(instance=Speakers_strategy)
@settings(max_examples=50)
def test_speakers_instantiation(instance):
    assert isinstance(instance, Speakers)



@given(instance=Speakers_strategy)
def test_speakers_SpeakerID_setter(instance):
    original = instance.SpeakerID
    instance.SpeakerID = original
    assert instance.SpeakerID == original

@given(instance=Camera_strategy)
@settings(max_examples=50)
def test_camera_instantiation(instance):
    assert isinstance(instance, Camera)



@given(instance=Camera_strategy)
def test_camera_CameraID_setter(instance):
    original = instance.CameraID
    instance.CameraID = original
    assert instance.CameraID == original

@given(instance=Door_strategy)
@settings(max_examples=50)
def test_door_instantiation(instance):
    assert isinstance(instance, Door)



@given(instance=Door_strategy)
def test_door_DoorID_setter(instance):
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

@given(instance=PressureSensor_strategy)
@settings(max_examples=50)
def test_pressuresensor_instantiation(instance):
    assert isinstance(instance, PressureSensor)

@given(instance=Motion_Sensor_strategy)
@settings(max_examples=50)
def test_motion_sensor_instantiation(instance):
    assert isinstance(instance, Motion_Sensor)

@given(instance=FireAlarm_Sensor_strategy)
@settings(max_examples=50)
def test_firealarm_sensor_instantiation(instance):
    assert isinstance(instance, FireAlarm_Sensor)



@given(instance=FireAlarm_Sensor_strategy)
def test_firealarm_sensor_DispenseSprinkler_setter(instance):
    original = instance.DispenseSprinkler
    instance.DispenseSprinkler = original
    assert instance.DispenseSprinkler == original



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
def test_sensor_SensorType_setter(instance):
    original = instance.SensorType
    instance.SensorType = original
    assert instance.SensorType == original

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)



@given(instance=System_strategy)
def test_system_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original



@given(instance=System_strategy)
def test_system_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original
