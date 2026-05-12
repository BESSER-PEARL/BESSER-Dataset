import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entities_Model,
    Property,
    entities_ReferenceProperty,
    entities_SimpleProperty,
    entities_Property,
    entities_Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entities_model_is_not_abstract():
    assert not inspect.isabstract(entities_Model)


def test_entities_model_constructor_exists():
    assert callable(entities_Model.__init__)


def test_entities_model_constructor_args():
    sig = inspect.signature(entities_Model.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_entities_referenceproperty_is_not_abstract():
    assert not inspect.isabstract(entities_ReferenceProperty)


def test_entities_referenceproperty_constructor_exists():
    assert callable(entities_ReferenceProperty.__init__)


def test_entities_referenceproperty_constructor_args():
    sig = inspect.signature(entities_ReferenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_entities_referenceproperty_has_many():
    assert hasattr(entities_ReferenceProperty, "many")
    descriptor = None
    for klass in entities_ReferenceProperty.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_entities_simpleproperty_is_not_abstract():
    assert not inspect.isabstract(entities_SimpleProperty)


def test_entities_simpleproperty_constructor_exists():
    assert callable(entities_SimpleProperty.__init__)


def test_entities_simpleproperty_constructor_args():
    sig = inspect.signature(entities_SimpleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_entities_simpleproperty_has_type():
    assert hasattr(entities_SimpleProperty, "type")
    descriptor = None
    for klass in entities_SimpleProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_entities_property_is_not_abstract():
    assert not inspect.isabstract(entities_Property)


def test_entities_property_constructor_exists():
    assert callable(entities_Property.__init__)


def test_entities_property_constructor_args():
    sig = inspect.signature(entities_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities_property_has_name():
    assert hasattr(entities_Property, "name")
    descriptor = None
    for klass in entities_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entities_entity_is_not_abstract():
    assert not inspect.isabstract(entities_Entity)


def test_entities_entity_constructor_exists():
    assert callable(entities_Entity.__init__)


def test_entities_entity_constructor_args():
    sig = inspect.signature(entities_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities_entity_has_name():
    assert hasattr(entities_Entity, "name")
    descriptor = None
    for klass in entities_Entity.__mro__:
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
entities_Model_strategy = st.builds(
    entities_Model,
)
Property_strategy = st.builds(
    Property,
)
entities_ReferenceProperty_strategy = st.builds(
    entities_ReferenceProperty,
    many=
        st.booleans()
)
entities_SimpleProperty_strategy = st.builds(
    entities_SimpleProperty,
    type=
        safe_text
)
entities_Property_strategy = st.builds(
    entities_Property,
    name=
        safe_text
)
entities_Entity_strategy = st.builds(
    entities_Entity,
    name=
        safe_text
)

@given(instance=entities_Model_strategy)
@settings(max_examples=50)
def test_entities_model_instantiation(instance):
    assert isinstance(instance, entities_Model)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=entities_ReferenceProperty_strategy)
@settings(max_examples=50)
def test_entities_referenceproperty_instantiation(instance):
    assert isinstance(instance, entities_ReferenceProperty)



@given(instance=entities_ReferenceProperty_strategy)
def test_entities_referenceproperty_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entities_SimpleProperty_strategy)
@settings(max_examples=50)
def test_entities_simpleproperty_instantiation(instance):
    assert isinstance(instance, entities_SimpleProperty)



@given(instance=entities_SimpleProperty_strategy)
def test_entities_simpleproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=entities_Property_strategy)
@settings(max_examples=50)
def test_entities_property_instantiation(instance):
    assert isinstance(instance, entities_Property)



@given(instance=entities_Property_strategy)
def test_entities_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entities_Entity_strategy)
@settings(max_examples=50)
def test_entities_entity_instantiation(instance):
    assert isinstance(instance, entities_Entity)



@given(instance=entities_Entity_strategy)
def test_entities_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
