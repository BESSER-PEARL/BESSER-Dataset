import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Diagram,
    model_Constraint,
    model_Column,
    model_Table,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_diagram_is_not_abstract():
    assert not inspect.isabstract(model_Diagram)


def test_model_diagram_constructor_exists():
    assert callable(model_Diagram.__init__)


def test_model_diagram_constructor_args():
    sig = inspect.signature(model_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_model_constraint_is_not_abstract():
    assert not inspect.isabstract(model_Constraint)


def test_model_constraint_constructor_exists():
    assert callable(model_Constraint.__init__)


def test_model_constraint_constructor_args():
    sig = inspect.signature(model_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_model_column_is_not_abstract():
    assert not inspect.isabstract(model_Column)


def test_model_column_constructor_exists():
    assert callable(model_Column.__init__)


def test_model_column_constructor_args():
    sig = inspect.signature(model_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_column_has_name():
    assert hasattr(model_Column, "name")
    descriptor = None
    for klass in model_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_table_is_not_abstract():
    assert not inspect.isabstract(model_Table)


def test_model_table_constructor_exists():
    assert callable(model_Table.__init__)


def test_model_table_constructor_args():
    sig = inspect.signature(model_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_table_has_name():
    assert hasattr(model_Table, "name")
    descriptor = None
    for klass in model_Table.__mro__:
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
model_Diagram_strategy = st.builds(
    model_Diagram,
)
model_Constraint_strategy = st.builds(
    model_Constraint,
)
model_Column_strategy = st.builds(
    model_Column,
    name=
        safe_text
)
model_Table_strategy = st.builds(
    model_Table,
    name=
        safe_text
)

@given(instance=model_Diagram_strategy)
@settings(max_examples=50)
def test_model_diagram_instantiation(instance):
    assert isinstance(instance, model_Diagram)

@given(instance=model_Constraint_strategy)
@settings(max_examples=50)
def test_model_constraint_instantiation(instance):
    assert isinstance(instance, model_Constraint)

@given(instance=model_Column_strategy)
@settings(max_examples=50)
def test_model_column_instantiation(instance):
    assert isinstance(instance, model_Column)



@given(instance=model_Column_strategy)
def test_model_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Table_strategy)
@settings(max_examples=50)
def test_model_table_instantiation(instance):
    assert isinstance(instance, model_Table)



@given(instance=model_Table_strategy)
def test_model_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
