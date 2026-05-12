import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TV,
    Fire_Alarm,
    Security_System,
    Fan,
    Light,
    System,
    Login,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tv_is_not_abstract():
    assert not inspect.isabstract(TV)


def test_tv_constructor_exists():
    assert callable(TV.__init__)


def test_tv_constructor_args():
    sig = inspect.signature(TV.__init__)
    params = list(sig.parameters.keys())



def test_fire_alarm_is_not_abstract():
    assert not inspect.isabstract(Fire_Alarm)


def test_fire_alarm_constructor_exists():
    assert callable(Fire_Alarm.__init__)


def test_fire_alarm_constructor_args():
    sig = inspect.signature(Fire_Alarm.__init__)
    params = list(sig.parameters.keys())
    assert "systemOff" in params, "Missing parameter 'systemOff'"
    assert "systemOn" in params, "Missing parameter 'systemOn'"

def test_fire_alarm_has_systemOff():
    assert hasattr(Fire_Alarm, "systemOff")
    descriptor = None
    for klass in Fire_Alarm.__mro__:
        if "systemOff" in klass.__dict__:
            descriptor = klass.__dict__["systemOff"]
            break
    assert isinstance(descriptor, property)

def test_fire_alarm_has_systemOn():
    assert hasattr(Fire_Alarm, "systemOn")
    descriptor = None
    for klass in Fire_Alarm.__mro__:
        if "systemOn" in klass.__dict__:
            descriptor = klass.__dict__["systemOn"]
            break
    assert isinstance(descriptor, property)



def test_security_system_is_not_abstract():
    assert not inspect.isabstract(Security_System)


def test_security_system_constructor_exists():
    assert callable(Security_System.__init__)


def test_security_system_constructor_args():
    sig = inspect.signature(Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "systemOn" in params, "Missing parameter 'systemOn'"
    assert "systemOff" in params, "Missing parameter 'systemOff'"

def test_security_system_has_systemOn():
    assert hasattr(Security_System, "systemOn")
    descriptor = None
    for klass in Security_System.__mro__:
        if "systemOn" in klass.__dict__:
            descriptor = klass.__dict__["systemOn"]
            break
    assert isinstance(descriptor, property)

def test_security_system_has_systemOff():
    assert hasattr(Security_System, "systemOff")
    descriptor = None
    for klass in Security_System.__mro__:
        if "systemOff" in klass.__dict__:
            descriptor = klass.__dict__["systemOff"]
            break
    assert isinstance(descriptor, property)



def test_fan_is_not_abstract():
    assert not inspect.isabstract(Fan)


def test_fan_constructor_exists():
    assert callable(Fan.__init__)


def test_fan_constructor_args():
    sig = inspect.signature(Fan.__init__)
    params = list(sig.parameters.keys())



def test_light_is_not_abstract():
    assert not inspect.isabstract(Light)


def test_light_constructor_exists():
    assert callable(Light.__init__)


def test_light_constructor_args():
    sig = inspect.signature(Light.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_system_has_status():
    assert hasattr(System, "status")
    descriptor = None
    for klass in System.__mro__:
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
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Name():
    assert hasattr(Login, "Name")
    descriptor = None
    for klass in Login.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
TV_strategy = st.builds(
    TV,
)
Fire_Alarm_strategy = st.builds(
    Fire_Alarm,
    systemOff=
        st.booleans(),
    systemOn=
        st.booleans()
)
Security_System_strategy = st.builds(
    Security_System,
    systemOn=
        st.booleans(),
    systemOff=
        st.booleans()
)
Fan_strategy = st.builds(
    Fan,
)
Light_strategy = st.builds(
    Light,
)
System_strategy = st.builds(
    System,
    status=
        st.booleans()
)
Login_strategy = st.builds(
    Login,
    Password=
        safe_text,
    Name=
        safe_text
)
User_strategy = st.builds(
    User,
    Name=
        safe_text
)

@given(instance=TV_strategy)
@settings(max_examples=50)
def test_tv_instantiation(instance):
    assert isinstance(instance, TV)

@given(instance=Fire_Alarm_strategy)
@settings(max_examples=50)
def test_fire_alarm_instantiation(instance):
    assert isinstance(instance, Fire_Alarm)



@given(instance=Fire_Alarm_strategy)
def test_fire_alarm_systemOff_setter(instance):
    original = instance.systemOff
    instance.systemOff = original
    assert instance.systemOff == original



@given(instance=Fire_Alarm_strategy)
def test_fire_alarm_systemOn_setter(instance):
    original = instance.systemOn
    instance.systemOn = original
    assert instance.systemOn == original

@given(instance=Security_System_strategy)
@settings(max_examples=50)
def test_security_system_instantiation(instance):
    assert isinstance(instance, Security_System)



@given(instance=Security_System_strategy)
def test_security_system_systemOn_setter(instance):
    original = instance.systemOn
    instance.systemOn = original
    assert instance.systemOn == original



@given(instance=Security_System_strategy)
def test_security_system_systemOff_setter(instance):
    original = instance.systemOff
    instance.systemOff = original
    assert instance.systemOff == original

@given(instance=Fan_strategy)
@settings(max_examples=50)
def test_fan_instantiation(instance):
    assert isinstance(instance, Fan)

@given(instance=Light_strategy)
@settings(max_examples=50)
def test_light_instantiation(instance):
    assert isinstance(instance, Light)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)



@given(instance=System_strategy)
def test_system_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Login_strategy)
def test_login_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
