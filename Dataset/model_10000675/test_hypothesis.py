import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    T1,
    T,
    Hola,
    Login,
    Friend,
    Message,
    Group,
    Post,
    Profile,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_t1_is_not_abstract():
    assert not inspect.isabstract(T1)


def test_t1_constructor_exists():
    assert callable(T1.__init__)


def test_t1_constructor_args():
    sig = inspect.signature(T1.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_hola_is_not_abstract():
    assert not inspect.isabstract(Hola)


def test_hola_constructor_exists():
    assert callable(Hola.__init__)


def test_hola_constructor_args():
    sig = inspect.signature(Hola.__init__)
    params = list(sig.parameters.keys())
    assert "hppal" in params, "Missing parameter 'hppal'"

def test_hola_has_hppal():
    assert hasattr(Hola, "hppal")
    descriptor = None
    for klass in Hola.__mro__:
        if "hppal" in klass.__dict__:
            descriptor = klass.__dict__["hppal"]
            break
    assert isinstance(descriptor, property)



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
T1_strategy = st.builds(
    T1,
)
T_strategy = st.builds(
    T,
)
Hola_strategy = st.builds(
    Hola,
    hppal=
        safe_text
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
Profile_strategy = st.builds(
    Profile,
)
User_strategy = st.builds(
    User,
)

@given(instance=T1_strategy)
@settings(max_examples=50)
def test_t1_instantiation(instance):
    assert isinstance(instance, T1)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Hola_strategy)
@settings(max_examples=50)
def test_hola_instantiation(instance):
    assert isinstance(instance, Hola)



@given(instance=Hola_strategy)
def test_hola_hppal_setter(instance):
    original = instance.hppal
    instance.hppal = original
    assert instance.hppal == original

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

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)
