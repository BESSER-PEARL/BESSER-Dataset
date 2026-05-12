import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Table,
    SimpleRDBMS_FKey,
    SimpleRDBMS_Column,
    Column,
    FKey,
    SimpleRDBMS_Table,
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



def test_simplerdbms_fkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_FKey)


def test_simplerdbms_fkey_constructor_exists():
    assert callable(SimpleRDBMS_FKey.__init__)


def test_simplerdbms_fkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_FKey.__init__)
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



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(SimpleRDBMS_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_table_has_tipo():
    assert hasattr(SimpleRDBMS_Table, "tipo")
    descriptor = None
    for klass in SimpleRDBMS_Table.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
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
Table_strategy = st.builds(
    Table,
)
SimpleRDBMS_FKey_strategy = st.builds(
    SimpleRDBMS_FKey,
)
SimpleRDBMS_Column_strategy = st.builds(
    SimpleRDBMS_Column,
    type=
        safe_text,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
FKey_strategy = st.builds(
    FKey,
)
SimpleRDBMS_Table_strategy = st.builds(
    SimpleRDBMS_Table,
    tipo=
        safe_text,
    name=
        safe_text
)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SimpleRDBMS_FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_FKey)

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

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=FKey_strategy)
@settings(max_examples=50)
def test_fkey_instantiation(instance):
    assert isinstance(instance, FKey)

@given(instance=SimpleRDBMS_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Table)



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
