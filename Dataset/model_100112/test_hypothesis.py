import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    database::Column,
    database::Table,
    database::Scheme,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())
    assert "NotNull" in params, "Missing parameter 'NotNull'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "PrimaryKey" in params, "Missing parameter 'PrimaryKey'"

def test_database::column_has_NotNull():
    assert hasattr(database::Column, "NotNull")
    descriptor = None
    for klass in database::Column.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)

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

def test_database::column_has_PrimaryKey():
    assert hasattr(database::Column, "PrimaryKey")
    descriptor = None
    for klass in database::Column.__mro__:
        if "PrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["PrimaryKey"]
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

def test_database::table_has_name():
    assert hasattr(database::Table, "name")
    descriptor = None
    for klass in database::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_database::scheme_is_not_abstract():
    assert not inspect.isabstract(database::Scheme)


def test_database::scheme_constructor_exists():
    assert callable(database::Scheme.__init__)


def test_database::scheme_constructor_args():
    sig = inspect.signature(database::Scheme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database::scheme_has_name():
    assert hasattr(database::Scheme, "name")
    descriptor = None
    for klass in database::Scheme.__mro__:
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
database::Column_strategy = st.builds(
    database::Column,
    NotNull=
        st.booleans(),
    name=
        safe_text,
    type=
        safe_text,
    PrimaryKey=
        st.booleans()
)
database::Table_strategy = st.builds(
    database::Table,
    name=
        safe_text
)
database::Scheme_strategy = st.builds(
    database::Scheme,
    name=
        safe_text
)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Column_strategy)
def test_database::column_NotNull_type(instance):
    assert isinstance(instance.NotNull, bool)


@given(instance=database::Column_strategy)
def test_database::column_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

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

@given(instance=database::Column_strategy)
def test_database::column_PrimaryKey_type(instance):
    assert isinstance(instance.PrimaryKey, bool)


@given(instance=database::Column_strategy)
def test_database::column_PrimaryKey_setter(instance):
    original = instance.PrimaryKey
    instance.PrimaryKey = original
    assert instance.PrimaryKey == original

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

@given(instance=database::Scheme_strategy)
@settings(max_examples=50)
def test_database::scheme_instantiation(instance):
    assert isinstance(instance, database::Scheme)

@given(instance=database::Scheme_strategy)
def test_database::scheme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=database::Scheme_strategy)
def test_database::scheme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
