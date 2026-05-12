import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    entitymm_PrimitiveType,
    entitymm_Entity,
    entitymm_Attribute,
    entitymm_Type,
    entitymm_Model,
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



def test_entitymm_primitivetype_is_not_abstract():
    assert not inspect.isabstract(entitymm_PrimitiveType)


def test_entitymm_primitivetype_constructor_exists():
    assert callable(entitymm_PrimitiveType.__init__)


def test_entitymm_primitivetype_constructor_args():
    sig = inspect.signature(entitymm_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_entitymm_entity_is_not_abstract():
    assert not inspect.isabstract(entitymm_Entity)


def test_entitymm_entity_constructor_exists():
    assert callable(entitymm_Entity.__init__)


def test_entitymm_entity_constructor_args():
    sig = inspect.signature(entitymm_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "size" in params, "Missing parameter 'size'"
    assert "isPersistent" in params, "Missing parameter 'isPersistent'"

def test_entitymm_entity_has_desc():
    assert hasattr(entitymm_Entity, "desc")
    descriptor = None
    for klass in entitymm_Entity.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_entitymm_entity_has_size():
    assert hasattr(entitymm_Entity, "size")
    descriptor = None
    for klass in entitymm_Entity.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_entitymm_entity_has_isPersistent():
    assert hasattr(entitymm_Entity, "isPersistent")
    descriptor = None
    for klass in entitymm_Entity.__mro__:
        if "isPersistent" in klass.__dict__:
            descriptor = klass.__dict__["isPersistent"]
            break
    assert isinstance(descriptor, property)



def test_entitymm_attribute_is_not_abstract():
    assert not inspect.isabstract(entitymm_Attribute)


def test_entitymm_attribute_constructor_exists():
    assert callable(entitymm_Attribute.__init__)


def test_entitymm_attribute_constructor_args():
    sig = inspect.signature(entitymm_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm_attribute_has_name():
    assert hasattr(entitymm_Attribute, "name")
    descriptor = None
    for klass in entitymm_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitymm_type_is_not_abstract():
    assert not inspect.isabstract(entitymm_Type)


def test_entitymm_type_constructor_exists():
    assert callable(entitymm_Type.__init__)


def test_entitymm_type_constructor_args():
    sig = inspect.signature(entitymm_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm_type_has_name():
    assert hasattr(entitymm_Type, "name")
    descriptor = None
    for klass in entitymm_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitymm_model_is_not_abstract():
    assert not inspect.isabstract(entitymm_Model)


def test_entitymm_model_constructor_exists():
    assert callable(entitymm_Model.__init__)


def test_entitymm_model_constructor_args():
    sig = inspect.signature(entitymm_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitymm_model_has_name():
    assert hasattr(entitymm_Model, "name")
    descriptor = None
    for klass in entitymm_Model.__mro__:
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
entitymm_PrimitiveType_strategy = st.builds(
    entitymm_PrimitiveType,
)
entitymm_Entity_strategy = st.builds(
    entitymm_Entity,
    desc=
        safe_text,
    size=
        st.integers(),
    isPersistent=
        st.booleans()
)
entitymm_Attribute_strategy = st.builds(
    entitymm_Attribute,
    name=
        safe_text
)
entitymm_Type_strategy = st.builds(
    entitymm_Type,
    name=
        safe_text
)
entitymm_Model_strategy = st.builds(
    entitymm_Model,
    name=
        safe_text
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entitymm_PrimitiveType_strategy)
@settings(max_examples=50)
def test_entitymm_primitivetype_instantiation(instance):
    assert isinstance(instance, entitymm_PrimitiveType)

@given(instance=entitymm_Entity_strategy)
@settings(max_examples=50)
def test_entitymm_entity_instantiation(instance):
    assert isinstance(instance, entitymm_Entity)



@given(instance=entitymm_Entity_strategy)
def test_entitymm_entity_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=entitymm_Entity_strategy)
def test_entitymm_entity_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=entitymm_Entity_strategy)
def test_entitymm_entity_isPersistent_setter(instance):
    original = instance.isPersistent
    instance.isPersistent = original
    assert instance.isPersistent == original

@given(instance=entitymm_Attribute_strategy)
@settings(max_examples=50)
def test_entitymm_attribute_instantiation(instance):
    assert isinstance(instance, entitymm_Attribute)



@given(instance=entitymm_Attribute_strategy)
def test_entitymm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitymm_Type_strategy)
@settings(max_examples=50)
def test_entitymm_type_instantiation(instance):
    assert isinstance(instance, entitymm_Type)



@given(instance=entitymm_Type_strategy)
def test_entitymm_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entitymm_Model_strategy)
@settings(max_examples=50)
def test_entitymm_model_instantiation(instance):
    assert isinstance(instance, entitymm_Model)



@given(instance=entitymm_Model_strategy)
def test_entitymm_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
