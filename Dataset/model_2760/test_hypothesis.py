import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractClassB,
    opposite2_ConcreteEndB2,
    opposite2_ConcreteEndB1,
    opposite2_AbstractClassB,
    opposite2_EndA,
    opposite2_Root,
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



def test_opposite2_concreteendb2_is_not_abstract():
    assert not inspect.isabstract(opposite2_ConcreteEndB2)


def test_opposite2_concreteendb2_constructor_exists():
    assert callable(opposite2_ConcreteEndB2.__init__)


def test_opposite2_concreteendb2_constructor_args():
    sig = inspect.signature(opposite2_ConcreteEndB2.__init__)
    params = list(sig.parameters.keys())



def test_opposite2_concreteendb1_is_not_abstract():
    assert not inspect.isabstract(opposite2_ConcreteEndB1)


def test_opposite2_concreteendb1_constructor_exists():
    assert callable(opposite2_ConcreteEndB1.__init__)


def test_opposite2_concreteendb1_constructor_args():
    sig = inspect.signature(opposite2_ConcreteEndB1.__init__)
    params = list(sig.parameters.keys())



def test_opposite2_abstractclassb_is_not_abstract():
    assert not inspect.isabstract(opposite2_AbstractClassB)


def test_opposite2_abstractclassb_constructor_exists():
    assert callable(opposite2_AbstractClassB.__init__)


def test_opposite2_abstractclassb_constructor_args():
    sig = inspect.signature(opposite2_AbstractClassB.__init__)
    params = list(sig.parameters.keys())



def test_opposite2_enda_is_not_abstract():
    assert not inspect.isabstract(opposite2_EndA)


def test_opposite2_enda_constructor_exists():
    assert callable(opposite2_EndA.__init__)


def test_opposite2_enda_constructor_args():
    sig = inspect.signature(opposite2_EndA.__init__)
    params = list(sig.parameters.keys())



def test_opposite2_root_is_not_abstract():
    assert not inspect.isabstract(opposite2_Root)


def test_opposite2_root_constructor_exists():
    assert callable(opposite2_Root.__init__)


def test_opposite2_root_constructor_args():
    sig = inspect.signature(opposite2_Root.__init__)
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
opposite2_ConcreteEndB2_strategy = st.builds(
    opposite2_ConcreteEndB2,
)
opposite2_ConcreteEndB1_strategy = st.builds(
    opposite2_ConcreteEndB1,
)
opposite2_AbstractClassB_strategy = st.builds(
    opposite2_AbstractClassB,
)
opposite2_EndA_strategy = st.builds(
    opposite2_EndA,
)
opposite2_Root_strategy = st.builds(
    opposite2_Root,
)

@given(instance=AbstractClassB_strategy)
@settings(max_examples=50)
def test_abstractclassb_instantiation(instance):
    assert isinstance(instance, AbstractClassB)

@given(instance=opposite2_ConcreteEndB2_strategy)
@settings(max_examples=50)
def test_opposite2_concreteendb2_instantiation(instance):
    assert isinstance(instance, opposite2_ConcreteEndB2)

@given(instance=opposite2_ConcreteEndB1_strategy)
@settings(max_examples=50)
def test_opposite2_concreteendb1_instantiation(instance):
    assert isinstance(instance, opposite2_ConcreteEndB1)

@given(instance=opposite2_AbstractClassB_strategy)
@settings(max_examples=50)
def test_opposite2_abstractclassb_instantiation(instance):
    assert isinstance(instance, opposite2_AbstractClassB)

@given(instance=opposite2_EndA_strategy)
@settings(max_examples=50)
def test_opposite2_enda_instantiation(instance):
    assert isinstance(instance, opposite2_EndA)

@given(instance=opposite2_Root_strategy)
@settings(max_examples=50)
def test_opposite2_root_instantiation(instance):
    assert isinstance(instance, opposite2_Root)
