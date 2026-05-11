import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimitiveType,
    relationaldb::Integer,
    relationaldb::UmlToNoSQLID,
    relationaldb::Varchar,
    Type,
    relationaldb::PrimitiveType,
    Named,
    relationaldb::Table,
    relationaldb::Database,
    relationaldb::Named,
    Column,
    relationaldb::ForeignKey,
    relationaldb::Type,
    relationaldb::Column,
    DatabaseKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::integer_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Integer)


def test_relationaldb::integer_constructor_exists():
    assert callable(relationaldb::Integer.__init__)


def test_relationaldb::integer_constructor_args():
    sig = inspect.signature(relationaldb::Integer.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::umltonosqlid_is_not_abstract():
    assert not inspect.isabstract(relationaldb::UmlToNoSQLID)


def test_relationaldb::umltonosqlid_constructor_exists():
    assert callable(relationaldb::UmlToNoSQLID.__init__)


def test_relationaldb::umltonosqlid_constructor_args():
    sig = inspect.signature(relationaldb::UmlToNoSQLID.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::varchar_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Varchar)


def test_relationaldb::varchar_constructor_exists():
    assert callable(relationaldb::Varchar.__init__)


def test_relationaldb::varchar_constructor_args():
    sig = inspect.signature(relationaldb::Varchar.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_relationaldb::varchar_has_length():
    assert hasattr(relationaldb::Varchar, "length")
    descriptor = None
    for klass in relationaldb::Varchar.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::primitivetype_is_not_abstract():
    assert not inspect.isabstract(relationaldb::PrimitiveType)


def test_relationaldb::primitivetype_constructor_exists():
    assert callable(relationaldb::PrimitiveType.__init__)


def test_relationaldb::primitivetype_constructor_args():
    sig = inspect.signature(relationaldb::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::table_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Table)


def test_relationaldb::table_constructor_exists():
    assert callable(relationaldb::Table.__init__)


def test_relationaldb::table_constructor_args():
    sig = inspect.signature(relationaldb::Table.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::database_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Database)


def test_relationaldb::database_constructor_exists():
    assert callable(relationaldb::Database.__init__)


def test_relationaldb::database_constructor_args():
    sig = inspect.signature(relationaldb::Database.__init__)
    params = list(sig.parameters.keys())
    assert "rawDatabase" in params, "Missing parameter 'rawDatabase'"

def test_relationaldb::database_has_rawDatabase():
    assert hasattr(relationaldb::Database, "rawDatabase")
    descriptor = None
    for klass in relationaldb::Database.__mro__:
        if "rawDatabase" in klass.__dict__:
            descriptor = klass.__dict__["rawDatabase"]
            break
    assert isinstance(descriptor, property)



def test_relationaldb::named_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Named)


def test_relationaldb::named_constructor_exists():
    assert callable(relationaldb::Named.__init__)


def test_relationaldb::named_constructor_args():
    sig = inspect.signature(relationaldb::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationaldb::named_has_name():
    assert hasattr(relationaldb::Named, "name")
    descriptor = None
    for klass in relationaldb::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relationaldb::ForeignKey)


def test_relationaldb::foreignkey_constructor_exists():
    assert callable(relationaldb::ForeignKey.__init__)


def test_relationaldb::foreignkey_constructor_args():
    sig = inspect.signature(relationaldb::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::type_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Type)


def test_relationaldb::type_constructor_exists():
    assert callable(relationaldb::Type.__init__)


def test_relationaldb::type_constructor_args():
    sig = inspect.signature(relationaldb::Type.__init__)
    params = list(sig.parameters.keys())



def test_relationaldb::column_is_not_abstract():
    assert not inspect.isabstract(relationaldb::Column)


def test_relationaldb::column_constructor_exists():
    assert callable(relationaldb::Column.__init__)


def test_relationaldb::column_constructor_args():
    sig = inspect.signature(relationaldb::Column.__init__)
    params = list(sig.parameters.keys())

def test_databasekind_exists():
    # Check that the Enumeration exists
    assert DatabaseKind is not None

def test_databasekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseKind]
    expected_literals = [
        "POSTGRES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatabaseKind"


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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
relationaldb::Integer_strategy = st.builds(
    relationaldb::Integer,
)
relationaldb::UmlToNoSQLID_strategy = st.builds(
    relationaldb::UmlToNoSQLID,
)
relationaldb::Varchar_strategy = st.builds(
    relationaldb::Varchar,
    length=
        st.integers()
)
Type_strategy = st.builds(
    Type,
)
relationaldb::PrimitiveType_strategy = st.builds(
    relationaldb::PrimitiveType,
)
Named_strategy = st.builds(
    Named,
)
relationaldb::Table_strategy = st.builds(
    relationaldb::Table,
)
relationaldb::Database_strategy = st.builds(
    relationaldb::Database,
    rawDatabase=
        safe_text
)
relationaldb::Named_strategy = st.builds(
    relationaldb::Named,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
relationaldb::ForeignKey_strategy = st.builds(
    relationaldb::ForeignKey,
)
relationaldb::Type_strategy = st.builds(
    relationaldb::Type,
)
relationaldb::Column_strategy = st.builds(
    relationaldb::Column,
)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=relationaldb::Integer_strategy)
@settings(max_examples=50)
def test_relationaldb::integer_instantiation(instance):
    assert isinstance(instance, relationaldb::Integer)

@given(instance=relationaldb::UmlToNoSQLID_strategy)
@settings(max_examples=50)
def test_relationaldb::umltonosqlid_instantiation(instance):
    assert isinstance(instance, relationaldb::UmlToNoSQLID)

@given(instance=relationaldb::Varchar_strategy)
@settings(max_examples=50)
def test_relationaldb::varchar_instantiation(instance):
    assert isinstance(instance, relationaldb::Varchar)

@given(instance=relationaldb::Varchar_strategy)
def test_relationaldb::varchar_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=relationaldb::Varchar_strategy)
def test_relationaldb::varchar_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=relationaldb::PrimitiveType_strategy)
@settings(max_examples=50)
def test_relationaldb::primitivetype_instantiation(instance):
    assert isinstance(instance, relationaldb::PrimitiveType)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=relationaldb::Table_strategy)
