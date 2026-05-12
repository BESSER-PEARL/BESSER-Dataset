import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rdbms_ForeignKey,
    rdbms_Column,
    rdbms_Table,
    rdbms_RDBMSModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_ForeignKey)


def test_rdbms_foreignkey_constructor_exists():
    assert callable(rdbms_ForeignKey.__init__)


def test_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(rdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(rdbms_Column)


def test_rdbms_column_constructor_exists():
    assert callable(rdbms_Column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(rdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_column_has_type():
    assert hasattr(rdbms_Column, "type")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_name():
    assert hasattr(rdbms_Column, "name")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(rdbms_Table)


def test_rdbms_table_constructor_exists():
    assert callable(rdbms_Table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(rdbms_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_table_has_name():
    assert hasattr(rdbms_Table, "name")
    descriptor = None
    for klass in rdbms_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(rdbms_RDBMSModel)


def test_rdbms_rdbmsmodel_constructor_exists():
    assert callable(rdbms_RDBMSModel.__init__)


def test_rdbms_rdbmsmodel_constructor_args():
    sig = inspect.signature(rdbms_RDBMSModel.__init__)
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
rdbms_ForeignKey_strategy = st.builds(
    rdbms_ForeignKey,
)
rdbms_Column_strategy = st.builds(
    rdbms_Column,
    type=
        safe_text,
    name=
        safe_text
)
rdbms_Table_strategy = st.builds(
    rdbms_Table,
    name=
        safe_text
)
rdbms_RDBMSModel_strategy = st.builds(
    rdbms_RDBMSModel,
)

@given(instance=rdbms_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms_ForeignKey)

@given(instance=rdbms_Column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, rdbms_Column)



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms_Table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, rdbms_Table)



@given(instance=rdbms_Table_strategy)
def test_rdbms_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rdbms_RDBMSModel_strategy)
@settings(max_examples=50)
def test_rdbms_rdbmsmodel_instantiation(instance):
    assert isinstance(instance, rdbms_RDBMSModel)
