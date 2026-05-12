import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    Registration,
    Event,
    Notification,
    Interest,
    Post,
    Profile,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "lname" in params, "Missing parameter 'lname'"

def test_registration_has_fname():
    assert hasattr(Registration, "fname")
    descriptor = None
    for klass in Registration.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_password():
    assert hasattr(Registration, "password")
    descriptor = None
    for klass in Registration.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_userName():
    assert hasattr(Registration, "userName")
    descriptor = None
    for klass in Registration.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_lname():
    assert hasattr(Registration, "lname")
    descriptor = None
    for klass in Registration.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "time" in params, "Missing parameter 'time'"
    assert "name" in params, "Missing parameter 'name'"

def test_event_has_location():
    assert hasattr(Event, "location")
    descriptor = None
    for klass in Event.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_event_has_time():
    assert hasattr(Event, "time")
    descriptor = None
    for klass in Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_event_has_name():
    assert hasattr(Event, "name")
    descriptor = None
    for klass in Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_notification_is_not_abstract():
    assert not inspect.isabstract(Notification)


def test_notification_constructor_exists():
    assert callable(Notification.__init__)


def test_notification_constructor_args():
    sig = inspect.signature(Notification.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"

def test_notification_has_update():
    assert hasattr(Notification, "update")
    descriptor = None
    for klass in Notification.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)



def test_interest_is_not_abstract():
    assert not inspect.isabstract(Interest)


def test_interest_constructor_exists():
    assert callable(Interest.__init__)


def test_interest_constructor_args():
    sig = inspect.signature(Interest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "discription" in params, "Missing parameter 'discription'"

def test_interest_has_name():
    assert hasattr(Interest, "name")
    descriptor = None
    for klass in Interest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_interest_has_discription():
    assert hasattr(Interest, "discription")
    descriptor = None
    for klass in Interest.__mro__:
        if "discription" in klass.__dict__:
            descriptor = klass.__dict__["discription"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"

def test_post_has_info():
    assert hasattr(Post, "info")
    descriptor = None
    for klass in Post.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "interests" in params, "Missing parameter 'interests'"

def test_profile_has_username():
    assert hasattr(Profile, "username")
    descriptor = None
    for klass in Profile.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_password():
    assert hasattr(Profile, "password")
    descriptor = None
    for klass in Profile.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_interests():
    assert hasattr(Profile, "interests")
    descriptor = None
    for klass in Profile.__mro__:
        if "interests" in klass.__dict__:
            descriptor = klass.__dict__["interests"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"
    assert "username" in params, "Missing parameter 'username'"
    assert "fname" in params, "Missing parameter 'fname'"

def test_user_has_lname():
    assert hasattr(User, "lname")
    descriptor = None
    for klass in User.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_fname():
    assert hasattr(User, "fname")
    descriptor = None
    for klass in User.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
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
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    fname=
        safe_text,
    password=
        safe_text,
    userName=
        safe_text,
    lname=
        safe_text
)
Event_strategy = st.builds(
    Event,
    location=
        safe_text,
    time=
        safe_text,
    name=
        safe_text
)
Notification_strategy = st.builds(
    Notification,
    update=
        safe_text
)
Interest_strategy = st.builds(
    Interest,
    name=
        safe_text,
    discription=
        safe_text
)
Post_strategy = st.builds(
    Post,
    info=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    username=
        safe_text,
    password=
        safe_text,
    interests=
        safe_text
)
User_strategy = st.builds(
    User,
    lname=
        safe_text,
    username=
        safe_text,
    fname=
        safe_text
)

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
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)



@given(instance=Registration_strategy)
def test_registration_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Registration_strategy)
def test_registration_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Registration_strategy)
def test_registration_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Registration_strategy)
def test_registration_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_event_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Event_strategy)
def test_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Event_strategy)
def test_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Notification_strategy)
@settings(max_examples=50)
def test_notification_instantiation(instance):
    assert isinstance(instance, Notification)



@given(instance=Notification_strategy)
def test_notification_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=Interest_strategy)
@settings(max_examples=50)
def test_interest_instantiation(instance):
    assert isinstance(instance, Interest)



@given(instance=Interest_strategy)
def test_interest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Interest_strategy)
def test_interest_discription_setter(instance):
    original = instance.discription
    instance.discription = original
    assert instance.discription == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Profile_strategy)
def test_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Profile_strategy)
def test_profile_interests_setter(instance):
    original = instance.interests
    instance.interests = original
    assert instance.interests == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_user_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original
