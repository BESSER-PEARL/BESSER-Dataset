import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dSDL::Table,
    dSDL::Database,
    Property,
    dSDL::ForeignKey,
    dSDL::Nullable,
    dSDL::AutoIncrement,
    dSDL::PrimaryKey,
    Type,
    dSDL::Varchar,
    dSDL::Text,
    dSDL::DateTime,
    dSDL::Integer,
    dSDL::Property,
    dSDL::Type,
    dSDL::Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsdl::table_is_not_abstract():
    assert not inspect.isabstract(dSDL::Table)


def test_dsdl::table_constructor_exists():
    assert callable(dSDL::Table.__init__)


def test_dsdl::table_constructor_args():
    sig = inspect.signature(dSDL::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsdl::table_has_name():
    assert hasattr(dSDL::Table, "name")
    descriptor = None
    for klass in dSDL::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::database_is_not_abstract():
    assert not inspect.isabstract(dSDL::Database)


def test_dsdl::database_constructor_exists():
    assert callable(dSDL::Database.__init__)


def test_dsdl::database_constructor_args():
    sig = inspect.signature(dSDL::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsdl::database_has_name():
    assert hasattr(dSDL::Database, "name")
    descriptor = None
    for klass in dSDL::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_dsdl::foreignkey_is_not_abstract():
    assert not inspect.isabstract(dSDL::ForeignKey)


def test_dsdl::foreignkey_constructor_exists():
    assert callable(dSDL::ForeignKey.__init__)


def test_dsdl::foreignkey_constructor_args():
    sig = inspect.signature(dSDL::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_dsdl::foreignkey_has_attributeName():
    assert hasattr(dSDL::ForeignKey, "attributeName")
    descriptor = None
    for klass in dSDL::ForeignKey.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)

def test_dsdl::foreignkey_has_tableName():
    assert hasattr(dSDL::ForeignKey, "tableName")
    descriptor = None
    for klass in dSDL::ForeignKey.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::nullable_is_not_abstract():
    assert not inspect.isabstract(dSDL::Nullable)


def test_dsdl::nullable_constructor_exists():
    assert callable(dSDL::Nullable.__init__)


def test_dsdl::nullable_constructor_args():
    sig = inspect.signature(dSDL::Nullable.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_dsdl::nullable_has_nullable():
    assert hasattr(dSDL::Nullable, "nullable")
    descriptor = None
    for klass in dSDL::Nullable.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::autoincrement_is_not_abstract():
    assert not inspect.isabstract(dSDL::AutoIncrement)


def test_dsdl::autoincrement_constructor_exists():
    assert callable(dSDL::AutoIncrement.__init__)


def test_dsdl::autoincrement_constructor_args():
    sig = inspect.signature(dSDL::AutoIncrement.__init__)
    params = list(sig.parameters.keys())
    assert "autoIncrement" in params, "Missing parameter 'autoIncrement'"

def test_dsdl::autoincrement_has_autoIncrement():
    assert hasattr(dSDL::AutoIncrement, "autoIncrement")
    descriptor = None
    for klass in dSDL::AutoIncrement.__mro__:
        if "autoIncrement" in klass.__dict__:
            descriptor = klass.__dict__["autoIncrement"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::primarykey_is_not_abstract():
    assert not inspect.isabstract(dSDL::PrimaryKey)


def test_dsdl::primarykey_constructor_exists():
    assert callable(dSDL::PrimaryKey.__init__)


def test_dsdl::primarykey_constructor_args():
    sig = inspect.signature(dSDL::PrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"

def test_dsdl::primarykey_has_primaryKey():
    assert hasattr(dSDL::PrimaryKey, "primaryKey")
    descriptor = None
    for klass in dSDL::PrimaryKey.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dsdl::varchar_is_not_abstract():
    assert not inspect.isabstract(dSDL::Varchar)


def test_dsdl::varchar_constructor_exists():
    assert callable(dSDL::Varchar.__init__)


def test_dsdl::varchar_constructor_args():
    sig = inspect.signature(dSDL::Varchar.__init__)
    params = list(sig.parameters.keys())
    assert "varchar" in params, "Missing parameter 'varchar'"
    assert "length" in params, "Missing parameter 'length'"

def test_dsdl::varchar_has_varchar():
    assert hasattr(dSDL::Varchar, "varchar")
    descriptor = None
    for klass in dSDL::Varchar.__mro__:
        if "varchar" in klass.__dict__:
            descriptor = klass.__dict__["varchar"]
            break
    assert isinstance(descriptor, property)

def test_dsdl::varchar_has_length():
    assert hasattr(dSDL::Varchar, "length")
    descriptor = None
    for klass in dSDL::Varchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::text_is_not_abstract():
    assert not inspect.isabstract(dSDL::Text)


def test_dsdl::text_constructor_exists():
    assert callable(dSDL::Text.__init__)


def test_dsdl::text_constructor_args():
    sig = inspect.signature(dSDL::Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_dsdl::text_has_text():
    assert hasattr(dSDL::Text, "text")
    descriptor = None
    for klass in dSDL::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::datetime_is_not_abstract():
    assert not inspect.isabstract(dSDL::DateTime)


def test_dsdl::datetime_constructor_exists():
    assert callable(dSDL::DateTime.__init__)


def test_dsdl::datetime_constructor_args():
    sig = inspect.signature(dSDL::DateTime.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_dsdl::datetime_has_date():
    assert hasattr(dSDL::DateTime, "date")
    descriptor = None
    for klass in dSDL::DateTime.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::integer_is_not_abstract():
    assert not inspect.isabstract(dSDL::Integer)


def test_dsdl::integer_constructor_exists():
    assert callable(dSDL::Integer.__init__)


def test_dsdl::integer_constructor_args():
    sig = inspect.signature(dSDL::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"
    assert "length" in params, "Missing parameter 'length'"

def test_dsdl::integer_has_integer():
    assert hasattr(dSDL::Integer, "integer")
    descriptor = None
    for klass in dSDL::Integer.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)

def test_dsdl::integer_has_length():
    assert hasattr(dSDL::Integer, "length")
    descriptor = None
    for klass in dSDL::Integer.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_dsdl::property_is_not_abstract():
    assert not inspect.isabstract(dSDL::Property)


def test_dsdl::property_constructor_exists():
    assert callable(dSDL::Property.__init__)


def test_dsdl::property_constructor_args():
    sig = inspect.signature(dSDL::Property.__init__)
    params = list(sig.parameters.keys())



def test_dsdl::type_is_not_abstract():
    assert not inspect.isabstract(dSDL::Type)


def test_dsdl::type_constructor_exists():
    assert callable(dSDL::Type.__init__)


def test_dsdl::type_constructor_args():
    sig = inspect.signature(dSDL::Type.__init__)
    params = list(sig.parameters.keys())



def test_dsdl::attribute_is_not_abstract():
    assert not inspect.isabstract(dSDL::Attribute)


def test_dsdl::attribute_constructor_exists():
    assert callable(dSDL::Attribute.__init__)


def test_dsdl::attribute_constructor_args():
    sig = inspect.signature(dSDL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_dsdl::attribute_has_attributeName():
    assert hasattr(dSDL::Attribute, "attributeName")
    descriptor = None
    for klass in dSDL::Attribute.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
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
dSDL::Table_strategy = st.builds(
    dSDL::Table,
    name=
        safe_text
)
dSDL::Database_strategy = st.builds(
    dSDL::Database,
    name=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
dSDL::ForeignKey_strategy = st.builds(
    dSDL::ForeignKey,
    attributeName=
        safe_text,
    tableName=
        safe_text
)
dSDL::Nullable_strategy = st.builds(
    dSDL::Nullable,
    nullable=
        st.booleans()
)
dSDL::AutoIncrement_strategy = st.builds(
    dSDL::AutoIncrement,
    autoIncrement=
        st.booleans()
)
dSDL::PrimaryKey_strategy = st.builds(
    dSDL::PrimaryKey,
    primaryKey=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
dSDL::Varchar_strategy = st.builds(
    dSDL::Varchar,
    varchar=
        safe_text,
    length=
        st.integers()
)
dSDL::Text_strategy = st.builds(
    dSDL::Text,
    text=
        safe_text
)
dSDL::DateTime_strategy = st.builds(
    dSDL::DateTime,
    date=
        safe_text
)
dSDL::Integer_strategy = st.builds(
    dSDL::Integer,
    integer=
        safe_text,
    length=
        st.integers()
)
dSDL::Property_strategy = st.builds(
    dSDL::Property,
)
dSDL::Type_strategy = st.builds(
    dSDL::Type,
)
dSDL::Attribute_strategy = st.builds(
    dSDL::Attribute,
    attributeName=
        safe_text
)

@given(instance=dSDL::Table_strategy)
@settings(max_examples=50)
def test_dsdl::table_instantiation(instance):
    assert isinstance(instance, dSDL::Table)

@given(instance=dSDL::Table_strategy)
def test_dsdl::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSDL::Table_strategy)
def test_dsdl::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSDL::Database_strategy)
@settings(max_examples=50)
def test_dsdl::database_instantiation(instance):
    assert isinstance(instance, dSDL::Database)

@given(instance=dSDL::Database_strategy)
def test_dsdl::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSDL::Database_strategy)
def test_dsdl::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=dSDL::ForeignKey_strategy)
@settings(max_examples=50)
def test_dsdl::foreignkey_instantiation(instance):
    assert isinstance(instance, dSDL::ForeignKey)

@given(instance=dSDL::ForeignKey_strategy)
def test_dsdl::foreignkey_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=dSDL::ForeignKey_strategy)
def test_dsdl::foreignkey_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=dSDL::ForeignKey_strategy)
def test_dsdl::foreignkey_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=dSDL::ForeignKey_strategy)
def test_dsdl::foreignkey_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=dSDL::Nullable_strategy)
@settings(max_examples=50)
def test_dsdl::nullable_instantiation(instance):
    assert isinstance(instance, dSDL::Nullable)

@given(instance=dSDL::Nullable_strategy)
def test_dsdl::nullable_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=dSDL::Nullable_strategy)
def test_dsdl::nullable_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=dSDL::AutoIncrement_strategy)
@settings(max_examples=50)
def test_dsdl::autoincrement_instantiation(instance):
    assert isinstance(instance, dSDL::AutoIncrement)

