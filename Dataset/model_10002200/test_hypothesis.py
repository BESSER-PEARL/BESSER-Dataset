import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FloorCoordinates,
    Segment,
    FloorPlan,
    ActivationCode,
    Home_Theatre,
    Television,
    Home_Entertainment_Devices,
    HeatAirConditioning,
    Lights,
    Telephone_Answering_machine,
    Camera,
    Alarm_Signaler,
    Sensor,
    Automation_System,
    Device_Configuration,
    securitySystem,
    config,
    SAFE_HOME_SYSTEM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_floorcoordinates_is_not_abstract():
    assert not inspect.isabstract(FloorCoordinates)


def test_floorcoordinates_constructor_exists():
    assert callable(FloorCoordinates.__init__)


def test_floorcoordinates_constructor_args():
    sig = inspect.signature(FloorCoordinates.__init__)
    params = list(sig.parameters.keys())
    assert "XcoordinatePosition" in params, "Missing parameter 'XcoordinatePosition'"
    assert "YcoordinatePosition" in params, "Missing parameter 'YcoordinatePosition'"

def test_floorcoordinates_has_XcoordinatePosition():
    assert hasattr(FloorCoordinates, "XcoordinatePosition")
    descriptor = None
    for klass in FloorCoordinates.__mro__:
        if "XcoordinatePosition" in klass.__dict__:
            descriptor = klass.__dict__["XcoordinatePosition"]
            break
    assert isinstance(descriptor, property)

def test_floorcoordinates_has_YcoordinatePosition():
    assert hasattr(FloorCoordinates, "YcoordinatePosition")
    descriptor = None
    for klass in FloorCoordinates.__mro__:
        if "YcoordinatePosition" in klass.__dict__:
            descriptor = klass.__dict__["YcoordinatePosition"]
            break
    assert isinstance(descriptor, property)



def test_segment_is_not_abstract():
    assert not inspect.isabstract(Segment)


def test_segment_constructor_exists():
    assert callable(Segment.__init__)


def test_segment_constructor_args():
    sig = inspect.signature(Segment.__init__)
    params = list(sig.parameters.keys())



def test_floorplan_is_not_abstract():
    assert not inspect.isabstract(FloorPlan)


def test_floorplan_constructor_exists():
    assert callable(FloorPlan.__init__)


def test_floorplan_constructor_args():
    sig = inspect.signature(FloorPlan.__init__)
    params = list(sig.parameters.keys())
    assert "floorName" in params, "Missing parameter 'floorName'"

def test_floorplan_has_floorName():
    assert hasattr(FloorPlan, "floorName")
    descriptor = None
    for klass in FloorPlan.__mro__:
        if "floorName" in klass.__dict__:
            descriptor = klass.__dict__["floorName"]
            break
    assert isinstance(descriptor, property)



def test_activationcode_is_not_abstract():
    assert not inspect.isabstract(ActivationCode)


def test_activationcode_constructor_exists():
    assert callable(ActivationCode.__init__)


