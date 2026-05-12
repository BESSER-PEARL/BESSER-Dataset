import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    View_sensors_data_external,
    Sense_and_Update_Data_external,
    Close_Alarm_external,
    Add_new_alarm_external,
    Notify_User_of_fire_external,
    Sensors_Actor,
    Fire_Department__Actor,
    Building_Owner__Actor,
    Fire_Alarm_System__Component,
    Web,
    Arduino,
    Count_Sensor,
    Mobile_App,
    Temperature_Sensor,
    Gas_Smoke_Sensor,
    Sensor,
    Firebase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_view_sensors_data_external_is_not_abstract():
    assert not inspect.isabstract(View_sensors_data_external)


def test_view_sensors_data_external_constructor_exists():
    assert callable(View_sensors_data_external.__init__)


def test_view_sensors_data_external_constructor_args():
    sig = inspect.signature(View_sensors_data_external.__init__)
    params = list(sig.parameters.keys())



def test_sense_and_update_data_external_is_not_abstract():
    assert not inspect.isabstract(Sense_and_Update_Data_external)


def test_sense_and_update_data_external_constructor_exists():
    assert callable(Sense_and_Update_Data_external.__init__)


def test_sense_and_update_data_external_constructor_args():
    sig = inspect.signature(Sense_and_Update_Data_external.__init__)
    params = list(sig.parameters.keys())



def test_close_alarm_external_is_not_abstract():
    assert not inspect.isabstract(Close_Alarm_external)


def test_close_alarm_external_constructor_exists():
    assert callable(Close_Alarm_external.__init__)


def test_close_alarm_external_constructor_args():
    sig = inspect.signature(Close_Alarm_external.__init__)
    params = list(sig.parameters.keys())



def test_add_new_alarm_external_is_not_abstract():
    assert not inspect.isabstract(Add_new_alarm_external)


def test_add_new_alarm_external_constructor_exists():
    assert callable(Add_new_alarm_external.__init__)


def test_add_new_alarm_external_constructor_args():
    sig = inspect.signature(Add_new_alarm_external.__init__)
    params = list(sig.parameters.keys())



def test_notify_user_of_fire_external_is_not_abstract():
    assert not inspect.isabstract(Notify_User_of_fire_external)


def test_notify_user_of_fire_external_constructor_exists():
    assert callable(Notify_User_of_fire_external.__init__)


def test_notify_user_of_fire_external_constructor_args():
    sig = inspect.signature(Notify_User_of_fire_external.__init__)
    params = list(sig.parameters.keys())



def test_sensors_actor_is_not_abstract():
    assert not inspect.isabstract(Sensors_Actor)


def test_sensors_actor_constructor_exists():
    assert callable(Sensors_Actor.__init__)


def test_sensors_actor_constructor_args():
    sig = inspect.signature(Sensors_Actor.__init__)
    params = list(sig.parameters.keys())



def test_fire_department__actor_is_not_abstract():
    assert not inspect.isabstract(Fire_Department__Actor)


def test_fire_department__actor_constructor_exists():
    assert callable(Fire_Department__Actor.__init__)


def test_fire_department__actor_constructor_args():
    sig = inspect.signature(Fire_Department__Actor.__init__)
    params = list(sig.parameters.keys())



def test_building_owner__actor_is_not_abstract():
    assert not inspect.isabstract(Building_Owner__Actor)


def test_building_owner__actor_constructor_exists():
    assert callable(Building_Owner__Actor.__init__)


def test_building_owner__actor_constructor_args():
    sig = inspect.signature(Building_Owner__Actor.__init__)
    params = list(sig.parameters.keys())



def test_fire_alarm_system__component_is_not_abstract():
    assert not inspect.isabstract(Fire_Alarm_System__Component)


def test_fire_alarm_system__component_constructor_exists():
    assert callable(Fire_Alarm_System__Component.__init__)


def test_fire_alarm_system__component_constructor_args():
    sig = inspect.signature(Fire_Alarm_System__Component.__init__)
    params = list(sig.parameters.keys())



def test_web_is_not_abstract():
    assert not inspect.isabstract(Web)


def test_web_constructor_exists():
    assert callable(Web.__init__)


def test_web_constructor_args():
    sig = inspect.signature(Web.__init__)
    params = list(sig.parameters.keys())
    assert "SmokeValue" in params, "Missing parameter 'SmokeValue'"
    assert "People_" in params, "Missing parameter 'People_'"
    assert "OwnerData" in params, "Missing parameter 'OwnerData'"
    assert "TempValue" in params, "Missing parameter 'TempValue'"
    assert "HomeLoc" in params, "Missing parameter 'HomeLoc'"

