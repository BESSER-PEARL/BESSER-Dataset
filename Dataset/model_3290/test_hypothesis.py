import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basetest_EObject,
    basetest_BaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basetest_eobject_is_not_abstract():
    assert not inspect.isabstract(basetest_EObject)


def test_basetest_eobject_constructor_exists():
    assert callable(basetest_EObject.__init__)


def test_basetest_eobject_constructor_args():
    sig = inspect.signature(basetest_EObject.__init__)
    params = list(sig.parameters.keys())



def test_basetest_basemodel_is_not_abstract():
    assert not inspect.isabstract(basetest_BaseModel)


def test_basetest_basemodel_constructor_exists():
    assert callable(basetest_BaseModel.__init__)


def test_basetest_basemodel_constructor_args():
    sig = inspect.signature(basetest_BaseModel.__init__)
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
basetest_EObject_strategy = st.builds(
    basetest_EObject,
)
basetest_BaseModel_strategy = st.builds(
    basetest_BaseModel,
)

@given(instance=basetest_EObject_strategy)
@settings(max_examples=50)
def test_basetest_eobject_instantiation(instance):
    assert isinstance(instance, basetest_EObject)

@given(instance=basetest_BaseModel_strategy)
@settings(max_examples=50)
def test_basetest_basemodel_instantiation(instance):
    assert isinstance(instance, basetest_BaseModel)
