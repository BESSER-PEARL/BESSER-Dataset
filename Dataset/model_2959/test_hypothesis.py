import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entities::Attribute,
    entities::Entity,
    entities::Model,
    ElementType,
    entities::EntityType,
    entities::BasicType,
    entities::ElementType,
    entities::AttributeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entities::attribute_is_not_abstract():
    assert not inspect.isabstract(entities::Attribute)


def test_entities::attribute_constructor_exists():
    assert callable(entities::Attribute.__init__)


def test_entities::attribute_constructor_args():
    sig = inspect.signature(entities::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities::attribute_has_name():
    assert hasattr(entities::Attribute, "name")
    descriptor = None
    for klass in entities::Attribute.__mro__:
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



def test_entities::model_is_not_abstract():
    assert not inspect.isabstract(entities::Model)


def test_entities::model_constructor_exists():
    assert callable(entities::Model.__init__)


def test_entities::model_constructor_args():
    sig = inspect.signature(entities::Model.__init__)
    params = list(sig.parameters.keys())



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_entities::entitytype_is_not_abstract():
    assert not inspect.isabstract(entities::EntityType)


def test_entities::entitytype_constructor_exists():
    assert callable(entities::EntityType.__init__)


def test_entities::entitytype_constructor_args():
    sig = inspect.signature(entities::EntityType.__init__)
    params = list(sig.parameters.keys())



def test_entities::basictype_is_not_abstract():
    assert not inspect.isabstract(entities::BasicType)


def test_entities::basictype_constructor_exists():
    assert callable(entities::BasicType.__init__)


def test_entities::basictype_constructor_args():
    sig = inspect.signature(entities::BasicType.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_entities::basictype_has_typeName():
    assert hasattr(entities::BasicType, "typeName")
    descriptor = None
    for klass in entities::BasicType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_entities::elementtype_is_not_abstract():
    assert not inspect.isabstract(entities::ElementType)


def test_entities::elementtype_constructor_exists():
    assert callable(entities::ElementType.__init__)


def test_entities::elementtype_constructor_args():
    sig = inspect.signature(entities::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_entities::attributetype_is_not_abstract():
    assert not inspect.isabstract(entities::AttributeType)


def test_entities::attributetype_constructor_exists():
    assert callable(entities::AttributeType.__init__)


def test_entities::attributetype_constructor_args():
    sig = inspect.signature(entities::AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "array" in params, "Missing parameter 'array'"

def test_entities::attributetype_has_length():
    assert hasattr(entities::AttributeType, "length")
    descriptor = None
    for klass in entities::AttributeType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_entities::attributetype_has_array():
    assert hasattr(entities::AttributeType, "array")
    descriptor = None
    for klass in entities::AttributeType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
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
entities::Attribute_strategy = st.builds(
    entities::Attribute,
    name=
        safe_text
)
entities::Entity_strategy = st.builds(
    entities::Entity,
    name=
        safe_text
)
entities::Model_strategy = st.builds(
    entities::Model,
)
ElementType_strategy = st.builds(
    ElementType,
)
entities::EntityType_strategy = st.builds(
    entities::EntityType,
)
entities::BasicType_strategy = st.builds(
    entities::BasicType,
    typeName=
        safe_text
)
entities::ElementType_strategy = st.builds(
    entities::ElementType,
)
entities::AttributeType_strategy = st.builds(
    entities::AttributeType,
    length=
        st.integers(),
    array=
        st.booleans()
)

@given(instance=entities::Attribute_strategy)
@settings(max_examples=50)
def test_entities::attribute_instantiation(instance):
    assert isinstance(instance, entities::Attribute)

@given(instance=entities::Attribute_strategy)
def test_entities::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Attribute_strategy)
def test_entities::attribute_name_setter(instance):
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

@given(instance=entities::Model_strategy)
@settings(max_examples=50)
def test_entities::model_instantiation(instance):
    assert isinstance(instance, entities::Model)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=entities::EntityType_strategy)
@settings(max_examples=50)
def test_entities::entitytype_instantiation(instance):
    assert isinstance(instance, entities::EntityType)

@given(instance=entities::BasicType_strategy)
@settings(max_examples=50)
def test_entities::basictype_instantiation(instance):
    assert isinstance(instance, entities::BasicType)

@given(instance=entities::BasicType_strategy)
def test_entities::basictype_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=entities::BasicType_strategy)
def test_entities::basictype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=entities::ElementType_strategy)
@settings(max_examples=50)
def test_entities::elementtype_instantiation(instance):
    assert isinstance(instance, entities::ElementType)

@given(instance=entities::AttributeType_strategy)
@settings(max_examples=50)
def test_entities::attributetype_instantiation(instance):
    assert isinstance(instance, entities::AttributeType)

@given(instance=entities::AttributeType_strategy)
def test_entities::attributetype_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=entities::AttributeType_strategy)
def test_entities::attributetype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=entities::AttributeType_strategy)
def test_entities::attributetype_array_type(instance):
    assert isinstance(instance.array, bool)


@given(instance=entities::AttributeType_strategy)
def test_entities::attributetype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original
