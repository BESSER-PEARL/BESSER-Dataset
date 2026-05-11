import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entity::Attribute,
    entity::JAVAID,
    Type,
    entity::Entity,
    entity::TypeDef,
    entity::Type,
    entity::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity::attribute_is_not_abstract():
    assert not inspect.isabstract(entity::Attribute)


def test_entity::attribute_constructor_exists():
    assert callable(entity::Attribute.__init__)


def test_entity::attribute_constructor_args():
    sig = inspect.signature(entity::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_entity::attribute_has_many():
    assert hasattr(entity::Attribute, "many")
    descriptor = None
    for klass in entity::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_entity::attribute_has_name():
    assert hasattr(entity::Attribute, "name")
    descriptor = None
    for klass in entity::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::javaid_is_not_abstract():
    assert not inspect.isabstract(entity::JAVAID)


def test_entity::javaid_constructor_exists():
    assert callable(entity::JAVAID.__init__)


def test_entity::javaid_constructor_args():
    sig = inspect.signature(entity::JAVAID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::javaid_has_name():
    assert hasattr(entity::JAVAID, "name")
    descriptor = None
    for klass in entity::JAVAID.__mro__:
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



def test_entity::entity_is_not_abstract():
    assert not inspect.isabstract(entity::Entity)


def test_entity::entity_constructor_exists():
    assert callable(entity::Entity.__init__)


def test_entity::entity_constructor_args():
    sig = inspect.signature(entity::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entity::typedef_is_not_abstract():
    assert not inspect.isabstract(entity::TypeDef)


def test_entity::typedef_constructor_exists():
    assert callable(entity::TypeDef.__init__)


def test_entity::typedef_constructor_args():
    sig = inspect.signature(entity::TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_entity::type_is_not_abstract():
    assert not inspect.isabstract(entity::Type)


def test_entity::type_constructor_exists():
    assert callable(entity::Type.__init__)


def test_entity::type_constructor_args():
    sig = inspect.signature(entity::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::type_has_name():
    assert hasattr(entity::Type, "name")
    descriptor = None
    for klass in entity::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::model_is_not_abstract():
    assert not inspect.isabstract(entity::Model)


def test_entity::model_constructor_exists():
    assert callable(entity::Model.__init__)


def test_entity::model_constructor_args():
    sig = inspect.signature(entity::Model.__init__)
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
entity::Attribute_strategy = st.builds(
    entity::Attribute,
    many=
        st.booleans(),
    name=
        safe_text
)
entity::JAVAID_strategy = st.builds(
    entity::JAVAID,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
entity::Entity_strategy = st.builds(
    entity::Entity,
)
entity::TypeDef_strategy = st.builds(
    entity::TypeDef,
)
entity::Type_strategy = st.builds(
    entity::Type,
    name=
        safe_text
)
entity::Model_strategy = st.builds(
    entity::Model,
)

@given(instance=entity::Attribute_strategy)
@settings(max_examples=50)
def test_entity::attribute_instantiation(instance):
    assert isinstance(instance, entity::Attribute)

@given(instance=entity::Attribute_strategy)
def test_entity::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=entity::Attribute_strategy)
def test_entity::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entity::Attribute_strategy)
def test_entity::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Attribute_strategy)
def test_entity::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity::JAVAID_strategy)
@settings(max_examples=50)
def test_entity::javaid_instantiation(instance):
    assert isinstance(instance, entity::JAVAID)

@given(instance=entity::JAVAID_strategy)
def test_entity::javaid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::JAVAID_strategy)
def test_entity::javaid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity::Entity_strategy)
@settings(max_examples=50)
def test_entity::entity_instantiation(instance):
    assert isinstance(instance, entity::Entity)

@given(instance=entity::TypeDef_strategy)
@settings(max_examples=50)
def test_entity::typedef_instantiation(instance):
    assert isinstance(instance, entity::TypeDef)

@given(instance=entity::Type_strategy)
@settings(max_examples=50)
def test_entity::type_instantiation(instance):
    assert isinstance(instance, entity::Type)

@given(instance=entity::Type_strategy)
def test_entity::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Type_strategy)
def test_entity::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity::Model_strategy)
@settings(max_examples=50)
def test_entity::model_instantiation(instance):
    assert isinstance(instance, entity::Model)
