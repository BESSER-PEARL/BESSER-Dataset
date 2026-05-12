import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ingest_Catalogue,
    ingest_DbColumn,
    ingest_DbTable,
    ingest_DbSchema,
    SqoopHiveImport,
    ingest_SqoopHiveIncrementalImport,
    SqoopImport,
    ingest_SqoopHiveImport,
    ingest_SqoopImport,
    ingest_Database,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ingest_catalogue_is_not_abstract():
    assert not inspect.isabstract(ingest_Catalogue)


def test_ingest_catalogue_constructor_exists():
    assert callable(ingest_Catalogue.__init__)


def test_ingest_catalogue_constructor_args():
    sig = inspect.signature(ingest_Catalogue.__init__)
    params = list(sig.parameters.keys())



def test_ingest_dbcolumn_is_not_abstract():
    assert not inspect.isabstract(ingest_DbColumn)


def test_ingest_dbcolumn_constructor_exists():
    assert callable(ingest_DbColumn.__init__)


def test_ingest_dbcolumn_constructor_args():
    sig = inspect.signature(ingest_DbColumn.__init__)
    params = list(sig.parameters.keys())
    assert "jdbcType" in params, "Missing parameter 'jdbcType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "jdbcPrecision" in params, "Missing parameter 'jdbcPrecision'"
    assert "jdbcScale" in params, "Missing parameter 'jdbcScale'"

def test_ingest_dbcolumn_has_jdbcType():
    assert hasattr(ingest_DbColumn, "jdbcType")
    descriptor = None
    for klass in ingest_DbColumn.__mro__:
        if "jdbcType" in klass.__dict__:
            descriptor = klass.__dict__["jdbcType"]
            break
    assert isinstance(descriptor, property)

def test_ingest_dbcolumn_has_name():
    assert hasattr(ingest_DbColumn, "name")
    descriptor = None
    for klass in ingest_DbColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ingest_dbcolumn_has_jdbcPrecision():
    assert hasattr(ingest_DbColumn, "jdbcPrecision")
    descriptor = None
    for klass in ingest_DbColumn.__mro__:
        if "jdbcPrecision" in klass.__dict__:
            descriptor = klass.__dict__["jdbcPrecision"]
            break
    assert isinstance(descriptor, property)

def test_ingest_dbcolumn_has_jdbcScale():
    assert hasattr(ingest_DbColumn, "jdbcScale")
    descriptor = None
    for klass in ingest_DbColumn.__mro__:
        if "jdbcScale" in klass.__dict__:
            descriptor = klass.__dict__["jdbcScale"]
            break
    assert isinstance(descriptor, property)



def test_ingest_dbtable_is_not_abstract():
    assert not inspect.isabstract(ingest_DbTable)


def test_ingest_dbtable_constructor_exists():
    assert callable(ingest_DbTable.__init__)


