import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Actor_Actor,
    UseCase7_UseCase,
    UseCase6_UseCase,
    Class,
    UseCase5_UseCase,
    UseCase4_UseCase,
    UseCase3_UseCase,
    UseCase2_UseCase,
    UseCase_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase7_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase7_UseCase)


def test_usecase7_usecase_constructor_exists():
    assert callable(UseCase7_UseCase.__init__)


def test_usecase7_usecase_constructor_args():
    sig = inspect.signature(UseCase7_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase6_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase6_UseCase)


def test_usecase6_usecase_constructor_exists():
    assert callable(UseCase6_UseCase.__init__)


def test_usecase6_usecase_constructor_args():
    sig = inspect.signature(UseCase6_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_usecase5_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase5_UseCase)


def test_usecase5_usecase_constructor_exists():
    assert callable(UseCase5_UseCase.__init__)


def test_usecase5_usecase_constructor_args():
    sig = inspect.signature(UseCase5_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase4_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase4_UseCase)


def test_usecase4_usecase_constructor_exists():
    assert callable(UseCase4_UseCase.__init__)


def test_usecase4_usecase_constructor_args():
    sig = inspect.signature(UseCase4_UseCase.__init__)
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



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
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
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
UseCase7_UseCase_strategy = st.builds(
    UseCase7_UseCase,
)
UseCase6_UseCase_strategy = st.builds(
    UseCase6_UseCase,
)
Class_strategy = st.builds(
    Class,
)
UseCase5_UseCase_strategy = st.builds(
    UseCase5_UseCase,
)
UseCase4_UseCase_strategy = st.builds(
    UseCase4_UseCase,
)
UseCase3_UseCase_strategy = st.builds(
    UseCase3_UseCase,
)
UseCase2_UseCase_strategy = st.builds(
    UseCase2_UseCase,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=UseCase7_UseCase_strategy)
@settings(max_examples=50)
def test_usecase7_usecase_instantiation(instance):
    assert isinstance(instance, UseCase7_UseCase)

@given(instance=UseCase6_UseCase_strategy)
@settings(max_examples=50)
def test_usecase6_usecase_instantiation(instance):
    assert isinstance(instance, UseCase6_UseCase)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UseCase5_UseCase_strategy)
@settings(max_examples=50)
def test_usecase5_usecase_instantiation(instance):
    assert isinstance(instance, UseCase5_UseCase)

@given(instance=UseCase4_UseCase_strategy)
@settings(max_examples=50)
def test_usecase4_usecase_instantiation(instance):
    assert isinstance(instance, UseCase4_UseCase)

@given(instance=UseCase3_UseCase_strategy)
@settings(max_examples=50)
def test_usecase3_usecase_instantiation(instance):
    assert isinstance(instance, UseCase3_UseCase)

@given(instance=UseCase2_UseCase_strategy)
@settings(max_examples=50)
def test_usecase2_usecase_instantiation(instance):
    assert isinstance(instance, UseCase2_UseCase)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)
