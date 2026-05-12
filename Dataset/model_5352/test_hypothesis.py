import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p2_C2,
    p2_C1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p2_c2_is_not_abstract():
    assert not inspect.isabstract(p2_C2)


def test_p2_c2_constructor_exists():
    assert callable(p2_C2.__init__)


def test_p2_c2_constructor_args():
    sig = inspect.signature(p2_C2.__init__)
    params = list(sig.parameters.keys())



def test_p2_c1_is_not_abstract():
    assert not inspect.isabstract(p2_C1)


def test_p2_c1_constructor_exists():
    assert callable(p2_C1.__init__)


def test_p2_c1_constructor_args():
    sig = inspect.signature(p2_C1.__init__)
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
p2_C2_strategy = st.builds(
    p2_C2,
)
p2_C1_strategy = st.builds(
    p2_C1,
)

@given(instance=p2_C2_strategy)
@settings(max_examples=50)
def test_p2_c2_instantiation(instance):
    assert isinstance(instance, p2_C2)

@given(instance=p2_C1_strategy)
@settings(max_examples=50)
def test_p2_c1_instantiation(instance):
    assert isinstance(instance, p2_C1)
