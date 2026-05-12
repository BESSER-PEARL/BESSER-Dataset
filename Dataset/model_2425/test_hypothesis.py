import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Named,
    Relational_Column,
    Relational_Database,
    Relational_Type,
    Relational_Table,
    Relational_Named,
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



def test_relational_column_is_not_abstract():
    assert not inspect.isabstract(Relational_Column)


def test_relational_column_constructor_exists():
    assert callable(Relational_Column.__init__)


def test_relational_column_constructor_args():
    sig = inspect.signature(Relational_Column.__init__)
    params = list(sig.parameters.keys())



def test_relational_database_is_not_abstract():
    assert not inspect.isabstract(Relational_Database)


def test_relational_database_constructor_exists():
    assert callable(Relational_Database.__init__)


def test_relational_database_constructor_args():
    sig = inspect.signature(Relational_Database.__init__)
    params = list(sig.parameters.keys())



def test_relational_type_is_not_abstract():
    assert not inspect.isabstract(Relational_Type)


def test_relational_type_constructor_exists():
    assert callable(Relational_Type.__init__)


def test_relational_type_constructor_args():
    sig = inspect.signature(Relational_Type.__init__)
    params = list(sig.parameters.keys())



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(Relational_Table)


def test_relational_table_constructor_exists():
    assert callable(Relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(Relational_Table.__init__)
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
Relational_Column_strategy = st.builds(
    Relational_Column,
)
Relational_Database_strategy = st.builds(
    Relational_Database,
)
Relational_Type_strategy = st.builds(
    Relational_Type,
)
Relational_Table_strategy = st.builds(
    Relational_Table,
)
Relational_Named_strategy = st.builds(
    Relational_Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, Relational_Column)

@given(instance=Relational_Database_strategy)
@settings(max_examples=50)
def test_relational_database_instantiation(instance):
    assert isinstance(instance, Relational_Database)

@given(instance=Relational_Type_strategy)
@settings(max_examples=50)
def test_relational_type_instantiation(instance):
    assert isinstance(instance, Relational_Type)

@given(instance=Relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, Relational_Table)

@given(instance=Relational_Named_strategy)
@settings(max_examples=50)
def test_relational_named_instantiation(instance):
    assert isinstance(instance, Relational_Named)



@given(instance=Relational_Named_strategy)
def test_relational_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
