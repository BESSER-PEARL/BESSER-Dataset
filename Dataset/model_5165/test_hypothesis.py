import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractSuperClass,
    opposite1_ClassA,
    opposite1_ClassB,
    opposite1_AbstractSuperClass,
    opposite1_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractsuperclass_is_not_abstract():
    assert not inspect.isabstract(AbstractSuperClass)


def test_abstractsuperclass_constructor_exists():
    assert callable(AbstractSuperClass.__init__)


def test_abstractsuperclass_constructor_args():
    sig = inspect.signature(AbstractSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_opposite1_classa_is_not_abstract():
    assert not inspect.isabstract(opposite1_ClassA)


def test_opposite1_classa_constructor_exists():
    assert callable(opposite1_ClassA.__init__)


def test_opposite1_classa_constructor_args():
    sig = inspect.signature(opposite1_ClassA.__init__)
    params = list(sig.parameters.keys())



def test_opposite1_classb_is_not_abstract():
    assert not inspect.isabstract(opposite1_ClassB)


def test_opposite1_classb_constructor_exists():
    assert callable(opposite1_ClassB.__init__)


def test_opposite1_classb_constructor_args():
    sig = inspect.signature(opposite1_ClassB.__init__)
    params = list(sig.parameters.keys())



def test_opposite1_abstractsuperclass_is_not_abstract():
    assert not inspect.isabstract(opposite1_AbstractSuperClass)


def test_opposite1_abstractsuperclass_constructor_exists():
    assert callable(opposite1_AbstractSuperClass.__init__)


def test_opposite1_abstractsuperclass_constructor_args():
    sig = inspect.signature(opposite1_AbstractSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_opposite1_root_is_not_abstract():
    assert not inspect.isabstract(opposite1_Root)


def test_opposite1_root_constructor_exists():
    assert callable(opposite1_Root.__init__)


def test_opposite1_root_constructor_args():
    sig = inspect.signature(opposite1_Root.__init__)
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
AbstractSuperClass_strategy = st.builds(
    AbstractSuperClass,
)
opposite1_ClassA_strategy = st.builds(
    opposite1_ClassA,
)
opposite1_ClassB_strategy = st.builds(
    opposite1_ClassB,
)
opposite1_AbstractSuperClass_strategy = st.builds(
    opposite1_AbstractSuperClass,
)
opposite1_Root_strategy = st.builds(
    opposite1_Root,
)

@given(instance=AbstractSuperClass_strategy)
@settings(max_examples=50)
def test_abstractsuperclass_instantiation(instance):
    assert isinstance(instance, AbstractSuperClass)

@given(instance=opposite1_ClassA_strategy)
@settings(max_examples=50)
def test_opposite1_classa_instantiation(instance):
    assert isinstance(instance, opposite1_ClassA)

@given(instance=opposite1_ClassB_strategy)
@settings(max_examples=50)
def test_opposite1_classb_instantiation(instance):
    assert isinstance(instance, opposite1_ClassB)

@given(instance=opposite1_AbstractSuperClass_strategy)
@settings(max_examples=50)
def test_opposite1_abstractsuperclass_instantiation(instance):
    assert isinstance(instance, opposite1_AbstractSuperClass)

@given(instance=opposite1_Root_strategy)
@settings(max_examples=50)
def test_opposite1_root_instantiation(instance):
    assert isinstance(instance, opposite1_Root)
