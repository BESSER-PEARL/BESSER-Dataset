import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbms::ForeignKey,
    rdbms::Column,
    rdbms::Table,
    rdbms::RDBMSModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms::ForeignKey)


def test_rdbms::foreignkey_constructor_exists():
    assert callable(rdbms::ForeignKey.__init__)


def test_rdbms::foreignkey_constructor_args():
    sig = inspect.signature(rdbms::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms::column_is_not_abstract():
    assert not inspect.isabstract(rdbms::Column)


def test_rdbms::column_constructor_exists():
    assert callable(rdbms::Column.__init__)


def test_rdbms::column_constructor_args():
    sig = inspect.signature(rdbms::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::column_has_type():
    assert hasattr(rdbms::Column, "type")
    descriptor = None
    for klass in rdbms::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_name():
    assert hasattr(rdbms::Column, "name")
    descriptor = None
    for klass in rdbms::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::table_is_not_abstract():
    assert not inspect.isabstract(rdbms::Table)


def test_rdbms::table_constructor_exists():
    assert callable(rdbms::Table.__init__)


def test_rdbms::table_constructor_args():
    sig = inspect.signature(rdbms::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::table_has_name():
    assert hasattr(rdbms::Table, "name")
    descriptor = None
    for klass in rdbms::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(rdbms::RDBMSModel)


def test_rdbms::rdbmsmodel_constructor_exists():
    assert callable(rdbms::RDBMSModel.__init__)


def test_rdbms::rdbmsmodel_constructor_args():
    sig = inspect.signature(rdbms::RDBMSModel.__init__)
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
rdbms::ForeignKey_strategy = st.builds(
    rdbms::ForeignKey,
)
rdbms::Column_strategy = st.builds(
    rdbms::Column,
    type=
        safe_text,
    name=
        safe_text
)
rdbms::Table_strategy = st.builds(
    rdbms::Table,
    name=
        safe_text
)
rdbms::RDBMSModel_strategy = st.builds(
    rdbms::RDBMSModel,
)

@given(instance=rdbms::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms::ForeignKey)

@given(instance=rdbms::Column_strategy)
@settings(max_examples=50)
def test_rdbms::column_instantiation(instance):
    assert isinstance(instance, rdbms::Column)

@given(instance=rdbms::Column_strategy)
def test_rdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdbms::Column_strategy)
def test_rdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbms::Column_strategy)
def test_rdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::Column_strategy)
def test_rdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::Table_strategy)
@settings(max_examples=50)
def test_rdbms::table_instantiation(instance):
    assert isinstance(instance, rdbms::Table)

@given(instance=rdbms::Table_strategy)
def test_rdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbms::Table_strategy)
def test_rdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms::RDBMSModel_strategy)
@settings(max_examples=50)
def test_rdbms::rdbmsmodel_instantiation(instance):
    assert isinstance(instance, rdbms::RDBMSModel)
