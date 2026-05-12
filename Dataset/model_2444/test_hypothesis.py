import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Named,
    relationalmm_Column,
    relationalmm_Type,
    relationalmm_Table,
    relationalmm_Named,
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



def test_relationalmm_column_is_not_abstract():
    assert not inspect.isabstract(relationalmm_Column)


def test_relationalmm_column_constructor_exists():
    assert callable(relationalmm_Column.__init__)


def test_relationalmm_column_constructor_args():
    sig = inspect.signature(relationalmm_Column.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm_type_is_not_abstract():
    assert not inspect.isabstract(relationalmm_Type)


def test_relationalmm_type_constructor_exists():
    assert callable(relationalmm_Type.__init__)


def test_relationalmm_type_constructor_args():
    sig = inspect.signature(relationalmm_Type.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm_table_is_not_abstract():
    assert not inspect.isabstract(relationalmm_Table)


def test_relationalmm_table_constructor_exists():
    assert callable(relationalmm_Table.__init__)


def test_relationalmm_table_constructor_args():
    sig = inspect.signature(relationalmm_Table.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm_named_is_not_abstract():
    assert not inspect.isabstract(relationalmm_Named)


def test_relationalmm_named_constructor_exists():
    assert callable(relationalmm_Named.__init__)


def test_relationalmm_named_constructor_args():
    sig = inspect.signature(relationalmm_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationalmm_named_has_name():
    assert hasattr(relationalmm_Named, "name")
    descriptor = None
    for klass in relationalmm_Named.__mro__:
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
relationalmm_Column_strategy = st.builds(
    relationalmm_Column,
)
relationalmm_Type_strategy = st.builds(
    relationalmm_Type,
)
relationalmm_Table_strategy = st.builds(
    relationalmm_Table,
)
relationalmm_Named_strategy = st.builds(
    relationalmm_Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=relationalmm_Column_strategy)
@settings(max_examples=50)
def test_relationalmm_column_instantiation(instance):
    assert isinstance(instance, relationalmm_Column)

@given(instance=relationalmm_Type_strategy)
@settings(max_examples=50)
def test_relationalmm_type_instantiation(instance):
    assert isinstance(instance, relationalmm_Type)

@given(instance=relationalmm_Table_strategy)
@settings(max_examples=50)
def test_relationalmm_table_instantiation(instance):
    assert isinstance(instance, relationalmm_Table)

@given(instance=relationalmm_Named_strategy)
@settings(max_examples=50)
def test_relationalmm_named_instantiation(instance):
    assert isinstance(instance, relationalmm_Named)



@given(instance=relationalmm_Named_strategy)
def test_relationalmm_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
