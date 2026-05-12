import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testmerge_SuperA3,
    testmerge_B3,
    SuperA3,
    testmerge_A3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmerge_supera3_is_not_abstract():
    assert not inspect.isabstract(testmerge_SuperA3)


def test_testmerge_supera3_constructor_exists():
    assert callable(testmerge_SuperA3.__init__)


def test_testmerge_supera3_constructor_args():
    sig = inspect.signature(testmerge_SuperA3.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_b3_is_not_abstract():
    assert not inspect.isabstract(testmerge_B3)


def test_testmerge_b3_constructor_exists():
    assert callable(testmerge_B3.__init__)


def test_testmerge_b3_constructor_args():
    sig = inspect.signature(testmerge_B3.__init__)
    params = list(sig.parameters.keys())



def test_supera3_is_not_abstract():
    assert not inspect.isabstract(SuperA3)


def test_supera3_constructor_exists():
    assert callable(SuperA3.__init__)


def test_supera3_constructor_args():
    sig = inspect.signature(SuperA3.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_a3_is_not_abstract():
    assert not inspect.isabstract(testmerge_A3)


def test_testmerge_a3_constructor_exists():
    assert callable(testmerge_A3.__init__)


def test_testmerge_a3_constructor_args():
    sig = inspect.signature(testmerge_A3.__init__)
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
testmerge_SuperA3_strategy = st.builds(
    testmerge_SuperA3,
)
testmerge_B3_strategy = st.builds(
    testmerge_B3,
)
SuperA3_strategy = st.builds(
    SuperA3,
)
testmerge_A3_strategy = st.builds(
    testmerge_A3,
)

@given(instance=testmerge_SuperA3_strategy)
@settings(max_examples=50)
def test_testmerge_supera3_instantiation(instance):
    assert isinstance(instance, testmerge_SuperA3)

@given(instance=testmerge_B3_strategy)
@settings(max_examples=50)
def test_testmerge_b3_instantiation(instance):
    assert isinstance(instance, testmerge_B3)

@given(instance=SuperA3_strategy)
@settings(max_examples=50)
def test_supera3_instantiation(instance):
    assert isinstance(instance, SuperA3)

@given(instance=testmerge_A3_strategy)
@settings(max_examples=50)
def test_testmerge_a3_instantiation(instance):
    assert isinstance(instance, testmerge_A3)
