import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ic_sub2_B3,
    ic_sub2_B2,
    ic_sub2_B1,
    ic_sub1_A3,
    ic_sub1_A2,
    ic_sub1_A1,
    ic_TopLevelClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ic_sub2_b3_is_not_abstract():
    assert not inspect.isabstract(ic_sub2_B3)


def test_ic_sub2_b3_constructor_exists():
    assert callable(ic_sub2_B3.__init__)


def test_ic_sub2_b3_constructor_args():
    sig = inspect.signature(ic_sub2_B3.__init__)
    params = list(sig.parameters.keys())



def test_ic_sub2_b2_is_not_abstract():
    assert not inspect.isabstract(ic_sub2_B2)


def test_ic_sub2_b2_constructor_exists():
    assert callable(ic_sub2_B2.__init__)


def test_ic_sub2_b2_constructor_args():
    sig = inspect.signature(ic_sub2_B2.__init__)
    params = list(sig.parameters.keys())



def test_ic_sub2_b1_is_not_abstract():
    assert not inspect.isabstract(ic_sub2_B1)


def test_ic_sub2_b1_constructor_exists():
    assert callable(ic_sub2_B1.__init__)


def test_ic_sub2_b1_constructor_args():
    sig = inspect.signature(ic_sub2_B1.__init__)
    params = list(sig.parameters.keys())



def test_ic_sub1_a3_is_not_abstract():
    assert not inspect.isabstract(ic_sub1_A3)


def test_ic_sub1_a3_constructor_exists():
    assert callable(ic_sub1_A3.__init__)


def test_ic_sub1_a3_constructor_args():
    sig = inspect.signature(ic_sub1_A3.__init__)
    params = list(sig.parameters.keys())



def test_ic_sub1_a2_is_not_abstract():
    assert not inspect.isabstract(ic_sub1_A2)


def test_ic_sub1_a2_constructor_exists():
    assert callable(ic_sub1_A2.__init__)


def test_ic_sub1_a2_constructor_args():
    sig = inspect.signature(ic_sub1_A2.__init__)
    params = list(sig.parameters.keys())



def test_ic_sub1_a1_is_not_abstract():
    assert not inspect.isabstract(ic_sub1_A1)


def test_ic_sub1_a1_constructor_exists():
    assert callable(ic_sub1_A1.__init__)


def test_ic_sub1_a1_constructor_args():
    sig = inspect.signature(ic_sub1_A1.__init__)
    params = list(sig.parameters.keys())



def test_ic_toplevelclass_is_not_abstract():
    assert not inspect.isabstract(ic_TopLevelClass)


def test_ic_toplevelclass_constructor_exists():
    assert callable(ic_TopLevelClass.__init__)


def test_ic_toplevelclass_constructor_args():
    sig = inspect.signature(ic_TopLevelClass.__init__)
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
ic_sub2_B3_strategy = st.builds(
    ic_sub2_B3,
)
ic_sub2_B2_strategy = st.builds(
    ic_sub2_B2,
)
ic_sub2_B1_strategy = st.builds(
    ic_sub2_B1,
)
ic_sub1_A3_strategy = st.builds(
    ic_sub1_A3,
)
ic_sub1_A2_strategy = st.builds(
    ic_sub1_A2,
)
ic_sub1_A1_strategy = st.builds(
    ic_sub1_A1,
)
ic_TopLevelClass_strategy = st.builds(
    ic_TopLevelClass,
)

@given(instance=ic_sub2_B3_strategy)
@settings(max_examples=50)
def test_ic_sub2_b3_instantiation(instance):
    assert isinstance(instance, ic_sub2_B3)

@given(instance=ic_sub2_B2_strategy)
@settings(max_examples=50)
def test_ic_sub2_b2_instantiation(instance):
    assert isinstance(instance, ic_sub2_B2)

@given(instance=ic_sub2_B1_strategy)
@settings(max_examples=50)
def test_ic_sub2_b1_instantiation(instance):
    assert isinstance(instance, ic_sub2_B1)

@given(instance=ic_sub1_A3_strategy)
@settings(max_examples=50)
def test_ic_sub1_a3_instantiation(instance):
    assert isinstance(instance, ic_sub1_A3)

@given(instance=ic_sub1_A2_strategy)
@settings(max_examples=50)
def test_ic_sub1_a2_instantiation(instance):
    assert isinstance(instance, ic_sub1_A2)

@given(instance=ic_sub1_A1_strategy)
@settings(max_examples=50)
def test_ic_sub1_a1_instantiation(instance):
    assert isinstance(instance, ic_sub1_A1)

@given(instance=ic_TopLevelClass_strategy)
@settings(max_examples=50)
def test_ic_toplevelclass_instantiation(instance):
    assert isinstance(instance, ic_TopLevelClass)
