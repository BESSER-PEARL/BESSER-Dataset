import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Package,
    Attribute,
    Classifier,
    ClassDiagram_Class,
    ClassDiagram_DataType,
    Class,
    NamedElement,
    ClassDiagram_Attribute,
    ClassDiagram_System,
    ClassDiagram_Classifier,
    ClassDiagram_Package,
    ClassDiagram_NamedElement,
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



def test_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Class)


def test_classdiagram_class_constructor_exists():
    assert callable(ClassDiagram_Class.__init__)


def test_classdiagram_class_constructor_args():
    sig = inspect.signature(ClassDiagram_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classdiagram_class_has_isAbstract():
    assert hasattr(ClassDiagram_Class, "isAbstract")
    descriptor = None
    for klass in ClassDiagram_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_datatype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_DataType)


def test_classdiagram_datatype_constructor_exists():
    assert callable(ClassDiagram_DataType.__init__)


def test_classdiagram_datatype_constructor_args():
    sig = inspect.signature(ClassDiagram_DataType.__init__)
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



def test_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Attribute)


def test_classdiagram_attribute_constructor_exists():
    assert callable(ClassDiagram_Attribute.__init__)


def test_classdiagram_attribute_constructor_args():
    sig = inspect.signature(ClassDiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_classdiagram_attribute_has_multiValued():
    assert hasattr(ClassDiagram_Attribute, "multiValued")
    descriptor = None
    for klass in ClassDiagram_Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_system_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_System)


def test_classdiagram_system_constructor_exists():
    assert callable(ClassDiagram_System.__init__)


def test_classdiagram_system_constructor_args():
    sig = inspect.signature(ClassDiagram_System.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Classifier)


def test_classdiagram_classifier_constructor_exists():
    assert callable(ClassDiagram_Classifier.__init__)


def test_classdiagram_classifier_constructor_args():
    sig = inspect.signature(ClassDiagram_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_package_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Package)


def test_classdiagram_package_constructor_exists():
    assert callable(ClassDiagram_Package.__init__)


def test_classdiagram_package_constructor_args():
    sig = inspect.signature(ClassDiagram_Package.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_namedelement_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_NamedElement)


def test_classdiagram_namedelement_constructor_exists():
    assert callable(ClassDiagram_NamedElement.__init__)


def test_classdiagram_namedelement_constructor_args():
    sig = inspect.signature(ClassDiagram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_namedelement_has_name():
    assert hasattr(ClassDiagram_NamedElement, "name")
    descriptor = None
    for klass in ClassDiagram_NamedElement.__mro__:
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
ClassDiagram_Class_strategy = st.builds(
    ClassDiagram_Class,
    isAbstract=
        safe_text
)
ClassDiagram_DataType_strategy = st.builds(
    ClassDiagram_DataType,
)
Class_strategy = st.builds(
    Class,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ClassDiagram_Attribute_strategy = st.builds(
    ClassDiagram_Attribute,
    multiValued=
        safe_text
)
ClassDiagram_System_strategy = st.builds(
    ClassDiagram_System,
)
ClassDiagram_Classifier_strategy = st.builds(
    ClassDiagram_Classifier,
)
ClassDiagram_Package_strategy = st.builds(
    ClassDiagram_Package,
)
ClassDiagram_NamedElement_strategy = st.builds(
    ClassDiagram_NamedElement,
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

@given(instance=ClassDiagram_Class_strategy)
@settings(max_examples=50)
def test_classdiagram_class_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Class)



@given(instance=ClassDiagram_Class_strategy)
def test_classdiagram_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ClassDiagram_DataType_strategy)
@settings(max_examples=50)
def test_classdiagram_datatype_instantiation(instance):
    assert isinstance(instance, ClassDiagram_DataType)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ClassDiagram_Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram_attribute_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Attribute)



@given(instance=ClassDiagram_Attribute_strategy)
def test_classdiagram_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=ClassDiagram_System_strategy)
@settings(max_examples=50)
def test_classdiagram_system_instantiation(instance):
    assert isinstance(instance, ClassDiagram_System)

@given(instance=ClassDiagram_Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram_classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Classifier)

@given(instance=ClassDiagram_Package_strategy)
@settings(max_examples=50)
def test_classdiagram_package_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Package)

@given(instance=ClassDiagram_NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram_namedelement_instantiation(instance):
    assert isinstance(instance, ClassDiagram_NamedElement)



@given(instance=ClassDiagram_NamedElement_strategy)
def test_classdiagram_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
