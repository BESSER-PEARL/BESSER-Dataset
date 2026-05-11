import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    genericTest::OtherType,
    genericTest::D,
    genericTest::C,
    genericTest::B,
    genericTest::SomeType,
    genericTest::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generictest::othertype_is_not_abstract():
    assert not inspect.isabstract(genericTest::OtherType)


def test_generictest::othertype_constructor_exists():
    assert callable(genericTest::OtherType.__init__)


def test_generictest::othertype_constructor_args():
    sig = inspect.signature(genericTest::OtherType.__init__)
    params = list(sig.parameters.keys())



def test_generictest::d_is_not_abstract():
    assert not inspect.isabstract(genericTest::D)


def test_generictest::d_constructor_exists():
    assert callable(genericTest::D.__init__)


def test_generictest::d_constructor_args():
    sig = inspect.signature(genericTest::D.__init__)
    params = list(sig.parameters.keys())



def test_generictest::c_is_not_abstract():
    assert not inspect.isabstract(genericTest::C)


def test_generictest::c_constructor_exists():
    assert callable(genericTest::C.__init__)


def test_generictest::c_constructor_args():
    sig = inspect.signature(genericTest::C.__init__)
    params = list(sig.parameters.keys())



def test_generictest::b_is_not_abstract():
    assert not inspect.isabstract(genericTest::B)


def test_generictest::b_constructor_exists():
    assert callable(genericTest::B.__init__)


def test_generictest::b_constructor_args():
    sig = inspect.signature(genericTest::B.__init__)
    params = list(sig.parameters.keys())



def test_generictest::sometype_is_not_abstract():
    assert not inspect.isabstract(genericTest::SomeType)


def test_generictest::sometype_constructor_exists():
    assert callable(genericTest::SomeType.__init__)


def test_generictest::sometype_constructor_args():
    sig = inspect.signature(genericTest::SomeType.__init__)
    params = list(sig.parameters.keys())



def test_generictest::a_is_not_abstract():
    assert not inspect.isabstract(genericTest::A)


def test_generictest::a_constructor_exists():
    assert callable(genericTest::A.__init__)


def test_generictest::a_constructor_args():
    sig = inspect.signature(genericTest::A.__init__)
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
genericTest::OtherType_strategy = st.builds(
    genericTest::OtherType,
)
genericTest::D_strategy = st.builds(
    genericTest::D,
)
genericTest::C_strategy = st.builds(
    genericTest::C,
)
genericTest::B_strategy = st.builds(
    genericTest::B,
)
genericTest::SomeType_strategy = st.builds(
    genericTest::SomeType,
)
genericTest::A_strategy = st.builds(
    genericTest::A,
)

@given(instance=genericTest::OtherType_strategy)
@settings(max_examples=50)
def test_generictest::othertype_instantiation(instance):
    assert isinstance(instance, genericTest::OtherType)

@given(instance=genericTest::D_strategy)
@settings(max_examples=50)
def test_generictest::d_instantiation(instance):
    assert isinstance(instance, genericTest::D)

@given(instance=genericTest::C_strategy)
@settings(max_examples=50)
def test_generictest::c_instantiation(instance):
    assert isinstance(instance, genericTest::C)

@given(instance=genericTest::B_strategy)
@settings(max_examples=50)
def test_generictest::b_instantiation(instance):
    assert isinstance(instance, genericTest::B)

@given(instance=genericTest::SomeType_strategy)
@settings(max_examples=50)
def test_generictest::sometype_instantiation(instance):
    assert isinstance(instance, genericTest::SomeType)

@given(instance=genericTest::A_strategy)
@settings(max_examples=50)
def test_generictest::a_instantiation(instance):
    assert isinstance(instance, genericTest::A)
