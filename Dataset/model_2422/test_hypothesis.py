import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ingest::Catalogue,
    ingest::DbColumn,
    ingest::DbTable,
    ingest::DbSchema,
    SqoopHiveImport,
    ingest::SqoopHiveIncrementalImport,
    SqoopImport,
    ingest::SqoopHiveImport,
    ingest::SqoopImport,
    ingest::Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ingest::catalogue_is_not_abstract():
    assert not inspect.isabstract(ingest::Catalogue)


def test_ingest::catalogue_constructor_exists():
    assert callable(ingest::Catalogue.__init__)


def test_ingest::catalogue_constructor_args():
    sig = inspect.signature(ingest::Catalogue.__init__)
    params = list(sig.parameters.keys())



def test_ingest::dbcolumn_is_not_abstract():
    assert not inspect.isabstract(ingest::DbColumn)


def test_ingest::dbcolumn_constructor_exists():
    assert callable(ingest::DbColumn.__init__)


def test_ingest::dbcolumn_constructor_args():
    sig = inspect.signature(ingest::DbColumn.__init__)
    params = list(sig.parameters.keys())
    assert "jdbcScale" in params, "Missing parameter 'jdbcScale'"
    assert "name" in params, "Missing parameter 'name'"
    assert "jdbcType" in params, "Missing parameter 'jdbcType'"
    assert "jdbcPrecision" in params, "Missing parameter 'jdbcPrecision'"

def test_ingest::dbcolumn_has_jdbcScale():
    assert hasattr(ingest::DbColumn, "jdbcScale")
    descriptor = None
    for klass in ingest::DbColumn.__mro__:
        if "jdbcScale" in klass.__dict__:
            descriptor = klass.__dict__["jdbcScale"]
            break
    assert isinstance(descriptor, property)

def test_ingest::dbcolumn_has_name():
    assert hasattr(ingest::DbColumn, "name")
    descriptor = None
    for klass in ingest::DbColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ingest::dbcolumn_has_jdbcType():
    assert hasattr(ingest::DbColumn, "jdbcType")
    descriptor = None
    for klass in ingest::DbColumn.__mro__:
        if "jdbcType" in klass.__dict__:
            descriptor = klass.__dict__["jdbcType"]
            break
    assert isinstance(descriptor, property)

def test_ingest::dbcolumn_has_jdbcPrecision():
    assert hasattr(ingest::DbColumn, "jdbcPrecision")
    descriptor = None
    for klass in ingest::DbColumn.__mro__:
        if "jdbcPrecision" in klass.__dict__:
            descriptor = klass.__dict__["jdbcPrecision"]
            break
    assert isinstance(descriptor, property)



def test_ingest::dbtable_is_not_abstract():
    assert not inspect.isabstract(ingest::DbTable)


def test_ingest::dbtable_constructor_exists():
    assert callable(ingest::DbTable.__init__)


