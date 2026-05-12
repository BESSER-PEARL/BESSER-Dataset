import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    SimpleUML_Property,
    SimpleUML_Package,
    SimpleUML_NamedElement,
    SimpleUML_Class,
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



def test_simpleuml_property_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Property)


def test_simpleuml_property_constructor_exists():
    assert callable(SimpleUML_Property.__init__)


def test_simpleuml_property_constructor_args():
    sig = inspect.signature(SimpleUML_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isContainment" in params, "Missing parameter 'isContainment'"
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_simpleuml_property_has_isContainment():
    assert hasattr(SimpleUML_Property, "isContainment")
    descriptor = None
    for klass in SimpleUML_Property.__mro__:
        if "isContainment" in klass.__dict__:
            descriptor = klass.__dict__["isContainment"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml_property_has_primitiveType():
    assert hasattr(SimpleUML_Property, "primitiveType")
    descriptor = None
    for klass in SimpleUML_Property.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(SimpleUML_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(SimpleUML_Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_NamedElement)


def test_simpleuml_namedelement_constructor_exists():
    assert callable(SimpleUML_NamedElement.__init__)


def test_simpleuml_namedelement_constructor_args():
    sig = inspect.signature(SimpleUML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_namedelement_has_name():
    assert hasattr(SimpleUML_NamedElement, "name")
    descriptor = None
    for klass in SimpleUML_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(SimpleUML_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(SimpleUML_Class.__init__)
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
SimpleUML_Property_strategy = st.builds(
    SimpleUML_Property,
    isContainment=
        st.booleans(),
    primitiveType=
        safe_text
)
SimpleUML_Package_strategy = st.builds(
    SimpleUML_Package,
)
SimpleUML_NamedElement_strategy = st.builds(
    SimpleUML_NamedElement,
    name=
        safe_text
)
SimpleUML_Class_strategy = st.builds(
    SimpleUML_Class,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUML_Property_strategy)
@settings(max_examples=50)
def test_simpleuml_property_instantiation(instance):
    assert isinstance(instance, SimpleUML_Property)



@given(instance=SimpleUML_Property_strategy)
def test_simpleuml_property_isContainment_setter(instance):
    original = instance.isContainment
    instance.isContainment = original
    assert instance.isContainment == original



@given(instance=SimpleUML_Property_strategy)
def test_simpleuml_property_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=SimpleUML_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, SimpleUML_Package)

@given(instance=SimpleUML_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml_namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUML_NamedElement)



@given(instance=SimpleUML_NamedElement_strategy)
def test_simpleuml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleUML_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, SimpleUML_Class)
