import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entityDsl::Property,
    Type,
    entityDsl::Entity,
    entityDsl::SimpleType,
    entityDsl::Type,
    entityDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entitydsl::property_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Property)


def test_entitydsl::property_constructor_exists():
    assert callable(entityDsl::Property.__init__)


def test_entitydsl::property_constructor_args():
    sig = inspect.signature(entityDsl::Property.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_entitydsl::property_has_many():
    assert hasattr(entityDsl::Property, "many")
    descriptor = None
    for klass in entityDsl::Property.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_entitydsl::property_has_name():
    assert hasattr(entityDsl::Property, "name")
    descriptor = None
    for klass in entityDsl::Property.__mro__:
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



def test_entitydsl::entity_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Entity)


def test_entitydsl::entity_constructor_exists():
    assert callable(entityDsl::Entity.__init__)


def test_entitydsl::entity_constructor_args():
    sig = inspect.signature(entityDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::simpletype_is_not_abstract():
    assert not inspect.isabstract(entityDsl::SimpleType)


def test_entitydsl::simpletype_constructor_exists():
    assert callable(entityDsl::SimpleType.__init__)


def test_entitydsl::simpletype_constructor_args():
    sig = inspect.signature(entityDsl::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::type_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Type)


def test_entitydsl::type_constructor_exists():
    assert callable(entityDsl::Type.__init__)


def test_entitydsl::type_constructor_args():
    sig = inspect.signature(entityDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitydsl::type_has_name():
    assert hasattr(entityDsl::Type, "name")
    descriptor = None
    for klass in entityDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitydsl::model_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Model)


def test_entitydsl::model_constructor_exists():
    assert callable(entityDsl::Model.__init__)


def test_entitydsl::model_constructor_args():
    sig = inspect.signature(entityDsl::Model.__init__)
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
entityDsl::Property_strategy = st.builds(
    entityDsl::Property,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
entityDsl::Entity_strategy = st.builds(
    entityDsl::Entity,
)
entityDsl::SimpleType_strategy = st.builds(
    entityDsl::SimpleType,
)
entityDsl::Type_strategy = st.builds(
    entityDsl::Type,
    name=
        safe_text
)
entityDsl::Model_strategy = st.builds(
    entityDsl::Model,
)

@given(instance=entityDsl::Property_strategy)
@settings(max_examples=50)
def test_entitydsl::property_instantiation(instance):
    assert isinstance(instance, entityDsl::Property)

@given(instance=entityDsl::Property_strategy)
def test_entitydsl::property_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=entityDsl::Property_strategy)
def test_entitydsl::property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entityDsl::Property_strategy)
def test_entitydsl::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entityDsl::Property_strategy)
def test_entitydsl::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entityDsl::Entity_strategy)
@settings(max_examples=50)
def test_entitydsl::entity_instantiation(instance):
    assert isinstance(instance, entityDsl::Entity)

@given(instance=entityDsl::SimpleType_strategy)
@settings(max_examples=50)
def test_entitydsl::simpletype_instantiation(instance):
    assert isinstance(instance, entityDsl::SimpleType)

@given(instance=entityDsl::Type_strategy)
@settings(max_examples=50)
def test_entitydsl::type_instantiation(instance):
    assert isinstance(instance, entityDsl::Type)

@given(instance=entityDsl::Type_strategy)
def test_entitydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entityDsl::Type_strategy)
def test_entitydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entityDsl::Model_strategy)
@settings(max_examples=50)
def test_entitydsl::model_instantiation(instance):
    assert isinstance(instance, entityDsl::Model)
