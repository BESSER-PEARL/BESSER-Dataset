import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classes_Attribute,
    Type,
    classes_DataType,
    classes_Type,
    classes_Class,
    classes_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(classes_Attribute)


def test_classes_attribute_constructor_exists():
    assert callable(classes_Attribute.__init__)


def test_classes_attribute_constructor_args():
    sig = inspect.signature(classes_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_classes_attribute_has_value():
    assert hasattr(classes_Attribute, "value")
    descriptor = None
    for klass in classes_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_classes_attribute_has_name():
    assert hasattr(classes_Attribute, "name")
    descriptor = None
    for klass in classes_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_classes_datatype_is_not_abstract():
    assert not inspect.isabstract(classes_DataType)


def test_classes_datatype_constructor_exists():
    assert callable(classes_DataType.__init__)


def test_classes_datatype_constructor_args():
    sig = inspect.signature(classes_DataType.__init__)
    params = list(sig.parameters.keys())



def test_classes_type_is_not_abstract():
    assert not inspect.isabstract(classes_Type)


def test_classes_type_constructor_exists():
    assert callable(classes_Type.__init__)


def test_classes_type_constructor_args():
    sig = inspect.signature(classes_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes_type_has_name():
    assert hasattr(classes_Type, "name")
    descriptor = None
    for klass in classes_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_classes_model_is_not_abstract():
    assert not inspect.isabstract(classes_Model)


def test_classes_model_constructor_exists():
    assert callable(classes_Model.__init__)


def test_classes_model_constructor_args():
    sig = inspect.signature(classes_Model.__init__)
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
classes_Attribute_strategy = st.builds(
    classes_Attribute,
    value=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
classes_DataType_strategy = st.builds(
    classes_DataType,
)
classes_Type_strategy = st.builds(
    classes_Type,
    name=
        safe_text
)
classes_Class_strategy = st.builds(
    classes_Class,
)
classes_Model_strategy = st.builds(
    classes_Model,
)

@given(instance=classes_Attribute_strategy)
@settings(max_examples=50)
def test_classes_attribute_instantiation(instance):
    assert isinstance(instance, classes_Attribute)



@given(instance=classes_Attribute_strategy)
def test_classes_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=classes_Attribute_strategy)
def test_classes_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=classes_DataType_strategy)
@settings(max_examples=50)
def test_classes_datatype_instantiation(instance):
    assert isinstance(instance, classes_DataType)

@given(instance=classes_Type_strategy)
@settings(max_examples=50)
def test_classes_type_instantiation(instance):
    assert isinstance(instance, classes_Type)



@given(instance=classes_Type_strategy)
def test_classes_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_Class_strategy)
@settings(max_examples=50)
def test_classes_class_instantiation(instance):
    assert isinstance(instance, classes_Class)

@given(instance=classes_Model_strategy)
@settings(max_examples=50)
def test_classes_model_instantiation(instance):
    assert isinstance(instance, classes_Model)
