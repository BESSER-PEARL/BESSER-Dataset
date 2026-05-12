import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Page,
    Message,
    Group,
    Post,
    User,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Page" in params, "Missing parameter 'ID_Page'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_page_has_ID_Page():
    assert hasattr(Page, "ID_Page")
    descriptor = None
    for klass in Page.__mro__:
        if "ID_Page" in klass.__dict__:
            descriptor = klass.__dict__["ID_Page"]
            break
    assert isinstance(descriptor, property)

def test_page_has_Name():
    assert hasattr(Page, "Name")
    descriptor = None
    for klass in Page.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_page_has_ID_User():
    assert hasattr(Page, "ID_User")
    descriptor = None
    for klass in Page.__mro__:
        if "ID_User" in klass.__dict__:
            descriptor = klass.__dict__["ID_User"]
            break
    assert isinstance(descriptor, property)

def test_page_has_Description():
    assert hasattr(Page, "Description")
    descriptor = None
    for klass in Page.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "Max_Chars" in params, "Missing parameter 'Max_Chars'"
    assert "ID_Message" in params, "Missing parameter 'ID_Message'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Mail" in params, "Missing parameter 'Mail'"

def test_message_has_Max_Chars():
    assert hasattr(Message, "Max_Chars")
    descriptor = None
    for klass in Message.__mro__:
        if "Max_Chars" in klass.__dict__:
            descriptor = klass.__dict__["Max_Chars"]
            break
    assert isinstance(descriptor, property)

def test_message_has_ID_Message():
    assert hasattr(Message, "ID_Message")
    descriptor = None
    for klass in Message.__mro__:
        if "ID_Message" in klass.__dict__:
            descriptor = klass.__dict__["ID_Message"]
            break
    assert isinstance(descriptor, property)

def test_message_has_ID_User():
    assert hasattr(Message, "ID_User")
    descriptor = None
    for klass in Message.__mro__:
        if "ID_User" in klass.__dict__:
            descriptor = klass.__dict__["ID_User"]
            break
    assert isinstance(descriptor, property)

def test_message_has_Mail():
    assert hasattr(Message, "Mail")
    descriptor = None
    for klass in Message.__mro__:
        if "Mail" in klass.__dict__:
            descriptor = klass.__dict__["Mail"]
            break
    assert isinstance(descriptor, property)



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Group" in params, "Missing parameter 'ID_Group'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_group_has_ID_Group():
    assert hasattr(Group, "ID_Group")
    descriptor = None
    for klass in Group.__mro__:
        if "ID_Group" in klass.__dict__:
            descriptor = klass.__dict__["ID_Group"]
            break
    assert isinstance(descriptor, property)

def test_group_has_ID_User():
    assert hasattr(Group, "ID_User")
    descriptor = None
    for klass in Group.__mro__:
        if "ID_User" in klass.__dict__:
            descriptor = klass.__dict__["ID_User"]
            break
    assert isinstance(descriptor, property)

def test_group_has_Name():
    assert hasattr(Group, "Name")
    descriptor = None
    for klass in Group.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_group_has_Description():
    assert hasattr(Group, "Description")
    descriptor = None
    for klass in Group.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Post" in params, "Missing parameter 'ID_Post'"
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Info" in params, "Missing parameter 'Info'"
    assert "Privacy" in params, "Missing parameter 'Privacy'"
    assert "ID_Page" in params, "Missing parameter 'ID_Page'"

def test_post_has_ID_Post():
    assert hasattr(Post, "ID_Post")
    descriptor = None
    for klass in Post.__mro__:
        if "ID_Post" in klass.__dict__:
            descriptor = klass.__dict__["ID_Post"]
            break
    assert isinstance(descriptor, property)

def test_post_has_Mail():
    assert hasattr(Post, "Mail")
    descriptor = None
    for klass in Post.__mro__:
        if "Mail" in klass.__dict__:
            descriptor = klass.__dict__["Mail"]
            break
    assert isinstance(descriptor, property)

def test_post_has_Info():
    assert hasattr(Post, "Info")
    descriptor = None
    for klass in Post.__mro__:
        if "Info" in klass.__dict__:
            descriptor = klass.__dict__["Info"]
            break
    assert isinstance(descriptor, property)

def test_post_has_Privacy():
    assert hasattr(Post, "Privacy")
    descriptor = None
    for klass in Post.__mro__:
        if "Privacy" in klass.__dict__:
            descriptor = klass.__dict__["Privacy"]
            break
    assert isinstance(descriptor, property)

