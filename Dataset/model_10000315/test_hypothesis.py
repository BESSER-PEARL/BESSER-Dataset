import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Alumni,
    Admin,
    HomePage,
    Message,
    Friend,
    Student,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alumni_is_not_abstract():
    assert not inspect.isabstract(Alumni)


def test_alumni_constructor_exists():
    assert callable(Alumni.__init__)


def test_alumni_constructor_args():
    sig = inspect.signature(Alumni.__init__)
    params = list(sig.parameters.keys())
    assert "Report" in params, "Missing parameter 'Report'"
    assert "__M" in params, "Missing parameter '__M'"
    assert "_F" in params, "Missing parameter '_F'"

def test_alumni_has_Report():
    assert hasattr(Alumni, "Report")
    descriptor = None
    for klass in Alumni.__mro__:
        if "Report" in klass.__dict__:
            descriptor = klass.__dict__["Report"]
            break
    assert isinstance(descriptor, property)

def test_alumni_has___M():
    assert hasattr(Alumni, "__M")
    descriptor = None
    for klass in Alumni.__mro__:
        if "__M" in klass.__dict__:
            descriptor = klass.__dict__["__M"]
            break
    assert isinstance(descriptor, property)

def test_alumni_has__F():
    assert hasattr(Alumni, "_F")
    descriptor = None
    for klass in Alumni.__mro__:
        if "_F" in klass.__dict__:
            descriptor = klass.__dict__["_F"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_homepage_is_not_abstract():
    assert not inspect.isabstract(HomePage)


def test_homepage_constructor_exists():
    assert callable(HomePage.__init__)


def test_homepage_constructor_args():
    sig = inspect.signature(HomePage.__init__)
    params = list(sig.parameters.keys())
    assert "__friendpost" in params, "Missing parameter '__friendpost'"

def test_homepage_has___friendpost():
    assert hasattr(HomePage, "__friendpost")
    descriptor = None
    for klass in HomePage.__mro__:
        if "__friendpost" in klass.__dict__:
            descriptor = klass.__dict__["__friendpost"]
            break
    assert isinstance(descriptor, property)



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "reciver" in params, "Missing parameter 'reciver'"
    assert "message" in params, "Missing parameter 'message'"
    assert "sender" in params, "Missing parameter 'sender'"

def test_message_has_reciver():
    assert hasattr(Message, "reciver")
    descriptor = None
    for klass in Message.__mro__:
        if "reciver" in klass.__dict__:
            descriptor = klass.__dict__["reciver"]
            break
    assert isinstance(descriptor, property)

def test_message_has_message():
    assert hasattr(Message, "message")
    descriptor = None
    for klass in Message.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_message_has_sender():
    assert hasattr(Message, "sender")
    descriptor = None
    for klass in Message.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)



def test_friend_is_not_abstract():
    assert not inspect.isabstract(Friend)


def test_friend_constructor_exists():
    assert callable(Friend.__init__)


def test_friend_constructor_args():
    sig = inspect.signature(Friend.__init__)
    params = list(sig.parameters.keys())
    assert "friend____" in params, "Missing parameter 'friend____'"
    assert "acceptornot" in params, "Missing parameter 'acceptornot'"

def test_friend_has_friend____():
    assert hasattr(Friend, "friend____")
    descriptor = None
    for klass in Friend.__mro__:
        if "friend____" in klass.__dict__:
            descriptor = klass.__dict__["friend____"]
            break
    assert isinstance(descriptor, property)

