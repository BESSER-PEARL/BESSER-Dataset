import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    Relational::Database,
    Relational::Type,
    Relational::Column,
    Relational::Table,
    Relational::Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_relational::database_is_not_abstract():
    assert not inspect.isabstract(Relational::Database)


def test_relational::database_constructor_exists():
    assert callable(Relational::Database.__init__)


def test_relational::database_constructor_args():
    sig = inspect.signature(Relational::Database.__init__)
    params = list(sig.parameters.keys())



def test_relational::type_is_not_abstract():
    assert not inspect.isabstract(Relational::Type)


def test_relational::type_constructor_exists():
    assert callable(Relational::Type.__init__)


def test_relational::type_constructor_args():
    sig = inspect.signature(Relational::Type.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(Relational::Column)


def test_relational::column_constructor_exists():
    assert callable(Relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(Relational::Column.__init__)
    params = list(sig.parameters.keys())



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(Relational::Table)


def test_relational::table_constructor_exists():
    assert callable(Relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(Relational::Table.__init__)
    params = list(sig.parameters.keys())



def test_relational::named_is_not_abstract():
    assert not inspect.isabstract(Relational::Named)


def test_relational::named_constructor_exists():
    assert callable(Relational::Named.__init__)


def test_relational::named_constructor_args():
    sig = inspect.signature(Relational::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::named_has_name():
    assert hasattr(Relational::Named, "name")
    descriptor = None
    for klass in Relational::Named.__mro__:
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
Named_strategy = st.builds(
    Named,
)
Relational::Database_strategy = st.builds(
    Relational::Database,
)
Relational::Type_strategy = st.builds(
    Relational::Type,
)
Relational::Column_strategy = st.builds(
    Relational::Column,
)
Relational::Table_strategy = st.builds(
    Relational::Table,
)
Relational::Named_strategy = st.builds(
    Relational::Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Relational::Database_strategy)
@settings(max_examples=50)
def test_relational::database_instantiation(instance):
    assert isinstance(instance, Relational::Database)

@given(instance=Relational::Type_strategy)
@settings(max_examples=50)
def test_relational::type_instantiation(instance):
    assert isinstance(instance, Relational::Type)

@given(instance=Relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, Relational::Column)

@given(instance=Relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, Relational::Table)

@given(instance=Relational::Named_strategy)
@settings(max_examples=50)
def test_relational::named_instantiation(instance):
    assert isinstance(instance, Relational::Named)

@given(instance=Relational::Named_strategy)
def test_relational::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Named_strategy)
def test_relational::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
