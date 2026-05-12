import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    post,
    club,
    Actor_Actor,
    Actor1_Actor,
    user_Actor,
    Search,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_post_is_not_abstract():
    assert not inspect.isabstract(post)


def test_post_constructor_exists():
    assert callable(post.__init__)


def test_post_constructor_args():
    sig = inspect.signature(post.__init__)
    params = list(sig.parameters.keys())



def test_club_is_not_abstract():
    assert not inspect.isabstract(club)


def test_club_constructor_exists():
    assert callable(club.__init__)


def test_club_constructor_args():
    sig = inspect.signature(club.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor1_actor_is_not_abstract():
    assert not inspect.isabstract(Actor1_Actor)


def test_actor1_actor_constructor_exists():
    assert callable(Actor1_Actor.__init__)


def test_actor1_actor_constructor_args():
    sig = inspect.signature(Actor1_Actor.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(user_Actor)


def test_user_actor_constructor_exists():
    assert callable(user_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(user_Actor.__init__)
    params = list(sig.parameters.keys())



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
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
post_strategy = st.builds(
    post,
)
club_strategy = st.builds(
    club,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Actor1_Actor_strategy = st.builds(
    Actor1_Actor,
)
user_Actor_strategy = st.builds(
    user_Actor,
)
Search_strategy = st.builds(
    Search,
)

@given(instance=post_strategy)
@settings(max_examples=50)
def test_post_instantiation(instance):
    assert isinstance(instance, post)

@given(instance=club_strategy)
@settings(max_examples=50)
def test_club_instantiation(instance):
    assert isinstance(instance, club)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Actor1_Actor_strategy)
@settings(max_examples=50)
def test_actor1_actor_instantiation(instance):
    assert isinstance(instance, Actor1_Actor)

@given(instance=user_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, user_Actor)

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)
