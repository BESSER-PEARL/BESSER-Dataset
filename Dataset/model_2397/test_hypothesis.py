import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Constraint,
    SqlMetamodel_ForeingKey,
    SqlMetamodel_PrimaryKey,
    SqlMetamodel_Constraint,
    SqlMetamodel_Column,
    SqlMetamodel_Table,
    SqlMetamodel_Schema,
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



def test_sqlmetamodel_foreingkey_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_ForeingKey)


def test_sqlmetamodel_foreingkey_constructor_exists():
    assert callable(SqlMetamodel_ForeingKey.__init__)


def test_sqlmetamodel_foreingkey_constructor_args():
    sig = inspect.signature(SqlMetamodel_ForeingKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlmetamodel_primarykey_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_PrimaryKey)


def test_sqlmetamodel_primarykey_constructor_exists():
    assert callable(SqlMetamodel_PrimaryKey.__init__)


def test_sqlmetamodel_primarykey_constructor_args():
    sig = inspect.signature(SqlMetamodel_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_sqlmetamodel_constraint_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_Constraint)


def test_sqlmetamodel_constraint_constructor_exists():
    assert callable(SqlMetamodel_Constraint.__init__)


def test_sqlmetamodel_constraint_constructor_args():
    sig = inspect.signature(SqlMetamodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel_constraint_has_name():
    assert hasattr(SqlMetamodel_Constraint, "name")
    descriptor = None
    for klass in SqlMetamodel_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel_column_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_Column)


def test_sqlmetamodel_column_constructor_exists():
    assert callable(SqlMetamodel_Column.__init__)


def test_sqlmetamodel_column_constructor_args():
    sig = inspect.signature(SqlMetamodel_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "type" in params, "Missing parameter 'type'"

def test_sqlmetamodel_column_has_name():
    assert hasattr(SqlMetamodel_Column, "name")
    descriptor = None
    for klass in SqlMetamodel_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqlmetamodel_column_has_nullable():
    assert hasattr(SqlMetamodel_Column, "nullable")
    descriptor = None
    for klass in SqlMetamodel_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_sqlmetamodel_column_has_type():
    assert hasattr(SqlMetamodel_Column, "type")
    descriptor = None
    for klass in SqlMetamodel_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel_table_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_Table)


def test_sqlmetamodel_table_constructor_exists():
    assert callable(SqlMetamodel_Table.__init__)


def test_sqlmetamodel_table_constructor_args():
    sig = inspect.signature(SqlMetamodel_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel_table_has_name():
    assert hasattr(SqlMetamodel_Table, "name")
    descriptor = None
    for klass in SqlMetamodel_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlmetamodel_schema_is_not_abstract():
    assert not inspect.isabstract(SqlMetamodel_Schema)


def test_sqlmetamodel_schema_constructor_exists():
    assert callable(SqlMetamodel_Schema.__init__)


def test_sqlmetamodel_schema_constructor_args():
    sig = inspect.signature(SqlMetamodel_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlmetamodel_schema_has_name():
    assert hasattr(SqlMetamodel_Schema, "name")
    descriptor = None
    for klass in SqlMetamodel_Schema.__mro__:
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
        "INT",
        "DOUBLE",
        "FLOAT",
        "DATE",
        "BOOLEAN",
        "STRING",
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
SqlMetamodel_ForeingKey_strategy = st.builds(
    SqlMetamodel_ForeingKey,
)
SqlMetamodel_PrimaryKey_strategy = st.builds(
    SqlMetamodel_PrimaryKey,
)
SqlMetamodel_Constraint_strategy = st.builds(
    SqlMetamodel_Constraint,
    name=
        safe_text
)
SqlMetamodel_Column_strategy = st.builds(
    SqlMetamodel_Column,
    name=
        safe_text,
    nullable=
        st.booleans(),
    type=
        safe_text
)
SqlMetamodel_Table_strategy = st.builds(
    SqlMetamodel_Table,
    name=
        safe_text
)
SqlMetamodel_Schema_strategy = st.builds(
    SqlMetamodel_Schema,
    name=
        safe_text
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=SqlMetamodel_ForeingKey_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_foreingkey_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_ForeingKey)

@given(instance=SqlMetamodel_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_primarykey_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_PrimaryKey)

@given(instance=SqlMetamodel_Constraint_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_constraint_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_Constraint)



@given(instance=SqlMetamodel_Constraint_strategy)
def test_sqlmetamodel_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqlMetamodel_Column_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_column_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_Column)



@given(instance=SqlMetamodel_Column_strategy)
def test_sqlmetamodel_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SqlMetamodel_Column_strategy)
def test_sqlmetamodel_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=SqlMetamodel_Column_strategy)
def test_sqlmetamodel_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SqlMetamodel_Table_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_table_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_Table)



@given(instance=SqlMetamodel_Table_strategy)
def test_sqlmetamodel_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqlMetamodel_Schema_strategy)
@settings(max_examples=50)
def test_sqlmetamodel_schema_instantiation(instance):
    assert isinstance(instance, SqlMetamodel_Schema)



@given(instance=SqlMetamodel_Schema_strategy)
def test_sqlmetamodel_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
