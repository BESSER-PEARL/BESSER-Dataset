import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    class::ClassModel,
    Classifier,
    class::Class,
    class::DataType,
    class::NamedElt,
    NamedElt,
    class::Attribute,
    class::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class::classmodel_is_not_abstract():
    assert not inspect.isabstract(class::ClassModel)


def test_class::classmodel_constructor_exists():
    assert callable(class::ClassModel.__init__)


def test_class::classmodel_constructor_args():
    sig = inspect.signature(class::ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_class::class_is_not_abstract():
    assert not inspect.isabstract(class::Class)


def test_class::class_constructor_exists():
    assert callable(class::Class.__init__)


def test_class::class_constructor_args():
    sig = inspect.signature(class::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_class::class_has_isAbstract():
    assert hasattr(class::Class, "isAbstract")
    descriptor = None
    for klass in class::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class::datatype_is_not_abstract():
    assert not inspect.isabstract(class::DataType)


def test_class::datatype_constructor_exists():
    assert callable(class::DataType.__init__)


def test_class::datatype_constructor_args():
    sig = inspect.signature(class::DataType.__init__)
    params = list(sig.parameters.keys())



def test_class::namedelt_is_not_abstract():
    assert not inspect.isabstract(class::NamedElt)


def test_class::namedelt_constructor_exists():
    assert callable(class::NamedElt.__init__)


def test_class::namedelt_constructor_args():
    sig = inspect.signature(class::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::namedelt_has_name():
    assert hasattr(class::NamedElt, "name")
    descriptor = None
    for klass in class::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_class::attribute_is_not_abstract():
    assert not inspect.isabstract(class::Attribute)


def test_class::attribute_constructor_exists():
    assert callable(class::Attribute.__init__)


def test_class::attribute_constructor_args():
    sig = inspect.signature(class::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_class::attribute_has_multiValued():
    assert hasattr(class::Attribute, "multiValued")
    descriptor = None
    for klass in class::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_class::classifier_is_not_abstract():
    assert not inspect.isabstract(class::Classifier)


def test_class::classifier_constructor_exists():
    assert callable(class::Classifier.__init__)


def test_class::classifier_constructor_args():
    sig = inspect.signature(class::Classifier.__init__)
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
class::ClassModel_strategy = st.builds(
    class::ClassModel,
)
Classifier_strategy = st.builds(
    Classifier,
)
class::Class_strategy = st.builds(
    class::Class,
    isAbstract=
        st.booleans()
)
class::DataType_strategy = st.builds(
    class::DataType,
)
class::NamedElt_strategy = st.builds(
    class::NamedElt,
    name=
        safe_text
)
NamedElt_strategy = st.builds(
    NamedElt,
)
class::Attribute_strategy = st.builds(
    class::Attribute,
    multiValued=
        st.booleans()
)
class::Classifier_strategy = st.builds(
    class::Classifier,
)

@given(instance=class::ClassModel_strategy)
@settings(max_examples=50)
def test_class::classmodel_instantiation(instance):
    assert isinstance(instance, class::ClassModel)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=class::Class_strategy)
@settings(max_examples=50)
def test_class::class_instantiation(instance):
    assert isinstance(instance, class::Class)

@given(instance=class::Class_strategy)
def test_class::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=class::Class_strategy)
def test_class::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=class::DataType_strategy)
@settings(max_examples=50)
def test_class::datatype_instantiation(instance):
    assert isinstance(instance, class::DataType)

@given(instance=class::NamedElt_strategy)
@settings(max_examples=50)
def test_class::namedelt_instantiation(instance):
    assert isinstance(instance, class::NamedElt)

@given(instance=class::NamedElt_strategy)
def test_class::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::NamedElt_strategy)
def test_class::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=class::Attribute_strategy)
@settings(max_examples=50)
def test_class::attribute_instantiation(instance):
    assert isinstance(instance, class::Attribute)

@given(instance=class::Attribute_strategy)
def test_class::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, bool)


@given(instance=class::Attribute_strategy)
def test_class::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=class::Classifier_strategy)
@settings(max_examples=50)
def test_class::classifier_instantiation(instance):
    assert isinstance(instance, class::Classifier)
