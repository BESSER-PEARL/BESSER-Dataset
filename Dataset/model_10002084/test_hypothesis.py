import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Registration,
    EventType,
    User,
    Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())



def test_eventtype_is_not_abstract():
    assert not inspect.isabstract(EventType)


def test_eventtype_constructor_exists():
    assert callable(EventType.__init__)


def test_eventtype_constructor_args():
    sig = inspect.signature(EventType.__init__)
    params = list(sig.parameters.keys())
    assert "EventTypeId" in params, "Missing parameter 'EventTypeId'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_eventtype_has_EventTypeId():
    assert hasattr(EventType, "EventTypeId")
    descriptor = None
    for klass in EventType.__mro__:
        if "EventTypeId" in klass.__dict__:
            descriptor = klass.__dict__["EventTypeId"]
            break
    assert isinstance(descriptor, property)

def test_eventtype_has_Type():
    assert hasattr(EventType, "Type")
    descriptor = None
    for klass in EventType.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "Login" in params, "Missing parameter 'Login'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_user_has_PhoneNumber():
    assert hasattr(User, "PhoneNumber")
    descriptor = None
    for klass in User.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Login():
    assert hasattr(User, "Login")
    descriptor = None
    for klass in User.__mro__:
        if "Login" in klass.__dict__:
            descriptor = klass.__dict__["Login"]
            break
    assert isinstance(descriptor, property)

def test_user_has_DateOfBirth():
    assert hasattr(User, "DateOfBirth")
    descriptor = None
    for klass in User.__mro__:
        if "DateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["DateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Email():
    assert hasattr(User, "Email")
    descriptor = None
    for klass in User.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserId():
    assert hasattr(User, "UserId")
    descriptor = None
    for klass in User.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "MaxNumberOfPlayers" in params, "Missing parameter 'MaxNumberOfPlayers'"
    assert "EventId" in params, "Missing parameter 'EventId'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "CurrentNumberOfPlayers" in params, "Missing parameter 'CurrentNumberOfPlayers'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "DateTime" in params, "Missing parameter 'DateTime'"

def test_event_has_MaxNumberOfPlayers():
    assert hasattr(Event, "MaxNumberOfPlayers")
    descriptor = None
    for klass in Event.__mro__:
        if "MaxNumberOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["MaxNumberOfPlayers"]
            break
    assert isinstance(descriptor, property)

def test_event_has_EventId():
    assert hasattr(Event, "EventId")
    descriptor = None
    for klass in Event.__mro__:
        if "EventId" in klass.__dict__:
            descriptor = klass.__dict__["EventId"]
            break
    assert isinstance(descriptor, property)

def test_event_has_Address():
    assert hasattr(Event, "Address")
    descriptor = None
    for klass in Event.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_event_has_CurrentNumberOfPlayers():
    assert hasattr(Event, "CurrentNumberOfPlayers")
    descriptor = None
    for klass in Event.__mro__:
        if "CurrentNumberOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["CurrentNumberOfPlayers"]
            break
    assert isinstance(descriptor, property)

def test_event_has_attribute():
    assert hasattr(Event, "attribute")
    descriptor = None
    for klass in Event.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_event_has_Description():
    assert hasattr(Event, "Description")
    descriptor = None
    for klass in Event.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_event_has_DateTime():
    assert hasattr(Event, "DateTime")
    descriptor = None
    for klass in Event.__mro__:
        if "DateTime" in klass.__dict__:
            descriptor = klass.__dict__["DateTime"]
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
Registration_strategy = st.builds(
    Registration,
)
EventType_strategy = st.builds(
    EventType,
    EventTypeId=
        st.integers(),
    Type=
        safe_text
)
User_strategy = st.builds(
    User,
    PhoneNumber=
        safe_text,
    Login=
        safe_text,
    DateOfBirth=
        safe_text,
    Email=
        safe_text,
    UserId=
        st.integers(),
    Password=
        safe_text
)
Event_strategy = st.builds(
    Event,
    MaxNumberOfPlayers=
        st.integers(),
    EventId=
        st.integers(),
    Address=
        safe_text,
    CurrentNumberOfPlayers=
        st.integers(),
    attribute=
        safe_text,
    Description=
        safe_text,
    DateTime=
        safe_text
)

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)

@given(instance=EventType_strategy)
@settings(max_examples=50)
def test_eventtype_instantiation(instance):
    assert isinstance(instance, EventType)



@given(instance=EventType_strategy)
def test_eventtype_EventTypeId_setter(instance):
    original = instance.EventTypeId
    instance.EventTypeId = original
    assert instance.EventTypeId == original



@given(instance=EventType_strategy)
def test_eventtype_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=User_strategy)
def test_user_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=User_strategy)
def test_user_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_user_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_MaxNumberOfPlayers_setter(instance):
    original = instance.MaxNumberOfPlayers
    instance.MaxNumberOfPlayers = original
    assert instance.MaxNumberOfPlayers == original



@given(instance=Event_strategy)
def test_event_EventId_setter(instance):
    original = instance.EventId
    instance.EventId = original
    assert instance.EventId == original



@given(instance=Event_strategy)
def test_event_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Event_strategy)
def test_event_CurrentNumberOfPlayers_setter(instance):
    original = instance.CurrentNumberOfPlayers
    instance.CurrentNumberOfPlayers = original
    assert instance.CurrentNumberOfPlayers == original



@given(instance=Event_strategy)
def test_event_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Event_strategy)
def test_event_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Event_strategy)
def test_event_DateTime_setter(instance):
    original = instance.DateTime
    instance.DateTime = original
    assert instance.DateTime == original
