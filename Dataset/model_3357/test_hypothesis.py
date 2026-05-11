import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractDataType,
    dbDsl::CharType,
    dbDsl::AbstractColumnMapper,
    dbDsl::AbstractDataType,
    dbDsl::Column,
    dbDsl::Table,
    Root,
    dbDsl::Database,
    dbDsl::Root,
    dbDsl::NumberType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractdatatype_is_not_abstract():
    assert not inspect.isabstract(AbstractDataType)


def test_abstractdatatype_constructor_exists():
    assert callable(AbstractDataType.__init__)


def test_abstractdatatype_constructor_args():
    sig = inspect.signature(AbstractDataType.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::chartype_is_not_abstract():
    assert not inspect.isabstract(dbDsl::CharType)


def test_dbdsl::chartype_constructor_exists():
    assert callable(dbDsl::CharType.__init__)


def test_dbdsl::chartype_constructor_args():
    sig = inspect.signature(dbDsl::CharType.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::abstractcolumnmapper_is_not_abstract():
    assert not inspect.isabstract(dbDsl::AbstractColumnMapper)


def test_dbdsl::abstractcolumnmapper_constructor_exists():
    assert callable(dbDsl::AbstractColumnMapper.__init__)


def test_dbdsl::abstractcolumnmapper_constructor_args():
    sig = inspect.signature(dbDsl::AbstractColumnMapper.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::abstractdatatype_is_not_abstract():
    assert not inspect.isabstract(dbDsl::AbstractDataType)


def test_dbdsl::abstractdatatype_constructor_exists():
    assert callable(dbDsl::AbstractDataType.__init__)


def test_dbdsl::abstractdatatype_constructor_args():
    sig = inspect.signature(dbDsl::AbstractDataType.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::column_is_not_abstract():
    assert not inspect.isabstract(dbDsl::Column)


def test_dbdsl::column_constructor_exists():
    assert callable(dbDsl::Column.__init__)


def test_dbdsl::column_constructor_args():
    sig = inspect.signature(dbDsl::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl::column_has_name():
    assert hasattr(dbDsl::Column, "name")
    descriptor = None
    for klass in dbDsl::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdsl::table_is_not_abstract():
    assert not inspect.isabstract(dbDsl::Table)


def test_dbdsl::table_constructor_exists():
    assert callable(dbDsl::Table.__init__)


def test_dbdsl::table_constructor_args():
    sig = inspect.signature(dbDsl::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl::table_has_name():
    assert hasattr(dbDsl::Table, "name")
    descriptor = None
    for klass in dbDsl::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::database_is_not_abstract():
    assert not inspect.isabstract(dbDsl::Database)


def test_dbdsl::database_constructor_exists():
    assert callable(dbDsl::Database.__init__)


def test_dbdsl::database_constructor_args():
    sig = inspect.signature(dbDsl::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl::database_has_name():
    assert hasattr(dbDsl::Database, "name")
    descriptor = None
    for klass in dbDsl::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdsl::root_is_not_abstract():
    assert not inspect.isabstract(dbDsl::Root)


def test_dbdsl::root_constructor_exists():
    assert callable(dbDsl::Root.__init__)


def test_dbdsl::root_constructor_args():
    sig = inspect.signature(dbDsl::Root.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl::numbertype_is_not_abstract():
    assert not inspect.isabstract(dbDsl::NumberType)


def test_dbdsl::numbertype_constructor_exists():
    assert callable(dbDsl::NumberType.__init__)


def test_dbdsl::numbertype_constructor_args():
    sig = inspect.signature(dbDsl::NumberType.__init__)
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
AbstractDataType_strategy = st.builds(
    AbstractDataType,
)
dbDsl::CharType_strategy = st.builds(
    dbDsl::CharType,
)
dbDsl::AbstractColumnMapper_strategy = st.builds(
    dbDsl::AbstractColumnMapper,
)
dbDsl::AbstractDataType_strategy = st.builds(
    dbDsl::AbstractDataType,
)
dbDsl::Column_strategy = st.builds(
    dbDsl::Column,
    name=
        safe_text
)
dbDsl::Table_strategy = st.builds(
    dbDsl::Table,
    name=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
dbDsl::Database_strategy = st.builds(
    dbDsl::Database,
    name=
        safe_text
)
dbDsl::Root_strategy = st.builds(
    dbDsl::Root,
)
dbDsl::NumberType_strategy = st.builds(
    dbDsl::NumberType,
)

@given(instance=AbstractDataType_strategy)
@settings(max_examples=50)
def test_abstractdatatype_instantiation(instance):
    assert isinstance(instance, AbstractDataType)

@given(instance=dbDsl::CharType_strategy)
@settings(max_examples=50)
def test_dbdsl::chartype_instantiation(instance):
    assert isinstance(instance, dbDsl::CharType)

@given(instance=dbDsl::AbstractColumnMapper_strategy)
@settings(max_examples=50)
def test_dbdsl::abstractcolumnmapper_instantiation(instance):
    assert isinstance(instance, dbDsl::AbstractColumnMapper)

@given(instance=dbDsl::AbstractDataType_strategy)
@settings(max_examples=50)
def test_dbdsl::abstractdatatype_instantiation(instance):
    assert isinstance(instance, dbDsl::AbstractDataType)

@given(instance=dbDsl::Column_strategy)
@settings(max_examples=50)
def test_dbdsl::column_instantiation(instance):
    assert isinstance(instance, dbDsl::Column)

@given(instance=dbDsl::Column_strategy)
def test_dbdsl::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbDsl::Column_strategy)
def test_dbdsl::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbDsl::Table_strategy)
@settings(max_examples=50)
def test_dbdsl::table_instantiation(instance):
    assert isinstance(instance, dbDsl::Table)

@given(instance=dbDsl::Table_strategy)
def test_dbdsl::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbDsl::Table_strategy)
def test_dbdsl::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=dbDsl::Database_strategy)
@settings(max_examples=50)
def test_dbdsl::database_instantiation(instance):
    assert isinstance(instance, dbDsl::Database)

@given(instance=dbDsl::Database_strategy)
def test_dbdsl::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbDsl::Database_strategy)
def test_dbdsl::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbDsl::Root_strategy)
@settings(max_examples=50)
def test_dbdsl::root_instantiation(instance):
    assert isinstance(instance, dbDsl::Root)

@given(instance=dbDsl::NumberType_strategy)
@settings(max_examples=50)
def test_dbdsl::numbertype_instantiation(instance):
    assert isinstance(instance, dbDsl::NumberType)
