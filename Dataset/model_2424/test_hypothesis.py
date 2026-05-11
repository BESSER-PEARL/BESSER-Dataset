import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatabaseElement,
    DB::ForeignKey,
    DB::Column,
    DB::Table,
    NamedElement,
    DB::DatabaseElement,
    DB::Database,
    DB::NamedElement,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_databaseelement_is_not_abstract():
    assert not inspect.isabstract(DatabaseElement)


def test_databaseelement_constructor_exists():
    assert callable(DatabaseElement.__init__)


def test_databaseelement_constructor_args():
    sig = inspect.signature(DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db::foreignkey_is_not_abstract():
    assert not inspect.isabstract(DB::ForeignKey)


def test_db::foreignkey_constructor_exists():
    assert callable(DB::ForeignKey.__init__)


def test_db::foreignkey_constructor_args():
    sig = inspect.signature(DB::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_db::foreignkey_has_isMany():
    assert hasattr(DB::ForeignKey, "isMany")
    descriptor = None
    for klass in DB::ForeignKey.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_db::column_is_not_abstract():
    assert not inspect.isabstract(DB::Column)


def test_db::column_constructor_exists():
    assert callable(DB::Column.__init__)


def test_db::column_constructor_args():
    sig = inspect.signature(DB::Column.__init__)
    params = list(sig.parameters.keys())
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "type" in params, "Missing parameter 'type'"

def test_db::column_has_notNull():
    assert hasattr(DB::Column, "notNull")
    descriptor = None
    for klass in DB::Column.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)

def test_db::column_has_type():
    assert hasattr(DB::Column, "type")
    descriptor = None
    for klass in DB::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_db::table_is_not_abstract():
    assert not inspect.isabstract(DB::Table)


def test_db::table_constructor_exists():
    assert callable(DB::Table.__init__)


def test_db::table_constructor_args():
    sig = inspect.signature(DB::Table.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_db::databaseelement_is_not_abstract():
    assert not inspect.isabstract(DB::DatabaseElement)


def test_db::databaseelement_constructor_exists():
    assert callable(DB::DatabaseElement.__init__)


def test_db::databaseelement_constructor_args():
    sig = inspect.signature(DB::DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db::database_is_not_abstract():
    assert not inspect.isabstract(DB::Database)


def test_db::database_constructor_exists():
    assert callable(DB::Database.__init__)


def test_db::database_constructor_args():
    sig = inspect.signature(DB::Database.__init__)
    params = list(sig.parameters.keys())



def test_db::namedelement_is_not_abstract():
    assert not inspect.isabstract(DB::NamedElement)


def test_db::namedelement_constructor_exists():
    assert callable(DB::NamedElement.__init__)


def test_db::namedelement_constructor_args():
    sig = inspect.signature(DB::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_db::namedelement_has_name():
    assert hasattr(DB::NamedElement, "name")
    descriptor = None
    for klass in DB::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "varchar",
        "int",
        "text",
        "unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
DatabaseElement_strategy = st.builds(
    DatabaseElement,
)
DB::ForeignKey_strategy = st.builds(
    DB::ForeignKey,
    isMany=
        safe_text
)
DB::Column_strategy = st.builds(
    DB::Column,
    notNull=
        st.booleans(),
    type=
        safe_text
)
DB::Table_strategy = st.builds(
    DB::Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
DB::DatabaseElement_strategy = st.builds(
    DB::DatabaseElement,
)
DB::Database_strategy = st.builds(
    DB::Database,
)
DB::NamedElement_strategy = st.builds(
    DB::NamedElement,
    name=
        safe_text
)

@given(instance=DatabaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DatabaseElement)

@given(instance=DB::ForeignKey_strategy)
@settings(max_examples=50)
def test_db::foreignkey_instantiation(instance):
    assert isinstance(instance, DB::ForeignKey)

@given(instance=DB::ForeignKey_strategy)
def test_db::foreignkey_isMany_type(instance):
    assert isinstance(instance.isMany, str)


@given(instance=DB::ForeignKey_strategy)
def test_db::foreignkey_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=DB::Column_strategy)
@settings(max_examples=50)
def test_db::column_instantiation(instance):
    assert isinstance(instance, DB::Column)

@given(instance=DB::Column_strategy)
def test_db::column_notNull_type(instance):
    assert isinstance(instance.notNull, bool)


@given(instance=DB::Column_strategy)
def test_db::column_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original

@given(instance=DB::Column_strategy)
def test_db::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=DB::Column_strategy)
def test_db::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DB::Table_strategy)
@settings(max_examples=50)
def test_db::table_instantiation(instance):
    assert isinstance(instance, DB::Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=DB::DatabaseElement_strategy)
@settings(max_examples=50)
def test_db::databaseelement_instantiation(instance):
    assert isinstance(instance, DB::DatabaseElement)

@given(instance=DB::Database_strategy)
@settings(max_examples=50)
def test_db::database_instantiation(instance):
    assert isinstance(instance, DB::Database)

@given(instance=DB::NamedElement_strategy)
@settings(max_examples=50)
def test_db::namedelement_instantiation(instance):
    assert isinstance(instance, DB::NamedElement)

@given(instance=DB::NamedElement_strategy)
def test_db::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DB::NamedElement_strategy)
def test_db::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
