import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    CLASS::Class,
    CLASS::DataType,
    NamedElement,
    CLASS::Attribute,
    CLASS::Classifier,
    CLASS::System,
    CLASS::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class::class_is_not_abstract():
    assert not inspect.isabstract(CLASS::Class)


def test_class::class_constructor_exists():
    assert callable(CLASS::Class.__init__)


def test_class::class_constructor_args():
    sig = inspect.signature(CLASS::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class::class_has_isAbstract():
    assert hasattr(CLASS::Class, "isAbstract")
    descriptor = None
    for klass in CLASS::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class::datatype_is_not_abstract():
    assert not inspect.isabstract(CLASS::DataType)


def test_class::datatype_constructor_exists():
    assert callable(CLASS::DataType.__init__)


def test_class::datatype_constructor_args():
    sig = inspect.signature(CLASS::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_class::attribute_is_not_abstract():
    assert not inspect.isabstract(CLASS::Attribute)


def test_class::attribute_constructor_exists():
    assert callable(CLASS::Attribute.__init__)


def test_class::attribute_constructor_args():
    sig = inspect.signature(CLASS::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class::attribute_has_multiValued():
    assert hasattr(CLASS::Attribute, "multiValued")
    descriptor = None
    for klass in CLASS::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_class::classifier_is_not_abstract():
    assert not inspect.isabstract(CLASS::Classifier)


def test_class::classifier_constructor_exists():
    assert callable(CLASS::Classifier.__init__)


def test_class::classifier_constructor_args():
    sig = inspect.signature(CLASS::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class::system_is_not_abstract():
    assert not inspect.isabstract(CLASS::System)


def test_class::system_constructor_exists():
    assert callable(CLASS::System.__init__)


def test_class::system_constructor_args():
    sig = inspect.signature(CLASS::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::system_has_name():
    assert hasattr(CLASS::System, "name")
    descriptor = None
    for klass in CLASS::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class::namedelement_is_not_abstract():
    assert not inspect.isabstract(CLASS::NamedElement)


def test_class::namedelement_constructor_exists():
    assert callable(CLASS::NamedElement.__init__)


def test_class::namedelement_constructor_args():
    sig = inspect.signature(CLASS::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::namedelement_has_name():
    assert hasattr(CLASS::NamedElement, "name")
    descriptor = None
    for klass in CLASS::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Classifier_strategy = st.builds(
    Classifier,
)
CLASS::Class_strategy = st.builds(
    CLASS::Class,
    isAbstract=
        st.booleans()
)
CLASS::DataType_strategy = st.builds(
    CLASS::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CLASS::Attribute_strategy = st.builds(
    CLASS::Attribute,
    multiValued=
        st.booleans()
)
CLASS::Classifier_strategy = st.builds(
    CLASS::Classifier,
)
CLASS::System_strategy = st.builds(
    CLASS::System,
    name=
        safe_text
)
CLASS::NamedElement_strategy = st.builds(
    CLASS::NamedElement,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CLASS::Class_strategy)
@settings(max_examples=50)
def test_class::class_instantiation(instance):
    assert isinstance(instance, CLASS::Class)

@given(instance=CLASS::Class_strategy)
def test_class::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=CLASS::Class_strategy)
def test_class::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CLASS::DataType_strategy)
@settings(max_examples=50)
def test_class::datatype_instantiation(instance):
    assert isinstance(instance, CLASS::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=CLASS::Attribute_strategy)
@settings(max_examples=50)
def test_class::attribute_instantiation(instance):
    assert isinstance(instance, CLASS::Attribute)

@given(instance=CLASS::Attribute_strategy)
def test_class::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, bool)


@given(instance=CLASS::Attribute_strategy)
def test_class::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=CLASS::Classifier_strategy)
@settings(max_examples=50)
def test_class::classifier_instantiation(instance):
    assert isinstance(instance, CLASS::Classifier)

@given(instance=CLASS::System_strategy)
@settings(max_examples=50)
def test_class::system_instantiation(instance):
    assert isinstance(instance, CLASS::System)

@given(instance=CLASS::System_strategy)
def test_class::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CLASS::System_strategy)
def test_class::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CLASS::NamedElement_strategy)
@settings(max_examples=50)
def test_class::namedelement_instantiation(instance):
    assert isinstance(instance, CLASS::NamedElement)

@given(instance=CLASS::NamedElement_strategy)
def test_class::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CLASS::NamedElement_strategy)
def test_class::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
