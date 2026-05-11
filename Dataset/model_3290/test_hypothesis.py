import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basetest::EObject,
    basetest::BaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basetest::eobject_is_not_abstract():
    assert not inspect.isabstract(basetest::EObject)


def test_basetest::eobject_constructor_exists():
    assert callable(basetest::EObject.__init__)


def test_basetest::eobject_constructor_args():
    sig = inspect.signature(basetest::EObject.__init__)
    params = list(sig.parameters.keys())



def test_basetest::basemodel_is_not_abstract():
    assert not inspect.isabstract(basetest::BaseModel)


def test_basetest::basemodel_constructor_exists():
    assert callable(basetest::BaseModel.__init__)


def test_basetest::basemodel_constructor_args():
    sig = inspect.signature(basetest::BaseModel.__init__)
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
basetest::EObject_strategy = st.builds(
    basetest::EObject,
)
basetest::BaseModel_strategy = st.builds(
    basetest::BaseModel,
)

@given(instance=basetest::EObject_strategy)
@settings(max_examples=50)
def test_basetest::eobject_instantiation(instance):
    assert isinstance(instance, basetest::EObject)

@given(instance=basetest::BaseModel_strategy)
@settings(max_examples=50)
def test_basetest::basemodel_instantiation(instance):
    assert isinstance(instance, basetest::BaseModel)
