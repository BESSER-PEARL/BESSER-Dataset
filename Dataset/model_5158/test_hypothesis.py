import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    depcycle::B,
    depcycle::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_depcycle::b_is_not_abstract():
    assert not inspect.isabstract(depcycle::B)


def test_depcycle::b_constructor_exists():
    assert callable(depcycle::B.__init__)


def test_depcycle::b_constructor_args():
    sig = inspect.signature(depcycle::B.__init__)
    params = list(sig.parameters.keys())



def test_depcycle::a_is_not_abstract():
    assert not inspect.isabstract(depcycle::A)


def test_depcycle::a_constructor_exists():
    assert callable(depcycle::A.__init__)


def test_depcycle::a_constructor_args():
    sig = inspect.signature(depcycle::A.__init__)
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
depcycle::B_strategy = st.builds(
    depcycle::B,
)
depcycle::A_strategy = st.builds(
    depcycle::A,
)

@given(instance=depcycle::B_strategy)
@settings(max_examples=50)
def test_depcycle::b_instantiation(instance):
    assert isinstance(instance, depcycle::B)

@given(instance=depcycle::A_strategy)
@settings(max_examples=50)
def test_depcycle::a_instantiation(instance):
    assert isinstance(instance, depcycle::A)
