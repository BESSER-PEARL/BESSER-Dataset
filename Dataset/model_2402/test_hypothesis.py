import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Named,
    relational_Schema,
    relational_Type,
    relational_Column,
    relational_Table,
    relational_Named,
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
    assert not inspect.isabstract(relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(relational_Schema.__init__)
    params = list(sig.parameters.keys())



def test_relational_type_is_not_abstract():
    assert not inspect.isabstract(relational_Type)


def test_relational_type_constructor_exists():
    assert callable(relational_Type.__init__)


def test_relational_type_constructor_args():
    sig = inspect.signature(relational_Type.__init__)
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



def test_relational_named_is_not_abstract():
    assert not inspect.isabstract(relational_Named)


def test_relational_named_constructor_exists():
    assert callable(relational_Named.__init__)


def test_relational_named_constructor_args():
    sig = inspect.signature(relational_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_named_has_name():
    assert hasattr(relational_Named, "name")
    descriptor = None
    for klass in relational_Named.__mro__:
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
relational_Schema_strategy = st.builds(
    relational_Schema,
)
relational_Type_strategy = st.builds(
    relational_Type,
)
relational_Column_strategy = st.builds(
    relational_Column,
)
relational_Table_strategy = st.builds(
    relational_Table,
)
relational_Named_strategy = st.builds(
    relational_Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, relational_Schema)

@given(instance=relational_Type_strategy)
@settings(max_examples=50)
def test_relational_type_instantiation(instance):
    assert isinstance(instance, relational_Type)

@given(instance=relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, relational_Column)

@given(instance=relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, relational_Table)

@given(instance=relational_Named_strategy)
@settings(max_examples=50)
def test_relational_named_instantiation(instance):
    assert isinstance(instance, relational_Named)



@given(instance=relational_Named_strategy)
def test_relational_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
