import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Column,
    FKey,
    RDBMS_Table,
    RDBMS_Schema,
    Table,
    RDBMS_FKey,
    RDBMS_Column,
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



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Table)


def test_rdbms_table_constructor_exists():
    assert callable(RDBMS_Table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(RDBMS_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tipo" in params, "Missing parameter 'tipo'"

def test_rdbms_table_has_name():
    assert hasattr(RDBMS_Table, "name")
    descriptor = None
    for klass in RDBMS_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_table_has_tipo():
    assert hasattr(RDBMS_Table, "tipo")
    descriptor = None
    for klass in RDBMS_Table.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_schema_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Schema)


def test_rdbms_schema_constructor_exists():
    assert callable(RDBMS_Schema.__init__)


def test_rdbms_schema_constructor_args():
    sig = inspect.signature(RDBMS_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_schema_has_name():
    assert hasattr(RDBMS_Schema, "name")
    descriptor = None
    for klass in RDBMS_Schema.__mro__:
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



def test_rdbms_fkey_is_not_abstract():
    assert not inspect.isabstract(RDBMS_FKey)


def test_rdbms_fkey_constructor_exists():
    assert callable(RDBMS_FKey.__init__)


def test_rdbms_fkey_constructor_args():
    sig = inspect.signature(RDBMS_FKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Column)


def test_rdbms_column_constructor_exists():
    assert callable(RDBMS_Column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(RDBMS_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms_column_has_name():
    assert hasattr(RDBMS_Column, "name")
    descriptor = None
    for klass in RDBMS_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_type():
    assert hasattr(RDBMS_Column, "type")
    descriptor = None
    for klass in RDBMS_Column.__mro__:
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
RDBMS_Table_strategy = st.builds(
    RDBMS_Table,
    name=
        safe_text,
    tipo=
        safe_text
)
RDBMS_Schema_strategy = st.builds(
    RDBMS_Schema,
    name=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
RDBMS_FKey_strategy = st.builds(
    RDBMS_FKey,
)
RDBMS_Column_strategy = st.builds(
    RDBMS_Column,
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

@given(instance=RDBMS_Table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, RDBMS_Table)



@given(instance=RDBMS_Table_strategy)
def test_rdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RDBMS_Table_strategy)
def test_rdbms_table_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=RDBMS_Schema_strategy)
@settings(max_examples=50)
def test_rdbms_schema_instantiation(instance):
    assert isinstance(instance, RDBMS_Schema)



@given(instance=RDBMS_Schema_strategy)
def test_rdbms_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=RDBMS_FKey_strategy)
@settings(max_examples=50)
def test_rdbms_fkey_instantiation(instance):
    assert isinstance(instance, RDBMS_FKey)

@given(instance=RDBMS_Column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, RDBMS_Column)



@given(instance=RDBMS_Column_strategy)
def test_rdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RDBMS_Column_strategy)
def test_rdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