def test_web_has_SmokeValue():
    assert hasattr(Web, "SmokeValue")
    descriptor = None
    for klass in Web.__mro__:
        if "SmokeValue" in klass.__dict__:
            descriptor = klass.__dict__["SmokeValue"]
            break
    assert isinstance(descriptor, property)

def test_web_has_People_():
    assert hasattr(Web, "People_")
    descriptor = None
    for klass in Web.__mro__:
        if "People_" in klass.__dict__:
            descriptor = klass.__dict__["People_"]
            break
    assert isinstance(descriptor, property)

def test_web_has_OwnerData():
    assert hasattr(Web, "OwnerData")
    descriptor = None
    for klass in Web.__mro__:
        if "OwnerData" in klass.__dict__:
            descriptor = klass.__dict__["OwnerData"]
            break
    assert isinstance(descriptor, property)

def test_web_has_TempValue():
    assert hasattr(Web, "TempValue")
    descriptor = None
    for klass in Web.__mro__:
        if "TempValue" in klass.__dict__:
            descriptor = klass.__dict__["TempValue"]
            break
    assert isinstance(descriptor, property)

def test_web_has_HomeLoc():
    assert hasattr(Web, "HomeLoc")
    descriptor = None
    for klass in Web.__mro__:
        if "HomeLoc" in klass.__dict__:
            descriptor = klass.__dict__["HomeLoc"]
            break
    assert isinstance(descriptor, property)



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



def test_count_sensor_is_not_abstract():
    assert not inspect.isabstract(Count_Sensor)


def test_count_sensor_constructor_exists():
    assert callable(Count_Sensor.__init__)


