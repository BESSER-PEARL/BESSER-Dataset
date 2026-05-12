import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entity_Attribute,
    entity_JAVAID,
    Type,
    entity_Entity,
    entity_TypeDef,
    entity_Type,
    entity_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_attribute_is_not_abstract():
    assert not inspect.isabstract(entity_Attribute)


def test_entity_attribute_constructor_exists():
    assert callable(entity_Attribute.__init__)


def test_entity_attribute_constructor_args():
    sig = inspect.signature(entity_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_entity_attribute_has_name():
    assert hasattr(entity_Attribute, "name")
    descriptor = None
    for klass in entity_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_entity_attribute_has_many():
    assert hasattr(entity_Attribute, "many")
    descriptor = None
    for klass in entity_Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_entity_javaid_is_not_abstract():
    assert not inspect.isabstract(entity_JAVAID)


def test_entity_javaid_constructor_exists():
    assert callable(entity_JAVAID.__init__)


def test_entity_javaid_constructor_args():
    sig = inspect.signature(entity_JAVAID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_javaid_has_name():
    assert hasattr(entity_JAVAID, "name")
    descriptor = None
    for klass in entity_JAVAID.__mro__:
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



def test_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
    params = list(sig.parameters.keys())



def test_entity_typedef_is_not_abstract():
    assert not inspect.isabstract(entity_TypeDef)


def test_entity_typedef_constructor_exists():
    assert callable(entity_TypeDef.__init__)


def test_entity_typedef_constructor_args():
    sig = inspect.signature(entity_TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_entity_type_is_not_abstract():
    assert not inspect.isabstract(entity_Type)


def test_entity_type_constructor_exists():
    assert callable(entity_Type.__init__)


def test_entity_type_constructor_args():
    sig = inspect.signature(entity_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_type_has_name():
    assert hasattr(entity_Type, "name")
    descriptor = None
    for klass in entity_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_model_is_not_abstract():
    assert not inspect.isabstract(entity_Model)


def test_entity_model_constructor_exists():
    assert callable(entity_Model.__init__)


def test_entity_model_constructor_args():
    sig = inspect.signature(entity_Model.__init__)
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
entity_Attribute_strategy = st.builds(
    entity_Attribute,
    name=
        safe_text,
    many=
        st.booleans()
)
entity_JAVAID_strategy = st.builds(
    entity_JAVAID,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)
entity_TypeDef_strategy = st.builds(
    entity_TypeDef,
)
entity_Type_strategy = st.builds(
    entity_Type,
    name=
        safe_text
)
entity_Model_strategy = st.builds(
    entity_Model,
)

@given(instance=entity_Attribute_strategy)
@settings(max_examples=50)
def test_entity_attribute_instantiation(instance):
    assert isinstance(instance, entity_Attribute)



@given(instance=entity_Attribute_strategy)
def test_entity_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=entity_Attribute_strategy)
def test_entity_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entity_JAVAID_strategy)
@settings(max_examples=50)
def test_entity_javaid_instantiation(instance):
    assert isinstance(instance, entity_JAVAID)



@given(instance=entity_JAVAID_strategy)
def test_entity_javaid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity_Entity_strategy)
@settings(max_examples=50)
def test_entity_entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)

@given(instance=entity_TypeDef_strategy)
@settings(max_examples=50)
def test_entity_typedef_instantiation(instance):
    assert isinstance(instance, entity_TypeDef)

@given(instance=entity_Type_strategy)
@settings(max_examples=50)
def test_entity_type_instantiation(instance):
    assert isinstance(instance, entity_Type)



@given(instance=entity_Type_strategy)
def test_entity_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity_Model_strategy)
@settings(max_examples=50)
def test_entity_model_instantiation(instance):
    assert isinstance(instance, entity_Model)
