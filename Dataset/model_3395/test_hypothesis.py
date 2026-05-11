import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tables::Restaurant,
    tables::Waitress,
    tables::Chair,
    tables::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tables::restaurant_is_not_abstract():
    assert not inspect.isabstract(tables::Restaurant)


def test_tables::restaurant_constructor_exists():
    assert callable(tables::Restaurant.__init__)


def test_tables::restaurant_constructor_args():
    sig = inspect.signature(tables::Restaurant.__init__)
    params = list(sig.parameters.keys())



def test_tables::waitress_is_not_abstract():
    assert not inspect.isabstract(tables::Waitress)


def test_tables::waitress_constructor_exists():
    assert callable(tables::Waitress.__init__)


def test_tables::waitress_constructor_args():
    sig = inspect.signature(tables::Waitress.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tables::waitress_has_name():
    assert hasattr(tables::Waitress, "name")
    descriptor = None
    for klass in tables::Waitress.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tables::chair_is_not_abstract():
    assert not inspect.isabstract(tables::Chair)


def test_tables::chair_constructor_exists():
    assert callable(tables::Chair.__init__)


def test_tables::chair_constructor_args():
    sig = inspect.signature(tables::Chair.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_tables::chair_has_order():
    assert hasattr(tables::Chair, "order")
    descriptor = None
    for klass in tables::Chair.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_tables::table_is_not_abstract():
    assert not inspect.isabstract(tables::Table)


def test_tables::table_constructor_exists():
    assert callable(tables::Table.__init__)


def test_tables::table_constructor_args():
    sig = inspect.signature(tables::Table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isReserved" in params, "Missing parameter 'isReserved'"

def test_tables::table_has_id():
    assert hasattr(tables::Table, "id")
    descriptor = None
    for klass in tables::Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_tables::table_has_isReserved():
    assert hasattr(tables::Table, "isReserved")
    descriptor = None
    for klass in tables::Table.__mro__:
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
tables::Restaurant_strategy = st.builds(
    tables::Restaurant,
)
tables::Waitress_strategy = st.builds(
    tables::Waitress,
    name=
        safe_text
)
tables::Chair_strategy = st.builds(
    tables::Chair,
    order=
        st.integers()
)
tables::Table_strategy = st.builds(
    tables::Table,
    id=
        st.integers(),
    isReserved=
        st.booleans()
)

@given(instance=tables::Restaurant_strategy)
@settings(max_examples=50)
def test_tables::restaurant_instantiation(instance):
    assert isinstance(instance, tables::Restaurant)

@given(instance=tables::Waitress_strategy)
@settings(max_examples=50)
def test_tables::waitress_instantiation(instance):
    assert isinstance(instance, tables::Waitress)

@given(instance=tables::Waitress_strategy)
def test_tables::waitress_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tables::Waitress_strategy)
def test_tables::waitress_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tables::Chair_strategy)
@settings(max_examples=50)
def test_tables::chair_instantiation(instance):
    assert isinstance(instance, tables::Chair)

@given(instance=tables::Chair_strategy)
def test_tables::chair_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=tables::Chair_strategy)
def test_tables::chair_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=tables::Table_strategy)
@settings(max_examples=50)
def test_tables::table_instantiation(instance):
    assert isinstance(instance, tables::Table)

@given(instance=tables::Table_strategy)
def test_tables::table_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=tables::Table_strategy)
def test_tables::table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tables::Table_strategy)
def test_tables::table_isReserved_type(instance):
    assert isinstance(instance.isReserved, bool)


@given(instance=tables::Table_strategy)
def test_tables::table_isReserved_setter(instance):
    original = instance.isReserved
    instance.isReserved = original
    assert instance.isReserved == original