def test_ingest::dbtable_constructor_args():
    sig = inspect.signature(ingest::DbTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ingest::dbtable_has_name():
    assert hasattr(ingest::DbTable, "name")
    descriptor = None
    for klass in ingest::DbTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ingest::dbschema_is_not_abstract():
    assert not inspect.isabstract(ingest::DbSchema)


def test_ingest::dbschema_constructor_exists():
    assert callable(ingest::DbSchema.__init__)


def test_ingest::dbschema_constructor_args():
    sig = inspect.signature(ingest::DbSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ingest::dbschema_has_name():
    assert hasattr(ingest::DbSchema, "name")
    descriptor = None
    for klass in ingest::DbSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqoophiveimport_is_not_abstract():
    assert not inspect.isabstract(SqoopHiveImport)


def test_sqoophiveimport_constructor_exists():
    assert callable(SqoopHiveImport.__init__)


def test_sqoophiveimport_constructor_args():
    sig = inspect.signature(SqoopHiveImport.__init__)
    params = list(sig.parameters.keys())



def test_ingest::sqoophiveincrementalimport_is_not_abstract():
    assert not inspect.isabstract(ingest::SqoopHiveIncrementalImport)


def test_ingest::sqoophiveincrementalimport_constructor_exists():
    assert callable(ingest::SqoopHiveIncrementalImport.__init__)


def test_ingest::sqoophiveincrementalimport_constructor_args():
    sig = inspect.signature(ingest::SqoopHiveIncrementalImport.__init__)
    params = list(sig.parameters.keys())



def test_sqoopimport_is_not_abstract():
    assert not inspect.isabstract(SqoopImport)


def test_sqoopimport_constructor_exists():
    assert callable(SqoopImport.__init__)


def test_sqoopimport_constructor_args():
    sig = inspect.signature(SqoopImport.__init__)
    params = list(sig.parameters.keys())



def test_ingest::sqoophiveimport_is_not_abstract():
    assert not inspect.isabstract(ingest::SqoopHiveImport)


def test_ingest::sqoophiveimport_constructor_exists():
    assert callable(ingest::SqoopHiveImport.__init__)


def test_ingest::sqoophiveimport_constructor_args():
    sig = inspect.signature(ingest::SqoopHiveImport.__init__)
    params = list(sig.parameters.keys())
    assert "targetHiveTable" in params, "Missing parameter 'targetHiveTable'"
    assert "targetHiveDatabase" in params, "Missing parameter 'targetHiveDatabase'"

def test_ingest::sqoophiveimport_has_targetHiveTable():
    assert hasattr(ingest::SqoopHiveImport, "targetHiveTable")
    descriptor = None
    for klass in ingest::SqoopHiveImport.__mro__:
        if "targetHiveTable" in klass.__dict__:
            descriptor = klass.__dict__["targetHiveTable"]
            break
    assert isinstance(descriptor, property)

def test_ingest::sqoophiveimport_has_targetHiveDatabase():
    assert hasattr(ingest::SqoopHiveImport, "targetHiveDatabase")
    descriptor = None
    for klass in ingest::SqoopHiveImport.__mro__:
        if "targetHiveDatabase" in klass.__dict__:
            descriptor = klass.__dict__["targetHiveDatabase"]
            break
    assert isinstance(descriptor, property)



def test_ingest::sqoopimport_is_not_abstract():
    assert not inspect.isabstract(ingest::SqoopImport)


def test_ingest::sqoopimport_constructor_exists():
    assert callable(ingest::SqoopImport.__init__)


def test_ingest::sqoopimport_constructor_args():
    sig = inspect.signature(ingest::SqoopImport.__init__)
    params = list(sig.parameters.keys())



def test_ingest::database_is_not_abstract():
    assert not inspect.isabstract(ingest::Database)


def test_ingest::database_constructor_exists():
    assert callable(ingest::Database.__init__)


def test_ingest::database_constructor_args():
    sig = inspect.signature(ingest::Database.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "jdbcPassword" in params, "Missing parameter 'jdbcPassword'"
    assert "jdbcUrl" in params, "Missing parameter 'jdbcUrl'"
    assert "jdbcUser" in params, "Missing parameter 'jdbcUser'"
    assert "jdbcDriver" in params, "Missing parameter 'jdbcDriver'"

def test_ingest::database_has_label():
    assert hasattr(ingest::Database, "label")
    descriptor = None
    for klass in ingest::Database.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ingest::database_has_jdbcPassword():
    assert hasattr(ingest::Database, "jdbcPassword")
    descriptor = None
    for klass in ingest::Database.__mro__:
        if "jdbcPassword" in klass.__dict__:
            descriptor = klass.__dict__["jdbcPassword"]
            break
    assert isinstance(descriptor, property)

def test_ingest::database_has_jdbcUrl():
    assert hasattr(ingest::Database, "jdbcUrl")
    descriptor = None
    for klass in ingest::Database.__mro__:
        if "jdbcUrl" in klass.__dict__:
            descriptor = klass.__dict__["jdbcUrl"]
            break
    assert isinstance(descriptor, property)

def test_ingest::database_has_jdbcUser():
    assert hasattr(ingest::Database, "jdbcUser")
    descriptor = None
    for klass in ingest::Database.__mro__:
        if "jdbcUser" in klass.__dict__:
            descriptor = klass.__dict__["jdbcUser"]
            break
    assert isinstance(descriptor, property)

def test_ingest::database_has_jdbcDriver():
    assert hasattr(ingest::Database, "jdbcDriver")
    descriptor = None
    for klass in ingest::Database.__mro__:
        if "jdbcDriver" in klass.__dict__:
            descriptor = klass.__dict__["jdbcDriver"]
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
ingest::Catalogue_strategy = st.builds(
    ingest::Catalogue,
)
ingest::DbColumn_strategy = st.builds(
    ingest::DbColumn,
    jdbcScale=
        st.integers(),
    name=
        safe_text,
    jdbcType=
        st.integers(),
    jdbcPrecision=
        st.integers()
)
ingest::DbTable_strategy = st.builds(
    ingest::DbTable,
    name=
        safe_text
)
ingest::DbSchema_strategy = st.builds(
    ingest::DbSchema,
    name=
        safe_text
)
SqoopHiveImport_strategy = st.builds(
    SqoopHiveImport,
)
ingest::SqoopHiveIncrementalImport_strategy = st.builds(
    ingest::SqoopHiveIncrementalImport,
)
SqoopImport_strategy = st.builds(
    SqoopImport,
)
ingest::SqoopHiveImport_strategy = st.builds(
    ingest::SqoopHiveImport,
    targetHiveTable=
        safe_text,
    targetHiveDatabase=
        safe_text
)
ingest::SqoopImport_strategy = st.builds(
    ingest::SqoopImport,
)
ingest::Database_strategy = st.builds(
    ingest::Database,
    label=
        safe_text,
    jdbcPassword=
        safe_text,
    jdbcUrl=
        safe_text,
    jdbcUser=
        safe_text,
    jdbcDriver=
        safe_text
)

@given(instance=ingest::Catalogue_strategy)
@settings(max_examples=50)
def test_ingest::catalogue_instantiation(instance):
    assert isinstance(instance, ingest::Catalogue)

@given(instance=ingest::DbColumn_strategy)
@settings(max_examples=50)
def test_ingest::dbcolumn_instantiation(instance):
    assert isinstance(instance, ingest::DbColumn)

@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcScale_type(instance):
    assert isinstance(instance.jdbcScale, int)


@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcScale_setter(instance):
    original = instance.jdbcScale
    instance.jdbcScale = original
    assert instance.jdbcScale == original

@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcType_type(instance):
    assert isinstance(instance.jdbcType, int)


@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcType_setter(instance):
    original = instance.jdbcType
    instance.jdbcType = original
    assert instance.jdbcType == original

@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcPrecision_type(instance):
    assert isinstance(instance.jdbcPrecision, int)


@given(instance=ingest::DbColumn_strategy)
def test_ingest::dbcolumn_jdbcPrecision_setter(instance):
    original = instance.jdbcPrecision
    instance.jdbcPrecision = original
    assert instance.jdbcPrecision == original

@given(instance=ingest::DbTable_strategy)
@settings(max_examples=50)
def test_ingest::dbtable_instantiation(instance):
    assert isinstance(instance, ingest::DbTable)

@given(instance=ingest::DbTable_strategy)
def test_ingest::dbtable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ingest::DbTable_strategy)
def test_ingest::dbtable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ingest::DbSchema_strategy)
@settings(max_examples=50)
def test_ingest::dbschema_instantiation(instance):
    assert isinstance(instance, ingest::DbSchema)

@given(instance=ingest::DbSchema_strategy)
def test_ingest::dbschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ingest::DbSchema_strategy)
def test_ingest::dbschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqoopHiveImport_strategy)
@settings(max_examples=50)
def test_sqoophiveimport_instantiation(instance):
    assert isinstance(instance, SqoopHiveImport)

