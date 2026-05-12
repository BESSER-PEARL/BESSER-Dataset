import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    class_DataType,
    class_Class,
    NamedElt,
    class_Classifier,
    class_Package,
    class_NamedElt,
    class_Attribute,
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



def test_class_datatype_is_not_abstract():
    assert not inspect.isabstract(class_DataType)


def test_class_datatype_constructor_exists():
    assert callable(class_DataType.__init__)


def test_class_datatype_constructor_args():
    sig = inspect.signature(class_DataType.__init__)
    params = list(sig.parameters.keys())



def test_class_class_is_not_abstract():
    assert not inspect.isabstract(class_Class)


def test_class_class_constructor_exists():
    assert callable(class_Class.__init__)


def test_class_class_constructor_args():
    sig = inspect.signature(class_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class_class_has_isAbstract():
    assert hasattr(class_Class, "isAbstract")
    descriptor = None
    for klass in class_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_class_classifier_is_not_abstract():
    assert not inspect.isabstract(class_Classifier)


def test_class_classifier_constructor_exists():
    assert callable(class_Classifier.__init__)


def test_class_classifier_constructor_args():
    sig = inspect.signature(class_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class_package_is_not_abstract():
    assert not inspect.isabstract(class_Package)


def test_class_package_constructor_exists():
    assert callable(class_Package.__init__)


def test_class_package_constructor_args():
    sig = inspect.signature(class_Package.__init__)
    params = list(sig.parameters.keys())



def test_class_namedelt_is_not_abstract():
    assert not inspect.isabstract(class_NamedElt)


def test_class_namedelt_constructor_exists():
    assert callable(class_NamedElt.__init__)


def test_class_namedelt_constructor_args():
    sig = inspect.signature(class_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class_namedelt_has_name():
    assert hasattr(class_NamedElt, "name")
    descriptor = None
    for klass in class_NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class_attribute_is_not_abstract():
    assert not inspect.isabstract(class_Attribute)


def test_class_attribute_constructor_exists():
    assert callable(class_Attribute.__init__)


def test_class_attribute_constructor_args():
    sig = inspect.signature(class_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class_attribute_has_multiValued():
    assert hasattr(class_Attribute, "multiValued")
    descriptor = None
    for klass in class_Attribute.__mro__:
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
class_DataType_strategy = st.builds(
    class_DataType,
)
class_Class_strategy = st.builds(
    class_Class,
    isAbstract=
        st.booleans()
)
NamedElt_strategy = st.builds(
    NamedElt,
)
class_Classifier_strategy = st.builds(
    class_Classifier,
)
class_Package_strategy = st.builds(
    class_Package,
)
class_NamedElt_strategy = st.builds(
    class_NamedElt,
    name=
        safe_text
)
class_Attribute_strategy = st.builds(
    class_Attribute,
    multiValued=
        st.booleans()
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=class_DataType_strategy)
@settings(max_examples=50)
def test_class_datatype_instantiation(instance):
    assert isinstance(instance, class_DataType)

@given(instance=class_Class_strategy)
@settings(max_examples=50)
def test_class_class_instantiation(instance):
    assert isinstance(instance, class_Class)



@given(instance=class_Class_strategy)
def test_class_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=class_Classifier_strategy)
@settings(max_examples=50)
def test_class_classifier_instantiation(instance):
    assert isinstance(instance, class_Classifier)

@given(instance=class_Package_strategy)
@settings(max_examples=50)
def test_class_package_instantiation(instance):
    assert isinstance(instance, class_Package)

@given(instance=class_NamedElt_strategy)
@settings(max_examples=50)
def test_class_namedelt_instantiation(instance):
    assert isinstance(instance, class_NamedElt)



@given(instance=class_NamedElt_strategy)
def test_class_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class_Attribute_strategy)
@settings(max_examples=50)
def test_class_attribute_instantiation(instance):
    assert isinstance(instance, class_Attribute)



@given(instance=class_Attribute_strategy)
def test_class_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original
