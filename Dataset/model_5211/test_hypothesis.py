import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bug1312::C,
    bug1312::B,
    bug1312::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bug1312::c_is_not_abstract():
    assert not inspect.isabstract(bug1312::C)


def test_bug1312::c_constructor_exists():
    assert callable(bug1312::C.__init__)


def test_bug1312::c_constructor_args():
    sig = inspect.signature(bug1312::C.__init__)
    params = list(sig.parameters.keys())



def test_bug1312::b_is_not_abstract():
    assert not inspect.isabstract(bug1312::B)


def test_bug1312::b_constructor_exists():
    assert callable(bug1312::B.__init__)


def test_bug1312::b_constructor_args():
    sig = inspect.signature(bug1312::B.__init__)
    params = list(sig.parameters.keys())



def test_bug1312::root_is_not_abstract():
    assert not inspect.isabstract(bug1312::Root)


def test_bug1312::root_constructor_exists():
    assert callable(bug1312::Root.__init__)


def test_bug1312::root_constructor_args():
    sig = inspect.signature(bug1312::Root.__init__)
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
bug1312::C_strategy = st.builds(
    bug1312::C,
)
bug1312::B_strategy = st.builds(
    bug1312::B,
)
bug1312::Root_strategy = st.builds(
    bug1312::Root,
)

@given(instance=bug1312::C_strategy)
@settings(max_examples=50)
def test_bug1312::c_instantiation(instance):
    assert isinstance(instance, bug1312::C)

@given(instance=bug1312::B_strategy)
@settings(max_examples=50)
def test_bug1312::b_instantiation(instance):
    assert isinstance(instance, bug1312::B)

@given(instance=bug1312::Root_strategy)
@settings(max_examples=50)
def test_bug1312::root_instantiation(instance):
    assert isinstance(instance, bug1312::Root)
