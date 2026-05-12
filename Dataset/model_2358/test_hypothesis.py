import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbmsMM_dummy,
    rdbmsMM_Table,
    rdbmsMM_Schema,
    rdbmsMM_Key,
    rdbmsMM_Column,
    rdbmsMM_ForeignKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm_dummy_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_dummy)


def test_rdbmsmm_dummy_constructor_exists():
    assert callable(rdbmsMM_dummy.__init__)


def test_rdbmsmm_dummy_constructor_args():
    sig = inspect.signature(rdbmsMM_dummy.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm_table_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Table)


def test_rdbmsmm_table_constructor_exists():
    assert callable(rdbmsMM_Table.__init__)


def test_rdbmsmm_table_constructor_args():
    sig = inspect.signature(rdbmsMM_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_table_has_name():
    assert hasattr(rdbmsMM_Table, "name")
    descriptor = None
    for klass in rdbmsMM_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_schema_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Schema)


def test_rdbmsmm_schema_constructor_exists():
    assert callable(rdbmsMM_Schema.__init__)


def test_rdbmsmm_schema_constructor_args():
    sig = inspect.signature(rdbmsMM_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_schema_has_name():
    assert hasattr(rdbmsMM_Schema, "name")
    descriptor = None
    for klass in rdbmsMM_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_key_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Key)


def test_rdbmsmm_key_constructor_exists():
    assert callable(rdbmsMM_Key.__init__)


def test_rdbmsmm_key_constructor_args():
    sig = inspect.signature(rdbmsMM_Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_key_has_name():
    assert hasattr(rdbmsMM_Key, "name")
    descriptor = None
    for klass in rdbmsMM_Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_column_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_Column)


def test_rdbmsmm_column_constructor_exists():
    assert callable(rdbmsMM_Column.__init__)


def test_rdbmsmm_column_constructor_args():
    sig = inspect.signature(rdbmsMM_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_column_has_type():
    assert hasattr(rdbmsMM_Column, "type")
    descriptor = None
    for klass in rdbmsMM_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm_column_has_name():
    assert hasattr(rdbmsMM_Column, "name")
    descriptor = None
    for klass in rdbmsMM_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbmsMM_ForeignKey)


def test_rdbmsmm_foreignkey_constructor_exists():
    assert callable(rdbmsMM_ForeignKey.__init__)


def test_rdbmsmm_foreignkey_constructor_args():
    sig = inspect.signature(rdbmsMM_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_foreignkey_has_name():
    assert hasattr(rdbmsMM_ForeignKey, "name")
    descriptor = None
    for klass in rdbmsMM_ForeignKey.__mro__:
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
rdbmsMM_dummy_strategy = st.builds(
    rdbmsMM_dummy,
)
rdbmsMM_Table_strategy = st.builds(
    rdbmsMM_Table,
    name=
        safe_text
)
rdbmsMM_Schema_strategy = st.builds(
    rdbmsMM_Schema,
    name=
        safe_text
)
rdbmsMM_Key_strategy = st.builds(
    rdbmsMM_Key,
    name=
        safe_text
)
rdbmsMM_Column_strategy = st.builds(
    rdbmsMM_Column,
    type=
        safe_text,
    name=
        safe_text
)
rdbmsMM_ForeignKey_strategy = st.builds(
    rdbmsMM_ForeignKey,
    name=
        safe_text
)

@given(instance=rdbmsMM_dummy_strategy)
@settings(max_examples=50)
def test_rdbmsmm_dummy_instantiation(instance):
    assert isinstance(instance, rdbmsMM_dummy)

@given(instance=rdbmsMM_Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm_table_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Table)



@given(instance=rdbmsMM_Table_strategy)
def test_rdbmsmm_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM_Schema_strategy)
@settings(max_examples=50)
def test_rdbmsmm_schema_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Schema)



@given(instance=rdbmsMM_Schema_strategy)
def test_rdbmsmm_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM_Key_strategy)
@settings(max_examples=50)
def test_rdbmsmm_key_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Key)



@given(instance=rdbmsMM_Key_strategy)
def test_rdbmsmm_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM_Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm_column_instantiation(instance):
    assert isinstance(instance, rdbmsMM_Column)



@given(instance=rdbmsMM_Column_strategy)
def test_rdbmsmm_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rdbmsMM_Column_strategy)
def test_rdbmsmm_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbmsMM_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbmsMM_ForeignKey)



@given(instance=rdbmsMM_ForeignKey_strategy)
def test_rdbmsmm_foreignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
