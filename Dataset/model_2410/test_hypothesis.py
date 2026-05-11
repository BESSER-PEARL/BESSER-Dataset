import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    relationalMetaModel::RelationalForeignKey,
    relationalMetaModel::RelationalSchema,
    relationalMetaModel::RelationalTable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relationalmetamodel::relationalforeignkey_is_not_abstract():
    assert not inspect.isabstract(relationalMetaModel::RelationalForeignKey)


def test_relationalmetamodel::relationalforeignkey_constructor_exists():
    assert callable(relationalMetaModel::RelationalForeignKey.__init__)


def test_relationalmetamodel::relationalforeignkey_constructor_args():
    sig = inspect.signature(relationalMetaModel::RelationalForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_relationalmetamodel::relationalforeignkey_has_Name():
    assert hasattr(relationalMetaModel::RelationalForeignKey, "Name")
    descriptor = None
    for klass in relationalMetaModel::RelationalForeignKey.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_relationalmetamodel::relationalschema_is_not_abstract():
    assert not inspect.isabstract(relationalMetaModel::RelationalSchema)


def test_relationalmetamodel::relationalschema_constructor_exists():
    assert callable(relationalMetaModel::RelationalSchema.__init__)


def test_relationalmetamodel::relationalschema_constructor_args():
    sig = inspect.signature(relationalMetaModel::RelationalSchema.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_relationalmetamodel::relationalschema_has_Name():
    assert hasattr(relationalMetaModel::RelationalSchema, "Name")
    descriptor = None
    for klass in relationalMetaModel::RelationalSchema.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_relationalmetamodel::relationaltable_is_not_abstract():
    assert not inspect.isabstract(relationalMetaModel::RelationalTable)


def test_relationalmetamodel::relationaltable_constructor_exists():
    assert callable(relationalMetaModel::RelationalTable.__init__)


def test_relationalmetamodel::relationaltable_constructor_args():
    sig = inspect.signature(relationalMetaModel::RelationalTable.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_relationalmetamodel::relationaltable_has_Name():
    assert hasattr(relationalMetaModel::RelationalTable, "Name")
    descriptor = None
    for klass in relationalMetaModel::RelationalTable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
relationalMetaModel::RelationalForeignKey_strategy = st.builds(
    relationalMetaModel::RelationalForeignKey,
    Name=
        safe_text
)
relationalMetaModel::RelationalSchema_strategy = st.builds(
    relationalMetaModel::RelationalSchema,
    Name=
        safe_text
)
relationalMetaModel::RelationalTable_strategy = st.builds(
    relationalMetaModel::RelationalTable,
    Name=
        safe_text
)

@given(instance=relationalMetaModel::RelationalForeignKey_strategy)
@settings(max_examples=50)
def test_relationalmetamodel::relationalforeignkey_instantiation(instance):
    assert isinstance(instance, relationalMetaModel::RelationalForeignKey)

@given(instance=relationalMetaModel::RelationalForeignKey_strategy)
def test_relationalmetamodel::relationalforeignkey_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=relationalMetaModel::RelationalForeignKey_strategy)
def test_relationalmetamodel::relationalforeignkey_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=relationalMetaModel::RelationalSchema_strategy)
@settings(max_examples=50)
def test_relationalmetamodel::relationalschema_instantiation(instance):
    assert isinstance(instance, relationalMetaModel::RelationalSchema)

@given(instance=relationalMetaModel::RelationalSchema_strategy)
def test_relationalmetamodel::relationalschema_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=relationalMetaModel::RelationalSchema_strategy)
def test_relationalmetamodel::relationalschema_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=relationalMetaModel::RelationalTable_strategy)
@settings(max_examples=50)
def test_relationalmetamodel::relationaltable_instantiation(instance):
    assert isinstance(instance, relationalMetaModel::RelationalTable)

@given(instance=relationalMetaModel::RelationalTable_strategy)
def test_relationalmetamodel::relationaltable_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=relationalMetaModel::RelationalTable_strategy)
def test_relationalmetamodel::relationaltable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
