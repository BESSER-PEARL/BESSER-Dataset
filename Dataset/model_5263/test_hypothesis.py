import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lazyBuilder_B,
    lazyBuilder_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lazybuilder_b_is_not_abstract():
    assert not inspect.isabstract(lazyBuilder_B)


def test_lazybuilder_b_constructor_exists():
    assert callable(lazyBuilder_B.__init__)


def test_lazybuilder_b_constructor_args():
    sig = inspect.signature(lazyBuilder_B.__init__)
    params = list(sig.parameters.keys())



def test_lazybuilder_a_is_not_abstract():
    assert not inspect.isabstract(lazyBuilder_A)


def test_lazybuilder_a_constructor_exists():
    assert callable(lazyBuilder_A.__init__)


def test_lazybuilder_a_constructor_args():
    sig = inspect.signature(lazyBuilder_A.__init__)
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
lazyBuilder_B_strategy = st.builds(
    lazyBuilder_B,
)
lazyBuilder_A_strategy = st.builds(
    lazyBuilder_A,
)

@given(instance=lazyBuilder_B_strategy)
@settings(max_examples=50)
def test_lazybuilder_b_instantiation(instance):
    assert isinstance(instance, lazyBuilder_B)

@given(instance=lazyBuilder_A_strategy)
@settings(max_examples=50)
def test_lazybuilder_a_instantiation(instance):
    assert isinstance(instance, lazyBuilder_A)
