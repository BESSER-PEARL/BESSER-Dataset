import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Named,
    Relational_Schema,
    Relational_Named,
    Relational_Type,
    Type,
    Relational_System,
    Relational_Column,
    Column,
    Schema,
    Relational_Table,
    Table,
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



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(Relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(Relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(Relational_Schema.__init__)
    params = list(sig.parameters.keys())



def test_relational_named_is_not_abstract():
    assert not inspect.isabstract(Relational_Named)


def test_relational_named_constructor_exists():
    assert callable(Relational_Named.__init__)


def test_relational_named_constructor_args():
    sig = inspect.signature(Relational_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_named_has_name():
    assert hasattr(Relational_Named, "name")
    descriptor = None
    for klass in Relational_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_type_is_not_abstract():
    assert not inspect.isabstract(Relational_Type)


def test_relational_type_constructor_exists():
    assert callable(Relational_Type.__init__)


def test_relational_type_constructor_args():
    sig = inspect.signature(Relational_Type.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_relational_system_is_not_abstract():
    assert not inspect.isabstract(Relational_System)


def test_relational_system_constructor_exists():
    assert callable(Relational_System.__init__)


def test_relational_system_constructor_args():
    sig = inspect.signature(Relational_System.__init__)
    params = list(sig.parameters.keys())



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(Relational_Column)


def test_relational_column_constructor_exists():
    assert callable(Relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(Relational_Column.__init__)
    params = list(sig.parameters.keys())



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



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(Relational_Table)


def test_relational_table_constructor_exists():
    assert callable(Relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(Relational_Table.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
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
Named_strategy = st.builds(
    Named,
)
Relational_Schema_strategy = st.builds(
    Relational_Schema,
)
Relational_Named_strategy = st.builds(
    Relational_Named,
    name=
        safe_text
)
Relational_Type_strategy = st.builds(
    Relational_Type,
)
Type_strategy = st.builds(
    Type,
)
Relational_System_strategy = st.builds(
    Relational_System,
)
Relational_Column_strategy = st.builds(
    Relational_Column,
)
Column_strategy = st.builds(
    Column,
)
Schema_strategy = st.builds(
    Schema,
)
Relational_Table_strategy = st.builds(
    Relational_Table,
)
Table_strategy = st.builds(
    Table,
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, Relational_Schema)

@given(instance=Relational_Named_strategy)
@settings(max_examples=50)
def test_relational_named_instantiation(instance):
    assert isinstance(instance, Relational_Named)



@given(instance=Relational_Named_strategy)
def test_relational_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_Type_strategy)
@settings(max_examples=50)
def test_relational_type_instantiation(instance):
    assert isinstance(instance, Relational_Type)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Relational_System_strategy)
@settings(max_examples=50)
def test_relational_system_instantiation(instance):
    assert isinstance(instance, Relational_System)

@given(instance=Relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, Relational_Column)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=Relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, Relational_Table)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)
