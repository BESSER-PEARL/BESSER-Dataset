import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Library::Cards,
    Library::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::cards_is_not_abstract():
    assert not inspect.isabstract(Library::Cards)


def test_library::cards_constructor_exists():
    assert callable(Library::Cards.__init__)


def test_library::cards_constructor_args():
    sig = inspect.signature(Library::Cards.__init__)
    params = list(sig.parameters.keys())



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(Library::Library)


def test_library::library_constructor_exists():
    assert callable(Library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(Library::Library.__init__)
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
Library::Cards_strategy = st.builds(
    Library::Cards,
)
Library::Library_strategy = st.builds(
    Library::Library,
)

@given(instance=Library::Cards_strategy)
@settings(max_examples=50)
def test_library::cards_instantiation(instance):
    assert isinstance(instance, Library::Cards)

@given(instance=Library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, Library::Library)
