import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DataDefinition,
    DDL_CreateDatabase,
    DDL_CreateColumn,
    DDL_CreateCk,
    DDL_DDLDefinition,
    DDL_CreateCommentColumn,
    DDL_CreateCommentTable,
    DDL_CreateTable,
    DDL_CreateFk,
    DDL_CreatePk,
    Statement,
    DDL_DataDefinition,
    DDL_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DataDefinition)


def test_datadefinition_constructor_exists():
    assert callable(DataDefinition.__init__)


def test_datadefinition_constructor_args():
    sig = inspect.signature(DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl_createdatabase_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateDatabase)


def test_ddl_createdatabase_constructor_exists():
    assert callable(DDL_CreateDatabase.__init__)


def test_ddl_createdatabase_constructor_args():
    sig = inspect.signature(DDL_CreateDatabase.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_ddl_createdatabase_has_databaseName():
    assert hasattr(DDL_CreateDatabase, "databaseName")
    descriptor = None
    for klass in DDL_CreateDatabase.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createcolumn_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateColumn)


def test_ddl_createcolumn_constructor_exists():
    assert callable(DDL_CreateColumn.__init__)


def test_ddl_createcolumn_constructor_args():
    sig = inspect.signature(DDL_CreateColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnNull" in params, "Missing parameter 'columnNull'"
    assert "columnType" in params, "Missing parameter 'columnType'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "commentColumn" in params, "Missing parameter 'commentColumn'"

def test_ddl_createcolumn_has_columnNull():
    assert hasattr(DDL_CreateColumn, "columnNull")
    descriptor = None
    for klass in DDL_CreateColumn.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcolumn_has_columnType():
    assert hasattr(DDL_CreateColumn, "columnType")
    descriptor = None
    for klass in DDL_CreateColumn.__mro__:
        if "columnType" in klass.__dict__:
            descriptor = klass.__dict__["columnType"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcolumn_has_columnName():
    assert hasattr(DDL_CreateColumn, "columnName")
    descriptor = None
    for klass in DDL_CreateColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcolumn_has_commentColumn():
    assert hasattr(DDL_CreateColumn, "commentColumn")
    descriptor = None
    for klass in DDL_CreateColumn.__mro__:
        if "commentColumn" in klass.__dict__:
            descriptor = klass.__dict__["commentColumn"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createck_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateCk)


def test_ddl_createck_constructor_exists():
    assert callable(DDL_CreateCk.__init__)


def test_ddl_createck_constructor_args():
    sig = inspect.signature(DDL_CreateCk.__init__)
    params = list(sig.parameters.keys())
    assert "nameColumn" in params, "Missing parameter 'nameColumn'"
    assert "nameCk" in params, "Missing parameter 'nameCk'"
    assert "valuesCk" in params, "Missing parameter 'valuesCk'"

def test_ddl_createck_has_nameColumn():
    assert hasattr(DDL_CreateCk, "nameColumn")
    descriptor = None
    for klass in DDL_CreateCk.__mro__:
        if "nameColumn" in klass.__dict__:
            descriptor = klass.__dict__["nameColumn"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createck_has_nameCk():
    assert hasattr(DDL_CreateCk, "nameCk")
    descriptor = None
    for klass in DDL_CreateCk.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createck_has_valuesCk():
    assert hasattr(DDL_CreateCk, "valuesCk")
    descriptor = None
    for klass in DDL_CreateCk.__mro__:
        if "valuesCk" in klass.__dict__:
            descriptor = klass.__dict__["valuesCk"]
            break
    assert isinstance(descriptor, property)



def test_ddl_ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DDL_DDLDefinition)


def test_ddl_ddldefinition_constructor_exists():
    assert callable(DDL_DDLDefinition.__init__)


def test_ddl_ddldefinition_constructor_args():
    sig = inspect.signature(DDL_DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl_createcommentcolumn_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateCommentColumn)


def test_ddl_createcommentcolumn_constructor_exists():
    assert callable(DDL_CreateCommentColumn.__init__)


def test_ddl_createcommentcolumn_constructor_args():
    sig = inspect.signature(DDL_CreateCommentColumn.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "columnComment" in params, "Missing parameter 'columnComment'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl_createcommentcolumn_has_tableName():
    assert hasattr(DDL_CreateCommentColumn, "tableName")
    descriptor = None
    for klass in DDL_CreateCommentColumn.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcommentcolumn_has_columnComment():
    assert hasattr(DDL_CreateCommentColumn, "columnComment")
    descriptor = None
    for klass in DDL_CreateCommentColumn.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcommentcolumn_has_columnName():
    assert hasattr(DDL_CreateCommentColumn, "columnName")
    descriptor = None
    for klass in DDL_CreateCommentColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createcommenttable_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateCommentTable)


def test_ddl_createcommenttable_constructor_exists():
    assert callable(DDL_CreateCommentTable.__init__)


def test_ddl_createcommenttable_constructor_args():
    sig = inspect.signature(DDL_CreateCommentTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "tableComment" in params, "Missing parameter 'tableComment'"

def test_ddl_createcommenttable_has_tableName():
    assert hasattr(DDL_CreateCommentTable, "tableName")
    descriptor = None
    for klass in DDL_CreateCommentTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createcommenttable_has_tableComment():
    assert hasattr(DDL_CreateCommentTable, "tableComment")
    descriptor = None
    for klass in DDL_CreateCommentTable.__mro__:
        if "tableComment" in klass.__dict__:
            descriptor = klass.__dict__["tableComment"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createtable_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateTable)


def test_ddl_createtable_constructor_exists():
    assert callable(DDL_CreateTable.__init__)


def test_ddl_createtable_constructor_args():
    sig = inspect.signature(DDL_CreateTable.__init__)
    params = list(sig.parameters.keys())
    assert "commentTable" in params, "Missing parameter 'commentTable'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_ddl_createtable_has_commentTable():
    assert hasattr(DDL_CreateTable, "commentTable")
    descriptor = None
    for klass in DDL_CreateTable.__mro__:
        if "commentTable" in klass.__dict__:
            descriptor = klass.__dict__["commentTable"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createtable_has_tableName():
    assert hasattr(DDL_CreateTable, "tableName")
    descriptor = None
    for klass in DDL_CreateTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createfk_is_not_abstract():
    assert not inspect.isabstract(DDL_CreateFk)


def test_ddl_createfk_constructor_exists():
    assert callable(DDL_CreateFk.__init__)


def test_ddl_createfk_constructor_args():
    sig = inspect.signature(DDL_CreateFk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "columnReference" in params, "Missing parameter 'columnReference'"
    assert "nameFk" in params, "Missing parameter 'nameFk'"

def test_ddl_createfk_has_columnName():
    assert hasattr(DDL_CreateFk, "columnName")
    descriptor = None
    for klass in DDL_CreateFk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createfk_has_columnReference():
    assert hasattr(DDL_CreateFk, "columnReference")
    descriptor = None
    for klass in DDL_CreateFk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createfk_has_nameFk():
    assert hasattr(DDL_CreateFk, "nameFk")
    descriptor = None
    for klass in DDL_CreateFk.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)



def test_ddl_createpk_is_not_abstract():
    assert not inspect.isabstract(DDL_CreatePk)


def test_ddl_createpk_constructor_exists():
    assert callable(DDL_CreatePk.__init__)


def test_ddl_createpk_constructor_args():
    sig = inspect.signature(DDL_CreatePk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "namePk" in params, "Missing parameter 'namePk'"

def test_ddl_createpk_has_columnName():
    assert hasattr(DDL_CreatePk, "columnName")
    descriptor = None
    for klass in DDL_CreatePk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl_createpk_has_namePk():
    assert hasattr(DDL_CreatePk, "namePk")
    descriptor = None
    for klass in DDL_CreatePk.__mro__:
        if "namePk" in klass.__dict__:
            descriptor = klass.__dict__["namePk"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ddl_datadefinition_is_not_abstract():
    assert not inspect.isabstract(DDL_DataDefinition)


def test_ddl_datadefinition_constructor_exists():
    assert callable(DDL_DataDefinition.__init__)


def test_ddl_datadefinition_constructor_args():
    sig = inspect.signature(DDL_DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl_statement_is_not_abstract():
    assert not inspect.isabstract(DDL_Statement)


def test_ddl_statement_constructor_exists():
    assert callable(DDL_Statement.__init__)


def test_ddl_statement_constructor_args():
    sig = inspect.signature(DDL_Statement.__init__)
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
DataDefinition_strategy = st.builds(
    DataDefinition,
)
DDL_CreateDatabase_strategy = st.builds(
    DDL_CreateDatabase,
    databaseName=
        safe_text
)
DDL_CreateColumn_strategy = st.builds(
    DDL_CreateColumn,
    columnNull=
        st.booleans(),
    columnType=
        safe_text,
    columnName=
        safe_text,
    commentColumn=
        safe_text
)
DDL_CreateCk_strategy = st.builds(
    DDL_CreateCk,
    nameColumn=
        safe_text,
    nameCk=
        safe_text,
    valuesCk=
        safe_text
)
DDL_DDLDefinition_strategy = st.builds(
    DDL_DDLDefinition,
)
DDL_CreateCommentColumn_strategy = st.builds(
    DDL_CreateCommentColumn,
    tableName=
        safe_text,
    columnComment=
        safe_text,
    columnName=
        safe_text
)
DDL_CreateCommentTable_strategy = st.builds(
    DDL_CreateCommentTable,
    tableName=
        safe_text,
    tableComment=
        safe_text
)
DDL_CreateTable_strategy = st.builds(
    DDL_CreateTable,
    commentTable=
        safe_text,
    tableName=
        safe_text
)
DDL_CreateFk_strategy = st.builds(
    DDL_CreateFk,
    columnName=
        safe_text,
    columnReference=
        safe_text,
    nameFk=
        safe_text
)
DDL_CreatePk_strategy = st.builds(
    DDL_CreatePk,
    columnName=
        safe_text,
    namePk=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
DDL_DataDefinition_strategy = st.builds(
    DDL_DataDefinition,
)
DDL_Statement_strategy = st.builds(
    DDL_Statement,
)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=DDL_CreateDatabase_strategy)
@settings(max_examples=50)
def test_ddl_createdatabase_instantiation(instance):
    assert isinstance(instance, DDL_CreateDatabase)



@given(instance=DDL_CreateDatabase_strategy)
def test_ddl_createdatabase_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=DDL_CreateColumn_strategy)
@settings(max_examples=50)
def test_ddl_createcolumn_instantiation(instance):
    assert isinstance(instance, DDL_CreateColumn)



@given(instance=DDL_CreateColumn_strategy)
def test_ddl_createcolumn_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original



@given(instance=DDL_CreateColumn_strategy)
def test_ddl_createcolumn_columnType_setter(instance):
    original = instance.columnType
    instance.columnType = original
    assert instance.columnType == original



@given(instance=DDL_CreateColumn_strategy)
def test_ddl_createcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DDL_CreateColumn_strategy)
def test_ddl_createcolumn_commentColumn_setter(instance):
    original = instance.commentColumn
    instance.commentColumn = original
    assert instance.commentColumn == original

@given(instance=DDL_CreateCk_strategy)
@settings(max_examples=50)
def test_ddl_createck_instantiation(instance):
    assert isinstance(instance, DDL_CreateCk)



@given(instance=DDL_CreateCk_strategy)
def test_ddl_createck_nameColumn_setter(instance):
    original = instance.nameColumn
    instance.nameColumn = original
    assert instance.nameColumn == original



@given(instance=DDL_CreateCk_strategy)
def test_ddl_createck_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original



@given(instance=DDL_CreateCk_strategy)
def test_ddl_createck_valuesCk_setter(instance):
    original = instance.valuesCk
    instance.valuesCk = original
    assert instance.valuesCk == original

@given(instance=DDL_DDLDefinition_strategy)
@settings(max_examples=50)
def test_ddl_ddldefinition_instantiation(instance):
    assert isinstance(instance, DDL_DDLDefinition)

@given(instance=DDL_CreateCommentColumn_strategy)
@settings(max_examples=50)
def test_ddl_createcommentcolumn_instantiation(instance):
    assert isinstance(instance, DDL_CreateCommentColumn)



@given(instance=DDL_CreateCommentColumn_strategy)
def test_ddl_createcommentcolumn_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=DDL_CreateCommentColumn_strategy)
def test_ddl_createcommentcolumn_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original



@given(instance=DDL_CreateCommentColumn_strategy)
def test_ddl_createcommentcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL_CreateCommentTable_strategy)
@settings(max_examples=50)
def test_ddl_createcommenttable_instantiation(instance):
    assert isinstance(instance, DDL_CreateCommentTable)



@given(instance=DDL_CreateCommentTable_strategy)
def test_ddl_createcommenttable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=DDL_CreateCommentTable_strategy)
def test_ddl_createcommenttable_tableComment_setter(instance):
    original = instance.tableComment
    instance.tableComment = original
    assert instance.tableComment == original

@given(instance=DDL_CreateTable_strategy)
@settings(max_examples=50)
def test_ddl_createtable_instantiation(instance):
    assert isinstance(instance, DDL_CreateTable)



@given(instance=DDL_CreateTable_strategy)
def test_ddl_createtable_commentTable_setter(instance):
    original = instance.commentTable
    instance.commentTable = original
    assert instance.commentTable == original



@given(instance=DDL_CreateTable_strategy)
def test_ddl_createtable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL_CreateFk_strategy)
@settings(max_examples=50)
def test_ddl_createfk_instantiation(instance):
    assert isinstance(instance, DDL_CreateFk)



@given(instance=DDL_CreateFk_strategy)
def test_ddl_createfk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DDL_CreateFk_strategy)
def test_ddl_createfk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original



@given(instance=DDL_CreateFk_strategy)
def test_ddl_createfk_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original

@given(instance=DDL_CreatePk_strategy)
@settings(max_examples=50)
def test_ddl_createpk_instantiation(instance):
    assert isinstance(instance, DDL_CreatePk)



@given(instance=DDL_CreatePk_strategy)
def test_ddl_createpk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=DDL_CreatePk_strategy)
def test_ddl_createpk_namePk_setter(instance):
    original = instance.namePk
    instance.namePk = original
    assert instance.namePk == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DDL_DataDefinition_strategy)
@settings(max_examples=50)
def test_ddl_datadefinition_instantiation(instance):
    assert isinstance(instance, DDL_DataDefinition)

@given(instance=DDL_Statement_strategy)
@settings(max_examples=50)
def test_ddl_statement_instantiation(instance):
    assert isinstance(instance, DDL_Statement)
