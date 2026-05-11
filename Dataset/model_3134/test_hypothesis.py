import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassDiagram::Classifier,
    ClassDiagram::Model,
    StructuralFeature,
    ClassDiagram::Attribute,
    ClassDiagram::Operation,
    ClassDiagram::TypedElement,
    TypedElement,
    ClassDiagram::Parameter,
    ClassDiagram::StructuralFeature,
    Classifier,
    ClassDiagram::PrimitiveType,
    ClassDiagram::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(ClassDiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(ClassDiagram::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::classifier_has_name():
    assert hasattr(ClassDiagram::Classifier, "name")
    descriptor = None
    for klass in ClassDiagram::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::model_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Model)


def test_classdiagram::model_constructor_exists():
    assert callable(ClassDiagram::Model.__init__)


def test_classdiagram::model_constructor_args():
    sig = inspect.signature(ClassDiagram::Model.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(ClassDiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(ClassDiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_classdiagram::attribute_has_multivalued():
    assert hasattr(ClassDiagram::Attribute, "multivalued")
    descriptor = None
    for klass in ClassDiagram::Attribute.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::operation_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Operation)


def test_classdiagram::operation_constructor_exists():
    assert callable(ClassDiagram::Operation.__init__)


def test_classdiagram::operation_constructor_args():
    sig = inspect.signature(ClassDiagram::Operation.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::typedelement_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::TypedElement)


def test_classdiagram::typedelement_constructor_exists():
    assert callable(ClassDiagram::TypedElement.__init__)


def test_classdiagram::typedelement_constructor_args():
    sig = inspect.signature(ClassDiagram::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::parameter_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Parameter)


def test_classdiagram::parameter_constructor_exists():
    assert callable(ClassDiagram::Parameter.__init__)


def test_classdiagram::parameter_constructor_args():
    sig = inspect.signature(ClassDiagram::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::parameter_has_name():
    assert hasattr(ClassDiagram::Parameter, "name")
    descriptor = None
    for klass in ClassDiagram::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::StructuralFeature)


def test_classdiagram::structuralfeature_constructor_exists():
    assert callable(ClassDiagram::StructuralFeature.__init__)


def test_classdiagram::structuralfeature_constructor_args():
    sig = inspect.signature(ClassDiagram::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::structuralfeature_has_visibility():
    assert hasattr(ClassDiagram::StructuralFeature, "visibility")
    descriptor = None
    for klass in ClassDiagram::StructuralFeature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::structuralfeature_has_name():
    assert hasattr(ClassDiagram::StructuralFeature, "name")
    descriptor = None
    for klass in ClassDiagram::StructuralFeature.__mro__:
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



def test_classdiagram::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::PrimitiveType)


def test_classdiagram::primitivetype_constructor_exists():
    assert callable(ClassDiagram::PrimitiveType.__init__)


def test_classdiagram::primitivetype_constructor_args():
    sig = inspect.signature(ClassDiagram::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(ClassDiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(ClassDiagram::Class.__init__)
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
ClassDiagram::Classifier_strategy = st.builds(
    ClassDiagram::Classifier,
    name=
        safe_text
)
ClassDiagram::Model_strategy = st.builds(
    ClassDiagram::Model,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ClassDiagram::Attribute_strategy = st.builds(
    ClassDiagram::Attribute,
    multivalued=
        st.booleans()
)
ClassDiagram::Operation_strategy = st.builds(
    ClassDiagram::Operation,
)
ClassDiagram::TypedElement_strategy = st.builds(
    ClassDiagram::TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ClassDiagram::Parameter_strategy = st.builds(
    ClassDiagram::Parameter,
    name=
        safe_text
)
ClassDiagram::StructuralFeature_strategy = st.builds(
    ClassDiagram::StructuralFeature,
    visibility=
        safe_text,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassDiagram::PrimitiveType_strategy = st.builds(
    ClassDiagram::PrimitiveType,
)
ClassDiagram::Class_strategy = st.builds(
    ClassDiagram::Class,
)

@given(instance=ClassDiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Classifier)

@given(instance=ClassDiagram::Classifier_strategy)
def test_classdiagram::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Classifier_strategy)
def test_classdiagram::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassDiagram::Model_strategy)
@settings(max_examples=50)
def test_classdiagram::model_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Model)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ClassDiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Attribute)

@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=ClassDiagram::Operation_strategy)
@settings(max_examples=50)
def test_classdiagram::operation_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Operation)

@given(instance=ClassDiagram::TypedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::typedelement_instantiation(instance):
    assert isinstance(instance, ClassDiagram::TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ClassDiagram::Parameter_strategy)
@settings(max_examples=50)
def test_classdiagram::parameter_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Parameter)

@given(instance=ClassDiagram::Parameter_strategy)
def test_classdiagram::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Parameter_strategy)
def test_classdiagram::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassDiagram::StructuralFeature_strategy)
@settings(max_examples=50)
def test_classdiagram::structuralfeature_instantiation(instance):
    assert isinstance(instance, ClassDiagram::StructuralFeature)

@given(instance=ClassDiagram::StructuralFeature_strategy)
def test_classdiagram::structuralfeature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ClassDiagram::StructuralFeature_strategy)
def test_classdiagram::structuralfeature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ClassDiagram::StructuralFeature_strategy)
def test_classdiagram::structuralfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::StructuralFeature_strategy)
def test_classdiagram::structuralfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassDiagram::PrimitiveType_strategy)
@settings(max_examples=50)
def test_classdiagram::primitivetype_instantiation(instance):
    assert isinstance(instance, ClassDiagram::PrimitiveType)

@given(instance=ClassDiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Class)
