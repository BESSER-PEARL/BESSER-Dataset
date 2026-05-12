import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Key,
    rdb_ForeignKey,
    rdb_PrimaryKey,
    rdb_Key,
    rdb_Column,
    rdb_Table,
    rdb_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_rdb_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdb_ForeignKey)


def test_rdb_foreignkey_constructor_exists():
    assert callable(rdb_ForeignKey.__init__)


def test_rdb_foreignkey_constructor_args():
    sig = inspect.signature(rdb_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb_primarykey_is_not_abstract():
    assert not inspect.isabstract(rdb_PrimaryKey)


def test_rdb_primarykey_constructor_exists():
    assert callable(rdb_PrimaryKey.__init__)


def test_rdb_primarykey_constructor_args():
    sig = inspect.signature(rdb_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb_key_is_not_abstract():
    assert not inspect.isabstract(rdb_Key)


def test_rdb_key_constructor_exists():
    assert callable(rdb_Key.__init__)


def test_rdb_key_constructor_args():
    sig = inspect.signature(rdb_Key.__init__)
    params = list(sig.parameters.keys())



def test_rdb_column_is_not_abstract():
    assert not inspect.isabstract(rdb_Column)


def test_rdb_column_constructor_exists():
    assert callable(rdb_Column.__init__)


def test_rdb_column_constructor_args():
    sig = inspect.signature(rdb_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdb_column_has_name():
    assert hasattr(rdb_Column, "name")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdb_column_has_type():
    assert hasattr(rdb_Column, "type")
    descriptor = None
    for klass in rdb_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdb_table_is_not_abstract():
    assert not inspect.isabstract(rdb_Table)


def test_rdb_table_constructor_exists():
    assert callable(rdb_Table.__init__)


def test_rdb_table_constructor_args():
    sig = inspect.signature(rdb_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdb_table_has_name():
    assert hasattr(rdb_Table, "name")
    descriptor = None
    for klass in rdb_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdb_schema_is_not_abstract():
    assert not inspect.isabstract(rdb_Schema)


def test_rdb_schema_constructor_exists():
    assert callable(rdb_Schema.__init__)


def test_rdb_schema_constructor_args():
    sig = inspect.signature(rdb_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdb_schema_has_name():
    assert hasattr(rdb_Schema, "name")
    descriptor = None
    for klass in rdb_Schema.__mro__:
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
Key_strategy = st.builds(
    Key,
)
rdb_ForeignKey_strategy = st.builds(
    rdb_ForeignKey,
)
rdb_PrimaryKey_strategy = st.builds(
    rdb_PrimaryKey,
)
rdb_Key_strategy = st.builds(
    rdb_Key,
)
rdb_Column_strategy = st.builds(
    rdb_Column,
    name=
        safe_text,
    type=
        safe_text
)
rdb_Table_strategy = st.builds(
    rdb_Table,
    name=
        safe_text
)
rdb_Schema_strategy = st.builds(
    rdb_Schema,
    name=
        safe_text
)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=rdb_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdb_foreignkey_instantiation(instance):
    assert isinstance(instance, rdb_ForeignKey)

@given(instance=rdb_PrimaryKey_strategy)
@settings(max_examples=50)
def test_rdb_primarykey_instantiation(instance):
    assert isinstance(instance, rdb_PrimaryKey)

@given(instance=rdb_Key_strategy)
@settings(max_examples=50)
def test_rdb_key_instantiation(instance):
    assert isinstance(instance, rdb_Key)

@given(instance=rdb_Column_strategy)
@settings(max_examples=50)
def test_rdb_column_instantiation(instance):
    assert isinstance(instance, rdb_Column)



@given(instance=rdb_Column_strategy)
def test_rdb_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rdb_Column_strategy)
def test_rdb_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdb_Table_strategy)
@settings(max_examples=50)
def test_rdb_table_instantiation(instance):
    assert isinstance(instance, rdb_Table)



@given(instance=rdb_Table_strategy)
def test_rdb_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdb_Schema_strategy)
@settings(max_examples=50)
def test_rdb_schema_instantiation(instance):
    assert isinstance(instance, rdb_Schema)



@given(instance=rdb_Schema_strategy)
def test_rdb_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
