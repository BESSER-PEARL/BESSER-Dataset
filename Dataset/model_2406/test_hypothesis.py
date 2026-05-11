import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    database::NamedElement,
    NamedElement,
    database::Column,
    database::Table,
    database::DataBase,
    Index,
    database::Unique,
    database::PrimaryKey,
    database::Index,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::namedelement_is_not_abstract():
    assert not inspect.isabstract(database::NamedElement)


def test_database::namedelement_constructor_exists():
    assert callable(database::NamedElement.__init__)


def test_database::namedelement_constructor_args():
    sig = inspect.signature(database::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database::namedelement_has_name():
    assert hasattr(database::NamedElement, "name")
    descriptor = None
    for klass in database::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "collation" in params, "Missing parameter 'collation'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "type" in params, "Missing parameter 'type'"
    assert "length" in params, "Missing parameter 'length'"

def test_database::column_has_default():
    assert hasattr(database::Column, "default")
    descriptor = None
    for klass in database::Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_collation():
    assert hasattr(database::Column, "collation")
    descriptor = None
    for klass in database::Column.__mro__:
        if "collation" in klass.__dict__:
            descriptor = klass.__dict__["collation"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_nullable():
    assert hasattr(database::Column, "nullable")
    descriptor = None
    for klass in database::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_type():
    assert hasattr(database::Column, "type")
    descriptor = None
    for klass in database::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_database::column_has_length():
    assert hasattr(database::Column, "length")
    descriptor = None
    for klass in database::Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(database::Table)


def test_database::table_constructor_exists():
    assert callable(database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(database::Table.__init__)
    params = list(sig.parameters.keys())
    assert "collation" in params, "Missing parameter 'collation'"
    assert "storageEngine" in params, "Missing parameter 'storageEngine'"

def test_database::table_has_collation():
    assert hasattr(database::Table, "collation")
    descriptor = None
    for klass in database::Table.__mro__:
        if "collation" in klass.__dict__:
            descriptor = klass.__dict__["collation"]
            break
    assert isinstance(descriptor, property)

def test_database::table_has_storageEngine():
    assert hasattr(database::Table, "storageEngine")
    descriptor = None
    for klass in database::Table.__mro__:
        if "storageEngine" in klass.__dict__:
            descriptor = klass.__dict__["storageEngine"]
            break
    assert isinstance(descriptor, property)



def test_database::database_is_not_abstract():
    assert not inspect.isabstract(database::DataBase)


def test_database::database_constructor_exists():
    assert callable(database::DataBase.__init__)


def test_database::database_constructor_args():
    sig = inspect.signature(database::DataBase.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_database::unique_is_not_abstract():
    assert not inspect.isabstract(database::Unique)


def test_database::unique_constructor_exists():
    assert callable(database::Unique.__init__)


def test_database::unique_constructor_args():
    sig = inspect.signature(database::Unique.__init__)
    params = list(sig.parameters.keys())



def test_database::primarykey_is_not_abstract():
    assert not inspect.isabstract(database::PrimaryKey)


def test_database::primarykey_constructor_exists():
    assert callable(database::PrimaryKey.__init__)


def test_database::primarykey_constructor_args():
    sig = inspect.signature(database::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_database::index_is_not_abstract():
    assert not inspect.isabstract(database::Index)


def test_database::index_constructor_exists():
    assert callable(database::Index.__init__)


def test_database::index_constructor_args():
    sig = inspect.signature(database::Index.__init__)
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
database::NamedElement_strategy = st.builds(
    database::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
database::Column_strategy = st.builds(
    database::Column,
    default=
        safe_text,
    collation=
        safe_text,
    nullable=
        st.booleans(),
    type=
        safe_text,
    length=
        st.integers()
)
database::Table_strategy = st.builds(
    database::Table,
    collation=
        safe_text,
    storageEngine=
        safe_text
)
database::DataBase_strategy = st.builds(
    database::DataBase,
)
Index_strategy = st.builds(
    Index,
)
database::Unique_strategy = st.builds(
    database::Unique,
)
database::PrimaryKey_strategy = st.builds(
    database::PrimaryKey,
)
database::Index_strategy = st.builds(
    database::Index,
)

@given(instance=database::NamedElement_strategy)
@settings(max_examples=50)
def test_database::namedelement_instantiation(instance):
    assert isinstance(instance, database::NamedElement)

@given(instance=database::NamedElement_strategy)
def test_database::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::NamedElement_strategy)
def test_database::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Column_strategy)
def test_database::column_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=database::Column_strategy)
def test_database::column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=database::Column_strategy)
def test_database::column_collation_type(instance):
    assert isinstance(instance.collation, str)


@given(instance=database::Column_strategy)
def test_database::column_collation_setter(instance):
    original = instance.collation
    instance.collation = original
    assert instance.collation == original

@given(instance=database::Column_strategy)
def test_database::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=database::Column_strategy)
def test_database::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=database::Column_strategy)
def test_database::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=database::Column_strategy)
def test_database::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=database::Column_strategy)
def test_database::column_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=database::Column_strategy)
def test_database::column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, database::Table)

@given(instance=database::Table_strategy)
def test_database::table_collation_type(instance):
    assert isinstance(instance.collation, str)


@given(instance=database::Table_strategy)
def test_database::table_collation_setter(instance):
    original = instance.collation
    instance.collation = original
    assert instance.collation == original

@given(instance=database::Table_strategy)
def test_database::table_storageEngine_type(instance):
    assert isinstance(instance.storageEngine, str)


@given(instance=database::Table_strategy)
def test_database::table_storageEngine_setter(instance):
    original = instance.storageEngine
    instance.storageEngine = original
    assert instance.storageEngine == original

@given(instance=database::DataBase_strategy)
@settings(max_examples=50)
def test_database::database_instantiation(instance):
    assert isinstance(instance, database::DataBase)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=database::Unique_strategy)
@settings(max_examples=50)
def test_database::unique_instantiation(instance):
    assert isinstance(instance, database::Unique)

@given(instance=database::PrimaryKey_strategy)
@settings(max_examples=50)
def test_database::primarykey_instantiation(instance):
    assert isinstance(instance, database::PrimaryKey)

@given(instance=database::Index_strategy)
@settings(max_examples=50)
def test_database::index_instantiation(instance):
    assert isinstance(instance, database::Index)
