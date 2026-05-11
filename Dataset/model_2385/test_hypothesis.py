import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    sql::Column,
    sql::Table,
    sql::Element,
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



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sql::Column)


def test_sql::column_constructor_exists():
    assert callable(sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sql::column_has_type():
    assert hasattr(sql::Column, "type")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sql::Table)


def test_sql::table_constructor_exists():
    assert callable(sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sql::Table.__init__)
    params = list(sig.parameters.keys())



def test_sql::element_is_not_abstract():
    assert not inspect.isabstract(sql::Element)


def test_sql::element_constructor_exists():
    assert callable(sql::Element.__init__)


def test_sql::element_constructor_args():
    sig = inspect.signature(sql::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::element_has_name():
    assert hasattr(sql::Element, "name")
    descriptor = None
    for klass in sql::Element.__mro__:
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
sql::Column_strategy = st.builds(
    sql::Column,
    type=
        safe_text
)
sql::Table_strategy = st.builds(
    sql::Table,
)
sql::Element_strategy = st.builds(
    sql::Element,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sql::Column)

@given(instance=sql::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sql::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sql::Table)

@given(instance=sql::Element_strategy)
@settings(max_examples=50)
def test_sql::element_instantiation(instance):
    assert isinstance(instance, sql::Element)

@given(instance=sql::Element_strategy)
def test_sql::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::Element_strategy)
def test_sql::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
