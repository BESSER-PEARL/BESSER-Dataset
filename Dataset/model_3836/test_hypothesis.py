import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Database_Table,
    Database_DB,
    Database_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_table_is_not_abstract():
    assert not inspect.isabstract(Database_Table)


def test_database_table_constructor_exists():
    assert callable(Database_Table.__init__)


def test_database_table_constructor_args():
    sig = inspect.signature(Database_Table.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"

def test_database_table_has_heading():
    assert hasattr(Database_Table, "heading")
    descriptor = None
    for klass in Database_Table.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_database_db_is_not_abstract():
    assert not inspect.isabstract(Database_DB)


def test_database_db_constructor_exists():
    assert callable(Database_DB.__init__)


def test_database_db_constructor_args():
    sig = inspect.signature(Database_DB.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_database_db_has_title():
    assert hasattr(Database_DB, "title")
    descriptor = None
    for klass in Database_DB.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_database_column_is_not_abstract():
    assert not inspect.isabstract(Database_Column)


def test_database_column_constructor_exists():
    assert callable(Database_Column.__init__)


def test_database_column_constructor_args():
    sig = inspect.signature(Database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database_column_has_name():
    assert hasattr(Database_Column, "name")
    descriptor = None
    for klass in Database_Column.__mro__:
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
Database_Table_strategy = st.builds(
    Database_Table,
    heading=
        safe_text
)
Database_DB_strategy = st.builds(
    Database_DB,
    title=
        safe_text
)
Database_Column_strategy = st.builds(
    Database_Column,
    name=
        safe_text
)

@given(instance=Database_Table_strategy)
@settings(max_examples=50)
def test_database_table_instantiation(instance):
    assert isinstance(instance, Database_Table)



@given(instance=Database_Table_strategy)
def test_database_table_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=Database_DB_strategy)
@settings(max_examples=50)
def test_database_db_instantiation(instance):
    assert isinstance(instance, Database_DB)



@given(instance=Database_DB_strategy)
def test_database_db_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Database_Column_strategy)
@settings(max_examples=50)
def test_database_column_instantiation(instance):
    assert isinstance(instance, Database_Column)



@given(instance=Database_Column_strategy)
def test_database_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
