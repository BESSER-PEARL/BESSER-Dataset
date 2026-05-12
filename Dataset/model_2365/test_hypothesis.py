import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RelationalEntity,
    relational_Column,
    relational_Table,
    Table,
    relational_View,
    relational_Key,
    relational_RelationalEntity,
    Key,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_Schema,
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



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(relational_Column)


def test_relational_column_constructor_exists():
    assert callable(relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(relational_Column.__init__)
    params = list(sig.parameters.keys())



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(relational_Table)


def test_relational_table_constructor_exists():
    assert callable(relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(relational_Table.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_relational_view_is_not_abstract():
    assert not inspect.isabstract(relational_View)


def test_relational_view_constructor_exists():
    assert callable(relational_View.__init__)


def test_relational_view_constructor_args():
    sig = inspect.signature(relational_View.__init__)
    params = list(sig.parameters.keys())



def test_relational_key_is_not_abstract():
    assert not inspect.isabstract(relational_Key)


def test_relational_key_constructor_exists():
    assert callable(relational_Key.__init__)


def test_relational_key_constructor_args():
    sig = inspect.signature(relational_Key.__init__)
    params = list(sig.parameters.keys())



def test_relational_relationalentity_is_not_abstract():
    assert not inspect.isabstract(relational_RelationalEntity)


def test_relational_relationalentity_constructor_exists():
    assert callable(relational_RelationalEntity.__init__)


def test_relational_relationalentity_constructor_args():
    sig = inspect.signature(relational_RelationalEntity.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_primarykey_is_not_abstract():
    assert not inspect.isabstract(relational_PrimaryKey)


def test_relational_primarykey_constructor_exists():
    assert callable(relational_PrimaryKey.__init__)


def test_relational_primarykey_constructor_args():
    sig = inspect.signature(relational_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())

def test_sqldatatype_exists():
    # Check that the Enumeration exists
    assert SqlDataType is not None

def test_sqldatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SqlDataType]
    expected_literals = [
        "DATE",
        "CHAR",
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
relational_Column_strategy = st.builds(
    relational_Column,
)
relational_Table_strategy = st.builds(
    relational_Table,
)
Table_strategy = st.builds(
    Table,
)
relational_View_strategy = st.builds(
    relational_View,
)
relational_Key_strategy = st.builds(
    relational_Key,
)
relational_RelationalEntity_strategy = st.builds(
    relational_RelationalEntity,
)
Key_strategy = st.builds(
    Key,
)
relational_ForeignKey_strategy = st.builds(
    relational_ForeignKey,
)
relational_PrimaryKey_strategy = st.builds(
    relational_PrimaryKey,
)
relational_Schema_strategy = st.builds(
    relational_Schema,
)

@given(instance=RelationalEntity_strategy)
@settings(max_examples=50)
def test_relationalentity_instantiation(instance):
    assert isinstance(instance, RelationalEntity)

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=relational_View_strategy)
@settings(max_examples=50)
def test_relational_view_instantiation(instance):
    assert isinstance(instance, relational_View)

@given(instance=relational_Key_strategy)
@settings(max_examples=50)
def test_relational_key_instantiation(instance):
    assert isinstance(instance, relational_Key)

@given(instance=relational_RelationalEntity_strategy)
@settings(max_examples=50)
def test_relational_relationalentity_instantiation(instance):
    assert isinstance(instance, relational_RelationalEntity)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, relational_ForeignKey)

@given(instance=relational_PrimaryKey_strategy)
@settings(max_examples=50)
def test_relational_primarykey_instantiation(instance):
    assert isinstance(instance, relational_PrimaryKey)

@given(instance=relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)
