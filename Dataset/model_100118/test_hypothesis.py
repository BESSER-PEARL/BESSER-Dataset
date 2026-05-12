import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JRESResourceInfo,
    database_DatabaseResourceData,
    database_DBModuleCommonProperty,
    ExtensibleModel,
    database_DBGenContext,
    database_TableKey,
    database_TableIndex,
    database_TableIndexColumn,
    database_ForeignKey,
    database_TableColumn,
    DatabaseResourceData,
    database_ViewResourceData,
    database_TableResourceData,
    ColumnType,
    key_type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jresresourceinfo_is_not_abstract():
    assert not inspect.isabstract(JRESResourceInfo)


def test_jresresourceinfo_constructor_exists():
    assert callable(JRESResourceInfo.__init__)


def test_jresresourceinfo_constructor_args():
    sig = inspect.signature(JRESResourceInfo.__init__)
    params = list(sig.parameters.keys())



def test_database_databaseresourcedata_is_not_abstract():
    assert not inspect.isabstract(database_DatabaseResourceData)


def test_database_databaseresourcedata_constructor_exists():
    assert callable(database_DatabaseResourceData.__init__)


def test_database_databaseresourcedata_constructor_args():
    sig = inspect.signature(database_DatabaseResourceData.__init__)
    params = list(sig.parameters.keys())



def test_database_dbmodulecommonproperty_is_not_abstract():
    assert not inspect.isabstract(database_DBModuleCommonProperty)


def test_database_dbmodulecommonproperty_constructor_exists():
    assert callable(database_DBModuleCommonProperty.__init__)


def test_database_dbmodulecommonproperty_constructor_args():
    sig = inspect.signature(database_DBModuleCommonProperty.__init__)
    params = list(sig.parameters.keys())
    assert "supportDatabases" in params, "Missing parameter 'supportDatabases'"
    assert "database" in params, "Missing parameter 'database'"

def test_database_dbmodulecommonproperty_has_supportDatabases():
    assert hasattr(database_DBModuleCommonProperty, "supportDatabases")
    descriptor = None
    for klass in database_DBModuleCommonProperty.__mro__:
        if "supportDatabases" in klass.__dict__:
            descriptor = klass.__dict__["supportDatabases"]
            break
    assert isinstance(descriptor, property)

def test_database_dbmodulecommonproperty_has_database():
    assert hasattr(database_DBModuleCommonProperty, "database")
    descriptor = None
    for klass in database_DBModuleCommonProperty.__mro__:
        if "database" in klass.__dict__:
            descriptor = klass.__dict__["database"]
            break
    assert isinstance(descriptor, property)



def test_extensiblemodel_is_not_abstract():
    assert not inspect.isabstract(ExtensibleModel)


def test_extensiblemodel_constructor_exists():
    assert callable(ExtensibleModel.__init__)


def test_extensiblemodel_constructor_args():
    sig = inspect.signature(ExtensibleModel.__init__)
    params = list(sig.parameters.keys())



def test_database_dbgencontext_is_not_abstract():
    assert not inspect.isabstract(database_DBGenContext)


def test_database_dbgencontext_constructor_exists():
    assert callable(database_DBGenContext.__init__)


def test_database_dbgencontext_constructor_args():
    sig = inspect.signature(database_DBGenContext.__init__)
    params = list(sig.parameters.keys())



def test_database_tablekey_is_not_abstract():
    assert not inspect.isabstract(database_TableKey)


def test_database_tablekey_constructor_exists():
    assert callable(database_TableKey.__init__)


