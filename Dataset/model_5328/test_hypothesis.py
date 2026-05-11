import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sub::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sub::b_is_not_abstract():
    assert not inspect.isabstract(sub::B)


def test_sub::b_constructor_exists():
    assert callable(sub::B.__init__)


def test_sub::b_constructor_args():
    sig = inspect.signature(sub::B.__init__)
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
sub::B_strategy = st.builds(
    sub::B,
)

@given(instance=sub::B_strategy)
@settings(max_examples=50)
def test_sub::b_instantiation(instance):
    assert isinstance(instance, sub::B)
