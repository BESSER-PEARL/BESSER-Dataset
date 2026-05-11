import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RDBMS::Key,
    RDBMS::Column,
    RDBMS::ForeignKey,
    RDBMS::Table,
    RDBMS::Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms::key_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Key)


def test_rdbms::key_constructor_exists():
    assert callable(RDBMS::Key.__init__)


def test_rdbms::key_constructor_args():
    sig = inspect.signature(RDBMS::Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::key_has_name():
    assert hasattr(RDBMS::Key, "name")
    descriptor = None
    for klass in RDBMS::Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::column_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Column)


def test_rdbms::column_constructor_exists():
    assert callable(RDBMS::Column.__init__)


def test_rdbms::column_constructor_args():
    sig = inspect.signature(RDBMS::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms::column_has_name():
    assert hasattr(RDBMS::Column, "name")
    descriptor = None
    for klass in RDBMS::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms::column_has_type():
    assert hasattr(RDBMS::Column, "type")
    descriptor = None
    for klass in RDBMS::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(RDBMS::ForeignKey)


def test_rdbms::foreignkey_constructor_exists():
    assert callable(RDBMS::ForeignKey.__init__)


def test_rdbms::foreignkey_constructor_args():
    sig = inspect.signature(RDBMS::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::foreignkey_has_name():
    assert hasattr(RDBMS::ForeignKey, "name")
    descriptor = None
    for klass in RDBMS::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::table_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Table)


def test_rdbms::table_constructor_exists():
    assert callable(RDBMS::Table.__init__)


def test_rdbms::table_constructor_args():
    sig = inspect.signature(RDBMS::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::table_has_name():
    assert hasattr(RDBMS::Table, "name")
    descriptor = None
    for klass in RDBMS::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms::schema_is_not_abstract():
    assert not inspect.isabstract(RDBMS::Schema)


def test_rdbms::schema_constructor_exists():
    assert callable(RDBMS::Schema.__init__)


def test_rdbms::schema_constructor_args():
    sig = inspect.signature(RDBMS::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms::schema_has_name():
    assert hasattr(RDBMS::Schema, "name")
    descriptor = None
    for klass in RDBMS::Schema.__mro__:
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
RDBMS::Key_strategy = st.builds(
    RDBMS::Key,
    name=
        safe_text
)
RDBMS::Column_strategy = st.builds(
    RDBMS::Column,
    name=
        safe_text,
    type=
        safe_text
)
RDBMS::ForeignKey_strategy = st.builds(
    RDBMS::ForeignKey,
    name=
        safe_text
)
RDBMS::Table_strategy = st.builds(
    RDBMS::Table,
    name=
        safe_text
)
RDBMS::Schema_strategy = st.builds(
    RDBMS::Schema,
    name=
        safe_text
)

@given(instance=RDBMS::Key_strategy)
@settings(max_examples=50)
def test_rdbms::key_instantiation(instance):
    assert isinstance(instance, RDBMS::Key)

@given(instance=RDBMS::Key_strategy)
def test_rdbms::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Key_strategy)
def test_rdbms::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Column_strategy)
@settings(max_examples=50)
def test_rdbms::column_instantiation(instance):
    assert isinstance(instance, RDBMS::Column)

@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=RDBMS::Column_strategy)
def test_rdbms::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=RDBMS::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, RDBMS::ForeignKey)

@given(instance=RDBMS::ForeignKey_strategy)
def test_rdbms::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::ForeignKey_strategy)
def test_rdbms::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Table_strategy)
@settings(max_examples=50)
def test_rdbms::table_instantiation(instance):
    assert isinstance(instance, RDBMS::Table)

@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Table_strategy)
def test_rdbms::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS::Schema_strategy)
@settings(max_examples=50)
def test_rdbms::schema_instantiation(instance):
    assert isinstance(instance, RDBMS::Schema)

@given(instance=RDBMS::Schema_strategy)
def test_rdbms::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDBMS::Schema_strategy)
def test_rdbms::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
