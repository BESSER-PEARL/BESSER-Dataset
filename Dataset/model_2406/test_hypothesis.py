import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    database_NamedElement,
    NamedElement,
    database_Column,
    database_Table,
    database_DataBase,
    Index,
    database_Unique,
    database_PrimaryKey,
    database_Index,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_namedelement_is_not_abstract():
    assert not inspect.isabstract(database_NamedElement)


def test_database_namedelement_constructor_exists():
    assert callable(database_NamedElement.__init__)


def test_database_namedelement_constructor_args():
    sig = inspect.signature(database_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_database_namedelement_has_name():
    assert hasattr(database_NamedElement, "name")
    descriptor = None
    for klass in database_NamedElement.__mro__:
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



def test_database_column_is_not_abstract():
    assert not inspect.isabstract(database_Column)


def test_database_column_constructor_exists():
    assert callable(database_Column.__init__)


def test_database_column_constructor_args():
    sig = inspect.signature(database_Column.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "type" in params, "Missing parameter 'type'"
    assert "collation" in params, "Missing parameter 'collation'"
    assert "length" in params, "Missing parameter 'length'"

def test_database_column_has_default():
    assert hasattr(database_Column, "default")
    descriptor = None
    for klass in database_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_nullable():
    assert hasattr(database_Column, "nullable")
    descriptor = None
    for klass in database_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_type():
    assert hasattr(database_Column, "type")
    descriptor = None
    for klass in database_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_collation():
    assert hasattr(database_Column, "collation")
    descriptor = None
    for klass in database_Column.__mro__:
        if "collation" in klass.__dict__:
            descriptor = klass.__dict__["collation"]
            break
    assert isinstance(descriptor, property)

def test_database_column_has_length():
    assert hasattr(database_Column, "length")
    descriptor = None
    for klass in database_Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_database_table_is_not_abstract():
    assert not inspect.isabstract(database_Table)


def test_database_table_constructor_exists():
    assert callable(database_Table.__init__)


def test_database_table_constructor_args():
    sig = inspect.signature(database_Table.__init__)
    params = list(sig.parameters.keys())
    assert "collation" in params, "Missing parameter 'collation'"
    assert "storageEngine" in params, "Missing parameter 'storageEngine'"

def test_database_table_has_collation():
    assert hasattr(database_Table, "collation")
    descriptor = None
    for klass in database_Table.__mro__:
        if "collation" in klass.__dict__:
            descriptor = klass.__dict__["collation"]
            break
    assert isinstance(descriptor, property)

def test_database_table_has_storageEngine():
    assert hasattr(database_Table, "storageEngine")
    descriptor = None
    for klass in database_Table.__mro__:
        if "storageEngine" in klass.__dict__:
            descriptor = klass.__dict__["storageEngine"]
            break
    assert isinstance(descriptor, property)



def test_database_database_is_not_abstract():
    assert not inspect.isabstract(database_DataBase)


def test_database_database_constructor_exists():
    assert callable(database_DataBase.__init__)


def test_database_database_constructor_args():
    sig = inspect.signature(database_DataBase.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_database_unique_is_not_abstract():
    assert not inspect.isabstract(database_Unique)


def test_database_unique_constructor_exists():
    assert callable(database_Unique.__init__)


def test_database_unique_constructor_args():
    sig = inspect.signature(database_Unique.__init__)
    params = list(sig.parameters.keys())



def test_database_primarykey_is_not_abstract():
    assert not inspect.isabstract(database_PrimaryKey)


def test_database_primarykey_constructor_exists():
    assert callable(database_PrimaryKey.__init__)


def test_database_primarykey_constructor_args():
    sig = inspect.signature(database_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_database_index_is_not_abstract():
    assert not inspect.isabstract(database_Index)


def test_database_index_constructor_exists():
    assert callable(database_Index.__init__)


def test_database_index_constructor_args():
    sig = inspect.signature(database_Index.__init__)
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
database_NamedElement_strategy = st.builds(
    database_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
database_Column_strategy = st.builds(
    database_Column,
    default=
        safe_text,
    nullable=
        st.booleans(),
    type=
        safe_text,
    collation=
        safe_text,
    length=
        st.integers()
)
database_Table_strategy = st.builds(
    database_Table,
    collation=
        safe_text,
    storageEngine=
        safe_text
)
database_DataBase_strategy = st.builds(
    database_DataBase,
)
Index_strategy = st.builds(
    Index,
)
database_Unique_strategy = st.builds(
    database_Unique,
)
database_PrimaryKey_strategy = st.builds(
    database_PrimaryKey,
)
database_Index_strategy = st.builds(
    database_Index,
)

@given(instance=database_NamedElement_strategy)
@settings(max_examples=50)
def test_database_namedelement_instantiation(instance):
    assert isinstance(instance, database_NamedElement)



@given(instance=database_NamedElement_strategy)
def test_database_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=database_Column_strategy)
@settings(max_examples=50)
def test_database_column_instantiation(instance):
    assert isinstance(instance, database_Column)



@given(instance=database_Column_strategy)
def test_database_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=database_Column_strategy)
def test_database_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=database_Column_strategy)
def test_database_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=database_Column_strategy)
def test_database_column_collation_setter(instance):
    original = instance.collation
    instance.collation = original
    assert instance.collation == original



@given(instance=database_Column_strategy)
def test_database_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=database_Table_strategy)
@settings(max_examples=50)
def test_database_table_instantiation(instance):
    assert isinstance(instance, database_Table)



@given(instance=database_Table_strategy)
def test_database_table_collation_setter(instance):
    original = instance.collation
    instance.collation = original
    assert instance.collation == original



@given(instance=database_Table_strategy)
def test_database_table_storageEngine_setter(instance):
    original = instance.storageEngine
    instance.storageEngine = original
    assert instance.storageEngine == original

@given(instance=database_DataBase_strategy)
@settings(max_examples=50)
def test_database_database_instantiation(instance):
    assert isinstance(instance, database_DataBase)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=database_Unique_strategy)
@settings(max_examples=50)
def test_database_unique_instantiation(instance):
    assert isinstance(instance, database_Unique)

@given(instance=database_PrimaryKey_strategy)
@settings(max_examples=50)
def test_database_primarykey_instantiation(instance):
    assert isinstance(instance, database_PrimaryKey)

@given(instance=database_Index_strategy)
@settings(max_examples=50)
def test_database_index_instantiation(instance):
    assert isinstance(instance, database_Index)
