import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tbase::NamedElement,
    tbase::TRoot,
    tbase::C,
    NamedElement,
    tbase::B,
    tbase::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tbase::namedelement_is_not_abstract():
    assert not inspect.isabstract(tbase::NamedElement)


def test_tbase::namedelement_constructor_exists():
    assert callable(tbase::NamedElement.__init__)


def test_tbase::namedelement_constructor_args():
    sig = inspect.signature(tbase::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tbase::namedelement_has_name():
    assert hasattr(tbase::NamedElement, "name")
    descriptor = None
    for klass in tbase::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tbase::troot_is_not_abstract():
    assert not inspect.isabstract(tbase::TRoot)


def test_tbase::troot_constructor_exists():
    assert callable(tbase::TRoot.__init__)


def test_tbase::troot_constructor_args():
    sig = inspect.signature(tbase::TRoot.__init__)
    params = list(sig.parameters.keys())



def test_tbase::c_is_not_abstract():
    assert not inspect.isabstract(tbase::C)


def test_tbase::c_constructor_exists():
    assert callable(tbase::C.__init__)


def test_tbase::c_constructor_args():
    sig = inspect.signature(tbase::C.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tbase::b_is_not_abstract():
    assert not inspect.isabstract(tbase::B)


def test_tbase::b_constructor_exists():
    assert callable(tbase::B.__init__)


def test_tbase::b_constructor_args():
    sig = inspect.signature(tbase::B.__init__)
    params = list(sig.parameters.keys())



def test_tbase::a_is_not_abstract():
    assert not inspect.isabstract(tbase::A)


def test_tbase::a_constructor_exists():
    assert callable(tbase::A.__init__)


def test_tbase::a_constructor_args():
    sig = inspect.signature(tbase::A.__init__)
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
tbase::NamedElement_strategy = st.builds(
    tbase::NamedElement,
    name=
        safe_text
)
tbase::TRoot_strategy = st.builds(
    tbase::TRoot,
)
tbase::C_strategy = st.builds(
    tbase::C,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tbase::B_strategy = st.builds(
    tbase::B,
)
tbase::A_strategy = st.builds(
    tbase::A,
)

@given(instance=tbase::NamedElement_strategy)
@settings(max_examples=50)
def test_tbase::namedelement_instantiation(instance):
    assert isinstance(instance, tbase::NamedElement)

@given(instance=tbase::NamedElement_strategy)
def test_tbase::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tbase::NamedElement_strategy)
def test_tbase::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tbase::TRoot_strategy)
@settings(max_examples=50)
def test_tbase::troot_instantiation(instance):
    assert isinstance(instance, tbase::TRoot)

@given(instance=tbase::C_strategy)
@settings(max_examples=50)
def test_tbase::c_instantiation(instance):
    assert isinstance(instance, tbase::C)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tbase::B_strategy)
@settings(max_examples=50)
def test_tbase::b_instantiation(instance):
    assert isinstance(instance, tbase::B)

@given(instance=tbase::A_strategy)
@settings(max_examples=50)
def test_tbase::a_instantiation(instance):
    assert isinstance(instance, tbase::A)
