import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    target_Database,
    target_Column,
    target_FKey,
    target_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_target_database_is_not_abstract():
    assert not inspect.isabstract(target_Database)


def test_target_database_constructor_exists():
    assert callable(target_Database.__init__)


def test_target_database_constructor_args():
    sig = inspect.signature(target_Database.__init__)
    params = list(sig.parameters.keys())



def test_target_column_is_not_abstract():
    assert not inspect.isabstract(target_Column)


def test_target_column_constructor_exists():
    assert callable(target_Column.__init__)


def test_target_column_constructor_args():
    sig = inspect.signature(target_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_target_column_has_name():
    assert hasattr(target_Column, "name")
    descriptor = None
    for klass in target_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_target_column_has_type():
    assert hasattr(target_Column, "type")
    descriptor = None
    for klass in target_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_target_fkey_is_not_abstract():
    assert not inspect.isabstract(target_FKey)


def test_target_fkey_constructor_exists():
    assert callable(target_FKey.__init__)


def test_target_fkey_constructor_args():
    sig = inspect.signature(target_FKey.__init__)
    params = list(sig.parameters.keys())



def test_target_table_is_not_abstract():
    assert not inspect.isabstract(target_Table)


def test_target_table_constructor_exists():
    assert callable(target_Table.__init__)


def test_target_table_constructor_args():
    sig = inspect.signature(target_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_target_table_has_name():
    assert hasattr(target_Table, "name")
    descriptor = None
    for klass in target_Table.__mro__:
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
target_Database_strategy = st.builds(
    target_Database,
)
target_Column_strategy = st.builds(
    target_Column,
    name=
        safe_text,
    type=
        safe_text
)
target_FKey_strategy = st.builds(
    target_FKey,
)
target_Table_strategy = st.builds(
    target_Table,
    name=
        safe_text
)

@given(instance=target_Database_strategy)
@settings(max_examples=50)
def test_target_database_instantiation(instance):
    assert isinstance(instance, target_Database)

@given(instance=target_Column_strategy)
@settings(max_examples=50)
def test_target_column_instantiation(instance):
    assert isinstance(instance, target_Column)



@given(instance=target_Column_strategy)
def test_target_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=target_Column_strategy)
def test_target_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=target_FKey_strategy)
@settings(max_examples=50)
def test_target_fkey_instantiation(instance):
    assert isinstance(instance, target_FKey)

@given(instance=target_Table_strategy)
@settings(max_examples=50)
def test_target_table_instantiation(instance):
    assert isinstance(instance, target_Table)



@given(instance=target_Table_strategy)
def test_target_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