def test_database_tablekey_constructor_args():
    sig = inspect.signature(database_TableKey.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mark" in params, "Missing parameter 'mark'"

def test_database_tablekey_has_type():
    assert hasattr(database_TableKey, "type")
    descriptor = None
    for klass in database_TableKey.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_database_tablekey_has_name():
    assert hasattr(database_TableKey, "name")
    descriptor = None
    for klass in database_TableKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_database_tablekey_has_mark():
    assert hasattr(database_TableKey, "mark")
    descriptor = None
    for klass in database_TableKey.__mro__:
        if "mark" in klass.__dict__:
            descriptor = klass.__dict__["mark"]
            break
    assert isinstance(descriptor, property)



def test_database_tableindex_is_not_abstract():
    assert not inspect.isabstract(database_TableIndex)


def test_database_tableindex_constructor_exists():
    assert callable(database_TableIndex.__init__)


def test_database_tableindex_constructor_args():
    sig = inspect.signature(database_TableIndex.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "mark" in params, "Missing parameter 'mark'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cluster" in params, "Missing parameter 'cluster'"

def test_database_tableindex_has_unique():
    assert hasattr(database_TableIndex, "unique")
    descriptor = None
    for klass in database_TableIndex.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_database_tableindex_has_mark():
    assert hasattr(database_TableIndex, "mark")
    descriptor = None
    for klass in database_TableIndex.__mro__:
        if "mark" in klass.__dict__:
            descriptor = klass.__dict__["mark"]
            break
    assert isinstance(descriptor, property)

def test_database_tableindex_has_name():
    assert hasattr(database_TableIndex, "name")
    descriptor = None
    for klass in database_TableIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_database_tableindex_has_cluster():
    assert hasattr(database_TableIndex, "cluster")
    descriptor = None
    for klass in database_TableIndex.__mro__:
        if "cluster" in klass.__dict__:
            descriptor = klass.__dict__["cluster"]
            break
    assert isinstance(descriptor, property)



def test_database_tableindexcolumn_is_not_abstract():
    assert not inspect.isabstract(database_TableIndexColumn)


def test_database_tableindexcolumn_constructor_exists():
    assert callable(database_TableIndexColumn.__init__)


def test_database_tableindexcolumn_constructor_args():
    sig = inspect.signature(database_TableIndexColumn.__init__)
    params = list(sig.parameters.keys())
    assert "columnType" in params, "Missing parameter 'columnType'"
    assert "ascending" in params, "Missing parameter 'ascending'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_database_tableindexcolumn_has_columnType():
    assert hasattr(database_TableIndexColumn, "columnType")
    descriptor = None
    for klass in database_TableIndexColumn.__mro__:
        if "columnType" in klass.__dict__:
            descriptor = klass.__dict__["columnType"]
            break
    assert isinstance(descriptor, property)

def test_database_tableindexcolumn_has_ascending():
    assert hasattr(database_TableIndexColumn, "ascending")
    descriptor = None
    for klass in database_TableIndexColumn.__mro__:
        if "ascending" in klass.__dict__:
            descriptor = klass.__dict__["ascending"]
            break
    assert isinstance(descriptor, property)

def test_database_tableindexcolumn_has_columnName():
    assert hasattr(database_TableIndexColumn, "columnName")
    descriptor = None
    for klass in database_TableIndexColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_database_foreignkey_is_not_abstract():
    assert not inspect.isabstract(database_ForeignKey)


def test_database_foreignkey_constructor_exists():
    assert callable(database_ForeignKey.__init__)


def test_database_foreignkey_constructor_args():
    sig = inspect.signature(database_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_database_foreignkey_has_tableName():
    assert hasattr(database_ForeignKey, "tableName")
    descriptor = None
    for klass in database_ForeignKey.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_database_foreignkey_has_fieldName():
    assert hasattr(database_ForeignKey, "fieldName")
    descriptor = None
    for klass in database_ForeignKey.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_database_tablecolumn_is_not_abstract():
    assert not inspect.isabstract(database_TableColumn)


def test_database_tablecolumn_constructor_exists():
    assert callable(database_TableColumn.__init__)


def test_database_tablecolumn_constructor_args():
    sig = inspect.signature(database_TableColumn.__init__)
    params = list(sig.parameters.keys())
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "description" in params, "Missing parameter 'description'"
    assert "columnType" in params, "Missing parameter 'columnType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "chineseName" in params, "Missing parameter 'chineseName'"
    assert "mark" in params, "Missing parameter 'mark'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_database_tablecolumn_has_primaryKey():
    assert hasattr(database_TableColumn, "primaryKey")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_unique():
    assert hasattr(database_TableColumn, "unique")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_dataType():
    assert hasattr(database_TableColumn, "dataType")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_description():
    assert hasattr(database_TableColumn, "description")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_columnType():
    assert hasattr(database_TableColumn, "columnType")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "columnType" in klass.__dict__:
            descriptor = klass.__dict__["columnType"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_name():
    assert hasattr(database_TableColumn, "name")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_nullable():
    assert hasattr(database_TableColumn, "nullable")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_columnName():
    assert hasattr(database_TableColumn, "columnName")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_fieldName():
    assert hasattr(database_TableColumn, "fieldName")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_chineseName():
    assert hasattr(database_TableColumn, "chineseName")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "chineseName" in klass.__dict__:
            descriptor = klass.__dict__["chineseName"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_mark():
    assert hasattr(database_TableColumn, "mark")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "mark" in klass.__dict__:
            descriptor = klass.__dict__["mark"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_comments():
    assert hasattr(database_TableColumn, "comments")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_database_tablecolumn_has_defaultValue():
    assert hasattr(database_TableColumn, "defaultValue")
    descriptor = None
    for klass in database_TableColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_databaseresourcedata_is_not_abstract():
    assert not inspect.isabstract(DatabaseResourceData)


def test_databaseresourcedata_constructor_exists():
    assert callable(DatabaseResourceData.__init__)


def test_databaseresourcedata_constructor_args():
    sig = inspect.signature(DatabaseResourceData.__init__)
    params = list(sig.parameters.keys())



def test_database_viewresourcedata_is_not_abstract():
    assert not inspect.isabstract(database_ViewResourceData)


def test_database_viewresourcedata_constructor_exists():
    assert callable(database_ViewResourceData.__init__)


def test_database_viewresourcedata_constructor_args():
    sig = inspect.signature(database_ViewResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "sql" in params, "Missing parameter 'sql'"

def test_database_viewresourcedata_has_isHistory():
    assert hasattr(database_ViewResourceData, "isHistory")
    descriptor = None
    for klass in database_ViewResourceData.__mro__:
        if "isHistory" in klass.__dict__:
            descriptor = klass.__dict__["isHistory"]
            break
    assert isinstance(descriptor, property)

def test_database_viewresourcedata_has_sql():
    assert hasattr(database_ViewResourceData, "sql")
    descriptor = None
    for klass in database_ViewResourceData.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_database_tableresourcedata_is_not_abstract():
    assert not inspect.isabstract(database_TableResourceData)


def test_database_tableresourcedata_constructor_exists():
    assert callable(database_TableResourceData.__init__)


def test_database_tableresourcedata_constructor_args():
    sig = inspect.signature(database_TableResourceData.__init__)
    params = list(sig.parameters.keys())

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "STD_FIELD",
        "NON_STD_FIELD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"

def test_key_type_exists():
    # Check that the Enumeration exists
    assert key_type is not None

def test_key_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in key_type]
    expected_literals = [
        "Foreign",
        "Primary",
        "Unique",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in key_type"


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
JRESResourceInfo_strategy = st.builds(
    JRESResourceInfo,
)
database_DatabaseResourceData_strategy = st.builds(
    database_DatabaseResourceData,
)
database_DBModuleCommonProperty_strategy = st.builds(
    database_DBModuleCommonProperty,
    supportDatabases=
        safe_text,
    database=
        safe_text
)
ExtensibleModel_strategy = st.builds(
    ExtensibleModel,
)
database_DBGenContext_strategy = st.builds(
    database_DBGenContext,
)
database_TableKey_strategy = st.builds(
    database_TableKey,
    type=
        safe_text,
    name=
        safe_text,
    mark=
        safe_text
)
database_TableIndex_strategy = st.builds(
    database_TableIndex,
    unique=
        st.booleans(),
    mark=
        safe_text,
    name=
        safe_text,
    cluster=
        st.booleans()
)
database_TableIndexColumn_strategy = st.builds(
    database_TableIndexColumn,
    columnType=
        safe_text,
    ascending=
        st.booleans(),
    columnName=
        safe_text
)
database_ForeignKey_strategy = st.builds(
    database_ForeignKey,
    tableName=
        safe_text,
    fieldName=
        safe_text
)
database_TableColumn_strategy = st.builds(
    database_TableColumn,
    primaryKey=
        st.booleans(),
    unique=
        st.booleans(),
    dataType=
        safe_text,
    description=
        safe_text,
    columnType=
        safe_text,
    name=
        safe_text,
    nullable=
        st.booleans(),
    columnName=
        safe_text,
    fieldName=
        safe_text,
    chineseName=
        safe_text,
    mark=
        safe_text,
    comments=
        safe_text,
    defaultValue=
        safe_text
)
DatabaseResourceData_strategy = st.builds(
    DatabaseResourceData,
)
database_ViewResourceData_strategy = st.builds(
    database_ViewResourceData,
    isHistory=
        st.booleans(),
    sql=
        safe_text
)
database_TableResourceData_strategy = st.builds(
    database_TableResourceData,
)

@given(instance=JRESResourceInfo_strategy)
@settings(max_examples=50)
def test_jresresourceinfo_instantiation(instance):
    assert isinstance(instance, JRESResourceInfo)

@given(instance=database_DatabaseResourceData_strategy)
@settings(max_examples=50)
def test_database_databaseresourcedata_instantiation(instance):
    assert isinstance(instance, database_DatabaseResourceData)

@given(instance=database_DBModuleCommonProperty_strategy)
@settings(max_examples=50)
def test_database_dbmodulecommonproperty_instantiation(instance):
    assert isinstance(instance, database_DBModuleCommonProperty)



@given(instance=database_DBModuleCommonProperty_strategy)
def test_database_dbmodulecommonproperty_supportDatabases_setter(instance):
    original = instance.supportDatabases
    instance.supportDatabases = original
    assert instance.supportDatabases == original



@given(instance=database_DBModuleCommonProperty_strategy)
def test_database_dbmodulecommonproperty_database_setter(instance):
    original = instance.database
    instance.database = original
    assert instance.database == original

@given(instance=ExtensibleModel_strategy)
@settings(max_examples=50)
def test_extensiblemodel_instantiation(instance):
    assert isinstance(instance, ExtensibleModel)

@given(instance=database_DBGenContext_strategy)
@settings(max_examples=50)
def test_database_dbgencontext_instantiation(instance):
    assert isinstance(instance, database_DBGenContext)

@given(instance=database_TableKey_strategy)
@settings(max_examples=50)
def test_database_tablekey_instantiation(instance):
    assert isinstance(instance, database_TableKey)



@given(instance=database_TableKey_strategy)
def test_database_tablekey_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=database_TableKey_strategy)
def test_database_tablekey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=database_TableKey_strategy)
def test_database_tablekey_mark_setter(instance):
    original = instance.mark
    instance.mark = original
    assert instance.mark == original

@given(instance=database_TableIndex_strategy)
@settings(max_examples=50)
def test_database_tableindex_instantiation(instance):
    assert isinstance(instance, database_TableIndex)



@given(instance=database_TableIndex_strategy)
def test_database_tableindex_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=database_TableIndex_strategy)
def test_database_tableindex_mark_setter(instance):
    original = instance.mark
    instance.mark = original
    assert instance.mark == original



@given(instance=database_TableIndex_strategy)
def test_database_tableindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=database_TableIndex_strategy)
def test_database_tableindex_cluster_setter(instance):
    original = instance.cluster
    instance.cluster = original
    assert instance.cluster == original

@given(instance=database_TableIndexColumn_strategy)
@settings(max_examples=50)
def test_database_tableindexcolumn_instantiation(instance):
    assert isinstance(instance, database_TableIndexColumn)



@given(instance=database_TableIndexColumn_strategy)
def test_database_tableindexcolumn_columnType_setter(instance):
    original = instance.columnType
    instance.columnType = original
    assert instance.columnType == original



@given(instance=database_TableIndexColumn_strategy)
def test_database_tableindexcolumn_ascending_setter(instance):
    original = instance.ascending
    instance.ascending = original
    assert instance.ascending == original



@given(instance=database_TableIndexColumn_strategy)
def test_database_tableindexcolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=database_ForeignKey_strategy)
@settings(max_examples=50)
def test_database_foreignkey_instantiation(instance):
    assert isinstance(instance, database_ForeignKey)



@given(instance=database_ForeignKey_strategy)
def test_database_foreignkey_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=database_ForeignKey_strategy)
def test_database_foreignkey_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=database_TableColumn_strategy)
@settings(max_examples=50)
def test_database_tablecolumn_instantiation(instance):
    assert isinstance(instance, database_TableColumn)



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_columnType_setter(instance):
    original = instance.columnType
    instance.columnType = original
    assert instance.columnType == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_chineseName_setter(instance):
    original = instance.chineseName
    instance.chineseName = original
    assert instance.chineseName == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_mark_setter(instance):
    original = instance.mark
    instance.mark = original
    assert instance.mark == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=database_TableColumn_strategy)
def test_database_tablecolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=DatabaseResourceData_strategy)
@settings(max_examples=50)
def test_databaseresourcedata_instantiation(instance):
    assert isinstance(instance, DatabaseResourceData)

@given(instance=database_ViewResourceData_strategy)
@settings(max_examples=50)
def test_database_viewresourcedata_instantiation(instance):
    assert isinstance(instance, database_ViewResourceData)



@given(instance=database_ViewResourceData_strategy)
def test_database_viewresourcedata_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original



@given(instance=database_ViewResourceData_strategy)
def test_database_viewresourcedata_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=database_TableResourceData_strategy)
@settings(max_examples=50)
def test_database_tableresourcedata_instantiation(instance):
    assert isinstance(instance, database_TableResourceData)
