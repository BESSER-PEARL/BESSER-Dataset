import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConceptA,
    test1::ConceptB,
    test1::ConceptC,
    test1::ConceptA,
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



def test_test1::conceptb_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptB)


def test_test1::conceptb_constructor_exists():
    assert callable(test1::ConceptB.__init__)


def test_test1::conceptb_constructor_args():
    sig = inspect.signature(test1::ConceptB.__init__)
    params = list(sig.parameters.keys())



def test_test1::conceptc_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptC)


def test_test1::conceptc_constructor_exists():
    assert callable(test1::ConceptC.__init__)


def test_test1::conceptc_constructor_args():
    sig = inspect.signature(test1::ConceptC.__init__)
    params = list(sig.parameters.keys())
    assert "cool" in params, "Missing parameter 'cool'"
    assert "nbr" in params, "Missing parameter 'nbr'"

def test_test1::conceptc_has_cool():
    assert hasattr(test1::ConceptC, "cool")
    descriptor = None
    for klass in test1::ConceptC.__mro__:
        if "cool" in klass.__dict__:
            descriptor = klass.__dict__["cool"]
            break
    assert isinstance(descriptor, property)

def test_test1::conceptc_has_nbr():
    assert hasattr(test1::ConceptC, "nbr")
    descriptor = None
    for klass in test1::ConceptC.__mro__:
        if "nbr" in klass.__dict__:
            descriptor = klass.__dict__["nbr"]
            break
    assert isinstance(descriptor, property)



def test_test1::concepta_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptA)


def test_test1::concepta_constructor_exists():
    assert callable(test1::ConceptA.__init__)


def test_test1::concepta_constructor_args():
    sig = inspect.signature(test1::ConceptA.__init__)
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
test1::ConceptB_strategy = st.builds(
    test1::ConceptB,
)
test1::ConceptC_strategy = st.builds(
    test1::ConceptC,
    cool=
        st.booleans(),
    nbr=
        st.integers()
)
test1::ConceptA_strategy = st.builds(
    test1::ConceptA,
)

@given(instance=ConceptA_strategy)
@settings(max_examples=50)
def test_concepta_instantiation(instance):
    assert isinstance(instance, ConceptA)

@given(instance=test1::ConceptB_strategy)
@settings(max_examples=50)
def test_test1::conceptb_instantiation(instance):
    assert isinstance(instance, test1::ConceptB)

@given(instance=test1::ConceptC_strategy)
@settings(max_examples=50)
def test_test1::conceptc_instantiation(instance):
    assert isinstance(instance, test1::ConceptC)

@given(instance=test1::ConceptC_strategy)
def test_test1::conceptc_cool_type(instance):
    assert isinstance(instance.cool, bool)


@given(instance=test1::ConceptC_strategy)
def test_test1::conceptc_cool_setter(instance):
    original = instance.cool
    instance.cool = original
    assert instance.cool == original

@given(instance=test1::ConceptC_strategy)
def test_test1::conceptc_nbr_type(instance):
    assert isinstance(instance.nbr, int)


@given(instance=test1::ConceptC_strategy)
def test_test1::conceptc_nbr_setter(instance):
    original = instance.nbr
    instance.nbr = original
    assert instance.nbr == original

@given(instance=test1::ConceptA_strategy)
@settings(max_examples=50)
def test_test1::concepta_instantiation(instance):
    assert isinstance(instance, test1::ConceptA)
