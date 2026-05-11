import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::B,
    example::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::b_is_not_abstract():
    assert not inspect.isabstract(example::B)


def test_example::b_constructor_exists():
    assert callable(example::B.__init__)


def test_example::b_constructor_args():
    sig = inspect.signature(example::B.__init__)
    params = list(sig.parameters.keys())



def test_example::a_is_not_abstract():
    assert not inspect.isabstract(example::A)


def test_example::a_constructor_exists():
    assert callable(example::A.__init__)


def test_example::a_constructor_args():
    sig = inspect.signature(example::A.__init__)
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
example::B_strategy = st.builds(
    example::B,
)
example::A_strategy = st.builds(
    example::A,
)

@given(instance=example::B_strategy)
@settings(max_examples=50)
def test_example::b_instantiation(instance):
    assert isinstance(instance, example::B)

@given(instance=example::A_strategy)
@settings(max_examples=50)
def test_example::a_instantiation(instance):
    assert isinstance(instance, example::A)
