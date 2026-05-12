import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleUml_NamedElement,
    NamedElement,
    SimpleUml_Package,
    SimpleUml_Property,
    SimpleUml_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUml_NamedElement)


def test_simpleuml_namedelement_constructor_exists():
    assert callable(SimpleUml_NamedElement.__init__)


def test_simpleuml_namedelement_constructor_args():
    sig = inspect.signature(SimpleUml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_namedelement_has_name():
    assert hasattr(SimpleUml_NamedElement, "name")
    descriptor = None
    for klass in SimpleUml_NamedElement.__mro__:
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



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(SimpleUml_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(SimpleUml_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(SimpleUml_Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_property_is_not_abstract():
    assert not inspect.isabstract(SimpleUml_Property)


def test_simpleuml_property_constructor_exists():
    assert callable(SimpleUml_Property.__init__)


def test_simpleuml_property_constructor_args():
    sig = inspect.signature(SimpleUml_Property.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "isContainment" in params, "Missing parameter 'isContainment'"

def test_simpleuml_property_has_primitiveType():
    assert hasattr(SimpleUml_Property, "primitiveType")
    descriptor = None
    for klass in SimpleUml_Property.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml_property_has_isContainment():
    assert hasattr(SimpleUml_Property, "isContainment")
    descriptor = None
    for klass in SimpleUml_Property.__mro__:
        if "isContainment" in klass.__dict__:
            descriptor = klass.__dict__["isContainment"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(SimpleUml_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(SimpleUml_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(SimpleUml_Class.__init__)
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
SimpleUml_NamedElement_strategy = st.builds(
    SimpleUml_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SimpleUml_Package_strategy = st.builds(
    SimpleUml_Package,
)
SimpleUml_Property_strategy = st.builds(
    SimpleUml_Property,
    primitiveType=
        safe_text,
    isContainment=
        st.booleans()
)
SimpleUml_Class_strategy = st.builds(
    SimpleUml_Class,
)

@given(instance=SimpleUml_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml_namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUml_NamedElement)



@given(instance=SimpleUml_NamedElement_strategy)
def test_simpleuml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUml_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, SimpleUml_Package)

@given(instance=SimpleUml_Property_strategy)
@settings(max_examples=50)
def test_simpleuml_property_instantiation(instance):
    assert isinstance(instance, SimpleUml_Property)



@given(instance=SimpleUml_Property_strategy)
def test_simpleuml_property_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original



@given(instance=SimpleUml_Property_strategy)
def test_simpleuml_property_isContainment_setter(instance):
    original = instance.isContainment
    instance.isContainment = original
    assert instance.isContainment == original

@given(instance=SimpleUml_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, SimpleUml_Class)
