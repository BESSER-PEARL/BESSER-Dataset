import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConceptA,
    test1_ConceptB,
    test1_ConceptC,
    test1_ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_concepta_is_not_abstract():
    assert not inspect.isabstract(ConceptA)


def test_concepta_constructor_exists():
    assert callable(ConceptA.__init__)


def test_concepta_constructor_args():
    sig = inspect.signature(ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_test1_conceptb_is_not_abstract():
    assert not inspect.isabstract(test1_ConceptB)


def test_test1_conceptb_constructor_exists():
    assert callable(test1_ConceptB.__init__)


def test_test1_conceptb_constructor_args():
    sig = inspect.signature(test1_ConceptB.__init__)
    params = list(sig.parameters.keys())



def test_test1_conceptc_is_not_abstract():
    assert not inspect.isabstract(test1_ConceptC)


def test_test1_conceptc_constructor_exists():
    assert callable(test1_ConceptC.__init__)


def test_test1_conceptc_constructor_args():
    sig = inspect.signature(test1_ConceptC.__init__)
    params = list(sig.parameters.keys())
    assert "cool" in params, "Missing parameter 'cool'"
    assert "nbr" in params, "Missing parameter 'nbr'"

def test_test1_conceptc_has_cool():
    assert hasattr(test1_ConceptC, "cool")
    descriptor = None
    for klass in test1_ConceptC.__mro__:
        if "cool" in klass.__dict__:
            descriptor = klass.__dict__["cool"]
            break
    assert isinstance(descriptor, property)

def test_test1_conceptc_has_nbr():
    assert hasattr(test1_ConceptC, "nbr")
    descriptor = None
    for klass in test1_ConceptC.__mro__:
        if "nbr" in klass.__dict__:
            descriptor = klass.__dict__["nbr"]
            break
    assert isinstance(descriptor, property)



def test_test1_concepta_is_not_abstract():
    assert not inspect.isabstract(test1_ConceptA)


def test_test1_concepta_constructor_exists():
    assert callable(test1_ConceptA.__init__)


def test_test1_concepta_constructor_args():
    sig = inspect.signature(test1_ConceptA.__init__)
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
ConceptA_strategy = st.builds(
    ConceptA,
)
test1_ConceptB_strategy = st.builds(
    test1_ConceptB,
)
test1_ConceptC_strategy = st.builds(
    test1_ConceptC,
    cool=
        st.booleans(),
    nbr=
        st.integers()
)
test1_ConceptA_strategy = st.builds(
    test1_ConceptA,
)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=test1_ConceptB_strategy)
@settings(max_examples=50)
def test_test1_conceptb_instantiation(instance):
    assert isinstance(instance, test1_ConceptB)

@given(instance=test1_ConceptC_strategy)
@settings(max_examples=50)
def test_test1_conceptc_instantiation(instance):
    assert isinstance(instance, test1_ConceptC)



@given(instance=test1_ConceptC_strategy)
def test_test1_conceptc_cool_setter(instance):
    original = instance.cool
    instance.cool = original
    assert instance.cool == original



@given(instance=test1_ConceptC_strategy)
def test_test1_conceptc_nbr_setter(instance):
    original = instance.nbr
    instance.nbr = original
    assert instance.nbr == original

@given(instance=test1_ConceptA_strategy)
@settings(max_examples=50)
def test_test1_concepta_instantiation(instance):
    assert isinstance(instance, test1_ConceptA)
