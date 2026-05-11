import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    table::Column,
    table::Table,
    table::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_table::column_is_not_abstract():
    assert not inspect.isabstract(table::Column)


def test_table::column_constructor_exists():
    assert callable(table::Column.__init__)


def test_table::column_constructor_args():
    sig = inspect.signature(table::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_table::column_has_type():
    assert hasattr(table::Column, "type")
    descriptor = None
    for klass in table::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_table::table_is_not_abstract():
    assert not inspect.isabstract(table::Table)


def test_table::table_constructor_exists():
    assert callable(table::Table.__init__)


def test_table::table_constructor_args():
    sig = inspect.signature(table::Table.__init__)
    params = list(sig.parameters.keys())



def test_table::namedelement_is_not_abstract():
    assert not inspect.isabstract(table::NamedElement)


def test_table::namedelement_constructor_exists():
    assert callable(table::NamedElement.__init__)


def test_table::namedelement_constructor_args():
    sig = inspect.signature(table::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_table::namedelement_has_name():
    assert hasattr(table::NamedElement, "name")
    descriptor = None
    for klass in table::NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
table::Column_strategy = st.builds(
    table::Column,
    type=
        safe_text
)
table::Table_strategy = st.builds(
    table::Table,
)
table::NamedElement_strategy = st.builds(
    table::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=table::Column_strategy)
@settings(max_examples=50)
def test_table::column_instantiation(instance):
    assert isinstance(instance, table::Column)

@given(instance=table::Column_strategy)
def test_table::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=table::Column_strategy)
def test_table::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=table::Table_strategy)
@settings(max_examples=50)
def test_table::table_instantiation(instance):
    assert isinstance(instance, table::Table)

@given(instance=table::NamedElement_strategy)
@settings(max_examples=50)
def test_table::namedelement_instantiation(instance):
    assert isinstance(instance, table::NamedElement)

@given(instance=table::NamedElement_strategy)
def test_table::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=table::NamedElement_strategy)
def test_table::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
