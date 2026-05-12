import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Locatable_Interface,
    Login,
    Friend,
    Message,
    Group,
    Post,
    Locatable,
    Home,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_locatable_interface_is_not_abstract():
    assert not inspect.isabstract(Locatable_Interface)


def test_locatable_interface_constructor_exists():
    assert callable(Locatable_Interface.__init__)


def test_locatable_interface_constructor_args():
    sig = inspect.signature(Locatable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())



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



def test_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_group_constructor_exists():
    assert callable(Group.__init__)


def test_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())



def test_locatable_is_not_abstract():
    assert not inspect.isabstract(Locatable)


def test_locatable_constructor_exists():
    assert callable(Locatable.__init__)


def test_locatable_constructor_args():
    sig = inspect.signature(Locatable.__init__)
    params = list(sig.parameters.keys())



def test_home_is_not_abstract():
    assert not inspect.isabstract(Home)


def test_home_constructor_exists():
    assert callable(Home.__init__)


def test_home_constructor_args():
    sig = inspect.signature(Home.__init__)
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
Locatable_Interface_strategy = st.builds(
    Locatable_Interface,
)
Login_strategy = st.builds(
    Login,
)
Friend_strategy = st.builds(
    Friend,
)
Message_strategy = st.builds(
    Message,
)
Group_strategy = st.builds(
    Group,
)
Post_strategy = st.builds(
    Post,
)
Locatable_strategy = st.builds(
    Locatable,
)
Home_strategy = st.builds(
    Home,
)

@given(instance=Locatable_Interface_strategy)
@settings(max_examples=50)
def test_locatable_interface_instantiation(instance):
    assert isinstance(instance, Locatable_Interface)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)

@given(instance=Friend_strategy)
@settings(max_examples=50)
def test_friend_instantiation(instance):
    assert isinstance(instance, Friend)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=Group_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, Group)

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)

@given(instance=Locatable_strategy)
@settings(max_examples=50)
def test_locatable_instantiation(instance):
    assert isinstance(instance, Locatable)

@given(instance=Home_strategy)
@settings(max_examples=50)
def test_home_instantiation(instance):
    assert isinstance(instance, Home)
