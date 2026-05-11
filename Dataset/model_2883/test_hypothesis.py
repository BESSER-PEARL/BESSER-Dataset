import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entitiesDsl::Feature,
    Type,
    entitiesDsl::Entity,
    entitiesDsl::DataType,
    entitiesDsl::Type,
    entitiesDsl::Model,
    Feature,
    entitiesDsl::Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entitiesdsl::feature_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::Feature)


def test_entitiesdsl::feature_constructor_exists():
    assert callable(entitiesDsl::Feature.__init__)


def test_entitiesdsl::feature_constructor_args():
    sig = inspect.signature(entitiesDsl::Feature.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl::entity_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::Entity)


def test_entitiesdsl::entity_constructor_exists():
    assert callable(entitiesDsl::Entity.__init__)


def test_entitiesdsl::entity_constructor_args():
    sig = inspect.signature(entitiesDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl::datatype_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::DataType)


def test_entitiesdsl::datatype_constructor_exists():
    assert callable(entitiesDsl::DataType.__init__)


def test_entitiesdsl::datatype_constructor_args():
    sig = inspect.signature(entitiesDsl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl::type_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::Type)


def test_entitiesdsl::type_constructor_exists():
    assert callable(entitiesDsl::Type.__init__)


def test_entitiesdsl::type_constructor_args():
    sig = inspect.signature(entitiesDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitiesdsl::type_has_name():
    assert hasattr(entitiesDsl::Type, "name")
    descriptor = None
    for klass in entitiesDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitiesdsl::model_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::Model)


def test_entitiesdsl::model_constructor_exists():
    assert callable(entitiesDsl::Model.__init__)


def test_entitiesdsl::model_constructor_args():
    sig = inspect.signature(entitiesDsl::Model.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_entitiesdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(entitiesDsl::Attribute)


def test_entitiesdsl::attribute_constructor_exists():
    assert callable(entitiesDsl::Attribute.__init__)


def test_entitiesdsl::attribute_constructor_args():
    sig = inspect.signature(entitiesDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "attrrName" in params, "Missing parameter 'attrrName'"

def test_entitiesdsl::attribute_has_attrrName():
    assert hasattr(entitiesDsl::Attribute, "attrrName")
    descriptor = None
    for klass in entitiesDsl::Attribute.__mro__:
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
entitiesDsl::Feature_strategy = st.builds(
    entitiesDsl::Feature,
)
Type_strategy = st.builds(
    Type,
)
entitiesDsl::Entity_strategy = st.builds(
    entitiesDsl::Entity,
)
entitiesDsl::DataType_strategy = st.builds(
    entitiesDsl::DataType,
)
entitiesDsl::Type_strategy = st.builds(
    entitiesDsl::Type,
    name=
        safe_text
)
entitiesDsl::Model_strategy = st.builds(
    entitiesDsl::Model,
)
Feature_strategy = st.builds(
    Feature,
)
entitiesDsl::Attribute_strategy = st.builds(
    entitiesDsl::Attribute,
    attrrName=
        safe_text
)

@given(instance=entitiesDsl::Feature_strategy)
@settings(max_examples=50)
def test_entitiesdsl::feature_instantiation(instance):
    assert isinstance(instance, entitiesDsl::Feature)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entitiesDsl::Entity_strategy)
@settings(max_examples=50)
def test_entitiesdsl::entity_instantiation(instance):
    assert isinstance(instance, entitiesDsl::Entity)

@given(instance=entitiesDsl::DataType_strategy)
@settings(max_examples=50)
def test_entitiesdsl::datatype_instantiation(instance):
    assert isinstance(instance, entitiesDsl::DataType)

@given(instance=entitiesDsl::Type_strategy)
@settings(max_examples=50)
def test_entitiesdsl::type_instantiation(instance):
    assert isinstance(instance, entitiesDsl::Type)

@given(instance=entitiesDsl::Type_strategy)
def test_entitiesdsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entitiesDsl::Type_strategy)
def test_entitiesdsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitiesDsl::Model_strategy)
@settings(max_examples=50)
def test_entitiesdsl::model_instantiation(instance):
    assert isinstance(instance, entitiesDsl::Model)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=entitiesDsl::Attribute_strategy)
@settings(max_examples=50)
def test_entitiesdsl::attribute_instantiation(instance):
    assert isinstance(instance, entitiesDsl::Attribute)

@given(instance=entitiesDsl::Attribute_strategy)
def test_entitiesdsl::attribute_attrrName_type(instance):
    assert isinstance(instance.attrrName, str)


@given(instance=entitiesDsl::Attribute_strategy)
def test_entitiesdsl::attribute_attrrName_setter(instance):
    original = instance.attrrName
    instance.attrrName = original
    assert instance.attrrName == original
