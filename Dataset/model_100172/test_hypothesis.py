import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rdbmsMM::dummy,
    rdbmsMM::Key,
    rdbmsMM::Column,
    rdbmsMM::ForeignKey,
    rdbmsMM::Table,
    rdbmsMM::Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm::dummy_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::dummy)


def test_rdbmsmm::dummy_constructor_exists():
    assert callable(rdbmsMM::dummy.__init__)


def test_rdbmsmm::dummy_constructor_args():
    sig = inspect.signature(rdbmsMM::dummy.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm::key_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Key)


def test_rdbmsmm::key_constructor_exists():
    assert callable(rdbmsMM::Key.__init__)


def test_rdbmsmm::key_constructor_args():
    sig = inspect.signature(rdbmsMM::Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm::key_has_name():
    assert hasattr(rdbmsMM::Key, "name")
    descriptor = None
    for klass in rdbmsMM::Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm::column_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Column)


def test_rdbmsmm::column_constructor_exists():
    assert callable(rdbmsMM::Column.__init__)


def test_rdbmsmm::column_constructor_args():
    sig = inspect.signature(rdbmsMM::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbmsmm::column_has_name():
    assert hasattr(rdbmsMM::Column, "name")
    descriptor = None
    for klass in rdbmsMM::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm::column_has_type():
    assert hasattr(rdbmsMM::Column, "type")
    descriptor = None
    for klass in rdbmsMM::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm::foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::ForeignKey)


def test_rdbmsmm::foreignkey_constructor_exists():
    assert callable(rdbmsMM::ForeignKey.__init__)


def test_rdbmsmm::foreignkey_constructor_args():
    sig = inspect.signature(rdbmsMM::ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm::foreignkey_has_name():
    assert hasattr(rdbmsMM::ForeignKey, "name")
    descriptor = None
    for klass in rdbmsMM::ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm::table_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Table)


def test_rdbmsmm::table_constructor_exists():
    assert callable(rdbmsMM::Table.__init__)


def test_rdbmsmm::table_constructor_args():
    sig = inspect.signature(rdbmsMM::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm::table_has_name():
    assert hasattr(rdbmsMM::Table, "name")
    descriptor = None
    for klass in rdbmsMM::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm::schema_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM::Schema)


def test_rdbmsmm::schema_constructor_exists():
    assert callable(rdbmsMM::Schema.__init__)


def test_rdbmsmm::schema_constructor_args():
    sig = inspect.signature(rdbmsMM::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm::schema_has_name():
    assert hasattr(rdbmsMM::Schema, "name")
    descriptor = None
    for klass in rdbmsMM::Schema.__mro__:
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
rdbmsMM::dummy_strategy = st.builds(
    rdbmsMM::dummy,
)
rdbmsMM::Key_strategy = st.builds(
    rdbmsMM::Key,
    name=
        safe_text
)
rdbmsMM::Column_strategy = st.builds(
    rdbmsMM::Column,
    name=
        safe_text,
    type=
        safe_text
)
rdbmsMM::ForeignKey_strategy = st.builds(
    rdbmsMM::ForeignKey,
    name=
        safe_text
)
rdbmsMM::Table_strategy = st.builds(
    rdbmsMM::Table,
    name=
        safe_text
)
rdbmsMM::Schema_strategy = st.builds(
    rdbmsMM::Schema,
    name=
        safe_text
)

@given(instance=rdbmsMM::dummy_strategy)
@settings(max_examples=50)
def test_rdbmsmm::dummy_instantiation(instance):
    assert isinstance(instance, rdbmsMM::dummy)

@given(instance=rdbmsMM::Key_strategy)
@settings(max_examples=50)
def test_rdbmsmm::key_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Key)

@given(instance=rdbmsMM::Key_strategy)
def test_rdbmsmm::key_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::Key_strategy)
def test_rdbmsmm::key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM::Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm::column_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Column)

@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=rdbmsMM::Column_strategy)
def test_rdbmsmm::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=rdbmsMM::ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm::foreignkey_instantiation(instance):
    assert isinstance(instance, rdbmsMM::ForeignKey)

@given(instance=rdbmsMM::ForeignKey_strategy)
def test_rdbmsmm::foreignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::ForeignKey_strategy)
def test_rdbmsmm::foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM::Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm::table_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Table)

@given(instance=rdbmsMM::Table_strategy)
def test_rdbmsmm::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::Table_strategy)
def test_rdbmsmm::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM::Schema_strategy)
@settings(max_examples=50)
def test_rdbmsmm::schema_instantiation(instance):
    assert isinstance(instance, rdbmsMM::Schema)

@given(instance=rdbmsMM::Schema_strategy)
def test_rdbmsmm::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rdbmsMM::Schema_strategy)
def test_rdbmsmm::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
