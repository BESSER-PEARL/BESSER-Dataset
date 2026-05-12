import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IValue,
    mongodb_ValueList,
    mongodb_SubDocument,
    mongodb_Value,
    mongodb_IValue,
    mongodb_Document,
    mongodb_Collection,
    mongodb_Database,
    mongodb_Field,
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



def test_mongodb_valuelist_is_not_abstract():
    assert not inspect.isabstract(mongodb_ValueList)


def test_mongodb_valuelist_constructor_exists():
    assert callable(mongodb_ValueList.__init__)


def test_mongodb_valuelist_constructor_args():
    sig = inspect.signature(mongodb_ValueList.__init__)
    params = list(sig.parameters.keys())



def test_mongodb_subdocument_is_not_abstract():
    assert not inspect.isabstract(mongodb_SubDocument)


def test_mongodb_subdocument_constructor_exists():
    assert callable(mongodb_SubDocument.__init__)


def test_mongodb_subdocument_constructor_args():
    sig = inspect.signature(mongodb_SubDocument.__init__)
    params = list(sig.parameters.keys())



def test_mongodb_value_is_not_abstract():
    assert not inspect.isabstract(mongodb_Value)


def test_mongodb_value_constructor_exists():
    assert callable(mongodb_Value.__init__)


def test_mongodb_value_constructor_args():
    sig = inspect.signature(mongodb_Value.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mongodb_value_has_type():
    assert hasattr(mongodb_Value, "type")
    descriptor = None
    for klass in mongodb_Value.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mongodb_value_has_value():
    assert hasattr(mongodb_Value, "value")
    descriptor = None
    for klass in mongodb_Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mongodb_ivalue_is_not_abstract():
    assert not inspect.isabstract(mongodb_IValue)


def test_mongodb_ivalue_constructor_exists():
    assert callable(mongodb_IValue.__init__)


def test_mongodb_ivalue_constructor_args():
    sig = inspect.signature(mongodb_IValue.__init__)
    params = list(sig.parameters.keys())



def test_mongodb_document_is_not_abstract():
    assert not inspect.isabstract(mongodb_Document)


def test_mongodb_document_constructor_exists():
    assert callable(mongodb_Document.__init__)


def test_mongodb_document_constructor_args():
    sig = inspect.signature(mongodb_Document.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"

def test_mongodb_document_has__id():
    assert hasattr(mongodb_Document, "_id")
    descriptor = None
    for klass in mongodb_Document.__mro__:
        if "_id" in klass.__dict__:
            descriptor = klass.__dict__["_id"]
            break
    assert isinstance(descriptor, property)



def test_mongodb_collection_is_not_abstract():
    assert not inspect.isabstract(mongodb_Collection)


def test_mongodb_collection_constructor_exists():
    assert callable(mongodb_Collection.__init__)


def test_mongodb_collection_constructor_args():
    sig = inspect.signature(mongodb_Collection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mongodb_collection_has_name():
    assert hasattr(mongodb_Collection, "name")
    descriptor = None
    for klass in mongodb_Collection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mongodb_database_is_not_abstract():
    assert not inspect.isabstract(mongodb_Database)


def test_mongodb_database_constructor_exists():
    assert callable(mongodb_Database.__init__)


def test_mongodb_database_constructor_args():
    sig = inspect.signature(mongodb_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mongodb_database_has_name():
    assert hasattr(mongodb_Database, "name")
    descriptor = None
    for klass in mongodb_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mongodb_field_is_not_abstract():
    assert not inspect.isabstract(mongodb_Field)


def test_mongodb_field_constructor_exists():
    assert callable(mongodb_Field.__init__)


def test_mongodb_field_constructor_args():
    sig = inspect.signature(mongodb_Field.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_mongodb_field_has_key():
    assert hasattr(mongodb_Field, "key")
    descriptor = None
    for klass in mongodb_Field.__mro__:
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
        "TIMESTAMP",
        "DATE",
        "STRING",
        "JAVASCRIPT",
        "REGEXPR",
        "BOOLEAN",
        "NULL",
        "DOUBLE",
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
mongodb_ValueList_strategy = st.builds(
    mongodb_ValueList,
)
mongodb_SubDocument_strategy = st.builds(
    mongodb_SubDocument,
)
mongodb_Value_strategy = st.builds(
    mongodb_Value,
    type=
        safe_text,
    value=
        safe_text
)
mongodb_IValue_strategy = st.builds(
    mongodb_IValue,
)
mongodb_Document_strategy = st.builds(
    mongodb_Document,
    _id=
        safe_text
)
mongodb_Collection_strategy = st.builds(
    mongodb_Collection,
    name=
        safe_text
)
mongodb_Database_strategy = st.builds(
    mongodb_Database,
    name=
        safe_text
)
mongodb_Field_strategy = st.builds(
    mongodb_Field,
    key=
        safe_text
)

@given(instance=IValue_strategy)
@settings(max_examples=50)
def test_ivalue_instantiation(instance):
    assert isinstance(instance, IValue)

@given(instance=mongodb_ValueList_strategy)
@settings(max_examples=50)
def test_mongodb_valuelist_instantiation(instance):
    assert isinstance(instance, mongodb_ValueList)

@given(instance=mongodb_SubDocument_strategy)
@settings(max_examples=50)
def test_mongodb_subdocument_instantiation(instance):
    assert isinstance(instance, mongodb_SubDocument)

@given(instance=mongodb_Value_strategy)
@settings(max_examples=50)
def test_mongodb_value_instantiation(instance):
    assert isinstance(instance, mongodb_Value)



@given(instance=mongodb_Value_strategy)
def test_mongodb_value_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=mongodb_Value_strategy)
def test_mongodb_value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mongodb_IValue_strategy)
@settings(max_examples=50)
def test_mongodb_ivalue_instantiation(instance):
    assert isinstance(instance, mongodb_IValue)

@given(instance=mongodb_Document_strategy)
@settings(max_examples=50)
def test_mongodb_document_instantiation(instance):
    assert isinstance(instance, mongodb_Document)



@given(instance=mongodb_Document_strategy)
def test_mongodb_document__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original

@given(instance=mongodb_Collection_strategy)
@settings(max_examples=50)
def test_mongodb_collection_instantiation(instance):
    assert isinstance(instance, mongodb_Collection)



@given(instance=mongodb_Collection_strategy)
def test_mongodb_collection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mongodb_Database_strategy)
@settings(max_examples=50)
def test_mongodb_database_instantiation(instance):
    assert isinstance(instance, mongodb_Database)



@given(instance=mongodb_Database_strategy)
def test_mongodb_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mongodb_Field_strategy)
@settings(max_examples=50)
def test_mongodb_field_instantiation(instance):
    assert isinstance(instance, mongodb_Field)



@given(instance=mongodb_Field_strategy)
def test_mongodb_field_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original
