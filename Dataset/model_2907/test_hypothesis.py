import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Model,
    Type,
    Data_PrimitiveType,
    Data_Entity,
    Data_Attribute,
    Data_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_data_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Data_PrimitiveType)


def test_data_primitivetype_constructor_exists():
    assert callable(Data_PrimitiveType.__init__)


def test_data_primitivetype_constructor_args():
    sig = inspect.signature(Data_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_data_entity_is_not_abstract():
    assert not inspect.isabstract(Data_Entity)


def test_data_entity_constructor_exists():
    assert callable(Data_Entity.__init__)


def test_data_entity_constructor_args():
    sig = inspect.signature(Data_Entity.__init__)
    params = list(sig.parameters.keys())



def test_data_attribute_is_not_abstract():
    assert not inspect.isabstract(Data_Attribute)


def test_data_attribute_constructor_exists():
    assert callable(Data_Attribute.__init__)


def test_data_attribute_constructor_args():
    sig = inspect.signature(Data_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data_attribute_has_name():
    assert hasattr(Data_Attribute, "name")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_type_is_not_abstract():
    assert not inspect.isabstract(Data_Type)


def test_data_type_constructor_exists():
    assert callable(Data_Type.__init__)


def test_data_type_constructor_args():
    sig = inspect.signature(Data_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data_type_has_name():
    assert hasattr(Data_Type, "name")
    descriptor = None
    for klass in Data_Type.__mro__:
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
Data_Model_strategy = st.builds(
    Data_Model,
)
Type_strategy = st.builds(
    Type,
)
Data_PrimitiveType_strategy = st.builds(
    Data_PrimitiveType,
)
Data_Entity_strategy = st.builds(
    Data_Entity,
)
Data_Attribute_strategy = st.builds(
    Data_Attribute,
    name=
        safe_text
)
Data_Type_strategy = st.builds(
    Data_Type,
    name=
        safe_text
)

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Data_PrimitiveType_strategy)
@settings(max_examples=50)
def test_data_primitivetype_instantiation(instance):
    assert isinstance(instance, Data_PrimitiveType)

@given(instance=Data_Entity_strategy)
@settings(max_examples=50)
def test_data_entity_instantiation(instance):
    assert isinstance(instance, Data_Entity)

@given(instance=Data_Attribute_strategy)
@settings(max_examples=50)
def test_data_attribute_instantiation(instance):
    assert isinstance(instance, Data_Attribute)



@given(instance=Data_Attribute_strategy)
def test_data_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Type_strategy)
@settings(max_examples=50)
def test_data_type_instantiation(instance):
    assert isinstance(instance, Data_Type)



@given(instance=Data_Type_strategy)
def test_data_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
