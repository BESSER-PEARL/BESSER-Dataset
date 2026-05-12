import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplestmm_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestmm_a_is_not_abstract():
    assert not inspect.isabstract(simplestmm_A)


def test_simplestmm_a_constructor_exists():
    assert callable(simplestmm_A.__init__)


def test_simplestmm_a_constructor_args():
    sig = inspect.signature(simplestmm_A.__init__)
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
simplestmm_A_strategy = st.builds(
    simplestmm_A,
)

@given(instance=simplestmm_A_strategy)
@settings(max_examples=50)
def test_simplestmm_a_instantiation(instance):
    assert isinstance(instance, simplestmm_A)
