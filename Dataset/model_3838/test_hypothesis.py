import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sql::NamedElement,
    NamedElement,
    sql::Column,
    sql::Table,
    sql::SelectQuery,
    sql::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::namedelement_is_not_abstract():
    assert not inspect.isabstract(sql::NamedElement)


def test_sql::namedelement_constructor_exists():
    assert callable(sql::NamedElement.__init__)


def test_sql::namedelement_constructor_args():
    sig = inspect.signature(sql::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::namedelement_has_name():
    assert hasattr(sql::NamedElement, "name")
    descriptor = None
    for klass in sql::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sql::Column)


def test_sql::column_constructor_exists():
    assert callable(sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sql::Column.__init__)
    params = list(sig.parameters.keys())



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sql::Table)


def test_sql::table_constructor_exists():
    assert callable(sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sql::Table.__init__)
    params = list(sig.parameters.keys())



def test_sql::selectquery_is_not_abstract():
    assert not inspect.isabstract(sql::SelectQuery)


def test_sql::selectquery_constructor_exists():
    assert callable(sql::SelectQuery.__init__)


def test_sql::selectquery_constructor_args():
    sig = inspect.signature(sql::SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql::model_is_not_abstract():
    assert not inspect.isabstract(sql::Model)


def test_sql::model_constructor_exists():
    assert callable(sql::Model.__init__)


def test_sql::model_constructor_args():
    sig = inspect.signature(sql::Model.__init__)
    params = list(sig.parameters.keys())


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
sql::NamedElement_strategy = st.builds(
    sql::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sql::Column_strategy = st.builds(
    sql::Column,
)
sql::Table_strategy = st.builds(
    sql::Table,
)
sql::SelectQuery_strategy = st.builds(
    sql::SelectQuery,
)
sql::Model_strategy = st.builds(
    sql::Model,
)

@given(instance=sql::NamedElement_strategy)
@settings(max_examples=50)
def test_sql::namedelement_instantiation(instance):
    assert isinstance(instance, sql::NamedElement)

@given(instance=sql::NamedElement_strategy)
def test_sql::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::NamedElement_strategy)
def test_sql::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sql::Column)

@given(instance=sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sql::Table)

@given(instance=sql::SelectQuery_strategy)
@settings(max_examples=50)
def test_sql::selectquery_instantiation(instance):
    assert isinstance(instance, sql::SelectQuery)

@given(instance=sql::Model_strategy)
@settings(max_examples=50)
def test_sql::model_instantiation(instance):
    assert isinstance(instance, sql::Model)
