import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelOperation,
    mm_ops_SetDefaultValue,
    mm_ops_HasNoOwnInstances,
    mm_ops_RemoveSequence,
    mm_ops_RemoveIndex,
    mm_ops_AddColumn,
    mm_ops_RemoveColumn,
    mm_ops_AddIndex,
    mm_ops_DeleteRows,
    mm_ops_RemoveTable,
    mm_ops_RenameColumn,
    mm_ops_UpdateRows,
    mm_ops_AddSequence,
    mm_ops_RemoveDefaultValue,
    mm_ops_RemoveConstraint,
    mm_ops_InsertRows,
    mm_ops_GenerateSequenceNumbers,
    mm_ops_RemoveNotNull,
    mm_ops_AddTable,
    mm_ops_NillRows,
    mm_ops_RenameTable,
    mm_ops_SetColumnType,
    mm_ops_HasNoInstances,
    mm_ops_AddPrimaryKey,
    mm_ops_AddSchema,
    Operations,
    mm_ops_AddNotNull,
    mm_ops_AddUnique,
    mm_ops_AddForeignKey,
    mm_rdb_TableConstraint,
    mm_rdb_Column,
    TableConstraint,
    mm_rdb_Unique,
    mm_rdb_Table,
    Column,
    mm_ops_ModelOperation,
    mm_rdb_ForeignKey,
    Sequence,
    mm_rdb_PrimaryKey,
    Table,
    Structure,
    mm_rdb_Schema,
    Schema,
    ops_ModelOperation,
    ModelRoot,
    mm_rdb_Structure,
    mm_rdb_Operations,
    mm_rdb_Index,
    mm_rdb_Sequence,
    Index,
    mm_rdb_ModelRoot,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_mm_ops_setdefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm_ops_SetDefaultValue)


def test_mm_ops_setdefaultvalue_constructor_exists():
    assert callable(mm_ops_SetDefaultValue.__init__)


