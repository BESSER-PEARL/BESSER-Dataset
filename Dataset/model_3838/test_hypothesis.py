import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sql_NamedElement,
    NamedElement,
    sql_Column,
    sql_Table,
    sql_SelectQuery,
    sql_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_namedelement_is_not_abstract():
    assert not inspect.isabstract(sql_NamedElement)


def test_sql_namedelement_constructor_exists():
    assert callable(sql_NamedElement.__init__)


def test_sql_namedelement_constructor_args():
    sig = inspect.signature(sql_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_namedelement_has_name():
    assert hasattr(sql_NamedElement, "name")
    descriptor = None
    for klass in sql_NamedElement.__mro__:
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



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(sql_Table)


def test_sql_table_constructor_exists():
    assert callable(sql_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(sql_Table.__init__)
    params = list(sig.parameters.keys())



def test_sql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sql_SelectQuery)


def test_sql_selectquery_constructor_exists():
    assert callable(sql_SelectQuery.__init__)


def test_sql_selectquery_constructor_args():
    sig = inspect.signature(sql_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
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
sql_NamedElement_strategy = st.builds(
    sql_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sql_Column_strategy = st.builds(
    sql_Column,
)
sql_Table_strategy = st.builds(
    sql_Table,
)
sql_SelectQuery_strategy = st.builds(
    sql_SelectQuery,
)
sql_Model_strategy = st.builds(
    sql_Model,
)

@given(instance=sql_NamedElement_strategy)
@settings(max_examples=50)
def test_sql_namedelement_instantiation(instance):
    assert isinstance(instance, sql_NamedElement)



@given(instance=sql_NamedElement_strategy)
def test_sql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sql_Column)

@given(instance=sql_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, sql_Table)

@given(instance=sql_SelectQuery_strategy)
@settings(max_examples=50)
def test_sql_selectquery_instantiation(instance):
    assert isinstance(instance, sql_SelectQuery)

@given(instance=sql_Model_strategy)
@settings(max_examples=50)
def test_sql_model_instantiation(instance):
    assert isinstance(instance, sql_Model)
