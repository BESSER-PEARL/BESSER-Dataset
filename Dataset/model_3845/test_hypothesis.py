import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RDBMSMM::RDBMSModel,
    RDBMSMM::FKey,
    RDBMSMM::Column,
    RDBMSMM::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm::rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM::RDBMSModel)


def test_rdbmsmm::rdbmsmodel_constructor_exists():
    assert callable(RDBMSMM::RDBMSModel.__init__)


def test_rdbmsmm::rdbmsmodel_constructor_args():
    sig = inspect.signature(RDBMSMM::RDBMSModel.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::fkey_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM::FKey)


def test_rdbmsmm::fkey_constructor_exists():
    assert callable(RDBMSMM::FKey.__init__)


def test_rdbmsmm::fkey_constructor_args():
    sig = inspect.signature(RDBMSMM::FKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::column_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM::Column)


def test_rdbmsmm::column_constructor_exists():
    assert callable(RDBMSMM::Column.__init__)


def test_rdbmsmm::column_constructor_args():
    sig = inspect.signature(RDBMSMM::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbmsmm::column_has_name():
    assert hasattr(RDBMSMM::Column, "name")
    descriptor = None
    for klass in RDBMSMM::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm::column_has_type():
    assert hasattr(RDBMSMM::Column, "type")
    descriptor = None
    for klass in RDBMSMM::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm::table_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM::Table)


def test_rdbmsmm::table_constructor_exists():
    assert callable(RDBMSMM::Table.__init__)


def test_rdbmsmm::table_constructor_args():
    sig = inspect.signature(RDBMSMM::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm::table_has_name():
    assert hasattr(RDBMSMM::Table, "name")
    descriptor = None
    for klass in RDBMSMM::Table.__mro__:
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
RDBMSMM::RDBMSModel_strategy = st.builds(
    RDBMSMM::RDBMSModel,
)
RDBMSMM::FKey_strategy = st.builds(
    RDBMSMM::FKey,
)
RDBMSMM::Column_strategy = st.builds(
    RDBMSMM::Column,
    name=
        safe_text,
    type=
        safe_text
)
RDBMSMM::Table_strategy = st.builds(
    RDBMSMM::Table,
    name=
        safe_text
)

@given(instance=RDBMSMM::RDBMSModel_strategy)
@settings(max_examples=50)
def test_rdbmsmm::rdbmsmodel_instantiation(instance):
    assert isinstance(instance, RDBMSMM::RDBMSModel)

@given(instance=RDBMSMM::FKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm::fkey_instantiation(instance):
    assert isinstance(instance, RDBMSMM::FKey)

@given(instance=RDBMSMM::Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm::column_instantiation(instance):
    assert isinstance(instance, RDBMSMM::Column)

@given(instance=RDBMSMM::Column_strategy)
def test_rdbmsmm::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMSMM::Column_strategy)
def test_rdbmsmm::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMSMM::Column_strategy)
def test_rdbmsmm::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=RDBMSMM::Column_strategy)
def test_rdbmsmm::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=RDBMSMM::Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm::table_instantiation(instance):
    assert isinstance(instance, RDBMSMM::Table)

@given(instance=RDBMSMM::Table_strategy)
def test_rdbmsmm::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMSMM::Table_strategy)
def test_rdbmsmm::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