def test_activationcode_constructor_args():
    sig = inspect.signature(ActivationCode.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_activationcode_has_code():
    assert hasattr(ActivationCode, "code")
    descriptor = None
    for klass in ActivationCode.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_home_theatre_is_not_abstract():
    assert not inspect.isabstract(Home_Theatre)


def test_home_theatre_constructor_exists():
    assert callable(Home_Theatre.__init__)


def test_home_theatre_constructor_args():
    sig = inspect.signature(Home_Theatre.__init__)
    params = list(sig.parameters.keys())
    assert "companyName" in params, "Missing parameter 'companyName'"

def test_home_theatre_has_companyName():
    assert hasattr(Home_Theatre, "companyName")
    descriptor = None
    for klass in Home_Theatre.__mro__:
        if "companyName" in klass.__dict__:
            descriptor = klass.__dict__["companyName"]
            break
    assert isinstance(descriptor, property)



def test_television_is_not_abstract():
    assert not inspect.isabstract(Television)


def test_television_constructor_exists():
    assert callable(Television.__init__)


def test_television_constructor_args():
    sig = inspect.signature(Television.__init__)
    params = list(sig.parameters.keys())
    assert "companyName" in params, "Missing parameter 'companyName'"

def test_television_has_companyName():
    assert hasattr(Television, "companyName")
    descriptor = None
    for klass in Television.__mro__:
        if "companyName" in klass.__dict__:
            descriptor = klass.__dict__["companyName"]
            break
    assert isinstance(descriptor, property)



def test_home_entertainment_devices_is_not_abstract():
    assert not inspect.isabstract(Home_Entertainment_Devices)


def test_home_entertainment_devices_constructor_exists():
    assert callable(Home_Entertainment_Devices.__init__)


def test_home_entertainment_devices_constructor_args():
    sig = inspect.signature(Home_Entertainment_Devices.__init__)
    params = list(sig.parameters.keys())



def test_heatairconditioning_is_not_abstract():
    assert not inspect.isabstract(HeatAirConditioning)


def test_heatairconditioning_constructor_exists():
    assert callable(HeatAirConditioning.__init__)


def test_heatairconditioning_constructor_args():
    sig = inspect.signature(HeatAirConditioning.__init__)
    params = list(sig.parameters.keys())
    assert "voltage" in params, "Missing parameter 'voltage'"

def test_heatairconditioning_has_voltage():
    assert hasattr(HeatAirConditioning, "voltage")
    descriptor = None
    for klass in HeatAirConditioning.__mro__:
        if "voltage" in klass.__dict__:
            descriptor = klass.__dict__["voltage"]
            break
    assert isinstance(descriptor, property)



def test_lights_is_not_abstract():
    assert not inspect.isabstract(Lights)


def test_lights_constructor_exists():
    assert callable(Lights.__init__)


def test_lights_constructor_args():
    sig = inspect.signature(Lights.__init__)
    params = list(sig.parameters.keys())
    assert "brightness" in params, "Missing parameter 'brightness'"

def test_lights_has_brightness():
    assert hasattr(Lights, "brightness")
    descriptor = None
    for klass in Lights.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)



def test_telephone_answering_machine_is_not_abstract():
    assert not inspect.isabstract(Telephone_Answering_machine)


def test_telephone_answering_machine_constructor_exists():
    assert callable(Telephone_Answering_machine.__init__)


