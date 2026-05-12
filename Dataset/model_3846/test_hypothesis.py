import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RDBMSMM_RDBMSModel,
    RDBMSMM_Column,
    RDBMSMM_Table,
    RDBMSMM_FKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbmsmm_rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM_RDBMSModel)


def test_rdbmsmm_rdbmsmodel_constructor_exists():
    assert callable(RDBMSMM_RDBMSModel.__init__)


def test_rdbmsmm_rdbmsmodel_constructor_args():
    sig = inspect.signature(RDBMSMM_RDBMSModel.__init__)
    params = list(sig.parameters.keys())



def test_rdbmsmm_column_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM_Column)


def test_rdbmsmm_column_constructor_exists():
    assert callable(RDBMSMM_Column.__init__)


def test_rdbmsmm_column_constructor_args():
    sig = inspect.signature(RDBMSMM_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_column_has_type():
    assert hasattr(RDBMSMM_Column, "type")
    descriptor = None
    for klass in RDBMSMM_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbmsmm_column_has_name():
    assert hasattr(RDBMSMM_Column, "name")
    descriptor = None
    for klass in RDBMSMM_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_table_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM_Table)


def test_rdbmsmm_table_constructor_exists():
    assert callable(RDBMSMM_Table.__init__)


def test_rdbmsmm_table_constructor_args():
    sig = inspect.signature(RDBMSMM_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbmsmm_table_has_name():
    assert hasattr(RDBMSMM_Table, "name")
    descriptor = None
    for klass in RDBMSMM_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbmsmm_fkey_is_not_abstract():
    assert not inspect.isabstract(RDBMSMM_FKey)


def test_rdbmsmm_fkey_constructor_exists():
    assert callable(RDBMSMM_FKey.__init__)


def test_rdbmsmm_fkey_constructor_args():
    sig = inspect.signature(RDBMSMM_FKey.__init__)
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
RDBMSMM_RDBMSModel_strategy = st.builds(
    RDBMSMM_RDBMSModel,
)
RDBMSMM_Column_strategy = st.builds(
    RDBMSMM_Column,
    type=
        safe_text,
    name=
        safe_text
)
RDBMSMM_Table_strategy = st.builds(
    RDBMSMM_Table,
    name=
        safe_text
)
RDBMSMM_FKey_strategy = st.builds(
    RDBMSMM_FKey,
)

@given(instance=RDBMSMM_RDBMSModel_strategy)
@settings(max_examples=50)
def test_rdbmsmm_rdbmsmodel_instantiation(instance):
    assert isinstance(instance, RDBMSMM_RDBMSModel)

@given(instance=RDBMSMM_Column_strategy)
@settings(max_examples=50)
def test_rdbmsmm_column_instantiation(instance):
    assert isinstance(instance, RDBMSMM_Column)



@given(instance=RDBMSMM_Column_strategy)
def test_rdbmsmm_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=RDBMSMM_Column_strategy)
def test_rdbmsmm_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMSMM_Table_strategy)
@settings(max_examples=50)
def test_rdbmsmm_table_instantiation(instance):
    assert isinstance(instance, RDBMSMM_Table)



@given(instance=RDBMSMM_Table_strategy)
def test_rdbmsmm_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDBMSMM_FKey_strategy)
@settings(max_examples=50)
def test_rdbmsmm_fkey_instantiation(instance):
    assert isinstance(instance, RDBMSMM_FKey)
