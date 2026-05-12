import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TableM_FKey,
    TableM_Column,
    TableM_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tablem_fkey_is_not_abstract():
    assert not inspect.isabstract(TableM_FKey)


def test_tablem_fkey_constructor_exists():
    assert callable(TableM_FKey.__init__)


def test_tablem_fkey_constructor_args():
    sig = inspect.signature(TableM_FKey.__init__)
    params = list(sig.parameters.keys())



def test_tablem_column_is_not_abstract():
    assert not inspect.isabstract(TableM_Column)


def test_tablem_column_constructor_exists():
    assert callable(TableM_Column.__init__)


def test_tablem_column_constructor_args():
    sig = inspect.signature(TableM_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_tablem_column_has_name():
    assert hasattr(TableM_Column, "name")
    descriptor = None
    for klass in TableM_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tablem_column_has_type():
    assert hasattr(TableM_Column, "type")
    descriptor = None
    for klass in TableM_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tablem_table_is_not_abstract():
    assert not inspect.isabstract(TableM_Table)


def test_tablem_table_constructor_exists():
    assert callable(TableM_Table.__init__)


def test_tablem_table_constructor_args():
    sig = inspect.signature(TableM_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tablem_table_has_name():
    assert hasattr(TableM_Table, "name")
    descriptor = None
    for klass in TableM_Table.__mro__:
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
TableM_FKey_strategy = st.builds(
    TableM_FKey,
)
TableM_Column_strategy = st.builds(
    TableM_Column,
    name=
        safe_text,
    type=
        safe_text
)
TableM_Table_strategy = st.builds(
    TableM_Table,
    name=
        safe_text
)

@given(instance=TableM_FKey_strategy)
@settings(max_examples=50)
def test_tablem_fkey_instantiation(instance):
    assert isinstance(instance, TableM_FKey)

@given(instance=TableM_Column_strategy)
@settings(max_examples=50)
def test_tablem_column_instantiation(instance):
    assert isinstance(instance, TableM_Column)



@given(instance=TableM_Column_strategy)
def test_tablem_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=TableM_Column_strategy)
def test_tablem_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TableM_Table_strategy)
@settings(max_examples=50)
def test_tablem_table_instantiation(instance):
    assert isinstance(instance, TableM_Table)



@given(instance=TableM_Table_strategy)
def test_tablem_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
