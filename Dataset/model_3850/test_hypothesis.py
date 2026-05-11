import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Table,
    SimpleRDBMS::FKey,
    SimpleRDBMS::Column,
    Column,
    FKey,
    SimpleRDBMS::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::fkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::FKey)


def test_simplerdbms::fkey_constructor_exists():
    assert callable(SimpleRDBMS::FKey.__init__)


def test_simplerdbms::fkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS::FKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(SimpleRDBMS::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_simplerdbms::column_has_name():
    assert hasattr(SimpleRDBMS::Column, "name")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::column_has_type():
    assert hasattr(SimpleRDBMS::Column, "type")
    descriptor = None
    for klass in SimpleRDBMS::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_fkey_is_not_abstract():
    assert not inspect.isabstract(FKey)


def test_fkey_constructor_exists():
    assert callable(FKey.__init__)


def test_fkey_constructor_args():
    sig = inspect.signature(FKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(SimpleRDBMS::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(SimpleRDBMS::Table.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms::table_has_tipo():
    assert hasattr(SimpleRDBMS::Table, "tipo")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms::table_has_name():
    assert hasattr(SimpleRDBMS::Table, "name")
    descriptor = None
    for klass in SimpleRDBMS::Table.__mro__:
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
Table_strategy = st.builds(
    Table,
)
SimpleRDBMS::FKey_strategy = st.builds(
    SimpleRDBMS::FKey,
)
SimpleRDBMS::Column_strategy = st.builds(
    SimpleRDBMS::Column,
    name=
        safe_text,
    type=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
FKey_strategy = st.builds(
    FKey,
)
SimpleRDBMS::Table_strategy = st.builds(
    SimpleRDBMS::Table,
    tipo=
        safe_text,
    name=
        safe_text
)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SimpleRDBMS::FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::FKey)

@given(instance=SimpleRDBMS::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Column)

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SimpleRDBMS::Column_strategy)
def test_simplerdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=FKey_strategy)
@settings(max_examples=50)
def test_fkey_instantiation(instance):
    assert isinstance(instance, FKey)

@given(instance=SimpleRDBMS::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS::Table)

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_tipo_type(instance):
    assert isinstance(instance.tipo, str)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleRDBMS::Table_strategy)
def test_simplerdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