def test_mm_ops_setdefaultvalue_constructor_args():
    sig = inspect.signature(mm_ops_SetDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "newDefaultValue" in params, "Missing parameter 'newDefaultValue'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"

def test_mm_ops_setdefaultvalue_has_owningColumnName():
    assert hasattr(mm_ops_SetDefaultValue, "owningColumnName")
    descriptor = None
    for klass in mm_ops_SetDefaultValue.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setdefaultvalue_has_owningSchemaName():
    assert hasattr(mm_ops_SetDefaultValue, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_SetDefaultValue.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setdefaultvalue_has_newDefaultValue():
    assert hasattr(mm_ops_SetDefaultValue, "newDefaultValue")
    descriptor = None
    for klass in mm_ops_SetDefaultValue.__mro__:
        if "newDefaultValue" in klass.__dict__:
            descriptor = klass.__dict__["newDefaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setdefaultvalue_has_owningTableName():
    assert hasattr(mm_ops_SetDefaultValue, "owningTableName")
    descriptor = None
    for klass in mm_ops_SetDefaultValue.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_hasnoowninstances_is_not_abstract():
    assert not inspect.isabstract(mm_ops_HasNoOwnInstances)


def test_mm_ops_hasnoowninstances_constructor_exists():
    assert callable(mm_ops_HasNoOwnInstances.__init__)


def test_mm_ops_hasnoowninstances_constructor_args():
    sig = inspect.signature(mm_ops_HasNoOwnInstances.__init__)
    params = list(sig.parameters.keys())
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm_ops_hasnoowninstances_has_whereCondition():
    assert hasattr(mm_ops_HasNoOwnInstances, "whereCondition")
    descriptor = None
    for klass in mm_ops_HasNoOwnInstances.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_hasnoowninstances_has_owningSchemaName():
    assert hasattr(mm_ops_HasNoOwnInstances, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_HasNoOwnInstances.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_hasnoowninstances_has_tableName():
    assert hasattr(mm_ops_HasNoOwnInstances, "tableName")
    descriptor = None
    for klass in mm_ops_HasNoOwnInstances.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removesequence_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveSequence)


def test_mm_ops_removesequence_constructor_exists():
    assert callable(mm_ops_RemoveSequence.__init__)


def test_mm_ops_removesequence_constructor_args():
    sig = inspect.signature(mm_ops_RemoveSequence.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm_ops_removesequence_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveSequence, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveSequence.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removesequence_has_name():
    assert hasattr(mm_ops_RemoveSequence, "name")
    descriptor = None
    for klass in mm_ops_RemoveSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removeindex_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveIndex)


def test_mm_ops_removeindex_constructor_exists():
    assert callable(mm_ops_RemoveIndex.__init__)


def test_mm_ops_removeindex_constructor_args():
    sig = inspect.signature(mm_ops_RemoveIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_removeindex_has_name():
    assert hasattr(mm_ops_RemoveIndex, "name")
    descriptor = None
    for klass in mm_ops_RemoveIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removeindex_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveIndex, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveIndex.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addcolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddColumn)


def test_mm_ops_addcolumn_constructor_exists():
    assert callable(mm_ops_AddColumn.__init__)


def test_mm_ops_addcolumn_constructor_args():
    sig = inspect.signature(mm_ops_AddColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "type" in params, "Missing parameter 'type'"

def test_mm_ops_addcolumn_has_owningTableName():
    assert hasattr(mm_ops_AddColumn, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addcolumn_has_name():
    assert hasattr(mm_ops_AddColumn, "name")
    descriptor = None
    for klass in mm_ops_AddColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addcolumn_has_owningSchemaName():
    assert hasattr(mm_ops_AddColumn, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addcolumn_has_defaultValue():
    assert hasattr(mm_ops_AddColumn, "defaultValue")
    descriptor = None
    for klass in mm_ops_AddColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addcolumn_has_type():
    assert hasattr(mm_ops_AddColumn, "type")
    descriptor = None
    for klass in mm_ops_AddColumn.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removecolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveColumn)


def test_mm_ops_removecolumn_constructor_exists():
    assert callable(mm_ops_RemoveColumn.__init__)


def test_mm_ops_removecolumn_constructor_args():
    sig = inspect.signature(mm_ops_RemoveColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_removecolumn_has_owningTableName():
    assert hasattr(mm_ops_RemoveColumn, "owningTableName")
    descriptor = None
    for klass in mm_ops_RemoveColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removecolumn_has_name():
    assert hasattr(mm_ops_RemoveColumn, "name")
    descriptor = None
    for klass in mm_ops_RemoveColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removecolumn_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveColumn, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addindex_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddIndex)


def test_mm_ops_addindex_constructor_exists():
    assert callable(mm_ops_AddIndex.__init__)


def test_mm_ops_addindex_constructor_args():
    sig = inspect.signature(mm_ops_AddIndex.__init__)
    params = list(sig.parameters.keys())
    assert "columnsNames" in params, "Missing parameter 'columnsNames'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_addindex_has_columnsNames():
    assert hasattr(mm_ops_AddIndex, "columnsNames")
    descriptor = None
    for klass in mm_ops_AddIndex.__mro__:
        if "columnsNames" in klass.__dict__:
            descriptor = klass.__dict__["columnsNames"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addindex_has_owningTableName():
    assert hasattr(mm_ops_AddIndex, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddIndex.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addindex_has_name():
    assert hasattr(mm_ops_AddIndex, "name")
    descriptor = None
    for klass in mm_ops_AddIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addindex_has_owningSchemaName():
    assert hasattr(mm_ops_AddIndex, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddIndex.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_deleterows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_DeleteRows)


def test_mm_ops_deleterows_constructor_exists():
    assert callable(mm_ops_DeleteRows.__init__)


def test_mm_ops_deleterows_constructor_args():
    sig = inspect.signature(mm_ops_DeleteRows.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm_ops_deleterows_has_owningSchemaName():
    assert hasattr(mm_ops_DeleteRows, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_DeleteRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_deleterows_has_whereCondition():
    assert hasattr(mm_ops_DeleteRows, "whereCondition")
    descriptor = None
    for klass in mm_ops_DeleteRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_deleterows_has_tableName():
    assert hasattr(mm_ops_DeleteRows, "tableName")
    descriptor = None
    for klass in mm_ops_DeleteRows.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removetable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveTable)


def test_mm_ops_removetable_constructor_exists():
    assert callable(mm_ops_RemoveTable.__init__)


def test_mm_ops_removetable_constructor_args():
    sig = inspect.signature(mm_ops_RemoveTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_removetable_has_name():
    assert hasattr(mm_ops_RemoveTable, "name")
    descriptor = None
    for klass in mm_ops_RemoveTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removetable_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveTable, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_renamecolumn_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RenameColumn)


def test_mm_ops_renamecolumn_constructor_exists():
    assert callable(mm_ops_RenameColumn.__init__)


def test_mm_ops_renamecolumn_constructor_args():
    sig = inspect.signature(mm_ops_RenameColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "newName" in params, "Missing parameter 'newName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_renamecolumn_has_owningTableName():
    assert hasattr(mm_ops_RenameColumn, "owningTableName")
    descriptor = None
    for klass in mm_ops_RenameColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_renamecolumn_has_newName():
    assert hasattr(mm_ops_RenameColumn, "newName")
    descriptor = None
    for klass in mm_ops_RenameColumn.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_renamecolumn_has_name():
    assert hasattr(mm_ops_RenameColumn, "name")
    descriptor = None
    for klass in mm_ops_RenameColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_renamecolumn_has_owningSchemaName():
    assert hasattr(mm_ops_RenameColumn, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RenameColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_updaterows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_UpdateRows)


def test_mm_ops_updaterows_constructor_exists():
    assert callable(mm_ops_UpdateRows.__init__)


def test_mm_ops_updaterows_constructor_args():
    sig = inspect.signature(mm_ops_UpdateRows.__init__)
    params = list(sig.parameters.keys())
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"
    assert "sourceColumnName" in params, "Missing parameter 'sourceColumnName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_updaterows_has_sourceTableName():
    assert hasattr(mm_ops_UpdateRows, "sourceTableName")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "sourceTableName" in klass.__dict__:
            descriptor = klass.__dict__["sourceTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_updaterows_has_targetColumnName():
    assert hasattr(mm_ops_UpdateRows, "targetColumnName")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_updaterows_has_sourceColumnName():
    assert hasattr(mm_ops_UpdateRows, "sourceColumnName")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "sourceColumnName" in klass.__dict__:
            descriptor = klass.__dict__["sourceColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_updaterows_has_whereCondition():
    assert hasattr(mm_ops_UpdateRows, "whereCondition")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_updaterows_has_targetTableName():
    assert hasattr(mm_ops_UpdateRows, "targetTableName")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_updaterows_has_owningSchemaName():
    assert hasattr(mm_ops_UpdateRows, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_UpdateRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addsequence_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddSequence)


def test_mm_ops_addsequence_constructor_exists():
    assert callable(mm_ops_AddSequence.__init__)


def test_mm_ops_addsequence_constructor_args():
    sig = inspect.signature(mm_ops_AddSequence.__init__)
    params = list(sig.parameters.keys())
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm_ops_addsequence_has_startValue():
    assert hasattr(mm_ops_AddSequence, "startValue")
    descriptor = None
    for klass in mm_ops_AddSequence.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addsequence_has_owningSchemaName():
    assert hasattr(mm_ops_AddSequence, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddSequence.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addsequence_has_name():
    assert hasattr(mm_ops_AddSequence, "name")
    descriptor = None
    for klass in mm_ops_AddSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removedefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveDefaultValue)


def test_mm_ops_removedefaultvalue_constructor_exists():
    assert callable(mm_ops_RemoveDefaultValue.__init__)


def test_mm_ops_removedefaultvalue_constructor_args():
    sig = inspect.signature(mm_ops_RemoveDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"

def test_mm_ops_removedefaultvalue_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveDefaultValue, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveDefaultValue.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removedefaultvalue_has_owningColumnName():
    assert hasattr(mm_ops_RemoveDefaultValue, "owningColumnName")
    descriptor = None
    for klass in mm_ops_RemoveDefaultValue.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removedefaultvalue_has_owningTableName():
    assert hasattr(mm_ops_RemoveDefaultValue, "owningTableName")
    descriptor = None
    for klass in mm_ops_RemoveDefaultValue.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removeconstraint_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveConstraint)


def test_mm_ops_removeconstraint_constructor_exists():
    assert callable(mm_ops_RemoveConstraint.__init__)


def test_mm_ops_removeconstraint_constructor_args():
    sig = inspect.signature(mm_ops_RemoveConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_removeconstraint_has_owningTableName():
    assert hasattr(mm_ops_RemoveConstraint, "owningTableName")
    descriptor = None
    for klass in mm_ops_RemoveConstraint.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removeconstraint_has_name():
    assert hasattr(mm_ops_RemoveConstraint, "name")
    descriptor = None
    for klass in mm_ops_RemoveConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removeconstraint_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveConstraint, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveConstraint.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_insertrows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_InsertRows)


def test_mm_ops_insertrows_constructor_exists():
    assert callable(mm_ops_InsertRows.__init__)


def test_mm_ops_insertrows_constructor_args():
    sig = inspect.signature(mm_ops_InsertRows.__init__)
    params = list(sig.parameters.keys())
    assert "sourceColumnsNames" in params, "Missing parameter 'sourceColumnsNames'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "targetColumnNames" in params, "Missing parameter 'targetColumnNames'"

def test_mm_ops_insertrows_has_sourceColumnsNames():
    assert hasattr(mm_ops_InsertRows, "sourceColumnsNames")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "sourceColumnsNames" in klass.__dict__:
            descriptor = klass.__dict__["sourceColumnsNames"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_insertrows_has_owningSchemaName():
    assert hasattr(mm_ops_InsertRows, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_insertrows_has_sourceTableName():
    assert hasattr(mm_ops_InsertRows, "sourceTableName")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "sourceTableName" in klass.__dict__:
            descriptor = klass.__dict__["sourceTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_insertrows_has_targetTableName():
    assert hasattr(mm_ops_InsertRows, "targetTableName")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_insertrows_has_whereCondition():
    assert hasattr(mm_ops_InsertRows, "whereCondition")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_insertrows_has_targetColumnNames():
    assert hasattr(mm_ops_InsertRows, "targetColumnNames")
    descriptor = None
    for klass in mm_ops_InsertRows.__mro__:
        if "targetColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnNames"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_generatesequencenumbers_is_not_abstract():
    assert not inspect.isabstract(mm_ops_GenerateSequenceNumbers)


def test_mm_ops_generatesequencenumbers_constructor_exists():
    assert callable(mm_ops_GenerateSequenceNumbers.__init__)


def test_mm_ops_generatesequencenumbers_constructor_args():
    sig = inspect.signature(mm_ops_GenerateSequenceNumbers.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "sequenceName" in params, "Missing parameter 'sequenceName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_mm_ops_generatesequencenumbers_has_tableName():
    assert hasattr(mm_ops_GenerateSequenceNumbers, "tableName")
    descriptor = None
    for klass in mm_ops_GenerateSequenceNumbers.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_generatesequencenumbers_has_sequenceName():
    assert hasattr(mm_ops_GenerateSequenceNumbers, "sequenceName")
    descriptor = None
    for klass in mm_ops_GenerateSequenceNumbers.__mro__:
        if "sequenceName" in klass.__dict__:
            descriptor = klass.__dict__["sequenceName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_generatesequencenumbers_has_owningSchemaName():
    assert hasattr(mm_ops_GenerateSequenceNumbers, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_GenerateSequenceNumbers.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_generatesequencenumbers_has_columnName():
    assert hasattr(mm_ops_GenerateSequenceNumbers, "columnName")
    descriptor = None
    for klass in mm_ops_GenerateSequenceNumbers.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_removenotnull_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RemoveNotNull)


def test_mm_ops_removenotnull_constructor_exists():
    assert callable(mm_ops_RemoveNotNull.__init__)


def test_mm_ops_removenotnull_constructor_args():
    sig = inspect.signature(mm_ops_RemoveNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"

def test_mm_ops_removenotnull_has_owningSchemaName():
    assert hasattr(mm_ops_RemoveNotNull, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RemoveNotNull.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removenotnull_has_constrainedColumnName():
    assert hasattr(mm_ops_RemoveNotNull, "constrainedColumnName")
    descriptor = None
    for klass in mm_ops_RemoveNotNull.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_removenotnull_has_owningTableName():
    assert hasattr(mm_ops_RemoveNotNull, "owningTableName")
    descriptor = None
    for klass in mm_ops_RemoveNotNull.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addtable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddTable)


def test_mm_ops_addtable_constructor_exists():
    assert callable(mm_ops_AddTable.__init__)


def test_mm_ops_addtable_constructor_args():
    sig = inspect.signature(mm_ops_AddTable.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm_ops_addtable_has_owningSchemaName():
    assert hasattr(mm_ops_AddTable, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addtable_has_name():
    assert hasattr(mm_ops_AddTable, "name")
    descriptor = None
    for klass in mm_ops_AddTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_nillrows_is_not_abstract():
    assert not inspect.isabstract(mm_ops_NillRows)


def test_mm_ops_nillrows_constructor_exists():
    assert callable(mm_ops_NillRows.__init__)


def test_mm_ops_nillrows_constructor_args():
    sig = inspect.signature(mm_ops_NillRows.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm_ops_nillrows_has_owningSchemaName():
    assert hasattr(mm_ops_NillRows, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_NillRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_nillrows_has_columnName():
    assert hasattr(mm_ops_NillRows, "columnName")
    descriptor = None
    for klass in mm_ops_NillRows.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_nillrows_has_whereCondition():
    assert hasattr(mm_ops_NillRows, "whereCondition")
    descriptor = None
    for klass in mm_ops_NillRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_nillrows_has_tableName():
    assert hasattr(mm_ops_NillRows, "tableName")
    descriptor = None
    for klass in mm_ops_NillRows.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_renametable_is_not_abstract():
    assert not inspect.isabstract(mm_ops_RenameTable)


def test_mm_ops_renametable_constructor_exists():
    assert callable(mm_ops_RenameTable.__init__)


def test_mm_ops_renametable_constructor_args():
    sig = inspect.signature(mm_ops_RenameTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "newName" in params, "Missing parameter 'newName'"

def test_mm_ops_renametable_has_name():
    assert hasattr(mm_ops_RenameTable, "name")
    descriptor = None
    for klass in mm_ops_RenameTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_renametable_has_owningSchemaName():
    assert hasattr(mm_ops_RenameTable, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_RenameTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_renametable_has_newName():
    assert hasattr(mm_ops_RenameTable, "newName")
    descriptor = None
    for klass in mm_ops_RenameTable.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_setcolumntype_is_not_abstract():
    assert not inspect.isabstract(mm_ops_SetColumnType)


def test_mm_ops_setcolumntype_constructor_exists():
    assert callable(mm_ops_SetColumnType.__init__)


def test_mm_ops_setcolumntype_constructor_args():
    sig = inspect.signature(mm_ops_SetColumnType.__init__)
    params = list(sig.parameters.keys())
    assert "oldType" in params, "Missing parameter 'oldType'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "newType" in params, "Missing parameter 'newType'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"

def test_mm_ops_setcolumntype_has_oldType():
    assert hasattr(mm_ops_SetColumnType, "oldType")
    descriptor = None
    for klass in mm_ops_SetColumnType.__mro__:
        if "oldType" in klass.__dict__:
            descriptor = klass.__dict__["oldType"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setcolumntype_has_owningSchemaName():
    assert hasattr(mm_ops_SetColumnType, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_SetColumnType.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setcolumntype_has_owningTableName():
    assert hasattr(mm_ops_SetColumnType, "owningTableName")
    descriptor = None
    for klass in mm_ops_SetColumnType.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setcolumntype_has_newType():
    assert hasattr(mm_ops_SetColumnType, "newType")
    descriptor = None
    for klass in mm_ops_SetColumnType.__mro__:
        if "newType" in klass.__dict__:
            descriptor = klass.__dict__["newType"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_setcolumntype_has_owningColumnName():
    assert hasattr(mm_ops_SetColumnType, "owningColumnName")
    descriptor = None
    for klass in mm_ops_SetColumnType.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_hasnoinstances_is_not_abstract():
    assert not inspect.isabstract(mm_ops_HasNoInstances)


def test_mm_ops_hasnoinstances_constructor_exists():
    assert callable(mm_ops_HasNoInstances.__init__)


def test_mm_ops_hasnoinstances_constructor_args():
    sig = inspect.signature(mm_ops_HasNoInstances.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm_ops_hasnoinstances_has_owningSchemaName():
    assert hasattr(mm_ops_HasNoInstances, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_HasNoInstances.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_hasnoinstances_has_tableName():
    assert hasattr(mm_ops_HasNoInstances, "tableName")
    descriptor = None
    for klass in mm_ops_HasNoInstances.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addprimarykey_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddPrimaryKey)


def test_mm_ops_addprimarykey_constructor_exists():
    assert callable(mm_ops_AddPrimaryKey.__init__)


def test_mm_ops_addprimarykey_constructor_args():
    sig = inspect.signature(mm_ops_AddPrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"

def test_mm_ops_addprimarykey_has_owningSchemaName():
    assert hasattr(mm_ops_AddPrimaryKey, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddPrimaryKey.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addprimarykey_has_name():
    assert hasattr(mm_ops_AddPrimaryKey, "name")
    descriptor = None
    for klass in mm_ops_AddPrimaryKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addprimarykey_has_owningTableName():
    assert hasattr(mm_ops_AddPrimaryKey, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddPrimaryKey.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addprimarykey_has_constrainedColumnName():
    assert hasattr(mm_ops_AddPrimaryKey, "constrainedColumnName")
    descriptor = None
    for klass in mm_ops_AddPrimaryKey.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addschema_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddSchema)


def test_mm_ops_addschema_constructor_exists():
    assert callable(mm_ops_AddSchema.__init__)


def test_mm_ops_addschema_constructor_args():
    sig = inspect.signature(mm_ops_AddSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm_ops_addschema_has_name():
    assert hasattr(mm_ops_AddSchema, "name")
    descriptor = None
    for klass in mm_ops_AddSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operations_is_not_abstract():
    assert not inspect.isabstract(Operations)


def test_operations_constructor_exists():
    assert callable(Operations.__init__)


def test_operations_constructor_args():
    sig = inspect.signature(Operations.__init__)
    params = list(sig.parameters.keys())



def test_mm_ops_addnotnull_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddNotNull)


def test_mm_ops_addnotnull_constructor_exists():
    assert callable(mm_ops_AddNotNull.__init__)


def test_mm_ops_addnotnull_constructor_args():
    sig = inspect.signature(mm_ops_AddNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"

def test_mm_ops_addnotnull_has_owningSchemaName():
    assert hasattr(mm_ops_AddNotNull, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddNotNull.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addnotnull_has_constrainedColumnName():
    assert hasattr(mm_ops_AddNotNull, "constrainedColumnName")
    descriptor = None
    for klass in mm_ops_AddNotNull.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addnotnull_has_owningTableName():
    assert hasattr(mm_ops_AddNotNull, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddNotNull.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addunique_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddUnique)


def test_mm_ops_addunique_constructor_exists():
    assert callable(mm_ops_AddUnique.__init__)


def test_mm_ops_addunique_constructor_args():
    sig = inspect.signature(mm_ops_AddUnique.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constrainedColumnNames" in params, "Missing parameter 'constrainedColumnNames'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"

def test_mm_ops_addunique_has_name():
    assert hasattr(mm_ops_AddUnique, "name")
    descriptor = None
    for klass in mm_ops_AddUnique.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addunique_has_constrainedColumnNames():
    assert hasattr(mm_ops_AddUnique, "constrainedColumnNames")
    descriptor = None
    for klass in mm_ops_AddUnique.__mro__:
        if "constrainedColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnNames"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addunique_has_owningSchemaName():
    assert hasattr(mm_ops_AddUnique, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddUnique.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addunique_has_owningTableName():
    assert hasattr(mm_ops_AddUnique, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddUnique.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)



def test_mm_ops_addforeignkey_is_not_abstract():
    assert not inspect.isabstract(mm_ops_AddForeignKey)


def test_mm_ops_addforeignkey_constructor_exists():
    assert callable(mm_ops_AddForeignKey.__init__)


def test_mm_ops_addforeignkey_constructor_args():
    sig = inspect.signature(mm_ops_AddForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm_ops_addforeignkey_has_constrainedColumnName():
    assert hasattr(mm_ops_AddForeignKey, "constrainedColumnName")
    descriptor = None
    for klass in mm_ops_AddForeignKey.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addforeignkey_has_owningTableName():
    assert hasattr(mm_ops_AddForeignKey, "owningTableName")
    descriptor = None
    for klass in mm_ops_AddForeignKey.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addforeignkey_has_targetTableName():
    assert hasattr(mm_ops_AddForeignKey, "targetTableName")
    descriptor = None
    for klass in mm_ops_AddForeignKey.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addforeignkey_has_name():
    assert hasattr(mm_ops_AddForeignKey, "name")
    descriptor = None
    for klass in mm_ops_AddForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_ops_addforeignkey_has_owningSchemaName():
    assert hasattr(mm_ops_AddForeignKey, "owningSchemaName")
    descriptor = None
    for klass in mm_ops_AddForeignKey.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm_rdb_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_TableConstraint)


def test_mm_rdb_tableconstraint_constructor_exists():
    assert callable(mm_rdb_TableConstraint.__init__)


def test_mm_rdb_tableconstraint_constructor_args():
    sig = inspect.signature(mm_rdb_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm_rdb_tableconstraint_has_name():
    assert hasattr(mm_rdb_TableConstraint, "name")
    descriptor = None
    for klass in mm_rdb_TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm_rdb_column_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Column)


def test_mm_rdb_column_constructor_exists():
    assert callable(mm_rdb_Column.__init__)


def test_mm_rdb_column_constructor_args():
    sig = inspect.signature(mm_rdb_Column.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isNillable" in params, "Missing parameter 'isNillable'"
    assert "type" in params, "Missing parameter 'type'"

def test_mm_rdb_column_has_defaultValue():
    assert hasattr(mm_rdb_Column, "defaultValue")
    descriptor = None
    for klass in mm_rdb_Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mm_rdb_column_has_name():
    assert hasattr(mm_rdb_Column, "name")
    descriptor = None
    for klass in mm_rdb_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_rdb_column_has_isNillable():
    assert hasattr(mm_rdb_Column, "isNillable")
    descriptor = None
    for klass in mm_rdb_Column.__mro__:
        if "isNillable" in klass.__dict__:
            descriptor = klass.__dict__["isNillable"]
            break
    assert isinstance(descriptor, property)

def test_mm_rdb_column_has_type():
    assert hasattr(mm_rdb_Column, "type")
    descriptor = None
    for klass in mm_rdb_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_unique_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Unique)


def test_mm_rdb_unique_constructor_exists():
    assert callable(mm_rdb_Unique.__init__)


def test_mm_rdb_unique_constructor_args():
    sig = inspect.signature(mm_rdb_Unique.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_table_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Table)


def test_mm_rdb_table_constructor_exists():
    assert callable(mm_rdb_Table.__init__)


def test_mm_rdb_table_constructor_args():
    sig = inspect.signature(mm_rdb_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm_rdb_table_has_name():
    assert hasattr(mm_rdb_Table, "name")
    descriptor = None
    for klass in mm_rdb_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_mm_ops_modeloperation_is_not_abstract():
    assert not inspect.isabstract(mm_ops_ModelOperation)


def test_mm_ops_modeloperation_constructor_exists():
    assert callable(mm_ops_ModelOperation.__init__)


def test_mm_ops_modeloperation_constructor_args():
    sig = inspect.signature(mm_ops_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_foreignkey_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_ForeignKey)


def test_mm_rdb_foreignkey_constructor_exists():
    assert callable(mm_rdb_ForeignKey.__init__)


def test_mm_rdb_foreignkey_constructor_args():
    sig = inspect.signature(mm_rdb_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_primarykey_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_PrimaryKey)


def test_mm_rdb_primarykey_constructor_exists():
    assert callable(mm_rdb_PrimaryKey.__init__)


def test_mm_rdb_primarykey_constructor_args():
    sig = inspect.signature(mm_rdb_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_schema_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Schema)


def test_mm_rdb_schema_constructor_exists():
    assert callable(mm_rdb_Schema.__init__)


def test_mm_rdb_schema_constructor_args():
    sig = inspect.signature(mm_rdb_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm_rdb_schema_has_name():
    assert hasattr(mm_rdb_Schema, "name")
    descriptor = None
    for klass in mm_rdb_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_ops_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ops_ModelOperation)


def test_ops_modeloperation_constructor_exists():
    assert callable(ops_ModelOperation.__init__)


def test_ops_modeloperation_constructor_args():
    sig = inspect.signature(ops_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_modelroot_is_not_abstract():
    assert not inspect.isabstract(ModelRoot)


def test_modelroot_constructor_exists():
    assert callable(ModelRoot.__init__)


def test_modelroot_constructor_args():
    sig = inspect.signature(ModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_structure_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Structure)


def test_mm_rdb_structure_constructor_exists():
    assert callable(mm_rdb_Structure.__init__)


def test_mm_rdb_structure_constructor_args():
    sig = inspect.signature(mm_rdb_Structure.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_operations_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Operations)


def test_mm_rdb_operations_constructor_exists():
    assert callable(mm_rdb_Operations.__init__)


def test_mm_rdb_operations_constructor_args():
    sig = inspect.signature(mm_rdb_Operations.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_index_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Index)


def test_mm_rdb_index_constructor_exists():
    assert callable(mm_rdb_Index.__init__)


def test_mm_rdb_index_constructor_args():
    sig = inspect.signature(mm_rdb_Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm_rdb_index_has_name():
    assert hasattr(mm_rdb_Index, "name")
    descriptor = None
    for klass in mm_rdb_Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm_rdb_sequence_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_Sequence)


def test_mm_rdb_sequence_constructor_exists():
    assert callable(mm_rdb_Sequence.__init__)


def test_mm_rdb_sequence_constructor_args():
    sig = inspect.signature(mm_rdb_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "startValue" in params, "Missing parameter 'startValue'"

def test_mm_rdb_sequence_has_name():
    assert hasattr(mm_rdb_Sequence, "name")
    descriptor = None
    for klass in mm_rdb_Sequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm_rdb_sequence_has_startValue():
    assert hasattr(mm_rdb_Sequence, "startValue")
    descriptor = None
    for klass in mm_rdb_Sequence.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_mm_rdb_modelroot_is_not_abstract():
    assert not inspect.isabstract(mm_rdb_ModelRoot)


def test_mm_rdb_modelroot_constructor_exists():
    assert callable(mm_rdb_ModelRoot.__init__)


def test_mm_rdb_modelroot_constructor_args():
    sig = inspect.signature(mm_rdb_ModelRoot.__init__)
    params = list(sig.parameters.keys())

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "char",
        "int",
        "boolean",
        "float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
ModelOperation_strategy = st.builds(
    ModelOperation,
)
mm_ops_SetDefaultValue_strategy = st.builds(
    mm_ops_SetDefaultValue,
    owningColumnName=
        safe_text,
    owningSchemaName=
        safe_text,
    newDefaultValue=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_HasNoOwnInstances_strategy = st.builds(
    mm_ops_HasNoOwnInstances,
    whereCondition=
        safe_text,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RemoveSequence_strategy = st.builds(
    mm_ops_RemoveSequence,
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_RemoveIndex_strategy = st.builds(
    mm_ops_RemoveIndex,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddColumn_strategy = st.builds(
    mm_ops_AddColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    defaultValue=
        safe_text,
    type=
        safe_text
)
mm_ops_RemoveColumn_strategy = st.builds(
    mm_ops_RemoveColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddIndex_strategy = st.builds(
    mm_ops_AddIndex,
    columnsNames=
        safe_text,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_DeleteRows_strategy = st.builds(
    mm_ops_DeleteRows,
    owningSchemaName=
        safe_text,
    whereCondition=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RemoveTable_strategy = st.builds(
    mm_ops_RemoveTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_RenameColumn_strategy = st.builds(
    mm_ops_RenameColumn,
    owningTableName=
        safe_text,
    newName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_UpdateRows_strategy = st.builds(
    mm_ops_UpdateRows,
    sourceTableName=
        safe_text,
    targetColumnName=
        safe_text,
    sourceColumnName=
        safe_text,
    whereCondition=
        safe_text,
    targetTableName=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_AddSequence_strategy = st.builds(
    mm_ops_AddSequence,
    startValue=
        st.integers(),
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_RemoveDefaultValue_strategy = st.builds(
    mm_ops_RemoveDefaultValue,
    owningSchemaName=
        safe_text,
    owningColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_RemoveConstraint_strategy = st.builds(
    mm_ops_RemoveConstraint,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_ops_InsertRows_strategy = st.builds(
    mm_ops_InsertRows,
    sourceColumnsNames=
        safe_text,
    owningSchemaName=
        safe_text,
    sourceTableName=
        safe_text,
    targetTableName=
        safe_text,
    whereCondition=
        safe_text,
    targetColumnNames=
        safe_text
)
mm_ops_GenerateSequenceNumbers_strategy = st.builds(
    mm_ops_GenerateSequenceNumbers,
    tableName=
        safe_text,
    sequenceName=
        safe_text,
    owningSchemaName=
        safe_text,
    columnName=
        safe_text
)
mm_ops_RemoveNotNull_strategy = st.builds(
    mm_ops_RemoveNotNull,
    owningSchemaName=
        safe_text,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddTable_strategy = st.builds(
    mm_ops_AddTable,
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm_ops_NillRows_strategy = st.builds(
    mm_ops_NillRows,
    owningSchemaName=
        safe_text,
    columnName=
        safe_text,
    whereCondition=
        safe_text,
    tableName=
        safe_text
)
mm_ops_RenameTable_strategy = st.builds(
    mm_ops_RenameTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    newName=
        safe_text
)
mm_ops_SetColumnType_strategy = st.builds(
    mm_ops_SetColumnType,
    oldType=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    newType=
        safe_text,
    owningColumnName=
        safe_text
)
mm_ops_HasNoInstances_strategy = st.builds(
    mm_ops_HasNoInstances,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm_ops_AddPrimaryKey_strategy = st.builds(
    mm_ops_AddPrimaryKey,
    owningSchemaName=
        safe_text,
    name=
        safe_text,
    owningTableName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm_ops_AddSchema_strategy = st.builds(
    mm_ops_AddSchema,
    name=
        safe_text
)
Operations_strategy = st.builds(
    Operations,
)
mm_ops_AddNotNull_strategy = st.builds(
    mm_ops_AddNotNull,
    owningSchemaName=
        safe_text,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddUnique_strategy = st.builds(
    mm_ops_AddUnique,
    name=
        safe_text,
    constrainedColumnNames=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text
)
mm_ops_AddForeignKey_strategy = st.builds(
    mm_ops_AddForeignKey,
    constrainedColumnName=
        safe_text,
    owningTableName=
        safe_text,
    targetTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm_rdb_TableConstraint_strategy = st.builds(
    mm_rdb_TableConstraint,
    name=
        safe_text
)
mm_rdb_Column_strategy = st.builds(
    mm_rdb_Column,
    defaultValue=
        safe_text,
    name=
        safe_text,
    isNillable=
        safe_text,
    type=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
mm_rdb_Unique_strategy = st.builds(
    mm_rdb_Unique,
)
mm_rdb_Table_strategy = st.builds(
    mm_rdb_Table,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
mm_ops_ModelOperation_strategy = st.builds(
    mm_ops_ModelOperation,
)
mm_rdb_ForeignKey_strategy = st.builds(
    mm_rdb_ForeignKey,
)
Sequence_strategy = st.builds(
    Sequence,
)
mm_rdb_PrimaryKey_strategy = st.builds(
    mm_rdb_PrimaryKey,
)
Table_strategy = st.builds(
    Table,
)
Structure_strategy = st.builds(
    Structure,
)
mm_rdb_Schema_strategy = st.builds(
    mm_rdb_Schema,
    name=
        safe_text
)
Schema_strategy = st.builds(
    Schema,
)
ops_ModelOperation_strategy = st.builds(
    ops_ModelOperation,
)
ModelRoot_strategy = st.builds(
    ModelRoot,
)
mm_rdb_Structure_strategy = st.builds(
    mm_rdb_Structure,
)
mm_rdb_Operations_strategy = st.builds(
    mm_rdb_Operations,
)
mm_rdb_Index_strategy = st.builds(
    mm_rdb_Index,
    name=
        safe_text
)
mm_rdb_Sequence_strategy = st.builds(
    mm_rdb_Sequence,
    name=
        safe_text,
    startValue=
        st.integers()
)
Index_strategy = st.builds(
    Index,
)
mm_rdb_ModelRoot_strategy = st.builds(
    mm_rdb_ModelRoot,
)

@given(instance=ModelOperation_strategy)
@settings(max_examples=50)
def test_modeloperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)

@given(instance=mm_ops_SetDefaultValue_strategy)
@settings(max_examples=50)
def test_mm_ops_setdefaultvalue_instantiation(instance):
    assert isinstance(instance, mm_ops_SetDefaultValue)



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_mm_ops_setdefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_mm_ops_setdefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_mm_ops_setdefaultvalue_newDefaultValue_setter(instance):
    original = instance.newDefaultValue
    instance.newDefaultValue = original
    assert instance.newDefaultValue == original



@given(instance=mm_ops_SetDefaultValue_strategy)
def test_mm_ops_setdefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm_ops_HasNoOwnInstances_strategy)
@settings(max_examples=50)
def test_mm_ops_hasnoowninstances_instantiation(instance):
    assert isinstance(instance, mm_ops_HasNoOwnInstances)



@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_mm_ops_hasnoowninstances_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_mm_ops_hasnoowninstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_HasNoOwnInstances_strategy)
def test_mm_ops_hasnoowninstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm_ops_RemoveSequence_strategy)
@settings(max_examples=50)
def test_mm_ops_removesequence_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveSequence)



@given(instance=mm_ops_RemoveSequence_strategy)
def test_mm_ops_removesequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveSequence_strategy)
def test_mm_ops_removesequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm_ops_RemoveIndex_strategy)
@settings(max_examples=50)
def test_mm_ops_removeindex_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveIndex)



@given(instance=mm_ops_RemoveIndex_strategy)
def test_mm_ops_removeindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveIndex_strategy)
def test_mm_ops_removeindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_AddColumn_strategy)
@settings(max_examples=50)
def test_mm_ops_addcolumn_instantiation(instance):
    assert isinstance(instance, mm_ops_AddColumn)



@given(instance=mm_ops_AddColumn_strategy)
def test_mm_ops_addcolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddColumn_strategy)
def test_mm_ops_addcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddColumn_strategy)
def test_mm_ops_addcolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddColumn_strategy)
def test_mm_ops_addcolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=mm_ops_AddColumn_strategy)
def test_mm_ops_addcolumn_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm_ops_RemoveColumn_strategy)
@settings(max_examples=50)
def test_mm_ops_removecolumn_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveColumn)



@given(instance=mm_ops_RemoveColumn_strategy)
def test_mm_ops_removecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RemoveColumn_strategy)
def test_mm_ops_removecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveColumn_strategy)
def test_mm_ops_removecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_AddIndex_strategy)
@settings(max_examples=50)
def test_mm_ops_addindex_instantiation(instance):
    assert isinstance(instance, mm_ops_AddIndex)



@given(instance=mm_ops_AddIndex_strategy)
def test_mm_ops_addindex_columnsNames_setter(instance):
    original = instance.columnsNames
    instance.columnsNames = original
    assert instance.columnsNames == original



@given(instance=mm_ops_AddIndex_strategy)
def test_mm_ops_addindex_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddIndex_strategy)
def test_mm_ops_addindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddIndex_strategy)
def test_mm_ops_addindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_DeleteRows_strategy)
@settings(max_examples=50)
def test_mm_ops_deleterows_instantiation(instance):
    assert isinstance(instance, mm_ops_DeleteRows)



@given(instance=mm_ops_DeleteRows_strategy)
def test_mm_ops_deleterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_DeleteRows_strategy)
def test_mm_ops_deleterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_DeleteRows_strategy)
def test_mm_ops_deleterows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm_ops_RemoveTable_strategy)
@settings(max_examples=50)
def test_mm_ops_removetable_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveTable)



@given(instance=mm_ops_RemoveTable_strategy)
def test_mm_ops_removetable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveTable_strategy)
def test_mm_ops_removetable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_RenameColumn_strategy)
@settings(max_examples=50)
def test_mm_ops_renamecolumn_instantiation(instance):
    assert isinstance(instance, mm_ops_RenameColumn)



@given(instance=mm_ops_RenameColumn_strategy)
def test_mm_ops_renamecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_mm_ops_renamecolumn_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_mm_ops_renamecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RenameColumn_strategy)
def test_mm_ops_renamecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_UpdateRows_strategy)
@settings(max_examples=50)
def test_mm_ops_updaterows_instantiation(instance):
    assert isinstance(instance, mm_ops_UpdateRows)



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_sourceColumnName_setter(instance):
    original = instance.sourceColumnName
    instance.sourceColumnName = original
    assert instance.sourceColumnName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_UpdateRows_strategy)
def test_mm_ops_updaterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_AddSequence_strategy)
@settings(max_examples=50)
def test_mm_ops_addsequence_instantiation(instance):
    assert isinstance(instance, mm_ops_AddSequence)



@given(instance=mm_ops_AddSequence_strategy)
def test_mm_ops_addsequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=mm_ops_AddSequence_strategy)
def test_mm_ops_addsequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddSequence_strategy)
def test_mm_ops_addsequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm_ops_RemoveDefaultValue_strategy)
@settings(max_examples=50)
def test_mm_ops_removedefaultvalue_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveDefaultValue)



@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_mm_ops_removedefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_mm_ops_removedefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original



@given(instance=mm_ops_RemoveDefaultValue_strategy)
def test_mm_ops_removedefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm_ops_RemoveConstraint_strategy)
@settings(max_examples=50)
def test_mm_ops_removeconstraint_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveConstraint)



@given(instance=mm_ops_RemoveConstraint_strategy)
def test_mm_ops_removeconstraint_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_RemoveConstraint_strategy)
def test_mm_ops_removeconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RemoveConstraint_strategy)
def test_mm_ops_removeconstraint_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_ops_InsertRows_strategy)
@settings(max_examples=50)
def test_mm_ops_insertrows_instantiation(instance):
    assert isinstance(instance, mm_ops_InsertRows)



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_sourceColumnsNames_setter(instance):
    original = instance.sourceColumnsNames
    instance.sourceColumnsNames = original
    assert instance.sourceColumnsNames == original



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_InsertRows_strategy)
def test_mm_ops_insertrows_targetColumnNames_setter(instance):
    original = instance.targetColumnNames
    instance.targetColumnNames = original
    assert instance.targetColumnNames == original

@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
@settings(max_examples=50)
def test_mm_ops_generatesequencenumbers_instantiation(instance):
    assert isinstance(instance, mm_ops_GenerateSequenceNumbers)



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_mm_ops_generatesequencenumbers_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_mm_ops_generatesequencenumbers_sequenceName_setter(instance):
    original = instance.sequenceName
    instance.sequenceName = original
    assert instance.sequenceName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_mm_ops_generatesequencenumbers_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_GenerateSequenceNumbers_strategy)
def test_mm_ops_generatesequencenumbers_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=mm_ops_RemoveNotNull_strategy)
@settings(max_examples=50)
def test_mm_ops_removenotnull_instantiation(instance):
    assert isinstance(instance, mm_ops_RemoveNotNull)



@given(instance=mm_ops_RemoveNotNull_strategy)
def test_mm_ops_removenotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RemoveNotNull_strategy)
def test_mm_ops_removenotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_RemoveNotNull_strategy)
def test_mm_ops_removenotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm_ops_AddTable_strategy)
@settings(max_examples=50)
def test_mm_ops_addtable_instantiation(instance):
    assert isinstance(instance, mm_ops_AddTable)



@given(instance=mm_ops_AddTable_strategy)
def test_mm_ops_addtable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddTable_strategy)
def test_mm_ops_addtable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm_ops_NillRows_strategy)
@settings(max_examples=50)
def test_mm_ops_nillrows_instantiation(instance):
    assert isinstance(instance, mm_ops_NillRows)



@given(instance=mm_ops_NillRows_strategy)
def test_mm_ops_nillrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_NillRows_strategy)
def test_mm_ops_nillrows_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=mm_ops_NillRows_strategy)
def test_mm_ops_nillrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original



@given(instance=mm_ops_NillRows_strategy)
def test_mm_ops_nillrows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm_ops_RenameTable_strategy)
@settings(max_examples=50)
def test_mm_ops_renametable_instantiation(instance):
    assert isinstance(instance, mm_ops_RenameTable)



@given(instance=mm_ops_RenameTable_strategy)
def test_mm_ops_renametable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_RenameTable_strategy)
def test_mm_ops_renametable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_RenameTable_strategy)
def test_mm_ops_renametable_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original

@given(instance=mm_ops_SetColumnType_strategy)
@settings(max_examples=50)
def test_mm_ops_setcolumntype_instantiation(instance):
    assert isinstance(instance, mm_ops_SetColumnType)



@given(instance=mm_ops_SetColumnType_strategy)
def test_mm_ops_setcolumntype_oldType_setter(instance):
    original = instance.oldType
    instance.oldType = original
    assert instance.oldType == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_mm_ops_setcolumntype_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_mm_ops_setcolumntype_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_mm_ops_setcolumntype_newType_setter(instance):
    original = instance.newType
    instance.newType = original
    assert instance.newType == original



@given(instance=mm_ops_SetColumnType_strategy)
def test_mm_ops_setcolumntype_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original

@given(instance=mm_ops_HasNoInstances_strategy)
@settings(max_examples=50)
def test_mm_ops_hasnoinstances_instantiation(instance):
    assert isinstance(instance, mm_ops_HasNoInstances)



@given(instance=mm_ops_HasNoInstances_strategy)
def test_mm_ops_hasnoinstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_HasNoInstances_strategy)
def test_mm_ops_hasnoinstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm_ops_AddPrimaryKey_strategy)
@settings(max_examples=50)
def test_mm_ops_addprimarykey_instantiation(instance):
    assert isinstance(instance, mm_ops_AddPrimaryKey)



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_mm_ops_addprimarykey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_mm_ops_addprimarykey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_mm_ops_addprimarykey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddPrimaryKey_strategy)
def test_mm_ops_addprimarykey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original

