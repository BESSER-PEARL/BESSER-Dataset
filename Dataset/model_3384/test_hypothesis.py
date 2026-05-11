import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    errors::Error,
    errors::Errores,
    errors::ColumnFk,
    errors::Table,
    Error,
    errors::CheckError,
    errors::ForeignError,
    errors::ValueCk,
    errors::ColumnCk,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errors::error_is_not_abstract():
    assert not inspect.isabstract(errors::Error)


def test_errors::error_constructor_exists():
    assert callable(errors::Error.__init__)


def test_errors::error_constructor_args():
    sig = inspect.signature(errors::Error.__init__)
    params = list(sig.parameters.keys())



def test_errors::errores_is_not_abstract():
    assert not inspect.isabstract(errors::Errores)


def test_errors::errores_constructor_exists():
    assert callable(errors::Errores.__init__)


def test_errors::errores_constructor_args():
    sig = inspect.signature(errors::Errores.__init__)
    params = list(sig.parameters.keys())



def test_errors::columnfk_is_not_abstract():
    assert not inspect.isabstract(errors::ColumnFk)


def test_errors::columnfk_constructor_exists():
    assert callable(errors::ColumnFk.__init__)


def test_errors::columnfk_constructor_args():
    sig = inspect.signature(errors::ColumnFk.__init__)
    params = list(sig.parameters.keys())
    assert "nameColumn" in params, "Missing parameter 'nameColumn'"

def test_errors::columnfk_has_nameColumn():
    assert hasattr(errors::ColumnFk, "nameColumn")
    descriptor = None
    for klass in errors::ColumnFk.__mro__:
        if "nameColumn" in klass.__dict__:
            descriptor = klass.__dict__["nameColumn"]
            break
    assert isinstance(descriptor, property)



def test_errors::table_is_not_abstract():
    assert not inspect.isabstract(errors::Table)


def test_errors::table_constructor_exists():
    assert callable(errors::Table.__init__)


def test_errors::table_constructor_args():
    sig = inspect.signature(errors::Table.__init__)
    params = list(sig.parameters.keys())
    assert "nameTable" in params, "Missing parameter 'nameTable'"

def test_errors::table_has_nameTable():
    assert hasattr(errors::Table, "nameTable")
    descriptor = None
    for klass in errors::Table.__mro__:
        if "nameTable" in klass.__dict__:
            descriptor = klass.__dict__["nameTable"]
            break
    assert isinstance(descriptor, property)



def test_error_is_not_abstract():
    assert not inspect.isabstract(Error)


def test_error_constructor_exists():
    assert callable(Error.__init__)


def test_error_constructor_args():
    sig = inspect.signature(Error.__init__)
    params = list(sig.parameters.keys())



def test_errors::checkerror_is_not_abstract():
    assert not inspect.isabstract(errors::CheckError)


def test_errors::checkerror_constructor_exists():
    assert callable(errors::CheckError.__init__)


def test_errors::checkerror_constructor_args():
    sig = inspect.signature(errors::CheckError.__init__)
    params = list(sig.parameters.keys())
    assert "porcent" in params, "Missing parameter 'porcent'"
    assert "nameTable" in params, "Missing parameter 'nameTable'"
    assert "nameCk" in params, "Missing parameter 'nameCk'"

def test_errors::checkerror_has_porcent():
    assert hasattr(errors::CheckError, "porcent")
    descriptor = None
    for klass in errors::CheckError.__mro__:
        if "porcent" in klass.__dict__:
            descriptor = klass.__dict__["porcent"]
            break
    assert isinstance(descriptor, property)

def test_errors::checkerror_has_nameTable():
    assert hasattr(errors::CheckError, "nameTable")
    descriptor = None
    for klass in errors::CheckError.__mro__:
        if "nameTable" in klass.__dict__:
            descriptor = klass.__dict__["nameTable"]
            break
    assert isinstance(descriptor, property)

def test_errors::checkerror_has_nameCk():
    assert hasattr(errors::CheckError, "nameCk")
    descriptor = None
    for klass in errors::CheckError.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)



def test_errors::foreignerror_is_not_abstract():
    assert not inspect.isabstract(errors::ForeignError)


def test_errors::foreignerror_constructor_exists():
    assert callable(errors::ForeignError.__init__)


def test_errors::foreignerror_constructor_args():
    sig = inspect.signature(errors::ForeignError.__init__)
    params = list(sig.parameters.keys())
    assert "porcent" in params, "Missing parameter 'porcent'"
    assert "nameFk" in params, "Missing parameter 'nameFk'"

def test_errors::foreignerror_has_porcent():
    assert hasattr(errors::ForeignError, "porcent")
    descriptor = None
    for klass in errors::ForeignError.__mro__:
        if "porcent" in klass.__dict__:
            descriptor = klass.__dict__["porcent"]
            break
    assert isinstance(descriptor, property)

def test_errors::foreignerror_has_nameFk():
    assert hasattr(errors::ForeignError, "nameFk")
    descriptor = None
    for klass in errors::ForeignError.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)



def test_errors::valueck_is_not_abstract():
    assert not inspect.isabstract(errors::ValueCk)


