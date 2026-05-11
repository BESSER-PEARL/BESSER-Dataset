import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p2::C2,
    p2::C1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p2::c2_is_not_abstract():
    assert not inspect.isabstract(p2::C2)


def test_p2::c2_constructor_exists():
    assert callable(p2::C2.__init__)


def test_p2::c2_constructor_args():
    sig = inspect.signature(p2::C2.__init__)
    params = list(sig.parameters.keys())



def test_p2::c1_is_not_abstract():
    assert not inspect.isabstract(p2::C1)


def test_p2::c1_constructor_exists():
    assert callable(p2::C1.__init__)


def test_p2::c1_constructor_args():
    sig = inspect.signature(p2::C1.__init__)
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
p2::C2_strategy = st.builds(
    p2::C2,
)
p2::C1_strategy = st.builds(
    p2::C1,
)

@given(instance=p2::C2_strategy)
@settings(max_examples=50)
def test_p2::c2_instantiation(instance):
    assert isinstance(instance, p2::C2)

@given(instance=p2::C1_strategy)
@settings(max_examples=50)
def test_p2::c1_instantiation(instance):
    assert isinstance(instance, p2::C1)
