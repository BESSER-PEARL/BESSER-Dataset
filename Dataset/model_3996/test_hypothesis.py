import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    Class_Class,
    Class_DataType,
    NamedElt,
    Class_Classifier,
    Class_Package,
    Class_NamedElt,
    Class_Attribute,
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
    assert not inspect.isabstract(Class_Class)


def test_class_class_constructor_exists():
    assert callable(Class_Class.__init__)


def test_class_class_constructor_args():
    sig = inspect.signature(Class_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class_class_has_isAbstract():
    assert hasattr(Class_Class, "isAbstract")
    descriptor = None
    for klass in Class_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class_datatype_is_not_abstract():
    assert not inspect.isabstract(Class_DataType)


def test_class_datatype_constructor_exists():
    assert callable(Class_DataType.__init__)


def test_class_datatype_constructor_args():
    sig = inspect.signature(Class_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_class_classifier_is_not_abstract():
    assert not inspect.isabstract(Class_Classifier)


def test_class_classifier_constructor_exists():
    assert callable(Class_Classifier.__init__)


def test_class_classifier_constructor_args():
    sig = inspect.signature(Class_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class_package_is_not_abstract():
    assert not inspect.isabstract(Class_Package)


def test_class_package_constructor_exists():
    assert callable(Class_Package.__init__)


def test_class_package_constructor_args():
    sig = inspect.signature(Class_Package.__init__)
    params = list(sig.parameters.keys())



def test_class_namedelt_is_not_abstract():
    assert not inspect.isabstract(Class_NamedElt)


def test_class_namedelt_constructor_exists():
    assert callable(Class_NamedElt.__init__)


def test_class_namedelt_constructor_args():
    sig = inspect.signature(Class_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class_namedelt_has_name():
    assert hasattr(Class_NamedElt, "name")
    descriptor = None
    for klass in Class_NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class_attribute_is_not_abstract():
    assert not inspect.isabstract(Class_Attribute)


def test_class_attribute_constructor_exists():
    assert callable(Class_Attribute.__init__)


def test_class_attribute_constructor_args():
    sig = inspect.signature(Class_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class_attribute_has_multiValued():
    assert hasattr(Class_Attribute, "multiValued")
    descriptor = None
    for klass in Class_Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
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
Class_Class_strategy = st.builds(
    Class_Class,
    isAbstract=
        st.booleans()
)
Class_DataType_strategy = st.builds(
    Class_DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
Class_Classifier_strategy = st.builds(
    Class_Classifier,
)
Class_Package_strategy = st.builds(
    Class_Package,
)
Class_NamedElt_strategy = st.builds(
    Class_NamedElt,
    name=
        safe_text
)
Class_Attribute_strategy = st.builds(
    Class_Attribute,
    multiValued=
        st.booleans()
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=Class_Class_strategy)
@settings(max_examples=50)
def test_class_class_instantiation(instance):
    assert isinstance(instance, Class_Class)



@given(instance=Class_Class_strategy)
def test_class_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class_DataType_strategy)
@settings(max_examples=50)
def test_class_datatype_instantiation(instance):
    assert isinstance(instance, Class_DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=Class_Classifier_strategy)
@settings(max_examples=50)
def test_class_classifier_instantiation(instance):
    assert isinstance(instance, Class_Classifier)

@given(instance=Class_Package_strategy)
@settings(max_examples=50)
def test_class_package_instantiation(instance):
    assert isinstance(instance, Class_Package)

@given(instance=Class_NamedElt_strategy)
@settings(max_examples=50)
def test_class_namedelt_instantiation(instance):
    assert isinstance(instance, Class_NamedElt)



@given(instance=Class_NamedElt_strategy)
def test_class_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class_Attribute_strategy)
@settings(max_examples=50)
def test_class_attribute_instantiation(instance):
    assert isinstance(instance, Class_Attribute)



@given(instance=Class_Attribute_strategy)
def test_class_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original
