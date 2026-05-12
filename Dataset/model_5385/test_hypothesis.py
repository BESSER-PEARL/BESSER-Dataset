import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p_Exception2,
    p_Exception1,
    p_Class4,
    p_Class3,
    p_Class2,
    p_Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p_exception2_is_not_abstract():
    assert not inspect.isabstract(p_Exception2)


def test_p_exception2_constructor_exists():
    assert callable(p_Exception2.__init__)


def test_p_exception2_constructor_args():
    sig = inspect.signature(p_Exception2.__init__)
    params = list(sig.parameters.keys())



def test_p_exception1_is_not_abstract():
    assert not inspect.isabstract(p_Exception1)


def test_p_exception1_constructor_exists():
    assert callable(p_Exception1.__init__)


def test_p_exception1_constructor_args():
    sig = inspect.signature(p_Exception1.__init__)
    params = list(sig.parameters.keys())



def test_p_class4_is_not_abstract():
    assert not inspect.isabstract(p_Class4)


def test_p_class4_constructor_exists():
    assert callable(p_Class4.__init__)


def test_p_class4_constructor_args():
    sig = inspect.signature(p_Class4.__init__)
    params = list(sig.parameters.keys())



def test_p_class3_is_not_abstract():
    assert not inspect.isabstract(p_Class3)


def test_p_class3_constructor_exists():
    assert callable(p_Class3.__init__)


def test_p_class3_constructor_args():
    sig = inspect.signature(p_Class3.__init__)
    params = list(sig.parameters.keys())



def test_p_class2_is_not_abstract():
    assert not inspect.isabstract(p_Class2)


def test_p_class2_constructor_exists():
    assert callable(p_Class2.__init__)


def test_p_class2_constructor_args():
    sig = inspect.signature(p_Class2.__init__)
    params = list(sig.parameters.keys())



def test_p_class1_is_not_abstract():
    assert not inspect.isabstract(p_Class1)


def test_p_class1_constructor_exists():
    assert callable(p_Class1.__init__)


def test_p_class1_constructor_args():
    sig = inspect.signature(p_Class1.__init__)
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
p_Exception2_strategy = st.builds(
    p_Exception2,
)
p_Exception1_strategy = st.builds(
    p_Exception1,
)
p_Class4_strategy = st.builds(
    p_Class4,
)
p_Class3_strategy = st.builds(
    p_Class3,
)
p_Class2_strategy = st.builds(
    p_Class2,
)
p_Class1_strategy = st.builds(
    p_Class1,
)

@given(instance=p_Exception2_strategy)
@settings(max_examples=50)
def test_p_exception2_instantiation(instance):
    assert isinstance(instance, p_Exception2)

@given(instance=p_Exception1_strategy)
@settings(max_examples=50)
def test_p_exception1_instantiation(instance):
    assert isinstance(instance, p_Exception1)

@given(instance=p_Class4_strategy)
@settings(max_examples=50)
def test_p_class4_instantiation(instance):
    assert isinstance(instance, p_Class4)

@given(instance=p_Class3_strategy)
@settings(max_examples=50)
def test_p_class3_instantiation(instance):
    assert isinstance(instance, p_Class3)

@given(instance=p_Class2_strategy)
@settings(max_examples=50)
def test_p_class2_instantiation(instance):
    assert isinstance(instance, p_Class2)

@given(instance=p_Class1_strategy)
@settings(max_examples=50)
def test_p_class1_instantiation(instance):
    assert isinstance(instance, p_Class1)
