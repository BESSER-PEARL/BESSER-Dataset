import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    astrans_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astrans_b_is_not_abstract():
    assert not inspect.isabstract(astrans_B)


def test_astrans_b_constructor_exists():
    assert callable(astrans_B.__init__)


def test_astrans_b_constructor_args():
    sig = inspect.signature(astrans_B.__init__)
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
astrans_B_strategy = st.builds(
    astrans_B,
)

@given(instance=astrans_B_strategy)
@settings(max_examples=50)
def test_astrans_b_instantiation(instance):
    assert isinstance(instance, astrans_B)
