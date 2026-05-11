import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractSuperClass,
    opposite1::ClassA,
    opposite1::ClassB,
    opposite1::AbstractSuperClass,
    opposite1::Root,
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



def test_opposite1::classa_is_not_abstract():
    assert not inspect.isabstract(opposite1::ClassA)


def test_opposite1::classa_constructor_exists():
    assert callable(opposite1::ClassA.__init__)


def test_opposite1::classa_constructor_args():
    sig = inspect.signature(opposite1::ClassA.__init__)
    params = list(sig.parameters.keys())



def test_opposite1::classb_is_not_abstract():
    assert not inspect.isabstract(opposite1::ClassB)


def test_opposite1::classb_constructor_exists():
    assert callable(opposite1::ClassB.__init__)


def test_opposite1::classb_constructor_args():
    sig = inspect.signature(opposite1::ClassB.__init__)
    params = list(sig.parameters.keys())



def test_opposite1::abstractsuperclass_is_not_abstract():
    assert not inspect.isabstract(opposite1::AbstractSuperClass)


def test_opposite1::abstractsuperclass_constructor_exists():
    assert callable(opposite1::AbstractSuperClass.__init__)


def test_opposite1::abstractsuperclass_constructor_args():
    sig = inspect.signature(opposite1::AbstractSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_opposite1::root_is_not_abstract():
    assert not inspect.isabstract(opposite1::Root)


def test_opposite1::root_constructor_exists():
    assert callable(opposite1::Root.__init__)


def test_opposite1::root_constructor_args():
    sig = inspect.signature(opposite1::Root.__init__)
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
opposite1::ClassA_strategy = st.builds(
    opposite1::ClassA,
)
opposite1::ClassB_strategy = st.builds(
    opposite1::ClassB,
)
opposite1::AbstractSuperClass_strategy = st.builds(
    opposite1::AbstractSuperClass,
)
opposite1::Root_strategy = st.builds(
    opposite1::Root,
)

@given(instance=AbstractSuperClass_strategy)
@settings(max_examples=50)
def test_abstractsuperclass_instantiation(instance):
    assert isinstance(instance, AbstractSuperClass)

@given(instance=opposite1::ClassA_strategy)
@settings(max_examples=50)
def test_opposite1::classa_instantiation(instance):
    assert isinstance(instance, opposite1::ClassA)

@given(instance=opposite1::ClassB_strategy)
@settings(max_examples=50)
def test_opposite1::classb_instantiation(instance):
    assert isinstance(instance, opposite1::ClassB)

@given(instance=opposite1::AbstractSuperClass_strategy)
@settings(max_examples=50)
def test_opposite1::abstractsuperclass_instantiation(instance):
    assert isinstance(instance, opposite1::AbstractSuperClass)

@given(instance=opposite1::Root_strategy)
@settings(max_examples=50)
def test_opposite1::root_instantiation(instance):
    assert isinstance(instance, opposite1::Root)
