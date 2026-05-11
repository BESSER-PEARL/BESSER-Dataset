import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    CD::Package,
    CD::Class,
    CD::DataType,
    NamedElt,
    CD::Attribute,
    CD::Classifier,
    CD::NamedElt,
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



def test_cd::package_is_not_abstract():
    assert not inspect.isabstract(CD::Package)


def test_cd::package_constructor_exists():
    assert callable(CD::Package.__init__)


def test_cd::package_constructor_args():
    sig = inspect.signature(CD::Package.__init__)
    params = list(sig.parameters.keys())



def test_cd::class_is_not_abstract():
    assert not inspect.isabstract(CD::Class)


def test_cd::class_constructor_exists():
    assert callable(CD::Class.__init__)


def test_cd::class_constructor_args():
    sig = inspect.signature(CD::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_cd::class_has_isAbstract():
    assert hasattr(CD::Class, "isAbstract")
    descriptor = None
    for klass in CD::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_cd::datatype_is_not_abstract():
    assert not inspect.isabstract(CD::DataType)


def test_cd::datatype_constructor_exists():
    assert callable(CD::DataType.__init__)


def test_cd::datatype_constructor_args():
    sig = inspect.signature(CD::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_cd::attribute_is_not_abstract():
    assert not inspect.isabstract(CD::Attribute)


def test_cd::attribute_constructor_exists():
    assert callable(CD::Attribute.__init__)


def test_cd::attribute_constructor_args():
    sig = inspect.signature(CD::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_cd::attribute_has_multiValued():
    assert hasattr(CD::Attribute, "multiValued")
    descriptor = None
    for klass in CD::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_cd::classifier_is_not_abstract():
    assert not inspect.isabstract(CD::Classifier)


def test_cd::classifier_constructor_exists():
    assert callable(CD::Classifier.__init__)


def test_cd::classifier_constructor_args():
    sig = inspect.signature(CD::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_cd::namedelt_is_not_abstract():
    assert not inspect.isabstract(CD::NamedElt)


def test_cd::namedelt_constructor_exists():
    assert callable(CD::NamedElt.__init__)


def test_cd::namedelt_constructor_args():
    sig = inspect.signature(CD::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cd::namedelt_has_name():
    assert hasattr(CD::NamedElt, "name")
    descriptor = None
    for klass in CD::NamedElt.__mro__:
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
CD::Package_strategy = st.builds(
    CD::Package,
)
CD::Class_strategy = st.builds(
    CD::Class,
    isAbstract=
        safe_text
)
CD::DataType_strategy = st.builds(
    CD::DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
CD::Attribute_strategy = st.builds(
    CD::Attribute,
    multiValued=
        safe_text
)
CD::Classifier_strategy = st.builds(
    CD::Classifier,
)
CD::NamedElt_strategy = st.builds(
    CD::NamedElt,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CD::Package_strategy)
@settings(max_examples=50)
def test_cd::package_instantiation(instance):
    assert isinstance(instance, CD::Package)

@given(instance=CD::Class_strategy)
@settings(max_examples=50)
def test_cd::class_instantiation(instance):
    assert isinstance(instance, CD::Class)

@given(instance=CD::Class_strategy)
def test_cd::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=CD::Class_strategy)
def test_cd::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CD::DataType_strategy)
@settings(max_examples=50)
def test_cd::datatype_instantiation(instance):
    assert isinstance(instance, CD::DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=CD::Attribute_strategy)
@settings(max_examples=50)
def test_cd::attribute_instantiation(instance):
    assert isinstance(instance, CD::Attribute)

@given(instance=CD::Attribute_strategy)
def test_cd::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, str)


@given(instance=CD::Attribute_strategy)
def test_cd::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=CD::Classifier_strategy)
@settings(max_examples=50)
def test_cd::classifier_instantiation(instance):
    assert isinstance(instance, CD::Classifier)

@given(instance=CD::NamedElt_strategy)
@settings(max_examples=50)
def test_cd::namedelt_instantiation(instance):
    assert isinstance(instance, CD::NamedElt)

@given(instance=CD::NamedElt_strategy)
def test_cd::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CD::NamedElt_strategy)
def test_cd::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
