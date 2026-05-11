import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Model,
    Type,
    Data::PrimitiveType,
    Data::Entity,
    Data::Attribute,
    Data::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_data::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Data::PrimitiveType)


def test_data::primitivetype_constructor_exists():
    assert callable(Data::PrimitiveType.__init__)


def test_data::primitivetype_constructor_args():
    sig = inspect.signature(Data::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_data::entity_is_not_abstract():
    assert not inspect.isabstract(Data::Entity)


def test_data::entity_constructor_exists():
    assert callable(Data::Entity.__init__)


def test_data::entity_constructor_args():
    sig = inspect.signature(Data::Entity.__init__)
    params = list(sig.parameters.keys())



def test_data::attribute_is_not_abstract():
    assert not inspect.isabstract(Data::Attribute)


def test_data::attribute_constructor_exists():
    assert callable(Data::Attribute.__init__)


def test_data::attribute_constructor_args():
    sig = inspect.signature(Data::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data::attribute_has_name():
    assert hasattr(Data::Attribute, "name")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data::type_is_not_abstract():
    assert not inspect.isabstract(Data::Type)


def test_data::type_constructor_exists():
    assert callable(Data::Type.__init__)


def test_data::type_constructor_args():
    sig = inspect.signature(Data::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data::type_has_name():
    assert hasattr(Data::Type, "name")
    descriptor = None
    for klass in Data::Type.__mro__:
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
Data::Model_strategy = st.builds(
    Data::Model,
)
Type_strategy = st.builds(
    Type,
)
Data::PrimitiveType_strategy = st.builds(
    Data::PrimitiveType,
)
Data::Entity_strategy = st.builds(
    Data::Entity,
)
Data::Attribute_strategy = st.builds(
    Data::Attribute,
    name=
        safe_text
)
Data::Type_strategy = st.builds(
    Data::Type,
    name=
        safe_text
)

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Data::PrimitiveType_strategy)
@settings(max_examples=50)
def test_data::primitivetype_instantiation(instance):
    assert isinstance(instance, Data::PrimitiveType)

@given(instance=Data::Entity_strategy)
@settings(max_examples=50)
def test_data::entity_instantiation(instance):
    assert isinstance(instance, Data::Entity)

@given(instance=Data::Attribute_strategy)
@settings(max_examples=50)
def test_data::attribute_instantiation(instance):
    assert isinstance(instance, Data::Attribute)

@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Type_strategy)
@settings(max_examples=50)
def test_data::type_instantiation(instance):
    assert isinstance(instance, Data::Type)

@given(instance=Data::Type_strategy)
def test_data::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Type_strategy)
def test_data::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
