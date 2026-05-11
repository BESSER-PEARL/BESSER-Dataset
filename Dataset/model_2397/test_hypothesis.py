import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Constraint,
    SqlMetamodel::ForeingKey,
    SqlMetamodel::PrimaryKey,
    SqlMetamodel::Constraint,
    SqlMetamodel::Column,
    SqlMetamodel::Table,
    SqlMetamodel::Schema,
    TypeData,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlmetamodel::foreingkey_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::ForeingKey)


def test_sqlmetamodel::foreingkey_constructor_exists():
    assert callable(SqlMetamodel::ForeingKey.__init__)


def test_sqlmetamodel::foreingkey_constructor_args():
    sig = inspect.signature(SqlMetamodel::ForeingKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlmetamodel::primarykey_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::PrimaryKey)


def test_sqlmetamodel::primarykey_constructor_exists():
    assert callable(SqlMetamodel::PrimaryKey.__init__)


def test_sqlmetamodel::primarykey_constructor_args():
    sig = inspect.signature(SqlMetamodel::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlmetamodel::constraint_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::Constraint)


def test_sqlmetamodel::constraint_constructor_exists():
    assert callable(SqlMetamodel::Constraint.__init__)


def test_sqlmetamodel::constraint_constructor_args():
    sig = inspect.signature(SqlMetamodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel::constraint_has_name():
    assert hasattr(SqlMetamodel::Constraint, "name")
    descriptor = None
    for klass in SqlMetamodel::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel::column_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::Column)


def test_sqlmetamodel::column_constructor_exists():
    assert callable(SqlMetamodel::Column.__init__)


def test_sqlmetamodel::column_constructor_args():
    sig = inspect.signature(SqlMetamodel::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel::column_has_type():
    assert hasattr(SqlMetamodel::Column, "type")
    descriptor = None
    for klass in SqlMetamodel::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sqlmetamodel::column_has_nullable():
    assert hasattr(SqlMetamodel::Column, "nullable")
    descriptor = None
    for klass in SqlMetamodel::Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmetamodel::column_has_name():
    assert hasattr(SqlMetamodel::Column, "name")
    descriptor = None
    for klass in SqlMetamodel::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel::table_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::Table)


def test_sqlmetamodel::table_constructor_exists():
    assert callable(SqlMetamodel::Table.__init__)


def test_sqlmetamodel::table_constructor_args():
    sig = inspect.signature(SqlMetamodel::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel::table_has_name():
    assert hasattr(SqlMetamodel::Table, "name")
    descriptor = None
    for klass in SqlMetamodel::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel::schema_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel::Schema)


def test_sqlmetamodel::schema_constructor_exists():
    assert callable(SqlMetamodel::Schema.__init__)


def test_sqlmetamodel::schema_constructor_args():
    sig = inspect.signature(SqlMetamodel::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel::schema_has_name():
    assert hasattr(SqlMetamodel::Schema, "name")
    descriptor = None
    for klass in SqlMetamodel::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typedata_exists():
    # Check that the Enumeration exists
    assert TypeData is not None

def test_typedata_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeData]
    expected_literals = [
        "DATE",
        "INT",
        "STRING",
        "BOOLEAN",
        "FLOAT",
        "DOUBLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeData"


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
Constraint_strategy = st.builds(
    Constraint,
)
SqlMetamodel::ForeingKey_strategy = st.builds(
    SqlMetamodel::ForeingKey,
)
SqlMetamodel::PrimaryKey_strategy = st.builds(
    SqlMetamodel::PrimaryKey,
)
SqlMetamodel::Constraint_strategy = st.builds(
    SqlMetamodel::Constraint,
    name=
        safe_text
)
SqlMetamodel::Column_strategy = st.builds(
    SqlMetamodel::Column,
    type=
        safe_text,
    nullable=
        st.booleans(),
    name=
        safe_text
)
SqlMetamodel::Table_strategy = st.builds(
    SqlMetamodel::Table,
    name=
        safe_text
)
SqlMetamodel::Schema_strategy = st.builds(
    SqlMetamodel::Schema,
    name=
        safe_text
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=SqlMetamodel::ForeingKey_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::foreingkey_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::ForeingKey)

@given(instance=SqlMetamodel::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::primarykey_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::PrimaryKey)

@given(instance=SqlMetamodel::Constraint_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::constraint_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::Constraint)

@given(instance=SqlMetamodel::Constraint_strategy)
def test_sqlmetamodel::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SqlMetamodel::Constraint_strategy)
def test_sqlmetamodel::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqlMetamodel::Column_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::column_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::Column)

@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SqlMetamodel::Column_strategy)
def test_sqlmetamodel::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqlMetamodel::Table_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::table_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::Table)

@given(instance=SqlMetamodel::Table_strategy)
def test_sqlmetamodel::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SqlMetamodel::Table_strategy)
def test_sqlmetamodel::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqlMetamodel::Schema_strategy)
@settings(max_examples=50)
def test_sqlmetamodel::schema_instantiation(instance):
    assert isinstance(instance, SqlMetamodel::Schema)

@given(instance=SqlMetamodel::Schema_strategy)
def test_sqlmetamodel::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SqlMetamodel::Schema_strategy)
def test_sqlmetamodel::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
