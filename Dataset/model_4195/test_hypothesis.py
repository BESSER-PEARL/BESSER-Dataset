import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dSL_EClass,
    dSL_Greeting,
    dSL_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_eclass_is_not_abstract():
    assert not inspect.isabstract(dSL_EClass)


def test_dsl_eclass_constructor_exists():
    assert callable(dSL_EClass.__init__)


def test_dsl_eclass_constructor_args():
    sig = inspect.signature(dSL_EClass.__init__)
    params = list(sig.parameters.keys())



def test_dsl_greeting_is_not_abstract():
    assert not inspect.isabstract(dSL_Greeting)


def test_dsl_greeting_constructor_exists():
    assert callable(dSL_Greeting.__init__)


def test_dsl_greeting_constructor_args():
    sig = inspect.signature(dSL_Greeting.__init__)
    params = list(sig.parameters.keys())



def test_dsl_model_is_not_abstract():
    assert not inspect.isabstract(dSL_Model)


def test_dsl_model_constructor_exists():
    assert callable(dSL_Model.__init__)


def test_dsl_model_constructor_args():
    sig = inspect.signature(dSL_Model.__init__)
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
dSL_EClass_strategy = st.builds(
    dSL_EClass,
)
dSL_Greeting_strategy = st.builds(
    dSL_Greeting,
)
dSL_Model_strategy = st.builds(
    dSL_Model,
)

@given(instance=dSL_EClass_strategy)
@settings(max_examples=50)
def test_dsl_eclass_instantiation(instance):
    assert isinstance(instance, dSL_EClass)

@given(instance=dSL_Greeting_strategy)
@settings(max_examples=50)
def test_dsl_greeting_instantiation(instance):
    assert isinstance(instance, dSL_Greeting)

@given(instance=dSL_Model_strategy)
@settings(max_examples=50)
def test_dsl_model_instantiation(instance):
    assert isinstance(instance, dSL_Model)
