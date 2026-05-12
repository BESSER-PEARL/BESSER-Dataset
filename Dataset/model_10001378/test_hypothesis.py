import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class2,
    Class,
    UseCase3_UseCase,
    UseCase2_UseCase,
    Actor3_Actor,
    Actor2_Actor,
    UseCase_UseCase,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_usecase3_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase3_UseCase)


def test_usecase3_usecase_constructor_exists():
    assert callable(UseCase3_UseCase.__init__)


def test_usecase3_usecase_constructor_args():
    sig = inspect.signature(UseCase3_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase2_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase2_UseCase)


def test_usecase2_usecase_constructor_exists():
    assert callable(UseCase2_UseCase.__init__)


def test_usecase2_usecase_constructor_args():
    sig = inspect.signature(UseCase2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actor3_actor_is_not_abstract():
    assert not inspect.isabstract(Actor3_Actor)


def test_actor3_actor_constructor_exists():
    assert callable(Actor3_Actor.__init__)


def test_actor3_actor_constructor_args():
    sig = inspect.signature(Actor3_Actor.__init__)
    params = list(sig.parameters.keys())



def test_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
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
Class2_strategy = st.builds(
    Class2,
)
Class_strategy = st.builds(
    Class,
)
UseCase3_UseCase_strategy = st.builds(
    UseCase3_UseCase,
)
UseCase2_UseCase_strategy = st.builds(
    UseCase2_UseCase,
)
Actor3_Actor_strategy = st.builds(
    Actor3_Actor,
)
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UseCase3_UseCase_strategy)
@settings(max_examples=50)
def test_usecase3_usecase_instantiation(instance):
    assert isinstance(instance, UseCase3_UseCase)

@given(instance=UseCase2_UseCase_strategy)
@settings(max_examples=50)
def test_usecase2_usecase_instantiation(instance):
    assert isinstance(instance, UseCase2_UseCase)

@given(instance=Actor3_Actor_strategy)
@settings(max_examples=50)
def test_actor3_actor_instantiation(instance):
    assert isinstance(instance, Actor3_Actor)

@given(instance=Actor2_Actor_strategy)
@settings(max_examples=50)
def test_actor2_actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
