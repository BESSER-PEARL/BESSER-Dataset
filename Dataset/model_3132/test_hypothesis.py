import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassM::Model,
    StructuralFeature,
    ClassM::Attribute,
    ClassM::Operation,
    TypedElement,
    ClassM::Parameter,
    ClassM::TypedElement,
    ClassM::Classifier,
    ClassM::StructuralFeature,
    Classifier,
    ClassM::PrimitiveType,
    ClassM::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classm::model_is_not_abstract():
    assert not inspect.isabstract(ClassM::Model)


def test_classm::model_constructor_exists():
    assert callable(ClassM::Model.__init__)


def test_classm::model_constructor_args():
    sig = inspect.signature(ClassM::Model.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classm::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassM::Attribute)


def test_classm::attribute_constructor_exists():
    assert callable(ClassM::Attribute.__init__)


def test_classm::attribute_constructor_args():
    sig = inspect.signature(ClassM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_classm::attribute_has_multivalued():
    assert hasattr(ClassM::Attribute, "multivalued")
    descriptor = None
    for klass in ClassM::Attribute.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_classm::operation_is_not_abstract():
    assert not inspect.isabstract(ClassM::Operation)


def test_classm::operation_constructor_exists():
    assert callable(ClassM::Operation.__init__)


def test_classm::operation_constructor_args():
    sig = inspect.signature(ClassM::Operation.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classm::parameter_is_not_abstract():
    assert not inspect.isabstract(ClassM::Parameter)


def test_classm::parameter_constructor_exists():
    assert callable(ClassM::Parameter.__init__)


def test_classm::parameter_constructor_args():
    sig = inspect.signature(ClassM::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm::parameter_has_name():
    assert hasattr(ClassM::Parameter, "name")
    descriptor = None
    for klass in ClassM::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classm::typedelement_is_not_abstract():
    assert not inspect.isabstract(ClassM::TypedElement)


def test_classm::typedelement_constructor_exists():
    assert callable(ClassM::TypedElement.__init__)


def test_classm::typedelement_constructor_args():
    sig = inspect.signature(ClassM::TypedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_classm::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassM::StructuralFeature)


def test_classm::structuralfeature_constructor_exists():
    assert callable(ClassM::StructuralFeature.__init__)


def test_classm::structuralfeature_constructor_args():
    sig = inspect.signature(ClassM::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_classm::structuralfeature_has_visibility():
    assert hasattr(ClassM::StructuralFeature, "visibility")
    descriptor = None
    for klass in ClassM::StructuralFeature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classm::structuralfeature_has_name():
    assert hasattr(ClassM::StructuralFeature, "name")
    descriptor = None
    for klass in ClassM::StructuralFeature.__mro__:
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



def test_classm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassM::PrimitiveType)


def test_classm::primitivetype_constructor_exists():
    assert callable(ClassM::PrimitiveType.__init__)


def test_classm::primitivetype_constructor_args():
    sig = inspect.signature(ClassM::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classm::class_is_not_abstract():
    assert not inspect.isabstract(ClassM::Class)


def test_classm::class_constructor_exists():
    assert callable(ClassM::Class.__init__)


def test_classm::class_constructor_args():
    sig = inspect.signature(ClassM::Class.__init__)
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
ClassM::Model_strategy = st.builds(
    ClassM::Model,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ClassM::Attribute_strategy = st.builds(
    ClassM::Attribute,
    multivalued=
        st.booleans()
)
ClassM::Operation_strategy = st.builds(
    ClassM::Operation,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ClassM::Parameter_strategy = st.builds(
    ClassM::Parameter,
    name=
        safe_text
)
ClassM::TypedElement_strategy = st.builds(
    ClassM::TypedElement,
)
ClassM::Classifier_strategy = st.builds(
    ClassM::Classifier,
    name=
        safe_text
)
ClassM::StructuralFeature_strategy = st.builds(
    ClassM::StructuralFeature,
    visibility=
        safe_text,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassM::PrimitiveType_strategy = st.builds(
    ClassM::PrimitiveType,
)
ClassM::Class_strategy = st.builds(
    ClassM::Class,
)

@given(instance=ClassM::Model_strategy)
@settings(max_examples=50)
def test_classm::model_instantiation(instance):
    assert isinstance(instance, ClassM::Model)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ClassM::Attribute_strategy)
@settings(max_examples=50)
def test_classm::attribute_instantiation(instance):
    assert isinstance(instance, ClassM::Attribute)

@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=ClassM::Attribute_strategy)
def test_classm::attribute_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=ClassM::Operation_strategy)
@settings(max_examples=50)
def test_classm::operation_instantiation(instance):
    assert isinstance(instance, ClassM::Operation)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ClassM::Parameter_strategy)
@settings(max_examples=50)
def test_classm::parameter_instantiation(instance):
    assert isinstance(instance, ClassM::Parameter)

@given(instance=ClassM::Parameter_strategy)
def test_classm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassM::Parameter_strategy)
def test_classm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassM::TypedElement_strategy)
@settings(max_examples=50)
def test_classm::typedelement_instantiation(instance):
    assert isinstance(instance, ClassM::TypedElement)

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

@given(instance=ClassM::StructuralFeature_strategy)
@settings(max_examples=50)
def test_classm::structuralfeature_instantiation(instance):
    assert isinstance(instance, ClassM::StructuralFeature)

@given(instance=ClassM::StructuralFeature_strategy)
def test_classm::structuralfeature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ClassM::StructuralFeature_strategy)
def test_classm::structuralfeature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ClassM::StructuralFeature_strategy)
def test_classm::structuralfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassM::StructuralFeature_strategy)
def test_classm::structuralfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassM::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classm::primitivetype_instantiation(instance):
    assert isinstance(instance, ClassM::PrimitiveType)

@given(instance=ClassM::Class_strategy)
@settings(max_examples=50)
def test_classm::class_instantiation(instance):
    assert isinstance(instance, ClassM::Class)
