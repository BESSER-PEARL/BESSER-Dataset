import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p1_1_EClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p1_1_eclass1_is_not_abstract():
    assert not inspect.isabstract(p1_1_EClass1)


def test_p1_1_eclass1_constructor_exists():
    assert callable(p1_1_EClass1.__init__)


def test_p1_1_eclass1_constructor_args():
    sig = inspect.signature(p1_1_EClass1.__init__)
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
p1_1_EClass1_strategy = st.builds(
    p1_1_EClass1,
)

@given(instance=p1_1_EClass1_strategy)
@settings(max_examples=50)
def test_p1_1_eclass1_instantiation(instance):
    assert isinstance(instance, p1_1_EClass1)
