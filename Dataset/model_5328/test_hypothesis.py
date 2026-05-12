import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sub_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sub_b_is_not_abstract():
    assert not inspect.isabstract(sub_B)


def test_sub_b_constructor_exists():
    assert callable(sub_B.__init__)


def test_sub_b_constructor_args():
    sig = inspect.signature(sub_B.__init__)
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
sub_B_strategy = st.builds(
    sub_B,
)

@given(instance=sub_B_strategy)
@settings(max_examples=50)
def test_sub_b_instantiation(instance):
    assert isinstance(instance, sub_B)