@given(instance=dSDL::AutoIncrement_strategy)
def test_dsdl::autoincrement_autoIncrement_type(instance):
    assert isinstance(instance.autoIncrement, bool)


@given(instance=dSDL::AutoIncrement_strategy)
def test_dsdl::autoincrement_autoIncrement_setter(instance):
    original = instance.autoIncrement
    instance.autoIncrement = original
    assert instance.autoIncrement == original

@given(instance=dSDL::PrimaryKey_strategy)
@settings(max_examples=50)
def test_dsdl::primarykey_instantiation(instance):
    assert isinstance(instance, dSDL::PrimaryKey)

@given(instance=dSDL::PrimaryKey_strategy)
def test_dsdl::primarykey_primaryKey_type(instance):
    assert isinstance(instance.primaryKey, bool)


@given(instance=dSDL::PrimaryKey_strategy)
def test_dsdl::primarykey_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dSDL::Varchar_strategy)
@settings(max_examples=50)
def test_dsdl::varchar_instantiation(instance):
    assert isinstance(instance, dSDL::Varchar)

@given(instance=dSDL::Varchar_strategy)
def test_dsdl::varchar_varchar_type(instance):
    assert isinstance(instance.varchar, str)


@given(instance=dSDL::Varchar_strategy)
def test_dsdl::varchar_varchar_setter(instance):
    original = instance.varchar
    instance.varchar = original
    assert instance.varchar == original

