import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    abc::NamedElement,
    NamedElement,
    abc::C,
    abc::B,
    abc::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc::namedelement_is_not_abstract():
    assert not inspect.isabstract(abc::NamedElement)


def test_abc::namedelement_constructor_exists():
    assert callable(abc::NamedElement.__init__)


def test_abc::namedelement_constructor_args():
    sig = inspect.signature(abc::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abc::namedelement_has_name():
    assert hasattr(abc::NamedElement, "name")
    descriptor = None
    for klass in abc::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_abc::c_is_not_abstract():
    assert not inspect.isabstract(abc::C)


def test_abc::c_constructor_exists():
    assert callable(abc::C.__init__)


def test_abc::c_constructor_args():
    sig = inspect.signature(abc::C.__init__)
    params = list(sig.parameters.keys())



def test_abc::b_is_not_abstract():
    assert not inspect.isabstract(abc::B)


def test_abc::b_constructor_exists():
    assert callable(abc::B.__init__)


def test_abc::b_constructor_args():
    sig = inspect.signature(abc::B.__init__)
    params = list(sig.parameters.keys())



def test_abc::a_is_not_abstract():
    assert not inspect.isabstract(abc::A)


def test_abc::a_constructor_exists():
    assert callable(abc::A.__init__)


def test_abc::a_constructor_args():
    sig = inspect.signature(abc::A.__init__)
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
abc::NamedElement_strategy = st.builds(
    abc::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
abc::C_strategy = st.builds(
    abc::C,
)
abc::B_strategy = st.builds(
    abc::B,
)
abc::A_strategy = st.builds(
    abc::A,
)

@given(instance=abc::NamedElement_strategy)
@settings(max_examples=50)
def test_abc::namedelement_instantiation(instance):
    assert isinstance(instance, abc::NamedElement)

@given(instance=abc::NamedElement_strategy)
def test_abc::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abc::NamedElement_strategy)
def test_abc::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=abc::C_strategy)
@settings(max_examples=50)
def test_abc::c_instantiation(instance):
    assert isinstance(instance, abc::C)

@given(instance=abc::B_strategy)
@settings(max_examples=50)
def test_abc::b_instantiation(instance):
    assert isinstance(instance, abc::B)

@given(instance=abc::A_strategy)
@settings(max_examples=50)
def test_abc::a_instantiation(instance):
    assert isinstance(instance, abc::A)
