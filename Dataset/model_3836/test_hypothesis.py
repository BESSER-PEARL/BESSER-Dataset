import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Database::Table,
    Database::DB,
    Database::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(Database::Table)


def test_database::table_constructor_exists():
    assert callable(Database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(Database::Table.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"

def test_database::table_has_heading():
    assert hasattr(Database::Table, "heading")
    descriptor = None
    for klass in Database::Table.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_database::db_is_not_abstract():
    assert not inspect.isabstract(Database::DB)


def test_database::db_constructor_exists():
    assert callable(Database::DB.__init__)


def test_database::db_constructor_args():
    sig = inspect.signature(Database::DB.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_database::db_has_title():
    assert hasattr(Database::DB, "title")
    descriptor = None
    for klass in Database::DB.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(Database::Column)


def test_database::column_constructor_exists():
    assert callable(Database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(Database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database::column_has_name():
    assert hasattr(Database::Column, "name")
    descriptor = None
    for klass in Database::Column.__mro__:
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
Database::Table_strategy = st.builds(
    Database::Table,
    heading=
        safe_text
)
Database::DB_strategy = st.builds(
    Database::DB,
    title=
        safe_text
)
Database::Column_strategy = st.builds(
    Database::Column,
    name=
        safe_text
)

@given(instance=Database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, Database::Table)

@given(instance=Database::Table_strategy)
def test_database::table_heading_type(instance):
    assert isinstance(instance.heading, str)


@given(instance=Database::Table_strategy)
def test_database::table_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=Database::DB_strategy)
@settings(max_examples=50)
def test_database::db_instantiation(instance):
    assert isinstance(instance, Database::DB)

@given(instance=Database::DB_strategy)
def test_database::db_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Database::DB_strategy)
def test_database::db_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, Database::Column)

@given(instance=Database::Column_strategy)
def test_database::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Database::Column_strategy)
def test_database::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
