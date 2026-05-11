import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DbMddAndroid::NamedElement,
    DbMddAndroid::Relation,
    NamedElement,
    DbMddAndroid::Table,
    DbMddAndroid::Column,
    DbMddAndroid::DBScheme,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbmddandroid::namedelement_is_not_abstract():
    assert not inspect.isabstract(DbMddAndroid::NamedElement)


def test_dbmddandroid::namedelement_constructor_exists():
    assert callable(DbMddAndroid::NamedElement.__init__)


def test_dbmddandroid::namedelement_constructor_args():
    sig = inspect.signature(DbMddAndroid::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbmddandroid::namedelement_has_name():
    assert hasattr(DbMddAndroid::NamedElement, "name")
    descriptor = None
    for klass in DbMddAndroid::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbmddandroid::relation_is_not_abstract():
    assert not inspect.isabstract(DbMddAndroid::Relation)


def test_dbmddandroid::relation_constructor_exists():
    assert callable(DbMddAndroid::Relation.__init__)


def test_dbmddandroid::relation_constructor_args():
    sig = inspect.signature(DbMddAndroid::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "maxSourceMultiplicity" in params, "Missing parameter 'maxSourceMultiplicity'"
    assert "minTargetMultiplicity" in params, "Missing parameter 'minTargetMultiplicity'"
    assert "minSourceMultiplicity" in params, "Missing parameter 'minSourceMultiplicity'"
    assert "maxTargetMultiplicity" in params, "Missing parameter 'maxTargetMultiplicity'"

def test_dbmddandroid::relation_has_maxSourceMultiplicity():
    assert hasattr(DbMddAndroid::Relation, "maxSourceMultiplicity")
    descriptor = None
    for klass in DbMddAndroid::Relation.__mro__:
        if "maxSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxSourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_minTargetMultiplicity():
    assert hasattr(DbMddAndroid::Relation, "minTargetMultiplicity")
    descriptor = None
    for klass in DbMddAndroid::Relation.__mro__:
        if "minTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minTargetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_minSourceMultiplicity():
    assert hasattr(DbMddAndroid::Relation, "minSourceMultiplicity")
    descriptor = None
    for klass in DbMddAndroid::Relation.__mro__:
        if "minSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minSourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid::relation_has_maxTargetMultiplicity():
    assert hasattr(DbMddAndroid::Relation, "maxTargetMultiplicity")
    descriptor = None
    for klass in DbMddAndroid::Relation.__mro__:
        if "maxTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxTargetMultiplicity"]
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
    assert not inspect.isabstract(DbMddAndroid::Table)


def test_dbmddandroid::table_constructor_exists():
    assert callable(DbMddAndroid::Table.__init__)


def test_dbmddandroid::table_constructor_args():
    sig = inspect.signature(DbMddAndroid::Table.__init__)
    params = list(sig.parameters.keys())



def test_dbmddandroid::column_is_not_abstract():
    assert not inspect.isabstract(DbMddAndroid::Column)


def test_dbmddandroid::column_constructor_exists():
    assert callable(DbMddAndroid::Column.__init__)


def test_dbmddandroid::column_constructor_args():
    sig = inspect.signature(DbMddAndroid::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dbmddandroid::column_has_type():
    assert hasattr(DbMddAndroid::Column, "type")
    descriptor = None
    for klass in DbMddAndroid::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dbmddandroid::dbscheme_is_not_abstract():
    assert not inspect.isabstract(DbMddAndroid::DBScheme)


def test_dbmddandroid::dbscheme_constructor_exists():
    assert callable(DbMddAndroid::DBScheme.__init__)


def test_dbmddandroid::dbscheme_constructor_args():
    sig = inspect.signature(DbMddAndroid::DBScheme.__init__)
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
DbMddAndroid::NamedElement_strategy = st.builds(
    DbMddAndroid::NamedElement,
    name=
        safe_text
)
DbMddAndroid::Relation_strategy = st.builds(
    DbMddAndroid::Relation,
    maxSourceMultiplicity=
        st.integers(),
    minTargetMultiplicity=
        st.integers(),
    minSourceMultiplicity=
        st.integers(),
    maxTargetMultiplicity=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
DbMddAndroid::Table_strategy = st.builds(
    DbMddAndroid::Table,
)
DbMddAndroid::Column_strategy = st.builds(
    DbMddAndroid::Column,
    type=
        safe_text
)
DbMddAndroid::DBScheme_strategy = st.builds(
    DbMddAndroid::DBScheme,
)

@given(instance=DbMddAndroid::NamedElement_strategy)
@settings(max_examples=50)
def test_dbmddandroid::namedelement_instantiation(instance):
    assert isinstance(instance, DbMddAndroid::NamedElement)

@given(instance=DbMddAndroid::NamedElement_strategy)
def test_dbmddandroid::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DbMddAndroid::NamedElement_strategy)
def test_dbmddandroid::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DbMddAndroid::Relation_strategy)
@settings(max_examples=50)
def test_dbmddandroid::relation_instantiation(instance):
    assert isinstance(instance, DbMddAndroid::Relation)

@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_maxSourceMultiplicity_type(instance):
    assert isinstance(instance.maxSourceMultiplicity, int)


@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_maxSourceMultiplicity_setter(instance):
    original = instance.maxSourceMultiplicity
    instance.maxSourceMultiplicity = original
    assert instance.maxSourceMultiplicity == original

@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_minTargetMultiplicity_type(instance):
    assert isinstance(instance.minTargetMultiplicity, int)


@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_minTargetMultiplicity_setter(instance):
    original = instance.minTargetMultiplicity
    instance.minTargetMultiplicity = original
    assert instance.minTargetMultiplicity == original

@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_minSourceMultiplicity_type(instance):
    assert isinstance(instance.minSourceMultiplicity, int)


@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_minSourceMultiplicity_setter(instance):
    original = instance.minSourceMultiplicity
    instance.minSourceMultiplicity = original
    assert instance.minSourceMultiplicity == original

@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_maxTargetMultiplicity_type(instance):
    assert isinstance(instance.maxTargetMultiplicity, int)


@given(instance=DbMddAndroid::Relation_strategy)
def test_dbmddandroid::relation_maxTargetMultiplicity_setter(instance):
    original = instance.maxTargetMultiplicity
    instance.maxTargetMultiplicity = original
    assert instance.maxTargetMultiplicity == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=DbMddAndroid::Table_strategy)
@settings(max_examples=50)
def test_dbmddandroid::table_instantiation(instance):
    assert isinstance(instance, DbMddAndroid::Table)

@given(instance=DbMddAndroid::Column_strategy)
@settings(max_examples=50)
def test_dbmddandroid::column_instantiation(instance):
    assert isinstance(instance, DbMddAndroid::Column)

@given(instance=DbMddAndroid::Column_strategy)
def test_dbmddandroid::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=DbMddAndroid::Column_strategy)
def test_dbmddandroid::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DbMddAndroid::DBScheme_strategy)
@settings(max_examples=50)
def test_dbmddandroid::dbscheme_instantiation(instance):
    assert isinstance(instance, DbMddAndroid::DBScheme)
