import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    Sql_Column,
    Sql_Table,
    Sql_Database,
    Sql_NamedElement,
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



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(Sql_Column)


def test_sql_column_constructor_exists():
    assert callable(Sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(Sql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sql_column_has_type():
    assert hasattr(Sql_Column, "type")
    descriptor = None
    for klass in Sql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(Sql_Table)


def test_sql_table_constructor_exists():
    assert callable(Sql_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(Sql_Table.__init__)
    params = list(sig.parameters.keys())



def test_sql_database_is_not_abstract():
    assert not inspect.isabstract(Sql_Database)


def test_sql_database_constructor_exists():
    assert callable(Sql_Database.__init__)


def test_sql_database_constructor_args():
    sig = inspect.signature(Sql_Database.__init__)
    params = list(sig.parameters.keys())



def test_sql_namedelement_is_not_abstract():
    assert not inspect.isabstract(Sql_NamedElement)


def test_sql_namedelement_constructor_exists():
    assert callable(Sql_NamedElement.__init__)


def test_sql_namedelement_constructor_args():
    sig = inspect.signature(Sql_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_namedelement_has_name():
    assert hasattr(Sql_NamedElement, "name")
    descriptor = None
    for klass in Sql_NamedElement.__mro__:
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
Sql_Column_strategy = st.builds(
    Sql_Column,
    type=
        safe_text
)
Sql_Table_strategy = st.builds(
    Sql_Table,
)
Sql_Database_strategy = st.builds(
    Sql_Database,
)
Sql_NamedElement_strategy = st.builds(
    Sql_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, Sql_Column)



@given(instance=Sql_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Sql_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, Sql_Table)

@given(instance=Sql_Database_strategy)
@settings(max_examples=50)
def test_sql_database_instantiation(instance):
    assert isinstance(instance, Sql_Database)

@given(instance=Sql_NamedElement_strategy)
@settings(max_examples=50)
def test_sql_namedelement_instantiation(instance):
    assert isinstance(instance, Sql_NamedElement)



@given(instance=Sql_NamedElement_strategy)
def test_sql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
