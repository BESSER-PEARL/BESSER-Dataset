import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DatabaseElement,
    DB_Column,
    DB_ForeignKey,
    DB_Table,
    NamedElement,
    DB_DatabaseElement,
    DB_Database,
    DB_NamedElement,
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



def test_db_column_is_not_abstract():
    assert not inspect.isabstract(DB_Column)


def test_db_column_constructor_exists():
    assert callable(DB_Column.__init__)


def test_db_column_constructor_args():
    sig = inspect.signature(DB_Column.__init__)
    params = list(sig.parameters.keys())
    assert "notNull" in params, "Missing parameter 'notNull'"
    assert "type" in params, "Missing parameter 'type'"

def test_db_column_has_notNull():
    assert hasattr(DB_Column, "notNull")
    descriptor = None
    for klass in DB_Column.__mro__:
        if "notNull" in klass.__dict__:
            descriptor = klass.__dict__["notNull"]
            break
    assert isinstance(descriptor, property)

def test_db_column_has_type():
    assert hasattr(DB_Column, "type")
    descriptor = None
    for klass in DB_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_db_foreignkey_is_not_abstract():
    assert not inspect.isabstract(DB_ForeignKey)


def test_db_foreignkey_constructor_exists():
    assert callable(DB_ForeignKey.__init__)


def test_db_foreignkey_constructor_args():
    sig = inspect.signature(DB_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_db_foreignkey_has_isMany():
    assert hasattr(DB_ForeignKey, "isMany")
    descriptor = None
    for klass in DB_ForeignKey.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_db_table_is_not_abstract():
    assert not inspect.isabstract(DB_Table)


def test_db_table_constructor_exists():
    assert callable(DB_Table.__init__)


def test_db_table_constructor_args():
    sig = inspect.signature(DB_Table.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_db_databaseelement_is_not_abstract():
    assert not inspect.isabstract(DB_DatabaseElement)


def test_db_databaseelement_constructor_exists():
    assert callable(DB_DatabaseElement.__init__)


def test_db_databaseelement_constructor_args():
    sig = inspect.signature(DB_DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db_database_is_not_abstract():
    assert not inspect.isabstract(DB_Database)


def test_db_database_constructor_exists():
    assert callable(DB_Database.__init__)


def test_db_database_constructor_args():
    sig = inspect.signature(DB_Database.__init__)
    params = list(sig.parameters.keys())



def test_db_namedelement_is_not_abstract():
    assert not inspect.isabstract(DB_NamedElement)


def test_db_namedelement_constructor_exists():
    assert callable(DB_NamedElement.__init__)


def test_db_namedelement_constructor_args():
    sig = inspect.signature(DB_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_db_namedelement_has_name():
    assert hasattr(DB_NamedElement, "name")
    descriptor = None
    for klass in DB_NamedElement.__mro__:
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
        "int",
        "text",
        "varchar",
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
DB_Column_strategy = st.builds(
    DB_Column,
    notNull=
        st.booleans(),
    type=
        safe_text
)
DB_ForeignKey_strategy = st.builds(
    DB_ForeignKey,
    isMany=
        safe_text
)
DB_Table_strategy = st.builds(
    DB_Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
DB_DatabaseElement_strategy = st.builds(
    DB_DatabaseElement,
)
DB_Database_strategy = st.builds(
    DB_Database,
)
DB_NamedElement_strategy = st.builds(
    DB_NamedElement,
    name=
        safe_text
)

@given(instance=DatabaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DatabaseElement)

@given(instance=DB_Column_strategy)
@settings(max_examples=50)
def test_db_column_instantiation(instance):
    assert isinstance(instance, DB_Column)



@given(instance=DB_Column_strategy)
def test_db_column_notNull_setter(instance):
    original = instance.notNull
    instance.notNull = original
    assert instance.notNull == original



@given(instance=DB_Column_strategy)
def test_db_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DB_ForeignKey_strategy)
@settings(max_examples=50)
def test_db_foreignkey_instantiation(instance):
    assert isinstance(instance, DB_ForeignKey)



@given(instance=DB_ForeignKey_strategy)
def test_db_foreignkey_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=DB_Table_strategy)
@settings(max_examples=50)
def test_db_table_instantiation(instance):
    assert isinstance(instance, DB_Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=DB_DatabaseElement_strategy)
@settings(max_examples=50)
def test_db_databaseelement_instantiation(instance):
    assert isinstance(instance, DB_DatabaseElement)

@given(instance=DB_Database_strategy)
@settings(max_examples=50)
def test_db_database_instantiation(instance):
    assert isinstance(instance, DB_Database)

@given(instance=DB_NamedElement_strategy)
@settings(max_examples=50)
def test_db_namedelement_instantiation(instance):
    assert isinstance(instance, DB_NamedElement)



@given(instance=DB_NamedElement_strategy)
def test_db_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
