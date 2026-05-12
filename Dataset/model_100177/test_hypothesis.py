import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    relational::ForeignKey,
    relational::Key,
    relational::Table,
    relational::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::key_is_not_abstract():
    assert not inspect.isabstract(relational::Key)


def test_relational::key_constructor_exists():
    assert callable(relational::Key.__init__)


def test_relational::key_constructor_args():
    sig = inspect.signature(relational::Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::key_has_name():
    assert hasattr(relational::Key, "name")
    descriptor = None
    for klass in relational::Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(relational::Table)


def test_relational::table_constructor_exists():
    assert callable(relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(relational::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::table_has_name():
    assert hasattr(relational::Table, "name")
    descriptor = None
    for klass in relational::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(relational::Column)


def test_relational::column_constructor_exists():
    assert callable(relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(relational::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational::column_has_type():
    assert hasattr(relational::Column, "type")
    descriptor = None
    for klass in relational::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_relational::column_has_name():
    assert hasattr(relational::Column, "name")
    descriptor = None
    for klass in relational::Column.__mro__:
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
relational::ForeignKey_strategy = st.builds(
    relational::ForeignKey,
)
relational::Key_strategy = st.builds(
    relational::Key,
    name=
        safe_text
)
relational::Table_strategy = st.builds(
    relational::Table,
    name=
        safe_text
)
relational::Column_strategy = st.builds(
    relational::Column,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::ForeignKey)

@given(instance=relational::Key_strategy)
@settings(max_examples=50)
def test_relational::key_instantiation(instance):
    assert isinstance(instance, relational::Key)

@given(instance=relational::Key_strategy)
def test_relational::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Key_strategy)
def test_relational::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=relational::Table_strategy)
def test_relational::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Table_strategy)
def test_relational::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Column_strategy)
def test_relational::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=relational::Column_strategy)
def test_relational::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=relational::Column_strategy)
def test_relational::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Column_strategy)
def test_relational::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
