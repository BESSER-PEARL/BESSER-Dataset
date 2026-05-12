import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleRDBMS_Database,
    SimpleRDBMS_Column,
    SimpleRDBMS_FKey,
    SimpleRDBMS_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms_database_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Database)


def test_simplerdbms_database_constructor_exists():
    assert callable(SimpleRDBMS_Database.__init__)


def test_simplerdbms_database_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Database.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(SimpleRDBMS_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_simplerdbms_column_has_type():
    assert hasattr(SimpleRDBMS_Column, "type")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_column_has_name():
    assert hasattr(SimpleRDBMS_Column, "name")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_column_has_id():
    assert hasattr(SimpleRDBMS_Column, "id")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_fkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_FKey)


def test_simplerdbms_fkey_constructor_exists():
    assert callable(SimpleRDBMS_FKey.__init__)


def test_simplerdbms_fkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_FKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(SimpleRDBMS_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_table_has_id():
    assert hasattr(SimpleRDBMS_Table, "id")
    descriptor = None
    for klass in SimpleRDBMS_Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_table_has_name():
    assert hasattr(SimpleRDBMS_Table, "name")
    descriptor = None
    for klass in SimpleRDBMS_Table.__mro__:
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
SimpleRDBMS_Database_strategy = st.builds(
    SimpleRDBMS_Database,
)
SimpleRDBMS_Column_strategy = st.builds(
    SimpleRDBMS_Column,
    type=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)
SimpleRDBMS_FKey_strategy = st.builds(
    SimpleRDBMS_FKey,
)
SimpleRDBMS_Table_strategy = st.builds(
    SimpleRDBMS_Table,
    id=
        st.integers(),
    name=
        safe_text
)

@given(instance=SimpleRDBMS_Database_strategy)
@settings(max_examples=50)
def test_simplerdbms_database_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Database)

@given(instance=SimpleRDBMS_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Column)



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS_FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_FKey)

@given(instance=SimpleRDBMS_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Table)



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