def test_telephone_answering_machine_constructor_args():
    sig = inspect.signature(Telephone_Answering_machine.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_telephone_answering_machine_has_number():
    assert hasattr(Telephone_Answering_machine, "number")
    descriptor = None
    for klass in Telephone_Answering_machine.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_camera_is_not_abstract():
    assert not inspect.isabstract(Camera)


def test_camera_constructor_exists():
    assert callable(Camera.__init__)


def test_camera_constructor_args():
    sig = inspect.signature(Camera.__init__)
    params = list(sig.parameters.keys())
    assert "panAngle" in params, "Missing parameter 'panAngle'"
    assert "zoomSetting" in params, "Missing parameter 'zoomSetting'"

def test_camera_has_panAngle():
    assert hasattr(Camera, "panAngle")
    descriptor = None
    for klass in Camera.__mro__:
        if "panAngle" in klass.__dict__:
            descriptor = klass.__dict__["panAngle"]
            break
    assert isinstance(descriptor, property)

def test_camera_has_zoomSetting():
    assert hasattr(Camera, "zoomSetting")
    descriptor = None
    for klass in Camera.__mro__:
        if "zoomSetting" in klass.__dict__:
            descriptor = klass.__dict__["zoomSetting"]
            break
    assert isinstance(descriptor, property)



def test_alarm_signaler_is_not_abstract():
    assert not inspect.isabstract(Alarm_Signaler)


def test_alarm_signaler_constructor_exists():
    assert callable(Alarm_Signaler.__init__)


def test_alarm_signaler_constructor_args():
    sig = inspect.signature(Alarm_Signaler.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_alarm_signaler_has_frequency():
    assert hasattr(Alarm_Signaler, "frequency")
    descriptor = None
    for klass in Alarm_Signaler.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "detectingAnomaly" in params, "Missing parameter 'detectingAnomaly'"

def test_sensor_has_detectingAnomaly():
    assert hasattr(Sensor, "detectingAnomaly")
    descriptor = None
    for klass in Sensor.__mro__:
        if "detectingAnomaly" in klass.__dict__:
            descriptor = klass.__dict__["detectingAnomaly"]
            break
    assert isinstance(descriptor, property)



def test_automation_system_is_not_abstract():
    assert not inspect.isabstract(Automation_System)


def test_automation_system_constructor_exists():
    assert callable(Automation_System.__init__)


def test_automation_system_constructor_args():
    sig = inspect.signature(Automation_System.__init__)
    params = list(sig.parameters.keys())



def test_device_configuration_is_not_abstract():
    assert not inspect.isabstract(Device_Configuration)


def test_device_configuration_constructor_exists():
    assert callable(Device_Configuration.__init__)


def test_device_configuration_constructor_args():
    sig = inspect.signature(Device_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "alarmIfoff" in params, "Missing parameter 'alarmIfoff'"
    assert "activeOnAway" in params, "Missing parameter 'activeOnAway'"
    assert "activeOnStay" in params, "Missing parameter 'activeOnStay'"
    assert "zone" in params, "Missing parameter 'zone'"

def test_device_configuration_has_alarmIfoff():
    assert hasattr(Device_Configuration, "alarmIfoff")
    descriptor = None
    for klass in Device_Configuration.__mro__:
        if "alarmIfoff" in klass.__dict__:
            descriptor = klass.__dict__["alarmIfoff"]
            break
    assert isinstance(descriptor, property)

def test_device_configuration_has_activeOnAway():
    assert hasattr(Device_Configuration, "activeOnAway")
    descriptor = None
    for klass in Device_Configuration.__mro__:
        if "activeOnAway" in klass.__dict__:
            descriptor = klass.__dict__["activeOnAway"]
            break
    assert isinstance(descriptor, property)

def test_device_configuration_has_activeOnStay():
    assert hasattr(Device_Configuration, "activeOnStay")
    descriptor = None
    for klass in Device_Configuration.__mro__:
        if "activeOnStay" in klass.__dict__:
            descriptor = klass.__dict__["activeOnStay"]
            break
    assert isinstance(descriptor, property)

def test_device_configuration_has_zone():
    assert hasattr(Device_Configuration, "zone")
    descriptor = None
    for klass in Device_Configuration.__mro__:
        if "zone" in klass.__dict__:
            descriptor = klass.__dict__["zone"]
            break
    assert isinstance(descriptor, property)



def test_securitysystem_is_not_abstract():
    assert not inspect.isabstract(securitySystem)


def test_securitysystem_constructor_exists():
    assert callable(securitySystem.__init__)


def test_securitysystem_constructor_args():
    sig = inspect.signature(securitySystem.__init__)
    params = list(sig.parameters.keys())



def test_config_is_not_abstract():
    assert not inspect.isabstract(config)


def test_config_constructor_exists():
    assert callable(config.__init__)


def test_config_constructor_args():
    sig = inspect.signature(config.__init__)
    params = list(sig.parameters.keys())
    assert "configurationName" in params, "Missing parameter 'configurationName'"

def test_config_has_configurationName():
    assert hasattr(config, "configurationName")
    descriptor = None
    for klass in config.__mro__:
        if "configurationName" in klass.__dict__:
            descriptor = klass.__dict__["configurationName"]
            break
    assert isinstance(descriptor, property)



def test_safe_home_system_is_not_abstract():
    assert not inspect.isabstract(SAFE_HOME_SYSTEM)


def test_safe_home_system_constructor_exists():
    assert callable(SAFE_HOME_SYSTEM.__init__)


def test_safe_home_system_constructor_args():
    sig = inspect.signature(SAFE_HOME_SYSTEM.__init__)
    params = list(sig.parameters.keys())
    assert "activationState" in params, "Missing parameter 'activationState'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "streetAddress" in params, "Missing parameter 'streetAddress'"
    assert "masterPwd" in params, "Missing parameter 'masterPwd'"

def test_safe_home_system_has_activationState():
    assert hasattr(SAFE_HOME_SYSTEM, "activationState")
    descriptor = None
    for klass in SAFE_HOME_SYSTEM.__mro__:
        if "activationState" in klass.__dict__:
            descriptor = klass.__dict__["activationState"]
            break
    assert isinstance(descriptor, property)

def test_safe_home_system_has_userId():
    assert hasattr(SAFE_HOME_SYSTEM, "userId")
    descriptor = None
    for klass in SAFE_HOME_SYSTEM.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_safe_home_system_has_streetAddress():
    assert hasattr(SAFE_HOME_SYSTEM, "streetAddress")
    descriptor = None
    for klass in SAFE_HOME_SYSTEM.__mro__:
        if "streetAddress" in klass.__dict__:
            descriptor = klass.__dict__["streetAddress"]
            break
    assert isinstance(descriptor, property)

def test_safe_home_system_has_masterPwd():
    assert hasattr(SAFE_HOME_SYSTEM, "masterPwd")
    descriptor = None
    for klass in SAFE_HOME_SYSTEM.__mro__:
        if "masterPwd" in klass.__dict__:
            descriptor = klass.__dict__["masterPwd"]
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
FloorCoordinates_strategy = st.builds(
    FloorCoordinates,
    XcoordinatePosition=
        st.integers(),
    YcoordinatePosition=
        st.integers()
)
Segment_strategy = st.builds(
    Segment,
)
FloorPlan_strategy = st.builds(
    FloorPlan,
    floorName=
        safe_text
)
ActivationCode_strategy = st.builds(
    ActivationCode,
    code=
        st.integers()
)
Home_Theatre_strategy = st.builds(
    Home_Theatre,
    companyName=
        safe_text
)
Television_strategy = st.builds(
    Television,
    companyName=
        safe_text
)
Home_Entertainment_Devices_strategy = st.builds(
    Home_Entertainment_Devices,
)
HeatAirConditioning_strategy = st.builds(
    HeatAirConditioning,
    voltage=
        st.integers()
)
Lights_strategy = st.builds(
    Lights,
    brightness=
        st.integers()
)
Telephone_Answering_machine_strategy = st.builds(
    Telephone_Answering_machine,
    number=
        st.integers()
)
Camera_strategy = st.builds(
    Camera,
    panAngle=
        st.integers(),
    zoomSetting=
        st.integers()
)
Alarm_Signaler_strategy = st.builds(
    Alarm_Signaler,
    frequency=
        st.integers()
)
Sensor_strategy = st.builds(
    Sensor,
    detectingAnomaly=
        st.booleans()
)
Automation_System_strategy = st.builds(
    Automation_System,
)
Device_Configuration_strategy = st.builds(
    Device_Configuration,
    alarmIfoff=
        st.booleans(),
    activeOnAway=
        st.booleans(),
    activeOnStay=
        st.booleans(),
    zone=
        st.integers()
)
securitySystem_strategy = st.builds(
    securitySystem,
)
config_strategy = st.builds(
    config,
    configurationName=
        safe_text
)
SAFE_HOME_SYSTEM_strategy = st.builds(
    SAFE_HOME_SYSTEM,
    activationState=
        safe_text,
    userId=
        safe_text,
    streetAddress=
        safe_text,
    masterPwd=
        safe_text
)

@given(instance=FloorCoordinates_strategy)
@settings(max_examples=50)
def test_floorcoordinates_instantiation(instance):
    assert isinstance(instance, FloorCoordinates)



@given(instance=FloorCoordinates_strategy)
def test_floorcoordinates_XcoordinatePosition_setter(instance):
    original = instance.XcoordinatePosition
    instance.XcoordinatePosition = original
    assert instance.XcoordinatePosition == original



@given(instance=FloorCoordinates_strategy)
def test_floorcoordinates_YcoordinatePosition_setter(instance):
    original = instance.YcoordinatePosition
    instance.YcoordinatePosition = original
    assert instance.YcoordinatePosition == original

@given(instance=Segment_strategy)
@settings(max_examples=50)
def test_segment_instantiation(instance):
    assert isinstance(instance, Segment)

@given(instance=FloorPlan_strategy)
@settings(max_examples=50)
def test_floorplan_instantiation(instance):
    assert isinstance(instance, FloorPlan)



@given(instance=FloorPlan_strategy)
def test_floorplan_floorName_setter(instance):
    original = instance.floorName
    instance.floorName = original
    assert instance.floorName == original

@given(instance=ActivationCode_strategy)
@settings(max_examples=50)
def test_activationcode_instantiation(instance):
    assert isinstance(instance, ActivationCode)



@given(instance=ActivationCode_strategy)
def test_activationcode_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Home_Theatre_strategy)
@settings(max_examples=50)
def test_home_theatre_instantiation(instance):
    assert isinstance(instance, Home_Theatre)



@given(instance=Home_Theatre_strategy)
def test_home_theatre_companyName_setter(instance):
    original = instance.companyName
    instance.companyName = original
    assert instance.companyName == original

@given(instance=Television_strategy)
@settings(max_examples=50)
def test_television_instantiation(instance):
    assert isinstance(instance, Television)



@given(instance=Television_strategy)
def test_television_companyName_setter(instance):
    original = instance.companyName
    instance.companyName = original
    assert instance.companyName == original

@given(instance=Home_Entertainment_Devices_strategy)
@settings(max_examples=50)
def test_home_entertainment_devices_instantiation(instance):
    assert isinstance(instance, Home_Entertainment_Devices)

@given(instance=HeatAirConditioning_strategy)
@settings(max_examples=50)
def test_heatairconditioning_instantiation(instance):
    assert isinstance(instance, HeatAirConditioning)



@given(instance=HeatAirConditioning_strategy)
def test_heatairconditioning_voltage_setter(instance):
    original = instance.voltage
    instance.voltage = original
    assert instance.voltage == original

@given(instance=Lights_strategy)
@settings(max_examples=50)
def test_lights_instantiation(instance):
    assert isinstance(instance, Lights)



@given(instance=Lights_strategy)
def test_lights_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=Telephone_Answering_machine_strategy)
@settings(max_examples=50)
def test_telephone_answering_machine_instantiation(instance):
    assert isinstance(instance, Telephone_Answering_machine)



@given(instance=Telephone_Answering_machine_strategy)
def test_telephone_answering_machine_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Camera_strategy)
@settings(max_examples=50)
def test_camera_instantiation(instance):
    assert isinstance(instance, Camera)



