import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassMM::ClassModel,
    Classifier,
    ClassMM::PrimitiveDataType,
    ClassMM::Attribute,
    ClassMM::Class,
    ClassMM::Association,
    ClassMM::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classmm::classmodel_is_not_abstract():
    assert not inspect.isabstract(ClassMM::ClassModel)


def test_classmm::classmodel_constructor_exists():
    assert callable(ClassMM::ClassModel.__init__)


def test_classmm::classmodel_constructor_args():
    sig = inspect.signature(ClassMM::ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classmm::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(ClassMM::PrimitiveDataType)


def test_classmm::primitivedatatype_constructor_exists():
    assert callable(ClassMM::PrimitiveDataType.__init__)


def test_classmm::primitivedatatype_constructor_args():
    sig = inspect.signature(ClassMM::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_classmm::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassMM::Attribute)


def test_classmm::attribute_constructor_exists():
    assert callable(ClassMM::Attribute.__init__)


def test_classmm::attribute_constructor_args():
    sig = inspect.signature(ClassMM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_classmm::attribute_has_is_primary():
    assert hasattr(ClassMM::Attribute, "is_primary")
    descriptor = None
    for klass in ClassMM::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_classmm::attribute_has_name():
    assert hasattr(ClassMM::Attribute, "name")
    descriptor = None
    for klass in ClassMM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmm::class_is_not_abstract():
    assert not inspect.isabstract(ClassMM::Class)


def test_classmm::class_constructor_exists():
    assert callable(ClassMM::Class.__init__)


def test_classmm::class_constructor_args():
    sig = inspect.signature(ClassMM::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_classmm::class_has_is_persistent():
    assert hasattr(ClassMM::Class, "is_persistent")
    descriptor = None
    for klass in ClassMM::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_classmm::association_is_not_abstract():
    assert not inspect.isabstract(ClassMM::Association)


def test_classmm::association_constructor_exists():
    assert callable(ClassMM::Association.__init__)


def test_classmm::association_constructor_args():
    sig = inspect.signature(ClassMM::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm::association_has_name():
    assert hasattr(ClassMM::Association, "name")
    descriptor = None
    for klass in ClassMM::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmm::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassMM::Classifier)


def test_classmm::classifier_constructor_exists():
    assert callable(ClassMM::Classifier.__init__)


def test_classmm::classifier_constructor_args():
    sig = inspect.signature(ClassMM::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm::classifier_has_name():
    assert hasattr(ClassMM::Classifier, "name")
    descriptor = None
    for klass in ClassMM::Classifier.__mro__:
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
ClassMM::ClassModel_strategy = st.builds(
    ClassMM::ClassModel,
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassMM::PrimitiveDataType_strategy = st.builds(
    ClassMM::PrimitiveDataType,
)
ClassMM::Attribute_strategy = st.builds(
    ClassMM::Attribute,
    is_primary=
        safe_text,
    name=
        safe_text
)
ClassMM::Class_strategy = st.builds(
    ClassMM::Class,
    is_persistent=
        safe_text
)
ClassMM::Association_strategy = st.builds(
    ClassMM::Association,
    name=
        safe_text
)
ClassMM::Classifier_strategy = st.builds(
    ClassMM::Classifier,
    name=
        safe_text
)

@given(instance=ClassMM::ClassModel_strategy)
@settings(max_examples=50)
def test_classmm::classmodel_instantiation(instance):
    assert isinstance(instance, ClassMM::ClassModel)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassMM::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_classmm::primitivedatatype_instantiation(instance):
    assert isinstance(instance, ClassMM::PrimitiveDataType)

@given(instance=ClassMM::Attribute_strategy)
@settings(max_examples=50)
def test_classmm::attribute_instantiation(instance):
    assert isinstance(instance, ClassMM::Attribute)

@given(instance=ClassMM::Attribute_strategy)
def test_classmm::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, str)


@given(instance=ClassMM::Attribute_strategy)
def test_classmm::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=ClassMM::Attribute_strategy)
def test_classmm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassMM::Attribute_strategy)
def test_classmm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassMM::Class_strategy)
@settings(max_examples=50)
def test_classmm::class_instantiation(instance):
    assert isinstance(instance, ClassMM::Class)

@given(instance=ClassMM::Class_strategy)
def test_classmm::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, str)


@given(instance=ClassMM::Class_strategy)
def test_classmm::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=ClassMM::Association_strategy)
@settings(max_examples=50)
def test_classmm::association_instantiation(instance):
    assert isinstance(instance, ClassMM::Association)

@given(instance=ClassMM::Association_strategy)
def test_classmm::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassMM::Association_strategy)
def test_classmm::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassMM::Classifier_strategy)
@settings(max_examples=50)
def test_classmm::classifier_instantiation(instance):
    assert isinstance(instance, ClassMM::Classifier)

@given(instance=ClassMM::Classifier_strategy)
def test_classmm::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassMM::Classifier_strategy)
def test_classmm::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
