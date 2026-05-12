import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    Contacts,
    Message,
    Bubbles,
    Meetings,
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



def test_contacts_is_not_abstract():
    assert not inspect.isabstract(Contacts)


def test_contacts_constructor_exists():
    assert callable(Contacts.__init__)


def test_contacts_constructor_args():
    sig = inspect.signature(Contacts.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_bubbles_is_not_abstract():
    assert not inspect.isabstract(Bubbles)


def test_bubbles_constructor_exists():
    assert callable(Bubbles.__init__)


def test_bubbles_constructor_args():
    sig = inspect.signature(Bubbles.__init__)
    params = list(sig.parameters.keys())



def test_meetings_is_not_abstract():
    assert not inspect.isabstract(Meetings)


def test_meetings_constructor_exists():
    assert callable(Meetings.__init__)


def test_meetings_constructor_args():
    sig = inspect.signature(Meetings.__init__)
    params = list(sig.parameters.keys())



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())


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
)
Contacts_strategy = st.builds(
    Contacts,
)
Message_strategy = st.builds(
    Message,
)
Bubbles_strategy = st.builds(
    Bubbles,
)
Meetings_strategy = st.builds(
    Meetings,
)
Profile_strategy = st.builds(
    Profile,
)
User_strategy = st.builds(
    User,
)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)

@given(instance=Contacts_strategy)
@settings(max_examples=50)
def test_contacts_instantiation(instance):
    assert isinstance(instance, Contacts)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=Bubbles_strategy)
@settings(max_examples=50)
def test_bubbles_instantiation(instance):
    assert isinstance(instance, Bubbles)

@given(instance=Meetings_strategy)
@settings(max_examples=50)
def test_meetings_instantiation(instance):
    assert isinstance(instance, Meetings)

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)
