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
    WebPage,
    Alarm,
    ViewTemp_Smoke,
    AddAlarm,
    TurnDownAlarm,
    Sensors_Actor,
    Fire_Department__Actor,
    Building_Owner__Actor,
    Fire_Alarm_System__Component,
    Arduino,
    Count_Sensor,
    Notification,
    MobileApp,
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



def test_webpage_is_not_abstract():
    assert not inspect.isabstract(WebPage)


def test_webpage_constructor_exists():
    assert callable(WebPage.__init__)


def test_webpage_constructor_args():
    sig = inspect.signature(WebPage.__init__)
    params = list(sig.parameters.keys())



def test_alarm_is_not_abstract():
    assert not inspect.isabstract(Alarm)


def test_alarm_constructor_exists():
    assert callable(Alarm.__init__)


def test_alarm_constructor_args():
    sig = inspect.signature(Alarm.__init__)
    params = list(sig.parameters.keys())



def test_viewtemp_smoke_is_not_abstract():
    assert not inspect.isabstract(ViewTemp_Smoke)


def test_viewtemp_smoke_constructor_exists():
    assert callable(ViewTemp_Smoke.__init__)


def test_viewtemp_smoke_constructor_args():
    sig = inspect.signature(ViewTemp_Smoke.__init__)
    params = list(sig.parameters.keys())



def test_addalarm_is_not_abstract():
    assert not inspect.isabstract(AddAlarm)


def test_addalarm_constructor_exists():
    assert callable(AddAlarm.__init__)


def test_addalarm_constructor_args():
    sig = inspect.signature(AddAlarm.__init__)
    params = list(sig.parameters.keys())



def test_turndownalarm_is_not_abstract():
    assert not inspect.isabstract(TurnDownAlarm)


def test_turndownalarm_constructor_exists():
    assert callable(TurnDownAlarm.__init__)


def test_turndownalarm_constructor_args():
    sig = inspect.signature(TurnDownAlarm.__init__)
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



def test_arduino_is_not_abstract():
    assert not inspect.isabstract(Arduino)


def test_arduino_constructor_exists():
    assert callable(Arduino.__init__)


def test_arduino_constructor_args():
    sig = inspect.signature(Arduino.__init__)
    params = list(sig.parameters.keys())



def test_count_sensor_is_not_abstract():
    assert not inspect.isabstract(Count_Sensor)


def test_count_sensor_constructor_exists():
    assert callable(Count_Sensor.__init__)


def test_count_sensor_constructor_args():
    sig = inspect.signature(Count_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_notification_is_not_abstract():
    assert not inspect.isabstract(Notification)


def test_notification_constructor_exists():
    assert callable(Notification.__init__)


def test_notification_constructor_args():
    sig = inspect.signature(Notification.__init__)
    params = list(sig.parameters.keys())



def test_mobileapp_is_not_abstract():
    assert not inspect.isabstract(MobileApp)


def test_mobileapp_constructor_exists():
    assert callable(MobileApp.__init__)


def test_mobileapp_constructor_args():
    sig = inspect.signature(MobileApp.__init__)
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



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



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
WebPage_strategy = st.builds(
    WebPage,
)
Alarm_strategy = st.builds(
    Alarm,
)
ViewTemp_Smoke_strategy = st.builds(
    ViewTemp_Smoke,
)
AddAlarm_strategy = st.builds(
    AddAlarm,
)
TurnDownAlarm_strategy = st.builds(
    TurnDownAlarm,
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
Arduino_strategy = st.builds(
    Arduino,
)
Count_Sensor_strategy = st.builds(
    Count_Sensor,
)
Notification_strategy = st.builds(
    Notification,
)
MobileApp_strategy = st.builds(
    MobileApp,
)
Temperature_Sensor_strategy = st.builds(
    Temperature_Sensor,
)
Gas_Smoke_Sensor_strategy = st.builds(
    Gas_Smoke_Sensor,
)
Sensor_strategy = st.builds(
    Sensor,
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

@given(instance=WebPage_strategy)
@settings(max_examples=50)
def test_webpage_instantiation(instance):
    assert isinstance(instance, WebPage)

@given(instance=Alarm_strategy)
@settings(max_examples=50)
def test_alarm_instantiation(instance):
    assert isinstance(instance, Alarm)

@given(instance=ViewTemp_Smoke_strategy)
@settings(max_examples=50)
def test_viewtemp_smoke_instantiation(instance):
    assert isinstance(instance, ViewTemp_Smoke)

@given(instance=AddAlarm_strategy)
@settings(max_examples=50)
def test_addalarm_instantiation(instance):
    assert isinstance(instance, AddAlarm)

@given(instance=TurnDownAlarm_strategy)
@settings(max_examples=50)
def test_turndownalarm_instantiation(instance):
    assert isinstance(instance, TurnDownAlarm)

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

@given(instance=Arduino_strategy)
@settings(max_examples=50)
def test_arduino_instantiation(instance):
    assert isinstance(instance, Arduino)

@given(instance=Count_Sensor_strategy)
@settings(max_examples=50)
def test_count_sensor_instantiation(instance):
    assert isinstance(instance, Count_Sensor)

@given(instance=Notification_strategy)
@settings(max_examples=50)
def test_notification_instantiation(instance):
    assert isinstance(instance, Notification)

@given(instance=MobileApp_strategy)
@settings(max_examples=50)
def test_mobileapp_instantiation(instance):
    assert isinstance(instance, MobileApp)

@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=50)
def test_temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)

@given(instance=Gas_Smoke_Sensor_strategy)
@settings(max_examples=50)
def test_gas_smoke_sensor_instantiation(instance):
    assert isinstance(instance, Gas_Smoke_Sensor)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=Firebase_strategy)
@settings(max_examples=50)
def test_firebase_instantiation(instance):
    assert isinstance(instance, Firebase)
