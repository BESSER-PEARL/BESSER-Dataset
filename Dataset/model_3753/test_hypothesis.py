import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dbmddandroid::NamedElement,
    NamedElement,
    dbmddandroid::Table,
    dbmddandroid::DBScheme,
    dbmddandroid::Column,
    dbmddandroid::Relation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbmddandroid::namedelement_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid::NamedElement)


def test_dbmddandroid::namedelement_constructor_exists():
    assert callable(dbmddandroid::NamedElement.__init__)


def test_dbmddandroid::namedelement_constructor_args():
    sig = inspect.signature(dbmddandroid::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbmddandroid::namedelement_has_name():
    assert hasattr(dbmddandroid::NamedElement, "name")
    descriptor = None
    for klass in dbmddandroid::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbmddandroid::table_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid::Table)


def test_dbmddandroid::table_constructor_exists():
    assert callable(dbmddandroid::Table.__init__)


def test_dbmddandroid::table_constructor_args():
    sig = inspect.signature(dbmddandroid::Table.__init__)
    params = list(sig.parameters.keys())



def test_dbmddandroid::dbscheme_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid::DBScheme)


def test_dbmddandroid::dbscheme_constructor_exists():
    assert callable(dbmddandroid::DBScheme.__init__)


def test_dbmddandroid::dbscheme_constructor_args():
    sig = inspect.signature(dbmddandroid::DBScheme.__init__)
    params = list(sig.parameters.keys())



def test_dbmddandroid::column_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid::Column)


def test_dbmddandroid::column_constructor_exists():
    assert callable(dbmddandroid::Column.__init__)


def test_dbmddandroid::column_constructor_args():
    sig = inspect.signature(dbmddandroid::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dbmddandroid::column_has_type():
    assert hasattr(dbmddandroid::Column, "type")
    descriptor = None
    for klass in dbmddandroid::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dbmddandroid::relation_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid::Relation)


def test_dbmddandroid::relation_constructor_exists():
    assert callable(dbmddandroid::Relation.__init__)


def test_dbmddandroid::relation_constructor_args():
    sig = inspect.signature(dbmddandroid::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "minTargetMultiplicity" in params, "Missing parameter 'minTargetMultiplicity'"
    assert "maxTargetMultiplicity" in params, "Missing parameter 'maxTargetMultiplicity'"
    assert "maxSourceMultiplicity" in params, "Missing parameter 'maxSourceMultiplicity'"
    assert "minSourceMultiplicity" in params, "Missing parameter 'minSourceMultiplicity'"

def test_dbmddandroid::relation_has_minTargetMultiplicity():
    assert hasattr(dbmddandroid::Relation, "minTargetMultiplicity")
    descriptor = None
    for klass in dbmddandroid::Relation.__mro__:
        if "minTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minTargetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_maxTargetMultiplicity():
    assert hasattr(dbmddandroid::Relation, "maxTargetMultiplicity")
    descriptor = None
    for klass in dbmddandroid::Relation.__mro__:
        if "maxTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxTargetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_maxSourceMultiplicity():
    assert hasattr(dbmddandroid::Relation, "maxSourceMultiplicity")
    descriptor = None
    for klass in dbmddandroid::Relation.__mro__:
        if "maxSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxSourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_minSourceMultiplicity():
    assert hasattr(dbmddandroid::Relation, "minSourceMultiplicity")
    descriptor = None
    for klass in dbmddandroid::Relation.__mro__:
        if "minSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minSourceMultiplicity"]
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
dbmddandroid::NamedElement_strategy = st.builds(
    dbmddandroid::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbmddandroid::Table_strategy = st.builds(
    dbmddandroid::Table,
)
dbmddandroid::DBScheme_strategy = st.builds(
    dbmddandroid::DBScheme,
)
dbmddandroid::Column_strategy = st.builds(
    dbmddandroid::Column,
    type=
        safe_text
)
dbmddandroid::Relation_strategy = st.builds(
    dbmddandroid::Relation,
    minTargetMultiplicity=
        st.integers(),
    maxTargetMultiplicity=
        st.integers(),
    maxSourceMultiplicity=
        st.integers(),
    minSourceMultiplicity=
        st.integers()
)

@given(instance=dbmddandroid::NamedElement_strategy)
@settings(max_examples=50)
def test_dbmddandroid::namedelement_instantiation(instance):
    assert isinstance(instance, dbmddandroid::NamedElement)

@given(instance=dbmddandroid::NamedElement_strategy)
def test_dbmddandroid::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbmddandroid::NamedElement_strategy)
def test_dbmddandroid::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbmddandroid::Table_strategy)
@settings(max_examples=50)
def test_dbmddandroid::table_instantiation(instance):
    assert isinstance(instance, dbmddandroid::Table)

@given(instance=dbmddandroid::DBScheme_strategy)
@settings(max_examples=50)
def test_dbmddandroid::dbscheme_instantiation(instance):
    assert isinstance(instance, dbmddandroid::DBScheme)

@given(instance=dbmddandroid::Column_strategy)
@settings(max_examples=50)
def test_dbmddandroid::column_instantiation(instance):
    assert isinstance(instance, dbmddandroid::Column)

@given(instance=dbmddandroid::Column_strategy)
def test_dbmddandroid::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dbmddandroid::Column_strategy)
def test_dbmddandroid::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dbmddandroid::Relation_strategy)
@settings(max_examples=50)
def test_dbmddandroid::relation_instantiation(instance):
    assert isinstance(instance, dbmddandroid::Relation)

@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_minTargetMultiplicity_type(instance):
    assert isinstance(instance.minTargetMultiplicity, int)


@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_minTargetMultiplicity_setter(instance):
    original = instance.minTargetMultiplicity
    instance.minTargetMultiplicity = original
    assert instance.minTargetMultiplicity == original

@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_maxTargetMultiplicity_type(instance):
    assert isinstance(instance.maxTargetMultiplicity, int)


@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_maxTargetMultiplicity_setter(instance):
    original = instance.maxTargetMultiplicity
    instance.maxTargetMultiplicity = original
    assert instance.maxTargetMultiplicity == original

@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_maxSourceMultiplicity_type(instance):
    assert isinstance(instance.maxSourceMultiplicity, int)


@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_maxSourceMultiplicity_setter(instance):
    original = instance.maxSourceMultiplicity
    instance.maxSourceMultiplicity = original
    assert instance.maxSourceMultiplicity == original

@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_minSourceMultiplicity_type(instance):
    assert isinstance(instance.minSourceMultiplicity, int)


@given(instance=dbmddandroid::Relation_strategy)
def test_dbmddandroid::relation_minSourceMultiplicity_setter(instance):
    original = instance.minSourceMultiplicity
    instance.minSourceMultiplicity = original
    assert instance.minSourceMultiplicity == original
