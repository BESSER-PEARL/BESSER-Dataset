import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassM_Classifier,
    ClassM_Attribute,
    Classifier,
    ClassM_Class,
    ClassM_Model,
    ClassM_PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_classm_attribute_is_not_abstract():
    assert not inspect.isabstract(ClassM_Attribute)


def test_classm_attribute_constructor_exists():
    assert callable(ClassM_Attribute.__init__)


def test_classm_attribute_constructor_args():
    sig = inspect.signature(ClassM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_classm_attribute_has_name():
    assert hasattr(ClassM_Attribute, "name")
    descriptor = None
    for klass in ClassM_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classm_attribute_has_is_primary():
    assert hasattr(ClassM_Attribute, "is_primary")
    descriptor = None
    for klass in ClassM_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classm_class_is_not_abstract():
    assert not inspect.isabstract(ClassM_Class)


def test_classm_class_constructor_exists():
    assert callable(ClassM_Class.__init__)


def test_classm_class_constructor_args():
    sig = inspect.signature(ClassM_Class.__init__)
    params = list(sig.parameters.keys())



def test_classm_model_is_not_abstract():
    assert not inspect.isabstract(ClassM_Model)


def test_classm_model_constructor_exists():
    assert callable(ClassM_Model.__init__)


def test_classm_model_constructor_args():
    sig = inspect.signature(ClassM_Model.__init__)
    params = list(sig.parameters.keys())



def test_classm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ClassM_PrimitiveType)


def test_classm_primitivetype_constructor_exists():
    assert callable(ClassM_PrimitiveType.__init__)


def test_classm_primitivetype_constructor_args():
    sig = inspect.signature(ClassM_PrimitiveType.__init__)
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
ClassM_Classifier_strategy = st.builds(
    ClassM_Classifier,
    name=
        safe_text
)
ClassM_Attribute_strategy = st.builds(
    ClassM_Attribute,
    name=
        safe_text,
    is_primary=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassM_Class_strategy = st.builds(
    ClassM_Class,
)
ClassM_Model_strategy = st.builds(
    ClassM_Model,
)
ClassM_PrimitiveType_strategy = st.builds(
    ClassM_PrimitiveType,
)

@given(instance=ClassM_Classifier_strategy)
@settings(max_examples=50)
def test_classm_classifier_instantiation(instance):
    assert isinstance(instance, ClassM_Classifier)



@given(instance=ClassM_Classifier_strategy)
def test_classm_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassM_Attribute_strategy)
@settings(max_examples=50)
def test_classm_attribute_instantiation(instance):
    assert isinstance(instance, ClassM_Attribute)



@given(instance=ClassM_Attribute_strategy)
def test_classm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ClassM_Attribute_strategy)
def test_classm_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassM_Class_strategy)
@settings(max_examples=50)
def test_classm_class_instantiation(instance):
    assert isinstance(instance, ClassM_Class)

@given(instance=ClassM_Model_strategy)
@settings(max_examples=50)
def test_classm_model_instantiation(instance):
    assert isinstance(instance, ClassM_Model)

@given(instance=ClassM_PrimitiveType_strategy)
@settings(max_examples=50)
def test_classm_primitivetype_instantiation(instance):
    assert isinstance(instance, ClassM_PrimitiveType)
