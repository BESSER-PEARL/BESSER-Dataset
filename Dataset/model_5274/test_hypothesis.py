import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    input_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_input_a_is_not_abstract():
    assert not inspect.isabstract(input_A)


def test_input_a_constructor_exists():
    assert callable(input_A.__init__)


def test_input_a_constructor_args():
    sig = inspect.signature(input_A.__init__)
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
input_A_strategy = st.builds(
    input_A,
)

@given(instance=input_A_strategy)
@settings(max_examples=50)
def test_input_a_instantiation(instance):
    assert isinstance(instance, input_A)
