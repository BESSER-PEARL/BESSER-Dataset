import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ER_Key,
    ER_Column,
    ER_ForeignKey,
    ER_Table,
    ER_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er_key_is_not_abstract():
    assert not inspect.isabstract(ER_Key)


def test_er_key_constructor_exists():
    assert callable(ER_Key.__init__)


def test_er_key_constructor_args():
    sig = inspect.signature(ER_Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_key_has_name():
    assert hasattr(ER_Key, "name")
    descriptor = None
    for klass in ER_Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_column_is_not_abstract():
    assert not inspect.isabstract(ER_Column)


def test_er_column_constructor_exists():
    assert callable(ER_Column.__init__)


def test_er_column_constructor_args():
    sig = inspect.signature(ER_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_er_column_has_name():
    assert hasattr(ER_Column, "name")
    descriptor = None
    for klass in ER_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_er_column_has_type():
    assert hasattr(ER_Column, "type")
    descriptor = None
    for klass in ER_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_er_foreignkey_is_not_abstract():
    assert not inspect.isabstract(ER_ForeignKey)


def test_er_foreignkey_constructor_exists():
    assert callable(ER_ForeignKey.__init__)


def test_er_foreignkey_constructor_args():
    sig = inspect.signature(ER_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_foreignkey_has_name():
    assert hasattr(ER_ForeignKey, "name")
    descriptor = None
    for klass in ER_ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_table_is_not_abstract():
    assert not inspect.isabstract(ER_Table)


def test_er_table_constructor_exists():
    assert callable(ER_Table.__init__)


def test_er_table_constructor_args():
    sig = inspect.signature(ER_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_table_has_name():
    assert hasattr(ER_Table, "name")
    descriptor = None
    for klass in ER_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_er_schema_is_not_abstract():
    assert not inspect.isabstract(ER_Schema)


def test_er_schema_constructor_exists():
    assert callable(ER_Schema.__init__)


def test_er_schema_constructor_args():
    sig = inspect.signature(ER_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_schema_has_name():
    assert hasattr(ER_Schema, "name")
    descriptor = None
    for klass in ER_Schema.__mro__:
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
ER_Key_strategy = st.builds(
    ER_Key,
    name=
        safe_text
)
ER_Column_strategy = st.builds(
    ER_Column,
    name=
        safe_text,
    type=
        safe_text
)
ER_ForeignKey_strategy = st.builds(
    ER_ForeignKey,
    name=
        safe_text
)
ER_Table_strategy = st.builds(
    ER_Table,
    name=
        safe_text
)
ER_Schema_strategy = st.builds(
    ER_Schema,
    name=
        safe_text
)

@given(instance=ER_Key_strategy)
@settings(max_examples=50)
def test_er_key_instantiation(instance):
    assert isinstance(instance, ER_Key)



@given(instance=ER_Key_strategy)
def test_er_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_Column_strategy)
@settings(max_examples=50)
def test_er_column_instantiation(instance):
    assert isinstance(instance, ER_Column)



@given(instance=ER_Column_strategy)
def test_er_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ER_Column_strategy)
def test_er_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ER_ForeignKey_strategy)
@settings(max_examples=50)
def test_er_foreignkey_instantiation(instance):
    assert isinstance(instance, ER_ForeignKey)



@given(instance=ER_ForeignKey_strategy)
def test_er_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_Table_strategy)
@settings(max_examples=50)
def test_er_table_instantiation(instance):
    assert isinstance(instance, ER_Table)



@given(instance=ER_Table_strategy)
def test_er_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ER_Schema_strategy)
@settings(max_examples=50)
def test_er_schema_instantiation(instance):
    assert isinstance(instance, ER_Schema)



@given(instance=ER_Schema_strategy)
def test_er_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
