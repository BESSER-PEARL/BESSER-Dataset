import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DB::Column,
    DB::Database,
    DB::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_db::column_is_not_abstract():
    assert not inspect.isabstract(DB::Column)


def test_db::column_constructor_exists():
    assert callable(DB::Column.__init__)


def test_db::column_constructor_args():
    sig = inspect.signature(DB::Column.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db::column_has_Name():
    assert hasattr(DB::Column, "Name")
    descriptor = None
    for klass in DB::Column.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_db::database_is_not_abstract():
    assert not inspect.isabstract(DB::Database)


def test_db::database_constructor_exists():
    assert callable(DB::Database.__init__)


def test_db::database_constructor_args():
    sig = inspect.signature(DB::Database.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db::database_has_Name():
    assert hasattr(DB::Database, "Name")
    descriptor = None
    for klass in DB::Database.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_db::table_is_not_abstract():
    assert not inspect.isabstract(DB::Table)


def test_db::table_constructor_exists():
    assert callable(DB::Table.__init__)


def test_db::table_constructor_args():
    sig = inspect.signature(DB::Table.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_db::table_has_Name():
    assert hasattr(DB::Table, "Name")
    descriptor = None
    for klass in DB::Table.__mro__:
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
DB::Column_strategy = st.builds(
    DB::Column,
    Name=
        safe_text
)
DB::Database_strategy = st.builds(
    DB::Database,
    Name=
        safe_text
)
DB::Table_strategy = st.builds(
    DB::Table,
    Name=
        safe_text
)

@given(instance=DB::Column_strategy)
@settings(max_examples=50)
def test_db::column_instantiation(instance):
    assert isinstance(instance, DB::Column)

@given(instance=DB::Column_strategy)
def test_db::column_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=DB::Column_strategy)
def test_db::column_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=DB::Database_strategy)
@settings(max_examples=50)
def test_db::database_instantiation(instance):
    assert isinstance(instance, DB::Database)

@given(instance=DB::Database_strategy)
def test_db::database_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=DB::Database_strategy)
def test_db::database_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=DB::Table_strategy)
@settings(max_examples=50)
def test_db::table_instantiation(instance):
    assert isinstance(instance, DB::Table)

@given(instance=DB::Table_strategy)
def test_db::table_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=DB::Table_strategy)
def test_db::table_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
