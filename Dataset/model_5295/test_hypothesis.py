import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::b_is_not_abstract():
    assert not inspect.isabstract(model::B)


def test_model::b_constructor_exists():
    assert callable(model::B.__init__)


def test_model::b_constructor_args():
    sig = inspect.signature(model::B.__init__)
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
model::B_strategy = st.builds(
    model::B,
)

@given(instance=model::B_strategy)
@settings(max_examples=50)
def test_model::b_instantiation(instance):
    assert isinstance(instance, model::B)
