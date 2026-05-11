import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    database::Column,
    database::Table,
    database::DB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database::column_is_not_abstract():
    assert not inspect.isabstract(database::Column)


def test_database::column_constructor_exists():
    assert callable(database::Column.__init__)


def test_database::column_constructor_args():
    sig = inspect.signature(database::Column.__init__)
    params = list(sig.parameters.keys())



def test_database::table_is_not_abstract():
    assert not inspect.isabstract(database::Table)


def test_database::table_constructor_exists():
    assert callable(database::Table.__init__)


def test_database::table_constructor_args():
    sig = inspect.signature(database::Table.__init__)
    params = list(sig.parameters.keys())



def test_database::db_is_not_abstract():
    assert not inspect.isabstract(database::DB)


def test_database::db_constructor_exists():
    assert callable(database::DB.__init__)


def test_database::db_constructor_args():
    sig = inspect.signature(database::DB.__init__)
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
database::Column_strategy = st.builds(
    database::Column,
)
database::Table_strategy = st.builds(
    database::Table,
)
database::DB_strategy = st.builds(
    database::DB,
)

@given(instance=database::Column_strategy)
@settings(max_examples=50)
def test_database::column_instantiation(instance):
    assert isinstance(instance, database::Column)

@given(instance=database::Table_strategy)
@settings(max_examples=50)
def test_database::table_instantiation(instance):
    assert isinstance(instance, database::Table)

@given(instance=database::DB_strategy)
@settings(max_examples=50)
def test_database::db_instantiation(instance):
    assert isinstance(instance, database::DB)
