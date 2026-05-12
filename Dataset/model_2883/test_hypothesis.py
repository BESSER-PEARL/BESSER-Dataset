import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entitiesDsl_Feature,
    Type,
    entitiesDsl_Entity,
    entitiesDsl_DataType,
    entitiesDsl_Type,
    entitiesDsl_Model,
    Feature,
    entitiesDsl_Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entitiesdsl_feature_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_Feature)


def test_entitiesdsl_feature_constructor_exists():
    assert callable(entitiesDsl_Feature.__init__)


def test_entitiesdsl_feature_constructor_args():
    sig = inspect.signature(entitiesDsl_Feature.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl_entity_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_Entity)


def test_entitiesdsl_entity_constructor_exists():
    assert callable(entitiesDsl_Entity.__init__)


def test_entitiesdsl_entity_constructor_args():
    sig = inspect.signature(entitiesDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl_datatype_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_DataType)


def test_entitiesdsl_datatype_constructor_exists():
    assert callable(entitiesDsl_DataType.__init__)


def test_entitiesdsl_datatype_constructor_args():
    sig = inspect.signature(entitiesDsl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl_type_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_Type)


def test_entitiesdsl_type_constructor_exists():
    assert callable(entitiesDsl_Type.__init__)


def test_entitiesdsl_type_constructor_args():
    sig = inspect.signature(entitiesDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitiesdsl_type_has_name():
    assert hasattr(entitiesDsl_Type, "name")
    descriptor = None
    for klass in entitiesDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitiesdsl_model_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_Model)


def test_entitiesdsl_model_constructor_exists():
    assert callable(entitiesDsl_Model.__init__)


def test_entitiesdsl_model_constructor_args():
    sig = inspect.signature(entitiesDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl_attribute_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl_Attribute)


def test_entitiesdsl_attribute_constructor_exists():
    assert callable(entitiesDsl_Attribute.__init__)


def test_entitiesdsl_attribute_constructor_args():
    sig = inspect.signature(entitiesDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "attrrName" in params, "Missing parameter 'attrrName'"

def test_entitiesdsl_attribute_has_attrrName():
    assert hasattr(entitiesDsl_Attribute, "attrrName")
    descriptor = None
    for klass in entitiesDsl_Attribute.__mro__:
        if "attrrName" in klass.__dict__:
            descriptor = klass.__dict__["attrrName"]
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
entitiesDsl_Feature_strategy = st.builds(
    entitiesDsl_Feature,
)
Type_strategy = st.builds(
    Type,
)
entitiesDsl_Entity_strategy = st.builds(
    entitiesDsl_Entity,
)
entitiesDsl_DataType_strategy = st.builds(
    entitiesDsl_DataType,
)
entitiesDsl_Type_strategy = st.builds(
    entitiesDsl_Type,
    name=
        safe_text
)
entitiesDsl_Model_strategy = st.builds(
    entitiesDsl_Model,
)
Feature_strategy = st.builds(
    Feature,
)
entitiesDsl_Attribute_strategy = st.builds(
    entitiesDsl_Attribute,
    attrrName=
        safe_text
)

@given(instance=entitiesDsl_Feature_strategy)
@settings(max_examples=50)
def test_entitiesdsl_feature_instantiation(instance):
    assert isinstance(instance, entitiesDsl_Feature)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entitiesDsl_Entity_strategy)
@settings(max_examples=50)
def test_entitiesdsl_entity_instantiation(instance):
    assert isinstance(instance, entitiesDsl_Entity)

@given(instance=entitiesDsl_DataType_strategy)
@settings(max_examples=50)
def test_entitiesdsl_datatype_instantiation(instance):
    assert isinstance(instance, entitiesDsl_DataType)

@given(instance=entitiesDsl_Type_strategy)
@settings(max_examples=50)
def test_entitiesdsl_type_instantiation(instance):
    assert isinstance(instance, entitiesDsl_Type)



@given(instance=entitiesDsl_Type_strategy)
def test_entitiesdsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitiesDsl_Model_strategy)
@settings(max_examples=50)
def test_entitiesdsl_model_instantiation(instance):
    assert isinstance(instance, entitiesDsl_Model)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=entitiesDsl_Attribute_strategy)
@settings(max_examples=50)
def test_entitiesdsl_attribute_instantiation(instance):
    assert isinstance(instance, entitiesDsl_Attribute)



@given(instance=entitiesDsl_Attribute_strategy)
def test_entitiesdsl_attribute_attrrName_setter(instance):
    original = instance.attrrName
    instance.attrrName = original
    assert instance.attrrName == original
