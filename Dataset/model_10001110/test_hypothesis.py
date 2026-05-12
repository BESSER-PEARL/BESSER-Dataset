import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    Search,
    Item,
    Login,
    Registration,
    Hashtag,
    Comment,
    Post,
    Profile,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_registration_has_name():
    assert hasattr(Registration, "name")
    descriptor = None
    for klass in Registration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_registration_has_password():
    assert hasattr(Registration, "password")
    descriptor = None
    for klass in Registration.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_username():
    assert hasattr(Registration, "username")
    descriptor = None
    for klass in Registration.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_hashtag_is_not_abstract():
    assert not inspect.isabstract(Hashtag)


def test_hashtag_constructor_exists():
    assert callable(Hashtag.__init__)


def test_hashtag_constructor_args():
    sig = inspect.signature(Hashtag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hashtag_has_name():
    assert hasattr(Hashtag, "name")
    descriptor = None
    for klass in Hashtag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_post_has_type():
    assert hasattr(Post, "type")
    descriptor = None
    for klass in Post.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_profile_has_username():
    assert hasattr(Profile, "username")
    descriptor = None
    for klass in Profile.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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
Class_strategy = st.builds(
    Class,
)
Search_strategy = st.builds(
    Search,
)
Item_strategy = st.builds(
    Item,
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    name=
        safe_text,
    userName=
        safe_text,
    password=
        safe_text,
    username=
        safe_text
)
Hashtag_strategy = st.builds(
    Hashtag,
    name=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Post_strategy = st.builds(
    Post,
    type=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    username=
        safe_text
)
User_strategy = st.builds(
    User,
    name=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

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
def test_registration_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Registration_strategy)
def test_registration_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Registration_strategy)
def test_registration_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Hashtag_strategy)
@settings(max_examples=50)
def test_hashtag_instantiation(instance):
    assert isinstance(instance, Hashtag)



@given(instance=Hashtag_strategy)
def test_hashtag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
