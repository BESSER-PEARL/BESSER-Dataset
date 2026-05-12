import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Search,
    Login,
    Post,
    Club,
    User,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())



def test_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_post_constructor_exists():
    assert callable(Post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())



def test_club_is_not_abstract():
    assert not inspect.isabstract(Club)


def test_club_constructor_exists():
    assert callable(Club.__init__)


def test_club_constructor_args():
    sig = inspect.signature(Club.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
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
Search_strategy = st.builds(
    Search,
)
Login_strategy = st.builds(
    Login,
)
Post_strategy = st.builds(
    Post,
)
Club_strategy = st.builds(
    Club,
)
User_strategy = st.builds(
    User,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)

@given(instance=Post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, Post)

@given(instance=Club_strategy)
@settings(max_examples=50)
def test_club_instantiation(instance):
    assert isinstance(instance, Club)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
