import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p_p1_myEClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p_p1_myeclass_is_not_abstract():
    assert not inspect.isabstract(p_p1_myEClass)


def test_p_p1_myeclass_constructor_exists():
    assert callable(p_p1_myEClass.__init__)


def test_p_p1_myeclass_constructor_args():
    sig = inspect.signature(p_p1_myEClass.__init__)
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
p_p1_myEClass_strategy = st.builds(
    p_p1_myEClass,
)

@given(instance=p_p1_myEClass_strategy)
@settings(max_examples=50)
def test_p_p1_myeclass_instantiation(instance):
    assert isinstance(instance, p_p1_myEClass)
