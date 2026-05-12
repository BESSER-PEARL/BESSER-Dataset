import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassMM_ClassModel,
    Classifier,
    ClassMM_PrimitiveDataType,
    ClassMM_Attribute,
    ClassMM_Class,
    ClassMM_Association,
    ClassMM_Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classmm_classmodel_is_not_abstract():
    assert not inspect.isabstract(ClassMM_ClassModel)


def test_classmm_classmodel_constructor_exists():
    assert callable(ClassMM_ClassModel.__init__)


def test_classmm_classmodel_constructor_args():
    sig = inspect.signature(ClassMM_ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classmm_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(ClassMM_PrimitiveDataType)


def test_classmm_primitivedatatype_constructor_exists():
    assert callable(ClassMM_PrimitiveDataType.__init__)


def test_classmm_primitivedatatype_constructor_args():
    sig = inspect.signature(ClassMM_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_classmm_attribute_is_not_abstract():
    assert not inspect.isabstract(ClassMM_Attribute)


def test_classmm_attribute_constructor_exists():
    assert callable(ClassMM_Attribute.__init__)


def test_classmm_attribute_constructor_args():
    sig = inspect.signature(ClassMM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_classmm_attribute_has_is_primary():
    assert hasattr(ClassMM_Attribute, "is_primary")
    descriptor = None
    for klass in ClassMM_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_classmm_attribute_has_name():
    assert hasattr(ClassMM_Attribute, "name")
    descriptor = None
    for klass in ClassMM_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmm_class_is_not_abstract():
    assert not inspect.isabstract(ClassMM_Class)


def test_classmm_class_constructor_exists():
    assert callable(ClassMM_Class.__init__)


def test_classmm_class_constructor_args():
    sig = inspect.signature(ClassMM_Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_classmm_class_has_is_persistent():
    assert hasattr(ClassMM_Class, "is_persistent")
    descriptor = None
    for klass in ClassMM_Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_classmm_association_is_not_abstract():
    assert not inspect.isabstract(ClassMM_Association)


def test_classmm_association_constructor_exists():
    assert callable(ClassMM_Association.__init__)


def test_classmm_association_constructor_args():
    sig = inspect.signature(ClassMM_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm_association_has_name():
    assert hasattr(ClassMM_Association, "name")
    descriptor = None
    for klass in ClassMM_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmm_classifier_is_not_abstract():
    assert not inspect.isabstract(ClassMM_Classifier)


def test_classmm_classifier_constructor_exists():
    assert callable(ClassMM_Classifier.__init__)


def test_classmm_classifier_constructor_args():
    sig = inspect.signature(ClassMM_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm_classifier_has_name():
    assert hasattr(ClassMM_Classifier, "name")
    descriptor = None
    for klass in ClassMM_Classifier.__mro__:
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
ClassMM_ClassModel_strategy = st.builds(
    ClassMM_ClassModel,
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassMM_PrimitiveDataType_strategy = st.builds(
    ClassMM_PrimitiveDataType,
)
ClassMM_Attribute_strategy = st.builds(
    ClassMM_Attribute,
    is_primary=
        safe_text,
    name=
        safe_text
)
ClassMM_Class_strategy = st.builds(
    ClassMM_Class,
    is_persistent=
        safe_text
)
ClassMM_Association_strategy = st.builds(
    ClassMM_Association,
    name=
        safe_text
)
ClassMM_Classifier_strategy = st.builds(
    ClassMM_Classifier,
    name=
        safe_text
)

@given(instance=ClassMM_ClassModel_strategy)
@settings(max_examples=50)
def test_classmm_classmodel_instantiation(instance):
    assert isinstance(instance, ClassMM_ClassModel)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassMM_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_classmm_primitivedatatype_instantiation(instance):
    assert isinstance(instance, ClassMM_PrimitiveDataType)

@given(instance=ClassMM_Attribute_strategy)
@settings(max_examples=50)
def test_classmm_attribute_instantiation(instance):
    assert isinstance(instance, ClassMM_Attribute)



@given(instance=ClassMM_Attribute_strategy)
def test_classmm_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original



@given(instance=ClassMM_Attribute_strategy)
def test_classmm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassMM_Class_strategy)
@settings(max_examples=50)
def test_classmm_class_instantiation(instance):
    assert isinstance(instance, ClassMM_Class)



@given(instance=ClassMM_Class_strategy)
def test_classmm_class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=ClassMM_Association_strategy)
@settings(max_examples=50)
def test_classmm_association_instantiation(instance):
    assert isinstance(instance, ClassMM_Association)



@given(instance=ClassMM_Association_strategy)
def test_classmm_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassMM_Classifier_strategy)
@settings(max_examples=50)
def test_classmm_classifier_instantiation(instance):
    assert isinstance(instance, ClassMM_Classifier)



@given(instance=ClassMM_Classifier_strategy)
def test_classmm_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
