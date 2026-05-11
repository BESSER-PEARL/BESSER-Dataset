import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModelOperation,
    mm::ops::RemoveIndex,
    mm::ops::SetDefaultValue,
    mm::ops::HasNoInstances,
    mm::ops::AddPrimaryKey,
    mm::ops::AddSequence,
    mm::ops::RemoveSequence,
    mm::ops::RemoveDefaultValue,
    mm::ops::RemoveColumn,
    mm::ops::RemoveNotNull,
    mm::ops::NillRows,
    mm::ops::GenerateSequenceNumbers,
    mm::ops::RenameTable,
    mm::ops::AddIndex,
    mm::ops::HasNoOwnInstances,
    mm::ops::RemoveConstraint,
    mm::ops::UpdateRows,
    mm::ops::InsertRows,
    mm::ops::RenameColumn,
    mm::ops::AddColumn,
    mm::ops::AddTable,
    mm::ops::RemoveTable,
    mm::ops::SetColumnType,
    mm::ops::DeleteRows,
    mm::ops::AddSchema,
    Operations,
    mm::ops::AddNotNull,
    mm::ops::AddUnique,
    mm::ops::AddForeignKey,
    mm::rdb::TableConstraint,
    mm::rdb::Column,
    TableConstraint,
    mm::rdb::Unique,
    mm::rdb::Table,
    Column,
    mm::ops::ModelOperation,
    mm::rdb::ForeignKey,
    Sequence,
    mm::rdb::PrimaryKey,
    Table,
    Structure,
    mm::rdb::Schema,
    Schema,
    ops::ModelOperation,
    ModelRoot,
    mm::rdb::Structure,
    mm::rdb::Operations,
    mm::rdb::Index,
    mm::rdb::Sequence,
    Index,
    mm::rdb::ModelRoot,
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



def test_mm::ops::removeindex_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveIndex)


def test_mm::ops::removeindex_constructor_exists():
    assert callable(mm::ops::RemoveIndex.__init__)


def test_mm::ops::removeindex_constructor_args():
    sig = inspect.signature(mm::ops::RemoveIndex.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm::ops::removeindex_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveIndex, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveIndex.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removeindex_has_name():
    assert hasattr(mm::ops::RemoveIndex, "name")
    descriptor = None
    for klass in mm::ops::RemoveIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::setdefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm::ops::SetDefaultValue)


def test_mm::ops::setdefaultvalue_constructor_exists():
    assert callable(mm::ops::SetDefaultValue.__init__)


