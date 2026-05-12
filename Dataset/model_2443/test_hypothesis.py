import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    databaseMetamodel_Relation,
    databaseMetamodel_Database,
    databaseMetamodel_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_databasemetamodel_relation_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel_Relation)


def test_databasemetamodel_relation_constructor_exists():
    assert callable(databaseMetamodel_Relation.__init__)


def test_databasemetamodel_relation_constructor_args():
    sig = inspect.signature(databaseMetamodel_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isJoinTable" in params, "Missing parameter 'isJoinTable'"
    assert "isSelfJoinTable" in params, "Missing parameter 'isSelfJoinTable'"
    assert "name" in params, "Missing parameter 'name'"

def test_databasemetamodel_relation_has_isJoinTable():
    assert hasattr(databaseMetamodel_Relation, "isJoinTable")
    descriptor = None
    for klass in databaseMetamodel_Relation.__mro__:
        if "isJoinTable" in klass.__dict__:
            descriptor = klass.__dict__["isJoinTable"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel_relation_has_isSelfJoinTable():
    assert hasattr(databaseMetamodel_Relation, "isSelfJoinTable")
    descriptor = None
    for klass in databaseMetamodel_Relation.__mro__:
        if "isSelfJoinTable" in klass.__dict__:
            descriptor = klass.__dict__["isSelfJoinTable"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel_relation_has_name():
    assert hasattr(databaseMetamodel_Relation, "name")
    descriptor = None
    for klass in databaseMetamodel_Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_databasemetamodel_database_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel_Database)


def test_databasemetamodel_database_constructor_exists():
    assert callable(databaseMetamodel_Database.__init__)


def test_databasemetamodel_database_constructor_args():
    sig = inspect.signature(databaseMetamodel_Database.__init__)
    params = list(sig.parameters.keys())



def test_databasemetamodel_column_is_not_abstract():
    assert not inspect.isabstract(databaseMetamodel_Column)


def test_databasemetamodel_column_constructor_exists():
    assert callable(databaseMetamodel_Column.__init__)


def test_databasemetamodel_column_constructor_args():
    sig = inspect.signature(databaseMetamodel_Column.__init__)
    params = list(sig.parameters.keys())
    assert "hasPKOrder" in params, "Missing parameter 'hasPKOrder'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hasFKOrder" in params, "Missing parameter 'hasFKOrder'"

def test_databasemetamodel_column_has_hasPKOrder():
    assert hasattr(databaseMetamodel_Column, "hasPKOrder")
    descriptor = None
    for klass in databaseMetamodel_Column.__mro__:
        if "hasPKOrder" in klass.__dict__:
            descriptor = klass.__dict__["hasPKOrder"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel_column_has_type():
    assert hasattr(databaseMetamodel_Column, "type")
    descriptor = None
    for klass in databaseMetamodel_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel_column_has_name():
    assert hasattr(databaseMetamodel_Column, "name")
    descriptor = None
    for klass in databaseMetamodel_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_databasemetamodel_column_has_hasFKOrder():
    assert hasattr(databaseMetamodel_Column, "hasFKOrder")
    descriptor = None
    for klass in databaseMetamodel_Column.__mro__:
        if "hasFKOrder" in klass.__dict__:
            descriptor = klass.__dict__["hasFKOrder"]
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
databaseMetamodel_Relation_strategy = st.builds(
    databaseMetamodel_Relation,
    isJoinTable=
        st.booleans(),
    isSelfJoinTable=
        st.booleans(),
    name=
        safe_text
)
databaseMetamodel_Database_strategy = st.builds(
    databaseMetamodel_Database,
)
databaseMetamodel_Column_strategy = st.builds(
    databaseMetamodel_Column,
    hasPKOrder=
        st.integers(),
    type=
        safe_text,
    name=
        safe_text,
    hasFKOrder=
        st.integers()
)

@given(instance=databaseMetamodel_Relation_strategy)
@settings(max_examples=50)
def test_databasemetamodel_relation_instantiation(instance):
    assert isinstance(instance, databaseMetamodel_Relation)



@given(instance=databaseMetamodel_Relation_strategy)
def test_databasemetamodel_relation_isJoinTable_setter(instance):
    original = instance.isJoinTable
    instance.isJoinTable = original
    assert instance.isJoinTable == original



@given(instance=databaseMetamodel_Relation_strategy)
def test_databasemetamodel_relation_isSelfJoinTable_setter(instance):
    original = instance.isSelfJoinTable
    instance.isSelfJoinTable = original
    assert instance.isSelfJoinTable == original



@given(instance=databaseMetamodel_Relation_strategy)
def test_databasemetamodel_relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=databaseMetamodel_Database_strategy)
@settings(max_examples=50)
def test_databasemetamodel_database_instantiation(instance):
    assert isinstance(instance, databaseMetamodel_Database)

@given(instance=databaseMetamodel_Column_strategy)
@settings(max_examples=50)
def test_databasemetamodel_column_instantiation(instance):
    assert isinstance(instance, databaseMetamodel_Column)



@given(instance=databaseMetamodel_Column_strategy)
def test_databasemetamodel_column_hasPKOrder_setter(instance):
    original = instance.hasPKOrder
    instance.hasPKOrder = original
    assert instance.hasPKOrder == original



@given(instance=databaseMetamodel_Column_strategy)
def test_databasemetamodel_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=databaseMetamodel_Column_strategy)
def test_databasemetamodel_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=databaseMetamodel_Column_strategy)
def test_databasemetamodel_column_hasFKOrder_setter(instance):
    original = instance.hasFKOrder
    instance.hasFKOrder = original
    assert instance.hasFKOrder == original
