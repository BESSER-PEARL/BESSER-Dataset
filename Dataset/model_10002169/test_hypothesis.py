import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HouseHolds,
    End_Of_Day,
    Start_Of_Day,
    MicroPhone,
    Lamp,
    Alert,
    Home_Security_System,
    Relay,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_households_is_not_abstract():
    assert not inspect.isabstract(HouseHolds)


def test_households_constructor_exists():
    assert callable(HouseHolds.__init__)


def test_households_constructor_args():
    sig = inspect.signature(HouseHolds.__init__)
    params = list(sig.parameters.keys())
    assert "LampLight" in params, "Missing parameter 'LampLight'"
    assert "TimeID" in params, "Missing parameter 'TimeID'"

def test_households_has_LampLight():
    assert hasattr(HouseHolds, "LampLight")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "LampLight" in klass.__dict__:
            descriptor = klass.__dict__["LampLight"]
            break
    assert isinstance(descriptor, property)

def test_households_has_TimeID():
    assert hasattr(HouseHolds, "TimeID")
    descriptor = None
    for klass in HouseHolds.__mro__:
        if "TimeID" in klass.__dict__:
            descriptor = klass.__dict__["TimeID"]
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



def test_lamp_is_not_abstract():
    assert not inspect.isabstract(Lamp)


def test_lamp_constructor_exists():
    assert callable(Lamp.__init__)


def test_lamp_constructor_args():
    sig = inspect.signature(Lamp.__init__)
    params = list(sig.parameters.keys())
    assert "LampID" in params, "Missing parameter 'LampID'"

def test_lamp_has_LampID():
    assert hasattr(Lamp, "LampID")
    descriptor = None
    for klass in Lamp.__mro__:
        if "LampID" in klass.__dict__:
            descriptor = klass.__dict__["LampID"]
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



def test_relay_is_not_abstract():
    assert not inspect.isabstract(Relay)


def test_relay_constructor_exists():
    assert callable(Relay.__init__)


def test_relay_constructor_args():
    sig = inspect.signature(Relay.__init__)
    params = list(sig.parameters.keys())
    assert "SensorType" in params, "Missing parameter 'SensorType'"
    assert "SensorID" in params, "Missing parameter 'SensorID'"

def test_relay_has_SensorType():
    assert hasattr(Relay, "SensorType")
    descriptor = None
    for klass in Relay.__mro__:
        if "SensorType" in klass.__dict__:
            descriptor = klass.__dict__["SensorType"]
            break
    assert isinstance(descriptor, property)

def test_relay_has_SensorID():
    assert hasattr(Relay, "SensorID")
    descriptor = None
    for klass in Relay.__mro__:
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
HouseHolds_strategy = st.builds(
    HouseHolds,
    LampLight=
        safe_text,
    TimeID=
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
MicroPhone_strategy = st.builds(
    MicroPhone,
    MicID=
        safe_text
)
Lamp_strategy = st.builds(
    Lamp,
    LampID=
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
Relay_strategy = st.builds(
    Relay,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
System_strategy = st.builds(
    System,
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Status=
        st.booleans()
)

@given(instance=HouseHolds_strategy)
@settings(max_examples=50)
def test_households_instantiation(instance):
    assert isinstance(instance, HouseHolds)



@given(instance=HouseHolds_strategy)
def test_households_LampLight_setter(instance):
    original = instance.LampLight
    instance.LampLight = original
    assert instance.LampLight == original



@given(instance=HouseHolds_strategy)
def test_households_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original

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

@given(instance=MicroPhone_strategy)
@settings(max_examples=50)
def test_microphone_instantiation(instance):
    assert isinstance(instance, MicroPhone)



@given(instance=MicroPhone_strategy)
def test_microphone_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original

@given(instance=Lamp_strategy)
@settings(max_examples=50)
def test_lamp_instantiation(instance):
    assert isinstance(instance, Lamp)



@given(instance=Lamp_strategy)
def test_lamp_LampID_setter(instance):
    original = instance.LampID
    instance.LampID = original
    assert instance.LampID == original

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

@given(instance=Relay_strategy)
@settings(max_examples=50)
def test_relay_instantiation(instance):
    assert isinstance(instance, Relay)



@given(instance=Relay_strategy)
def test_relay_SensorType_setter(instance):
    original = instance.SensorType
    instance.SensorType = original
    assert instance.SensorType == original



@given(instance=Relay_strategy)
def test_relay_SensorID_setter(instance):
    original = instance.SensorID
    instance.SensorID = original
    assert instance.SensorID == original

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
