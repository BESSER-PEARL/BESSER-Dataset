import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    c_SuperStuff2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_superstuff2_is_not_abstract():
    assert not inspect.isabstract(c_SuperStuff2)


def test_c_superstuff2_constructor_exists():
    assert callable(c_SuperStuff2.__init__)


def test_c_superstuff2_constructor_args():
    sig = inspect.signature(c_SuperStuff2.__init__)
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
c_SuperStuff2_strategy = st.builds(
    c_SuperStuff2,
)

@given(instance=c_SuperStuff2_strategy)
@settings(max_examples=50)
def test_c_superstuff2_instantiation(instance):
    assert isinstance(instance, c_SuperStuff2)
