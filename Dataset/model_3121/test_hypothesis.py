import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Package,
    Attribute,
    Classifier,
    ClassDiagram::Class,
    ClassDiagram::DataType,
    Class,
    NamedElement,
    ClassDiagram::Classifier,
    ClassDiagram::Attribute,
    ClassDiagram::System,
    ClassDiagram::Package,
    ClassDiagram::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(ClassDiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(ClassDiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classdiagram::class_has_isAbstract():
    assert hasattr(ClassDiagram::Class, "isAbstract")
    descriptor = None
    for klass in ClassDiagram::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::datatype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::DataType)


def test_classdiagram::datatype_constructor_exists():
    assert callable(ClassDiagram::DataType.__init__)


def test_classdiagram::datatype_constructor_args():
    sig = inspect.signature(ClassDiagram::DataType.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(ClassDiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(ClassDiagram::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(ClassDiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(ClassDiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_classdiagram::attribute_has_multiValued():
    assert hasattr(ClassDiagram::Attribute, "multiValued")
    descriptor = None
    for klass in ClassDiagram::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::system_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::System)


def test_classdiagram::system_constructor_exists():
    assert callable(ClassDiagram::System.__init__)


def test_classdiagram::system_constructor_args():
    sig = inspect.signature(ClassDiagram::System.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::package_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Package)


def test_classdiagram::package_constructor_exists():
    assert callable(ClassDiagram::Package.__init__)


def test_classdiagram::package_constructor_args():
    sig = inspect.signature(ClassDiagram::Package.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::NamedElement)


def test_classdiagram::namedelement_constructor_exists():
    assert callable(ClassDiagram::NamedElement.__init__)


def test_classdiagram::namedelement_constructor_args():
    sig = inspect.signature(ClassDiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::namedelement_has_name():
    assert hasattr(ClassDiagram::NamedElement, "name")
    descriptor = None
    for klass in ClassDiagram::NamedElement.__mro__:
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
Package_strategy = st.builds(
    Package,
)
Attribute_strategy = st.builds(
    Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassDiagram::Class_strategy = st.builds(
    ClassDiagram::Class,
    isAbstract=
        safe_text
)
ClassDiagram::DataType_strategy = st.builds(
    ClassDiagram::DataType,
)
Class_strategy = st.builds(
    Class,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ClassDiagram::Classifier_strategy = st.builds(
    ClassDiagram::Classifier,
)
ClassDiagram::Attribute_strategy = st.builds(
    ClassDiagram::Attribute,
    multiValued=
        safe_text
)
ClassDiagram::System_strategy = st.builds(
    ClassDiagram::System,
)
ClassDiagram::Package_strategy = st.builds(
    ClassDiagram::Package,
)
ClassDiagram::NamedElement_strategy = st.builds(
    ClassDiagram::NamedElement,
    name=
        safe_text
)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassDiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Class)

@given(instance=ClassDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=ClassDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ClassDiagram::DataType_strategy)
@settings(max_examples=50)
def test_classdiagram::datatype_instantiation(instance):
    assert isinstance(instance, ClassDiagram::DataType)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ClassDiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Classifier)

@given(instance=ClassDiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Attribute)

@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, str)


@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=ClassDiagram::System_strategy)
@settings(max_examples=50)
def test_classdiagram::system_instantiation(instance):
    assert isinstance(instance, ClassDiagram::System)

@given(instance=ClassDiagram::Package_strategy)
@settings(max_examples=50)
def test_classdiagram::package_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Package)

@given(instance=ClassDiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, ClassDiagram::NamedElement)

@given(instance=ClassDiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