def test_errors::valueck_constructor_exists():
    assert callable(errors::ValueCk.__init__)


def test_errors::valueck_constructor_args():
    sig = inspect.signature(errors::ValueCk.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_errors::valueck_has_value():
    assert hasattr(errors::ValueCk, "value")
    descriptor = None
    for klass in errors::ValueCk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_errors::columnck_is_not_abstract():
    assert not inspect.isabstract(errors::ColumnCk)


def test_errors::columnck_constructor_exists():
    assert callable(errors::ColumnCk.__init__)


def test_errors::columnck_constructor_args():
    sig = inspect.signature(errors::ColumnCk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_errors::columnck_has_columnName():
    assert hasattr(errors::ColumnCk, "columnName")
    descriptor = None
    for klass in errors::ColumnCk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
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
errors::Error_strategy = st.builds(
    errors::Error,
)
errors::Errores_strategy = st.builds(
    errors::Errores,
)
errors::ColumnFk_strategy = st.builds(
    errors::ColumnFk,
    nameColumn=
        safe_text
)
errors::Table_strategy = st.builds(
    errors::Table,
    nameTable=
        safe_text
)
Error_strategy = st.builds(
    Error,
)
errors::CheckError_strategy = st.builds(
    errors::CheckError,
    porcent=
        safe_text,
    nameTable=
        safe_text,
    nameCk=
        safe_text
)
errors::ForeignError_strategy = st.builds(
    errors::ForeignError,
    porcent=
        safe_text,
    nameFk=
        safe_text
)
errors::ValueCk_strategy = st.builds(
    errors::ValueCk,
    value=
        safe_text
)
errors::ColumnCk_strategy = st.builds(
    errors::ColumnCk,
    columnName=
        safe_text
)

@given(instance=errors::Error_strategy)
@settings(max_examples=50)
def test_errors::error_instantiation(instance):
    assert isinstance(instance, errors::Error)

@given(instance=errors::Errores_strategy)
@settings(max_examples=50)
def test_errors::errores_instantiation(instance):
    assert isinstance(instance, errors::Errores)

@given(instance=errors::ColumnFk_strategy)
@settings(max_examples=50)
def test_errors::columnfk_instantiation(instance):
    assert isinstance(instance, errors::ColumnFk)

@given(instance=errors::ColumnFk_strategy)
def test_errors::columnfk_nameColumn_type(instance):
    assert isinstance(instance.nameColumn, str)


@given(instance=errors::ColumnFk_strategy)
def test_errors::columnfk_nameColumn_setter(instance):
    original = instance.nameColumn
    instance.nameColumn = original
    assert instance.nameColumn == original

@given(instance=errors::Table_strategy)
@settings(max_examples=50)
def test_errors::table_instantiation(instance):
    assert isinstance(instance, errors::Table)

@given(instance=errors::Table_strategy)
def test_errors::table_nameTable_type(instance):
    assert isinstance(instance.nameTable, str)


@given(instance=errors::Table_strategy)
def test_errors::table_nameTable_setter(instance):
    original = instance.nameTable
    instance.nameTable = original
    assert instance.nameTable == original

@given(instance=Error_strategy)
@settings(max_examples=50)
def test_error_instantiation(instance):
    assert isinstance(instance, Error)

@given(instance=errors::CheckError_strategy)
@settings(max_examples=50)
def test_errors::checkerror_instantiation(instance):
    assert isinstance(instance, errors::CheckError)

@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_porcent_type(instance):
    assert isinstance(instance.porcent, str)


@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_porcent_setter(instance):
    original = instance.porcent
    instance.porcent = original
    assert instance.porcent == original

@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_nameTable_type(instance):
    assert isinstance(instance.nameTable, str)


@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_nameTable_setter(instance):
    original = instance.nameTable
    instance.nameTable = original
    assert instance.nameTable == original

@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_nameCk_type(instance):
    assert isinstance(instance.nameCk, str)


@given(instance=errors::CheckError_strategy)
def test_errors::checkerror_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original

@given(instance=errors::ForeignError_strategy)
@settings(max_examples=50)
def test_errors::foreignerror_instantiation(instance):
    assert isinstance(instance, errors::ForeignError)

@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_porcent_type(instance):
    assert isinstance(instance.porcent, str)


@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_porcent_setter(instance):
    original = instance.porcent
    instance.porcent = original
    assert instance.porcent == original

@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_nameFk_type(instance):
    assert isinstance(instance.nameFk, str)


@given(instance=errors::ForeignError_strategy)
def test_errors::foreignerror_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original

@given(instance=errors::ValueCk_strategy)
@settings(max_examples=50)
def test_errors::valueck_instantiation(instance):
    assert isinstance(instance, errors::ValueCk)

@given(instance=errors::ValueCk_strategy)
def test_errors::valueck_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=errors::ValueCk_strategy)
def test_errors::valueck_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=errors::ColumnCk_strategy)
@settings(max_examples=50)
def test_errors::columnck_instantiation(instance):
    assert isinstance(instance, errors::ColumnCk)

@given(instance=errors::ColumnCk_strategy)
def test_errors::columnck_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=errors::ColumnCk_strategy)
def test_errors::columnck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original
