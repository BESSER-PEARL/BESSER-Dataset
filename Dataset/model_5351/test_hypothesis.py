import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p::p1::myEClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p::p1::myeclass_is_not_abstract():
    assert not inspect.isabstract(p::p1::myEClass)


def test_p::p1::myeclass_constructor_exists():
    assert callable(p::p1::myEClass.__init__)


def test_p::p1::myeclass_constructor_args():
    sig = inspect.signature(p::p1::myEClass.__init__)
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
p::p1::myEClass_strategy = st.builds(
    p::p1::myEClass,
)

@given(instance=p::p1::myEClass_strategy)
@settings(max_examples=50)
def test_p::p1::myeclass_instantiation(instance):
    assert isinstance(instance, p::p1::myEClass)
