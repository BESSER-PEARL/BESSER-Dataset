import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplestmm::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestmm::a_is_not_abstract():
    assert not inspect.isabstract(simplestmm::A)


def test_simplestmm::a_constructor_exists():
    assert callable(simplestmm::A.__init__)


def test_simplestmm::a_constructor_args():
    sig = inspect.signature(simplestmm::A.__init__)
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
simplestmm::A_strategy = st.builds(
    simplestmm::A,
)

@given(instance=simplestmm::A_strategy)
@settings(max_examples=50)
def test_simplestmm::a_instantiation(instance):
    assert isinstance(instance, simplestmm::A)
