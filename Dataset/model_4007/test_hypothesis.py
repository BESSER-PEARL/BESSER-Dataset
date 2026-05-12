import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Type,
    Data_Attribute,
    Data_Class,
    Data_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_type_is_not_abstract():
    assert not inspect.isabstract(Data_Type)


def test_data_type_constructor_exists():
    assert callable(Data_Type.__init__)


def test_data_type_constructor_args():
    sig = inspect.signature(Data_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isReference" in params, "Missing parameter 'isReference'"
    assert "name" in params, "Missing parameter 'name'"

def test_data_type_has_isReference():
    assert hasattr(Data_Type, "isReference")
    descriptor = None
    for klass in Data_Type.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)

def test_data_type_has_name():
    assert hasattr(Data_Type, "name")
    descriptor = None
    for klass in Data_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_attribute_is_not_abstract():
    assert not inspect.isabstract(Data_Attribute)


def test_data_attribute_constructor_exists():
    assert callable(Data_Attribute.__init__)


def test_data_attribute_constructor_args():
    sig = inspect.signature(Data_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_data_attribute_has_name():
    assert hasattr(Data_Attribute, "name")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data_attribute_has_visibility():
    assert hasattr(Data_Attribute, "visibility")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_data_class_is_not_abstract():
    assert not inspect.isabstract(Data_Class)


def test_data_class_constructor_exists():
    assert callable(Data_Class.__init__)


def test_data_class_constructor_args():
    sig = inspect.signature(Data_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data_class_has_name():
    assert hasattr(Data_Class, "name")
    descriptor = None
    for klass in Data_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
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
Data_Type_strategy = st.builds(
    Data_Type,
    isReference=
        st.booleans(),
    name=
        safe_text
)
Data_Attribute_strategy = st.builds(
    Data_Attribute,
    name=
        safe_text,
    visibility=
        safe_text
)
Data_Class_strategy = st.builds(
    Data_Class,
    name=
        safe_text
)
Data_Model_strategy = st.builds(
    Data_Model,
)

@given(instance=Data_Type_strategy)
@settings(max_examples=50)
def test_data_type_instantiation(instance):
    assert isinstance(instance, Data_Type)



@given(instance=Data_Type_strategy)
def test_data_type_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original



@given(instance=Data_Type_strategy)
def test_data_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Attribute_strategy)
@settings(max_examples=50)
def test_data_attribute_instantiation(instance):
    assert isinstance(instance, Data_Attribute)



@given(instance=Data_Attribute_strategy)
def test_data_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Data_Attribute_strategy)
def test_data_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Data_Class_strategy)
@settings(max_examples=50)
def test_data_class_instantiation(instance):
    assert isinstance(instance, Data_Class)



@given(instance=Data_Class_strategy)
def test_data_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)