@given(instance=mm_ops_AddSchema_strategy)
@settings(max_examples=50)
def test_mm_ops_addschema_instantiation(instance):
    assert isinstance(instance, mm_ops_AddSchema)



@given(instance=mm_ops_AddSchema_strategy)
def test_mm_ops_addschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Operations_strategy)
@settings(max_examples=50)
def test_operations_instantiation(instance):
    assert isinstance(instance, Operations)

@given(instance=mm_ops_AddNotNull_strategy)
@settings(max_examples=50)
def test_mm_ops_addnotnull_instantiation(instance):
    assert isinstance(instance, mm_ops_AddNotNull)



@given(instance=mm_ops_AddNotNull_strategy)
def test_mm_ops_addnotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddNotNull_strategy)
def test_mm_ops_addnotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_AddNotNull_strategy)
def test_mm_ops_addnotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm_ops_AddUnique_strategy)
@settings(max_examples=50)
def test_mm_ops_addunique_instantiation(instance):
    assert isinstance(instance, mm_ops_AddUnique)



@given(instance=mm_ops_AddUnique_strategy)
def test_mm_ops_addunique_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddUnique_strategy)
def test_mm_ops_addunique_constrainedColumnNames_setter(instance):
    original = instance.constrainedColumnNames
    instance.constrainedColumnNames = original
    assert instance.constrainedColumnNames == original



