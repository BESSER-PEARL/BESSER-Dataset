import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    Registration,
    Friend,
    Message,
    secret,
    public,
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
    assert "email" in params, "Missing parameter 'email'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_email():
    assert hasattr(Login, "email")
    descriptor = None
    for klass in Login.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_registration_has_name():
    assert hasattr(Registration, "name")
    descriptor = None
    for klass in Registration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_registration_has_email():
    assert hasattr(Registration, "email")
    descriptor = None
    for klass in Registration.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_friend_is_not_abstract():
    assert not inspect.isabstract(Friend)


def test_friend_constructor_exists():
    assert callable(Friend.__init__)


def test_friend_constructor_args():
    sig = inspect.signature(Friend.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "maxChars" in params, "Missing parameter 'maxChars'"

def test_message_has_maxChars():
    assert hasattr(Message, "maxChars")
    descriptor = None
    for klass in Message.__mro__:
        if "maxChars" in klass.__dict__:
            descriptor = klass.__dict__["maxChars"]
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



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "likes" in params, "Missing parameter 'likes'"
    assert "info" in params, "Missing parameter 'info'"

def test_post_has_likes():
    assert hasattr(Post, "likes")
    descriptor = None
    for klass in Post.__mro__:
        if "likes" in klass.__dict__:
            descriptor = klass.__dict__["likes"]
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
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "photo" in params, "Missing parameter 'photo'"

def test_profile_has_password():
    assert hasattr(Profile, "password")
    descriptor = None
    for klass in Profile.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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

def test_profile_has_photo():
    assert hasattr(Profile, "photo")
    descriptor = None
    for klass in Profile.__mro__:
        if "photo" in klass.__dict__:
            descriptor = klass.__dict__["photo"]
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
    email=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    name=
        safe_text,
    password=
        st.none(),
    email=
        safe_text
)
Friend_strategy = st.builds(
    Friend,
)
Message_strategy = st.builds(
    Message,
    maxChars=
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
Post_strategy = st.builds(
    Post,
    likes=
        st.integers(),
    info=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    password=
        safe_text,
    username=
        safe_text,
    photo=
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
def test_login_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)



@given(instance=Registration_strategy)
def test_registration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Registration_strategy)
def test_registration_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Registration_strategy)
def test_registration_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Friend_strategy)
@settings(max_examples=50)
def test_friend_instantiation(instance):
    assert isinstance(instance, Friend)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)



@given(instance=Message_strategy)
def test_message_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original

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

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_likes_setter(instance):
    original = instance.likes
    instance.likes = original
    assert instance.likes == original



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
def test_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Profile_strategy)
def test_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Profile_strategy)
def test_profile_photo_setter(instance):
    original = instance.photo
    instance.photo = original
    assert instance.photo == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
