import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    table_Column,
    table_Table,
    table_NamedElement,
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



def test_table_column_is_not_abstract():
    assert not inspect.isabstract(table_Column)


def test_table_column_constructor_exists():
    assert callable(table_Column.__init__)


def test_table_column_constructor_args():
    sig = inspect.signature(table_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_table_column_has_type():
    assert hasattr(table_Column, "type")
    descriptor = None
    for klass in table_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_table_table_is_not_abstract():
    assert not inspect.isabstract(table_Table)


def test_table_table_constructor_exists():
    assert callable(table_Table.__init__)


def test_table_table_constructor_args():
    sig = inspect.signature(table_Table.__init__)
    params = list(sig.parameters.keys())



def test_table_namedelement_is_not_abstract():
    assert not inspect.isabstract(table_NamedElement)


def test_table_namedelement_constructor_exists():
    assert callable(table_NamedElement.__init__)


def test_table_namedelement_constructor_args():
    sig = inspect.signature(table_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_table_namedelement_has_name():
    assert hasattr(table_NamedElement, "name")
    descriptor = None
    for klass in table_NamedElement.__mro__:
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
table_Column_strategy = st.builds(
    table_Column,
    type=
        safe_text
)
table_Table_strategy = st.builds(
    table_Table,
)
table_NamedElement_strategy = st.builds(
    table_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=table_Column_strategy)
@settings(max_examples=50)
def test_table_column_instantiation(instance):
    assert isinstance(instance, table_Column)



@given(instance=table_Column_strategy)
def test_table_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=table_Table_strategy)
@settings(max_examples=50)
def test_table_table_instantiation(instance):
    assert isinstance(instance, table_Table)

@given(instance=table_NamedElement_strategy)
@settings(max_examples=50)
def test_table_namedelement_instantiation(instance):
    assert isinstance(instance, table_NamedElement)



@given(instance=table_NamedElement_strategy)
def test_table_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
