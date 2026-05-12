import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    CD_Class,
    CD_Package,
    CD_DataType,
    NamedElt,
    CD_Attribute,
    CD_Classifier,
    CD_NamedElt,
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



def test_cd_class_is_not_abstract():
    assert not inspect.isabstract(CD_Class)


def test_cd_class_constructor_exists():
    assert callable(CD_Class.__init__)


def test_cd_class_constructor_args():
    sig = inspect.signature(CD_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_cd_class_has_isAbstract():
    assert hasattr(CD_Class, "isAbstract")
    descriptor = None
    for klass in CD_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_cd_package_is_not_abstract():
    assert not inspect.isabstract(CD_Package)


def test_cd_package_constructor_exists():
    assert callable(CD_Package.__init__)


def test_cd_package_constructor_args():
    sig = inspect.signature(CD_Package.__init__)
    params = list(sig.parameters.keys())



def test_cd_datatype_is_not_abstract():
    assert not inspect.isabstract(CD_DataType)


def test_cd_datatype_constructor_exists():
    assert callable(CD_DataType.__init__)


def test_cd_datatype_constructor_args():
    sig = inspect.signature(CD_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_cd_attribute_is_not_abstract():
    assert not inspect.isabstract(CD_Attribute)


def test_cd_attribute_constructor_exists():
    assert callable(CD_Attribute.__init__)


def test_cd_attribute_constructor_args():
    sig = inspect.signature(CD_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_cd_attribute_has_multiValued():
    assert hasattr(CD_Attribute, "multiValued")
    descriptor = None
    for klass in CD_Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_cd_classifier_is_not_abstract():
    assert not inspect.isabstract(CD_Classifier)


def test_cd_classifier_constructor_exists():
    assert callable(CD_Classifier.__init__)


def test_cd_classifier_constructor_args():
    sig = inspect.signature(CD_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_cd_namedelt_is_not_abstract():
    assert not inspect.isabstract(CD_NamedElt)


def test_cd_namedelt_constructor_exists():
    assert callable(CD_NamedElt.__init__)


def test_cd_namedelt_constructor_args():
    sig = inspect.signature(CD_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cd_namedelt_has_name():
    assert hasattr(CD_NamedElt, "name")
    descriptor = None
    for klass in CD_NamedElt.__mro__:
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
CD_Class_strategy = st.builds(
    CD_Class,
    isAbstract=
        safe_text
)
CD_Package_strategy = st.builds(
    CD_Package,
)
CD_DataType_strategy = st.builds(
    CD_DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
CD_Attribute_strategy = st.builds(
    CD_Attribute,
    multiValued=
        safe_text
)
CD_Classifier_strategy = st.builds(
    CD_Classifier,
)
CD_NamedElt_strategy = st.builds(
    CD_NamedElt,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CD_Class_strategy)
@settings(max_examples=50)
def test_cd_class_instantiation(instance):
    assert isinstance(instance, CD_Class)



@given(instance=CD_Class_strategy)
def test_cd_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CD_Package_strategy)
@settings(max_examples=50)
def test_cd_package_instantiation(instance):
    assert isinstance(instance, CD_Package)

@given(instance=CD_DataType_strategy)
@settings(max_examples=50)
def test_cd_datatype_instantiation(instance):
    assert isinstance(instance, CD_DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=CD_Attribute_strategy)
@settings(max_examples=50)
def test_cd_attribute_instantiation(instance):
    assert isinstance(instance, CD_Attribute)



@given(instance=CD_Attribute_strategy)
def test_cd_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=CD_Classifier_strategy)
@settings(max_examples=50)
def test_cd_classifier_instantiation(instance):
    assert isinstance(instance, CD_Classifier)

@given(instance=CD_NamedElt_strategy)
@settings(max_examples=50)
def test_cd_namedelt_instantiation(instance):
    assert isinstance(instance, CD_NamedElt)



@given(instance=CD_NamedElt_strategy)
def test_cd_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
