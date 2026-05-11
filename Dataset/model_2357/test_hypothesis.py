import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ER::Key,
    ER::Column,
    ER::ForeignKey,
    ER::Table,
    ER::Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er::key_is_not_abstract():
    assert not inspect.isabstract(ER::Key)


def test_er::key_constructor_exists():
    assert callable(ER::Key.__init__)


def test_er::key_constructor_args():
    sig = inspect.signature(ER::Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::key_has_name():
    assert hasattr(ER::Key, "name")
    descriptor = None
    for klass in ER::Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::column_is_not_abstract():
    assert not inspect.isabstract(ER::Column)


def test_er::column_constructor_exists():
    assert callable(ER::Column.__init__)


def test_er::column_constructor_args():
    sig = inspect.signature(ER::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_er::column_has_name():
    assert hasattr(ER::Column, "name")
    descriptor = None
    for klass in ER::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_er::column_has_type():
    assert hasattr(ER::Column, "type")
    descriptor = None
    for klass in ER::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_er::foreignkey_is_not_abstract():
    assert not inspect.isabstract(ER::ForeignKey)


def test_er::foreignkey_constructor_exists():
    assert callable(ER::ForeignKey.__init__)


def test_er::foreignkey_constructor_args():
    sig = inspect.signature(ER::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::foreignkey_has_name():
    assert hasattr(ER::ForeignKey, "name")
    descriptor = None
    for klass in ER::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::table_is_not_abstract():
    assert not inspect.isabstract(ER::Table)


def test_er::table_constructor_exists():
    assert callable(ER::Table.__init__)


def test_er::table_constructor_args():
    sig = inspect.signature(ER::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::table_has_name():
    assert hasattr(ER::Table, "name")
    descriptor = None
    for klass in ER::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er::schema_is_not_abstract():
    assert not inspect.isabstract(ER::Schema)


def test_er::schema_constructor_exists():
    assert callable(ER::Schema.__init__)


def test_er::schema_constructor_args():
    sig = inspect.signature(ER::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::schema_has_name():
    assert hasattr(ER::Schema, "name")
    descriptor = None
    for klass in ER::Schema.__mro__:
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
ER::Key_strategy = st.builds(
    ER::Key,
    name=
        safe_text
)
ER::Column_strategy = st.builds(
    ER::Column,
    name=
        safe_text,
    type=
        safe_text
)
ER::ForeignKey_strategy = st.builds(
    ER::ForeignKey,
    name=
        safe_text
)
ER::Table_strategy = st.builds(
    ER::Table,
    name=
        safe_text
)
ER::Schema_strategy = st.builds(
    ER::Schema,
    name=
        safe_text
)

@given(instance=ER::Key_strategy)
@settings(max_examples=50)
def test_er::key_instantiation(instance):
    assert isinstance(instance, ER::Key)

@given(instance=ER::Key_strategy)
def test_er::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Key_strategy)
def test_er::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Column_strategy)
@settings(max_examples=50)
def test_er::column_instantiation(instance):
    assert isinstance(instance, ER::Column)

@given(instance=ER::Column_strategy)
def test_er::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Column_strategy)
def test_er::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Column_strategy)
def test_er::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ER::Column_strategy)
def test_er::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ER::ForeignKey_strategy)
@settings(max_examples=50)
def test_er::foreignkey_instantiation(instance):
    assert isinstance(instance, ER::ForeignKey)

@given(instance=ER::ForeignKey_strategy)
def test_er::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::ForeignKey_strategy)
def test_er::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Table_strategy)
@settings(max_examples=50)
def test_er::table_instantiation(instance):
    assert isinstance(instance, ER::Table)

@given(instance=ER::Table_strategy)
def test_er::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Table_strategy)
def test_er::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER::Schema_strategy)
@settings(max_examples=50)
def test_er::schema_instantiation(instance):
    assert isinstance(instance, ER::Schema)

@given(instance=ER::Schema_strategy)
def test_er::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::Schema_strategy)
def test_er::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
