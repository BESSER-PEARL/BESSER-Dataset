import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    necsis14::databaseschema::Column,
    necsis14::databaseschema::NamedElement,
    necsis14::databaseschema::Table,
    necsis14::databaseschema::DatabaseSchema,
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



def test_necsis14::databaseschema::column_is_not_abstract():
    assert not inspect.isabstract(necsis14::databaseschema::Column)


def test_necsis14::databaseschema::column_constructor_exists():
    assert callable(necsis14::databaseschema::Column.__init__)


def test_necsis14::databaseschema::column_constructor_args():
    sig = inspect.signature(necsis14::databaseschema::Column.__init__)
    params = list(sig.parameters.keys())



def test_necsis14::databaseschema::namedelement_is_not_abstract():
    assert not inspect.isabstract(necsis14::databaseschema::NamedElement)


def test_necsis14::databaseschema::namedelement_constructor_exists():
    assert callable(necsis14::databaseschema::NamedElement.__init__)


def test_necsis14::databaseschema::namedelement_constructor_args():
    sig = inspect.signature(necsis14::databaseschema::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_necsis14::databaseschema::namedelement_has_name():
    assert hasattr(necsis14::databaseschema::NamedElement, "name")
    descriptor = None
    for klass in necsis14::databaseschema::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_necsis14::databaseschema::table_is_not_abstract():
    assert not inspect.isabstract(necsis14::databaseschema::Table)


def test_necsis14::databaseschema::table_constructor_exists():
    assert callable(necsis14::databaseschema::Table.__init__)


def test_necsis14::databaseschema::table_constructor_args():
    sig = inspect.signature(necsis14::databaseschema::Table.__init__)
    params = list(sig.parameters.keys())



def test_necsis14::databaseschema::databaseschema_is_not_abstract():
    assert not inspect.isabstract(necsis14::databaseschema::DatabaseSchema)


def test_necsis14::databaseschema::databaseschema_constructor_exists():
    assert callable(necsis14::databaseschema::DatabaseSchema.__init__)


def test_necsis14::databaseschema::databaseschema_constructor_args():
    sig = inspect.signature(necsis14::databaseschema::DatabaseSchema.__init__)
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
necsis14::databaseschema::Column_strategy = st.builds(
    necsis14::databaseschema::Column,
)
necsis14::databaseschema::NamedElement_strategy = st.builds(
    necsis14::databaseschema::NamedElement,
    name=
        safe_text
)
necsis14::databaseschema::Table_strategy = st.builds(
    necsis14::databaseschema::Table,
)
necsis14::databaseschema::DatabaseSchema_strategy = st.builds(
    necsis14::databaseschema::DatabaseSchema,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=necsis14::databaseschema::Column_strategy)
@settings(max_examples=50)
def test_necsis14::databaseschema::column_instantiation(instance):
    assert isinstance(instance, necsis14::databaseschema::Column)

@given(instance=necsis14::databaseschema::NamedElement_strategy)
@settings(max_examples=50)
def test_necsis14::databaseschema::namedelement_instantiation(instance):
    assert isinstance(instance, necsis14::databaseschema::NamedElement)

@given(instance=necsis14::databaseschema::NamedElement_strategy)
def test_necsis14::databaseschema::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=necsis14::databaseschema::NamedElement_strategy)
def test_necsis14::databaseschema::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=necsis14::databaseschema::Table_strategy)
@settings(max_examples=50)
def test_necsis14::databaseschema::table_instantiation(instance):
    assert isinstance(instance, necsis14::databaseschema::Table)

@given(instance=necsis14::databaseschema::DatabaseSchema_strategy)
@settings(max_examples=50)
def test_necsis14::databaseschema::databaseschema_instantiation(instance):
    assert isinstance(instance, necsis14::databaseschema::DatabaseSchema)