@settings(max_examples=50)
def test_relationaldb::table_instantiation(instance):
    assert isinstance(instance, relationaldb::Table)

@given(instance=relationaldb::Database_strategy)
@settings(max_examples=50)
def test_relationaldb::database_instantiation(instance):
    assert isinstance(instance, relationaldb::Database)

@given(instance=relationaldb::Database_strategy)
def test_relationaldb::database_rawDatabase_type(instance):
    assert isinstance(instance.rawDatabase, str)


@given(instance=relationaldb::Database_strategy)
def test_relationaldb::database_rawDatabase_setter(instance):
    original = instance.rawDatabase
    instance.rawDatabase = original
    assert instance.rawDatabase == original

@given(instance=relationaldb::Named_strategy)
@settings(max_examples=50)
def test_relationaldb::named_instantiation(instance):
    assert isinstance(instance, relationaldb::Named)

@given(instance=relationaldb::Named_strategy)
def test_relationaldb::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relationaldb::Named_strategy)
def test_relationaldb::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=relationaldb::ForeignKey_strategy)
@settings(max_examples=50)
def test_relationaldb::foreignkey_instantiation(instance):
    assert isinstance(instance, relationaldb::ForeignKey)

@given(instance=relationaldb::Type_strategy)
@settings(max_examples=50)
def test_relationaldb::type_instantiation(instance):
    assert isinstance(instance, relationaldb::Type)

@given(instance=relationaldb::Column_strategy)
@settings(max_examples=50)
def test_relationaldb::column_instantiation(instance):
    assert isinstance(instance, relationaldb::Column)
