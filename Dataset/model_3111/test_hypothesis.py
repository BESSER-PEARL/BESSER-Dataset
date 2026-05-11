import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassM::Classifier,
    ClassM::Attribute,
    Classifier,
    ClassM::Class,
    ClassM::Model,
    ClassM::PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classm::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassM::Classifier)


def test_classm::classifier_constructor_exists():
    assert callable(ClassM::Classifier.__init__)


def test_classm::classifier_constructor_args():
    sig = inspect.signature(ClassM::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm::classifier_has_name():
    assert hasattr(ClassM::Classifier, "name")
    descriptor = None
    for klass in ClassM::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classm::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassM::Attribute)


def test_classm::attribute_constructor_exists():
    assert callable(ClassM::Attribute.__init__)


def test_classm::attribute_constructor_args():
    sig = inspect.signature(ClassM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_classm::attribute_has_is_primary():
    assert hasattr(ClassM::Attribute, "is_primary")
    descriptor = None
    for klass in ClassM::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_classm::attribute_has_name():
    assert hasattr(ClassM::Attribute, "name")
    descriptor = None
    for klass in ClassM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classm::class_is_not_abstract():
    assert not inspect.isabstract(ClassM::Class)


def test_classm::class_constructor_exists():
    assert callable(ClassM::Class.__init__)


def test_classm::class_constructor_args():
    sig = inspect.signature(ClassM::Class.__init__)
    params = list(sig.parameters.keys())



def test_classm::model_is_not_abstract():
    assert not inspect.isabstract(ClassM::Model)


def test_classm::model_constructor_exists():
    assert callable(ClassM::Model.__init__)


def test_classm::model_constructor_args():
    sig = inspect.signature(ClassM::Model.__init__)
    params = list(sig.parameters.keys())



def test_classm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassM::PrimitiveType)


def test_classm::primitivetype_constructor_exists():
    assert callable(ClassM::PrimitiveType.__init__)


def test_classm::primitivetype_constructor_args():
    sig = inspect.signature(ClassM::PrimitiveType.__init__)
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
ClassM::Classifier_strategy = st.builds(
    ClassM::Classifier,
    name=
        safe_text
)
ClassM::Attribute_strategy = st.builds(
    ClassM::Attribute,
    is_primary=
        st.booleans(),
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassM::Class_strategy = st.builds(
    ClassM::Class,
)
ClassM::Model_strategy = st.builds(
    ClassM::Model,
)
ClassM::PrimitiveType_strategy = st.builds(
    ClassM::PrimitiveType,
)

@given(instance=ClassM::Classifier_strategy)
@settings(max_examples=50)
def test_classm::classifier_instantiation(instance):
    assert isinstance(instance, ClassM::Classifier)

@given(instance=ClassM::Classifier_strategy)
def test_classm::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassM::Classifier_strategy)
def test_classm::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassM::Attribute_strategy)
@settings(max_examples=50)
def test_classm::attribute_instantiation(instance):
    assert isinstance(instance, ClassM::Attribute)

@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassM::Class_strategy)
@settings(max_examples=50)
def test_classm::class_instantiation(instance):
    assert isinstance(instance, ClassM::Class)

@given(instance=ClassM::Model_strategy)
@settings(max_examples=50)
def test_classm::model_instantiation(instance):
    assert isinstance(instance, ClassM::Model)

@given(instance=ClassM::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classm::primitivetype_instantiation(instance):
    assert isinstance(instance, ClassM::PrimitiveType)
