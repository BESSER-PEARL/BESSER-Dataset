import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    target::Database,
    target::Column,
    target::FKey,
    target::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_target::database_is_not_abstract():
    assert not inspect.isabstract(target::Database)


def test_target::database_constructor_exists():
    assert callable(target::Database.__init__)


def test_target::database_constructor_args():
    sig = inspect.signature(target::Database.__init__)
    params = list(sig.parameters.keys())



def test_target::column_is_not_abstract():
    assert not inspect.isabstract(target::Column)


def test_target::column_constructor_exists():
    assert callable(target::Column.__init__)


def test_target::column_constructor_args():
    sig = inspect.signature(target::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_target::column_has_type():
    assert hasattr(target::Column, "type")
    descriptor = None
    for klass in target::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_target::column_has_name():
    assert hasattr(target::Column, "name")
    descriptor = None
    for klass in target::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_target::fkey_is_not_abstract():
    assert not inspect.isabstract(target::FKey)


def test_target::fkey_constructor_exists():
    assert callable(target::FKey.__init__)


def test_target::fkey_constructor_args():
    sig = inspect.signature(target::FKey.__init__)
    params = list(sig.parameters.keys())



def test_target::table_is_not_abstract():
    assert not inspect.isabstract(target::Table)


def test_target::table_constructor_exists():
    assert callable(target::Table.__init__)


def test_target::table_constructor_args():
    sig = inspect.signature(target::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_target::table_has_name():
    assert hasattr(target::Table, "name")
    descriptor = None
    for klass in target::Table.__mro__:
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
target::Database_strategy = st.builds(
    target::Database,
)
target::Column_strategy = st.builds(
    target::Column,
    type=
        safe_text,
    name=
        safe_text
)
target::FKey_strategy = st.builds(
    target::FKey,
)
target::Table_strategy = st.builds(
    target::Table,
    name=
        safe_text
)

@given(instance=target::Database_strategy)
@settings(max_examples=50)
def test_target::database_instantiation(instance):
    assert isinstance(instance, target::Database)

@given(instance=target::Column_strategy)
@settings(max_examples=50)
def test_target::column_instantiation(instance):
    assert isinstance(instance, target::Column)

@given(instance=target::Column_strategy)
def test_target::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=target::Column_strategy)
def test_target::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=target::Column_strategy)
def test_target::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=target::Column_strategy)
def test_target::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=target::FKey_strategy)
@settings(max_examples=50)
def test_target::fkey_instantiation(instance):
    assert isinstance(instance, target::FKey)

@given(instance=target::Table_strategy)
@settings(max_examples=50)
def test_target::table_instantiation(instance):
    assert isinstance(instance, target::Table)

@given(instance=target::Table_strategy)
def test_target::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=target::Table_strategy)
def test_target::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