@given(instance=dSDL::Varchar_strategy)
def test_dsdl::varchar_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=dSDL::Varchar_strategy)
def test_dsdl::varchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=dSDL::Text_strategy)
@settings(max_examples=50)
def test_dsdl::text_instantiation(instance):
    assert isinstance(instance, dSDL::Text)

@given(instance=dSDL::Text_strategy)
def test_dsdl::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=dSDL::Text_strategy)
def test_dsdl::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=dSDL::DateTime_strategy)
@settings(max_examples=50)
def test_dsdl::datetime_instantiation(instance):
    assert isinstance(instance, dSDL::DateTime)

@given(instance=dSDL::DateTime_strategy)
def test_dsdl::datetime_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=dSDL::DateTime_strategy)
def test_dsdl::datetime_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=dSDL::Integer_strategy)
@settings(max_examples=50)
def test_dsdl::integer_instantiation(instance):
    assert isinstance(instance, dSDL::Integer)

@given(instance=dSDL::Integer_strategy)
def test_dsdl::integer_integer_type(instance):
    assert isinstance(instance.integer, str)


@given(instance=dSDL::Integer_strategy)
def test_dsdl::integer_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=dSDL::Integer_strategy)
def test_dsdl::integer_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=dSDL::Integer_strategy)
def test_dsdl::integer_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=dSDL::Property_strategy)
@settings(max_examples=50)
def test_dsdl::property_instantiation(instance):
    assert isinstance(instance, dSDL::Property)

@given(instance=dSDL::Type_strategy)
@settings(max_examples=50)
def test_dsdl::type_instantiation(instance):
    assert isinstance(instance, dSDL::Type)

@given(instance=dSDL::Attribute_strategy)
@settings(max_examples=50)
def test_dsdl::attribute_instantiation(instance):
    assert isinstance(instance, dSDL::Attribute)

@given(instance=dSDL::Attribute_strategy)
def test_dsdl::attribute_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=dSDL::Attribute_strategy)
def test_dsdl::attribute_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original
