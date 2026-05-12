import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    Registration,
    secret,
    public,
    Others,
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
    assert "userName" in params, "Missing parameter 'userName'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "fname" in params, "Missing parameter 'fname'"

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

def test_registration_has_password():
    assert hasattr(Registration, "password")
    descriptor = None
    for klass in Registration.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_fname():
    assert hasattr(Registration, "fname")
    descriptor = None
    for klass in Registration.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)



def test_secret_is_not_abstract():
    assert not inspect.isabstract(secret)


def test_secret_constructor_exists():
    assert callable(secret.__init__)


def test_secret_constructor_args():
    sig = inspect.signature(secret.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_secret_has_name():
    assert hasattr(secret, "name")
    descriptor = None
    for klass in secret.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_public_is_not_abstract():
    assert not inspect.isabstract(public)


def test_public_constructor_exists():
    assert callable(public.__init__)


def test_public_constructor_args():
    sig = inspect.signature(public.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_public_has_name():
    assert hasattr(public, "name")
    descriptor = None
    for klass in public.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_others_is_not_abstract():
    assert not inspect.isabstract(Others)


def test_others_constructor_exists():
    assert callable(Others.__init__)


def test_others_constructor_args():
    sig = inspect.signature(Others.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "discription" in params, "Missing parameter 'discription'"

def test_others_has_name():
    assert hasattr(Others, "name")
    descriptor = None
    for klass in Others.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_others_has_discription():
    assert hasattr(Others, "discription")
    descriptor = None
    for klass in Others.__mro__:
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
    assert "privacy" in params, "Missing parameter 'privacy'"
    assert "info" in params, "Missing parameter 'info'"

def test_post_has_privacy():
    assert hasattr(Post, "privacy")
    descriptor = None
    for klass in Post.__mro__:
        if "privacy" in klass.__dict__:
            descriptor = klass.__dict__["privacy"]
            break
    assert isinstance(descriptor, property)

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
    assert "about" in params, "Missing parameter 'about'"
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_profile_has_about():
    assert hasattr(Profile, "about")
    descriptor = None
    for klass in Profile.__mro__:
        if "about" in klass.__dict__:
            descriptor = klass.__dict__["about"]
            break
    assert isinstance(descriptor, property)

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



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
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
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    userName=
        safe_text,
    lname=
        safe_text,
    password=
        st.none(),
    fname=
        safe_text
)
secret_strategy = st.builds(
    secret,
    name=
        safe_text
)
public_strategy = st.builds(
    public,
    name=
        safe_text
)
Others_strategy = st.builds(
    Others,
    name=
        safe_text,
    discription=
        safe_text
)
Post_strategy = st.builds(
    Post,
    privacy=
        safe_text,
    info=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    about=
        safe_text,
    username=
        safe_text,
    password=
        safe_text
)
User_strategy = st.builds(
    User,
    name=
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
def test_registration_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Registration_strategy)
def test_registration_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Registration_strategy)
def test_registration_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Registration_strategy)
def test_registration_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original

@given(instance=secret_strategy)
@settings(max_examples=50)
def test_secret_instantiation(instance):
    assert isinstance(instance, secret)



@given(instance=secret_strategy)
def test_secret_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=public_strategy)
@settings(max_examples=50)
def test_public_instantiation(instance):
    assert isinstance(instance, public)



@given(instance=public_strategy)
def test_public_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Others_strategy)
@settings(max_examples=50)
def test_others_instantiation(instance):
    assert isinstance(instance, Others)



@given(instance=Others_strategy)
def test_others_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Others_strategy)
def test_others_discription_setter(instance):
    original = instance.discription
    instance.discription = original
    assert instance.discription == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_privacy_setter(instance):
    original = instance.privacy
    instance.privacy = original
    assert instance.privacy == original



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
def test_profile_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original



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

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
