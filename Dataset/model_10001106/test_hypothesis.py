import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    End_User,
    User_Admin_Module,
    System_User,
    Internet_Users,
    Thick_Client_Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_end_user_is_not_abstract():
    assert not inspect.isabstract(End_User)


def test_end_user_constructor_exists():
    assert callable(End_User.__init__)


def test_end_user_constructor_args():
    sig = inspect.signature(End_User.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "userType" in params, "Missing parameter 'userType'"
    assert "password" in params, "Missing parameter 'password'"

def test_end_user_has_login():
    assert hasattr(End_User, "login")
    descriptor = None
    for klass in End_User.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_end_user_has_userType():
    assert hasattr(End_User, "userType")
    descriptor = None
    for klass in End_User.__mro__:
        if "userType" in klass.__dict__:
            descriptor = klass.__dict__["userType"]
            break
    assert isinstance(descriptor, property)

def test_end_user_has_password():
    assert hasattr(End_User, "password")
    descriptor = None
    for klass in End_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_user_admin_module_is_not_abstract():
    assert not inspect.isabstract(User_Admin_Module)


def test_user_admin_module_constructor_exists():
    assert callable(User_Admin_Module.__init__)


def test_user_admin_module_constructor_args():
    sig = inspect.signature(User_Admin_Module.__init__)
    params = list(sig.parameters.keys())
    assert "Generate_User" in params, "Missing parameter 'Generate_User'"
    assert "View_User" in params, "Missing parameter 'View_User'"
    assert "Delete_User" in params, "Missing parameter 'Delete_User'"

def test_user_admin_module_has_Generate_User():
    assert hasattr(User_Admin_Module, "Generate_User")
    descriptor = None
    for klass in User_Admin_Module.__mro__:
        if "Generate_User" in klass.__dict__:
            descriptor = klass.__dict__["Generate_User"]
            break
    assert isinstance(descriptor, property)

def test_user_admin_module_has_View_User():
    assert hasattr(User_Admin_Module, "View_User")
    descriptor = None
    for klass in User_Admin_Module.__mro__:
        if "View_User" in klass.__dict__:
            descriptor = klass.__dict__["View_User"]
            break
    assert isinstance(descriptor, property)

def test_user_admin_module_has_Delete_User():
    assert hasattr(User_Admin_Module, "Delete_User")
    descriptor = None
    for klass in User_Admin_Module.__mro__:
        if "Delete_User" in klass.__dict__:
            descriptor = klass.__dict__["Delete_User"]
            break
    assert isinstance(descriptor, property)



def test_system_user_is_not_abstract():
    assert not inspect.isabstract(System_User)


def test_system_user_constructor_exists():
    assert callable(System_User.__init__)


def test_system_user_constructor_args():
    sig = inspect.signature(System_User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "login" in params, "Missing parameter 'login'"

def test_system_user_has_password():
    assert hasattr(System_User, "password")
    descriptor = None
    for klass in System_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_system_user_has_login():
    assert hasattr(System_User, "login")
    descriptor = None
    for klass in System_User.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_internet_users_is_not_abstract():
    assert not inspect.isabstract(Internet_Users)


def test_internet_users_constructor_exists():
    assert callable(Internet_Users.__init__)


def test_internet_users_constructor_args():
    sig = inspect.signature(Internet_Users.__init__)
    params = list(sig.parameters.keys())
    assert "Database_Access" in params, "Missing parameter 'Database_Access'"

def test_internet_users_has_Database_Access():
    assert hasattr(Internet_Users, "Database_Access")
    descriptor = None
    for klass in Internet_Users.__mro__:
        if "Database_Access" in klass.__dict__:
            descriptor = klass.__dict__["Database_Access"]
            break
    assert isinstance(descriptor, property)



def test_thick_client_users_is_not_abstract():
    assert not inspect.isabstract(Thick_Client_Users)


def test_thick_client_users_constructor_exists():
    assert callable(Thick_Client_Users.__init__)


def test_thick_client_users_constructor_args():
    sig = inspect.signature(Thick_Client_Users.__init__)
    params = list(sig.parameters.keys())
    assert "Database_Access" in params, "Missing parameter 'Database_Access'"
    assert "View_User" in params, "Missing parameter 'View_User'"

def test_thick_client_users_has_Database_Access():
    assert hasattr(Thick_Client_Users, "Database_Access")
    descriptor = None
    for klass in Thick_Client_Users.__mro__:
        if "Database_Access" in klass.__dict__:
            descriptor = klass.__dict__["Database_Access"]
            break
    assert isinstance(descriptor, property)

def test_thick_client_users_has_View_User():
    assert hasattr(Thick_Client_Users, "View_User")
    descriptor = None
    for klass in Thick_Client_Users.__mro__:
        if "View_User" in klass.__dict__:
            descriptor = klass.__dict__["View_User"]
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
End_User_strategy = st.builds(
    End_User,
    login=
        safe_text,
    userType=
        safe_text,
    password=
        safe_text
)
User_Admin_Module_strategy = st.builds(
    User_Admin_Module,
    Generate_User=
        st.none(),
    View_User=
        st.none(),
    Delete_User=
        st.none()
)
System_User_strategy = st.builds(
    System_User,
    password=
        safe_text,
    login=
        safe_text
)
Internet_Users_strategy = st.builds(
    Internet_Users,
    Database_Access=
        st.none()
)
Thick_Client_Users_strategy = st.builds(
    Thick_Client_Users,
    Database_Access=
        st.none(),
    View_User=
        st.none()
)

@given(instance=End_User_strategy)
@settings(max_examples=50)
def test_end_user_instantiation(instance):
    assert isinstance(instance, End_User)



@given(instance=End_User_strategy)
def test_end_user_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=End_User_strategy)
def test_end_user_userType_setter(instance):
    original = instance.userType
    instance.userType = original
    assert instance.userType == original



@given(instance=End_User_strategy)
def test_end_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=User_Admin_Module_strategy)
@settings(max_examples=50)
def test_user_admin_module_instantiation(instance):
    assert isinstance(instance, User_Admin_Module)



