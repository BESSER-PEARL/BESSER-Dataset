import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    relationaldatabase::ForeignKey,
    relationaldatabase::Column,
    relationaldatabase::NamedElement,
    relationaldatabase::Table,
    relationaldatabase::RelationalDatabase,
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



def test_relationaldatabase::foreignkey_is_not_abstract():
    assert not inspect.isabstract(relationaldatabase::ForeignKey)


def test_relationaldatabase::foreignkey_constructor_exists():
    assert callable(relationaldatabase::ForeignKey.__init__)


def test_relationaldatabase::foreignkey_constructor_args():
    sig = inspect.signature(relationaldatabase::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relationaldatabase::column_is_not_abstract():
    assert not inspect.isabstract(relationaldatabase::Column)


def test_relationaldatabase::column_constructor_exists():
    assert callable(relationaldatabase::Column.__init__)


def test_relationaldatabase::column_constructor_args():
    sig = inspect.signature(relationaldatabase::Column.__init__)
    params = list(sig.parameters.keys())



def test_relationaldatabase::namedelement_is_not_abstract():
    assert not inspect.isabstract(relationaldatabase::NamedElement)


def test_relationaldatabase::namedelement_constructor_exists():
    assert callable(relationaldatabase::NamedElement.__init__)


def test_relationaldatabase::namedelement_constructor_args():
    sig = inspect.signature(relationaldatabase::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relationaldatabase::namedelement_has_name():
    assert hasattr(relationaldatabase::NamedElement, "name")
    descriptor = None
    for klass in relationaldatabase::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relationaldatabase::table_is_not_abstract():
    assert not inspect.isabstract(relationaldatabase::Table)


def test_relationaldatabase::table_constructor_exists():
    assert callable(relationaldatabase::Table.__init__)


def test_relationaldatabase::table_constructor_args():
    sig = inspect.signature(relationaldatabase::Table.__init__)
    params = list(sig.parameters.keys())



def test_relationaldatabase::relationaldatabase_is_not_abstract():
    assert not inspect.isabstract(relationaldatabase::RelationalDatabase)


def test_relationaldatabase::relationaldatabase_constructor_exists():
    assert callable(relationaldatabase::RelationalDatabase.__init__)


def test_relationaldatabase::relationaldatabase_constructor_args():
    sig = inspect.signature(relationaldatabase::RelationalDatabase.__init__)
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
relationaldatabase::ForeignKey_strategy = st.builds(
    relationaldatabase::ForeignKey,
)
relationaldatabase::Column_strategy = st.builds(
    relationaldatabase::Column,
)
relationaldatabase::NamedElement_strategy = st.builds(
    relationaldatabase::NamedElement,
    name=
        safe_text
)
relationaldatabase::Table_strategy = st.builds(
    relationaldatabase::Table,
)
relationaldatabase::RelationalDatabase_strategy = st.builds(
    relationaldatabase::RelationalDatabase,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=relationaldatabase::ForeignKey_strategy)
@settings(max_examples=50)
def test_relationaldatabase::foreignkey_instantiation(instance):
    assert isinstance(instance, relationaldatabase::ForeignKey)

@given(instance=relationaldatabase::Column_strategy)
@settings(max_examples=50)
def test_relationaldatabase::column_instantiation(instance):
    assert isinstance(instance, relationaldatabase::Column)

@given(instance=relationaldatabase::NamedElement_strategy)
@settings(max_examples=50)
def test_relationaldatabase::namedelement_instantiation(instance):
    assert isinstance(instance, relationaldatabase::NamedElement)

@given(instance=relationaldatabase::NamedElement_strategy)
def test_relationaldatabase::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=relationaldatabase::NamedElement_strategy)
def test_relationaldatabase::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=relationaldatabase::Table_strategy)
@settings(max_examples=50)
def test_relationaldatabase::table_instantiation(instance):
    assert isinstance(instance, relationaldatabase::Table)

@given(instance=relationaldatabase::RelationalDatabase_strategy)
@settings(max_examples=50)
def test_relationaldatabase::relationaldatabase_instantiation(instance):
    assert isinstance(instance, relationaldatabase::RelationalDatabase)
