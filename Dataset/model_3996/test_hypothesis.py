import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    Class::Class,
    Class::DataType,
    NamedElt,
    Class::Classifier,
    Class::Package,
    Class::NamedElt,
    Class::Attribute,
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
    assert not inspect.isabstract(Class::Class)


def test_class::class_constructor_exists():
    assert callable(Class::Class.__init__)


def test_class::class_constructor_args():
    sig = inspect.signature(Class::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class::class_has_isAbstract():
    assert hasattr(Class::Class, "isAbstract")
    descriptor = None
    for klass in Class::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class::datatype_is_not_abstract():
    assert not inspect.isabstract(Class::DataType)


def test_class::datatype_constructor_exists():
    assert callable(Class::DataType.__init__)


def test_class::datatype_constructor_args():
    sig = inspect.signature(Class::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_class::classifier_is_not_abstract():
    assert not inspect.isabstract(Class::Classifier)


def test_class::classifier_constructor_exists():
    assert callable(Class::Classifier.__init__)


def test_class::classifier_constructor_args():
    sig = inspect.signature(Class::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class::package_is_not_abstract():
    assert not inspect.isabstract(Class::Package)


def test_class::package_constructor_exists():
    assert callable(Class::Package.__init__)


def test_class::package_constructor_args():
    sig = inspect.signature(Class::Package.__init__)
    params = list(sig.parameters.keys())



def test_class::namedelt_is_not_abstract():
    assert not inspect.isabstract(Class::NamedElt)


def test_class::namedelt_constructor_exists():
    assert callable(Class::NamedElt.__init__)


def test_class::namedelt_constructor_args():
    sig = inspect.signature(Class::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::namedelt_has_name():
    assert hasattr(Class::NamedElt, "name")
    descriptor = None
    for klass in Class::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class::attribute_is_not_abstract():
    assert not inspect.isabstract(Class::Attribute)


def test_class::attribute_constructor_exists():
    assert callable(Class::Attribute.__init__)


def test_class::attribute_constructor_args():
    sig = inspect.signature(Class::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class::attribute_has_multiValued():
    assert hasattr(Class::Attribute, "multiValued")
    descriptor = None
    for klass in Class::Attribute.__mro__:
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
Class::Class_strategy = st.builds(
    Class::Class,
    isAbstract=
        st.booleans()
)
Class::DataType_strategy = st.builds(
    Class::DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
Class::Classifier_strategy = st.builds(
    Class::Classifier,
)
Class::Package_strategy = st.builds(
    Class::Package,
)
Class::NamedElt_strategy = st.builds(
    Class::NamedElt,
    name=
        safe_text
)
Class::Attribute_strategy = st.builds(
    Class::Attribute,
    multiValued=
        st.booleans()
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=Class::Class_strategy)
@settings(max_examples=50)
def test_class::class_instantiation(instance):
    assert isinstance(instance, Class::Class)

@given(instance=Class::Class_strategy)
def test_class::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=Class::Class_strategy)
def test_class::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class::DataType_strategy)
@settings(max_examples=50)
def test_class::datatype_instantiation(instance):
    assert isinstance(instance, Class::DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=Class::Classifier_strategy)
@settings(max_examples=50)
def test_class::classifier_instantiation(instance):
    assert isinstance(instance, Class::Classifier)

@given(instance=Class::Package_strategy)
@settings(max_examples=50)
def test_class::package_instantiation(instance):
    assert isinstance(instance, Class::Package)

@given(instance=Class::NamedElt_strategy)
@settings(max_examples=50)
def test_class::namedelt_instantiation(instance):
    assert isinstance(instance, Class::NamedElt)

@given(instance=Class::NamedElt_strategy)
def test_class::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Class::NamedElt_strategy)
def test_class::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class::Attribute_strategy)
@settings(max_examples=50)
def test_class::attribute_instantiation(instance):
    assert isinstance(instance, Class::Attribute)

@given(instance=Class::Attribute_strategy)
def test_class::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, bool)


@given(instance=Class::Attribute_strategy)
def test_class::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original
