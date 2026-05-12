import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FireAlarm,
    securityAlarm,
    Police,
    smokeAlarm,
    Department,
    Home_Security_System,
    Fire_Alarm_system,
    Appliances,
    system,
    Login,
    Owner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_firealarm_is_not_abstract():
    assert not inspect.isabstract(FireAlarm)


def test_firealarm_constructor_exists():
    assert callable(FireAlarm.__init__)


def test_firealarm_constructor_args():
    sig = inspect.signature(FireAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_firealarm_has_status():
    assert hasattr(FireAlarm, "status")
    descriptor = None
    for klass in FireAlarm.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_securityalarm_is_not_abstract():
    assert not inspect.isabstract(securityAlarm)


def test_securityalarm_constructor_exists():
    assert callable(securityAlarm.__init__)


def test_securityalarm_constructor_args():
    sig = inspect.signature(securityAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_securityalarm_has_status():
    assert hasattr(securityAlarm, "status")
    descriptor = None
    for klass in securityAlarm.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_police_is_not_abstract():
    assert not inspect.isabstract(Police)


def test_police_constructor_exists():
    assert callable(Police.__init__)


def test_police_constructor_args():
    sig = inspect.signature(Police.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_police_has_name():
    assert hasattr(Police, "name")
    descriptor = None
    for klass in Police.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smokealarm_is_not_abstract():
    assert not inspect.isabstract(smokeAlarm)


def test_smokealarm_constructor_exists():
    assert callable(smokeAlarm.__init__)


def test_smokealarm_constructor_args():
    sig = inspect.signature(smokeAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_smokealarm_has_status():
    assert hasattr(smokeAlarm, "status")
    descriptor = None
    for klass in smokeAlarm.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_department_has_name():
    assert hasattr(Department, "name")
    descriptor = None
    for klass in Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_home_security_system_is_not_abstract():
    assert not inspect.isabstract(Home_Security_System)


def test_home_security_system_constructor_exists():
    assert callable(Home_Security_System.__init__)


def test_home_security_system_constructor_args():
    sig = inspect.signature(Home_Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "system_Off" in params, "Missing parameter 'system_Off'"
    assert "system_On" in params, "Missing parameter 'system_On'"

def test_home_security_system_has_system_Off():
    assert hasattr(Home_Security_System, "system_Off")
    descriptor = None
    for klass in Home_Security_System.__mro__:
        if "system_Off" in klass.__dict__:
            descriptor = klass.__dict__["system_Off"]
            break
    assert isinstance(descriptor, property)

def test_home_security_system_has_system_On():
    assert hasattr(Home_Security_System, "system_On")
    descriptor = None
    for klass in Home_Security_System.__mro__:
        if "system_On" in klass.__dict__:
            descriptor = klass.__dict__["system_On"]
            break
    assert isinstance(descriptor, property)



def test_fire_alarm_system_is_not_abstract():
    assert not inspect.isabstract(Fire_Alarm_system)


def test_fire_alarm_system_constructor_exists():
    assert callable(Fire_Alarm_system.__init__)


def test_fire_alarm_system_constructor_args():
    sig = inspect.signature(Fire_Alarm_system.__init__)
    params = list(sig.parameters.keys())
    assert "system_Off" in params, "Missing parameter 'system_Off'"
    assert "system_On" in params, "Missing parameter 'system_On'"

def test_fire_alarm_system_has_system_Off():
    assert hasattr(Fire_Alarm_system, "system_Off")
    descriptor = None
    for klass in Fire_Alarm_system.__mro__:
        if "system_Off" in klass.__dict__:
            descriptor = klass.__dict__["system_Off"]
            break
    assert isinstance(descriptor, property)

def test_fire_alarm_system_has_system_On():
    assert hasattr(Fire_Alarm_system, "system_On")
    descriptor = None
    for klass in Fire_Alarm_system.__mro__:
        if "system_On" in klass.__dict__:
            descriptor = klass.__dict__["system_On"]
            break
    assert isinstance(descriptor, property)



def test_appliances_is_not_abstract():
    assert not inspect.isabstract(Appliances)


def test_appliances_constructor_exists():
    assert callable(Appliances.__init__)


def test_appliances_constructor_args():
    sig = inspect.signature(Appliances.__init__)
    params = list(sig.parameters.keys())
    assert "Off_status" in params, "Missing parameter 'Off_status'"
    assert "On_status" in params, "Missing parameter 'On_status'"

def test_appliances_has_Off_status():
    assert hasattr(Appliances, "Off_status")
    descriptor = None
    for klass in Appliances.__mro__:
        if "Off_status" in klass.__dict__:
            descriptor = klass.__dict__["Off_status"]
            break
    assert isinstance(descriptor, property)

def test_appliances_has_On_status():
    assert hasattr(Appliances, "On_status")
    descriptor = None
    for klass in Appliances.__mro__:
        if "On_status" in klass.__dict__:
            descriptor = klass.__dict__["On_status"]
            break
    assert isinstance(descriptor, property)



def test_system_is_not_abstract():
    assert not inspect.isabstract(system)


def test_system_constructor_exists():
    assert callable(system.__init__)


def test_system_constructor_args():
    sig = inspect.signature(system.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_system_has_status():
    assert hasattr(system, "status")
    descriptor = None
    for klass in system.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_name():
    assert hasattr(Login, "name")
    descriptor = None
    for klass in Login.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_owner_is_not_abstract():
    assert not inspect.isabstract(Owner)


def test_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_owner_has_name():
    assert hasattr(Owner, "name")
    descriptor = None
    for klass in Owner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
FireAlarm_strategy = st.builds(
    FireAlarm,
    status=
        st.booleans()
)
securityAlarm_strategy = st.builds(
    securityAlarm,
    status=
        st.booleans()
)
Police_strategy = st.builds(
    Police,
    name=
        safe_text
)
smokeAlarm_strategy = st.builds(
    smokeAlarm,
    status=
        st.booleans()
)
Department_strategy = st.builds(
    Department,
    name=
        safe_text
)
Home_Security_System_strategy = st.builds(
    Home_Security_System,
    system_Off=
        st.booleans(),
    system_On=
        st.booleans()
)
Fire_Alarm_system_strategy = st.builds(
    Fire_Alarm_system,
    system_Off=
        st.booleans(),
    system_On=
        st.booleans()
)
Appliances_strategy = st.builds(
    Appliances,
    Off_status=
        st.booleans(),
    On_status=
        st.booleans()
)
system_strategy = st.builds(
    system,
    status=
        st.booleans()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    name=
        safe_text
)
Owner_strategy = st.builds(
    Owner,
    name=
        safe_text
)

@given(instance=FireAlarm_strategy)
@settings(max_examples=50)
def test_firealarm_instantiation(instance):
    assert isinstance(instance, FireAlarm)



@given(instance=FireAlarm_strategy)
def test_firealarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=securityAlarm_strategy)
@settings(max_examples=50)
def test_securityalarm_instantiation(instance):
    assert isinstance(instance, securityAlarm)



@given(instance=securityAlarm_strategy)
def test_securityalarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Police_strategy)
@settings(max_examples=50)
def test_police_instantiation(instance):
    assert isinstance(instance, Police)



@given(instance=Police_strategy)
def test_police_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smokeAlarm_strategy)
@settings(max_examples=50)
def test_smokealarm_instantiation(instance):
    assert isinstance(instance, smokeAlarm)



@given(instance=smokeAlarm_strategy)
def test_smokealarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Home_Security_System_strategy)
@settings(max_examples=50)
def test_home_security_system_instantiation(instance):
    assert isinstance(instance, Home_Security_System)



@given(instance=Home_Security_System_strategy)
def test_home_security_system_system_Off_setter(instance):
    original = instance.system_Off
    instance.system_Off = original
    assert instance.system_Off == original



@given(instance=Home_Security_System_strategy)
def test_home_security_system_system_On_setter(instance):
    original = instance.system_On
    instance.system_On = original
    assert instance.system_On == original

@given(instance=Fire_Alarm_system_strategy)
@settings(max_examples=50)
def test_fire_alarm_system_instantiation(instance):
    assert isinstance(instance, Fire_Alarm_system)



@given(instance=Fire_Alarm_system_strategy)
def test_fire_alarm_system_system_Off_setter(instance):
    original = instance.system_Off
    instance.system_Off = original
    assert instance.system_Off == original



@given(instance=Fire_Alarm_system_strategy)
def test_fire_alarm_system_system_On_setter(instance):
    original = instance.system_On
    instance.system_On = original
    assert instance.system_On == original

@given(instance=Appliances_strategy)
@settings(max_examples=50)
def test_appliances_instantiation(instance):
    assert isinstance(instance, Appliances)



@given(instance=Appliances_strategy)
def test_appliances_Off_status_setter(instance):
    original = instance.Off_status
    instance.Off_status = original
    assert instance.Off_status == original



@given(instance=Appliances_strategy)
def test_appliances_On_status_setter(instance):
    original = instance.On_status
    instance.On_status = original
    assert instance.On_status == original

@given(instance=system_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, system)



@given(instance=system_strategy)
def test_system_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Owner_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, Owner)



@given(instance=Owner_strategy)
def test_owner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
