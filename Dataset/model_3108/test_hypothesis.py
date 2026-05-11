import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uml::NamedElement,
    NamedElement,
    uml::Class,
    uml::UMLSpecification,
    uml::Attribute,
    uml::Association,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml::NamedElement)


def test_uml::namedelement_constructor_exists():
    assert callable(uml::NamedElement.__init__)


def test_uml::namedelement_constructor_args():
    sig = inspect.signature(uml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::namedelement_has_name():
    assert hasattr(uml::NamedElement, "name")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
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



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::Class)


def test_uml::class_constructor_exists():
    assert callable(uml::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(uml::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml::umlspecification_is_not_abstract():
    assert not inspect.isabstract(uml::UMLSpecification)


def test_uml::umlspecification_constructor_exists():
    assert callable(uml::UMLSpecification.__init__)


def test_uml::umlspecification_constructor_args():
    sig = inspect.signature(uml::UMLSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::attribute_is_not_abstract():
    assert not inspect.isabstract(uml::Attribute)


def test_uml::attribute_constructor_exists():
    assert callable(uml::Attribute.__init__)


def test_uml::attribute_constructor_args():
    sig = inspect.signature(uml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_uml::association_is_not_abstract():
    assert not inspect.isabstract(uml::Association)


def test_uml::association_constructor_exists():
    assert callable(uml::Association.__init__)


def test_uml::association_constructor_args():
    sig = inspect.signature(uml::Association.__init__)
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
uml::NamedElement_strategy = st.builds(
    uml::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml::Class_strategy = st.builds(
    uml::Class,
)
uml::UMLSpecification_strategy = st.builds(
    uml::UMLSpecification,
)
uml::Attribute_strategy = st.builds(
    uml::Attribute,
)
uml::Association_strategy = st.builds(
    uml::Association,
)

@given(instance=uml::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::namedelement_instantiation(instance):
    assert isinstance(instance, uml::NamedElement)

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, uml::Class)

@given(instance=uml::UMLSpecification_strategy)
@settings(max_examples=50)
def test_uml::umlspecification_instantiation(instance):
    assert isinstance(instance, uml::UMLSpecification)

@given(instance=uml::Attribute_strategy)
@settings(max_examples=50)
def test_uml::attribute_instantiation(instance):
    assert isinstance(instance, uml::Attribute)

@given(instance=uml::Association_strategy)
@settings(max_examples=50)
def test_uml::association_instantiation(instance):
    assert isinstance(instance, uml::Association)
