import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DatabaseElement,
    DB::Type,
    DB::Table,
    NamedElement,
    DB::Column,
    DB::DatabaseElement,
    DB::Database,
    DB::NamedElement,
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



def test_db::type_is_not_abstract():
    assert not inspect.isabstract(DB::Type)


def test_db::type_constructor_exists():
    assert callable(DB::Type.__init__)


def test_db::type_constructor_args():
    sig = inspect.signature(DB::Type.__init__)
    params = list(sig.parameters.keys())



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



def test_db::column_is_not_abstract():
    assert not inspect.isabstract(DB::Column)


def test_db::column_constructor_exists():
    assert callable(DB::Column.__init__)


def test_db::column_constructor_args():
    sig = inspect.signature(DB::Column.__init__)
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
DB::Type_strategy = st.builds(
    DB::Type,
)
DB::Table_strategy = st.builds(
    DB::Table,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
DB::Column_strategy = st.builds(
    DB::Column,
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

@given(instance=DB::Type_strategy)
@settings(max_examples=50)
def test_db::type_instantiation(instance):
    assert isinstance(instance, DB::Type)

@given(instance=DB::Table_strategy)
@settings(max_examples=50)
def test_db::table_instantiation(instance):
    assert isinstance(instance, DB::Table)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=DB::Column_strategy)
@settings(max_examples=50)
def test_db::column_instantiation(instance):
    assert isinstance(instance, DB::Column)

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
