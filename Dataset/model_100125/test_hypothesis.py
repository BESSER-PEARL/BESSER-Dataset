import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    db::DatabaseElement,
    db::Database,
    db::NamedElement,
    DatabaseElement,
    db::ForeignKey,
    db::Column,
    db::Table,
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



def test_db::databaseelement_is_not_abstract():
    assert not inspect.isabstract(db::DatabaseElement)


def test_db::databaseelement_constructor_exists():
    assert callable(db::DatabaseElement.__init__)


def test_db::databaseelement_constructor_args():
    sig = inspect.signature(db::DatabaseElement.__init__)
    params = list(sig.parameters.keys())



def test_db::database_is_not_abstract():
    assert not inspect.isabstract(db::Database)


def test_db::database_constructor_exists():
    assert callable(db::Database.__init__)


def test_db::database_constructor_args():
    sig = inspect.signature(db::Database.__init__)
    params = list(sig.parameters.keys())



def test_db::namedelement_is_not_abstract():
    assert not inspect.isabstract(db::NamedElement)


def test_db::namedelement_constructor_exists():
    assert callable(db::NamedElement.__init__)


def test_db::namedelement_constructor_args():
    sig = inspect.signature(db::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_db::namedelement_has_name():
    assert hasattr(db::NamedElement, "name")
    descriptor = None
    for klass in db::NamedElement.__mro__:
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



def test_db::foreignkey_is_not_abstract():
    assert not inspect.isabstract(db::ForeignKey)


def test_db::foreignkey_constructor_exists():
    assert callable(db::ForeignKey.__init__)


def test_db::foreignkey_constructor_args():
    sig = inspect.signature(db::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_db::foreignkey_has_isMany():
    assert hasattr(db::ForeignKey, "isMany")
    descriptor = None
    for klass in db::ForeignKey.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_db::column_is_not_abstract():
    assert not inspect.isabstract(db::Column)


def test_db::column_constructor_exists():
    assert callable(db::Column.__init__)


def test_db::column_constructor_args():
    sig = inspect.signature(db::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_db::column_has_type():
    assert hasattr(db::Column, "type")
    descriptor = None
    for klass in db::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_db::table_is_not_abstract():
    assert not inspect.isabstract(db::Table)


def test_db::table_constructor_exists():
    assert callable(db::Table.__init__)


def test_db::table_constructor_args():
    sig = inspect.signature(db::Table.__init__)
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
db::DatabaseElement_strategy = st.builds(
    db::DatabaseElement,
)
db::Database_strategy = st.builds(
    db::Database,
)
db::NamedElement_strategy = st.builds(
    db::NamedElement,
    name=
        safe_text
)
DatabaseElement_strategy = st.builds(
    DatabaseElement,
)
db::ForeignKey_strategy = st.builds(
    db::ForeignKey,
    isMany=
        safe_text
)
db::Column_strategy = st.builds(
    db::Column,
    type=
        safe_text
)
db::Table_strategy = st.builds(
    db::Table,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=db::DatabaseElement_strategy)
@settings(max_examples=50)
def test_db::databaseelement_instantiation(instance):
    assert isinstance(instance, db::DatabaseElement)

@given(instance=db::Database_strategy)
@settings(max_examples=50)
def test_db::database_instantiation(instance):
    assert isinstance(instance, db::Database)

@given(instance=db::NamedElement_strategy)
@settings(max_examples=50)
def test_db::namedelement_instantiation(instance):
    assert isinstance(instance, db::NamedElement)

@given(instance=db::NamedElement_strategy)
def test_db::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=db::NamedElement_strategy)
def test_db::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DatabaseElement_strategy)
@settings(max_examples=50)
def test_databaseelement_instantiation(instance):
    assert isinstance(instance, DatabaseElement)

@given(instance=db::ForeignKey_strategy)
@settings(max_examples=50)
def test_db::foreignkey_instantiation(instance):
    assert isinstance(instance, db::ForeignKey)

@given(instance=db::ForeignKey_strategy)
def test_db::foreignkey_isMany_type(instance):
    assert isinstance(instance.isMany, str)


@given(instance=db::ForeignKey_strategy)
def test_db::foreignkey_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=db::Column_strategy)
@settings(max_examples=50)
def test_db::column_instantiation(instance):
    assert isinstance(instance, db::Column)

@given(instance=db::Column_strategy)
def test_db::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=db::Column_strategy)
def test_db::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=db::Table_strategy)
@settings(max_examples=50)
def test_db::table_instantiation(instance):
    assert isinstance(instance, db::Table)
