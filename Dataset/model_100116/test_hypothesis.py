import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    database::Schema,
    database::ForeignKey,
    database::Column,
    database::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::schema_is_not_abstract():
    assert not inspect.isabstract(database::Schema)


def test_database::schema_constructor_exists():
    assert callable(database::Schema.__init__)


def test_database::schema_constructor_args():
    sig = inspect.signature(database::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database::schema_has_name():
    assert hasattr(database::Schema, "name")
    descriptor = None
    for klass in database::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_database::foreignkey_is_not_abstract():
    assert not inspect.isabstract(database::ForeignKey)


def test_database::foreignkey_constructor_exists():
    assert callable(database::ForeignKey.__init__)


def test_database::foreignkey_constructor_args():
    sig = inspect.signature(database::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_database::column_has_name():
    assert hasattr(database::Column, "name")
    descriptor = None
    for klass in database::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(database::Table)


def test_database::table_constructor_exists():
    assert callable(database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(database::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_local" in params, "Missing parameter 'is_local'"

def test_database::table_has_name():
    assert hasattr(database::Table, "name")
    descriptor = None
    for klass in database::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_database::table_has_is_local():
    assert hasattr(database::Table, "is_local")
    descriptor = None
    for klass in database::Table.__mro__:
        if "is_local" in klass.__dict__:
            descriptor = klass.__dict__["is_local"]
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
database::Schema_strategy = st.builds(
    database::Schema,
    name=
        safe_text
)
database::ForeignKey_strategy = st.builds(
    database::ForeignKey,
)
database::Column_strategy = st.builds(
    database::Column,
    name=
        safe_text,
    type=
        safe_text
)
database::Table_strategy = st.builds(
    database::Table,
    name=
        safe_text,
    is_local=
        st.booleans()
)

@given(instance=database::Schema_strategy)
@settings(max_examples=50)
def test_database::schema_instantiation(instance):
    assert isinstance(instance, database::Schema)

@given(instance=database::Schema_strategy)
def test_database::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::Schema_strategy)
def test_database::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=database::ForeignKey_strategy)
@settings(max_examples=50)
def test_database::foreignkey_instantiation(instance):
    assert isinstance(instance, database::ForeignKey)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Column_strategy)
def test_database::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::Column_strategy)
def test_database::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=database::Column_strategy)
def test_database::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=database::Column_strategy)
def test_database::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, database::Table)

@given(instance=database::Table_strategy)
def test_database::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::Table_strategy)
def test_database::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=database::Table_strategy)
def test_database::table_is_local_type(instance):
    assert isinstance(instance.is_local, bool)


@given(instance=database::Table_strategy)
def test_database::table_is_local_setter(instance):
    original = instance.is_local
    instance.is_local = original
    assert instance.is_local == original
