import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Column,
    FKey,
    RDBMS::Table,
    RDBMS::Schema,
    Table,
    RDBMS::FKey,
    RDBMS::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_rdbms::table_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Table)


def test_rdbms::table_constructor_exists():
    assert callable(RDBMS::Table.__init__)


def test_rdbms::table_constructor_args():
    sig = inspect.signature(RDBMS::Table.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::table_has_tipo():
    assert hasattr(RDBMS::Table, "tipo")
    descriptor = None
    for klass in RDBMS::Table.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::table_has_name():
    assert hasattr(RDBMS::Table, "name")
    descriptor = None
    for klass in RDBMS::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::schema_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Schema)


def test_rdbms::schema_constructor_exists():
    assert callable(RDBMS::Schema.__init__)


def test_rdbms::schema_constructor_args():
    sig = inspect.signature(RDBMS::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::schema_has_name():
    assert hasattr(RDBMS::Schema, "name")
    descriptor = None
    for klass in RDBMS::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::fkey_is_not_abstract():
    assert not inspect.isabstract(RDBMS::FKey)


def test_rdbms::fkey_constructor_exists():
    assert callable(RDBMS::FKey.__init__)


def test_rdbms::fkey_constructor_args():
    sig = inspect.signature(RDBMS::FKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::column_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Column)


def test_rdbms::column_constructor_exists():
    assert callable(RDBMS::Column.__init__)


def test_rdbms::column_constructor_args():
    sig = inspect.signature(RDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms::column_has_name():
    assert hasattr(RDBMS::Column, "name")
    descriptor = None
    for klass in RDBMS::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_type():
    assert hasattr(RDBMS::Column, "type")
    descriptor = None
    for klass in RDBMS::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
Column_strategy = st.builds(
    Column,
)
FKey_strategy = st.builds(
    FKey,
)
RDBMS::Table_strategy = st.builds(
    RDBMS::Table,
    tipo=
        safe_text,
    name=
        safe_text
)
RDBMS::Schema_strategy = st.builds(
    RDBMS::Schema,
    name=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
RDBMS::FKey_strategy = st.builds(
    RDBMS::FKey,
)
RDBMS::Column_strategy = st.builds(
    RDBMS::Column,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=FKey_strategy)
@settings(max_examples=50)
def test_fkey_instantiation(instance):
    assert isinstance(instance, FKey)

@given(instance=RDBMS::Table_strategy)
@settings(max_examples=50)
def test_rdbms::table_instantiation(instance):
    assert isinstance(instance, RDBMS::Table)

@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_tipo_type(instance):
    assert isinstance(instance.tipo, str)


@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Schema_strategy)
@settings(max_examples=50)
def test_rdbms::schema_instantiation(instance):
    assert isinstance(instance, RDBMS::Schema)

@given(instance=RDBMS::Schema_strategy)
def test_rdbms::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Schema_strategy)
def test_rdbms::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=RDBMS::FKey_strategy)
@settings(max_examples=50)
def test_rdbms::fkey_instantiation(instance):
    assert isinstance(instance, RDBMS::FKey)

@given(instance=RDBMS::Column_strategy)
@settings(max_examples=50)
def test_rdbms::column_instantiation(instance):
    assert isinstance(instance, RDBMS::Column)

@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
