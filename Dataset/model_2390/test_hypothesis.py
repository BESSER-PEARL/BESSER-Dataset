import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    simpleRDBMS::Key,
    simpleRDBMS::Column,
    simpleRDBMS::Table,
    simpleRDBMS::ForeignKey,
    simpleRDBMS::Schema,
    simpleRDBMS::NamedElement,
    simpleRDBMS::RDBMSModel,
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



def test_simplerdbms::key_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::Key)


def test_simplerdbms::key_constructor_exists():
    assert callable(simpleRDBMS::Key.__init__)


def test_simplerdbms::key_constructor_args():
    sig = inspect.signature(simpleRDBMS::Key.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::column_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::Column)


def test_simplerdbms::column_constructor_exists():
    assert callable(simpleRDBMS::Column.__init__)


def test_simplerdbms::column_constructor_args():
    sig = inspect.signature(simpleRDBMS::Column.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::table_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::Table)


def test_simplerdbms::table_constructor_exists():
    assert callable(simpleRDBMS::Table.__init__)


def test_simplerdbms::table_constructor_args():
    sig = inspect.signature(simpleRDBMS::Table.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::ForeignKey)


def test_simplerdbms::foreignkey_constructor_exists():
    assert callable(simpleRDBMS::ForeignKey.__init__)


def test_simplerdbms::foreignkey_constructor_args():
    sig = inspect.signature(simpleRDBMS::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::schema_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::Schema)


def test_simplerdbms::schema_constructor_exists():
    assert callable(simpleRDBMS::Schema.__init__)


def test_simplerdbms::schema_constructor_args():
    sig = inspect.signature(simpleRDBMS::Schema.__init__)
    params = list(sig.parameters.keys())



def test_simplerdbms::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::NamedElement)


def test_simplerdbms::namedelement_constructor_exists():
    assert callable(simpleRDBMS::NamedElement.__init__)


def test_simplerdbms::namedelement_constructor_args():
    sig = inspect.signature(simpleRDBMS::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplerdbms::namedelement_has_name():
    assert hasattr(simpleRDBMS::NamedElement, "name")
    descriptor = None
    for klass in simpleRDBMS::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplerdbms::rdbmsmodel_is_not_abstract():
    assert not inspect.isabstract(simpleRDBMS::RDBMSModel)


def test_simplerdbms::rdbmsmodel_constructor_exists():
    assert callable(simpleRDBMS::RDBMSModel.__init__)


def test_simplerdbms::rdbmsmodel_constructor_args():
    sig = inspect.signature(simpleRDBMS::RDBMSModel.__init__)
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
simpleRDBMS::Key_strategy = st.builds(
    simpleRDBMS::Key,
)
simpleRDBMS::Column_strategy = st.builds(
    simpleRDBMS::Column,
)
simpleRDBMS::Table_strategy = st.builds(
    simpleRDBMS::Table,
)
simpleRDBMS::ForeignKey_strategy = st.builds(
    simpleRDBMS::ForeignKey,
)
simpleRDBMS::Schema_strategy = st.builds(
    simpleRDBMS::Schema,
)
simpleRDBMS::NamedElement_strategy = st.builds(
    simpleRDBMS::NamedElement,
    name=
        safe_text
)
simpleRDBMS::RDBMSModel_strategy = st.builds(
    simpleRDBMS::RDBMSModel,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleRDBMS::Key_strategy)
@settings(max_examples=50)
def test_simplerdbms::key_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::Key)

@given(instance=simpleRDBMS::Column_strategy)
@settings(max_examples=50)
def test_simplerdbms::column_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::Column)

@given(instance=simpleRDBMS::Table_strategy)
@settings(max_examples=50)
def test_simplerdbms::table_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::Table)

@given(instance=simpleRDBMS::ForeignKey_strategy)
@settings(max_examples=50)
def test_simplerdbms::foreignkey_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::ForeignKey)

@given(instance=simpleRDBMS::Schema_strategy)
@settings(max_examples=50)
def test_simplerdbms::schema_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::Schema)

@given(instance=simpleRDBMS::NamedElement_strategy)
@settings(max_examples=50)
def test_simplerdbms::namedelement_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::NamedElement)

@given(instance=simpleRDBMS::NamedElement_strategy)
def test_simplerdbms::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleRDBMS::NamedElement_strategy)
def test_simplerdbms::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleRDBMS::RDBMSModel_strategy)
@settings(max_examples=50)
def test_simplerdbms::rdbmsmodel_instantiation(instance):
    assert isinstance(instance, simpleRDBMS::RDBMSModel)