def test_ingest_dbtable_constructor_args():
    sig = inspect.signature(ingest_DbTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ingest_dbtable_has_name():
    assert hasattr(ingest_DbTable, "name")
    descriptor = None
    for klass in ingest_DbTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ingest_dbschema_is_not_abstract():
    assert not inspect.isabstract(ingest_DbSchema)


def test_ingest_dbschema_constructor_exists():
    assert callable(ingest_DbSchema.__init__)


def test_ingest_dbschema_constructor_args():
    sig = inspect.signature(ingest_DbSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ingest_dbschema_has_name():
    assert hasattr(ingest_DbSchema, "name")
    descriptor = None
    for klass in ingest_DbSchema.__mro__:
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



def test_ingest_sqoophiveincrementalimport_is_not_abstract():
    assert not inspect.isabstract(ingest_SqoopHiveIncrementalImport)


def test_ingest_sqoophiveincrementalimport_constructor_exists():
    assert callable(ingest_SqoopHiveIncrementalImport.__init__)


def test_ingest_sqoophiveincrementalimport_constructor_args():
    sig = inspect.signature(ingest_SqoopHiveIncrementalImport.__init__)
    params = list(sig.parameters.keys())



def test_sqoopimport_is_not_abstract():
    assert not inspect.isabstract(SqoopImport)


def test_sqoopimport_constructor_exists():
    assert callable(SqoopImport.__init__)


def test_sqoopimport_constructor_args():
    sig = inspect.signature(SqoopImport.__init__)
    params = list(sig.parameters.keys())



def test_ingest_sqoophiveimport_is_not_abstract():
    assert not inspect.isabstract(ingest_SqoopHiveImport)


def test_ingest_sqoophiveimport_constructor_exists():
    assert callable(ingest_SqoopHiveImport.__init__)


def test_ingest_sqoophiveimport_constructor_args():
    sig = inspect.signature(ingest_SqoopHiveImport.__init__)
    params = list(sig.parameters.keys())
    assert "targetHiveTable" in params, "Missing parameter 'targetHiveTable'"
    assert "targetHiveDatabase" in params, "Missing parameter 'targetHiveDatabase'"

def test_ingest_sqoophiveimport_has_targetHiveTable():
    assert hasattr(ingest_SqoopHiveImport, "targetHiveTable")
    descriptor = None
    for klass in ingest_SqoopHiveImport.__mro__:
        if "targetHiveTable" in klass.__dict__:
            descriptor = klass.__dict__["targetHiveTable"]
            break
    assert isinstance(descriptor, property)

def test_ingest_sqoophiveimport_has_targetHiveDatabase():
    assert hasattr(ingest_SqoopHiveImport, "targetHiveDatabase")
    descriptor = None
    for klass in ingest_SqoopHiveImport.__mro__:
        if "targetHiveDatabase" in klass.__dict__:
            descriptor = klass.__dict__["targetHiveDatabase"]
            break
    assert isinstance(descriptor, property)



def test_ingest_sqoopimport_is_not_abstract():
    assert not inspect.isabstract(ingest_SqoopImport)


def test_ingest_sqoopimport_constructor_exists():
    assert callable(ingest_SqoopImport.__init__)


def test_ingest_sqoopimport_constructor_args():
    sig = inspect.signature(ingest_SqoopImport.__init__)
    params = list(sig.parameters.keys())



def test_ingest_database_is_not_abstract():
    assert not inspect.isabstract(ingest_Database)


def test_ingest_database_constructor_exists():
    assert callable(ingest_Database.__init__)


def test_ingest_database_constructor_args():
    sig = inspect.signature(ingest_Database.__init__)
    params = list(sig.parameters.keys())
    assert "jdbcUrl" in params, "Missing parameter 'jdbcUrl'"
    assert "jdbcUser" in params, "Missing parameter 'jdbcUser'"
    assert "jdbcDriver" in params, "Missing parameter 'jdbcDriver'"
    assert "jdbcPassword" in params, "Missing parameter 'jdbcPassword'"
    assert "label" in params, "Missing parameter 'label'"

def test_ingest_database_has_jdbcUrl():
    assert hasattr(ingest_Database, "jdbcUrl")
    descriptor = None
    for klass in ingest_Database.__mro__:
        if "jdbcUrl" in klass.__dict__:
            descriptor = klass.__dict__["jdbcUrl"]
            break
    assert isinstance(descriptor, property)

def test_ingest_database_has_jdbcUser():
    assert hasattr(ingest_Database, "jdbcUser")
    descriptor = None
    for klass in ingest_Database.__mro__:
        if "jdbcUser" in klass.__dict__:
            descriptor = klass.__dict__["jdbcUser"]
            break
    assert isinstance(descriptor, property)

def test_ingest_database_has_jdbcDriver():
    assert hasattr(ingest_Database, "jdbcDriver")
    descriptor = None
    for klass in ingest_Database.__mro__:
        if "jdbcDriver" in klass.__dict__:
            descriptor = klass.__dict__["jdbcDriver"]
            break
    assert isinstance(descriptor, property)

def test_ingest_database_has_jdbcPassword():
    assert hasattr(ingest_Database, "jdbcPassword")
    descriptor = None
    for klass in ingest_Database.__mro__:
        if "jdbcPassword" in klass.__dict__:
            descriptor = klass.__dict__["jdbcPassword"]
            break
    assert isinstance(descriptor, property)

def test_ingest_database_has_label():
    assert hasattr(ingest_Database, "label")
    descriptor = None
    for klass in ingest_Database.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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
ingest_Catalogue_strategy = st.builds(
    ingest_Catalogue,
)
ingest_DbColumn_strategy = st.builds(
    ingest_DbColumn,
    jdbcType=
        st.integers(),
    name=
        safe_text,
    jdbcPrecision=
        st.integers(),
    jdbcScale=
        st.integers()
)
ingest_DbTable_strategy = st.builds(
    ingest_DbTable,
    name=
        safe_text
)
ingest_DbSchema_strategy = st.builds(
    ingest_DbSchema,
    name=
        safe_text
)
SqoopHiveImport_strategy = st.builds(
    SqoopHiveImport,
)
ingest_SqoopHiveIncrementalImport_strategy = st.builds(
    ingest_SqoopHiveIncrementalImport,
)
SqoopImport_strategy = st.builds(
    SqoopImport,
)
ingest_SqoopHiveImport_strategy = st.builds(
    ingest_SqoopHiveImport,
    targetHiveTable=
        safe_text,
    targetHiveDatabase=
        safe_text
)
ingest_SqoopImport_strategy = st.builds(
    ingest_SqoopImport,
)
ingest_Database_strategy = st.builds(
    ingest_Database,
    jdbcUrl=
        safe_text,
    jdbcUser=
        safe_text,
    jdbcDriver=
        safe_text,
    jdbcPassword=
        safe_text,
    label=
        safe_text
)

@given(instance=ingest_Catalogue_strategy)
@settings(max_examples=50)
def test_ingest_catalogue_instantiation(instance):
    assert isinstance(instance, ingest_Catalogue)

@given(instance=ingest_DbColumn_strategy)
@settings(max_examples=50)
def test_ingest_dbcolumn_instantiation(instance):
    assert isinstance(instance, ingest_DbColumn)



@given(instance=ingest_DbColumn_strategy)
def test_ingest_dbcolumn_jdbcType_setter(instance):
    original = instance.jdbcType
    instance.jdbcType = original
    assert instance.jdbcType == original



@given(instance=ingest_DbColumn_strategy)
def test_ingest_dbcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ingest_DbColumn_strategy)
def test_ingest_dbcolumn_jdbcPrecision_setter(instance):
    original = instance.jdbcPrecision
    instance.jdbcPrecision = original
    assert instance.jdbcPrecision == original



@given(instance=ingest_DbColumn_strategy)
def test_ingest_dbcolumn_jdbcScale_setter(instance):
    original = instance.jdbcScale
    instance.jdbcScale = original
    assert instance.jdbcScale == original

@given(instance=ingest_DbTable_strategy)
@settings(max_examples=50)
def test_ingest_dbtable_instantiation(instance):
    assert isinstance(instance, ingest_DbTable)



@given(instance=ingest_DbTable_strategy)
def test_ingest_dbtable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ingest_DbSchema_strategy)
@settings(max_examples=50)
def test_ingest_dbschema_instantiation(instance):
    assert isinstance(instance, ingest_DbSchema)



