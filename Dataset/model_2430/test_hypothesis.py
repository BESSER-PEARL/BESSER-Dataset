import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    necsis14_databaseschema_Column,
    necsis14_databaseschema_NamedElement,
    necsis14_databaseschema_Table,
    necsis14_databaseschema_DatabaseSchema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_necsis14_databaseschema_column_is_not_abstract():
    assert not inspect.isabstract(necsis14_databaseschema_Column)


def test_necsis14_databaseschema_column_constructor_exists():
    assert callable(necsis14_databaseschema_Column.__init__)


def test_necsis14_databaseschema_column_constructor_args():
    sig = inspect.signature(necsis14_databaseschema_Column.__init__)
    params = list(sig.parameters.keys())



def test_necsis14_databaseschema_namedelement_is_not_abstract():
    assert not inspect.isabstract(necsis14_databaseschema_NamedElement)


def test_necsis14_databaseschema_namedelement_constructor_exists():
    assert callable(necsis14_databaseschema_NamedElement.__init__)


def test_necsis14_databaseschema_namedelement_constructor_args():
    sig = inspect.signature(necsis14_databaseschema_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_necsis14_databaseschema_namedelement_has_name():
    assert hasattr(necsis14_databaseschema_NamedElement, "name")
    descriptor = None
    for klass in necsis14_databaseschema_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_necsis14_databaseschema_table_is_not_abstract():
    assert not inspect.isabstract(necsis14_databaseschema_Table)


def test_necsis14_databaseschema_table_constructor_exists():
    assert callable(necsis14_databaseschema_Table.__init__)


def test_necsis14_databaseschema_table_constructor_args():
    sig = inspect.signature(necsis14_databaseschema_Table.__init__)
    params = list(sig.parameters.keys())



def test_necsis14_databaseschema_databaseschema_is_not_abstract():
    assert not inspect.isabstract(necsis14_databaseschema_DatabaseSchema)


def test_necsis14_databaseschema_databaseschema_constructor_exists():
    assert callable(necsis14_databaseschema_DatabaseSchema.__init__)


def test_necsis14_databaseschema_databaseschema_constructor_args():
    sig = inspect.signature(necsis14_databaseschema_DatabaseSchema.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
necsis14_databaseschema_Column_strategy = st.builds(
    necsis14_databaseschema_Column,
)
necsis14_databaseschema_NamedElement_strategy = st.builds(
    necsis14_databaseschema_NamedElement,
    name=
        safe_text
)
necsis14_databaseschema_Table_strategy = st.builds(
    necsis14_databaseschema_Table,
)
necsis14_databaseschema_DatabaseSchema_strategy = st.builds(
    necsis14_databaseschema_DatabaseSchema,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=necsis14_databaseschema_Column_strategy)
@settings(max_examples=50)
def test_necsis14_databaseschema_column_instantiation(instance):
    assert isinstance(instance, necsis14_databaseschema_Column)

@given(instance=necsis14_databaseschema_NamedElement_strategy)
@settings(max_examples=50)
def test_necsis14_databaseschema_namedelement_instantiation(instance):
    assert isinstance(instance, necsis14_databaseschema_NamedElement)



@given(instance=necsis14_databaseschema_NamedElement_strategy)
def test_necsis14_databaseschema_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=necsis14_databaseschema_Table_strategy)
@settings(max_examples=50)
def test_necsis14_databaseschema_table_instantiation(instance):
    assert isinstance(instance, necsis14_databaseschema_Table)

@given(instance=necsis14_databaseschema_DatabaseSchema_strategy)
@settings(max_examples=50)
def test_necsis14_databaseschema_databaseschema_instantiation(instance):
    assert isinstance(instance, necsis14_databaseschema_DatabaseSchema)
