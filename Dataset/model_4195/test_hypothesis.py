import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dSL::EClass,
    dSL::Greeting,
    dSL::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::eclass_is_not_abstract():
    assert not inspect.isabstract(dSL::EClass)


def test_dsl::eclass_constructor_exists():
    assert callable(dSL::EClass.__init__)


def test_dsl::eclass_constructor_args():
    sig = inspect.signature(dSL::EClass.__init__)
    params = list(sig.parameters.keys())



def test_dsl::greeting_is_not_abstract():
    assert not inspect.isabstract(dSL::Greeting)


def test_dsl::greeting_constructor_exists():
    assert callable(dSL::Greeting.__init__)


def test_dsl::greeting_constructor_args():
    sig = inspect.signature(dSL::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_dsl::model_is_not_abstract():
    assert not inspect.isabstract(dSL::Model)


def test_dsl::model_constructor_exists():
    assert callable(dSL::Model.__init__)


def test_dsl::model_constructor_args():
    sig = inspect.signature(dSL::Model.__init__)
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
dSL::EClass_strategy = st.builds(
    dSL::EClass,
)
dSL::Greeting_strategy = st.builds(
    dSL::Greeting,
)
dSL::Model_strategy = st.builds(
    dSL::Model,
)

@given(instance=dSL::EClass_strategy)
@settings(max_examples=50)
def test_dsl::eclass_instantiation(instance):
    assert isinstance(instance, dSL::EClass)

@given(instance=dSL::Greeting_strategy)
@settings(max_examples=50)
def test_dsl::greeting_instantiation(instance):
    assert isinstance(instance, dSL::Greeting)

@given(instance=dSL::Model_strategy)
@settings(max_examples=50)
def test_dsl::model_instantiation(instance):
    assert isinstance(instance, dSL::Model)
