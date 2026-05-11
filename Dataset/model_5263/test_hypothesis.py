import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lazyBuilder::B,
    lazyBuilder::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lazybuilder::b_is_not_abstract():
    assert not inspect.isabstract(lazyBuilder::B)


def test_lazybuilder::b_constructor_exists():
    assert callable(lazyBuilder::B.__init__)


def test_lazybuilder::b_constructor_args():
    sig = inspect.signature(lazyBuilder::B.__init__)
    params = list(sig.parameters.keys())



def test_lazybuilder::a_is_not_abstract():
    assert not inspect.isabstract(lazyBuilder::A)


def test_lazybuilder::a_constructor_exists():
    assert callable(lazyBuilder::A.__init__)


def test_lazybuilder::a_constructor_args():
    sig = inspect.signature(lazyBuilder::A.__init__)
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
lazyBuilder::B_strategy = st.builds(
    lazyBuilder::B,
)
lazyBuilder::A_strategy = st.builds(
    lazyBuilder::A,
)

@given(instance=lazyBuilder::B_strategy)
@settings(max_examples=50)
def test_lazybuilder::b_instantiation(instance):
    assert isinstance(instance, lazyBuilder::B)

@given(instance=lazyBuilder::A_strategy)
@settings(max_examples=50)
def test_lazybuilder::a_instantiation(instance):
    assert isinstance(instance, lazyBuilder::A)
