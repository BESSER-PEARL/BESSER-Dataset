import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestMerge_B,
    TestMerge_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmerge_b_is_not_abstract():
    assert not inspect.isabstract(TestMerge_B)


def test_testmerge_b_constructor_exists():
    assert callable(TestMerge_B.__init__)


def test_testmerge_b_constructor_args():
    sig = inspect.signature(TestMerge_B.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_a_is_not_abstract():
    assert not inspect.isabstract(TestMerge_A)


def test_testmerge_a_constructor_exists():
    assert callable(TestMerge_A.__init__)


def test_testmerge_a_constructor_args():
    sig = inspect.signature(TestMerge_A.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"

def test_testmerge_a_has_attr1():
    assert hasattr(TestMerge_A, "attr1")
    descriptor = None
    for klass in TestMerge_A.__mro__:
        if "attr1" in klass.__dict__:
            descriptor = klass.__dict__["attr1"]
            break
    assert isinstance(descriptor, property)


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
TestMerge_B_strategy = st.builds(
    TestMerge_B,
)
TestMerge_A_strategy = st.builds(
    TestMerge_A,
    attr1=
        safe_text
)

@given(instance=TestMerge_B_strategy)
@settings(max_examples=50)
def test_testmerge_b_instantiation(instance):
    assert isinstance(instance, TestMerge_B)

@given(instance=TestMerge_A_strategy)
@settings(max_examples=50)
def test_testmerge_a_instantiation(instance):
    assert isinstance(instance, TestMerge_A)



@given(instance=TestMerge_A_strategy)
def test_testmerge_a_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original
