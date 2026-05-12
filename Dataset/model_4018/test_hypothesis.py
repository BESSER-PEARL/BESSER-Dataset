import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Attribute,
    Data_Class,
    Data_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_attribute_is_not_abstract():
    assert not inspect.isabstract(Data_Attribute)


def test_data_attribute_constructor_exists():
    assert callable(Data_Attribute.__init__)


def test_data_attribute_constructor_args():
    sig = inspect.signature(Data_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_data_attribute_has_Type():
    assert hasattr(Data_Attribute, "Type")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_data_attribute_has_Name():
    assert hasattr(Data_Attribute, "Name")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_data_class_is_not_abstract():
    assert not inspect.isabstract(Data_Class)


def test_data_class_constructor_exists():
    assert callable(Data_Class.__init__)


def test_data_class_constructor_args():
    sig = inspect.signature(Data_Class.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_data_class_has_Name():
    assert hasattr(Data_Class, "Name")
    descriptor = None
    for klass in Data_Class.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Data_Attribute_strategy = st.builds(
    Data_Attribute,
    Type=
        safe_text,
    Name=
        safe_text
)
Data_Class_strategy = st.builds(
    Data_Class,
    Name=
        safe_text
)
Data_Model_strategy = st.builds(
    Data_Model,
)

@given(instance=Data_Attribute_strategy)
@settings(max_examples=50)
def test_data_attribute_instantiation(instance):
    assert isinstance(instance, Data_Attribute)



@given(instance=Data_Attribute_strategy)
def test_data_attribute_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Data_Attribute_strategy)
def test_data_attribute_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data_Class_strategy)
@settings(max_examples=50)
def test_data_class_instantiation(instance):
    assert isinstance(instance, Data_Class)



@given(instance=Data_Class_strategy)
def test_data_class_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)
