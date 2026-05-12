import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    relational_ForeignKey,
    relational_Key,
    relational_Table,
    relational_Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_key_is_not_abstract():
    assert not inspect.isabstract(relational_Key)


def test_relational_key_constructor_exists():
    assert callable(relational_Key.__init__)


def test_relational_key_constructor_args():
    sig = inspect.signature(relational_Key.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_key_has_name():
    assert hasattr(relational_Key, "name")
    descriptor = None
    for klass in relational_Key.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_table_has_name():
    assert hasattr(relational_Table, "name")
    descriptor = None
    for klass in relational_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_relational_column_has_name():
    assert hasattr(relational_Column, "name")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational_column_has_type():
    assert hasattr(relational_Column, "type")
    descriptor = None
    for klass in relational_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
)
relational_Key_strategy = st.builds(
    relational_Key,
    name=
        safe_text
)
relational_Table_strategy = st.builds(
    relational_Table,
    name=
        safe_text
)
relational_Column_strategy = st.builds(
    relational_Column,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)

@given(instance=relational_Key_strategy)
@settings(max_examples=50)
def test_relational_key_instantiation(instance):
    assert isinstance(instance, relational_Key)



@given(instance=relational_Key_strategy)
def test_relational_key_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)



@given(instance=relational_Table_strategy)
def test_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)



@given(instance=relational_Column_strategy)
def test_relational_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=relational_Column_strategy)
def test_relational_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
