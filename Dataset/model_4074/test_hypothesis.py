import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleUml::NamedElement,
    NamedElement,
    SimpleUml::Property,
    SimpleUml::Package,
    SimpleUml::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUml::NamedElement)


def test_simpleuml::namedelement_constructor_exists():
    assert callable(SimpleUml::NamedElement.__init__)


def test_simpleuml::namedelement_constructor_args():
    sig = inspect.signature(SimpleUml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::namedelement_has_name():
    assert hasattr(SimpleUml::NamedElement, "name")
    descriptor = None
    for klass in SimpleUml::NamedElement.__mro__:
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



def test_simpleuml::property_is_not_abstract():
    assert not inspect.isabstract(SimpleUml::Property)


def test_simpleuml::property_constructor_exists():
    assert callable(SimpleUml::Property.__init__)


def test_simpleuml::property_constructor_args():
    sig = inspect.signature(SimpleUml::Property.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "isContainment" in params, "Missing parameter 'isContainment'"

def test_simpleuml::property_has_primitiveType():
    assert hasattr(SimpleUml::Property, "primitiveType")
    descriptor = None
    for klass in SimpleUml::Property.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::property_has_isContainment():
    assert hasattr(SimpleUml::Property, "isContainment")
    descriptor = None
    for klass in SimpleUml::Property.__mro__:
        if "isContainment" in klass.__dict__:
            descriptor = klass.__dict__["isContainment"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(SimpleUml::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(SimpleUml::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(SimpleUml::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(SimpleUml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(SimpleUml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(SimpleUml::Class.__init__)
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
SimpleUml::NamedElement_strategy = st.builds(
    SimpleUml::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SimpleUml::Property_strategy = st.builds(
    SimpleUml::Property,
    primitiveType=
        safe_text,
    isContainment=
        st.booleans()
)
SimpleUml::Package_strategy = st.builds(
    SimpleUml::Package,
)
SimpleUml::Class_strategy = st.builds(
    SimpleUml::Class,
)

@given(instance=SimpleUml::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml::namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUml::NamedElement)

@given(instance=SimpleUml::NamedElement_strategy)
def test_simpleuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleUml::NamedElement_strategy)
def test_simpleuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUml::Property_strategy)
@settings(max_examples=50)
def test_simpleuml::property_instantiation(instance):
    assert isinstance(instance, SimpleUml::Property)

@given(instance=SimpleUml::Property_strategy)
def test_simpleuml::property_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=SimpleUml::Property_strategy)
def test_simpleuml::property_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=SimpleUml::Property_strategy)
def test_simpleuml::property_isContainment_type(instance):
    assert isinstance(instance.isContainment, bool)


@given(instance=SimpleUml::Property_strategy)
def test_simpleuml::property_isContainment_setter(instance):
    original = instance.isContainment
    instance.isContainment = original
    assert instance.isContainment == original

@given(instance=SimpleUml::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, SimpleUml::Package)

@given(instance=SimpleUml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, SimpleUml::Class)
