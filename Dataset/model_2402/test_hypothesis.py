import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    relational::Type,
    relational::Schema,
    relational::Column,
    relational::Table,
    relational::Named,
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



def test_relational::type_is_not_abstract():
    assert not inspect.isabstract(relational::Type)


def test_relational::type_constructor_exists():
    assert callable(relational::Type.__init__)


def test_relational::type_constructor_args():
    sig = inspect.signature(relational::Type.__init__)
    params = list(sig.parameters.keys())



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(relational::Schema.__init__)
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



def test_relational::named_is_not_abstract():
    assert not inspect.isabstract(relational::Named)


def test_relational::named_constructor_exists():
    assert callable(relational::Named.__init__)


def test_relational::named_constructor_args():
    sig = inspect.signature(relational::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::named_has_name():
    assert hasattr(relational::Named, "name")
    descriptor = None
    for klass in relational::Named.__mro__:
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
relational::Type_strategy = st.builds(
    relational::Type,
)
relational::Schema_strategy = st.builds(
    relational::Schema,
)
relational::Column_strategy = st.builds(
    relational::Column,
)
relational::Table_strategy = st.builds(
    relational::Table,
)
relational::Named_strategy = st.builds(
    relational::Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=relational::Type_strategy)
@settings(max_examples=50)
def test_relational::type_instantiation(instance):
    assert isinstance(instance, relational::Type)

@given(instance=relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, relational::Schema)

@given(instance=relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, relational::Column)

@given(instance=relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, relational::Table)

@given(instance=relational::Named_strategy)
@settings(max_examples=50)
def test_relational::named_instantiation(instance):
    assert isinstance(instance, relational::Named)

@given(instance=relational::Named_strategy)
def test_relational::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relational::Named_strategy)
def test_relational::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
