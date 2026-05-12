import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Field,
    relational_Column,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Table,
    relational_Schema,
    relational_DataBase,
    relational_Field,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_relational_column_has_type():
    assert hasattr(relational_Column, "type")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_primarykey_is_not_abstract():
    assert not inspect.isabstract(relational_PrimaryKey)


def test_relational_primarykey_constructor_exists():
    assert callable(relational_PrimaryKey.__init__)


def test_relational_primarykey_constructor_args():
    sig = inspect.signature(relational_PrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_relational_primarykey_has_id():
    assert hasattr(relational_PrimaryKey, "id")
    descriptor = None
    for klass in relational_PrimaryKey.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_table_has_name():
    assert hasattr(relational_Table, "name")
    descriptor = None
    for klass in relational_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_schema_has_name():
    assert hasattr(relational_Schema, "name")
    descriptor = None
    for klass in relational_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_database_is_not_abstract():
    assert not inspect.isabstract(relational_DataBase)


def test_relational_database_constructor_exists():
    assert callable(relational_DataBase.__init__)


def test_relational_database_constructor_args():
    sig = inspect.signature(relational_DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_relational_database_has_port():
    assert hasattr(relational_DataBase, "port")
    descriptor = None
    for klass in relational_DataBase.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_relational_database_has_uri():
    assert hasattr(relational_DataBase, "uri")
    descriptor = None
    for klass in relational_DataBase.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_relational_field_is_not_abstract():
    assert not inspect.isabstract(relational_Field)


def test_relational_field_constructor_exists():
    assert callable(relational_Field.__init__)


def test_relational_field_constructor_args():
    sig = inspect.signature(relational_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_field_has_name():
    assert hasattr(relational_Field, "name")
    descriptor = None
    for klass in relational_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "CHAR",
        "DATE",
        "VARCHAR",
        "TIME",
        "NUMERIC",
        "BOOLEAN",
        "FLOAT",
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
Field_strategy = st.builds(
    Field,
)
relational_Column_strategy = st.builds(
    relational_Column,
    type=
        safe_text
)
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
)
relational_PrimaryKey_strategy = st.builds(
    relational_PrimaryKey,
    id=
        safe_text
)
relational_Table_strategy = st.builds(
    relational_Table,
    name=
        safe_text
)
relational_Schema_strategy = st.builds(
    relational_Schema,
    name=
        safe_text
)
relational_DataBase_strategy = st.builds(
    relational_DataBase,
    port=
        st.integers(),
    uri=
        safe_text
)
relational_Field_strategy = st.builds(
    relational_Field,
    name=
        safe_text
)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)



@given(instance=relational_Column_strategy)
def test_relational_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)

@given(instance=relational_PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational_primarykey_instantiation(instance):
    assert isinstance(instance, relational_PrimaryKey)



@given(instance=relational_PrimaryKey_strategy)
def test_relational_primarykey_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)



@given(instance=relational_Table_strategy)
def test_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)



@given(instance=relational_Schema_strategy)
def test_relational_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_DataBase_strategy)
@settings(max_examples=50)
def test_relational_database_instantiation(instance):
    assert isinstance(instance, relational_DataBase)



@given(instance=relational_DataBase_strategy)
def test_relational_database_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=relational_DataBase_strategy)
def test_relational_database_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=relational_Field_strategy)
@settings(max_examples=50)
def test_relational_field_instantiation(instance):
    assert isinstance(instance, relational_Field)



@given(instance=relational_Field_strategy)
def test_relational_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
