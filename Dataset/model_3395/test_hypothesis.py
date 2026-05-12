import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tables_Restaurant,
    tables_Waitress,
    tables_Chair,
    tables_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tables_restaurant_is_not_abstract():
    assert not inspect.isabstract(tables_Restaurant)


def test_tables_restaurant_constructor_exists():
    assert callable(tables_Restaurant.__init__)


def test_tables_restaurant_constructor_args():
    sig = inspect.signature(tables_Restaurant.__init__)
    params = list(sig.parameters.keys())



def test_tables_waitress_is_not_abstract():
    assert not inspect.isabstract(tables_Waitress)


def test_tables_waitress_constructor_exists():
    assert callable(tables_Waitress.__init__)


def test_tables_waitress_constructor_args():
    sig = inspect.signature(tables_Waitress.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables_waitress_has_name():
    assert hasattr(tables_Waitress, "name")
    descriptor = None
    for klass in tables_Waitress.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables_chair_is_not_abstract():
    assert not inspect.isabstract(tables_Chair)


def test_tables_chair_constructor_exists():
    assert callable(tables_Chair.__init__)


def test_tables_chair_constructor_args():
    sig = inspect.signature(tables_Chair.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_tables_chair_has_order():
    assert hasattr(tables_Chair, "order")
    descriptor = None
    for klass in tables_Chair.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_tables_table_is_not_abstract():
    assert not inspect.isabstract(tables_Table)


def test_tables_table_constructor_exists():
    assert callable(tables_Table.__init__)


def test_tables_table_constructor_args():
    sig = inspect.signature(tables_Table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isReserved" in params, "Missing parameter 'isReserved'"

def test_tables_table_has_id():
    assert hasattr(tables_Table, "id")
    descriptor = None
    for klass in tables_Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tables_table_has_isReserved():
    assert hasattr(tables_Table, "isReserved")
    descriptor = None
    for klass in tables_Table.__mro__:
        if "isReserved" in klass.__dict__:
            descriptor = klass.__dict__["isReserved"]
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
tables_Restaurant_strategy = st.builds(
    tables_Restaurant,
)
tables_Waitress_strategy = st.builds(
    tables_Waitress,
    name=
        safe_text
)
tables_Chair_strategy = st.builds(
    tables_Chair,
    order=
        st.integers()
)
tables_Table_strategy = st.builds(
    tables_Table,
    id=
        st.integers(),
    isReserved=
        st.booleans()
)

@given(instance=tables_Restaurant_strategy)
@settings(max_examples=50)
def test_tables_restaurant_instantiation(instance):
    assert isinstance(instance, tables_Restaurant)

@given(instance=tables_Waitress_strategy)
@settings(max_examples=50)
def test_tables_waitress_instantiation(instance):
    assert isinstance(instance, tables_Waitress)



@given(instance=tables_Waitress_strategy)
def test_tables_waitress_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables_Chair_strategy)
@settings(max_examples=50)
def test_tables_chair_instantiation(instance):
    assert isinstance(instance, tables_Chair)



@given(instance=tables_Chair_strategy)
def test_tables_chair_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=tables_Table_strategy)
@settings(max_examples=50)
def test_tables_table_instantiation(instance):
    assert isinstance(instance, tables_Table)



@given(instance=tables_Table_strategy)
def test_tables_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=tables_Table_strategy)
def test_tables_table_isReserved_setter(instance):
    original = instance.isReserved
    instance.isReserved = original
    assert instance.isReserved == original
