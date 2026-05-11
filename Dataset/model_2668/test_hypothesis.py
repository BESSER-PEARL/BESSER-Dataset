import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    semlink::NamedElement,
    NamedElement,
    semlink::B,
    semlink::C,
    semlink::G,
    semlink::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_semlink::namedelement_is_not_abstract():
    assert not inspect.isabstract(semlink::NamedElement)


def test_semlink::namedelement_constructor_exists():
    assert callable(semlink::NamedElement.__init__)


def test_semlink::namedelement_constructor_args():
    sig = inspect.signature(semlink::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_semlink::namedelement_has_name():
    assert hasattr(semlink::NamedElement, "name")
    descriptor = None
    for klass in semlink::NamedElement.__mro__:
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



def test_semlink::b_is_not_abstract():
    assert not inspect.isabstract(semlink::B)


def test_semlink::b_constructor_exists():
    assert callable(semlink::B.__init__)


def test_semlink::b_constructor_args():
    sig = inspect.signature(semlink::B.__init__)
    params = list(sig.parameters.keys())



def test_semlink::c_is_not_abstract():
    assert not inspect.isabstract(semlink::C)


def test_semlink::c_constructor_exists():
    assert callable(semlink::C.__init__)


def test_semlink::c_constructor_args():
    sig = inspect.signature(semlink::C.__init__)
    params = list(sig.parameters.keys())



def test_semlink::g_is_not_abstract():
    assert not inspect.isabstract(semlink::G)


def test_semlink::g_constructor_exists():
    assert callable(semlink::G.__init__)


def test_semlink::g_constructor_args():
    sig = inspect.signature(semlink::G.__init__)
    params = list(sig.parameters.keys())



def test_semlink::a_is_not_abstract():
    assert not inspect.isabstract(semlink::A)


def test_semlink::a_constructor_exists():
    assert callable(semlink::A.__init__)


def test_semlink::a_constructor_args():
    sig = inspect.signature(semlink::A.__init__)
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
semlink::NamedElement_strategy = st.builds(
    semlink::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
semlink::B_strategy = st.builds(
    semlink::B,
)
semlink::C_strategy = st.builds(
    semlink::C,
)
semlink::G_strategy = st.builds(
    semlink::G,
)
semlink::A_strategy = st.builds(
    semlink::A,
)

@given(instance=semlink::NamedElement_strategy)
@settings(max_examples=50)
def test_semlink::namedelement_instantiation(instance):
    assert isinstance(instance, semlink::NamedElement)

@given(instance=semlink::NamedElement_strategy)
def test_semlink::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=semlink::NamedElement_strategy)
def test_semlink::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=semlink::B_strategy)
@settings(max_examples=50)
def test_semlink::b_instantiation(instance):
    assert isinstance(instance, semlink::B)

@given(instance=semlink::C_strategy)
@settings(max_examples=50)
def test_semlink::c_instantiation(instance):
    assert isinstance(instance, semlink::C)

@given(instance=semlink::G_strategy)
@settings(max_examples=50)
def test_semlink::g_instantiation(instance):
    assert isinstance(instance, semlink::G)

@given(instance=semlink::A_strategy)
@settings(max_examples=50)
def test_semlink::a_instantiation(instance):
    assert isinstance(instance, semlink::A)
