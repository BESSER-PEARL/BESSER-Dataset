import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractDataType,
    dbDsl_CharType,
    dbDsl_AbstractColumnMapper,
    dbDsl_AbstractDataType,
    dbDsl_Column,
    dbDsl_Table,
    Root,
    dbDsl_Database,
    dbDsl_Root,
    dbDsl_NumberType,
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



def test_dbdsl_chartype_is_not_abstract():
    assert not inspect.isabstract(dbDsl_CharType)


def test_dbdsl_chartype_constructor_exists():
    assert callable(dbDsl_CharType.__init__)


def test_dbdsl_chartype_constructor_args():
    sig = inspect.signature(dbDsl_CharType.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl_abstractcolumnmapper_is_not_abstract():
    assert not inspect.isabstract(dbDsl_AbstractColumnMapper)


def test_dbdsl_abstractcolumnmapper_constructor_exists():
    assert callable(dbDsl_AbstractColumnMapper.__init__)


def test_dbdsl_abstractcolumnmapper_constructor_args():
    sig = inspect.signature(dbDsl_AbstractColumnMapper.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl_abstractdatatype_is_not_abstract():
    assert not inspect.isabstract(dbDsl_AbstractDataType)


def test_dbdsl_abstractdatatype_constructor_exists():
    assert callable(dbDsl_AbstractDataType.__init__)


def test_dbdsl_abstractdatatype_constructor_args():
    sig = inspect.signature(dbDsl_AbstractDataType.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl_column_is_not_abstract():
    assert not inspect.isabstract(dbDsl_Column)


def test_dbdsl_column_constructor_exists():
    assert callable(dbDsl_Column.__init__)


def test_dbdsl_column_constructor_args():
    sig = inspect.signature(dbDsl_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl_column_has_name():
    assert hasattr(dbDsl_Column, "name")
    descriptor = None
    for klass in dbDsl_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdsl_table_is_not_abstract():
    assert not inspect.isabstract(dbDsl_Table)


def test_dbdsl_table_constructor_exists():
    assert callable(dbDsl_Table.__init__)


def test_dbdsl_table_constructor_args():
    sig = inspect.signature(dbDsl_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl_table_has_name():
    assert hasattr(dbDsl_Table, "name")
    descriptor = None
    for klass in dbDsl_Table.__mro__:
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



def test_dbdsl_database_is_not_abstract():
    assert not inspect.isabstract(dbDsl_Database)


def test_dbdsl_database_constructor_exists():
    assert callable(dbDsl_Database.__init__)


def test_dbdsl_database_constructor_args():
    sig = inspect.signature(dbDsl_Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbdsl_database_has_name():
    assert hasattr(dbDsl_Database, "name")
    descriptor = None
    for klass in dbDsl_Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbdsl_root_is_not_abstract():
    assert not inspect.isabstract(dbDsl_Root)


def test_dbdsl_root_constructor_exists():
    assert callable(dbDsl_Root.__init__)


def test_dbdsl_root_constructor_args():
    sig = inspect.signature(dbDsl_Root.__init__)
    params = list(sig.parameters.keys())



def test_dbdsl_numbertype_is_not_abstract():
    assert not inspect.isabstract(dbDsl_NumberType)


def test_dbdsl_numbertype_constructor_exists():
    assert callable(dbDsl_NumberType.__init__)


def test_dbdsl_numbertype_constructor_args():
    sig = inspect.signature(dbDsl_NumberType.__init__)
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
dbDsl_CharType_strategy = st.builds(
    dbDsl_CharType,
)
dbDsl_AbstractColumnMapper_strategy = st.builds(
    dbDsl_AbstractColumnMapper,
)
dbDsl_AbstractDataType_strategy = st.builds(
    dbDsl_AbstractDataType,
)
dbDsl_Column_strategy = st.builds(
    dbDsl_Column,
    name=
        safe_text
)
dbDsl_Table_strategy = st.builds(
    dbDsl_Table,
    name=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
dbDsl_Database_strategy = st.builds(
    dbDsl_Database,
    name=
        safe_text
)
dbDsl_Root_strategy = st.builds(
    dbDsl_Root,
)
dbDsl_NumberType_strategy = st.builds(
    dbDsl_NumberType,
)

@given(instance=AbstractDataType_strategy)
@settings(max_examples=50)
def test_abstractdatatype_instantiation(instance):
    assert isinstance(instance, AbstractDataType)

@given(instance=dbDsl_CharType_strategy)
@settings(max_examples=50)
def test_dbdsl_chartype_instantiation(instance):
    assert isinstance(instance, dbDsl_CharType)

@given(instance=dbDsl_AbstractColumnMapper_strategy)
@settings(max_examples=50)
def test_dbdsl_abstractcolumnmapper_instantiation(instance):
    assert isinstance(instance, dbDsl_AbstractColumnMapper)

@given(instance=dbDsl_AbstractDataType_strategy)
@settings(max_examples=50)
def test_dbdsl_abstractdatatype_instantiation(instance):
    assert isinstance(instance, dbDsl_AbstractDataType)

@given(instance=dbDsl_Column_strategy)
@settings(max_examples=50)
def test_dbdsl_column_instantiation(instance):
    assert isinstance(instance, dbDsl_Column)



@given(instance=dbDsl_Column_strategy)
def test_dbdsl_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbDsl_Table_strategy)
@settings(max_examples=50)
def test_dbdsl_table_instantiation(instance):
    assert isinstance(instance, dbDsl_Table)



@given(instance=dbDsl_Table_strategy)
def test_dbdsl_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=dbDsl_Database_strategy)
@settings(max_examples=50)
def test_dbdsl_database_instantiation(instance):
    assert isinstance(instance, dbDsl_Database)



@given(instance=dbDsl_Database_strategy)
def test_dbdsl_database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbDsl_Root_strategy)
@settings(max_examples=50)
def test_dbdsl_root_instantiation(instance):
    assert isinstance(instance, dbDsl_Root)

@given(instance=dbDsl_NumberType_strategy)
@settings(max_examples=50)
def test_dbdsl_numbertype_instantiation(instance):
    assert isinstance(instance, dbDsl_NumberType)
