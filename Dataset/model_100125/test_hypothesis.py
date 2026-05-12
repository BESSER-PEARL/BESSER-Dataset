import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    db_DatabaseElement,
    db_Database,
    db_NamedElement,
    DatabaseElement,
    db_Column,
    db_ForeignKey,
    db_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_db_databaseelement_is_not_abstract():
    assert not inspect.isabstract(db_DatabaseElement)


def test_db_databaseelement_constructor_exists():
    assert callable(db_DatabaseElement.__init__)


def test_db_databaseelement_constructor_args():
    sig = inspect.signature(db_DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db_database_is_not_abstract():
    assert not inspect.isabstract(db_Database)


def test_db_database_constructor_exists():
    assert callable(db_Database.__init__)


def test_db_database_constructor_args():
    sig = inspect.signature(db_Database.__init__)
    params = list(sig.parameters.keys())



def test_db_namedelement_is_not_abstract():
    assert not inspect.isabstract(db_NamedElement)


def test_db_namedelement_constructor_exists():
    assert callable(db_NamedElement.__init__)


def test_db_namedelement_constructor_args():
    sig = inspect.signature(db_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_db_namedelement_has_name():
    assert hasattr(db_NamedElement, "name")
    descriptor = None
    for klass in db_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_databaseelement_is_not_abstract():
    assert not inspect.isabstract(DatabaseElement)


def test_databaseelement_constructor_exists():
    assert callable(DatabaseElement.__init__)


def test_databaseelement_constructor_args():
    sig = inspect.signature(DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db_column_is_not_abstract():
    assert not inspect.isabstract(db_Column)


def test_db_column_constructor_exists():
    assert callable(db_Column.__init__)


def test_db_column_constructor_args():
    sig = inspect.signature(db_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_db_column_has_type():
    assert hasattr(db_Column, "type")
    descriptor = None
    for klass in db_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_db_foreignkey_is_not_abstract():
    assert not inspect.isabstract(db_ForeignKey)


def test_db_foreignkey_constructor_exists():
    assert callable(db_ForeignKey.__init__)


def test_db_foreignkey_constructor_args():
    sig = inspect.signature(db_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_db_foreignkey_has_isMany():
    assert hasattr(db_ForeignKey, "isMany")
    descriptor = None
    for klass in db_ForeignKey.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_db_table_is_not_abstract():
    assert not inspect.isabstract(db_Table)


def test_db_table_constructor_exists():
    assert callable(db_Table.__init__)


def test_db_table_constructor_args():
    sig = inspect.signature(db_Table.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
db_DatabaseElement_strategy = st.builds(
    db_DatabaseElement,
)
db_Database_strategy = st.builds(
    db_Database,
)
db_NamedElement_strategy = st.builds(
    db_NamedElement,
    name=
        safe_text
)
DatabaseElement_strategy = st.builds(
    DatabaseElement,
)
db_Column_strategy = st.builds(
    db_Column,
    type=
        safe_text
)
db_ForeignKey_strategy = st.builds(
    db_ForeignKey,
    isMany=
        safe_text
)
db_Table_strategy = st.builds(
    db_Table,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=db_DatabaseElement_strategy)
@settings(max_examples=50)
def test_db_databaseelement_instantiation(instance):
    assert isinstance(instance, db_DatabaseElement)

@given(instance=db_Database_strategy)
@settings(max_examples=50)
def test_db_database_instantiation(instance):
    assert isinstance(instance, db_Database)

@given(instance=db_NamedElement_strategy)
@settings(max_examples=50)
def test_db_namedelement_instantiation(instance):
    assert isinstance(instance, db_NamedElement)



@given(instance=db_NamedElement_strategy)
def test_db_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatabaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DatabaseElement)

@given(instance=db_Column_strategy)
@settings(max_examples=50)
def test_db_column_instantiation(instance):
    assert isinstance(instance, db_Column)



@given(instance=db_Column_strategy)
def test_db_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=db_ForeignKey_strategy)
@settings(max_examples=50)
def test_db_foreignkey_instantiation(instance):
    assert isinstance(instance, db_ForeignKey)



@given(instance=db_ForeignKey_strategy)
def test_db_foreignkey_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=db_Table_strategy)
@settings(max_examples=50)
def test_db_table_instantiation(instance):
    assert isinstance(instance, db_Table)