def test_post_has_ID_Page():
    assert hasattr(Post, "ID_Page")
    descriptor = None
    for klass in Post.__mro__:
        if "ID_Page" in klass.__dict__:
            descriptor = klass.__dict__["ID_Page"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Fist_Name" in params, "Missing parameter 'Fist_Name'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_user_has_Fist_Name():
    assert hasattr(User, "Fist_Name")
    descriptor = None
    for klass in User.__mro__:
        if "Fist_Name" in klass.__dict__:
            descriptor = klass.__dict__["Fist_Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_ID_User():
    assert hasattr(User, "ID_User")
    descriptor = None
    for klass in User.__mro__:
        if "ID_User" in klass.__dict__:
            descriptor = klass.__dict__["ID_User"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Mail():
    assert hasattr(User, "Mail")
    descriptor = None
    for klass in User.__mro__:
        if "Mail" in klass.__dict__:
            descriptor = klass.__dict__["Mail"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Name():
    assert hasattr(User, "Name")
    descriptor = None
    for klass in User.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Profile" in params, "Missing parameter 'ID_Profile'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"
    assert "About" in params, "Missing parameter 'About'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_profile_has_ID_Profile():
    assert hasattr(Profile, "ID_Profile")
    descriptor = None
    for klass in Profile.__mro__:
        if "ID_Profile" in klass.__dict__:
            descriptor = klass.__dict__["ID_Profile"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_User_Name():
    assert hasattr(Profile, "User_Name")
    descriptor = None
    for klass in Profile.__mro__:
        if "User_Name" in klass.__dict__:
            descriptor = klass.__dict__["User_Name"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_About():
    assert hasattr(Profile, "About")
    descriptor = None
    for klass in Profile.__mro__:
        if "About" in klass.__dict__:
            descriptor = klass.__dict__["About"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_Password():
    assert hasattr(Profile, "Password")
    descriptor = None
    for klass in Profile.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
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
Page_strategy = st.builds(
    Page,
    ID_Page=
        st.integers(),
    Name=
        safe_text,
    ID_User=
        st.integers(),
    Description=
        safe_text
)
Message_strategy = st.builds(
    Message,
    Max_Chars=
        safe_text,
    ID_Message=
        st.integers(),
    ID_User=
        st.integers(),
    Mail=
        safe_text
)
Group_strategy = st.builds(
    Group,
    ID_Group=
        st.integers(),
    ID_User=
        st.integers(),
    Name=
        safe_text,
    Description=
        safe_text
)
Post_strategy = st.builds(
    Post,
    ID_Post=
        st.integers(),
    Mail=
        safe_text,
    Info=
        safe_text,
    Privacy=
        safe_text,
    ID_Page=
        st.integers()
)
User_strategy = st.builds(
    User,
    Fist_Name=
        safe_text,
    ID_User=
        st.integers(),
    Mail=
        safe_text,
    Name=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    ID_Profile=
        safe_text,
    User_Name=
        safe_text,
    About=
        safe_text,
    Password=
        safe_text
)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)



@given(instance=Page_strategy)
def test_page_ID_Page_setter(instance):
    original = instance.ID_Page
    instance.ID_Page = original
    assert instance.ID_Page == original



@given(instance=Page_strategy)
def test_page_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Page_strategy)
def test_page_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Page_strategy)
def test_page_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)



@given(instance=Message_strategy)
def test_message_Max_Chars_setter(instance):
    original = instance.Max_Chars
    instance.Max_Chars = original
    assert instance.Max_Chars == original



@given(instance=Message_strategy)
def test_message_ID_Message_setter(instance):
    original = instance.ID_Message
    instance.ID_Message = original
    assert instance.ID_Message == original



@given(instance=Message_strategy)
def test_message_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Message_strategy)
def test_message_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)



@given(instance=Group_strategy)
def test_group_ID_Group_setter(instance):
    original = instance.ID_Group
    instance.ID_Group = original
    assert instance.ID_Group == original



@given(instance=Group_strategy)
def test_group_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Group_strategy)
def test_group_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Group_strategy)
def test_group_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)



@given(instance=Post_strategy)
def test_post_ID_Post_setter(instance):
    original = instance.ID_Post
    instance.ID_Post = original
    assert instance.ID_Post == original



@given(instance=Post_strategy)
def test_post_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=Post_strategy)
def test_post_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original



@given(instance=Post_strategy)
def test_post_Privacy_setter(instance):
    original = instance.Privacy
    instance.Privacy = original
    assert instance.Privacy == original



@given(instance=Post_strategy)
def test_post_ID_Page_setter(instance):
    original = instance.ID_Page
    instance.ID_Page = original
    assert instance.ID_Page == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Fist_Name_setter(instance):
    original = instance.Fist_Name
    instance.Fist_Name = original
    assert instance.Fist_Name == original



@given(instance=User_strategy)
def test_user_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=User_strategy)
def test_user_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=User_strategy)
def test_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_ID_Profile_setter(instance):
    original = instance.ID_Profile
    instance.ID_Profile = original
    assert instance.ID_Profile == original



@given(instance=Profile_strategy)
def test_profile_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original



@given(instance=Profile_strategy)
def test_profile_About_setter(instance):
    original = instance.About
    instance.About = original
    assert instance.About == original



@given(instance=Profile_strategy)
def test_profile_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original
