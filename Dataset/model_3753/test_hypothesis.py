import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dbmddandroid_Relation,
    dbmddandroid_NamedElement,
    NamedElement,
    dbmddandroid_Column,
    dbmddandroid_Table,
    dbmddandroid_DBScheme,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbmddandroid_relation_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid_Relation)


def test_dbmddandroid_relation_constructor_exists():
    assert callable(dbmddandroid_Relation.__init__)


def test_dbmddandroid_relation_constructor_args():
    sig = inspect.signature(dbmddandroid_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "minSourceMultiplicity" in params, "Missing parameter 'minSourceMultiplicity'"
    assert "maxTargetMultiplicity" in params, "Missing parameter 'maxTargetMultiplicity'"
    assert "maxSourceMultiplicity" in params, "Missing parameter 'maxSourceMultiplicity'"
    assert "minTargetMultiplicity" in params, "Missing parameter 'minTargetMultiplicity'"

def test_dbmddandroid_relation_has_minSourceMultiplicity():
    assert hasattr(dbmddandroid_Relation, "minSourceMultiplicity")
    descriptor = None
    for klass in dbmddandroid_Relation.__mro__:
        if "minSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minSourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid_relation_has_maxTargetMultiplicity():
    assert hasattr(dbmddandroid_Relation, "maxTargetMultiplicity")
    descriptor = None
    for klass in dbmddandroid_Relation.__mro__:
        if "maxTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxTargetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid_relation_has_maxSourceMultiplicity():
    assert hasattr(dbmddandroid_Relation, "maxSourceMultiplicity")
    descriptor = None
    for klass in dbmddandroid_Relation.__mro__:
        if "maxSourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxSourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_dbmddandroid_relation_has_minTargetMultiplicity():
    assert hasattr(dbmddandroid_Relation, "minTargetMultiplicity")
    descriptor = None
    for klass in dbmddandroid_Relation.__mro__:
        if "minTargetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["minTargetMultiplicity"]
            break
    assert isinstance(descriptor, property)



def test_dbmddandroid_namedelement_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid_NamedElement)


def test_dbmddandroid_namedelement_constructor_exists():
    assert callable(dbmddandroid_NamedElement.__init__)


def test_dbmddandroid_namedelement_constructor_args():
    sig = inspect.signature(dbmddandroid_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbmddandroid_namedelement_has_name():
    assert hasattr(dbmddandroid_NamedElement, "name")
    descriptor = None
    for klass in dbmddandroid_NamedElement.__mro__:
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



def test_dbmddandroid_column_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid_Column)


def test_dbmddandroid_column_constructor_exists():
    assert callable(dbmddandroid_Column.__init__)


def test_dbmddandroid_column_constructor_args():
    sig = inspect.signature(dbmddandroid_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dbmddandroid_column_has_type():
    assert hasattr(dbmddandroid_Column, "type")
    descriptor = None
    for klass in dbmddandroid_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dbmddandroid_table_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid_Table)


def test_dbmddandroid_table_constructor_exists():
    assert callable(dbmddandroid_Table.__init__)


def test_dbmddandroid_table_constructor_args():
    sig = inspect.signature(dbmddandroid_Table.__init__)
    params = list(sig.parameters.keys())



def test_dbmddandroid_dbscheme_is_not_abstract():
    assert not inspect.isabstract(dbmddandroid_DBScheme)


def test_dbmddandroid_dbscheme_constructor_exists():
    assert callable(dbmddandroid_DBScheme.__init__)


def test_dbmddandroid_dbscheme_constructor_args():
    sig = inspect.signature(dbmddandroid_DBScheme.__init__)
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
dbmddandroid_Relation_strategy = st.builds(
    dbmddandroid_Relation,
    minSourceMultiplicity=
        st.integers(),
    maxTargetMultiplicity=
        st.integers(),
    maxSourceMultiplicity=
        st.integers(),
    minTargetMultiplicity=
        st.integers()
)
dbmddandroid_NamedElement_strategy = st.builds(
    dbmddandroid_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbmddandroid_Column_strategy = st.builds(
    dbmddandroid_Column,
    type=
        safe_text
)
dbmddandroid_Table_strategy = st.builds(
    dbmddandroid_Table,
)
dbmddandroid_DBScheme_strategy = st.builds(
    dbmddandroid_DBScheme,
)

@given(instance=dbmddandroid_Relation_strategy)
@settings(max_examples=50)
def test_dbmddandroid_relation_instantiation(instance):
    assert isinstance(instance, dbmddandroid_Relation)



@given(instance=dbmddandroid_Relation_strategy)
def test_dbmddandroid_relation_minSourceMultiplicity_setter(instance):
    original = instance.minSourceMultiplicity
    instance.minSourceMultiplicity = original
    assert instance.minSourceMultiplicity == original



@given(instance=dbmddandroid_Relation_strategy)
def test_dbmddandroid_relation_maxTargetMultiplicity_setter(instance):
    original = instance.maxTargetMultiplicity
    instance.maxTargetMultiplicity = original
    assert instance.maxTargetMultiplicity == original



@given(instance=dbmddandroid_Relation_strategy)
def test_dbmddandroid_relation_maxSourceMultiplicity_setter(instance):
    original = instance.maxSourceMultiplicity
    instance.maxSourceMultiplicity = original
    assert instance.maxSourceMultiplicity == original



@given(instance=dbmddandroid_Relation_strategy)
def test_dbmddandroid_relation_minTargetMultiplicity_setter(instance):
    original = instance.minTargetMultiplicity
    instance.minTargetMultiplicity = original
    assert instance.minTargetMultiplicity == original

@given(instance=dbmddandroid_NamedElement_strategy)
@settings(max_examples=50)
def test_dbmddandroid_namedelement_instantiation(instance):
    assert isinstance(instance, dbmddandroid_NamedElement)



@given(instance=dbmddandroid_NamedElement_strategy)
def test_dbmddandroid_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbmddandroid_Column_strategy)
@settings(max_examples=50)
def test_dbmddandroid_column_instantiation(instance):
    assert isinstance(instance, dbmddandroid_Column)



@given(instance=dbmddandroid_Column_strategy)
def test_dbmddandroid_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dbmddandroid_Table_strategy)
@settings(max_examples=50)
def test_dbmddandroid_table_instantiation(instance):
    assert isinstance(instance, dbmddandroid_Table)

@given(instance=dbmddandroid_DBScheme_strategy)
@settings(max_examples=50)
def test_dbmddandroid_dbscheme_instantiation(instance):
    assert isinstance(instance, dbmddandroid_DBScheme)
