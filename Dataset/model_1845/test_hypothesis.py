import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Library_Cards,
    Library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_cards_is_not_abstract():
    assert not inspect.isabstract(Library_Cards)


def test_library_cards_constructor_exists():
    assert callable(Library_Cards.__init__)


def test_library_cards_constructor_args():
    sig = inspect.signature(Library_Cards.__init__)
    params = list(sig.parameters.keys())



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(Library_Library)


def test_library_library_constructor_exists():
    assert callable(Library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(Library_Library.__init__)
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
Library_Cards_strategy = st.builds(
    Library_Cards,
)
Library_Library_strategy = st.builds(
    Library_Library,
)

@given(instance=Library_Cards_strategy)
@settings(max_examples=50)
def test_library_cards_instantiation(instance):
    assert isinstance(instance, Library_Cards)

@given(instance=Library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, Library_Library)
