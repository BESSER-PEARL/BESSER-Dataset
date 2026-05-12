import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entityDsl_Property,
    Type,
    entityDsl_Entity,
    entityDsl_SimpleType,
    entityDsl_Type,
    entityDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entitydsl_property_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Property)


def test_entitydsl_property_constructor_exists():
    assert callable(entityDsl_Property.__init__)


def test_entitydsl_property_constructor_args():
    sig = inspect.signature(entityDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_entitydsl_property_has_name():
    assert hasattr(entityDsl_Property, "name")
    descriptor = None
    for klass in entityDsl_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_entitydsl_property_has_many():
    assert hasattr(entityDsl_Property, "many")
    descriptor = None
    for klass in entityDsl_Property.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_entity_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Entity)


def test_entitydsl_entity_constructor_exists():
    assert callable(entityDsl_Entity.__init__)


def test_entitydsl_entity_constructor_args():
    sig = inspect.signature(entityDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_simpletype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_SimpleType)


def test_entitydsl_simpletype_constructor_exists():
    assert callable(entityDsl_SimpleType.__init__)


def test_entitydsl_simpletype_constructor_args():
    sig = inspect.signature(entityDsl_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_type_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Type)


def test_entitydsl_type_constructor_exists():
    assert callable(entityDsl_Type.__init__)


def test_entitydsl_type_constructor_args():
    sig = inspect.signature(entityDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitydsl_type_has_name():
    assert hasattr(entityDsl_Type, "name")
    descriptor = None
    for klass in entityDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitydsl_model_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Model)


def test_entitydsl_model_constructor_exists():
    assert callable(entityDsl_Model.__init__)


def test_entitydsl_model_constructor_args():
    sig = inspect.signature(entityDsl_Model.__init__)
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
entityDsl_Property_strategy = st.builds(
    entityDsl_Property,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
entityDsl_Entity_strategy = st.builds(
    entityDsl_Entity,
)
entityDsl_SimpleType_strategy = st.builds(
    entityDsl_SimpleType,
)
entityDsl_Type_strategy = st.builds(
    entityDsl_Type,
    name=
        safe_text
)
entityDsl_Model_strategy = st.builds(
    entityDsl_Model,
)

@given(instance=entityDsl_Property_strategy)
@settings(max_examples=50)
def test_entitydsl_property_instantiation(instance):
    assert isinstance(instance, entityDsl_Property)



@given(instance=entityDsl_Property_strategy)
def test_entitydsl_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=entityDsl_Property_strategy)
def test_entitydsl_property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entityDsl_Entity_strategy)
@settings(max_examples=50)
def test_entitydsl_entity_instantiation(instance):
    assert isinstance(instance, entityDsl_Entity)

@given(instance=entityDsl_SimpleType_strategy)
@settings(max_examples=50)
def test_entitydsl_simpletype_instantiation(instance):
    assert isinstance(instance, entityDsl_SimpleType)

@given(instance=entityDsl_Type_strategy)
@settings(max_examples=50)
def test_entitydsl_type_instantiation(instance):
    assert isinstance(instance, entityDsl_Type)



@given(instance=entityDsl_Type_strategy)
def test_entitydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entityDsl_Model_strategy)
@settings(max_examples=50)
def test_entitydsl_model_instantiation(instance):
    assert isinstance(instance, entityDsl_Model)