@given(instance=Camera_strategy)
def test_camera_panAngle_setter(instance):
    original = instance.panAngle
    instance.panAngle = original
    assert instance.panAngle == original



@given(instance=Camera_strategy)
def test_camera_zoomSetting_setter(instance):
    original = instance.zoomSetting
    instance.zoomSetting = original
    assert instance.zoomSetting == original

@given(instance=Alarm_Signaler_strategy)
@settings(max_examples=50)
def test_alarm_signaler_instantiation(instance):
    assert isinstance(instance, Alarm_Signaler)



@given(instance=Alarm_Signaler_strategy)
def test_alarm_signaler_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)



@given(instance=Sensor_strategy)
def test_sensor_detectingAnomaly_setter(instance):
    original = instance.detectingAnomaly
    instance.detectingAnomaly = original
    assert instance.detectingAnomaly == original

@given(instance=Automation_System_strategy)
@settings(max_examples=50)
def test_automation_system_instantiation(instance):
    assert isinstance(instance, Automation_System)

@given(instance=Device_Configuration_strategy)
@settings(max_examples=50)
def test_device_configuration_instantiation(instance):
    assert isinstance(instance, Device_Configuration)



@given(instance=Device_Configuration_strategy)
def test_device_configuration_alarmIfoff_setter(instance):
    original = instance.alarmIfoff
    instance.alarmIfoff = original
    assert instance.alarmIfoff == original



