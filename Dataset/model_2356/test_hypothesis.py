import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RDBMS_Key,
    RDBMS_Column,
    RDBMS_ForeignKey,
    RDBMS_Table,
    RDBMS_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms_key_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Key)


def test_rdbms_key_constructor_exists():
    assert callable(RDBMS_Key.__init__)


def test_rdbms_key_constructor_args():
    sig = inspect.signature(RDBMS_Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_key_has_name():
    assert hasattr(RDBMS_Key, "name")
    descriptor = None
    for klass in RDBMS_Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Column)


def test_rdbms_column_constructor_exists():
    assert callable(RDBMS_Column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(RDBMS_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_rdbms_column_has_name():
    assert hasattr(RDBMS_Column, "name")
    descriptor = None
    for klass in RDBMS_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_type():
    assert hasattr(RDBMS_Column, "type")
    descriptor = None
    for klass in RDBMS_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(RDBMS_ForeignKey)


def test_rdbms_foreignkey_constructor_exists():
    assert callable(RDBMS_ForeignKey.__init__)


def test_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(RDBMS_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_foreignkey_has_name():
    assert hasattr(RDBMS_ForeignKey, "name")
    descriptor = None
    for klass in RDBMS_ForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Table)


def test_rdbms_table_constructor_exists():
    assert callable(RDBMS_Table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(RDBMS_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_table_has_name():
    assert hasattr(RDBMS_Table, "name")
    descriptor = None
    for klass in RDBMS_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_schema_is_not_abstract():
    assert not inspect.isabstract(RDBMS_Schema)


def test_rdbms_schema_constructor_exists():
    assert callable(RDBMS_Schema.__init__)


def test_rdbms_schema_constructor_args():
    sig = inspect.signature(RDBMS_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_schema_has_name():
    assert hasattr(RDBMS_Schema, "name")
    descriptor = None
    for klass in RDBMS_Schema.__mro__:
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
RDBMS_Key_strategy = st.builds(
    RDBMS_Key,
    name=
        safe_text
)
RDBMS_Column_strategy = st.builds(
    RDBMS_Column,
    name=
        safe_text,
    type=
        safe_text
)
RDBMS_ForeignKey_strategy = st.builds(
    RDBMS_ForeignKey,
    name=
        safe_text
)
RDBMS_Table_strategy = st.builds(
    RDBMS_Table,
    name=
        safe_text
)
RDBMS_Schema_strategy = st.builds(
    RDBMS_Schema,
    name=
        safe_text
)

@given(instance=RDBMS_Key_strategy)
@settings(max_examples=50)
def test_rdbms_key_instantiation(instance):
    assert isinstance(instance, RDBMS_Key)



@given(instance=RDBMS_Key_strategy)
def test_rdbms_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS_Column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, RDBMS_Column)



@given(instance=RDBMS_Column_strategy)
def test_rdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RDBMS_Column_strategy)
def test_rdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=RDBMS_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, RDBMS_ForeignKey)



@given(instance=RDBMS_ForeignKey_strategy)
def test_rdbms_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS_Table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, RDBMS_Table)



@given(instance=RDBMS_Table_strategy)
def test_rdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMS_Schema_strategy)
@settings(max_examples=50)
def test_rdbms_schema_instantiation(instance):
    assert isinstance(instance, RDBMS_Schema)



@given(instance=RDBMS_Schema_strategy)
def test_rdbms_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
