import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    sql_Column,
    sql_Table,
    sql_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sql_column_has_type():
    assert hasattr(sql_Column, "type")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(sql_Table)


def test_sql_table_constructor_exists():
    assert callable(sql_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(sql_Table.__init__)
    params = list(sig.parameters.keys())



def test_sql_element_is_not_abstract():
    assert not inspect.isabstract(sql_Element)


def test_sql_element_constructor_exists():
    assert callable(sql_Element.__init__)


def test_sql_element_constructor_args():
    sig = inspect.signature(sql_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_element_has_name():
    assert hasattr(sql_Element, "name")
    descriptor = None
    for klass in sql_Element.__mro__:
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
Element_strategy = st.builds(
    Element,
)
sql_Column_strategy = st.builds(
    sql_Column,
    type=
        safe_text
)
sql_Table_strategy = st.builds(
    sql_Table,
)
sql_Element_strategy = st.builds(
    sql_Element,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sql_Column)



@given(instance=sql_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, sql_Table)

@given(instance=sql_Element_strategy)
@settings(max_examples=50)
def test_sql_element_instantiation(instance):
    assert isinstance(instance, sql_Element)



@given(instance=sql_Element_strategy)
def test_sql_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
