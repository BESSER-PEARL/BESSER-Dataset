import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TableM::FKey,
    TableM::Column,
    TableM::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tablem::fkey_is_not_abstract():
    assert not inspect.isabstract(TableM::FKey)


def test_tablem::fkey_constructor_exists():
    assert callable(TableM::FKey.__init__)


def test_tablem::fkey_constructor_args():
    sig = inspect.signature(TableM::FKey.__init__)
    params = list(sig.parameters.keys())



def test_tablem::column_is_not_abstract():
    assert not inspect.isabstract(TableM::Column)


def test_tablem::column_constructor_exists():
    assert callable(TableM::Column.__init__)


def test_tablem::column_constructor_args():
    sig = inspect.signature(TableM::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_tablem::column_has_type():
    assert hasattr(TableM::Column, "type")
    descriptor = None
    for klass in TableM::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_tablem::column_has_name():
    assert hasattr(TableM::Column, "name")
    descriptor = None
    for klass in TableM::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tablem::table_is_not_abstract():
    assert not inspect.isabstract(TableM::Table)


def test_tablem::table_constructor_exists():
    assert callable(TableM::Table.__init__)


def test_tablem::table_constructor_args():
    sig = inspect.signature(TableM::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tablem::table_has_name():
    assert hasattr(TableM::Table, "name")
    descriptor = None
    for klass in TableM::Table.__mro__:
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
TableM::FKey_strategy = st.builds(
    TableM::FKey,
)
TableM::Column_strategy = st.builds(
    TableM::Column,
    type=
        safe_text,
    name=
        safe_text
)
TableM::Table_strategy = st.builds(
    TableM::Table,
    name=
        safe_text
)

@given(instance=TableM::FKey_strategy)
@settings(max_examples=50)
def test_tablem::fkey_instantiation(instance):
    assert isinstance(instance, TableM::FKey)

@given(instance=TableM::Column_strategy)
@settings(max_examples=50)
def test_tablem::column_instantiation(instance):
    assert isinstance(instance, TableM::Column)

@given(instance=TableM::Column_strategy)
def test_tablem::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=TableM::Column_strategy)
def test_tablem::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TableM::Column_strategy)
def test_tablem::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TableM::Column_strategy)
def test_tablem::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TableM::Table_strategy)
@settings(max_examples=50)
def test_tablem::table_instantiation(instance):
    assert isinstance(instance, TableM::Table)

@given(instance=TableM::Table_strategy)
def test_tablem::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TableM::Table_strategy)
def test_tablem::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