@given(instance=ingest_DbSchema_strategy)
def test_ingest_dbschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SqoopHiveImport_strategy)
@settings(max_examples=50)
def test_sqoophiveimport_instantiation(instance):
    assert isinstance(instance, SqoopHiveImport)

@given(instance=ingest_SqoopHiveIncrementalImport_strategy)
@settings(max_examples=50)
def test_ingest_sqoophiveincrementalimport_instantiation(instance):
    assert isinstance(instance, ingest_SqoopHiveIncrementalImport)

@given(instance=SqoopImport_strategy)
@settings(max_examples=50)
def test_sqoopimport_instantiation(instance):
    assert isinstance(instance, SqoopImport)

@given(instance=ingest_SqoopHiveImport_strategy)
@settings(max_examples=50)
def test_ingest_sqoophiveimport_instantiation(instance):
    assert isinstance(instance, ingest_SqoopHiveImport)



@given(instance=ingest_SqoopHiveImport_strategy)
def test_ingest_sqoophiveimport_targetHiveTable_setter(instance):
    original = instance.targetHiveTable
    instance.targetHiveTable = original
    assert instance.targetHiveTable == original



@given(instance=ingest_SqoopHiveImport_strategy)
def test_ingest_sqoophiveimport_targetHiveDatabase_setter(instance):
    original = instance.targetHiveDatabase
    instance.targetHiveDatabase = original
    assert instance.targetHiveDatabase == original

@given(instance=ingest_SqoopImport_strategy)
@settings(max_examples=50)
def test_ingest_sqoopimport_instantiation(instance):
    assert isinstance(instance, ingest_SqoopImport)

@given(instance=ingest_Database_strategy)
@settings(max_examples=50)
def test_ingest_database_instantiation(instance):
    assert isinstance(instance, ingest_Database)



@given(instance=ingest_Database_strategy)
def test_ingest_database_jdbcUrl_setter(instance):
    original = instance.jdbcUrl
    instance.jdbcUrl = original
    assert instance.jdbcUrl == original



@given(instance=ingest_Database_strategy)
def test_ingest_database_jdbcUser_setter(instance):
    original = instance.jdbcUser
    instance.jdbcUser = original
    assert instance.jdbcUser == original



@given(instance=ingest_Database_strategy)
def test_ingest_database_jdbcDriver_setter(instance):
    original = instance.jdbcDriver
    instance.jdbcDriver = original
    assert instance.jdbcDriver == original



@given(instance=ingest_Database_strategy)
def test_ingest_database_jdbcPassword_setter(instance):
    original = instance.jdbcPassword
    instance.jdbcPassword = original
    assert instance.jdbcPassword == original



@given(instance=ingest_Database_strategy)
def test_ingest_database_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
