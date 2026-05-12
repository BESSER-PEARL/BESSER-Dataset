import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass2,
    MyClass3,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
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
MyClass2_strategy = st.builds(
    MyClass2,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
MyClass_strategy = st.builds(
    MyClass,
)

@given(instance=MyClass2_strategy)
@settings(max_examples=50)
def test_myclass2_instantiation(instance):
    assert isinstance(instance, MyClass2)

@given(instance=MyClass3_strategy)
@settings(max_examples=50)
def test_myclass3_instantiation(instance):
    assert isinstance(instance, MyClass3)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)
