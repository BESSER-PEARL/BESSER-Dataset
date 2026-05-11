import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    relationalmm::Column,
    relationalmm::Type,
    relationalmm::Table,
    relationalmm::Named,
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



def test_relationalmm::column_is_not_abstract():
    assert not inspect.isabstract(relationalmm::Column)


def test_relationalmm::column_constructor_exists():
    assert callable(relationalmm::Column.__init__)


def test_relationalmm::column_constructor_args():
    sig = inspect.signature(relationalmm::Column.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm::type_is_not_abstract():
    assert not inspect.isabstract(relationalmm::Type)


def test_relationalmm::type_constructor_exists():
    assert callable(relationalmm::Type.__init__)


def test_relationalmm::type_constructor_args():
    sig = inspect.signature(relationalmm::Type.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm::table_is_not_abstract():
    assert not inspect.isabstract(relationalmm::Table)


def test_relationalmm::table_constructor_exists():
    assert callable(relationalmm::Table.__init__)


def test_relationalmm::table_constructor_args():
    sig = inspect.signature(relationalmm::Table.__init__)
    params = list(sig.parameters.keys())



def test_relationalmm::named_is_not_abstract():
    assert not inspect.isabstract(relationalmm::Named)


def test_relationalmm::named_constructor_exists():
    assert callable(relationalmm::Named.__init__)


def test_relationalmm::named_constructor_args():
    sig = inspect.signature(relationalmm::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationalmm::named_has_name():
    assert hasattr(relationalmm::Named, "name")
    descriptor = None
    for klass in relationalmm::Named.__mro__:
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
relationalmm::Column_strategy = st.builds(
    relationalmm::Column,
)
relationalmm::Type_strategy = st.builds(
    relationalmm::Type,
)
relationalmm::Table_strategy = st.builds(
    relationalmm::Table,
)
relationalmm::Named_strategy = st.builds(
    relationalmm::Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=relationalmm::Column_strategy)
@settings(max_examples=50)
def test_relationalmm::column_instantiation(instance):
    assert isinstance(instance, relationalmm::Column)

@given(instance=relationalmm::Type_strategy)
@settings(max_examples=50)
def test_relationalmm::type_instantiation(instance):
    assert isinstance(instance, relationalmm::Type)

@given(instance=relationalmm::Table_strategy)
@settings(max_examples=50)
def test_relationalmm::table_instantiation(instance):
    assert isinstance(instance, relationalmm::Table)

@given(instance=relationalmm::Named_strategy)
@settings(max_examples=50)
def test_relationalmm::named_instantiation(instance):
    assert isinstance(instance, relationalmm::Named)

@given(instance=relationalmm::Named_strategy)
def test_relationalmm::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relationalmm::Named_strategy)
def test_relationalmm::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
