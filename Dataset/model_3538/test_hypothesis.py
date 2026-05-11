import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    empty::Existing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_empty::existing_is_not_abstract():
    assert not inspect.isabstract(empty::Existing)


def test_empty::existing_constructor_exists():
    assert callable(empty::Existing.__init__)


def test_empty::existing_constructor_args():
    sig = inspect.signature(empty::Existing.__init__)
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
empty::Existing_strategy = st.builds(
    empty::Existing,
)

@given(instance=empty::Existing_strategy)
@settings(max_examples=50)
def test_empty::existing_instantiation(instance):
    assert isinstance(instance, empty::Existing)
