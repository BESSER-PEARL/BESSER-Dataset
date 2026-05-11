import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecore::EPackage,
    ecore::EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore::epackage_is_not_abstract():
    assert not inspect.isabstract(ecore::EPackage)


def test_ecore::epackage_constructor_exists():
    assert callable(ecore::EPackage.__init__)


def test_ecore::epackage_constructor_args():
    sig = inspect.signature(ecore::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ecore::eclass_is_not_abstract():
    assert not inspect.isabstract(ecore::EClass)


def test_ecore::eclass_constructor_exists():
    assert callable(ecore::EClass.__init__)


def test_ecore::eclass_constructor_args():
    sig = inspect.signature(ecore::EClass.__init__)
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
ecore::EPackage_strategy = st.builds(
    ecore::EPackage,
)
ecore::EClass_strategy = st.builds(
    ecore::EClass,
)

@given(instance=ecore::EPackage_strategy)
@settings(max_examples=50)
def test_ecore::epackage_instantiation(instance):
    assert isinstance(instance, ecore::EPackage)

@given(instance=ecore::EClass_strategy)
@settings(max_examples=50)
def test_ecore::eclass_instantiation(instance):
    assert isinstance(instance, ecore::EClass)
