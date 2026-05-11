import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TestMerge::B,
    TestMerge::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmerge::b_is_not_abstract():
    assert not inspect.isabstract(TestMerge::B)


def test_testmerge::b_constructor_exists():
    assert callable(TestMerge::B.__init__)


def test_testmerge::b_constructor_args():
    sig = inspect.signature(TestMerge::B.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::a_is_not_abstract():
    assert not inspect.isabstract(TestMerge::A)


def test_testmerge::a_constructor_exists():
    assert callable(TestMerge::A.__init__)


def test_testmerge::a_constructor_args():
    sig = inspect.signature(TestMerge::A.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"

def test_testmerge::a_has_attr1():
    assert hasattr(TestMerge::A, "attr1")
    descriptor = None
    for klass in TestMerge::A.__mro__:
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
TestMerge::B_strategy = st.builds(
    TestMerge::B,
)
TestMerge::A_strategy = st.builds(
    TestMerge::A,
    attr1=
        safe_text
)

@given(instance=TestMerge::B_strategy)
@settings(max_examples=50)
def test_testmerge::b_instantiation(instance):
    assert isinstance(instance, TestMerge::B)

@given(instance=TestMerge::A_strategy)
@settings(max_examples=50)
def test_testmerge::a_instantiation(instance):
    assert isinstance(instance, TestMerge::A)

@given(instance=TestMerge::A_strategy)
def test_testmerge::a_attr1_type(instance):
    assert isinstance(instance.attr1, str)


@given(instance=TestMerge::A_strategy)
def test_testmerge::a_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original
