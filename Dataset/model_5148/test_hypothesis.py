import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    TestMerge::C,
    TestMerge::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::c_is_not_abstract():
    assert not inspect.isabstract(TestMerge::C)


def test_testmerge::c_constructor_exists():
    assert callable(TestMerge::C.__init__)


def test_testmerge::c_constructor_args():
    sig = inspect.signature(TestMerge::C.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::a_is_not_abstract():
    assert not inspect.isabstract(TestMerge::A)


def test_testmerge::a_constructor_exists():
    assert callable(TestMerge::A.__init__)


def test_testmerge::a_constructor_args():
    sig = inspect.signature(TestMerge::A.__init__)
    params = list(sig.parameters.keys())
    assert "someNewAttribute" in params, "Missing parameter 'someNewAttribute'"

def test_testmerge::a_has_someNewAttribute():
    assert hasattr(TestMerge::A, "someNewAttribute")
    descriptor = None
    for klass in TestMerge::A.__mro__:
        if "someNewAttribute" in klass.__dict__:
            descriptor = klass.__dict__["someNewAttribute"]
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
A_strategy = st.builds(
    A,
)
TestMerge::C_strategy = st.builds(
    TestMerge::C,
)
TestMerge::A_strategy = st.builds(
    TestMerge::A,
    someNewAttribute=
        safe_text
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=TestMerge::C_strategy)
@settings(max_examples=50)
def test_testmerge::c_instantiation(instance):
    assert isinstance(instance, TestMerge::C)

@given(instance=TestMerge::A_strategy)
@settings(max_examples=50)
def test_testmerge::a_instantiation(instance):
    assert isinstance(instance, TestMerge::A)

@given(instance=TestMerge::A_strategy)
def test_testmerge::a_someNewAttribute_type(instance):
    assert isinstance(instance.someNewAttribute, str)


@given(instance=TestMerge::A_strategy)
def test_testmerge::a_someNewAttribute_setter(instance):
    original = instance.someNewAttribute
    instance.someNewAttribute = original
    assert instance.someNewAttribute == original
