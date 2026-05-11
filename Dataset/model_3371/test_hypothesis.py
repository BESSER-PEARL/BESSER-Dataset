import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataDefinition,
    DDL::CreateDatabase,
    DDL::CreateColumn,
    DDL::CreateCk,
    DDL::CreateTable,
    DDL::CreateFk,
    DDL::CreatePk,
    Statement,
    DDL::DataDefinition,
    DDL::Statement,
    DDL::DDLDefinition,
    DDL::CreateCommentColumn,
    DDL::CreateCommentTable,
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



def test_ddl::createdatabase_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateDatabase)


def test_ddl::createdatabase_constructor_exists():
    assert callable(DDL::CreateDatabase.__init__)


def test_ddl::createdatabase_constructor_args():
    sig = inspect.signature(DDL::CreateDatabase.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"

def test_ddl::createdatabase_has_databaseName():
    assert hasattr(DDL::CreateDatabase, "databaseName")
    descriptor = None
    for klass in DDL::CreateDatabase.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createcolumn_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateColumn)


def test_ddl::createcolumn_constructor_exists():
    assert callable(DDL::CreateColumn.__init__)


def test_ddl::createcolumn_constructor_args():
    sig = inspect.signature(DDL::CreateColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "columnType" in params, "Missing parameter 'columnType'"
    assert "commentColumn" in params, "Missing parameter 'commentColumn'"
    assert "columnNull" in params, "Missing parameter 'columnNull'"

def test_ddl::createcolumn_has_columnName():
    assert hasattr(DDL::CreateColumn, "columnName")
    descriptor = None
    for klass in DDL::CreateColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcolumn_has_columnType():
    assert hasattr(DDL::CreateColumn, "columnType")
    descriptor = None
    for klass in DDL::CreateColumn.__mro__:
        if "columnType" in klass.__dict__:
            descriptor = klass.__dict__["columnType"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcolumn_has_commentColumn():
    assert hasattr(DDL::CreateColumn, "commentColumn")
    descriptor = None
    for klass in DDL::CreateColumn.__mro__:
        if "commentColumn" in klass.__dict__:
            descriptor = klass.__dict__["commentColumn"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcolumn_has_columnNull():
    assert hasattr(DDL::CreateColumn, "columnNull")
    descriptor = None
    for klass in DDL::CreateColumn.__mro__:
        if "columnNull" in klass.__dict__:
            descriptor = klass.__dict__["columnNull"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createck_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateCk)


def test_ddl::createck_constructor_exists():
    assert callable(DDL::CreateCk.__init__)


def test_ddl::createck_constructor_args():
    sig = inspect.signature(DDL::CreateCk.__init__)
    params = list(sig.parameters.keys())
    assert "nameCk" in params, "Missing parameter 'nameCk'"
    assert "valuesCk" in params, "Missing parameter 'valuesCk'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl::createck_has_nameCk():
    assert hasattr(DDL::CreateCk, "nameCk")
    descriptor = None
    for klass in DDL::CreateCk.__mro__:
        if "nameCk" in klass.__dict__:
            descriptor = klass.__dict__["nameCk"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createck_has_valuesCk():
    assert hasattr(DDL::CreateCk, "valuesCk")
    descriptor = None
    for klass in DDL::CreateCk.__mro__:
        if "valuesCk" in klass.__dict__:
            descriptor = klass.__dict__["valuesCk"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createck_has_columnName():
    assert hasattr(DDL::CreateCk, "columnName")
    descriptor = None
    for klass in DDL::CreateCk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createtable_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateTable)


def test_ddl::createtable_constructor_exists():
    assert callable(DDL::CreateTable.__init__)


def test_ddl::createtable_constructor_args():
    sig = inspect.signature(DDL::CreateTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "commentTable" in params, "Missing parameter 'commentTable'"

def test_ddl::createtable_has_tableName():
    assert hasattr(DDL::CreateTable, "tableName")
    descriptor = None
    for klass in DDL::CreateTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createtable_has_commentTable():
    assert hasattr(DDL::CreateTable, "commentTable")
    descriptor = None
    for klass in DDL::CreateTable.__mro__:
        if "commentTable" in klass.__dict__:
            descriptor = klass.__dict__["commentTable"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createfk_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateFk)


def test_ddl::createfk_constructor_exists():
    assert callable(DDL::CreateFk.__init__)


def test_ddl::createfk_constructor_args():
    sig = inspect.signature(DDL::CreateFk.__init__)
    params = list(sig.parameters.keys())
    assert "columnReference" in params, "Missing parameter 'columnReference'"
    assert "nameFk" in params, "Missing parameter 'nameFk'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_ddl::createfk_has_columnReference():
    assert hasattr(DDL::CreateFk, "columnReference")
    descriptor = None
    for klass in DDL::CreateFk.__mro__:
        if "columnReference" in klass.__dict__:
            descriptor = klass.__dict__["columnReference"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createfk_has_nameFk():
    assert hasattr(DDL::CreateFk, "nameFk")
    descriptor = None
    for klass in DDL::CreateFk.__mro__:
        if "nameFk" in klass.__dict__:
            descriptor = klass.__dict__["nameFk"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createfk_has_columnName():
    assert hasattr(DDL::CreateFk, "columnName")
    descriptor = None
    for klass in DDL::CreateFk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createpk_is_not_abstract():
    assert not inspect.isabstract(DDL::CreatePk)


def test_ddl::createpk_constructor_exists():
    assert callable(DDL::CreatePk.__init__)


def test_ddl::createpk_constructor_args():
    sig = inspect.signature(DDL::CreatePk.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "namePk" in params, "Missing parameter 'namePk'"

def test_ddl::createpk_has_columnName():
    assert hasattr(DDL::CreatePk, "columnName")
    descriptor = None
    for klass in DDL::CreatePk.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createpk_has_namePk():
    assert hasattr(DDL::CreatePk, "namePk")
    descriptor = None
    for klass in DDL::CreatePk.__mro__:
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



def test_ddl::datadefinition_is_not_abstract():
    assert not inspect.isabstract(DDL::DataDefinition)


def test_ddl::datadefinition_constructor_exists():
    assert callable(DDL::DataDefinition.__init__)


def test_ddl::datadefinition_constructor_args():
    sig = inspect.signature(DDL::DataDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::statement_is_not_abstract():
    assert not inspect.isabstract(DDL::Statement)


def test_ddl::statement_constructor_exists():
    assert callable(DDL::Statement.__init__)


def test_ddl::statement_constructor_args():
    sig = inspect.signature(DDL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_ddl::ddldefinition_is_not_abstract():
    assert not inspect.isabstract(DDL::DDLDefinition)


def test_ddl::ddldefinition_constructor_exists():
    assert callable(DDL::DDLDefinition.__init__)


def test_ddl::ddldefinition_constructor_args():
    sig = inspect.signature(DDL::DDLDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ddl::createcommentcolumn_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateCommentColumn)


def test_ddl::createcommentcolumn_constructor_exists():
    assert callable(DDL::CreateCommentColumn.__init__)


def test_ddl::createcommentcolumn_constructor_args():
    sig = inspect.signature(DDL::CreateCommentColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnComment" in params, "Missing parameter 'columnComment'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_ddl::createcommentcolumn_has_columnComment():
    assert hasattr(DDL::CreateCommentColumn, "columnComment")
    descriptor = None
    for klass in DDL::CreateCommentColumn.__mro__:
        if "columnComment" in klass.__dict__:
            descriptor = klass.__dict__["columnComment"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcommentcolumn_has_columnName():
    assert hasattr(DDL::CreateCommentColumn, "columnName")
    descriptor = None
    for klass in DDL::CreateCommentColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcommentcolumn_has_tableName():
    assert hasattr(DDL::CreateCommentColumn, "tableName")
    descriptor = None
    for klass in DDL::CreateCommentColumn.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_ddl::createcommenttable_is_not_abstract():
    assert not inspect.isabstract(DDL::CreateCommentTable)


def test_ddl::createcommenttable_constructor_exists():
    assert callable(DDL::CreateCommentTable.__init__)


def test_ddl::createcommenttable_constructor_args():
    sig = inspect.signature(DDL::CreateCommentTable.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "tableComment" in params, "Missing parameter 'tableComment'"

def test_ddl::createcommenttable_has_tableName():
    assert hasattr(DDL::CreateCommentTable, "tableName")
    descriptor = None
    for klass in DDL::CreateCommentTable.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_ddl::createcommenttable_has_tableComment():
    assert hasattr(DDL::CreateCommentTable, "tableComment")
    descriptor = None
    for klass in DDL::CreateCommentTable.__mro__:
        if "tableComment" in klass.__dict__:
            descriptor = klass.__dict__["tableComment"]
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
DataDefinition_strategy = st.builds(
    DataDefinition,
)
DDL::CreateDatabase_strategy = st.builds(
    DDL::CreateDatabase,
    databaseName=
        safe_text
)
DDL::CreateColumn_strategy = st.builds(
    DDL::CreateColumn,
    columnName=
        safe_text,
    columnType=
        safe_text,
    commentColumn=
        safe_text,
    columnNull=
        st.booleans()
)
DDL::CreateCk_strategy = st.builds(
    DDL::CreateCk,
    nameCk=
        safe_text,
    valuesCk=
        safe_text,
    columnName=
        safe_text
)
DDL::CreateTable_strategy = st.builds(
    DDL::CreateTable,
    tableName=
        safe_text,
    commentTable=
        safe_text
)
DDL::CreateFk_strategy = st.builds(
    DDL::CreateFk,
    columnReference=
        safe_text,
    nameFk=
        safe_text,
    columnName=
        safe_text
)
DDL::CreatePk_strategy = st.builds(
    DDL::CreatePk,
    columnName=
        safe_text,
    namePk=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
DDL::DataDefinition_strategy = st.builds(
    DDL::DataDefinition,
)
DDL::Statement_strategy = st.builds(
    DDL::Statement,
)
DDL::DDLDefinition_strategy = st.builds(
    DDL::DDLDefinition,
)
DDL::CreateCommentColumn_strategy = st.builds(
    DDL::CreateCommentColumn,
    columnComment=
        safe_text,
    columnName=
        safe_text,
    tableName=
        safe_text
)
DDL::CreateCommentTable_strategy = st.builds(
    DDL::CreateCommentTable,
    tableName=
        safe_text,
    tableComment=
        safe_text
)

@given(instance=DataDefinition_strategy)
@settings(max_examples=50)
def test_datadefinition_instantiation(instance):
    assert isinstance(instance, DataDefinition)

@given(instance=DDL::CreateDatabase_strategy)
@settings(max_examples=50)
def test_ddl::createdatabase_instantiation(instance):
    assert isinstance(instance, DDL::CreateDatabase)

@given(instance=DDL::CreateDatabase_strategy)
def test_ddl::createdatabase_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=DDL::CreateDatabase_strategy)
def test_ddl::createdatabase_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=DDL::CreateColumn_strategy)
@settings(max_examples=50)
def test_ddl::createcolumn_instantiation(instance):
    assert isinstance(instance, DDL::CreateColumn)

@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnType_type(instance):
    assert isinstance(instance.columnType, str)


@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnType_setter(instance):
    original = instance.columnType
    instance.columnType = original
    assert instance.columnType == original

@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_commentColumn_type(instance):
    assert isinstance(instance.commentColumn, str)


@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_commentColumn_setter(instance):
    original = instance.commentColumn
    instance.commentColumn = original
    assert instance.commentColumn == original

@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnNull_type(instance):
    assert isinstance(instance.columnNull, bool)


@given(instance=DDL::CreateColumn_strategy)
def test_ddl::createcolumn_columnNull_setter(instance):
    original = instance.columnNull
    instance.columnNull = original
    assert instance.columnNull == original

@given(instance=DDL::CreateCk_strategy)
@settings(max_examples=50)
def test_ddl::createck_instantiation(instance):
    assert isinstance(instance, DDL::CreateCk)

@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_nameCk_type(instance):
    assert isinstance(instance.nameCk, str)


@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_nameCk_setter(instance):
    original = instance.nameCk
    instance.nameCk = original
    assert instance.nameCk == original

@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_valuesCk_type(instance):
    assert isinstance(instance.valuesCk, str)


@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_valuesCk_setter(instance):
    original = instance.valuesCk
    instance.valuesCk = original
    assert instance.valuesCk == original

@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CreateCk_strategy)
def test_ddl::createck_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CreateTable_strategy)
@settings(max_examples=50)
def test_ddl::createtable_instantiation(instance):
    assert isinstance(instance, DDL::CreateTable)

@given(instance=DDL::CreateTable_strategy)
def test_ddl::createtable_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::CreateTable_strategy)
def test_ddl::createtable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::CreateTable_strategy)
def test_ddl::createtable_commentTable_type(instance):
    assert isinstance(instance.commentTable, str)


@given(instance=DDL::CreateTable_strategy)
def test_ddl::createtable_commentTable_setter(instance):
    original = instance.commentTable
    instance.commentTable = original
    assert instance.commentTable == original

@given(instance=DDL::CreateFk_strategy)
@settings(max_examples=50)
def test_ddl::createfk_instantiation(instance):
    assert isinstance(instance, DDL::CreateFk)

@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_columnReference_type(instance):
    assert isinstance(instance.columnReference, str)


@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_columnReference_setter(instance):
    original = instance.columnReference
    instance.columnReference = original
    assert instance.columnReference == original

@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_nameFk_type(instance):
    assert isinstance(instance.nameFk, str)


@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_nameFk_setter(instance):
    original = instance.nameFk
    instance.nameFk = original
    assert instance.nameFk == original

@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CreateFk_strategy)
def test_ddl::createfk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CreatePk_strategy)
@settings(max_examples=50)
def test_ddl::createpk_instantiation(instance):
    assert isinstance(instance, DDL::CreatePk)

@given(instance=DDL::CreatePk_strategy)
def test_ddl::createpk_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CreatePk_strategy)
def test_ddl::createpk_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CreatePk_strategy)
def test_ddl::createpk_namePk_type(instance):
    assert isinstance(instance.namePk, str)


@given(instance=DDL::CreatePk_strategy)
def test_ddl::createpk_namePk_setter(instance):
    original = instance.namePk
    instance.namePk = original
    assert instance.namePk == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=DDL::DataDefinition_strategy)
@settings(max_examples=50)
def test_ddl::datadefinition_instantiation(instance):
    assert isinstance(instance, DDL::DataDefinition)

@given(instance=DDL::Statement_strategy)
@settings(max_examples=50)
def test_ddl::statement_instantiation(instance):
    assert isinstance(instance, DDL::Statement)

@given(instance=DDL::DDLDefinition_strategy)
@settings(max_examples=50)
def test_ddl::ddldefinition_instantiation(instance):
    assert isinstance(instance, DDL::DDLDefinition)

@given(instance=DDL::CreateCommentColumn_strategy)
@settings(max_examples=50)
def test_ddl::createcommentcolumn_instantiation(instance):
    assert isinstance(instance, DDL::CreateCommentColumn)

@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_columnComment_type(instance):
    assert isinstance(instance.columnComment, str)


@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_columnComment_setter(instance):
    original = instance.columnComment
    instance.columnComment = original
    assert instance.columnComment == original

@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::CreateCommentColumn_strategy)
def test_ddl::createcommentcolumn_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::CreateCommentTable_strategy)
@settings(max_examples=50)
def test_ddl::createcommenttable_instantiation(instance):
    assert isinstance(instance, DDL::CreateCommentTable)

@given(instance=DDL::CreateCommentTable_strategy)
def test_ddl::createcommenttable_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=DDL::CreateCommentTable_strategy)
def test_ddl::createcommenttable_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=DDL::CreateCommentTable_strategy)
def test_ddl::createcommenttable_tableComment_type(instance):
    assert isinstance(instance.tableComment, str)


@given(instance=DDL::CreateCommentTable_strategy)
def test_ddl::createcommenttable_tableComment_setter(instance):
    original = instance.tableComment
    instance.tableComment = original
    assert instance.tableComment == original
