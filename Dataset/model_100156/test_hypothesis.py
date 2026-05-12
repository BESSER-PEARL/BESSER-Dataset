import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IValue,
    mongodb::SubDocument,
    mongodb::ValueList,
    mongodb::Value,
    mongodb::IValue,
    mongodb::Document,
    mongodb::Collection,
    mongodb::Database,
    mongodb::Field,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ivalue_is_not_abstract():
    assert not inspect.isabstract(IValue)


def test_ivalue_constructor_exists():
    assert callable(IValue.__init__)


def test_ivalue_constructor_args():
    sig = inspect.signature(IValue.__init__)
    params = list(sig.parameters.keys())



def test_mongodb::subdocument_is_not_abstract():
    assert not inspect.isabstract(mongodb::SubDocument)


def test_mongodb::subdocument_constructor_exists():
    assert callable(mongodb::SubDocument.__init__)


def test_mongodb::subdocument_constructor_args():
    sig = inspect.signature(mongodb::SubDocument.__init__)
    params = list(sig.parameters.keys())



def test_mongodb::valuelist_is_not_abstract():
    assert not inspect.isabstract(mongodb::ValueList)


def test_mongodb::valuelist_constructor_exists():
    assert callable(mongodb::ValueList.__init__)


def test_mongodb::valuelist_constructor_args():
    sig = inspect.signature(mongodb::ValueList.__init__)
    params = list(sig.parameters.keys())



def test_mongodb::value_is_not_abstract():
    assert not inspect.isabstract(mongodb::Value)


def test_mongodb::value_constructor_exists():
    assert callable(mongodb::Value.__init__)


def test_mongodb::value_constructor_args():
    sig = inspect.signature(mongodb::Value.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mongodb::value_has_type():
    assert hasattr(mongodb::Value, "type")
    descriptor = None
    for klass in mongodb::Value.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mongodb::value_has_value():
    assert hasattr(mongodb::Value, "value")
    descriptor = None
    for klass in mongodb::Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mongodb::ivalue_is_not_abstract():
    assert not inspect.isabstract(mongodb::IValue)


def test_mongodb::ivalue_constructor_exists():
    assert callable(mongodb::IValue.__init__)


def test_mongodb::ivalue_constructor_args():
    sig = inspect.signature(mongodb::IValue.__init__)
    params = list(sig.parameters.keys())



def test_mongodb::document_is_not_abstract():
    assert not inspect.isabstract(mongodb::Document)


def test_mongodb::document_constructor_exists():
    assert callable(mongodb::Document.__init__)


def test_mongodb::document_constructor_args():
    sig = inspect.signature(mongodb::Document.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"

def test_mongodb::document_has__id():
    assert hasattr(mongodb::Document, "_id")
    descriptor = None
    for klass in mongodb::Document.__mro__:
        if "_id" in klass.__dict__:
            descriptor = klass.__dict__["_id"]
            break
    assert isinstance(descriptor, property)



def test_mongodb::collection_is_not_abstract():
    assert not inspect.isabstract(mongodb::Collection)


def test_mongodb::collection_constructor_exists():
    assert callable(mongodb::Collection.__init__)


def test_mongodb::collection_constructor_args():
    sig = inspect.signature(mongodb::Collection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mongodb::collection_has_name():
    assert hasattr(mongodb::Collection, "name")
    descriptor = None
    for klass in mongodb::Collection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mongodb::database_is_not_abstract():
    assert not inspect.isabstract(mongodb::Database)


def test_mongodb::database_constructor_exists():
    assert callable(mongodb::Database.__init__)


def test_mongodb::database_constructor_args():
    sig = inspect.signature(mongodb::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mongodb::database_has_name():
    assert hasattr(mongodb::Database, "name")
    descriptor = None
    for klass in mongodb::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mongodb::field_is_not_abstract():
    assert not inspect.isabstract(mongodb::Field)


def test_mongodb::field_constructor_exists():
    assert callable(mongodb::Field.__init__)


def test_mongodb::field_constructor_args():
    sig = inspect.signature(mongodb::Field.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_mongodb::field_has_key():
    assert hasattr(mongodb::Field, "key")
    descriptor = None
    for klass in mongodb::Field.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "NULL",
        "JAVASCRIPT",
        "REGEXPR",
        "DOUBLE",
        "STRING",
        "BOOLEAN",
        "DATE",
        "TIMESTAMP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
IValue_strategy = st.builds(
    IValue,
)
mongodb::SubDocument_strategy = st.builds(
    mongodb::SubDocument,
)
mongodb::ValueList_strategy = st.builds(
    mongodb::ValueList,
)
mongodb::Value_strategy = st.builds(
    mongodb::Value,
    type=
        safe_text,
    value=
        safe_text
)
mongodb::IValue_strategy = st.builds(
    mongodb::IValue,
)
mongodb::Document_strategy = st.builds(
    mongodb::Document,
    _id=
        safe_text
)
mongodb::Collection_strategy = st.builds(
    mongodb::Collection,
    name=
        safe_text
)
mongodb::Database_strategy = st.builds(
    mongodb::Database,
    name=
        safe_text
)
mongodb::Field_strategy = st.builds(
    mongodb::Field,
    key=
        safe_text
)

@given(instance=IValue_strategy)
@settings(max_examples=50)
def test_ivalue_instantiation(instance):
    assert isinstance(instance, IValue)

@given(instance=mongodb::SubDocument_strategy)
@settings(max_examples=50)
def test_mongodb::subdocument_instantiation(instance):
    assert isinstance(instance, mongodb::SubDocument)

@given(instance=mongodb::ValueList_strategy)
@settings(max_examples=50)
def test_mongodb::valuelist_instantiation(instance):
    assert isinstance(instance, mongodb::ValueList)

@given(instance=mongodb::Value_strategy)
@settings(max_examples=50)
def test_mongodb::value_instantiation(instance):
    assert isinstance(instance, mongodb::Value)

@given(instance=mongodb::Value_strategy)
def test_mongodb::value_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mongodb::Value_strategy)
def test_mongodb::value_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mongodb::Value_strategy)
def test_mongodb::value_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mongodb::Value_strategy)
def test_mongodb::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mongodb::IValue_strategy)
@settings(max_examples=50)
def test_mongodb::ivalue_instantiation(instance):
    assert isinstance(instance, mongodb::IValue)

@given(instance=mongodb::Document_strategy)
@settings(max_examples=50)
def test_mongodb::document_instantiation(instance):
    assert isinstance(instance, mongodb::Document)

@given(instance=mongodb::Document_strategy)
def test_mongodb::document__id_type(instance):
    assert isinstance(instance._id, str)


@given(instance=mongodb::Document_strategy)
def test_mongodb::document__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original

@given(instance=mongodb::Collection_strategy)
@settings(max_examples=50)
def test_mongodb::collection_instantiation(instance):
    assert isinstance(instance, mongodb::Collection)

@given(instance=mongodb::Collection_strategy)
def test_mongodb::collection_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mongodb::Collection_strategy)
def test_mongodb::collection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mongodb::Database_strategy)
@settings(max_examples=50)
def test_mongodb::database_instantiation(instance):
    assert isinstance(instance, mongodb::Database)

@given(instance=mongodb::Database_strategy)
def test_mongodb::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mongodb::Database_strategy)
def test_mongodb::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mongodb::Field_strategy)
@settings(max_examples=50)
def test_mongodb::field_instantiation(instance):
    assert isinstance(instance, mongodb::Field)

@given(instance=mongodb::Field_strategy)
def test_mongodb::field_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=mongodb::Field_strategy)
def test_mongodb::field_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original
