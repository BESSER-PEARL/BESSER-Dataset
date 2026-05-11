import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Column,
    Schema,
    Table,
    Named,
    Relational::Table,
    Relational::System,
    Relational::Column,
    Relational::Schema,
    Relational::Named,
    Relational::Type,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(Relational::Table)


def test_relational::table_constructor_exists():
    assert callable(Relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(Relational::Table.__init__)
    params = list(sig.parameters.keys())



def test_relational::system_is_not_abstract():
    assert not inspect.isabstract(Relational::System)


def test_relational::system_constructor_exists():
    assert callable(Relational::System.__init__)


def test_relational::system_constructor_args():
    sig = inspect.signature(Relational::System.__init__)
    params = list(sig.parameters.keys())



def test_relational::column_is_not_abstract():
    assert not inspect.isabstract(Relational::Column)


def test_relational::column_constructor_exists():
    assert callable(Relational::Column.__init__)


def test_relational::column_constructor_args():
    sig = inspect.signature(Relational::Column.__init__)
    params = list(sig.parameters.keys())



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(Relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(Relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(Relational::Schema.__init__)
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



def test_relational::type_is_not_abstract():
    assert not inspect.isabstract(Relational::Type)


def test_relational::type_constructor_exists():
    assert callable(Relational::Type.__init__)


def test_relational::type_constructor_args():
    sig = inspect.signature(Relational::Type.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
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
Column_strategy = st.builds(
    Column,
)
Schema_strategy = st.builds(
    Schema,
)
Table_strategy = st.builds(
    Table,
)
Named_strategy = st.builds(
    Named,
)
Relational::Table_strategy = st.builds(
    Relational::Table,
)
Relational::System_strategy = st.builds(
    Relational::System,
)
Relational::Column_strategy = st.builds(
    Relational::Column,
)
Relational::Schema_strategy = st.builds(
    Relational::Schema,
)
Relational::Named_strategy = st.builds(
    Relational::Named,
    name=
        safe_text
)
Relational::Type_strategy = st.builds(
    Relational::Type,
)
Type_strategy = st.builds(
    Type,
)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, Relational::Table)

@given(instance=Relational::System_strategy)
@settings(max_examples=50)
def test_relational::system_instantiation(instance):
    assert isinstance(instance, Relational::System)

@given(instance=Relational::Column_strategy)
@settings(max_examples=50)
def test_relational::column_instantiation(instance):
    assert isinstance(instance, Relational::Column)

@given(instance=Relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, Relational::Schema)

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

@given(instance=Relational::Type_strategy)
@settings(max_examples=50)
def test_relational::type_instantiation(instance):
    assert isinstance(instance, Relational::Type)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)
