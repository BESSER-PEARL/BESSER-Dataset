import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    grammarSql_Reference,
    grammarSql_ForeignKey,
    grammarSql_PrimaryKey,
    grammarSql_Column,
    grammarSql_EObject,
    grammarSql_Table,
    grammarSql_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grammarsql_reference_is_not_abstract():
    assert not inspect.isabstract(grammarSql_Reference)


def test_grammarsql_reference_constructor_exists():
    assert callable(grammarSql_Reference.__init__)


def test_grammarsql_reference_constructor_args():
    sig = inspect.signature(grammarSql_Reference.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(grammarSql_ForeignKey)


def test_grammarsql_foreignkey_constructor_exists():
    assert callable(grammarSql_ForeignKey.__init__)


def test_grammarsql_foreignkey_constructor_args():
    sig = inspect.signature(grammarSql_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql_primarykey_is_not_abstract():
    assert not inspect.isabstract(grammarSql_PrimaryKey)


def test_grammarsql_primarykey_constructor_exists():
    assert callable(grammarSql_PrimaryKey.__init__)


def test_grammarsql_primarykey_constructor_args():
    sig = inspect.signature(grammarSql_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql_column_is_not_abstract():
    assert not inspect.isabstract(grammarSql_Column)


def test_grammarsql_column_constructor_exists():
    assert callable(grammarSql_Column.__init__)


def test_grammarsql_column_constructor_args():
    sig = inspect.signature(grammarSql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_grammarsql_column_has_isNotNull():
    assert hasattr(grammarSql_Column, "isNotNull")
    descriptor = None
    for klass in grammarSql_Column.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_grammarsql_column_has_name():
    assert hasattr(grammarSql_Column, "name")
    descriptor = None
    for klass in grammarSql_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grammarsql_column_has_type():
    assert hasattr(grammarSql_Column, "type")
    descriptor = None
    for klass in grammarSql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_grammarsql_eobject_is_not_abstract():
    assert not inspect.isabstract(grammarSql_EObject)


def test_grammarsql_eobject_constructor_exists():
    assert callable(grammarSql_EObject.__init__)


def test_grammarsql_eobject_constructor_args():
    sig = inspect.signature(grammarSql_EObject.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql_table_is_not_abstract():
    assert not inspect.isabstract(grammarSql_Table)


def test_grammarsql_table_constructor_exists():
    assert callable(grammarSql_Table.__init__)


def test_grammarsql_table_constructor_args():
    sig = inspect.signature(grammarSql_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grammarsql_table_has_name():
    assert hasattr(grammarSql_Table, "name")
    descriptor = None
    for klass in grammarSql_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grammarsql_model_is_not_abstract():
    assert not inspect.isabstract(grammarSql_Model)


def test_grammarsql_model_constructor_exists():
    assert callable(grammarSql_Model.__init__)


def test_grammarsql_model_constructor_args():
    sig = inspect.signature(grammarSql_Model.__init__)
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
grammarSql_Reference_strategy = st.builds(
    grammarSql_Reference,
)
grammarSql_ForeignKey_strategy = st.builds(
    grammarSql_ForeignKey,
)
grammarSql_PrimaryKey_strategy = st.builds(
    grammarSql_PrimaryKey,
)
grammarSql_Column_strategy = st.builds(
    grammarSql_Column,
    isNotNull=
        st.booleans(),
    name=
        safe_text,
    type=
        safe_text
)
grammarSql_EObject_strategy = st.builds(
    grammarSql_EObject,
)
grammarSql_Table_strategy = st.builds(
    grammarSql_Table,
    name=
        safe_text
)
grammarSql_Model_strategy = st.builds(
    grammarSql_Model,
)

@given(instance=grammarSql_Reference_strategy)
@settings(max_examples=50)
def test_grammarsql_reference_instantiation(instance):
    assert isinstance(instance, grammarSql_Reference)

@given(instance=grammarSql_ForeignKey_strategy)
@settings(max_examples=50)
def test_grammarsql_foreignkey_instantiation(instance):
    assert isinstance(instance, grammarSql_ForeignKey)

@given(instance=grammarSql_PrimaryKey_strategy)
@settings(max_examples=50)
def test_grammarsql_primarykey_instantiation(instance):
    assert isinstance(instance, grammarSql_PrimaryKey)

@given(instance=grammarSql_Column_strategy)
@settings(max_examples=50)
def test_grammarsql_column_instantiation(instance):
    assert isinstance(instance, grammarSql_Column)



@given(instance=grammarSql_Column_strategy)
def test_grammarsql_column_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original



@given(instance=grammarSql_Column_strategy)
def test_grammarsql_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grammarSql_Column_strategy)
def test_grammarsql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=grammarSql_EObject_strategy)
@settings(max_examples=50)
def test_grammarsql_eobject_instantiation(instance):
    assert isinstance(instance, grammarSql_EObject)

@given(instance=grammarSql_Table_strategy)
@settings(max_examples=50)
def test_grammarsql_table_instantiation(instance):
    assert isinstance(instance, grammarSql_Table)



@given(instance=grammarSql_Table_strategy)
def test_grammarsql_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=grammarSql_Model_strategy)
@settings(max_examples=50)
def test_grammarsql_model_instantiation(instance):
    assert isinstance(instance, grammarSql_Model)
