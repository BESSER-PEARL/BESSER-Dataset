import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    entitymm::PrimitiveType,
    entitymm::Entity,
    entitymm::Attribute,
    entitymm::Model,
    entitymm::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entitymm::primitivetype_is_not_abstract():
    assert not inspect.isabstract(entitymm::PrimitiveType)


def test_entitymm::primitivetype_constructor_exists():
    assert callable(entitymm::PrimitiveType.__init__)


def test_entitymm::primitivetype_constructor_args():
    sig = inspect.signature(entitymm::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_entitymm::entity_is_not_abstract():
    assert not inspect.isabstract(entitymm::Entity)


def test_entitymm::entity_constructor_exists():
    assert callable(entitymm::Entity.__init__)


def test_entitymm::entity_constructor_args():
    sig = inspect.signature(entitymm::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "isPersistent" in params, "Missing parameter 'isPersistent'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_entitymm::entity_has_size():
    assert hasattr(entitymm::Entity, "size")
    descriptor = None
    for klass in entitymm::Entity.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_entitymm::entity_has_isPersistent():
    assert hasattr(entitymm::Entity, "isPersistent")
    descriptor = None
    for klass in entitymm::Entity.__mro__:
        if "isPersistent" in klass.__dict__:
            descriptor = klass.__dict__["isPersistent"]
            break
    assert isinstance(descriptor, property)

def test_entitymm::entity_has_desc():
    assert hasattr(entitymm::Entity, "desc")
    descriptor = None
    for klass in entitymm::Entity.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_entitymm::attribute_is_not_abstract():
    assert not inspect.isabstract(entitymm::Attribute)


def test_entitymm::attribute_constructor_exists():
    assert callable(entitymm::Attribute.__init__)


def test_entitymm::attribute_constructor_args():
    sig = inspect.signature(entitymm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm::attribute_has_name():
    assert hasattr(entitymm::Attribute, "name")
    descriptor = None
    for klass in entitymm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitymm::model_is_not_abstract():
    assert not inspect.isabstract(entitymm::Model)


def test_entitymm::model_constructor_exists():
    assert callable(entitymm::Model.__init__)


def test_entitymm::model_constructor_args():
    sig = inspect.signature(entitymm::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm::model_has_name():
    assert hasattr(entitymm::Model, "name")
    descriptor = None
    for klass in entitymm::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitymm::type_is_not_abstract():
    assert not inspect.isabstract(entitymm::Type)


def test_entitymm::type_constructor_exists():
    assert callable(entitymm::Type.__init__)


def test_entitymm::type_constructor_args():
    sig = inspect.signature(entitymm::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm::type_has_name():
    assert hasattr(entitymm::Type, "name")
    descriptor = None
    for klass in entitymm::Type.__mro__:
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
Type_strategy = st.builds(
    Type,
)
entitymm::PrimitiveType_strategy = st.builds(
    entitymm::PrimitiveType,
)
entitymm::Entity_strategy = st.builds(
    entitymm::Entity,
    size=
        st.integers(),
    isPersistent=
        st.booleans(),
    desc=
        safe_text
)
entitymm::Attribute_strategy = st.builds(
    entitymm::Attribute,
    name=
        safe_text
)
entitymm::Model_strategy = st.builds(
    entitymm::Model,
    name=
        safe_text
)
entitymm::Type_strategy = st.builds(
    entitymm::Type,
    name=
        safe_text
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entitymm::PrimitiveType_strategy)
@settings(max_examples=50)
def test_entitymm::primitivetype_instantiation(instance):
    assert isinstance(instance, entitymm::PrimitiveType)

@given(instance=entitymm::Entity_strategy)
@settings(max_examples=50)
def test_entitymm::entity_instantiation(instance):
    assert isinstance(instance, entitymm::Entity)

@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_isPersistent_type(instance):
    assert isinstance(instance.isPersistent, bool)


@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_isPersistent_setter(instance):
    original = instance.isPersistent
    instance.isPersistent = original
    assert instance.isPersistent == original

@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=entitymm::Entity_strategy)
def test_entitymm::entity_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=entitymm::Attribute_strategy)
@settings(max_examples=50)
def test_entitymm::attribute_instantiation(instance):
    assert isinstance(instance, entitymm::Attribute)

@given(instance=entitymm::Attribute_strategy)
def test_entitymm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entitymm::Attribute_strategy)
def test_entitymm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitymm::Model_strategy)
@settings(max_examples=50)
def test_entitymm::model_instantiation(instance):
    assert isinstance(instance, entitymm::Model)

@given(instance=entitymm::Model_strategy)
def test_entitymm::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entitymm::Model_strategy)
def test_entitymm::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitymm::Type_strategy)
@settings(max_examples=50)
def test_entitymm::type_instantiation(instance):
    assert isinstance(instance, entitymm::Type)

@given(instance=entitymm::Type_strategy)
def test_entitymm::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entitymm::Type_strategy)
def test_entitymm::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
