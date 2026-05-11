import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    input::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_input::a_is_not_abstract():
    assert not inspect.isabstract(input::A)


def test_input::a_constructor_exists():
    assert callable(input::A.__init__)


def test_input::a_constructor_args():
    sig = inspect.signature(input::A.__init__)
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
input::A_strategy = st.builds(
    input::A,
)

@given(instance=input::A_strategy)
@settings(max_examples=50)
def test_input::a_instantiation(instance):
    assert isinstance(instance, input::A)
