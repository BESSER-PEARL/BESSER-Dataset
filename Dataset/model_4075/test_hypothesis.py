import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    SimpleUML::Property,
    SimpleUML::Package,
    SimpleUML::NamedElement,
    SimpleUML::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::property_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Property)


def test_simpleuml::property_constructor_exists():
    assert callable(SimpleUML::Property.__init__)


def test_simpleuml::property_constructor_args():
    sig = inspect.signature(SimpleUML::Property.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "isContainment" in params, "Missing parameter 'isContainment'"

def test_simpleuml::property_has_primitiveType():
    assert hasattr(SimpleUML::Property, "primitiveType")
    descriptor = None
    for klass in SimpleUML::Property.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::property_has_isContainment():
    assert hasattr(SimpleUML::Property, "isContainment")
    descriptor = None
    for klass in SimpleUML::Property.__mro__:
        if "isContainment" in klass.__dict__:
            descriptor = klass.__dict__["isContainment"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(SimpleUML::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(SimpleUML::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::NamedElement)


def test_simpleuml::namedelement_constructor_exists():
    assert callable(SimpleUML::NamedElement.__init__)


def test_simpleuml::namedelement_constructor_args():
    sig = inspect.signature(SimpleUML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::namedelement_has_name():
    assert hasattr(SimpleUML::NamedElement, "name")
    descriptor = None
    for klass in SimpleUML::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(SimpleUML::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(SimpleUML::Class.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
SimpleUML::Property_strategy = st.builds(
    SimpleUML::Property,
    primitiveType=
        safe_text,
    isContainment=
        st.booleans()
)
SimpleUML::Package_strategy = st.builds(
    SimpleUML::Package,
)
SimpleUML::NamedElement_strategy = st.builds(
    SimpleUML::NamedElement,
    name=
        safe_text
)
SimpleUML::Class_strategy = st.builds(
    SimpleUML::Class,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUML::Property_strategy)
@settings(max_examples=50)
def test_simpleuml::property_instantiation(instance):
    assert isinstance(instance, SimpleUML::Property)

@given(instance=SimpleUML::Property_strategy)
def test_simpleuml::property_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=SimpleUML::Property_strategy)
def test_simpleuml::property_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=SimpleUML::Property_strategy)
def test_simpleuml::property_isContainment_type(instance):
    assert isinstance(instance.isContainment, bool)


@given(instance=SimpleUML::Property_strategy)
def test_simpleuml::property_isContainment_setter(instance):
    original = instance.isContainment
    instance.isContainment = original
    assert instance.isContainment == original

@given(instance=SimpleUML::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, SimpleUML::Package)

@given(instance=SimpleUML::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml::namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUML::NamedElement)

@given(instance=SimpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleUML::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, SimpleUML::Class)