def test_friend_has_acceptornot():
    assert hasattr(Friend, "acceptornot")
    descriptor = None
    for klass in Friend.__mro__:
        if "acceptornot" in klass.__dict__:
            descriptor = klass.__dict__["acceptornot"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "__M" in params, "Missing parameter '__M'"
    assert "Report" in params, "Missing parameter 'Report'"
    assert "_F" in params, "Missing parameter '_F'"

def test_student_has___M():
    assert hasattr(Student, "__M")
    descriptor = None
    for klass in Student.__mro__:
        if "__M" in klass.__dict__:
            descriptor = klass.__dict__["__M"]
            break
    assert isinstance(descriptor, property)

def test_student_has_Report():
    assert hasattr(Student, "Report")
    descriptor = None
    for klass in Student.__mro__:
        if "Report" in klass.__dict__:
            descriptor = klass.__dict__["Report"]
            break
    assert isinstance(descriptor, property)

def test_student_has__F():
    assert hasattr(Student, "_F")
    descriptor = None
    for klass in Student.__mro__:
        if "_F" in klass.__dict__:
            descriptor = klass.__dict__["_F"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "Branch" in params, "Missing parameter 'Branch'"
    assert "name" in params, "Missing parameter 'name'"
    assert "class" in params, "Missing parameter 'class'"
    assert "email" in params, "Missing parameter 'email'"

def test_account_has_password():
    assert hasattr(Account, "password")
    descriptor = None
    for klass in Account.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Department():
    assert hasattr(Account, "Department")
    descriptor = None
    for klass in Account.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Branch():
    assert hasattr(Account, "Branch")
    descriptor = None
    for klass in Account.__mro__:
        if "Branch" in klass.__dict__:
            descriptor = klass.__dict__["Branch"]
            break
    assert isinstance(descriptor, property)

def test_account_has_name():
    assert hasattr(Account, "name")
    descriptor = None
    for klass in Account.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_account_has_class():
    assert hasattr(Account, "class")
    descriptor = None
    for klass in Account.__mro__:
        if "class" in klass.__dict__:
            descriptor = klass.__dict__["class"]
            break
    assert isinstance(descriptor, property)

def test_account_has_email():
    assert hasattr(Account, "email")
    descriptor = None
    for klass in Account.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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
Alumni_strategy = st.builds(
    Alumni,
    Report=
        st.none(),
    __M=
        st.none(),
    _F=
        st.none()
)
Admin_strategy = st.builds(
    Admin,
)
HomePage_strategy = st.builds(
    HomePage,
    __friendpost=
        st.none()
)
Message_strategy = st.builds(
    Message,
    reciver=
        safe_text,
    message=
        safe_text,
    sender=
        safe_text
)
Friend_strategy = st.builds(
    Friend,
    friend____=
        safe_text,
    acceptornot=
        st.booleans()
)
Student_strategy = st.builds(
    Student,
    __M=
        st.none(),
    Report=
        st.none(),
    _F=
        st.none()
)
Account_strategy = st.builds(
    Account,
    password=
        safe_text,
    Department=
        safe_text,
    Branch=
        safe_text,
    name=
        safe_text,
    class=
        safe_text,
    email=
        safe_text
)

@given(instance=Alumni_strategy)
@settings(max_examples=50)
def test_alumni_instantiation(instance):
    assert isinstance(instance, Alumni)



@given(instance=Alumni_strategy)
def test_alumni_Report_setter(instance):
    original = instance.Report
    instance.Report = original
    assert instance.Report == original



@given(instance=Alumni_strategy)
def test_alumni___M_setter(instance):
    original = instance.__M
    instance.__M = original
    assert instance.__M == original



@given(instance=Alumni_strategy)
def test_alumni__F_setter(instance):
    original = instance._F
    instance._F = original
    assert instance._F == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=HomePage_strategy)
@settings(max_examples=50)
def test_homepage_instantiation(instance):
    assert isinstance(instance, HomePage)



@given(instance=HomePage_strategy)
def test_homepage___friendpost_setter(instance):
    original = instance.__friendpost
    instance.__friendpost = original
    assert instance.__friendpost == original

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)



@given(instance=Message_strategy)
def test_message_reciver_setter(instance):
    original = instance.reciver
    instance.reciver = original
    assert instance.reciver == original



@given(instance=Message_strategy)
def test_message_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Message_strategy)
def test_message_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original

@given(instance=Friend_strategy)
@settings(max_examples=50)
def test_friend_instantiation(instance):
    assert isinstance(instance, Friend)



@given(instance=Friend_strategy)
def test_friend_friend_____setter(instance):
    original = instance.friend____
    instance.friend____ = original
    assert instance.friend____ == original



@given(instance=Friend_strategy)
def test_friend_acceptornot_setter(instance):
    original = instance.acceptornot
    instance.acceptornot = original
    assert instance.acceptornot == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student___M_setter(instance):
    original = instance.__M
    instance.__M = original
    assert instance.__M == original



@given(instance=Student_strategy)
def test_student_Report_setter(instance):
    original = instance.Report
    instance.Report = original
    assert instance.Report == original



@given(instance=Student_strategy)
def test_student__F_setter(instance):
    original = instance._F
    instance._F = original
    assert instance._F == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Account_strategy)
def test_account_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Account_strategy)
def test_account_Branch_setter(instance):
    original = instance.Branch
    instance.Branch = original
    assert instance.Branch == original



@given(instance=Account_strategy)
def test_account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Account_strategy)
def test_account_class_setter(instance):
    original = instance.class
    instance.class = original
    assert instance.class == original



@given(instance=Account_strategy)
def test_account_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
