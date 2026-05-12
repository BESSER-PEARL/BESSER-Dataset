import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IAcc_Interface,
    Comment,
    Administrator,
    Project,
    User,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iacc_interface_is_not_abstract():
    assert not inspect.isabstract(IAcc_Interface)


def test_iacc_interface_constructor_exists():
    assert callable(IAcc_Interface.__init__)


def test_iacc_interface_constructor_args():
    sig = inspect.signature(IAcc_Interface.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())
    assert "Body" in params, "Missing parameter 'Body'"
    assert "CreationDate" in params, "Missing parameter 'CreationDate'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "Creator" in params, "Missing parameter 'Creator'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_comment_has_Body():
    assert hasattr(Comment, "Body")
    descriptor = None
    for klass in Comment.__mro__:
        if "Body" in klass.__dict__:
            descriptor = klass.__dict__["Body"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_CreationDate():
    assert hasattr(Comment, "CreationDate")
    descriptor = None
    for klass in Comment.__mro__:
        if "CreationDate" in klass.__dict__:
            descriptor = klass.__dict__["CreationDate"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Title():
    assert hasattr(Comment, "Title")
    descriptor = None
    for klass in Comment.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Creator():
    assert hasattr(Comment, "Creator")
    descriptor = None
    for klass in Comment.__mro__:
        if "Creator" in klass.__dict__:
            descriptor = klass.__dict__["Creator"]
            break
    assert isinstance(descriptor, property)

def test_comment_has_Id():
    assert hasattr(Comment, "Id")
    descriptor = None
    for klass in Comment.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"

def test_administrator_has_Id():
    assert hasattr(Administrator, "Id")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())
    assert "Info" in params, "Missing parameter 'Info'"
    assert "Access" in params, "Missing parameter 'Access'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "State" in params, "Missing parameter 'State'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_project_has_Info():
    assert hasattr(Project, "Info")
    descriptor = None
    for klass in Project.__mro__:
        if "Info" in klass.__dict__:
            descriptor = klass.__dict__["Info"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Access():
    assert hasattr(Project, "Access")
    descriptor = None
    for klass in Project.__mro__:
        if "Access" in klass.__dict__:
            descriptor = klass.__dict__["Access"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Title():
    assert hasattr(Project, "Title")
    descriptor = None
    for klass in Project.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_project_has_State():
    assert hasattr(Project, "State")
    descriptor = None
    for klass in Project.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_project_has_Id():
    assert hasattr(Project, "Id")
    descriptor = None
    for klass in Project.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"

def test_user_has_Id():
    assert hasattr(User, "Id")
    descriptor = None
    for klass in User.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Info" in params, "Missing parameter 'Info'"

def test_account_has_UserName():
    assert hasattr(Account, "UserName")
    descriptor = None
    for klass in Account.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Info():
    assert hasattr(Account, "Info")
    descriptor = None
    for klass in Account.__mro__:
        if "Info" in klass.__dict__:
            descriptor = klass.__dict__["Info"]
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
IAcc_Interface_strategy = st.builds(
    IAcc_Interface,
)
Comment_strategy = st.builds(
    Comment,
    Body=
        safe_text,
    CreationDate=
        safe_text,
    Title=
        safe_text,
    Creator=
        st.none(),
    Id=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    Id=
        st.integers()
)
Project_strategy = st.builds(
    Project,
    Info=
        safe_text,
    Access=
        safe_text,
    Title=
        safe_text,
    State=
        safe_text,
    Id=
        st.integers()
)
User_strategy = st.builds(
    User,
    Id=
        st.integers()
)
Account_strategy = st.builds(
    Account,
    UserName=
        safe_text,
    Info=
        safe_text
)

@given(instance=IAcc_Interface_strategy)
@settings(max_examples=50)
def test_iacc_interface_instantiation(instance):
    assert isinstance(instance, IAcc_Interface)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)



@given(instance=Comment_strategy)
def test_comment_Body_setter(instance):
    original = instance.Body
    instance.Body = original
    assert instance.Body == original



@given(instance=Comment_strategy)
def test_comment_CreationDate_setter(instance):
    original = instance.CreationDate
    instance.CreationDate = original
    assert instance.CreationDate == original



@given(instance=Comment_strategy)
def test_comment_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Comment_strategy)
def test_comment_Creator_setter(instance):
    original = instance.Creator
    instance.Creator = original
    assert instance.Creator == original



@given(instance=Comment_strategy)
def test_comment_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)



@given(instance=Project_strategy)
def test_project_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original



@given(instance=Project_strategy)
def test_project_Access_setter(instance):
    original = instance.Access
    instance.Access = original
    assert instance.Access == original



@given(instance=Project_strategy)
def test_project_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Project_strategy)
def test_project_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Project_strategy)
def test_project_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Account_strategy)
def test_account_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original