def test_mm::ops::setdefaultvalue_constructor_args():
    sig = inspect.signature(mm::ops::SetDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "newDefaultValue" in params, "Missing parameter 'newDefaultValue'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"

def test_mm::ops::setdefaultvalue_has_newDefaultValue():
    assert hasattr(mm::ops::SetDefaultValue, "newDefaultValue")
    descriptor = None
    for klass in mm::ops::SetDefaultValue.__mro__:
        if "newDefaultValue" in klass.__dict__:
            descriptor = klass.__dict__["newDefaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setdefaultvalue_has_owningSchemaName():
    assert hasattr(mm::ops::SetDefaultValue, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::SetDefaultValue.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setdefaultvalue_has_owningTableName():
    assert hasattr(mm::ops::SetDefaultValue, "owningTableName")
    descriptor = None
    for klass in mm::ops::SetDefaultValue.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setdefaultvalue_has_owningColumnName():
    assert hasattr(mm::ops::SetDefaultValue, "owningColumnName")
    descriptor = None
    for klass in mm::ops::SetDefaultValue.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::hasnoinstances_is_not_abstract():
    assert not inspect.isabstract(mm::ops::HasNoInstances)


def test_mm::ops::hasnoinstances_constructor_exists():
    assert callable(mm::ops::HasNoInstances.__init__)


def test_mm::ops::hasnoinstances_constructor_args():
    sig = inspect.signature(mm::ops::HasNoInstances.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::hasnoinstances_has_tableName():
    assert hasattr(mm::ops::HasNoInstances, "tableName")
    descriptor = None
    for klass in mm::ops::HasNoInstances.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::hasnoinstances_has_owningSchemaName():
    assert hasattr(mm::ops::HasNoInstances, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::HasNoInstances.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addprimarykey_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddPrimaryKey)


def test_mm::ops::addprimarykey_constructor_exists():
    assert callable(mm::ops::AddPrimaryKey.__init__)


def test_mm::ops::addprimarykey_constructor_args():
    sig = inspect.signature(mm::ops::AddPrimaryKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"

def test_mm::ops::addprimarykey_has_name():
    assert hasattr(mm::ops::AddPrimaryKey, "name")
    descriptor = None
    for klass in mm::ops::AddPrimaryKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addprimarykey_has_owningSchemaName():
    assert hasattr(mm::ops::AddPrimaryKey, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddPrimaryKey.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addprimarykey_has_owningTableName():
    assert hasattr(mm::ops::AddPrimaryKey, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddPrimaryKey.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addprimarykey_has_constrainedColumnName():
    assert hasattr(mm::ops::AddPrimaryKey, "constrainedColumnName")
    descriptor = None
    for klass in mm::ops::AddPrimaryKey.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addsequence_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddSequence)


def test_mm::ops::addsequence_constructor_exists():
    assert callable(mm::ops::AddSequence.__init__)


def test_mm::ops::addsequence_constructor_args():
    sig = inspect.signature(mm::ops::AddSequence.__init__)
    params = list(sig.parameters.keys())
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::addsequence_has_startValue():
    assert hasattr(mm::ops::AddSequence, "startValue")
    descriptor = None
    for klass in mm::ops::AddSequence.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addsequence_has_name():
    assert hasattr(mm::ops::AddSequence, "name")
    descriptor = None
    for klass in mm::ops::AddSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addsequence_has_owningSchemaName():
    assert hasattr(mm::ops::AddSequence, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddSequence.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removesequence_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveSequence)


def test_mm::ops::removesequence_constructor_exists():
    assert callable(mm::ops::RemoveSequence.__init__)


def test_mm::ops::removesequence_constructor_args():
    sig = inspect.signature(mm::ops::RemoveSequence.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::removesequence_has_name():
    assert hasattr(mm::ops::RemoveSequence, "name")
    descriptor = None
    for klass in mm::ops::RemoveSequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removesequence_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveSequence, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveSequence.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removedefaultvalue_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveDefaultValue)


def test_mm::ops::removedefaultvalue_constructor_exists():
    assert callable(mm::ops::RemoveDefaultValue.__init__)


def test_mm::ops::removedefaultvalue_constructor_args():
    sig = inspect.signature(mm::ops::RemoveDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::removedefaultvalue_has_owningColumnName():
    assert hasattr(mm::ops::RemoveDefaultValue, "owningColumnName")
    descriptor = None
    for klass in mm::ops::RemoveDefaultValue.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removedefaultvalue_has_owningTableName():
    assert hasattr(mm::ops::RemoveDefaultValue, "owningTableName")
    descriptor = None
    for klass in mm::ops::RemoveDefaultValue.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removedefaultvalue_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveDefaultValue, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveDefaultValue.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removecolumn_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveColumn)


def test_mm::ops::removecolumn_constructor_exists():
    assert callable(mm::ops::RemoveColumn.__init__)


def test_mm::ops::removecolumn_constructor_args():
    sig = inspect.signature(mm::ops::RemoveColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::removecolumn_has_owningTableName():
    assert hasattr(mm::ops::RemoveColumn, "owningTableName")
    descriptor = None
    for klass in mm::ops::RemoveColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removecolumn_has_name():
    assert hasattr(mm::ops::RemoveColumn, "name")
    descriptor = None
    for klass in mm::ops::RemoveColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removecolumn_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveColumn, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removenotnull_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveNotNull)


def test_mm::ops::removenotnull_constructor_exists():
    assert callable(mm::ops::RemoveNotNull.__init__)


def test_mm::ops::removenotnull_constructor_args():
    sig = inspect.signature(mm::ops::RemoveNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"

def test_mm::ops::removenotnull_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveNotNull, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveNotNull.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removenotnull_has_owningTableName():
    assert hasattr(mm::ops::RemoveNotNull, "owningTableName")
    descriptor = None
    for klass in mm::ops::RemoveNotNull.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removenotnull_has_constrainedColumnName():
    assert hasattr(mm::ops::RemoveNotNull, "constrainedColumnName")
    descriptor = None
    for klass in mm::ops::RemoveNotNull.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::nillrows_is_not_abstract():
    assert not inspect.isabstract(mm::ops::NillRows)


def test_mm::ops::nillrows_constructor_exists():
    assert callable(mm::ops::NillRows.__init__)


def test_mm::ops::nillrows_constructor_args():
    sig = inspect.signature(mm::ops::NillRows.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::nillrows_has_tableName():
    assert hasattr(mm::ops::NillRows, "tableName")
    descriptor = None
    for klass in mm::ops::NillRows.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::nillrows_has_whereCondition():
    assert hasattr(mm::ops::NillRows, "whereCondition")
    descriptor = None
    for klass in mm::ops::NillRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::nillrows_has_columnName():
    assert hasattr(mm::ops::NillRows, "columnName")
    descriptor = None
    for klass in mm::ops::NillRows.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::nillrows_has_owningSchemaName():
    assert hasattr(mm::ops::NillRows, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::NillRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::generatesequencenumbers_is_not_abstract():
    assert not inspect.isabstract(mm::ops::GenerateSequenceNumbers)


def test_mm::ops::generatesequencenumbers_constructor_exists():
    assert callable(mm::ops::GenerateSequenceNumbers.__init__)


def test_mm::ops::generatesequencenumbers_constructor_args():
    sig = inspect.signature(mm::ops::GenerateSequenceNumbers.__init__)
    params = list(sig.parameters.keys())
    assert "sequenceName" in params, "Missing parameter 'sequenceName'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm::ops::generatesequencenumbers_has_sequenceName():
    assert hasattr(mm::ops::GenerateSequenceNumbers, "sequenceName")
    descriptor = None
    for klass in mm::ops::GenerateSequenceNumbers.__mro__:
        if "sequenceName" in klass.__dict__:
            descriptor = klass.__dict__["sequenceName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::generatesequencenumbers_has_columnName():
    assert hasattr(mm::ops::GenerateSequenceNumbers, "columnName")
    descriptor = None
    for klass in mm::ops::GenerateSequenceNumbers.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::generatesequencenumbers_has_owningSchemaName():
    assert hasattr(mm::ops::GenerateSequenceNumbers, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::GenerateSequenceNumbers.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::generatesequencenumbers_has_tableName():
    assert hasattr(mm::ops::GenerateSequenceNumbers, "tableName")
    descriptor = None
    for klass in mm::ops::GenerateSequenceNumbers.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::renametable_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RenameTable)


def test_mm::ops::renametable_constructor_exists():
    assert callable(mm::ops::RenameTable.__init__)


def test_mm::ops::renametable_constructor_args():
    sig = inspect.signature(mm::ops::RenameTable.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "newName" in params, "Missing parameter 'newName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm::ops::renametable_has_owningSchemaName():
    assert hasattr(mm::ops::RenameTable, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RenameTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::renametable_has_newName():
    assert hasattr(mm::ops::RenameTable, "newName")
    descriptor = None
    for klass in mm::ops::RenameTable.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::renametable_has_name():
    assert hasattr(mm::ops::RenameTable, "name")
    descriptor = None
    for klass in mm::ops::RenameTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addindex_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddIndex)


def test_mm::ops::addindex_constructor_exists():
    assert callable(mm::ops::AddIndex.__init__)


def test_mm::ops::addindex_constructor_args():
    sig = inspect.signature(mm::ops::AddIndex.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "columnsNames" in params, "Missing parameter 'columnsNames'"

def test_mm::ops::addindex_has_owningTableName():
    assert hasattr(mm::ops::AddIndex, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddIndex.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addindex_has_owningSchemaName():
    assert hasattr(mm::ops::AddIndex, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddIndex.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addindex_has_name():
    assert hasattr(mm::ops::AddIndex, "name")
    descriptor = None
    for klass in mm::ops::AddIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addindex_has_columnsNames():
    assert hasattr(mm::ops::AddIndex, "columnsNames")
    descriptor = None
    for klass in mm::ops::AddIndex.__mro__:
        if "columnsNames" in klass.__dict__:
            descriptor = klass.__dict__["columnsNames"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::hasnoowninstances_is_not_abstract():
    assert not inspect.isabstract(mm::ops::HasNoOwnInstances)


def test_mm::ops::hasnoowninstances_constructor_exists():
    assert callable(mm::ops::HasNoOwnInstances.__init__)


def test_mm::ops::hasnoowninstances_constructor_args():
    sig = inspect.signature(mm::ops::HasNoOwnInstances.__init__)
    params = list(sig.parameters.keys())
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_mm::ops::hasnoowninstances_has_whereCondition():
    assert hasattr(mm::ops::HasNoOwnInstances, "whereCondition")
    descriptor = None
    for klass in mm::ops::HasNoOwnInstances.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::hasnoowninstances_has_owningSchemaName():
    assert hasattr(mm::ops::HasNoOwnInstances, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::HasNoOwnInstances.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::hasnoowninstances_has_tableName():
    assert hasattr(mm::ops::HasNoOwnInstances, "tableName")
    descriptor = None
    for klass in mm::ops::HasNoOwnInstances.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removeconstraint_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveConstraint)


def test_mm::ops::removeconstraint_constructor_exists():
    assert callable(mm::ops::RemoveConstraint.__init__)


def test_mm::ops::removeconstraint_constructor_args():
    sig = inspect.signature(mm::ops::RemoveConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm::ops::removeconstraint_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveConstraint, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveConstraint.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removeconstraint_has_owningTableName():
    assert hasattr(mm::ops::RemoveConstraint, "owningTableName")
    descriptor = None
    for klass in mm::ops::RemoveConstraint.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removeconstraint_has_name():
    assert hasattr(mm::ops::RemoveConstraint, "name")
    descriptor = None
    for klass in mm::ops::RemoveConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::updaterows_is_not_abstract():
    assert not inspect.isabstract(mm::ops::UpdateRows)


def test_mm::ops::updaterows_constructor_exists():
    assert callable(mm::ops::UpdateRows.__init__)


def test_mm::ops::updaterows_constructor_args():
    sig = inspect.signature(mm::ops::UpdateRows.__init__)
    params = list(sig.parameters.keys())
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "sourceColumnName" in params, "Missing parameter 'sourceColumnName'"
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"

def test_mm::ops::updaterows_has_whereCondition():
    assert hasattr(mm::ops::UpdateRows, "whereCondition")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::updaterows_has_sourceColumnName():
    assert hasattr(mm::ops::UpdateRows, "sourceColumnName")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "sourceColumnName" in klass.__dict__:
            descriptor = klass.__dict__["sourceColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::updaterows_has_sourceTableName():
    assert hasattr(mm::ops::UpdateRows, "sourceTableName")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "sourceTableName" in klass.__dict__:
            descriptor = klass.__dict__["sourceTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::updaterows_has_owningSchemaName():
    assert hasattr(mm::ops::UpdateRows, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::updaterows_has_targetTableName():
    assert hasattr(mm::ops::UpdateRows, "targetTableName")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::updaterows_has_targetColumnName():
    assert hasattr(mm::ops::UpdateRows, "targetColumnName")
    descriptor = None
    for klass in mm::ops::UpdateRows.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::insertrows_is_not_abstract():
    assert not inspect.isabstract(mm::ops::InsertRows)


def test_mm::ops::insertrows_constructor_exists():
    assert callable(mm::ops::InsertRows.__init__)


def test_mm::ops::insertrows_constructor_args():
    sig = inspect.signature(mm::ops::InsertRows.__init__)
    params = list(sig.parameters.keys())
    assert "sourceColumnsNames" in params, "Missing parameter 'sourceColumnsNames'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"
    assert "sourceTableName" in params, "Missing parameter 'sourceTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "targetColumnNames" in params, "Missing parameter 'targetColumnNames'"

def test_mm::ops::insertrows_has_sourceColumnsNames():
    assert hasattr(mm::ops::InsertRows, "sourceColumnsNames")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "sourceColumnsNames" in klass.__dict__:
            descriptor = klass.__dict__["sourceColumnsNames"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::insertrows_has_targetTableName():
    assert hasattr(mm::ops::InsertRows, "targetTableName")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::insertrows_has_whereCondition():
    assert hasattr(mm::ops::InsertRows, "whereCondition")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::insertrows_has_sourceTableName():
    assert hasattr(mm::ops::InsertRows, "sourceTableName")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "sourceTableName" in klass.__dict__:
            descriptor = klass.__dict__["sourceTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::insertrows_has_owningSchemaName():
    assert hasattr(mm::ops::InsertRows, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::insertrows_has_targetColumnNames():
    assert hasattr(mm::ops::InsertRows, "targetColumnNames")
    descriptor = None
    for klass in mm::ops::InsertRows.__mro__:
        if "targetColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnNames"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::renamecolumn_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RenameColumn)


def test_mm::ops::renamecolumn_constructor_exists():
    assert callable(mm::ops::RenameColumn.__init__)


def test_mm::ops::renamecolumn_constructor_args():
    sig = inspect.signature(mm::ops::RenameColumn.__init__)
    params = list(sig.parameters.keys())
    assert "newName" in params, "Missing parameter 'newName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm::ops::renamecolumn_has_newName():
    assert hasattr(mm::ops::RenameColumn, "newName")
    descriptor = None
    for klass in mm::ops::RenameColumn.__mro__:
        if "newName" in klass.__dict__:
            descriptor = klass.__dict__["newName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::renamecolumn_has_owningSchemaName():
    assert hasattr(mm::ops::RenameColumn, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RenameColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::renamecolumn_has_owningTableName():
    assert hasattr(mm::ops::RenameColumn, "owningTableName")
    descriptor = None
    for klass in mm::ops::RenameColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::renamecolumn_has_name():
    assert hasattr(mm::ops::RenameColumn, "name")
    descriptor = None
    for klass in mm::ops::RenameColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addcolumn_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddColumn)


def test_mm::ops::addcolumn_constructor_exists():
    assert callable(mm::ops::AddColumn.__init__)


def test_mm::ops::addcolumn_constructor_args():
    sig = inspect.signature(mm::ops::AddColumn.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "type" in params, "Missing parameter 'type'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_mm::ops::addcolumn_has_owningTableName():
    assert hasattr(mm::ops::AddColumn, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddColumn.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addcolumn_has_name():
    assert hasattr(mm::ops::AddColumn, "name")
    descriptor = None
    for klass in mm::ops::AddColumn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addcolumn_has_owningSchemaName():
    assert hasattr(mm::ops::AddColumn, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddColumn.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addcolumn_has_type():
    assert hasattr(mm::ops::AddColumn, "type")
    descriptor = None
    for klass in mm::ops::AddColumn.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addcolumn_has_defaultValue():
    assert hasattr(mm::ops::AddColumn, "defaultValue")
    descriptor = None
    for klass in mm::ops::AddColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addtable_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddTable)


def test_mm::ops::addtable_constructor_exists():
    assert callable(mm::ops::AddTable.__init__)


def test_mm::ops::addtable_constructor_args():
    sig = inspect.signature(mm::ops::AddTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::addtable_has_name():
    assert hasattr(mm::ops::AddTable, "name")
    descriptor = None
    for klass in mm::ops::AddTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addtable_has_owningSchemaName():
    assert hasattr(mm::ops::AddTable, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::removetable_is_not_abstract():
    assert not inspect.isabstract(mm::ops::RemoveTable)


def test_mm::ops::removetable_constructor_exists():
    assert callable(mm::ops::RemoveTable.__init__)


def test_mm::ops::removetable_constructor_args():
    sig = inspect.signature(mm::ops::RemoveTable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::removetable_has_name():
    assert hasattr(mm::ops::RemoveTable, "name")
    descriptor = None
    for klass in mm::ops::RemoveTable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::removetable_has_owningSchemaName():
    assert hasattr(mm::ops::RemoveTable, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::RemoveTable.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::setcolumntype_is_not_abstract():
    assert not inspect.isabstract(mm::ops::SetColumnType)


def test_mm::ops::setcolumntype_constructor_exists():
    assert callable(mm::ops::SetColumnType.__init__)


def test_mm::ops::setcolumntype_constructor_args():
    sig = inspect.signature(mm::ops::SetColumnType.__init__)
    params = list(sig.parameters.keys())
    assert "oldType" in params, "Missing parameter 'oldType'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "owningColumnName" in params, "Missing parameter 'owningColumnName'"
    assert "newType" in params, "Missing parameter 'newType'"

def test_mm::ops::setcolumntype_has_oldType():
    assert hasattr(mm::ops::SetColumnType, "oldType")
    descriptor = None
    for klass in mm::ops::SetColumnType.__mro__:
        if "oldType" in klass.__dict__:
            descriptor = klass.__dict__["oldType"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setcolumntype_has_owningTableName():
    assert hasattr(mm::ops::SetColumnType, "owningTableName")
    descriptor = None
    for klass in mm::ops::SetColumnType.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setcolumntype_has_owningSchemaName():
    assert hasattr(mm::ops::SetColumnType, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::SetColumnType.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setcolumntype_has_owningColumnName():
    assert hasattr(mm::ops::SetColumnType, "owningColumnName")
    descriptor = None
    for klass in mm::ops::SetColumnType.__mro__:
        if "owningColumnName" in klass.__dict__:
            descriptor = klass.__dict__["owningColumnName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::setcolumntype_has_newType():
    assert hasattr(mm::ops::SetColumnType, "newType")
    descriptor = None
    for klass in mm::ops::SetColumnType.__mro__:
        if "newType" in klass.__dict__:
            descriptor = klass.__dict__["newType"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::deleterows_is_not_abstract():
    assert not inspect.isabstract(mm::ops::DeleteRows)


def test_mm::ops::deleterows_constructor_exists():
    assert callable(mm::ops::DeleteRows.__init__)


def test_mm::ops::deleterows_constructor_args():
    sig = inspect.signature(mm::ops::DeleteRows.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "whereCondition" in params, "Missing parameter 'whereCondition'"

def test_mm::ops::deleterows_has_tableName():
    assert hasattr(mm::ops::DeleteRows, "tableName")
    descriptor = None
    for klass in mm::ops::DeleteRows.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::deleterows_has_owningSchemaName():
    assert hasattr(mm::ops::DeleteRows, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::DeleteRows.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::deleterows_has_whereCondition():
    assert hasattr(mm::ops::DeleteRows, "whereCondition")
    descriptor = None
    for klass in mm::ops::DeleteRows.__mro__:
        if "whereCondition" in klass.__dict__:
            descriptor = klass.__dict__["whereCondition"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addschema_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddSchema)


def test_mm::ops::addschema_constructor_exists():
    assert callable(mm::ops::AddSchema.__init__)


def test_mm::ops::addschema_constructor_args():
    sig = inspect.signature(mm::ops::AddSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm::ops::addschema_has_name():
    assert hasattr(mm::ops::AddSchema, "name")
    descriptor = None
    for klass in mm::ops::AddSchema.__mro__:
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



def test_mm::ops::addnotnull_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddNotNull)


def test_mm::ops::addnotnull_constructor_exists():
    assert callable(mm::ops::AddNotNull.__init__)


def test_mm::ops::addnotnull_constructor_args():
    sig = inspect.signature(mm::ops::AddNotNull.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"

def test_mm::ops::addnotnull_has_owningTableName():
    assert hasattr(mm::ops::AddNotNull, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddNotNull.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addnotnull_has_owningSchemaName():
    assert hasattr(mm::ops::AddNotNull, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddNotNull.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addnotnull_has_constrainedColumnName():
    assert hasattr(mm::ops::AddNotNull, "constrainedColumnName")
    descriptor = None
    for klass in mm::ops::AddNotNull.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addunique_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddUnique)


def test_mm::ops::addunique_constructor_exists():
    assert callable(mm::ops::AddUnique.__init__)


def test_mm::ops::addunique_constructor_args():
    sig = inspect.signature(mm::ops::AddUnique.__init__)
    params = list(sig.parameters.keys())
    assert "constrainedColumnNames" in params, "Missing parameter 'constrainedColumnNames'"
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"

def test_mm::ops::addunique_has_constrainedColumnNames():
    assert hasattr(mm::ops::AddUnique, "constrainedColumnNames")
    descriptor = None
    for klass in mm::ops::AddUnique.__mro__:
        if "constrainedColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnNames"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addunique_has_owningTableName():
    assert hasattr(mm::ops::AddUnique, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddUnique.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addunique_has_name():
    assert hasattr(mm::ops::AddUnique, "name")
    descriptor = None
    for klass in mm::ops::AddUnique.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addunique_has_owningSchemaName():
    assert hasattr(mm::ops::AddUnique, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddUnique.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)



def test_mm::ops::addforeignkey_is_not_abstract():
    assert not inspect.isabstract(mm::ops::AddForeignKey)


def test_mm::ops::addforeignkey_constructor_exists():
    assert callable(mm::ops::AddForeignKey.__init__)


def test_mm::ops::addforeignkey_constructor_args():
    sig = inspect.signature(mm::ops::AddForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "owningTableName" in params, "Missing parameter 'owningTableName'"
    assert "owningSchemaName" in params, "Missing parameter 'owningSchemaName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "targetTableName" in params, "Missing parameter 'targetTableName'"
    assert "constrainedColumnName" in params, "Missing parameter 'constrainedColumnName'"

def test_mm::ops::addforeignkey_has_owningTableName():
    assert hasattr(mm::ops::AddForeignKey, "owningTableName")
    descriptor = None
    for klass in mm::ops::AddForeignKey.__mro__:
        if "owningTableName" in klass.__dict__:
            descriptor = klass.__dict__["owningTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addforeignkey_has_owningSchemaName():
    assert hasattr(mm::ops::AddForeignKey, "owningSchemaName")
    descriptor = None
    for klass in mm::ops::AddForeignKey.__mro__:
        if "owningSchemaName" in klass.__dict__:
            descriptor = klass.__dict__["owningSchemaName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addforeignkey_has_name():
    assert hasattr(mm::ops::AddForeignKey, "name")
    descriptor = None
    for klass in mm::ops::AddForeignKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addforeignkey_has_targetTableName():
    assert hasattr(mm::ops::AddForeignKey, "targetTableName")
    descriptor = None
    for klass in mm::ops::AddForeignKey.__mro__:
        if "targetTableName" in klass.__dict__:
            descriptor = klass.__dict__["targetTableName"]
            break
    assert isinstance(descriptor, property)

def test_mm::ops::addforeignkey_has_constrainedColumnName():
    assert hasattr(mm::ops::AddForeignKey, "constrainedColumnName")
    descriptor = None
    for klass in mm::ops::AddForeignKey.__mro__:
        if "constrainedColumnName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedColumnName"]
            break
    assert isinstance(descriptor, property)



def test_mm::rdb::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::TableConstraint)


def test_mm::rdb::tableconstraint_constructor_exists():
    assert callable(mm::rdb::TableConstraint.__init__)


def test_mm::rdb::tableconstraint_constructor_args():
    sig = inspect.signature(mm::rdb::TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm::rdb::tableconstraint_has_name():
    assert hasattr(mm::rdb::TableConstraint, "name")
    descriptor = None
    for klass in mm::rdb::TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::rdb::column_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Column)


def test_mm::rdb::column_constructor_exists():
    assert callable(mm::rdb::Column.__init__)


def test_mm::rdb::column_constructor_args():
    sig = inspect.signature(mm::rdb::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isNillable" in params, "Missing parameter 'isNillable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_mm::rdb::column_has_name():
    assert hasattr(mm::rdb::Column, "name")
    descriptor = None
    for klass in mm::rdb::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm::rdb::column_has_type():
    assert hasattr(mm::rdb::Column, "type")
    descriptor = None
    for klass in mm::rdb::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mm::rdb::column_has_isNillable():
    assert hasattr(mm::rdb::Column, "isNillable")
    descriptor = None
    for klass in mm::rdb::Column.__mro__:
        if "isNillable" in klass.__dict__:
            descriptor = klass.__dict__["isNillable"]
            break
    assert isinstance(descriptor, property)

def test_mm::rdb::column_has_defaultValue():
    assert hasattr(mm::rdb::Column, "defaultValue")
    descriptor = None
    for klass in mm::rdb::Column.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::unique_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Unique)


def test_mm::rdb::unique_constructor_exists():
    assert callable(mm::rdb::Unique.__init__)


def test_mm::rdb::unique_constructor_args():
    sig = inspect.signature(mm::rdb::Unique.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::table_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Table)


def test_mm::rdb::table_constructor_exists():
    assert callable(mm::rdb::Table.__init__)


def test_mm::rdb::table_constructor_args():
    sig = inspect.signature(mm::rdb::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm::rdb::table_has_name():
    assert hasattr(mm::rdb::Table, "name")
    descriptor = None
    for klass in mm::rdb::Table.__mro__:
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



def test_mm::ops::modeloperation_is_not_abstract():
    assert not inspect.isabstract(mm::ops::ModelOperation)


def test_mm::ops::modeloperation_constructor_exists():
    assert callable(mm::ops::ModelOperation.__init__)


def test_mm::ops::modeloperation_constructor_args():
    sig = inspect.signature(mm::ops::ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::foreignkey_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::ForeignKey)


def test_mm::rdb::foreignkey_constructor_exists():
    assert callable(mm::rdb::ForeignKey.__init__)


def test_mm::rdb::foreignkey_constructor_args():
    sig = inspect.signature(mm::rdb::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::primarykey_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::PrimaryKey)


def test_mm::rdb::primarykey_constructor_exists():
    assert callable(mm::rdb::PrimaryKey.__init__)


def test_mm::rdb::primarykey_constructor_args():
    sig = inspect.signature(mm::rdb::PrimaryKey.__init__)
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



def test_mm::rdb::schema_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Schema)


def test_mm::rdb::schema_constructor_exists():
    assert callable(mm::rdb::Schema.__init__)


def test_mm::rdb::schema_constructor_args():
    sig = inspect.signature(mm::rdb::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm::rdb::schema_has_name():
    assert hasattr(mm::rdb::Schema, "name")
    descriptor = None
    for klass in mm::rdb::Schema.__mro__:
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



def test_ops::modeloperation_is_not_abstract():
    assert not inspect.isabstract(ops::ModelOperation)


def test_ops::modeloperation_constructor_exists():
    assert callable(ops::ModelOperation.__init__)


def test_ops::modeloperation_constructor_args():
    sig = inspect.signature(ops::ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_modelroot_is_not_abstract():
    assert not inspect.isabstract(ModelRoot)


def test_modelroot_constructor_exists():
    assert callable(ModelRoot.__init__)


def test_modelroot_constructor_args():
    sig = inspect.signature(ModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::structure_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Structure)


def test_mm::rdb::structure_constructor_exists():
    assert callable(mm::rdb::Structure.__init__)


def test_mm::rdb::structure_constructor_args():
    sig = inspect.signature(mm::rdb::Structure.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::operations_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Operations)


def test_mm::rdb::operations_constructor_exists():
    assert callable(mm::rdb::Operations.__init__)


def test_mm::rdb::operations_constructor_args():
    sig = inspect.signature(mm::rdb::Operations.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::index_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Index)


def test_mm::rdb::index_constructor_exists():
    assert callable(mm::rdb::Index.__init__)


def test_mm::rdb::index_constructor_args():
    sig = inspect.signature(mm::rdb::Index.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm::rdb::index_has_name():
    assert hasattr(mm::rdb::Index, "name")
    descriptor = None
    for klass in mm::rdb::Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm::rdb::sequence_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::Sequence)


def test_mm::rdb::sequence_constructor_exists():
    assert callable(mm::rdb::Sequence.__init__)


def test_mm::rdb::sequence_constructor_args():
    sig = inspect.signature(mm::rdb::Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm::rdb::sequence_has_startValue():
    assert hasattr(mm::rdb::Sequence, "startValue")
    descriptor = None
    for klass in mm::rdb::Sequence.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_mm::rdb::sequence_has_name():
    assert hasattr(mm::rdb::Sequence, "name")
    descriptor = None
    for klass in mm::rdb::Sequence.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_mm::rdb::modelroot_is_not_abstract():
    assert not inspect.isabstract(mm::rdb::ModelRoot)


def test_mm::rdb::modelroot_constructor_exists():
    assert callable(mm::rdb::ModelRoot.__init__)


def test_mm::rdb::modelroot_constructor_args():
    sig = inspect.signature(mm::rdb::ModelRoot.__init__)
    params = list(sig.parameters.keys())

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "boolean",
        "int",
        "char",
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
mm::ops::RemoveIndex_strategy = st.builds(
    mm::ops::RemoveIndex,
    owningSchemaName=
        safe_text,
    name=
        safe_text
)
mm::ops::SetDefaultValue_strategy = st.builds(
    mm::ops::SetDefaultValue,
    newDefaultValue=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    owningColumnName=
        safe_text
)
mm::ops::HasNoInstances_strategy = st.builds(
    mm::ops::HasNoInstances,
    tableName=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::AddPrimaryKey_strategy = st.builds(
    mm::ops::AddPrimaryKey,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm::ops::AddSequence_strategy = st.builds(
    mm::ops::AddSequence,
    startValue=
        st.integers(),
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::RemoveSequence_strategy = st.builds(
    mm::ops::RemoveSequence,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::RemoveDefaultValue_strategy = st.builds(
    mm::ops::RemoveDefaultValue,
    owningColumnName=
        safe_text,
    owningTableName=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::RemoveColumn_strategy = st.builds(
    mm::ops::RemoveColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::RemoveNotNull_strategy = st.builds(
    mm::ops::RemoveNotNull,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm::ops::NillRows_strategy = st.builds(
    mm::ops::NillRows,
    tableName=
        safe_text,
    whereCondition=
        safe_text,
    columnName=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::GenerateSequenceNumbers_strategy = st.builds(
    mm::ops::GenerateSequenceNumbers,
    sequenceName=
        safe_text,
    columnName=
        safe_text,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm::ops::RenameTable_strategy = st.builds(
    mm::ops::RenameTable,
    owningSchemaName=
        safe_text,
    newName=
        safe_text,
    name=
        safe_text
)
mm::ops::AddIndex_strategy = st.builds(
    mm::ops::AddIndex,
    owningTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    name=
        safe_text,
    columnsNames=
        safe_text
)
mm::ops::HasNoOwnInstances_strategy = st.builds(
    mm::ops::HasNoOwnInstances,
    whereCondition=
        safe_text,
    owningSchemaName=
        safe_text,
    tableName=
        safe_text
)
mm::ops::RemoveConstraint_strategy = st.builds(
    mm::ops::RemoveConstraint,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    name=
        safe_text
)
mm::ops::UpdateRows_strategy = st.builds(
    mm::ops::UpdateRows,
    whereCondition=
        safe_text,
    sourceColumnName=
        safe_text,
    sourceTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    targetTableName=
        safe_text,
    targetColumnName=
        safe_text
)
mm::ops::InsertRows_strategy = st.builds(
    mm::ops::InsertRows,
    sourceColumnsNames=
        safe_text,
    targetTableName=
        safe_text,
    whereCondition=
        safe_text,
    sourceTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    targetColumnNames=
        safe_text
)
mm::ops::RenameColumn_strategy = st.builds(
    mm::ops::RenameColumn,
    newName=
        safe_text,
    owningSchemaName=
        safe_text,
    owningTableName=
        safe_text,
    name=
        safe_text
)
mm::ops::AddColumn_strategy = st.builds(
    mm::ops::AddColumn,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text,
    type=
        safe_text,
    defaultValue=
        safe_text
)
mm::ops::AddTable_strategy = st.builds(
    mm::ops::AddTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::RemoveTable_strategy = st.builds(
    mm::ops::RemoveTable,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::SetColumnType_strategy = st.builds(
    mm::ops::SetColumnType,
    oldType=
        safe_text,
    owningTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    owningColumnName=
        safe_text,
    newType=
        safe_text
)
mm::ops::DeleteRows_strategy = st.builds(
    mm::ops::DeleteRows,
    tableName=
        safe_text,
    owningSchemaName=
        safe_text,
    whereCondition=
        safe_text
)
mm::ops::AddSchema_strategy = st.builds(
    mm::ops::AddSchema,
    name=
        safe_text
)
Operations_strategy = st.builds(
    Operations,
)
mm::ops::AddNotNull_strategy = st.builds(
    mm::ops::AddNotNull,
    owningTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm::ops::AddUnique_strategy = st.builds(
    mm::ops::AddUnique,
    constrainedColumnNames=
        safe_text,
    owningTableName=
        safe_text,
    name=
        safe_text,
    owningSchemaName=
        safe_text
)
mm::ops::AddForeignKey_strategy = st.builds(
    mm::ops::AddForeignKey,
    owningTableName=
        safe_text,
    owningSchemaName=
        safe_text,
    name=
        safe_text,
    targetTableName=
        safe_text,
    constrainedColumnName=
        safe_text
)
mm::rdb::TableConstraint_strategy = st.builds(
    mm::rdb::TableConstraint,
    name=
        safe_text
)
mm::rdb::Column_strategy = st.builds(
    mm::rdb::Column,
    name=
        safe_text,
    type=
        safe_text,
    isNillable=
        safe_text,
    defaultValue=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
mm::rdb::Unique_strategy = st.builds(
    mm::rdb::Unique,
)
mm::rdb::Table_strategy = st.builds(
    mm::rdb::Table,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
mm::ops::ModelOperation_strategy = st.builds(
    mm::ops::ModelOperation,
)
mm::rdb::ForeignKey_strategy = st.builds(
    mm::rdb::ForeignKey,
)
Sequence_strategy = st.builds(
    Sequence,
)
mm::rdb::PrimaryKey_strategy = st.builds(
    mm::rdb::PrimaryKey,
)
Table_strategy = st.builds(
    Table,
)
Structure_strategy = st.builds(
    Structure,
)
mm::rdb::Schema_strategy = st.builds(
    mm::rdb::Schema,
    name=
        safe_text
)
Schema_strategy = st.builds(
    Schema,
)
ops::ModelOperation_strategy = st.builds(
    ops::ModelOperation,
)
ModelRoot_strategy = st.builds(
    ModelRoot,
)
mm::rdb::Structure_strategy = st.builds(
    mm::rdb::Structure,
)
mm::rdb::Operations_strategy = st.builds(
    mm::rdb::Operations,
)
mm::rdb::Index_strategy = st.builds(
    mm::rdb::Index,
    name=
        safe_text
)
mm::rdb::Sequence_strategy = st.builds(
    mm::rdb::Sequence,
    startValue=
        st.integers(),
    name=
        safe_text
)
Index_strategy = st.builds(
    Index,
)
mm::rdb::ModelRoot_strategy = st.builds(
    mm::rdb::ModelRoot,
)

@given(instance=ModelOperation_strategy)
@settings(max_examples=50)
def test_modeloperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)

@given(instance=mm::ops::RemoveIndex_strategy)
@settings(max_examples=50)
def test_mm::ops::removeindex_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveIndex)

@given(instance=mm::ops::RemoveIndex_strategy)
def test_mm::ops::removeindex_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveIndex_strategy)
def test_mm::ops::removeindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveIndex_strategy)
def test_mm::ops::removeindex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RemoveIndex_strategy)
def test_mm::ops::removeindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::SetDefaultValue_strategy)
@settings(max_examples=50)
def test_mm::ops::setdefaultvalue_instantiation(instance):
    assert isinstance(instance, mm::ops::SetDefaultValue)

@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_newDefaultValue_type(instance):
    assert isinstance(instance.newDefaultValue, str)


@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_newDefaultValue_setter(instance):
    original = instance.newDefaultValue
    instance.newDefaultValue = original
    assert instance.newDefaultValue == original

@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningColumnName_type(instance):
    assert isinstance(instance.owningColumnName, str)


@given(instance=mm::ops::SetDefaultValue_strategy)
def test_mm::ops::setdefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original

@given(instance=mm::ops::HasNoInstances_strategy)
@settings(max_examples=50)
def test_mm::ops::hasnoinstances_instantiation(instance):
    assert isinstance(instance, mm::ops::HasNoInstances)

@given(instance=mm::ops::HasNoInstances_strategy)
def test_mm::ops::hasnoinstances_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=mm::ops::HasNoInstances_strategy)
def test_mm::ops::hasnoinstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm::ops::HasNoInstances_strategy)
def test_mm::ops::hasnoinstances_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::HasNoInstances_strategy)
def test_mm::ops::hasnoinstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddPrimaryKey_strategy)
@settings(max_examples=50)
def test_mm::ops::addprimarykey_instantiation(instance):
    assert isinstance(instance, mm::ops::AddPrimaryKey)

@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_constrainedColumnName_type(instance):
    assert isinstance(instance.constrainedColumnName, str)


@given(instance=mm::ops::AddPrimaryKey_strategy)
def test_mm::ops::addprimarykey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original

@given(instance=mm::ops::AddSequence_strategy)
@settings(max_examples=50)
def test_mm::ops::addsequence_instantiation(instance):
    assert isinstance(instance, mm::ops::AddSequence)

@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_startValue_type(instance):
    assert isinstance(instance.startValue, int)


@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original

@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddSequence_strategy)
def test_mm::ops::addsequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveSequence_strategy)
@settings(max_examples=50)
def test_mm::ops::removesequence_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveSequence)

@given(instance=mm::ops::RemoveSequence_strategy)
def test_mm::ops::removesequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RemoveSequence_strategy)
def test_mm::ops::removesequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::RemoveSequence_strategy)
def test_mm::ops::removesequence_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveSequence_strategy)
def test_mm::ops::removesequence_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveDefaultValue_strategy)
@settings(max_examples=50)
def test_mm::ops::removedefaultvalue_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveDefaultValue)

@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningColumnName_type(instance):
    assert isinstance(instance.owningColumnName, str)


@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original

@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveDefaultValue_strategy)
def test_mm::ops::removedefaultvalue_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveColumn_strategy)
@settings(max_examples=50)
def test_mm::ops::removecolumn_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveColumn)

@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveColumn_strategy)
def test_mm::ops::removecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveNotNull_strategy)
@settings(max_examples=50)
def test_mm::ops::removenotnull_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveNotNull)

@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_constrainedColumnName_type(instance):
    assert isinstance(instance.constrainedColumnName, str)


@given(instance=mm::ops::RemoveNotNull_strategy)
def test_mm::ops::removenotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original

@given(instance=mm::ops::NillRows_strategy)
@settings(max_examples=50)
def test_mm::ops::nillrows_instantiation(instance):
    assert isinstance(instance, mm::ops::NillRows)

@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_whereCondition_type(instance):
    assert isinstance(instance.whereCondition, str)


@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original

@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::NillRows_strategy)
def test_mm::ops::nillrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
@settings(max_examples=50)
def test_mm::ops::generatesequencenumbers_instantiation(instance):
    assert isinstance(instance, mm::ops::GenerateSequenceNumbers)

@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_sequenceName_type(instance):
    assert isinstance(instance.sequenceName, str)


@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_sequenceName_setter(instance):
    original = instance.sequenceName
    instance.sequenceName = original
    assert instance.sequenceName == original

@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=mm::ops::GenerateSequenceNumbers_strategy)
def test_mm::ops::generatesequencenumbers_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm::ops::RenameTable_strategy)
@settings(max_examples=50)
def test_mm::ops::renametable_instantiation(instance):
    assert isinstance(instance, mm::ops::RenameTable)

@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_newName_type(instance):
    assert isinstance(instance.newName, str)


@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original

@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RenameTable_strategy)
def test_mm::ops::renametable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddIndex_strategy)
@settings(max_examples=50)
def test_mm::ops::addindex_instantiation(instance):
    assert isinstance(instance, mm::ops::AddIndex)

@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_columnsNames_type(instance):
    assert isinstance(instance.columnsNames, str)


@given(instance=mm::ops::AddIndex_strategy)
def test_mm::ops::addindex_columnsNames_setter(instance):
    original = instance.columnsNames
    instance.columnsNames = original
    assert instance.columnsNames == original

@given(instance=mm::ops::HasNoOwnInstances_strategy)
@settings(max_examples=50)
def test_mm::ops::hasnoowninstances_instantiation(instance):
    assert isinstance(instance, mm::ops::HasNoOwnInstances)

@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_whereCondition_type(instance):
    assert isinstance(instance.whereCondition, str)


@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original

@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=mm::ops::HasNoOwnInstances_strategy)
def test_mm::ops::hasnoowninstances_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm::ops::RemoveConstraint_strategy)
@settings(max_examples=50)
def test_mm::ops::removeconstraint_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveConstraint)

@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RemoveConstraint_strategy)
def test_mm::ops::removeconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::UpdateRows_strategy)
@settings(max_examples=50)
def test_mm::ops::updaterows_instantiation(instance):
    assert isinstance(instance, mm::ops::UpdateRows)

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_whereCondition_type(instance):
    assert isinstance(instance.whereCondition, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_sourceColumnName_type(instance):
    assert isinstance(instance.sourceColumnName, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_sourceColumnName_setter(instance):
    original = instance.sourceColumnName
    instance.sourceColumnName = original
    assert instance.sourceColumnName == original

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_sourceTableName_type(instance):
    assert isinstance(instance.sourceTableName, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_targetTableName_type(instance):
    assert isinstance(instance.targetTableName, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original

@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_targetColumnName_type(instance):
    assert isinstance(instance.targetColumnName, str)


@given(instance=mm::ops::UpdateRows_strategy)
def test_mm::ops::updaterows_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=mm::ops::InsertRows_strategy)
@settings(max_examples=50)
def test_mm::ops::insertrows_instantiation(instance):
    assert isinstance(instance, mm::ops::InsertRows)

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_sourceColumnsNames_type(instance):
    assert isinstance(instance.sourceColumnsNames, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_sourceColumnsNames_setter(instance):
    original = instance.sourceColumnsNames
    instance.sourceColumnsNames = original
    assert instance.sourceColumnsNames == original

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_targetTableName_type(instance):
    assert isinstance(instance.targetTableName, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_whereCondition_type(instance):
    assert isinstance(instance.whereCondition, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_sourceTableName_type(instance):
    assert isinstance(instance.sourceTableName, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_sourceTableName_setter(instance):
    original = instance.sourceTableName
    instance.sourceTableName = original
    assert instance.sourceTableName == original

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_targetColumnNames_type(instance):
    assert isinstance(instance.targetColumnNames, str)


@given(instance=mm::ops::InsertRows_strategy)
def test_mm::ops::insertrows_targetColumnNames_setter(instance):
    original = instance.targetColumnNames
    instance.targetColumnNames = original
    assert instance.targetColumnNames == original

@given(instance=mm::ops::RenameColumn_strategy)
@settings(max_examples=50)
def test_mm::ops::renamecolumn_instantiation(instance):
    assert isinstance(instance, mm::ops::RenameColumn)

@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_newName_type(instance):
    assert isinstance(instance.newName, str)


@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_newName_setter(instance):
    original = instance.newName
    instance.newName = original
    assert instance.newName == original

@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RenameColumn_strategy)
def test_mm::ops::renamecolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddColumn_strategy)
@settings(max_examples=50)
def test_mm::ops::addcolumn_instantiation(instance):
    assert isinstance(instance, mm::ops::AddColumn)

@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=mm::ops::AddColumn_strategy)
def test_mm::ops::addcolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=mm::ops::AddTable_strategy)
@settings(max_examples=50)
def test_mm::ops::addtable_instantiation(instance):
    assert isinstance(instance, mm::ops::AddTable)

@given(instance=mm::ops::AddTable_strategy)
def test_mm::ops::addtable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddTable_strategy)
def test_mm::ops::addtable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddTable_strategy)
def test_mm::ops::addtable_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddTable_strategy)
def test_mm::ops::addtable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::RemoveTable_strategy)
@settings(max_examples=50)
def test_mm::ops::removetable_instantiation(instance):
    assert isinstance(instance, mm::ops::RemoveTable)

@given(instance=mm::ops::RemoveTable_strategy)
def test_mm::ops::removetable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::RemoveTable_strategy)
def test_mm::ops::removetable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::RemoveTable_strategy)
def test_mm::ops::removetable_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::RemoveTable_strategy)
def test_mm::ops::removetable_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::SetColumnType_strategy)
@settings(max_examples=50)
def test_mm::ops::setcolumntype_instantiation(instance):
    assert isinstance(instance, mm::ops::SetColumnType)

@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_oldType_type(instance):
    assert isinstance(instance.oldType, str)


@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_oldType_setter(instance):
    original = instance.oldType
    instance.oldType = original
    assert instance.oldType == original

@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningColumnName_type(instance):
    assert isinstance(instance.owningColumnName, str)


@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_owningColumnName_setter(instance):
    original = instance.owningColumnName
    instance.owningColumnName = original
    assert instance.owningColumnName == original

@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_newType_type(instance):
    assert isinstance(instance.newType, str)


@given(instance=mm::ops::SetColumnType_strategy)
def test_mm::ops::setcolumntype_newType_setter(instance):
    original = instance.newType
    instance.newType = original
    assert instance.newType == original

@given(instance=mm::ops::DeleteRows_strategy)
@settings(max_examples=50)
def test_mm::ops::deleterows_instantiation(instance):
    assert isinstance(instance, mm::ops::DeleteRows)

@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_whereCondition_type(instance):
    assert isinstance(instance.whereCondition, str)


@given(instance=mm::ops::DeleteRows_strategy)
def test_mm::ops::deleterows_whereCondition_setter(instance):
    original = instance.whereCondition
    instance.whereCondition = original
    assert instance.whereCondition == original

@given(instance=mm::ops::AddSchema_strategy)
@settings(max_examples=50)
def test_mm::ops::addschema_instantiation(instance):
    assert isinstance(instance, mm::ops::AddSchema)

@given(instance=mm::ops::AddSchema_strategy)
def test_mm::ops::addschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddSchema_strategy)
def test_mm::ops::addschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Operations_strategy)
@settings(max_examples=50)
def test_operations_instantiation(instance):
    assert isinstance(instance, Operations)

@given(instance=mm::ops::AddNotNull_strategy)
@settings(max_examples=50)
def test_mm::ops::addnotnull_instantiation(instance):
    assert isinstance(instance, mm::ops::AddNotNull)

@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_constrainedColumnName_type(instance):
    assert isinstance(instance.constrainedColumnName, str)


@given(instance=mm::ops::AddNotNull_strategy)
def test_mm::ops::addnotnull_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original

@given(instance=mm::ops::AddUnique_strategy)
@settings(max_examples=50)
def test_mm::ops::addunique_instantiation(instance):
    assert isinstance(instance, mm::ops::AddUnique)

@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_constrainedColumnNames_type(instance):
    assert isinstance(instance.constrainedColumnNames, str)


@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_constrainedColumnNames_setter(instance):
    original = instance.constrainedColumnNames
    instance.constrainedColumnNames = original
    assert instance.constrainedColumnNames == original

@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddUnique_strategy)
def test_mm::ops::addunique_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddForeignKey_strategy)
@settings(max_examples=50)
def test_mm::ops::addforeignkey_instantiation(instance):
    assert isinstance(instance, mm::ops::AddForeignKey)

@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_owningTableName_type(instance):
    assert isinstance(instance.owningTableName, str)


@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_owningTableName_setter(instance):
    original = instance.owningTableName
    instance.owningTableName = original
    assert instance.owningTableName == original

@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_owningSchemaName_type(instance):
    assert isinstance(instance.owningSchemaName, str)


@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_owningSchemaName_setter(instance):
    original = instance.owningSchemaName
    instance.owningSchemaName = original
    assert instance.owningSchemaName == original

@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_targetTableName_type(instance):
    assert isinstance(instance.targetTableName, str)


@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_targetTableName_setter(instance):
    original = instance.targetTableName
    instance.targetTableName = original
    assert instance.targetTableName == original

@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_constrainedColumnName_type(instance):
    assert isinstance(instance.constrainedColumnName, str)


@given(instance=mm::ops::AddForeignKey_strategy)
def test_mm::ops::addforeignkey_constrainedColumnName_setter(instance):
    original = instance.constrainedColumnName
    instance.constrainedColumnName = original
    assert instance.constrainedColumnName == original

@given(instance=mm::rdb::TableConstraint_strategy)
@settings(max_examples=50)
def test_mm::rdb::tableconstraint_instantiation(instance):
    assert isinstance(instance, mm::rdb::TableConstraint)

@given(instance=mm::rdb::TableConstraint_strategy)
def test_mm::rdb::tableconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::TableConstraint_strategy)
def test_mm::rdb::tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::rdb::Column_strategy)
@settings(max_examples=50)
def test_mm::rdb::column_instantiation(instance):
    assert isinstance(instance, mm::rdb::Column)

@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_isNillable_type(instance):
    assert isinstance(instance.isNillable, str)


@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_isNillable_setter(instance):
    original = instance.isNillable
    instance.isNillable = original
    assert instance.isNillable == original

@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=mm::rdb::Column_strategy)
def test_mm::rdb::column_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=mm::rdb::Unique_strategy)
@settings(max_examples=50)
def test_mm::rdb::unique_instantiation(instance):
    assert isinstance(instance, mm::rdb::Unique)

@given(instance=mm::rdb::Table_strategy)
@settings(max_examples=50)
def test_mm::rdb::table_instantiation(instance):
    assert isinstance(instance, mm::rdb::Table)

@given(instance=mm::rdb::Table_strategy)
def test_mm::rdb::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::Table_strategy)
def test_mm::rdb::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=mm::ops::ModelOperation_strategy)
@settings(max_examples=50)
def test_mm::ops::modeloperation_instantiation(instance):
    assert isinstance(instance, mm::ops::ModelOperation)

@given(instance=mm::rdb::ForeignKey_strategy)
@settings(max_examples=50)
def test_mm::rdb::foreignkey_instantiation(instance):
    assert isinstance(instance, mm::rdb::ForeignKey)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=mm::rdb::PrimaryKey_strategy)
@settings(max_examples=50)
def test_mm::rdb::primarykey_instantiation(instance):
    assert isinstance(instance, mm::rdb::PrimaryKey)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=mm::rdb::Schema_strategy)
@settings(max_examples=50)
def test_mm::rdb::schema_instantiation(instance):
    assert isinstance(instance, mm::rdb::Schema)

@given(instance=mm::rdb::Schema_strategy)
def test_mm::rdb::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::Schema_strategy)
def test_mm::rdb::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=ops::ModelOperation_strategy)
@settings(max_examples=50)
def test_ops::modeloperation_instantiation(instance):
    assert isinstance(instance, ops::ModelOperation)

@given(instance=ModelRoot_strategy)
@settings(max_examples=50)
def test_modelroot_instantiation(instance):
    assert isinstance(instance, ModelRoot)

@given(instance=mm::rdb::Structure_strategy)
@settings(max_examples=50)
def test_mm::rdb::structure_instantiation(instance):
    assert isinstance(instance, mm::rdb::Structure)

@given(instance=mm::rdb::Operations_strategy)
@settings(max_examples=50)
def test_mm::rdb::operations_instantiation(instance):
    assert isinstance(instance, mm::rdb::Operations)

@given(instance=mm::rdb::Index_strategy)
@settings(max_examples=50)
def test_mm::rdb::index_instantiation(instance):
    assert isinstance(instance, mm::rdb::Index)

@given(instance=mm::rdb::Index_strategy)
def test_mm::rdb::index_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::Index_strategy)
def test_mm::rdb::index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm::rdb::Sequence_strategy)
@settings(max_examples=50)
def test_mm::rdb::sequence_instantiation(instance):
    assert isinstance(instance, mm::rdb::Sequence)

@given(instance=mm::rdb::Sequence_strategy)
def test_mm::rdb::sequence_startValue_type(instance):
    assert isinstance(instance.startValue, int)


@given(instance=mm::rdb::Sequence_strategy)
def test_mm::rdb::sequence_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original

@given(instance=mm::rdb::Sequence_strategy)
def test_mm::rdb::sequence_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm::rdb::Sequence_strategy)
def test_mm::rdb::sequence_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=mm::rdb::ModelRoot_strategy)
@settings(max_examples=50)
def test_mm::rdb::modelroot_instantiation(instance):
    assert isinstance(instance, mm::rdb::ModelRoot)
