import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Route,
    Class,
    Routing_System_Actor,
    User_Actor,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_route_is_not_abstract():
    assert not inspect.isabstract(Route)


def test_route_constructor_exists():
    assert callable(Route.__init__)


def test_route_constructor_args():
    sig = inspect.signature(Route.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_routing_system_actor_is_not_abstract():
    assert not inspect.isabstract(Routing_System_Actor)


def test_routing_system_actor_constructor_exists():
    assert callable(Routing_System_Actor.__init__)


def test_routing_system_actor_constructor_args():
    sig = inspect.signature(Routing_System_Actor.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
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
Route_strategy = st.builds(
    Route,
)
Class_strategy = st.builds(
    Class,
)
Routing_System_Actor_strategy = st.builds(
    Routing_System_Actor,
)
User_Actor_strategy = st.builds(
    User_Actor,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=Route_strategy)
@settings(max_examples=50)
def test_route_instantiation(instance):
    assert isinstance(instance, Route)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Routing_System_Actor_strategy)
@settings(max_examples=50)
def test_routing_system_actor_instantiation(instance):
    assert isinstance(instance, Routing_System_Actor)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
