import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    relational::Field,
    relational::Table,
    relational::Schema,
    relational::DataBase,
    Field,
    relational::Column,
    relational::ForeignKey,
    relational::PrimaryKey,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::field_is_not_abstract():
    assert not inspect.isabstract(relational::Field)


def test_relational::field_constructor_exists():
    assert callable(relational::Field.__init__)


def test_relational::field_constructor_args():
    sig = inspect.signature(relational::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::field_has_name():
    assert hasattr(relational::Field, "name")
    descriptor = None
    for klass in relational::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(relational::Table)


def test_relational::table_constructor_exists():
    assert callable(relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(relational::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::table_has_name():
    assert hasattr(relational::Table, "name")
    descriptor = None
    for klass in relational::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(relational::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::schema_has_name():
    assert hasattr(relational::Schema, "name")
    descriptor = None
    for klass in relational::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::database_is_not_abstract():
    assert not inspect.isabstract(relational::DataBase)


def test_relational::database_constructor_exists():
    assert callable(relational::DataBase.__init__)


def test_relational::database_constructor_args():
    sig = inspect.signature(relational::DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "port" in params, "Missing parameter 'port'"

def test_relational::database_has_uri():
    assert hasattr(relational::DataBase, "uri")
    descriptor = None
    for klass in relational::DataBase.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_relational::database_has_port():
    assert hasattr(relational::DataBase, "port")
    descriptor = None
    for klass in relational::DataBase.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(relational::Column)


def test_relational::column_constructor_exists():
    assert callable(relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(relational::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_relational::column_has_type():
    assert hasattr(relational::Column, "type")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::primarykey_is_not_abstract():
    assert not inspect.isabstract(relational::PrimaryKey)


def test_relational::primarykey_constructor_exists():
    assert callable(relational::PrimaryKey.__init__)


def test_relational::primarykey_constructor_args():
    sig = inspect.signature(relational::PrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_relational::primarykey_has_id():
    assert hasattr(relational::PrimaryKey, "id")
    descriptor = None
    for klass in relational::PrimaryKey.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "DATE",
        "BOOLEAN",
        "TIME",
        "VARCHAR",
        "CHAR",
        "NUMERIC",
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
relational::Field_strategy = st.builds(
    relational::Field,
    name=
        safe_text
)
relational::Table_strategy = st.builds(
    relational::Table,
    name=
        safe_text
)
relational::Schema_strategy = st.builds(
    relational::Schema,
    name=
        safe_text
)
relational::DataBase_strategy = st.builds(
    relational::DataBase,
    uri=
        safe_text,
    port=
        st.integers()
)
Field_strategy = st.builds(
    Field,
)
relational::Column_strategy = st.builds(
    relational::Column,
    type=
        safe_text
)
relational::ForeignKey_strategy = st.builds(
    relational::ForeignKey,
)
relational::PrimaryKey_strategy = st.builds(
    relational::PrimaryKey,
    id=
        safe_text
)

@given(instance=relational::Field_strategy)
@settings(max_examples=50)
def test_relational::field_instantiation(instance):
    assert isinstance(instance, relational::Field)

@given(instance=relational::Field_strategy)
def test_relational::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Field_strategy)
def test_relational::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=relational::Table_strategy)
def test_relational::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Table_strategy)
def test_relational::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, relational::Schema)

@given(instance=relational::Schema_strategy)
def test_relational::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Schema_strategy)
def test_relational::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::DataBase_strategy)
@settings(max_examples=50)
def test_relational::database_instantiation(instance):
    assert isinstance(instance, relational::DataBase)

@given(instance=relational::DataBase_strategy)
def test_relational::database_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=relational::DataBase_strategy)
def test_relational::database_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=relational::DataBase_strategy)
def test_relational::database_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=relational::DataBase_strategy)
def test_relational::database_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Column_strategy)
def test_relational::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=relational::Column_strategy)
def test_relational::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::ForeignKey)

@given(instance=relational::PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational::primarykey_instantiation(instance):
    assert isinstance(instance, relational::PrimaryKey)

@given(instance=relational::PrimaryKey_strategy)
def test_relational::primarykey_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=relational::PrimaryKey_strategy)
def test_relational::primarykey_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
