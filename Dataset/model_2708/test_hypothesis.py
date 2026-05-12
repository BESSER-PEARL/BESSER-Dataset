import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tbase_NamedElement,
    tbase_TRoot,
    tbase_C,
    NamedElement,
    tbase_B,
    tbase_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tbase_namedelement_is_not_abstract():
    assert not inspect.isabstract(tbase_NamedElement)


def test_tbase_namedelement_constructor_exists():
    assert callable(tbase_NamedElement.__init__)


def test_tbase_namedelement_constructor_args():
    sig = inspect.signature(tbase_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tbase_namedelement_has_name():
    assert hasattr(tbase_NamedElement, "name")
    descriptor = None
    for klass in tbase_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tbase_troot_is_not_abstract():
    assert not inspect.isabstract(tbase_TRoot)


def test_tbase_troot_constructor_exists():
    assert callable(tbase_TRoot.__init__)


def test_tbase_troot_constructor_args():
    sig = inspect.signature(tbase_TRoot.__init__)
    params = list(sig.parameters.keys())



def test_tbase_c_is_not_abstract():
    assert not inspect.isabstract(tbase_C)


def test_tbase_c_constructor_exists():
    assert callable(tbase_C.__init__)


def test_tbase_c_constructor_args():
    sig = inspect.signature(tbase_C.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tbase_b_is_not_abstract():
    assert not inspect.isabstract(tbase_B)


def test_tbase_b_constructor_exists():
    assert callable(tbase_B.__init__)


def test_tbase_b_constructor_args():
    sig = inspect.signature(tbase_B.__init__)
    params = list(sig.parameters.keys())



def test_tbase_a_is_not_abstract():
    assert not inspect.isabstract(tbase_A)


def test_tbase_a_constructor_exists():
    assert callable(tbase_A.__init__)


def test_tbase_a_constructor_args():
    sig = inspect.signature(tbase_A.__init__)
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
tbase_NamedElement_strategy = st.builds(
    tbase_NamedElement,
    name=
        safe_text
)
tbase_TRoot_strategy = st.builds(
    tbase_TRoot,
)
tbase_C_strategy = st.builds(
    tbase_C,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tbase_B_strategy = st.builds(
    tbase_B,
)
tbase_A_strategy = st.builds(
    tbase_A,
)

@given(instance=tbase_NamedElement_strategy)
@settings(max_examples=50)
def test_tbase_namedelement_instantiation(instance):
    assert isinstance(instance, tbase_NamedElement)



@given(instance=tbase_NamedElement_strategy)
def test_tbase_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tbase_TRoot_strategy)
@settings(max_examples=50)
def test_tbase_troot_instantiation(instance):
    assert isinstance(instance, tbase_TRoot)

@given(instance=tbase_C_strategy)
@settings(max_examples=50)
def test_tbase_c_instantiation(instance):
    assert isinstance(instance, tbase_C)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tbase_B_strategy)
@settings(max_examples=50)
def test_tbase_b_instantiation(instance):
    assert isinstance(instance, tbase_B)

@given(instance=tbase_A_strategy)
@settings(max_examples=50)
def test_tbase_a_instantiation(instance):
    assert isinstance(instance, tbase_A)
