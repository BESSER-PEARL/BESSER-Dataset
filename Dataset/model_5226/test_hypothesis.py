import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ic::sub2::B3,
    ic::sub2::B2,
    ic::sub2::B1,
    ic::sub1::A3,
    ic::sub1::A2,
    ic::sub1::A1,
    ic::TopLevelClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ic::sub2::b3_is_not_abstract():
    assert not inspect.isabstract(ic::sub2::B3)


def test_ic::sub2::b3_constructor_exists():
    assert callable(ic::sub2::B3.__init__)


def test_ic::sub2::b3_constructor_args():
    sig = inspect.signature(ic::sub2::B3.__init__)
    params = list(sig.parameters.keys())



def test_ic::sub2::b2_is_not_abstract():
    assert not inspect.isabstract(ic::sub2::B2)


def test_ic::sub2::b2_constructor_exists():
    assert callable(ic::sub2::B2.__init__)


def test_ic::sub2::b2_constructor_args():
    sig = inspect.signature(ic::sub2::B2.__init__)
    params = list(sig.parameters.keys())



def test_ic::sub2::b1_is_not_abstract():
    assert not inspect.isabstract(ic::sub2::B1)


def test_ic::sub2::b1_constructor_exists():
    assert callable(ic::sub2::B1.__init__)


def test_ic::sub2::b1_constructor_args():
    sig = inspect.signature(ic::sub2::B1.__init__)
    params = list(sig.parameters.keys())



def test_ic::sub1::a3_is_not_abstract():
    assert not inspect.isabstract(ic::sub1::A3)


def test_ic::sub1::a3_constructor_exists():
    assert callable(ic::sub1::A3.__init__)


def test_ic::sub1::a3_constructor_args():
    sig = inspect.signature(ic::sub1::A3.__init__)
    params = list(sig.parameters.keys())



def test_ic::sub1::a2_is_not_abstract():
    assert not inspect.isabstract(ic::sub1::A2)


def test_ic::sub1::a2_constructor_exists():
    assert callable(ic::sub1::A2.__init__)


def test_ic::sub1::a2_constructor_args():
    sig = inspect.signature(ic::sub1::A2.__init__)
    params = list(sig.parameters.keys())



def test_ic::sub1::a1_is_not_abstract():
    assert not inspect.isabstract(ic::sub1::A1)


def test_ic::sub1::a1_constructor_exists():
    assert callable(ic::sub1::A1.__init__)


def test_ic::sub1::a1_constructor_args():
    sig = inspect.signature(ic::sub1::A1.__init__)
    params = list(sig.parameters.keys())



def test_ic::toplevelclass_is_not_abstract():
    assert not inspect.isabstract(ic::TopLevelClass)


def test_ic::toplevelclass_constructor_exists():
    assert callable(ic::TopLevelClass.__init__)


def test_ic::toplevelclass_constructor_args():
    sig = inspect.signature(ic::TopLevelClass.__init__)
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
ic::sub2::B3_strategy = st.builds(
    ic::sub2::B3,
)
ic::sub2::B2_strategy = st.builds(
    ic::sub2::B2,
)
ic::sub2::B1_strategy = st.builds(
    ic::sub2::B1,
)
ic::sub1::A3_strategy = st.builds(
    ic::sub1::A3,
)
ic::sub1::A2_strategy = st.builds(
    ic::sub1::A2,
)
ic::sub1::A1_strategy = st.builds(
    ic::sub1::A1,
)
ic::TopLevelClass_strategy = st.builds(
    ic::TopLevelClass,
)

@given(instance=ic::sub2::B3_strategy)
@settings(max_examples=50)
def test_ic::sub2::b3_instantiation(instance):
    assert isinstance(instance, ic::sub2::B3)

@given(instance=ic::sub2::B2_strategy)
@settings(max_examples=50)
def test_ic::sub2::b2_instantiation(instance):
    assert isinstance(instance, ic::sub2::B2)

@given(instance=ic::sub2::B1_strategy)
@settings(max_examples=50)
def test_ic::sub2::b1_instantiation(instance):
    assert isinstance(instance, ic::sub2::B1)

@given(instance=ic::sub1::A3_strategy)
@settings(max_examples=50)
def test_ic::sub1::a3_instantiation(instance):
    assert isinstance(instance, ic::sub1::A3)

@given(instance=ic::sub1::A2_strategy)
@settings(max_examples=50)
def test_ic::sub1::a2_instantiation(instance):
    assert isinstance(instance, ic::sub1::A2)

@given(instance=ic::sub1::A1_strategy)
@settings(max_examples=50)
def test_ic::sub1::a1_instantiation(instance):
    assert isinstance(instance, ic::sub1::A1)

@given(instance=ic::TopLevelClass_strategy)
@settings(max_examples=50)
def test_ic::toplevelclass_instantiation(instance):
    assert isinstance(instance, ic::TopLevelClass)
