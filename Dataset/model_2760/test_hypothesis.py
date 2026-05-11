import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractClassB,
    opposite2::ConcreteEndB2,
    opposite2::ConcreteEndB1,
    opposite2::AbstractClassB,
    opposite2::EndA,
    opposite2::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractclassb_is_not_abstract():
    assert not inspect.isabstract(AbstractClassB)


def test_abstractclassb_constructor_exists():
    assert callable(AbstractClassB.__init__)


def test_abstractclassb_constructor_args():
    sig = inspect.signature(AbstractClassB.__init__)
    params = list(sig.parameters.keys())



def test_opposite2::concreteendb2_is_not_abstract():
    assert not inspect.isabstract(opposite2::ConcreteEndB2)


def test_opposite2::concreteendb2_constructor_exists():
    assert callable(opposite2::ConcreteEndB2.__init__)


def test_opposite2::concreteendb2_constructor_args():
    sig = inspect.signature(opposite2::ConcreteEndB2.__init__)
    params = list(sig.parameters.keys())



def test_opposite2::concreteendb1_is_not_abstract():
    assert not inspect.isabstract(opposite2::ConcreteEndB1)


def test_opposite2::concreteendb1_constructor_exists():
    assert callable(opposite2::ConcreteEndB1.__init__)


def test_opposite2::concreteendb1_constructor_args():
    sig = inspect.signature(opposite2::ConcreteEndB1.__init__)
    params = list(sig.parameters.keys())



def test_opposite2::abstractclassb_is_not_abstract():
    assert not inspect.isabstract(opposite2::AbstractClassB)


def test_opposite2::abstractclassb_constructor_exists():
    assert callable(opposite2::AbstractClassB.__init__)


def test_opposite2::abstractclassb_constructor_args():
    sig = inspect.signature(opposite2::AbstractClassB.__init__)
    params = list(sig.parameters.keys())



def test_opposite2::enda_is_not_abstract():
    assert not inspect.isabstract(opposite2::EndA)


def test_opposite2::enda_constructor_exists():
    assert callable(opposite2::EndA.__init__)


def test_opposite2::enda_constructor_args():
    sig = inspect.signature(opposite2::EndA.__init__)
    params = list(sig.parameters.keys())



def test_opposite2::root_is_not_abstract():
    assert not inspect.isabstract(opposite2::Root)


def test_opposite2::root_constructor_exists():
    assert callable(opposite2::Root.__init__)


def test_opposite2::root_constructor_args():
    sig = inspect.signature(opposite2::Root.__init__)
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
AbstractClassB_strategy = st.builds(
    AbstractClassB,
)
opposite2::ConcreteEndB2_strategy = st.builds(
    opposite2::ConcreteEndB2,
)
opposite2::ConcreteEndB1_strategy = st.builds(
    opposite2::ConcreteEndB1,
)
opposite2::AbstractClassB_strategy = st.builds(
    opposite2::AbstractClassB,
)
opposite2::EndA_strategy = st.builds(
    opposite2::EndA,
)
opposite2::Root_strategy = st.builds(
    opposite2::Root,
)

@given(instance=AbstractClassB_strategy)
@settings(max_examples=50)
def test_abstractclassb_instantiation(instance):
    assert isinstance(instance, AbstractClassB)

@given(instance=opposite2::ConcreteEndB2_strategy)
@settings(max_examples=50)
def test_opposite2::concreteendb2_instantiation(instance):
    assert isinstance(instance, opposite2::ConcreteEndB2)

@given(instance=opposite2::ConcreteEndB1_strategy)
@settings(max_examples=50)
def test_opposite2::concreteendb1_instantiation(instance):
    assert isinstance(instance, opposite2::ConcreteEndB1)

@given(instance=opposite2::AbstractClassB_strategy)
@settings(max_examples=50)
def test_opposite2::abstractclassb_instantiation(instance):
    assert isinstance(instance, opposite2::AbstractClassB)

@given(instance=opposite2::EndA_strategy)
@settings(max_examples=50)
def test_opposite2::enda_instantiation(instance):
    assert isinstance(instance, opposite2::EndA)

@given(instance=opposite2::Root_strategy)
@settings(max_examples=50)
def test_opposite2::root_instantiation(instance):
    assert isinstance(instance, opposite2::Root)
