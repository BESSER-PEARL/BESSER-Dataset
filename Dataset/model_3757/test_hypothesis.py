import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relational_Column,
    Relational_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(Relational_Column)


def test_relational_column_constructor_exists():
    assert callable(Relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(Relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational_column_has_id():
    assert hasattr(Relational_Column, "id")
    descriptor = None
    for klass in Relational_Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_name():
    assert hasattr(Relational_Column, "name")
    descriptor = None
    for klass in Relational_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(Relational_Table)


def test_relational_table_constructor_exists():
    assert callable(Relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(Relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_relational_table_has_name():
    assert hasattr(Relational_Table, "name")
    descriptor = None
    for klass in Relational_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational_table_has_id():
    assert hasattr(Relational_Table, "id")
    descriptor = None
    for klass in Relational_Table.__mro__:
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
Relational_Column_strategy = st.builds(
    Relational_Column,
    id=
        safe_text,
    name=
        safe_text
)
Relational_Table_strategy = st.builds(
    Relational_Table,
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=Relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, Relational_Column)



@given(instance=Relational_Column_strategy)
def test_relational_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Relational_Column_strategy)
def test_relational_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, Relational_Table)



@given(instance=Relational_Table_strategy)
def test_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Relational_Table_strategy)
def test_relational_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
