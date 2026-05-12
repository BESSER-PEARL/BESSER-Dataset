import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DB_Column,
    DB_Database,
    DB_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_db_column_is_not_abstract():
    assert not inspect.isabstract(DB_Column)


def test_db_column_constructor_exists():
    assert callable(DB_Column.__init__)


def test_db_column_constructor_args():
    sig = inspect.signature(DB_Column.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db_column_has_Name():
    assert hasattr(DB_Column, "Name")
    descriptor = None
    for klass in DB_Column.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_db_database_is_not_abstract():
    assert not inspect.isabstract(DB_Database)


def test_db_database_constructor_exists():
    assert callable(DB_Database.__init__)


def test_db_database_constructor_args():
    sig = inspect.signature(DB_Database.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db_database_has_Name():
    assert hasattr(DB_Database, "Name")
    descriptor = None
    for klass in DB_Database.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_db_table_is_not_abstract():
    assert not inspect.isabstract(DB_Table)


def test_db_table_constructor_exists():
    assert callable(DB_Table.__init__)


def test_db_table_constructor_args():
    sig = inspect.signature(DB_Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db_table_has_Name():
    assert hasattr(DB_Table, "Name")
    descriptor = None
    for klass in DB_Table.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
DB_Column_strategy = st.builds(
    DB_Column,
    Name=
        safe_text
)
DB_Database_strategy = st.builds(
    DB_Database,
    Name=
        safe_text
)
DB_Table_strategy = st.builds(
    DB_Table,
    Name=
        safe_text
)

@given(instance=DB_Column_strategy)
@settings(max_examples=50)
def test_db_column_instantiation(instance):
    assert isinstance(instance, DB_Column)



@given(instance=DB_Column_strategy)
def test_db_column_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=DB_Database_strategy)
@settings(max_examples=50)
def test_db_database_instantiation(instance):
    assert isinstance(instance, DB_Database)



@given(instance=DB_Database_strategy)
def test_db_database_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=DB_Table_strategy)
@settings(max_examples=50)
def test_db_table_instantiation(instance):
    assert isinstance(instance, DB_Table)



@given(instance=DB_Table_strategy)
def test_db_table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
