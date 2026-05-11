import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relational::Column,
    Relational::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(Relational::Column)


def test_relational::column_constructor_exists():
    assert callable(Relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(Relational::Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational::column_has_id():
    assert hasattr(Relational::Column, "id")
    descriptor = None
    for klass in Relational::Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_name():
    assert hasattr(Relational::Column, "name")
    descriptor = None
    for klass in Relational::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(Relational::Table)


def test_relational::table_constructor_exists():
    assert callable(Relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(Relational::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_relational::table_has_name():
    assert hasattr(Relational::Table, "name")
    descriptor = None
    for klass in Relational::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational::table_has_id():
    assert hasattr(Relational::Table, "id")
    descriptor = None
    for klass in Relational::Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
Relational::Column_strategy = st.builds(
    Relational::Column,
    id=
        safe_text,
    name=
        safe_text
)
Relational::Table_strategy = st.builds(
    Relational::Table,
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=Relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, Relational::Column)

@given(instance=Relational::Column_strategy)
def test_relational::column_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Relational::Column_strategy)
def test_relational::column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Relational::Column_strategy)
def test_relational::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Column_strategy)
def test_relational::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, Relational::Table)

@given(instance=Relational::Table_strategy)
def test_relational::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Table_strategy)
def test_relational::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Table_strategy)
def test_relational::table_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Relational::Table_strategy)
def test_relational::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
