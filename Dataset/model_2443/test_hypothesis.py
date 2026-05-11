import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    databaseMetamodel::Relation,
    databaseMetamodel::Database,
    databaseMetamodel::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_databasemetamodel::relation_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel::Relation)


def test_databasemetamodel::relation_constructor_exists():
    assert callable(databaseMetamodel::Relation.__init__)


def test_databasemetamodel::relation_constructor_args():
    sig = inspect.signature(databaseMetamodel::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isSelfJoinTable" in params, "Missing parameter 'isSelfJoinTable'"
    assert "isJoinTable" in params, "Missing parameter 'isJoinTable'"
    assert "name" in params, "Missing parameter 'name'"

def test_databasemetamodel::relation_has_isSelfJoinTable():
    assert hasattr(databaseMetamodel::Relation, "isSelfJoinTable")
    descriptor = None
    for klass in databaseMetamodel::Relation.__mro__:
        if "isSelfJoinTable" in klass.__dict__:
            descriptor = klass.__dict__["isSelfJoinTable"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel::relation_has_isJoinTable():
    assert hasattr(databaseMetamodel::Relation, "isJoinTable")
    descriptor = None
    for klass in databaseMetamodel::Relation.__mro__:
        if "isJoinTable" in klass.__dict__:
            descriptor = klass.__dict__["isJoinTable"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel::relation_has_name():
    assert hasattr(databaseMetamodel::Relation, "name")
    descriptor = None
    for klass in databaseMetamodel::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_databasemetamodel::database_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel::Database)


def test_databasemetamodel::database_constructor_exists():
    assert callable(databaseMetamodel::Database.__init__)


def test_databasemetamodel::database_constructor_args():
    sig = inspect.signature(databaseMetamodel::Database.__init__)
    params = list(sig.parameters.keys())



def test_databasemetamodel::column_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel::Column)


def test_databasemetamodel::column_constructor_exists():
    assert callable(databaseMetamodel::Column.__init__)


def test_databasemetamodel::column_constructor_args():
    sig = inspect.signature(databaseMetamodel::Column.__init__)
    params = list(sig.parameters.keys())
    assert "hasFKOrder" in params, "Missing parameter 'hasFKOrder'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hasPKOrder" in params, "Missing parameter 'hasPKOrder'"

def test_databasemetamodel::column_has_hasFKOrder():
    assert hasattr(databaseMetamodel::Column, "hasFKOrder")
    descriptor = None
    for klass in databaseMetamodel::Column.__mro__:
        if "hasFKOrder" in klass.__dict__:
            descriptor = klass.__dict__["hasFKOrder"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel::column_has_type():
    assert hasattr(databaseMetamodel::Column, "type")
    descriptor = None
    for klass in databaseMetamodel::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel::column_has_name():
    assert hasattr(databaseMetamodel::Column, "name")
    descriptor = None
    for klass in databaseMetamodel::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel::column_has_hasPKOrder():
    assert hasattr(databaseMetamodel::Column, "hasPKOrder")
    descriptor = None
    for klass in databaseMetamodel::Column.__mro__:
        if "hasPKOrder" in klass.__dict__:
            descriptor = klass.__dict__["hasPKOrder"]
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
databaseMetamodel::Relation_strategy = st.builds(
    databaseMetamodel::Relation,
    isSelfJoinTable=
        st.booleans(),
    isJoinTable=
        st.booleans(),
    name=
        safe_text
)
databaseMetamodel::Database_strategy = st.builds(
    databaseMetamodel::Database,
)
databaseMetamodel::Column_strategy = st.builds(
    databaseMetamodel::Column,
    hasFKOrder=
        st.integers(),
    type=
        safe_text,
    name=
        safe_text,
    hasPKOrder=
        st.integers()
)

@given(instance=databaseMetamodel::Relation_strategy)
@settings(max_examples=50)
def test_databasemetamodel::relation_instantiation(instance):
    assert isinstance(instance, databaseMetamodel::Relation)

@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_isSelfJoinTable_type(instance):
    assert isinstance(instance.isSelfJoinTable, bool)


@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_isSelfJoinTable_setter(instance):
    original = instance.isSelfJoinTable
    instance.isSelfJoinTable = original
    assert instance.isSelfJoinTable == original

@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_isJoinTable_type(instance):
    assert isinstance(instance.isJoinTable, bool)


@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_isJoinTable_setter(instance):
    original = instance.isJoinTable
    instance.isJoinTable = original
    assert instance.isJoinTable == original

@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=databaseMetamodel::Relation_strategy)
def test_databasemetamodel::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=databaseMetamodel::Database_strategy)
@settings(max_examples=50)
def test_databasemetamodel::database_instantiation(instance):
    assert isinstance(instance, databaseMetamodel::Database)

@given(instance=databaseMetamodel::Column_strategy)
@settings(max_examples=50)
def test_databasemetamodel::column_instantiation(instance):
    assert isinstance(instance, databaseMetamodel::Column)

@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_hasFKOrder_type(instance):
    assert isinstance(instance.hasFKOrder, int)


@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_hasFKOrder_setter(instance):
    original = instance.hasFKOrder
    instance.hasFKOrder = original
    assert instance.hasFKOrder == original

@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_hasPKOrder_type(instance):
    assert isinstance(instance.hasPKOrder, int)


@given(instance=databaseMetamodel::Column_strategy)
def test_databasemetamodel::column_hasPKOrder_setter(instance):
    original = instance.hasPKOrder
    instance.hasPKOrder = original
    assert instance.hasPKOrder == original
