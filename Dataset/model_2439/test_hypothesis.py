import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    Sql::Column,
    Sql::Table,
    Sql::Database,
    Sql::NamedElement,
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



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(Sql::Column)


def test_sql::column_constructor_exists():
    assert callable(Sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(Sql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sql::column_has_type():
    assert hasattr(Sql::Column, "type")
    descriptor = None
    for klass in Sql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(Sql::Table)


def test_sql::table_constructor_exists():
    assert callable(Sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(Sql::Table.__init__)
    params = list(sig.parameters.keys())



def test_sql::database_is_not_abstract():
    assert not inspect.isabstract(Sql::Database)


def test_sql::database_constructor_exists():
    assert callable(Sql::Database.__init__)


def test_sql::database_constructor_args():
    sig = inspect.signature(Sql::Database.__init__)
    params = list(sig.parameters.keys())



def test_sql::namedelement_is_not_abstract():
    assert not inspect.isabstract(Sql::NamedElement)


def test_sql::namedelement_constructor_exists():
    assert callable(Sql::NamedElement.__init__)


def test_sql::namedelement_constructor_args():
    sig = inspect.signature(Sql::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::namedelement_has_name():
    assert hasattr(Sql::NamedElement, "name")
    descriptor = None
    for klass in Sql::NamedElement.__mro__:
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
Sql::Column_strategy = st.builds(
    Sql::Column,
    type=
        safe_text
)
Sql::Table_strategy = st.builds(
    Sql::Table,
)
Sql::Database_strategy = st.builds(
    Sql::Database,
)
Sql::NamedElement_strategy = st.builds(
    Sql::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, Sql::Column)

@given(instance=Sql::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Sql::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, Sql::Table)

@given(instance=Sql::Database_strategy)
@settings(max_examples=50)
def test_sql::database_instantiation(instance):
    assert isinstance(instance, Sql::Database)

@given(instance=Sql::NamedElement_strategy)
@settings(max_examples=50)
def test_sql::namedelement_instantiation(instance):
    assert isinstance(instance, Sql::NamedElement)

@given(instance=Sql::NamedElement_strategy)
def test_sql::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Sql::NamedElement_strategy)
def test_sql::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