@given(instance=Device_Configuration_strategy)
def test_device_configuration_activeOnAway_setter(instance):
    original = instance.activeOnAway
    instance.activeOnAway = original
    assert instance.activeOnAway == original



@given(instance=Device_Configuration_strategy)
def test_device_configuration_activeOnStay_setter(instance):
    original = instance.activeOnStay
    instance.activeOnStay = original
    assert instance.activeOnStay == original



@given(instance=Device_Configuration_strategy)
def test_device_configuration_zone_setter(instance):
    original = instance.zone
    instance.zone = original
    assert instance.zone == original

@given(instance=securitySystem_strategy)
@settings(max_examples=50)
def test_securitysystem_instantiation(instance):
    assert isinstance(instance, securitySystem)

@given(instance=config_strategy)
@settings(max_examples=50)
def test_config_instantiation(instance):
    assert isinstance(instance, config)



@given(instance=config_strategy)
def test_config_configurationName_setter(instance):
    original = instance.configurationName
    instance.configurationName = original
    assert instance.configurationName == original

@given(instance=SAFE_HOME_SYSTEM_strategy)
@settings(max_examples=50)
def test_safe_home_system_instantiation(instance):
    assert isinstance(instance, SAFE_HOME_SYSTEM)



@given(instance=SAFE_HOME_SYSTEM_strategy)
def test_safe_home_system_activationState_setter(instance):
    original = instance.activationState
    instance.activationState = original
    assert instance.activationState == original



@given(instance=SAFE_HOME_SYSTEM_strategy)
def test_safe_home_system_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=SAFE_HOME_SYSTEM_strategy)
def test_safe_home_system_streetAddress_setter(instance):
    original = instance.streetAddress
    instance.streetAddress = original
    assert instance.streetAddress == original



@given(instance=SAFE_HOME_SYSTEM_strategy)
def test_safe_home_system_masterPwd_setter(instance):
    original = instance.masterPwd
    instance.masterPwd = original
    assert instance.masterPwd == original