@given(instance=User_Admin_Module_strategy)
def test_user_admin_module_Generate_User_setter(instance):
    original = instance.Generate_User
    instance.Generate_User = original
    assert instance.Generate_User == original



@given(instance=User_Admin_Module_strategy)
def test_user_admin_module_View_User_setter(instance):
    original = instance.View_User
    instance.View_User = original
    assert instance.View_User == original



@given(instance=User_Admin_Module_strategy)
def test_user_admin_module_Delete_User_setter(instance):
    original = instance.Delete_User
    instance.Delete_User = original
    assert instance.Delete_User == original

@given(instance=System_User_strategy)
@settings(max_examples=50)
def test_system_user_instantiation(instance):
    assert isinstance(instance, System_User)



@given(instance=System_User_strategy)
def test_system_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=System_User_strategy)
def test_system_user_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=Internet_Users_strategy)
@settings(max_examples=50)
def test_internet_users_instantiation(instance):
    assert isinstance(instance, Internet_Users)



@given(instance=Internet_Users_strategy)
def test_internet_users_Database_Access_setter(instance):
    original = instance.Database_Access
    instance.Database_Access = original
    assert instance.Database_Access == original

@given(instance=Thick_Client_Users_strategy)
@settings(max_examples=50)
def test_thick_client_users_instantiation(instance):
    assert isinstance(instance, Thick_Client_Users)



@given(instance=Thick_Client_Users_strategy)
def test_thick_client_users_Database_Access_setter(instance):
    original = instance.Database_Access
    instance.Database_Access = original
    assert instance.Database_Access == original



@given(instance=Thick_Client_Users_strategy)
def test_thick_client_users_View_User_setter(instance):
    original = instance.View_User
    instance.View_User = original
    assert instance.View_User == original
