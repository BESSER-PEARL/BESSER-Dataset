import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Type,
    myDsl::Import,
    myDsl::Property,
    Type,
    myDsl::Entity,
    myDsl::SimpleType,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::import_is_not_abstract():
    assert not inspect.isabstract(myDsl::Import)


def test_mydsl::import_constructor_exists():
    assert callable(myDsl::Import.__init__)


def test_mydsl::import_constructor_args():
    sig = inspect.signature(myDsl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_mydsl::import_has_importURI():
    assert hasattr(myDsl::Import, "importURI")
    descriptor = None
    for klass in myDsl::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::property_is_not_abstract():
    assert not inspect.isabstract(myDsl::Property)


def test_mydsl::property_constructor_exists():
    assert callable(myDsl::Property.__init__)


def test_mydsl::property_constructor_args():
    sig = inspect.signature(myDsl::Property.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::property_has_many():
    assert hasattr(myDsl::Property, "many")
    descriptor = None
    for klass in myDsl::Property.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::property_has_name():
    assert hasattr(myDsl::Property, "name")
    descriptor = None
    for klass in myDsl::Property.__mro__:
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



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::simpletype_is_not_abstract():
    assert not inspect.isabstract(myDsl::SimpleType)


def test_mydsl::simpletype_constructor_exists():
    assert callable(myDsl::SimpleType.__init__)


def test_mydsl::simpletype_constructor_args():
    sig = inspect.signature(myDsl::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::Import_strategy = st.builds(
    myDsl::Import,
    importURI=
        safe_text
)
myDsl::Property_strategy = st.builds(
    myDsl::Property,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
myDsl::SimpleType_strategy = st.builds(
    myDsl::SimpleType,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Import_strategy)
@settings(max_examples=50)
def test_mydsl::import_instantiation(instance):
    assert isinstance(instance, myDsl::Import)

@given(instance=myDsl::Import_strategy)
def test_mydsl::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=myDsl::Import_strategy)
def test_mydsl::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=myDsl::Property_strategy)
@settings(max_examples=50)
def test_mydsl::property_instantiation(instance):
    assert isinstance(instance, myDsl::Property)

@given(instance=myDsl::Property_strategy)
def test_mydsl::property_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Property_strategy)
def test_mydsl::property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Property_strategy)
def test_mydsl::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::SimpleType_strategy)
@settings(max_examples=50)
def test_mydsl::simpletype_instantiation(instance):
    assert isinstance(instance, myDsl::SimpleType)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
