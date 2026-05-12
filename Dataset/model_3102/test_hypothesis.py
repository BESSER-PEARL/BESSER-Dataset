import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    simpleUML_MM_PrimitiveDataType,
    simpleUML_MM_Attribute,
    simpleUML_MM_Class,
    simpleUML_MM_Association,
    simpleUML_MM_Classifier,
    simpleUML_MM_ClassModel,
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



def test_simpleuml_mm_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_PrimitiveDataType)


def test_simpleuml_mm_primitivedatatype_constructor_exists():
    assert callable(simpleUML_MM_PrimitiveDataType.__init__)


def test_simpleuml_mm_primitivedatatype_constructor_args():
    sig = inspect.signature(simpleUML_MM_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_mm_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_Attribute)


def test_simpleuml_mm_attribute_constructor_exists():
    assert callable(simpleUML_MM_Attribute.__init__)


def test_simpleuml_mm_attribute_constructor_args():
    sig = inspect.signature(simpleUML_MM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_simpleuml_mm_attribute_has_name():
    assert hasattr(simpleUML_MM_Attribute, "name")
    descriptor = None
    for klass in simpleUML_MM_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml_mm_attribute_has_is_primary():
    assert hasattr(simpleUML_MM_Attribute, "is_primary")
    descriptor = None
    for klass in simpleUML_MM_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_mm_class_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_Class)


def test_simpleuml_mm_class_constructor_exists():
    assert callable(simpleUML_MM_Class.__init__)


def test_simpleuml_mm_class_constructor_args():
    sig = inspect.signature(simpleUML_MM_Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_simpleuml_mm_class_has_is_persistent():
    assert hasattr(simpleUML_MM_Class, "is_persistent")
    descriptor = None
    for klass in simpleUML_MM_Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_mm_association_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_Association)


def test_simpleuml_mm_association_constructor_exists():
    assert callable(simpleUML_MM_Association.__init__)


def test_simpleuml_mm_association_constructor_args():
    sig = inspect.signature(simpleUML_MM_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_mm_association_has_name():
    assert hasattr(simpleUML_MM_Association, "name")
    descriptor = None
    for klass in simpleUML_MM_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_mm_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_Classifier)


def test_simpleuml_mm_classifier_constructor_exists():
    assert callable(simpleUML_MM_Classifier.__init__)


def test_simpleuml_mm_classifier_constructor_args():
    sig = inspect.signature(simpleUML_MM_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_mm_classifier_has_name():
    assert hasattr(simpleUML_MM_Classifier, "name")
    descriptor = None
    for klass in simpleUML_MM_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_mm_classmodel_is_not_abstract():
    assert not inspect.isabstract(simpleUML_MM_ClassModel)


def test_simpleuml_mm_classmodel_constructor_exists():
    assert callable(simpleUML_MM_ClassModel.__init__)


def test_simpleuml_mm_classmodel_constructor_args():
    sig = inspect.signature(simpleUML_MM_ClassModel.__init__)
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
Classifier_strategy = st.builds(
    Classifier,
)
simpleUML_MM_PrimitiveDataType_strategy = st.builds(
    simpleUML_MM_PrimitiveDataType,
)
simpleUML_MM_Attribute_strategy = st.builds(
    simpleUML_MM_Attribute,
    name=
        safe_text,
    is_primary=
        st.booleans()
)
simpleUML_MM_Class_strategy = st.builds(
    simpleUML_MM_Class,
    is_persistent=
        st.booleans()
)
simpleUML_MM_Association_strategy = st.builds(
    simpleUML_MM_Association,
    name=
        safe_text
)
simpleUML_MM_Classifier_strategy = st.builds(
    simpleUML_MM_Classifier,
    name=
        safe_text
)
simpleUML_MM_ClassModel_strategy = st.builds(
    simpleUML_MM_ClassModel,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUML_MM_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_PrimitiveDataType)

@given(instance=simpleUML_MM_Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_attribute_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_Attribute)



@given(instance=simpleUML_MM_Attribute_strategy)
def test_simpleuml_mm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simpleUML_MM_Attribute_strategy)
def test_simpleuml_mm_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=simpleUML_MM_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_class_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_Class)



@given(instance=simpleUML_MM_Class_strategy)
def test_simpleuml_mm_class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=simpleUML_MM_Association_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_association_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_Association)



@given(instance=simpleUML_MM_Association_strategy)
def test_simpleuml_mm_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUML_MM_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_classifier_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_Classifier)



@given(instance=simpleUML_MM_Classifier_strategy)
def test_simpleuml_mm_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUML_MM_ClassModel_strategy)
@settings(max_examples=50)
def test_simpleuml_mm_classmodel_instantiation(instance):
    assert isinstance(instance, simpleUML_MM_ClassModel)
