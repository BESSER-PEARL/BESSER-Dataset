import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relational_Named,
    Relational_ERModel,
    Relational_FKey,
    Named,
    Relational_Column,
    Relational_Table,
    Relational_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_relational_ermodel_is_not_abstract():
    assert not inspect.isabstract(Relational_ERModel)


def test_relational_ermodel_constructor_exists():
    assert callable(Relational_ERModel.__init__)


def test_relational_ermodel_constructor_args():
    sig = inspect.signature(Relational_ERModel.__init__)
    params = list(sig.parameters.keys())



def test_relational_fkey_is_not_abstract():
    assert not inspect.isabstract(Relational_FKey)


def test_relational_fkey_constructor_exists():
    assert callable(Relational_FKey.__init__)


def test_relational_fkey_constructor_args():
    sig = inspect.signature(Relational_FKey.__init__)
    params = list(sig.parameters.keys())



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



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(Relational_Table)


def test_relational_table_constructor_exists():
    assert callable(Relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(Relational_Table.__init__)
    params = list(sig.parameters.keys())



def test_relational_type_is_not_abstract():
    assert not inspect.isabstract(Relational_Type)


def test_relational_type_constructor_exists():
    assert callable(Relational_Type.__init__)


def test_relational_type_constructor_args():
    sig = inspect.signature(Relational_Type.__init__)
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
Relational_Named_strategy = st.builds(
    Relational_Named,
    name=
        safe_text
)
Relational_ERModel_strategy = st.builds(
    Relational_ERModel,
)
Relational_FKey_strategy = st.builds(
    Relational_FKey,
)
Named_strategy = st.builds(
    Named,
)
Relational_Column_strategy = st.builds(
    Relational_Column,
)
Relational_Table_strategy = st.builds(
    Relational_Table,
)
Relational_Type_strategy = st.builds(
    Relational_Type,
)

@given(instance=Relational_Named_strategy)
@settings(max_examples=50)
def test_relational_named_instantiation(instance):
    assert isinstance(instance, Relational_Named)



@given(instance=Relational_Named_strategy)
def test_relational_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_ERModel_strategy)
@settings(max_examples=50)
def test_relational_ermodel_instantiation(instance):
    assert isinstance(instance, Relational_ERModel)

@given(instance=Relational_FKey_strategy)
@settings(max_examples=50)
def test_relational_fkey_instantiation(instance):
    assert isinstance(instance, Relational_FKey)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Relational_Column_strategy)
@settings(max_examples=50)
def test_relational_column_instantiation(instance):
    assert isinstance(instance, Relational_Column)

@given(instance=Relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, Relational_Table)

@given(instance=Relational_Type_strategy)
@settings(max_examples=50)
def test_relational_type_instantiation(instance):
    assert isinstance(instance, Relational_Type)
