import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    functioncall::ConceptA,
    functioncall::ConceptC,
    ConceptA,
    functioncall::ConceptB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_functioncall::concepta_is_not_abstract():
    assert not inspect.isabstract(functioncall::ConceptA)


def test_functioncall::concepta_constructor_exists():
    assert callable(functioncall::ConceptA.__init__)


def test_functioncall::concepta_constructor_args():
    sig = inspect.signature(functioncall::ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_functioncall::conceptc_is_not_abstract():
    assert not inspect.isabstract(functioncall::ConceptC)


def test_functioncall::conceptc_constructor_exists():
    assert callable(functioncall::ConceptC.__init__)


def test_functioncall::conceptc_constructor_args():
    sig = inspect.signature(functioncall::ConceptC.__init__)
    params = list(sig.parameters.keys())



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_functioncall::conceptb_is_not_abstract():
    assert not inspect.isabstract(functioncall::ConceptB)


def test_functioncall::conceptb_constructor_exists():
    assert callable(functioncall::ConceptB.__init__)


def test_functioncall::conceptb_constructor_args():
    sig = inspect.signature(functioncall::ConceptB.__init__)
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
functioncall::ConceptA_strategy = st.builds(
    functioncall::ConceptA,
)
functioncall::ConceptC_strategy = st.builds(
    functioncall::ConceptC,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
functioncall::ConceptB_strategy = st.builds(
    functioncall::ConceptB,
)

@given(instance=functioncall::ConceptA_strategy)
@settings(max_examples=50)
def test_functioncall::concepta_instantiation(instance):
    assert isinstance(instance, functioncall::ConceptA)

@given(instance=functioncall::ConceptC_strategy)
@settings(max_examples=50)
def test_functioncall::conceptc_instantiation(instance):
    assert isinstance(instance, functioncall::ConceptC)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=functioncall::ConceptB_strategy)
@settings(max_examples=50)
def test_functioncall::conceptb_instantiation(instance):
    assert isinstance(instance, functioncall::ConceptB)