@given(instance=mm_ops_AddUnique_strategy)
def test_mm_ops_addunique_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original



@given(instance=mm_ops_AddUnique_strategy)
def test_mm_ops_addunique_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm_ops_AddForeignKey_strategy)
@settings(max_examples=50)
def test_mm_ops_addforeignkey_instantiation(instance):
    assert isinstance(instance, mm_ops_AddForeignKey)



@given(instance=mm_ops_AddForeignKey_strategy)
def test_mm_ops_addforeignkey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_mm_ops_addforeignkey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_mm_ops_addforeignkey_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_mm_ops_addforeignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_ops_AddForeignKey_strategy)
def test_mm_ops_addforeignkey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm_rdb_TableConstraint_strategy)
@settings(max_examples=50)
def test_mm_rdb_tableconstraint_instantiation(instance):
    assert isinstance(instance, mm_rdb_TableConstraint)



@given(instance=mm_rdb_TableConstraint_strategy)
def test_mm_rdb_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm_rdb_Column_strategy)
@settings(max_examples=50)
def test_mm_rdb_column_instantiation(instance):
    assert isinstance(instance, mm_rdb_Column)



@given(instance=mm_rdb_Column_strategy)
def test_mm_rdb_column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=mm_rdb_Column_strategy)
def test_mm_rdb_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_rdb_Column_strategy)
def test_mm_rdb_column_isNillable_setter(instance):
    original = instance.isNillable
    instance.isNillable = original
    assert instance.isNillable == original



