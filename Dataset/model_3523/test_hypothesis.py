import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test1::ConceptA,
    ConceptA,
    test1::ConceptB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test1::concepta_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptA)


def test_test1::concepta_constructor_exists():
    assert callable(test1::ConceptA.__init__)


def test_test1::concepta_constructor_args():
    sig = inspect.signature(test1::ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_test1::conceptb_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptB)


def test_test1::conceptb_constructor_exists():
    assert callable(test1::ConceptB.__init__)


def test_test1::conceptb_constructor_args():
    sig = inspect.signature(test1::ConceptB.__init__)
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
test1::ConceptA_strategy = st.builds(
    test1::ConceptA,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
test1::ConceptB_strategy = st.builds(
    test1::ConceptB,
)

@given(instance=test1::ConceptA_strategy)
@settings(max_examples=50)
def test_test1::concepta_instantiation(instance):
    assert isinstance(instance, test1::ConceptA)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=test1::ConceptB_strategy)
@settings(max_examples=50)
def test_test1::conceptb_instantiation(instance):
    assert isinstance(instance, test1::ConceptB)
