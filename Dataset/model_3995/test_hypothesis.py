import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    CLASS_Class,
    CLASS_DataType,
    NamedElement,
    CLASS_Attribute,
    CLASS_Classifier,
    CLASS_System,
    CLASS_NamedElement,
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



def test_class_class_is_not_abstract():
    assert not inspect.isabstract(CLASS_Class)


def test_class_class_constructor_exists():
    assert callable(CLASS_Class.__init__)


def test_class_class_constructor_args():
    sig = inspect.signature(CLASS_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class_class_has_isAbstract():
    assert hasattr(CLASS_Class, "isAbstract")
    descriptor = None
    for klass in CLASS_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class_datatype_is_not_abstract():
    assert not inspect.isabstract(CLASS_DataType)


def test_class_datatype_constructor_exists():
    assert callable(CLASS_DataType.__init__)


def test_class_datatype_constructor_args():
    sig = inspect.signature(CLASS_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_class_attribute_is_not_abstract():
    assert not inspect.isabstract(CLASS_Attribute)


def test_class_attribute_constructor_exists():
    assert callable(CLASS_Attribute.__init__)


def test_class_attribute_constructor_args():
    sig = inspect.signature(CLASS_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class_attribute_has_multiValued():
    assert hasattr(CLASS_Attribute, "multiValued")
    descriptor = None
    for klass in CLASS_Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_class_classifier_is_not_abstract():
    assert not inspect.isabstract(CLASS_Classifier)


def test_class_classifier_constructor_exists():
    assert callable(CLASS_Classifier.__init__)


def test_class_classifier_constructor_args():
    sig = inspect.signature(CLASS_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class_system_is_not_abstract():
    assert not inspect.isabstract(CLASS_System)


def test_class_system_constructor_exists():
    assert callable(CLASS_System.__init__)


def test_class_system_constructor_args():
    sig = inspect.signature(CLASS_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class_system_has_name():
    assert hasattr(CLASS_System, "name")
    descriptor = None
    for klass in CLASS_System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class_namedelement_is_not_abstract():
    assert not inspect.isabstract(CLASS_NamedElement)


def test_class_namedelement_constructor_exists():
    assert callable(CLASS_NamedElement.__init__)


def test_class_namedelement_constructor_args():
    sig = inspect.signature(CLASS_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class_namedelement_has_name():
    assert hasattr(CLASS_NamedElement, "name")
    descriptor = None
    for klass in CLASS_NamedElement.__mro__:
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
CLASS_Class_strategy = st.builds(
    CLASS_Class,
    isAbstract=
        st.booleans()
)
CLASS_DataType_strategy = st.builds(
    CLASS_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CLASS_Attribute_strategy = st.builds(
    CLASS_Attribute,
    multiValued=
        st.booleans()
)
CLASS_Classifier_strategy = st.builds(
    CLASS_Classifier,
)
CLASS_System_strategy = st.builds(
    CLASS_System,
    name=
        safe_text
)
CLASS_NamedElement_strategy = st.builds(
    CLASS_NamedElement,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CLASS_Class_strategy)
@settings(max_examples=50)
def test_class_class_instantiation(instance):
    assert isinstance(instance, CLASS_Class)



@given(instance=CLASS_Class_strategy)
def test_class_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CLASS_DataType_strategy)
@settings(max_examples=50)
def test_class_datatype_instantiation(instance):
    assert isinstance(instance, CLASS_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=CLASS_Attribute_strategy)
@settings(max_examples=50)
def test_class_attribute_instantiation(instance):
    assert isinstance(instance, CLASS_Attribute)



@given(instance=CLASS_Attribute_strategy)
def test_class_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=CLASS_Classifier_strategy)
@settings(max_examples=50)
def test_class_classifier_instantiation(instance):
    assert isinstance(instance, CLASS_Classifier)

@given(instance=CLASS_System_strategy)
@settings(max_examples=50)
def test_class_system_instantiation(instance):
    assert isinstance(instance, CLASS_System)



@given(instance=CLASS_System_strategy)
def test_class_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CLASS_NamedElement_strategy)
@settings(max_examples=50)
def test_class_namedelement_instantiation(instance):
    assert isinstance(instance, CLASS_NamedElement)



@given(instance=CLASS_NamedElement_strategy)
def test_class_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
