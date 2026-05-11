import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Property,
    entities::Reference,
    entities::SimpleProperty,
    entities::Property,
    Type,
    entities::Entity,
    entities::SimpleType,
    entities::Type,
    entities::Import,
    entities::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_entities::reference_is_not_abstract():
    assert not inspect.isabstract(entities::Reference)


def test_entities::reference_constructor_exists():
    assert callable(entities::Reference.__init__)


def test_entities::reference_constructor_args():
    sig = inspect.signature(entities::Reference.__init__)
    params = list(sig.parameters.keys())



def test_entities::simpleproperty_is_not_abstract():
    assert not inspect.isabstract(entities::SimpleProperty)


def test_entities::simpleproperty_constructor_exists():
    assert callable(entities::SimpleProperty.__init__)


def test_entities::simpleproperty_constructor_args():
    sig = inspect.signature(entities::SimpleProperty.__init__)
    params = list(sig.parameters.keys())



def test_entities::property_is_not_abstract():
    assert not inspect.isabstract(entities::Property)


def test_entities::property_constructor_exists():
    assert callable(entities::Property.__init__)


def test_entities::property_constructor_args():
    sig = inspect.signature(entities::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_entities::property_has_name():
    assert hasattr(entities::Property, "name")
    descriptor = None
    for klass in entities::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_entities::property_has_many():
    assert hasattr(entities::Property, "many")
    descriptor = None
    for klass in entities::Property.__mro__:
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



def test_entities::entity_is_not_abstract():
    assert not inspect.isabstract(entities::Entity)


def test_entities::entity_constructor_exists():
    assert callable(entities::Entity.__init__)


def test_entities::entity_constructor_args():
    sig = inspect.signature(entities::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entities::simpletype_is_not_abstract():
    assert not inspect.isabstract(entities::SimpleType)


def test_entities::simpletype_constructor_exists():
    assert callable(entities::SimpleType.__init__)


def test_entities::simpletype_constructor_args():
    sig = inspect.signature(entities::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_entities::type_is_not_abstract():
    assert not inspect.isabstract(entities::Type)


def test_entities::type_constructor_exists():
    assert callable(entities::Type.__init__)


def test_entities::type_constructor_args():
    sig = inspect.signature(entities::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities::type_has_name():
    assert hasattr(entities::Type, "name")
    descriptor = None
    for klass in entities::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entities::import_is_not_abstract():
    assert not inspect.isabstract(entities::Import)


def test_entities::import_constructor_exists():
    assert callable(entities::Import.__init__)


def test_entities::import_constructor_args():
    sig = inspect.signature(entities::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_entities::import_has_importURI():
    assert hasattr(entities::Import, "importURI")
    descriptor = None
    for klass in entities::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_entities::model_is_not_abstract():
    assert not inspect.isabstract(entities::Model)


def test_entities::model_constructor_exists():
    assert callable(entities::Model.__init__)


def test_entities::model_constructor_args():
    sig = inspect.signature(entities::Model.__init__)
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
Property_strategy = st.builds(
    Property,
)
entities::Reference_strategy = st.builds(
    entities::Reference,
)
entities::SimpleProperty_strategy = st.builds(
    entities::SimpleProperty,
)
entities::Property_strategy = st.builds(
    entities::Property,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
entities::Entity_strategy = st.builds(
    entities::Entity,
)
entities::SimpleType_strategy = st.builds(
    entities::SimpleType,
)
entities::Type_strategy = st.builds(
    entities::Type,
    name=
        safe_text
)
entities::Import_strategy = st.builds(
    entities::Import,
    importURI=
        safe_text
)
entities::Model_strategy = st.builds(
    entities::Model,
)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=entities::Reference_strategy)
@settings(max_examples=50)
def test_entities::reference_instantiation(instance):
    assert isinstance(instance, entities::Reference)

@given(instance=entities::SimpleProperty_strategy)
@settings(max_examples=50)
def test_entities::simpleproperty_instantiation(instance):
    assert isinstance(instance, entities::SimpleProperty)

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

@given(instance=entities::Property_strategy)
def test_entities::property_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=entities::Property_strategy)
def test_entities::property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entities::Entity_strategy)
@settings(max_examples=50)
def test_entities::entity_instantiation(instance):
    assert isinstance(instance, entities::Entity)

@given(instance=entities::SimpleType_strategy)
@settings(max_examples=50)
def test_entities::simpletype_instantiation(instance):
    assert isinstance(instance, entities::SimpleType)

@given(instance=entities::Type_strategy)
@settings(max_examples=50)
def test_entities::type_instantiation(instance):
    assert isinstance(instance, entities::Type)

@given(instance=entities::Type_strategy)
def test_entities::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Type_strategy)
def test_entities::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entities::Import_strategy)
@settings(max_examples=50)
def test_entities::import_instantiation(instance):
    assert isinstance(instance, entities::Import)

@given(instance=entities::Import_strategy)
def test_entities::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=entities::Import_strategy)
def test_entities::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=entities::Model_strategy)
@settings(max_examples=50)
def test_entities::model_instantiation(instance):
    assert isinstance(instance, entities::Model)
