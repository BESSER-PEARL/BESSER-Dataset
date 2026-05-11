import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p::Exception2,
    p::Exception1,
    p::Class4,
    p::Class3,
    p::Class2,
    p::Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p::exception2_is_not_abstract():
    assert not inspect.isabstract(p::Exception2)


def test_p::exception2_constructor_exists():
    assert callable(p::Exception2.__init__)


def test_p::exception2_constructor_args():
    sig = inspect.signature(p::Exception2.__init__)
    params = list(sig.parameters.keys())



def test_p::exception1_is_not_abstract():
    assert not inspect.isabstract(p::Exception1)


def test_p::exception1_constructor_exists():
    assert callable(p::Exception1.__init__)


def test_p::exception1_constructor_args():
    sig = inspect.signature(p::Exception1.__init__)
    params = list(sig.parameters.keys())



def test_p::class4_is_not_abstract():
    assert not inspect.isabstract(p::Class4)


def test_p::class4_constructor_exists():
    assert callable(p::Class4.__init__)


def test_p::class4_constructor_args():
    sig = inspect.signature(p::Class4.__init__)
    params = list(sig.parameters.keys())



def test_p::class3_is_not_abstract():
    assert not inspect.isabstract(p::Class3)


def test_p::class3_constructor_exists():
    assert callable(p::Class3.__init__)


def test_p::class3_constructor_args():
    sig = inspect.signature(p::Class3.__init__)
    params = list(sig.parameters.keys())



def test_p::class2_is_not_abstract():
    assert not inspect.isabstract(p::Class2)


def test_p::class2_constructor_exists():
    assert callable(p::Class2.__init__)


def test_p::class2_constructor_args():
    sig = inspect.signature(p::Class2.__init__)
    params = list(sig.parameters.keys())



def test_p::class1_is_not_abstract():
    assert not inspect.isabstract(p::Class1)


def test_p::class1_constructor_exists():
    assert callable(p::Class1.__init__)


def test_p::class1_constructor_args():
    sig = inspect.signature(p::Class1.__init__)
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
p::Exception2_strategy = st.builds(
    p::Exception2,
)
p::Exception1_strategy = st.builds(
    p::Exception1,
)
p::Class4_strategy = st.builds(
    p::Class4,
)
p::Class3_strategy = st.builds(
    p::Class3,
)
p::Class2_strategy = st.builds(
    p::Class2,
)
p::Class1_strategy = st.builds(
    p::Class1,
)

@given(instance=p::Exception2_strategy)
@settings(max_examples=50)
def test_p::exception2_instantiation(instance):
    assert isinstance(instance, p::Exception2)

@given(instance=p::Exception1_strategy)
@settings(max_examples=50)
def test_p::exception1_instantiation(instance):
    assert isinstance(instance, p::Exception1)

@given(instance=p::Class4_strategy)
@settings(max_examples=50)
def test_p::class4_instantiation(instance):
    assert isinstance(instance, p::Class4)

@given(instance=p::Class3_strategy)
@settings(max_examples=50)
def test_p::class3_instantiation(instance):
    assert isinstance(instance, p::Class3)

@given(instance=p::Class2_strategy)
@settings(max_examples=50)
def test_p::class2_instantiation(instance):
    assert isinstance(instance, p::Class2)

@given(instance=p::Class1_strategy)
@settings(max_examples=50)
def test_p::class1_instantiation(instance):
    assert isinstance(instance, p::Class1)