@given(instance=ingest::SqoopHiveIncrementalImport_strategy)
@settings(max_examples=50)
def test_ingest::sqoophiveincrementalimport_instantiation(instance):
    assert isinstance(instance, ingest::SqoopHiveIncrementalImport)

@given(instance=SqoopImport_strategy)
@settings(max_examples=50)
def test_sqoopimport_instantiation(instance):
    assert isinstance(instance, SqoopImport)

@given(instance=ingest::SqoopHiveImport_strategy)
@settings(max_examples=50)
def test_ingest::sqoophiveimport_instantiation(instance):
    assert isinstance(instance, ingest::SqoopHiveImport)

@given(instance=ingest::SqoopHiveImport_strategy)
def test_ingest::sqoophiveimport_targetHiveTable_type(instance):
    assert isinstance(instance.targetHiveTable, str)


@given(instance=ingest::SqoopHiveImport_strategy)
def test_ingest::sqoophiveimport_targetHiveTable_setter(instance):
    original = instance.targetHiveTable
    instance.targetHiveTable = original
    assert instance.targetHiveTable == original

@given(instance=ingest::SqoopHiveImport_strategy)
def test_ingest::sqoophiveimport_targetHiveDatabase_type(instance):
    assert isinstance(instance.targetHiveDatabase, str)


@given(instance=ingest::SqoopHiveImport_strategy)
def test_ingest::sqoophiveimport_targetHiveDatabase_setter(instance):
    original = instance.targetHiveDatabase
    instance.targetHiveDatabase = original
    assert instance.targetHiveDatabase == original

@given(instance=ingest::SqoopImport_strategy)
@settings(max_examples=50)
def test_ingest::sqoopimport_instantiation(instance):
    assert isinstance(instance, ingest::SqoopImport)

@given(instance=ingest::Database_strategy)
@settings(max_examples=50)
def test_ingest::database_instantiation(instance):
    assert isinstance(instance, ingest::Database)

@given(instance=ingest::Database_strategy)
def test_ingest::database_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ingest::Database_strategy)
def test_ingest::database_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcPassword_type(instance):
    assert isinstance(instance.jdbcPassword, str)


@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcPassword_setter(instance):
    original = instance.jdbcPassword
    instance.jdbcPassword = original
    assert instance.jdbcPassword == original

@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcUrl_type(instance):
    assert isinstance(instance.jdbcUrl, str)


@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcUrl_setter(instance):
    original = instance.jdbcUrl
    instance.jdbcUrl = original
    assert instance.jdbcUrl == original

@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcUser_type(instance):
    assert isinstance(instance.jdbcUser, str)


@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcUser_setter(instance):
    original = instance.jdbcUser
    instance.jdbcUser = original
    assert instance.jdbcUser == original

@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcDriver_type(instance):
    assert isinstance(instance.jdbcDriver, str)


@given(instance=ingest::Database_strategy)
def test_ingest::database_jdbcDriver_setter(instance):
    original = instance.jdbcDriver
    instance.jdbcDriver = original
    assert instance.jdbcDriver == original
