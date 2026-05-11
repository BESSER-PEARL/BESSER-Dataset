import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    grammarSql::Reference,
    grammarSql::ForeignKey,
    grammarSql::PrimaryKey,
    grammarSql::Column,
    grammarSql::EObject,
    grammarSql::Table,
    grammarSql::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grammarsql::reference_is_not_abstract():
    assert not inspect.isabstract(grammarSql::Reference)


def test_grammarsql::reference_constructor_exists():
    assert callable(grammarSql::Reference.__init__)


def test_grammarsql::reference_constructor_args():
    sig = inspect.signature(grammarSql::Reference.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(grammarSql::ForeignKey)


def test_grammarsql::foreignkey_constructor_exists():
    assert callable(grammarSql::ForeignKey.__init__)


def test_grammarsql::foreignkey_constructor_args():
    sig = inspect.signature(grammarSql::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql::primarykey_is_not_abstract():
    assert not inspect.isabstract(grammarSql::PrimaryKey)


def test_grammarsql::primarykey_constructor_exists():
    assert callable(grammarSql::PrimaryKey.__init__)


def test_grammarsql::primarykey_constructor_args():
    sig = inspect.signature(grammarSql::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql::column_is_not_abstract():
    assert not inspect.isabstract(grammarSql::Column)


def test_grammarsql::column_constructor_exists():
    assert callable(grammarSql::Column.__init__)


def test_grammarsql::column_constructor_args():
    sig = inspect.signature(grammarSql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "name" in params, "Missing parameter 'name'"

def test_grammarsql::column_has_type():
    assert hasattr(grammarSql::Column, "type")
    descriptor = None
    for klass in grammarSql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grammarsql::column_has_isNotNull():
    assert hasattr(grammarSql::Column, "isNotNull")
    descriptor = None
    for klass in grammarSql::Column.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_grammarsql::column_has_name():
    assert hasattr(grammarSql::Column, "name")
    descriptor = None
    for klass in grammarSql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grammarsql::eobject_is_not_abstract():
    assert not inspect.isabstract(grammarSql::EObject)


def test_grammarsql::eobject_constructor_exists():
    assert callable(grammarSql::EObject.__init__)


def test_grammarsql::eobject_constructor_args():
    sig = inspect.signature(grammarSql::EObject.__init__)
    params = list(sig.parameters.keys())



def test_grammarsql::table_is_not_abstract():
    assert not inspect.isabstract(grammarSql::Table)


def test_grammarsql::table_constructor_exists():
    assert callable(grammarSql::Table.__init__)


def test_grammarsql::table_constructor_args():
    sig = inspect.signature(grammarSql::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grammarsql::table_has_name():
    assert hasattr(grammarSql::Table, "name")
    descriptor = None
    for klass in grammarSql::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grammarsql::model_is_not_abstract():
    assert not inspect.isabstract(grammarSql::Model)


def test_grammarsql::model_constructor_exists():
    assert callable(grammarSql::Model.__init__)


def test_grammarsql::model_constructor_args():
    sig = inspect.signature(grammarSql::Model.__init__)
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
grammarSql::Reference_strategy = st.builds(
    grammarSql::Reference,
)
grammarSql::ForeignKey_strategy = st.builds(
    grammarSql::ForeignKey,
)
grammarSql::PrimaryKey_strategy = st.builds(
    grammarSql::PrimaryKey,
)
grammarSql::Column_strategy = st.builds(
    grammarSql::Column,
    type=
        safe_text,
    isNotNull=
        st.booleans(),
    name=
        safe_text
)
grammarSql::EObject_strategy = st.builds(
    grammarSql::EObject,
)
grammarSql::Table_strategy = st.builds(
    grammarSql::Table,
    name=
        safe_text
)
grammarSql::Model_strategy = st.builds(
    grammarSql::Model,
)

@given(instance=grammarSql::Reference_strategy)
@settings(max_examples=50)
def test_grammarsql::reference_instantiation(instance):
    assert isinstance(instance, grammarSql::Reference)

@given(instance=grammarSql::ForeignKey_strategy)
@settings(max_examples=50)
def test_grammarsql::foreignkey_instantiation(instance):
    assert isinstance(instance, grammarSql::ForeignKey)

@given(instance=grammarSql::PrimaryKey_strategy)
@settings(max_examples=50)
def test_grammarsql::primarykey_instantiation(instance):
    assert isinstance(instance, grammarSql::PrimaryKey)

@given(instance=grammarSql::Column_strategy)
@settings(max_examples=50)
def test_grammarsql::column_instantiation(instance):
    assert isinstance(instance, grammarSql::Column)

@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_isNotNull_type(instance):
    assert isinstance(instance.isNotNull, bool)


@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original

@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=grammarSql::Column_strategy)
def test_grammarsql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=grammarSql::EObject_strategy)
@settings(max_examples=50)
def test_grammarsql::eobject_instantiation(instance):
    assert isinstance(instance, grammarSql::EObject)

@given(instance=grammarSql::Table_strategy)
@settings(max_examples=50)
def test_grammarsql::table_instantiation(instance):
    assert isinstance(instance, grammarSql::Table)

@given(instance=grammarSql::Table_strategy)
def test_grammarsql::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=grammarSql::Table_strategy)
def test_grammarsql::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=grammarSql::Model_strategy)
@settings(max_examples=50)
def test_grammarsql::model_instantiation(instance):
    assert isinstance(instance, grammarSql::Model)