@given(instance=mm_rdb_Column_strategy)
def test_mm_rdb_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=mm_rdb_Unique_strategy)
@settings(max_examples=50)
def test_mm_rdb_unique_instantiation(instance):
    assert isinstance(instance, mm_rdb_Unique)

@given(instance=mm_rdb_Table_strategy)
@settings(max_examples=50)
def test_mm_rdb_table_instantiation(instance):
    assert isinstance(instance, mm_rdb_Table)



@given(instance=mm_rdb_Table_strategy)
def test_mm_rdb_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=mm_ops_ModelOperation_strategy)
@settings(max_examples=50)
def test_mm_ops_modeloperation_instantiation(instance):
    assert isinstance(instance, mm_ops_ModelOperation)

@given(instance=mm_rdb_ForeignKey_strategy)
@settings(max_examples=50)
def test_mm_rdb_foreignkey_instantiation(instance):
    assert isinstance(instance, mm_rdb_ForeignKey)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=mm_rdb_PrimaryKey_strategy)
@settings(max_examples=50)
def test_mm_rdb_primarykey_instantiation(instance):
    assert isinstance(instance, mm_rdb_PrimaryKey)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=mm_rdb_Schema_strategy)
@settings(max_examples=50)
def test_mm_rdb_schema_instantiation(instance):
    assert isinstance(instance, mm_rdb_Schema)



