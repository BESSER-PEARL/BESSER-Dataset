import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    abc::A,
    abc::C,
    abc::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc::a_is_not_abstract():
    assert not inspect.isabstract(abc::A)


def test_abc::a_constructor_exists():
    assert callable(abc::A.__init__)


def test_abc::a_constructor_args():
    sig = inspect.signature(abc::A.__init__)
    params = list(sig.parameters.keys())



def test_abc::c_is_not_abstract():
    assert not inspect.isabstract(abc::C)


def test_abc::c_constructor_exists():
    assert callable(abc::C.__init__)


def test_abc::c_constructor_args():
    sig = inspect.signature(abc::C.__init__)
    params = list(sig.parameters.keys())



def test_abc::b_is_not_abstract():
    assert not inspect.isabstract(abc::B)


def test_abc::b_constructor_exists():
    assert callable(abc::B.__init__)


def test_abc::b_constructor_args():
    sig = inspect.signature(abc::B.__init__)
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
abc::A_strategy = st.builds(
    abc::A,
)
abc::C_strategy = st.builds(
    abc::C,
)
abc::B_strategy = st.builds(
    abc::B,
)

@given(instance=abc::A_strategy)
@settings(max_examples=50)
def test_abc::a_instantiation(instance):
    assert isinstance(instance, abc::A)

@given(instance=abc::C_strategy)
@settings(max_examples=50)
def test_abc::c_instantiation(instance):
    assert isinstance(instance, abc::C)

@given(instance=abc::B_strategy)
@settings(max_examples=50)
def test_abc::b_instantiation(instance):
    assert isinstance(instance, abc::B)
