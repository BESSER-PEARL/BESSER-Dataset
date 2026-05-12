import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    functioncall_ConceptA,
    functioncall_ConceptC,
    ConceptA,
    functioncall_ConceptB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_functioncall_concepta_is_not_abstract():
    assert not inspect.isabstract(functioncall_ConceptA)


def test_functioncall_concepta_constructor_exists():
    assert callable(functioncall_ConceptA.__init__)


def test_functioncall_concepta_constructor_args():
    sig = inspect.signature(functioncall_ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_functioncall_conceptc_is_not_abstract():
    assert not inspect.isabstract(functioncall_ConceptC)


def test_functioncall_conceptc_constructor_exists():
    assert callable(functioncall_ConceptC.__init__)


def test_functioncall_conceptc_constructor_args():
    sig = inspect.signature(functioncall_ConceptC.__init__)
    params = list(sig.parameters.keys())



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_functioncall_conceptb_is_not_abstract():
    assert not inspect.isabstract(functioncall_ConceptB)


def test_functioncall_conceptb_constructor_exists():
    assert callable(functioncall_ConceptB.__init__)


def test_functioncall_conceptb_constructor_args():
    sig = inspect.signature(functioncall_ConceptB.__init__)
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
functioncall_ConceptA_strategy = st.builds(
    functioncall_ConceptA,
)
functioncall_ConceptC_strategy = st.builds(
    functioncall_ConceptC,
)
ConceptA_strategy = st.builds(
    ConceptA,
)
functioncall_ConceptB_strategy = st.builds(
    functioncall_ConceptB,
)

@given(instance=functioncall_ConceptA_strategy)
@settings(max_examples=50)
def test_functioncall_concepta_instantiation(instance):
    assert isinstance(instance, functioncall_ConceptA)

@given(instance=functioncall_ConceptC_strategy)
@settings(max_examples=50)
def test_functioncall_conceptc_instantiation(instance):
    assert isinstance(instance, functioncall_ConceptC)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=functioncall_ConceptB_strategy)
@settings(max_examples=50)
def test_functioncall_conceptb_instantiation(instance):
    assert isinstance(instance, functioncall_ConceptB)