@given(instance=mm_rdb_Schema_strategy)
def test_mm_rdb_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=ops_ModelOperation_strategy)
@settings(max_examples=50)
def test_ops_modeloperation_instantiation(instance):
    assert isinstance(instance, ops_ModelOperation)

@given(instance=ModelRoot_strategy)
@settings(max_examples=50)
def test_modelroot_instantiation(instance):
    assert isinstance(instance, ModelRoot)

@given(instance=mm_rdb_Structure_strategy)
@settings(max_examples=50)
def test_mm_rdb_structure_instantiation(instance):
    assert isinstance(instance, mm_rdb_Structure)

@given(instance=mm_rdb_Operations_strategy)
@settings(max_examples=50)
def test_mm_rdb_operations_instantiation(instance):
    assert isinstance(instance, mm_rdb_Operations)

@given(instance=mm_rdb_Index_strategy)
@settings(max_examples=50)
def test_mm_rdb_index_instantiation(instance):
    assert isinstance(instance, mm_rdb_Index)



@given(instance=mm_rdb_Index_strategy)
def test_mm_rdb_index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm_rdb_Sequence_strategy)
@settings(max_examples=50)
def test_mm_rdb_sequence_instantiation(instance):
    assert isinstance(instance, mm_rdb_Sequence)



@given(instance=mm_rdb_Sequence_strategy)
def test_mm_rdb_sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm_rdb_Sequence_strategy)
def test_mm_rdb_sequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=mm_rdb_ModelRoot_strategy)
@settings(max_examples=50)
def test_mm_rdb_modelroot_instantiation(instance):
    assert isinstance(instance, mm_rdb_ModelRoot)
