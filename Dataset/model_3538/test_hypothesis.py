import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    empty_Existing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_empty_existing_is_not_abstract():
    assert not inspect.isabstract(empty_Existing)


def test_empty_existing_constructor_exists():
    assert callable(empty_Existing.__init__)


def test_empty_existing_constructor_args():
    sig = inspect.signature(empty_Existing.__init__)
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
empty_Existing_strategy = st.builds(
    empty_Existing,
)

@given(instance=empty_Existing_strategy)
@settings(max_examples=50)
def test_empty_existing_instantiation(instance):
    assert isinstance(instance, empty_Existing)
