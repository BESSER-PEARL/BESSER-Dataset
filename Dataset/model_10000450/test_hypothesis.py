import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HomePage,
    Photos,
    Message,
    Friend,
    User,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_homepage_is_not_abstract():
    assert not inspect.isabstract(HomePage)


def test_homepage_constructor_exists():
    assert callable(HomePage.__init__)


def test_homepage_constructor_args():
    sig = inspect.signature(HomePage.__init__)
    params = list(sig.parameters.keys())
    assert "likeorunlike" in params, "Missing parameter 'likeorunlike'"
    assert "__friendStatus" in params, "Missing parameter '__friendStatus'"
    assert "__status" in params, "Missing parameter '__status'"

def test_homepage_has_likeorunlike():
    assert hasattr(HomePage, "likeorunlike")
    descriptor = None
    for klass in HomePage.__mro__:
        if "likeorunlike" in klass.__dict__:
            descriptor = klass.__dict__["likeorunlike"]
            break
    assert isinstance(descriptor, property)

def test_homepage_has___friendStatus():
    assert hasattr(HomePage, "__friendStatus")
    descriptor = None
    for klass in HomePage.__mro__:
        if "__friendStatus" in klass.__dict__:
            descriptor = klass.__dict__["__friendStatus"]
            break
    assert isinstance(descriptor, property)

def test_homepage_has___status():
    assert hasattr(HomePage, "__status")
    descriptor = None
    for klass in HomePage.__mro__:
        if "__status" in klass.__dict__:
            descriptor = klass.__dict__["__status"]
            break
    assert isinstance(descriptor, property)



def test_photos_is_not_abstract():
    assert not inspect.isabstract(Photos)


def test_photos_constructor_exists():
    assert callable(Photos.__init__)


def test_photos_constructor_args():
    sig = inspect.signature(Photos.__init__)
    params = list(sig.parameters.keys())
    assert "__photos" in params, "Missing parameter '__photos'"

def test_photos_has___photos():
    assert hasattr(Photos, "__photos")
    descriptor = None
    for klass in Photos.__mro__:
        if "__photos" in klass.__dict__:
            descriptor = klass.__dict__["__photos"]
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
    assert "sender" in params, "Missing parameter 'sender'"
    assert "message" in params, "Missing parameter 'message'"

def test_message_has_reciver():
    assert hasattr(Message, "reciver")
    descriptor = None
    for klass in Message.__mro__:
        if "reciver" in klass.__dict__:
            descriptor = klass.__dict__["reciver"]
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

def test_message_has_message():
    assert hasattr(Message, "message")
    descriptor = None
    for klass in Message.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
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



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "_F" in params, "Missing parameter '_F'"
    assert "_P" in params, "Missing parameter '_P'"
    assert "__M" in params, "Missing parameter '__M'"

def test_user_has__F():
    assert hasattr(User, "_F")
    descriptor = None
    for klass in User.__mro__:
        if "_F" in klass.__dict__:
            descriptor = klass.__dict__["_F"]
            break
    assert isinstance(descriptor, property)

def test_user_has__P():
    assert hasattr(User, "_P")
    descriptor = None
    for klass in User.__mro__:
        if "_P" in klass.__dict__:
            descriptor = klass.__dict__["_P"]
            break
    assert isinstance(descriptor, property)

def test_user_has___M():
    assert hasattr(User, "__M")
    descriptor = None
    for klass in User.__mro__:
        if "__M" in klass.__dict__:
            descriptor = klass.__dict__["__M"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "entity" in params, "Missing parameter 'entity'"
    assert "name" in params, "Missing parameter 'name'"

def test_account_has_email():
    assert hasattr(Account, "email")
    descriptor = None
    for klass in Account.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_account_has_password():
    assert hasattr(Account, "password")
    descriptor = None
    for klass in Account.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_account_has_entity():
    assert hasattr(Account, "entity")
    descriptor = None
    for klass in Account.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
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
HomePage_strategy = st.builds(
    HomePage,
    likeorunlike=
        st.booleans(),
    __friendStatus=
        safe_text,
    __status=
        safe_text
)
Photos_strategy = st.builds(
    Photos,
    __photos=
        safe_text
)
Message_strategy = st.builds(
    Message,
    reciver=
        safe_text,
    sender=
        safe_text,
    message=
        safe_text
)
Friend_strategy = st.builds(
    Friend,
    friend____=
        safe_text,
    acceptornot=
        st.booleans()
)
User_strategy = st.builds(
    User,
    _F=
        st.none(),
    _P=
        st.none(),
    __M=
        st.none()
)
Account_strategy = st.builds(
    Account,
    email=
        safe_text,
    password=
        safe_text,
    entity=
        safe_text,
    name=
        safe_text
)

@given(instance=HomePage_strategy)
@settings(max_examples=50)
def test_homepage_instantiation(instance):
    assert isinstance(instance, HomePage)



@given(instance=HomePage_strategy)
def test_homepage_likeorunlike_setter(instance):
    original = instance.likeorunlike
    instance.likeorunlike = original
    assert instance.likeorunlike == original



@given(instance=HomePage_strategy)
def test_homepage___friendStatus_setter(instance):
    original = instance.__friendStatus
    instance.__friendStatus = original
    assert instance.__friendStatus == original



@given(instance=HomePage_strategy)
def test_homepage___status_setter(instance):
    original = instance.__status
    instance.__status = original
    assert instance.__status == original

@given(instance=Photos_strategy)
@settings(max_examples=50)
def test_photos_instantiation(instance):
    assert isinstance(instance, Photos)



@given(instance=Photos_strategy)
def test_photos___photos_setter(instance):
    original = instance.__photos
    instance.__photos = original
    assert instance.__photos == original

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
def test_message_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original



@given(instance=Message_strategy)
def test_message_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

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

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user__F_setter(instance):
    original = instance._F
    instance._F = original
    assert instance._F == original



@given(instance=User_strategy)
def test_user__P_setter(instance):
    original = instance._P
    instance._P = original
    assert instance._P == original



@given(instance=User_strategy)
def test_user___M_setter(instance):
    original = instance.__M
    instance.__M = original
    assert instance.__M == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Account_strategy)
def test_account_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Account_strategy)
def test_account_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original



@given(instance=Account_strategy)
def test_account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
