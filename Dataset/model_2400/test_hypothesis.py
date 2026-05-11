import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdb::Schema,
    Key,
    rdb::ForeignKey,
    rdb::PrimaryKey,
    rdb::Key,
    rdb::Column,
    rdb::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdb::schema_is_not_abstract():
    assert not inspect.isabstract(rdb::Schema)


def test_rdb::schema_constructor_exists():
    assert callable(rdb::Schema.__init__)


def test_rdb::schema_constructor_args():
    sig = inspect.signature(rdb::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdb::schema_has_name():
    assert hasattr(rdb::Schema, "name")
    descriptor = None
    for klass in rdb::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_rdb::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdb::ForeignKey)


def test_rdb::foreignkey_constructor_exists():
    assert callable(rdb::ForeignKey.__init__)


def test_rdb::foreignkey_constructor_args():
    sig = inspect.signature(rdb::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb::primarykey_is_not_abstract():
    assert not inspect.isabstract(rdb::PrimaryKey)


def test_rdb::primarykey_constructor_exists():
    assert callable(rdb::PrimaryKey.__init__)


def test_rdb::primarykey_constructor_args():
    sig = inspect.signature(rdb::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_rdb::key_is_not_abstract():
    assert not inspect.isabstract(rdb::Key)


def test_rdb::key_constructor_exists():
    assert callable(rdb::Key.__init__)


def test_rdb::key_constructor_args():
    sig = inspect.signature(rdb::Key.__init__)
    params = list(sig.parameters.keys())



def test_rdb::column_is_not_abstract():
    assert not inspect.isabstract(rdb::Column)


def test_rdb::column_constructor_exists():
    assert callable(rdb::Column.__init__)


def test_rdb::column_constructor_args():
    sig = inspect.signature(rdb::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdb::column_has_name():
    assert hasattr(rdb::Column, "name")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdb::column_has_type():
    assert hasattr(rdb::Column, "type")
    descriptor = None
    for klass in rdb::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdb::table_is_not_abstract():
    assert not inspect.isabstract(rdb::Table)


def test_rdb::table_constructor_exists():
    assert callable(rdb::Table.__init__)


def test_rdb::table_constructor_args():
    sig = inspect.signature(rdb::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdb::table_has_name():
    assert hasattr(rdb::Table, "name")
    descriptor = None
    for klass in rdb::Table.__mro__:
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
rdb::Schema_strategy = st.builds(
    rdb::Schema,
    name=
        safe_text
)
Key_strategy = st.builds(
    Key,
)
rdb::ForeignKey_strategy = st.builds(
    rdb::ForeignKey,
)
rdb::PrimaryKey_strategy = st.builds(
    rdb::PrimaryKey,
)
rdb::Key_strategy = st.builds(
    rdb::Key,
)
rdb::Column_strategy = st.builds(
    rdb::Column,
    name=
        safe_text,
    type=
        safe_text
)
rdb::Table_strategy = st.builds(
    rdb::Table,
    name=
        safe_text
)

@given(instance=rdb::Schema_strategy)
@settings(max_examples=50)
def test_rdb::schema_instantiation(instance):
    assert isinstance(instance, rdb::Schema)

@given(instance=rdb::Schema_strategy)
def test_rdb::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdb::Schema_strategy)
def test_rdb::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=rdb::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdb::foreignkey_instantiation(instance):
    assert isinstance(instance, rdb::ForeignKey)

@given(instance=rdb::PrimaryKey_strategy)
@settings(max_examples=50)
def test_rdb::primarykey_instantiation(instance):
    assert isinstance(instance, rdb::PrimaryKey)

@given(instance=rdb::Key_strategy)
@settings(max_examples=50)
def test_rdb::key_instantiation(instance):
    assert isinstance(instance, rdb::Key)

@given(instance=rdb::Column_strategy)
@settings(max_examples=50)
def test_rdb::column_instantiation(instance):
    assert isinstance(instance, rdb::Column)

@given(instance=rdb::Column_strategy)
def test_rdb::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdb::Column_strategy)
def test_rdb::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdb::Column_strategy)
def test_rdb::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdb::Table_strategy)
@settings(max_examples=50)
def test_rdb::table_instantiation(instance):
    assert isinstance(instance, rdb::Table)

@given(instance=rdb::Table_strategy)
def test_rdb::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdb::Table_strategy)
def test_rdb::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
