import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleRDBMS_Column,
    SimpleRDBMS_FKey,
    SimpleRDBMS_Table,
    FKeyType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplerdbms_column_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Column)


def test_simplerdbms_column_constructor_exists():
    assert callable(SimpleRDBMS_Column.__init__)


def test_simplerdbms_column_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_simplerdbms_column_has_name():
    assert hasattr(SimpleRDBMS_Column, "name")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_column_has_type():
    assert hasattr(SimpleRDBMS_Column, "type")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_column_has_id():
    assert hasattr(SimpleRDBMS_Column, "id")
    descriptor = None
    for klass in SimpleRDBMS_Column.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_fkey_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_FKey)


def test_simplerdbms_fkey_constructor_exists():
    assert callable(SimpleRDBMS_FKey.__init__)


def test_simplerdbms_fkey_constructor_args():
    sig = inspect.signature(SimpleRDBMS_FKey.__init__)
    params = list(sig.parameters.keys())
    assert "fkeyType" in params, "Missing parameter 'fkeyType'"

def test_simplerdbms_fkey_has_fkeyType():
    assert hasattr(SimpleRDBMS_FKey, "fkeyType")
    descriptor = None
    for klass in SimpleRDBMS_FKey.__mro__:
        if "fkeyType" in klass.__dict__:
            descriptor = klass.__dict__["fkeyType"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms_table_is_not_abstract():
    assert not inspect.isabstract(SimpleRDBMS_Table)


def test_simplerdbms_table_constructor_exists():
    assert callable(SimpleRDBMS_Table.__init__)


def test_simplerdbms_table_constructor_args():
    sig = inspect.signature(SimpleRDBMS_Table.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms_table_has_id():
    assert hasattr(SimpleRDBMS_Table, "id")
    descriptor = None
    for klass in SimpleRDBMS_Table.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simplerdbms_table_has_name():
    assert hasattr(SimpleRDBMS_Table, "name")
    descriptor = None
    for klass in SimpleRDBMS_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fkeytype_exists():
    # Check that the Enumeration exists
    assert FKeyType is not None

def test_fkeytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FKeyType]
    expected_literals = [
        "PKEY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FKeyType"


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
SimpleRDBMS_Column_strategy = st.builds(
    SimpleRDBMS_Column,
    name=
        safe_text,
    type=
        safe_text,
    id=
        st.integers()
)
SimpleRDBMS_FKey_strategy = st.builds(
    SimpleRDBMS_FKey,
    fkeyType=
        safe_text
)
SimpleRDBMS_Table_strategy = st.builds(
    SimpleRDBMS_Table,
    id=
        st.integers(),
    name=
        safe_text
)

@given(instance=SimpleRDBMS_Column_strategy)
@settings(max_examples=50)
def test_simplerdbms_column_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Column)



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=SimpleRDBMS_Column_strategy)
def test_simplerdbms_column_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SimpleRDBMS_FKey_strategy)
@settings(max_examples=50)
def test_simplerdbms_fkey_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_FKey)



@given(instance=SimpleRDBMS_FKey_strategy)
def test_simplerdbms_fkey_fkeyType_setter(instance):
    original = instance.fkeyType
    instance.fkeyType = original
    assert instance.fkeyType == original

@given(instance=SimpleRDBMS_Table_strategy)
@settings(max_examples=50)
def test_simplerdbms_table_instantiation(instance):
    assert isinstance(instance, SimpleRDBMS_Table)



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SimpleRDBMS_Table_strategy)
def test_simplerdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
