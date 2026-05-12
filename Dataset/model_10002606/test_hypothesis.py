import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    USER_TYPE,
    POST,
    CATEGORY,
    User,
    Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_user_type_is_not_abstract():
    assert not inspect.isabstract(USER_TYPE)


def test_user_type_constructor_exists():
    assert callable(USER_TYPE.__init__)


def test_user_type_constructor_args():
    sig = inspect.signature(USER_TYPE.__init__)
    params = list(sig.parameters.keys())



def test_post_is_not_abstract():
    assert not inspect.isabstract(POST)


def test_post_constructor_exists():
    assert callable(POST.__init__)


def test_post_constructor_args():
    sig = inspect.signature(POST.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_post_has_name():
    assert hasattr(POST, "name")
    descriptor = None
    for klass in POST.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(CATEGORY)


def test_category_constructor_exists():
    assert callable(CATEGORY.__init__)


def test_category_constructor_args():
    sig = inspect.signature(CATEGORY.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
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
USER_TYPE_strategy = st.builds(
    USER_TYPE,
)
POST_strategy = st.builds(
    POST,
    name=
        safe_text
)
CATEGORY_strategy = st.builds(
    CATEGORY,
)
User_strategy = st.builds(
    User,
)
Admin_strategy = st.builds(
    Admin,
)

@given(instance=USER_TYPE_strategy)
@settings(max_examples=50)
def test_user_type_instantiation(instance):
    assert isinstance(instance, USER_TYPE)

@given(instance=POST_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, POST)



@given(instance=POST_strategy)
def test_post_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CATEGORY_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, CATEGORY)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)
