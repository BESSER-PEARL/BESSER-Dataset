import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface_Interface,
    Login,
    Registration,
    Page,
    Hashtag,
    Friend,
    Message,
    Group,
    Post,
    Profile,
    User,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



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
    assert "lname" in params, "Missing parameter 'lname'"
    assert "userName" in params, "Missing parameter 'userName'"

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

def test_registration_has_lname():
    assert hasattr(Registration, "lname")
    descriptor = None
    for klass in Registration.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
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



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_page_has_name():
    assert hasattr(Page, "name")
    descriptor = None
    for klass in Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hashtag_is_not_abstract():
    assert not inspect.isabstract(Hashtag)


def test_hashtag_constructor_exists():
    assert callable(Hashtag.__init__)


def test_hashtag_constructor_args():
    sig = inspect.signature(Hashtag.__init__)
    params = list(sig.parameters.keys())
    assert "numOfRepeat" in params, "Missing parameter 'numOfRepeat'"
    assert "name" in params, "Missing parameter 'name'"

def test_hashtag_has_numOfRepeat():
    assert hasattr(Hashtag, "numOfRepeat")
    descriptor = None
    for klass in Hashtag.__mro__:
        if "numOfRepeat" in klass.__dict__:
            descriptor = klass.__dict__["numOfRepeat"]
            break
    assert isinstance(descriptor, property)

def test_hashtag_has_name():
    assert hasattr(Hashtag, "name")
    descriptor = None
    for klass in Hashtag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "discription" in params, "Missing parameter 'discription'"

def test_group_has_name():
    assert hasattr(Group, "name")
    descriptor = None
    for klass in Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_group_has_discription():
    assert hasattr(Group, "discription")
    descriptor = None
    for klass in Group.__mro__:
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
    assert "password" in params, "Missing parameter 'password'"
    assert "about" in params, "Missing parameter 'about'"
    assert "username" in params, "Missing parameter 'username'"

def test_profile_has_password():
    assert hasattr(Profile, "password")
    descriptor = None
    for klass in Profile.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

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

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
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
    lname=
        safe_text,
    userName=
        safe_text
)
Page_strategy = st.builds(
    Page,
    name=
        safe_text
)
Hashtag_strategy = st.builds(
    Hashtag,
    numOfRepeat=
        st.integers(),
    name=
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
Group_strategy = st.builds(
    Group,
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
    password=
        safe_text,
    about=
        safe_text,
    username=
        safe_text
)
User_strategy = st.builds(
    User,
    name=
        safe_text
)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

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
def test_registration_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Registration_strategy)
def test_registration_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)



@given(instance=Page_strategy)
def test_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Hashtag_strategy)
@settings(max_examples=50)
def test_hashtag_instantiation(instance):
    assert isinstance(instance, Hashtag)



@given(instance=Hashtag_strategy)
def test_hashtag_numOfRepeat_setter(instance):
    original = instance.numOfRepeat
    instance.numOfRepeat = original
    assert instance.numOfRepeat == original



@given(instance=Hashtag_strategy)
def test_hashtag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)



@given(instance=Group_strategy)
def test_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Group_strategy)
def test_group_discription_setter(instance):
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
def test_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



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

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
