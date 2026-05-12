import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    database_Column,
    database_Table,
    database_Scheme,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_column_is_not_abstract():
    assert not inspect.isabstract(database_Column)


def test_database_column_constructor_exists():
    assert callable(database_Column.__init__)


def test_database_column_constructor_args():
    sig = inspect.signature(database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "PrimaryKey" in params, "Missing parameter 'PrimaryKey'"
    assert "NotNull" in params, "Missing parameter 'NotNull'"

def test_database_column_has_name():
    assert hasattr(database_Column, "name")
    descriptor = None
    for klass in database_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_type():
    assert hasattr(database_Column, "type")
    descriptor = None
    for klass in database_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_PrimaryKey():
    assert hasattr(database_Column, "PrimaryKey")
    descriptor = None
    for klass in database_Column.__mro__:
        if "PrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["PrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_NotNull():
    assert hasattr(database_Column, "NotNull")
    descriptor = None
    for klass in database_Column.__mro__:
        if "NotNull" in klass.__dict__:
            descriptor = klass.__dict__["NotNull"]
            break
    assert isinstance(descriptor, property)



def test_database_table_is_not_abstract():
    assert not inspect.isabstract(database_Table)


def test_database_table_constructor_exists():
    assert callable(database_Table.__init__)


def test_database_table_constructor_args():
    sig = inspect.signature(database_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database_table_has_name():
    assert hasattr(database_Table, "name")
    descriptor = None
    for klass in database_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_database_scheme_is_not_abstract():
    assert not inspect.isabstract(database_Scheme)


def test_database_scheme_constructor_exists():
    assert callable(database_Scheme.__init__)


def test_database_scheme_constructor_args():
    sig = inspect.signature(database_Scheme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database_scheme_has_name():
    assert hasattr(database_Scheme, "name")
    descriptor = None
    for klass in database_Scheme.__mro__:
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
database_Column_strategy = st.builds(
    database_Column,
    name=
        safe_text,
    type=
        safe_text,
    PrimaryKey=
        st.booleans(),
    NotNull=
        st.booleans()
)
database_Table_strategy = st.builds(
    database_Table,
    name=
        safe_text
)
database_Scheme_strategy = st.builds(
    database_Scheme,
    name=
        safe_text
)

@given(instance=database_Column_strategy)
@settings(max_examples=50)
def test_database_column_instantiation(instance):
    assert isinstance(instance, database_Column)



@given(instance=database_Column_strategy)
def test_database_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=database_Column_strategy)
def test_database_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=database_Column_strategy)
def test_database_column_PrimaryKey_setter(instance):
    original = instance.PrimaryKey
    instance.PrimaryKey = original
    assert instance.PrimaryKey == original



@given(instance=database_Column_strategy)
def test_database_column_NotNull_setter(instance):
    original = instance.NotNull
    instance.NotNull = original
    assert instance.NotNull == original

@given(instance=database_Table_strategy)
@settings(max_examples=50)
def test_database_table_instantiation(instance):
    assert isinstance(instance, database_Table)



@given(instance=database_Table_strategy)
def test_database_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=database_Scheme_strategy)
@settings(max_examples=50)
def test_database_scheme_instantiation(instance):
    assert isinstance(instance, database_Scheme)



@given(instance=database_Scheme_strategy)
def test_database_scheme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
