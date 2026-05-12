import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassM_Model,
    StructuralFeature,
    ClassM_Attribute,
    ClassM_Operation,
    TypedElement,
    ClassM_Parameter,
    ClassM_TypedElement,
    ClassM_Classifier,
    ClassM_StructuralFeature,
    Classifier,
    ClassM_PrimitiveType,
    ClassM_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classm_model_is_not_abstract():
    assert not inspect.isabstract(ClassM_Model)


def test_classm_model_constructor_exists():
    assert callable(ClassM_Model.__init__)


def test_classm_model_constructor_args():
    sig = inspect.signature(ClassM_Model.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classm_attribute_is_not_abstract():
    assert not inspect.isabstract(ClassM_Attribute)


def test_classm_attribute_constructor_exists():
    assert callable(ClassM_Attribute.__init__)


def test_classm_attribute_constructor_args():
    sig = inspect.signature(ClassM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_classm_attribute_has_multivalued():
    assert hasattr(ClassM_Attribute, "multivalued")
    descriptor = None
    for klass in ClassM_Attribute.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_classm_operation_is_not_abstract():
    assert not inspect.isabstract(ClassM_Operation)


def test_classm_operation_constructor_exists():
    assert callable(ClassM_Operation.__init__)


def test_classm_operation_constructor_args():
    sig = inspect.signature(ClassM_Operation.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classm_parameter_is_not_abstract():
    assert not inspect.isabstract(ClassM_Parameter)


def test_classm_parameter_constructor_exists():
    assert callable(ClassM_Parameter.__init__)


def test_classm_parameter_constructor_args():
    sig = inspect.signature(ClassM_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm_parameter_has_name():
    assert hasattr(ClassM_Parameter, "name")
    descriptor = None
    for klass in ClassM_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classm_typedelement_is_not_abstract():
    assert not inspect.isabstract(ClassM_TypedElement)


def test_classm_typedelement_constructor_exists():
    assert callable(ClassM_TypedElement.__init__)


def test_classm_typedelement_constructor_args():
    sig = inspect.signature(ClassM_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classm_classifier_is_not_abstract():
    assert not inspect.isabstract(ClassM_Classifier)


def test_classm_classifier_constructor_exists():
    assert callable(ClassM_Classifier.__init__)


def test_classm_classifier_constructor_args():
    sig = inspect.signature(ClassM_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm_classifier_has_name():
    assert hasattr(ClassM_Classifier, "name")
    descriptor = None
    for klass in ClassM_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classm_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ClassM_StructuralFeature)


def test_classm_structuralfeature_constructor_exists():
    assert callable(ClassM_StructuralFeature.__init__)


def test_classm_structuralfeature_constructor_args():
    sig = inspect.signature(ClassM_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classm_structuralfeature_has_name():
    assert hasattr(ClassM_StructuralFeature, "name")
    descriptor = None
    for klass in ClassM_StructuralFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classm_structuralfeature_has_visibility():
    assert hasattr(ClassM_StructuralFeature, "visibility")
    descriptor = None
    for klass in ClassM_StructuralFeature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassM_PrimitiveType)


def test_classm_primitivetype_constructor_exists():
    assert callable(ClassM_PrimitiveType.__init__)


def test_classm_primitivetype_constructor_args():
    sig = inspect.signature(ClassM_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_classm_class_is_not_abstract():
    assert not inspect.isabstract(ClassM_Class)


def test_classm_class_constructor_exists():
    assert callable(ClassM_Class.__init__)


def test_classm_class_constructor_args():
    sig = inspect.signature(ClassM_Class.__init__)
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
ClassM_Model_strategy = st.builds(
    ClassM_Model,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ClassM_Attribute_strategy = st.builds(
    ClassM_Attribute,
    multivalued=
        st.booleans()
)
ClassM_Operation_strategy = st.builds(
    ClassM_Operation,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ClassM_Parameter_strategy = st.builds(
    ClassM_Parameter,
    name=
        safe_text
)
ClassM_TypedElement_strategy = st.builds(
    ClassM_TypedElement,
)
ClassM_Classifier_strategy = st.builds(
    ClassM_Classifier,
    name=
        safe_text
)
ClassM_StructuralFeature_strategy = st.builds(
    ClassM_StructuralFeature,
    name=
        safe_text,
    visibility=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassM_PrimitiveType_strategy = st.builds(
    ClassM_PrimitiveType,
)
ClassM_Class_strategy = st.builds(
    ClassM_Class,
)

@given(instance=ClassM_Model_strategy)
@settings(max_examples=50)
def test_classm_model_instantiation(instance):
    assert isinstance(instance, ClassM_Model)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ClassM_Attribute_strategy)
@settings(max_examples=50)
def test_classm_attribute_instantiation(instance):
    assert isinstance(instance, ClassM_Attribute)



@given(instance=ClassM_Attribute_strategy)
def test_classm_attribute_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=ClassM_Operation_strategy)
@settings(max_examples=50)
def test_classm_operation_instantiation(instance):
    assert isinstance(instance, ClassM_Operation)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ClassM_Parameter_strategy)
@settings(max_examples=50)
def test_classm_parameter_instantiation(instance):
    assert isinstance(instance, ClassM_Parameter)



@given(instance=ClassM_Parameter_strategy)
def test_classm_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassM_TypedElement_strategy)
@settings(max_examples=50)
def test_classm_typedelement_instantiation(instance):
    assert isinstance(instance, ClassM_TypedElement)

@given(instance=ClassM_Classifier_strategy)
@settings(max_examples=50)
def test_classm_classifier_instantiation(instance):
    assert isinstance(instance, ClassM_Classifier)



@given(instance=ClassM_Classifier_strategy)
def test_classm_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassM_StructuralFeature_strategy)
@settings(max_examples=50)
def test_classm_structuralfeature_instantiation(instance):
    assert isinstance(instance, ClassM_StructuralFeature)



@given(instance=ClassM_StructuralFeature_strategy)
def test_classm_structuralfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ClassM_StructuralFeature_strategy)
def test_classm_structuralfeature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassM_PrimitiveType_strategy)
@settings(max_examples=50)
def test_classm_primitivetype_instantiation(instance):
    assert isinstance(instance, ClassM_PrimitiveType)

@given(instance=ClassM_Class_strategy)
@settings(max_examples=50)
def test_classm_class_instantiation(instance):
    assert isinstance(instance, ClassM_Class)
