import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RelationalEntity,
    relational::Column,
    relational::Table,
    Table,
    relational::View,
    relational::Key,
    relational::RelationalEntity,
    Key,
    relational::ForeignKey,
    relational::PrimaryKey,
    relational::Schema,
    SqlDataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relationalentity_is_not_abstract():
    assert not inspect.isabstract(RelationalEntity)


def test_relationalentity_constructor_exists():
    assert callable(RelationalEntity.__init__)


def test_relationalentity_constructor_args():
    sig = inspect.signature(RelationalEntity.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(relational::Column)


def test_relational::column_constructor_exists():
    assert callable(relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(relational::Column.__init__)
    params = list(sig.parameters.keys())



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(relational::Table)


def test_relational::table_constructor_exists():
    assert callable(relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(relational::Table.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_relational::view_is_not_abstract():
    assert not inspect.isabstract(relational::View)


def test_relational::view_constructor_exists():
    assert callable(relational::View.__init__)


def test_relational::view_constructor_args():
    sig = inspect.signature(relational::View.__init__)
    params = list(sig.parameters.keys())



def test_relational::key_is_not_abstract():
    assert not inspect.isabstract(relational::Key)


def test_relational::key_constructor_exists():
    assert callable(relational::Key.__init__)


def test_relational::key_constructor_args():
    sig = inspect.signature(relational::Key.__init__)
    params = list(sig.parameters.keys())



def test_relational::relationalentity_is_not_abstract():
    assert not inspect.isabstract(relational::RelationalEntity)


def test_relational::relationalentity_constructor_exists():
    assert callable(relational::RelationalEntity.__init__)


def test_relational::relationalentity_constructor_args():
    sig = inspect.signature(relational::RelationalEntity.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::primarykey_is_not_abstract():
    assert not inspect.isabstract(relational::PrimaryKey)


def test_relational::primarykey_constructor_exists():
    assert callable(relational::PrimaryKey.__init__)


def test_relational::primarykey_constructor_args():
    sig = inspect.signature(relational::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(relational::Schema.__init__)
    params = list(sig.parameters.keys())

def test_sqldatatype_exists():
    # Check that the Enumeration exists
    assert SqlDataType is not None

def test_sqldatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SqlDataType]
    expected_literals = [
        "CHAR",
        "DATE",
        "VARCHAR",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SqlDataType"


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
RelationalEntity_strategy = st.builds(
    RelationalEntity,
)
relational::Column_strategy = st.builds(
    relational::Column,
)
relational::Table_strategy = st.builds(
    relational::Table,
)
Table_strategy = st.builds(
    Table,
)
relational::View_strategy = st.builds(
    relational::View,
)
relational::Key_strategy = st.builds(
    relational::Key,
)
relational::RelationalEntity_strategy = st.builds(
    relational::RelationalEntity,
)
Key_strategy = st.builds(
    Key,
)
relational::ForeignKey_strategy = st.builds(
    relational::ForeignKey,
)
relational::PrimaryKey_strategy = st.builds(
    relational::PrimaryKey,
)
relational::Schema_strategy = st.builds(
    relational::Schema,
)

@given(instance=RelationalEntity_strategy)
@settings(max_examples=50)
def test_relationalentity_instantiation(instance):
    assert isinstance(instance, RelationalEntity)

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=relational::View_strategy)
@settings(max_examples=50)
def test_relational::view_instantiation(instance):
    assert isinstance(instance, relational::View)

@given(instance=relational::Key_strategy)
@settings(max_examples=50)
def test_relational::key_instantiation(instance):
    assert isinstance(instance, relational::Key)

@given(instance=relational::RelationalEntity_strategy)
@settings(max_examples=50)
def test_relational::relationalentity_instantiation(instance):
    assert isinstance(instance, relational::RelationalEntity)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, relational::ForeignKey)

@given(instance=relational::PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational::primarykey_instantiation(instance):
    assert isinstance(instance, relational::PrimaryKey)

@given(instance=relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, relational::Schema)
