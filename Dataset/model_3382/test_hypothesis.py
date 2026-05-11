import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Diagram,
    model::Constraint,
    model::Column,
    model::Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::diagram_is_not_abstract():
    assert not inspect.isabstract(model::Diagram)


def test_model::diagram_constructor_exists():
    assert callable(model::Diagram.__init__)


def test_model::diagram_constructor_args():
    sig = inspect.signature(model::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_model::constraint_is_not_abstract():
    assert not inspect.isabstract(model::Constraint)


def test_model::constraint_constructor_exists():
    assert callable(model::Constraint.__init__)


def test_model::constraint_constructor_args():
    sig = inspect.signature(model::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_model::column_is_not_abstract():
    assert not inspect.isabstract(model::Column)


def test_model::column_constructor_exists():
    assert callable(model::Column.__init__)


def test_model::column_constructor_args():
    sig = inspect.signature(model::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::column_has_name():
    assert hasattr(model::Column, "name")
    descriptor = None
    for klass in model::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::table_is_not_abstract():
    assert not inspect.isabstract(model::Table)


def test_model::table_constructor_exists():
    assert callable(model::Table.__init__)


def test_model::table_constructor_args():
    sig = inspect.signature(model::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::table_has_name():
    assert hasattr(model::Table, "name")
    descriptor = None
    for klass in model::Table.__mro__:
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
model::Diagram_strategy = st.builds(
    model::Diagram,
)
model::Constraint_strategy = st.builds(
    model::Constraint,
)
model::Column_strategy = st.builds(
    model::Column,
    name=
        safe_text
)
model::Table_strategy = st.builds(
    model::Table,
    name=
        safe_text
)

@given(instance=model::Diagram_strategy)
@settings(max_examples=50)
def test_model::diagram_instantiation(instance):
    assert isinstance(instance, model::Diagram)

@given(instance=model::Constraint_strategy)
@settings(max_examples=50)
def test_model::constraint_instantiation(instance):
    assert isinstance(instance, model::Constraint)

@given(instance=model::Column_strategy)
@settings(max_examples=50)
def test_model::column_instantiation(instance):
    assert isinstance(instance, model::Column)

@given(instance=model::Column_strategy)
def test_model::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Column_strategy)
def test_model::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Table_strategy)
@settings(max_examples=50)
def test_model::table_instantiation(instance):
    assert isinstance(instance, model::Table)

@given(instance=model::Table_strategy)
def test_model::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Table_strategy)
def test_model::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
