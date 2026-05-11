import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entities::Model,
    Property,
    entities::ReferenceProperty,
    entities::SimpleProperty,
    entities::Property,
    entities::Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entities::model_is_not_abstract():
    assert not inspect.isabstract(entities::Model)


def test_entities::model_constructor_exists():
    assert callable(entities::Model.__init__)


def test_entities::model_constructor_args():
    sig = inspect.signature(entities::Model.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_entities::referenceproperty_is_not_abstract():
    assert not inspect.isabstract(entities::ReferenceProperty)


def test_entities::referenceproperty_constructor_exists():
    assert callable(entities::ReferenceProperty.__init__)


def test_entities::referenceproperty_constructor_args():
    sig = inspect.signature(entities::ReferenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_entities::referenceproperty_has_many():
    assert hasattr(entities::ReferenceProperty, "many")
    descriptor = None
    for klass in entities::ReferenceProperty.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_entities::simpleproperty_is_not_abstract():
    assert not inspect.isabstract(entities::SimpleProperty)


def test_entities::simpleproperty_constructor_exists():
    assert callable(entities::SimpleProperty.__init__)


def test_entities::simpleproperty_constructor_args():
    sig = inspect.signature(entities::SimpleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_entities::simpleproperty_has_type():
    assert hasattr(entities::SimpleProperty, "type")
    descriptor = None
    for klass in entities::SimpleProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_entities::property_is_not_abstract():
    assert not inspect.isabstract(entities::Property)


def test_entities::property_constructor_exists():
    assert callable(entities::Property.__init__)


def test_entities::property_constructor_args():
    sig = inspect.signature(entities::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities::property_has_name():
    assert hasattr(entities::Property, "name")
    descriptor = None
    for klass in entities::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entities::entity_is_not_abstract():
    assert not inspect.isabstract(entities::Entity)


def test_entities::entity_constructor_exists():
    assert callable(entities::Entity.__init__)


def test_entities::entity_constructor_args():
    sig = inspect.signature(entities::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities::entity_has_name():
    assert hasattr(entities::Entity, "name")
    descriptor = None
    for klass in entities::Entity.__mro__:
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
entities::Model_strategy = st.builds(
    entities::Model,
)
Property_strategy = st.builds(
    Property,
)
entities::ReferenceProperty_strategy = st.builds(
    entities::ReferenceProperty,
    many=
        st.booleans()
)
entities::SimpleProperty_strategy = st.builds(
    entities::SimpleProperty,
    type=
        safe_text
)
entities::Property_strategy = st.builds(
    entities::Property,
    name=
        safe_text
)
entities::Entity_strategy = st.builds(
    entities::Entity,
    name=
        safe_text
)

@given(instance=entities::Model_strategy)
@settings(max_examples=50)
def test_entities::model_instantiation(instance):
    assert isinstance(instance, entities::Model)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=entities::ReferenceProperty_strategy)
@settings(max_examples=50)
def test_entities::referenceproperty_instantiation(instance):
    assert isinstance(instance, entities::ReferenceProperty)

@given(instance=entities::ReferenceProperty_strategy)
def test_entities::referenceproperty_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=entities::ReferenceProperty_strategy)
def test_entities::referenceproperty_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entities::SimpleProperty_strategy)
@settings(max_examples=50)
def test_entities::simpleproperty_instantiation(instance):
    assert isinstance(instance, entities::SimpleProperty)

@given(instance=entities::SimpleProperty_strategy)
def test_entities::simpleproperty_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=entities::SimpleProperty_strategy)
def test_entities::simpleproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=entities::Property_strategy)
@settings(max_examples=50)
def test_entities::property_instantiation(instance):
    assert isinstance(instance, entities::Property)

@given(instance=entities::Property_strategy)
def test_entities::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Property_strategy)
def test_entities::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entities::Entity_strategy)
@settings(max_examples=50)
def test_entities::entity_instantiation(instance):
    assert isinstance(instance, entities::Entity)

@given(instance=entities::Entity_strategy)
def test_entities::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Entity_strategy)
def test_entities::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