def test_count_sensor_constructor_args():
    sig = inspect.signature(Count_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "People_" in params, "Missing parameter 'People_'"

def test_count_sensor_has_People_():
    assert hasattr(Count_Sensor, "People_")
    descriptor = None
    for klass in Count_Sensor.__mro__:
        if "People_" in klass.__dict__:
            descriptor = klass.__dict__["People_"]
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
    assert "AlarmID" in params, "Missing parameter 'AlarmID'"

def test_mobile_app_has_UserID():
    assert hasattr(Mobile_App, "UserID")
    descriptor = None
    for klass in Mobile_App.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_mobile_app_has_AlarmID():
    assert hasattr(Mobile_App, "AlarmID")
    descriptor = None
    for klass in Mobile_App.__mro__:
        if "AlarmID" in klass.__dict__:
            descriptor = klass.__dict__["AlarmID"]
            break
    assert isinstance(descriptor, property)



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
    assert "CheckSmoke" in params, "Missing parameter 'CheckSmoke'"
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"

def test_gas_smoke_sensor_has_CheckSmoke():
    assert hasattr(Gas_Smoke_Sensor, "CheckSmoke")
    descriptor = None
    for klass in Gas_Smoke_Sensor.__mro__:
        if "CheckSmoke" in klass.__dict__:
            descriptor = klass.__dict__["CheckSmoke"]
            break
    assert isinstance(descriptor, property)

def test_gas_smoke_sensor_has_SmokeAlarm():
    assert hasattr(Gas_Smoke_Sensor, "SmokeAlarm")
    descriptor = None
    for klass in Gas_Smoke_Sensor.__mro__:
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
View_sensors_data_external_strategy = st.builds(
    View_sensors_data_external,
)
Sense_and_Update_Data_external_strategy = st.builds(
    Sense_and_Update_Data_external,
)
Close_Alarm_external_strategy = st.builds(
    Close_Alarm_external,
)
Add_new_alarm_external_strategy = st.builds(
    Add_new_alarm_external,
)
Notify_User_of_fire_external_strategy = st.builds(
    Notify_User_of_fire_external,
)
Sensors_Actor_strategy = st.builds(
    Sensors_Actor,
)
Fire_Department__Actor_strategy = st.builds(
    Fire_Department__Actor,
)
Building_Owner__Actor_strategy = st.builds(
    Building_Owner__Actor,
)
Fire_Alarm_System__Component_strategy = st.builds(
    Fire_Alarm_System__Component,
)
Web_strategy = st.builds(
    Web,
    SmokeValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    People_=
        st.integers(),
    OwnerData=
        safe_text,
    TempValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    HomeLoc=
        safe_text
)
Arduino_strategy = st.builds(
    Arduino,
    MicID=
        safe_text
)
Count_Sensor_strategy = st.builds(
    Count_Sensor,
    People_=
        st.integers()
)
Mobile_App_strategy = st.builds(
    Mobile_App,
    UserID=
        st.integers(),
    AlarmID=
        st.integers()
)
Temperature_Sensor_strategy = st.builds(
    Temperature_Sensor,
)
Gas_Smoke_Sensor_strategy = st.builds(
    Gas_Smoke_Sensor,
    CheckSmoke=
        st.booleans(),
    SmokeAlarm=
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
)

@given(instance=View_sensors_data_external_strategy)
@settings(max_examples=50)
def test_view_sensors_data_external_instantiation(instance):
    assert isinstance(instance, View_sensors_data_external)

@given(instance=Sense_and_Update_Data_external_strategy)
@settings(max_examples=50)
def test_sense_and_update_data_external_instantiation(instance):
    assert isinstance(instance, Sense_and_Update_Data_external)

@given(instance=Close_Alarm_external_strategy)
@settings(max_examples=50)
def test_close_alarm_external_instantiation(instance):
    assert isinstance(instance, Close_Alarm_external)

@given(instance=Add_new_alarm_external_strategy)
@settings(max_examples=50)
def test_add_new_alarm_external_instantiation(instance):
    assert isinstance(instance, Add_new_alarm_external)

@given(instance=Notify_User_of_fire_external_strategy)
@settings(max_examples=50)
def test_notify_user_of_fire_external_instantiation(instance):
    assert isinstance(instance, Notify_User_of_fire_external)

@given(instance=Sensors_Actor_strategy)
@settings(max_examples=50)
def test_sensors_actor_instantiation(instance):
    assert isinstance(instance, Sensors_Actor)

@given(instance=Fire_Department__Actor_strategy)
@settings(max_examples=50)
def test_fire_department__actor_instantiation(instance):
    assert isinstance(instance, Fire_Department__Actor)

@given(instance=Building_Owner__Actor_strategy)
@settings(max_examples=50)
def test_building_owner__actor_instantiation(instance):
    assert isinstance(instance, Building_Owner__Actor)

@given(instance=Fire_Alarm_System__Component_strategy)
@settings(max_examples=50)
def test_fire_alarm_system__component_instantiation(instance):
    assert isinstance(instance, Fire_Alarm_System__Component)

@given(instance=Web_strategy)
@settings(max_examples=50)
def test_web_instantiation(instance):
    assert isinstance(instance, Web)



@given(instance=Web_strategy)
def test_web_SmokeValue_setter(instance):
    original = instance.SmokeValue
    instance.SmokeValue = original
    assert instance.SmokeValue == original



@given(instance=Web_strategy)
def test_web_People__setter(instance):
    original = instance.People_
    instance.People_ = original
    assert instance.People_ == original



@given(instance=Web_strategy)
def test_web_OwnerData_setter(instance):
    original = instance.OwnerData
    instance.OwnerData = original
    assert instance.OwnerData == original



@given(instance=Web_strategy)
def test_web_TempValue_setter(instance):
    original = instance.TempValue
    instance.TempValue = original
    assert instance.TempValue == original



@given(instance=Web_strategy)
def test_web_HomeLoc_setter(instance):
    original = instance.HomeLoc
    instance.HomeLoc = original
    assert instance.HomeLoc == original

@given(instance=Arduino_strategy)
@settings(max_examples=50)
def test_arduino_instantiation(instance):
    assert isinstance(instance, Arduino)



@given(instance=Arduino_strategy)
def test_arduino_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original

@given(instance=Count_Sensor_strategy)
@settings(max_examples=50)
def test_count_sensor_instantiation(instance):
    assert isinstance(instance, Count_Sensor)



@given(instance=Count_Sensor_strategy)
def test_count_sensor_People__setter(instance):
    original = instance.People_
    instance.People_ = original
    assert instance.People_ == original

@given(instance=Mobile_App_strategy)
@settings(max_examples=50)
def test_mobile_app_instantiation(instance):
    assert isinstance(instance, Mobile_App)



@given(instance=Mobile_App_strategy)
def test_mobile_app_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Mobile_App_strategy)
def test_mobile_app_AlarmID_setter(instance):
    original = instance.AlarmID
    instance.AlarmID = original
    assert instance.AlarmID == original

@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=50)
def test_temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)

@given(instance=Gas_Smoke_Sensor_strategy)
@settings(max_examples=50)
def test_gas_smoke_sensor_instantiation(instance):
    assert isinstance(instance, Gas_Smoke_Sensor)



@given(instance=Gas_Smoke_Sensor_strategy)
def test_gas_smoke_sensor_CheckSmoke_setter(instance):
    original = instance.CheckSmoke
    instance.CheckSmoke = original
    assert instance.CheckSmoke == original



@given(instance=Gas_Smoke_Sensor_strategy)
def test_gas_smoke_sensor_SmokeAlarm_setter(instance):
    original = instance.SmokeAlarm
    instance.SmokeAlarm = original
    assert instance.SmokeAlarm == original

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
