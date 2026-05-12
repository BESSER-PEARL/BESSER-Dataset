import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dbevolution_EObject,
    Diff,
    dbevolution_DBDiff,
    SchemaChange,
    dbevolution_RemoveSchema,
    dbevolution_UpdateSchemaCommentChange,
    dbevolution_AlterSchema,
    dbevolution_RenameSchemaChange,
    dbevolution_AddSchema,
    dbevolution_Schema,
    SequenceChange,
    dbevolution_RemoveSequence,
    dbevolution_UpdateSequence,
    dbevolution_AddSequence,
    dbevolution_Sequence,
    ForeignKeyChange,
    dbevolution_UpdateForeignKey,
    dbevolution_AddForeignKey,
    dbevolution_ForeignKey,
    IndexChange,
    dbevolution_UpdateIndex,
    dbevolution_RemoveIndex,
    dbevolution_AddIndex,
    dbevolution_Index,
    PrimaryKeyChange,
    dbevolution_RemovePrimaryKey,
    dbevolution_UpdatePrimaryKey,
    dbevolution_AddPrimaryKey,
    dbevolution_PrimaryKey,
    ConstraintChange,
    dbevolution_UpdateConstraint,
    dbevolution_RemoveConstraint,
    dbevolution_AddConstraint,
    dbevolution_Constraint,
    TableChange,
    dbevolution_RemoveTable,
    dbevolution_RenameTableChange,
    dbevolution_UpdateTableCommentChange,
    dbevolution_AlterTable,
    dbevolution_AddTable,
    dbevolution_Table,
    DBDiff,
    dbevolution_SequenceChange,
    dbevolution_ConstraintChange,
    dbevolution_ForeignKeyChange,
    dbevolution_IndexChange,
    dbevolution_SchemaChange,
    dbevolution_PrimaryKeyChange,
    dbevolution_ColumnChange,
    dbevolution_TableChange,
    Comparison,
    dbevolution_DatabaseChangeSet,
    ColumnChange,
    dbevolution_UpdateColumnChange,
    dbevolution_RemoveColumnChange,
    dbevolution_UpdateColumnCommentChange,
    dbevolution_RenameColumnChange,
    dbevolution_AddColumnChange,
    dbevolution_Column,
    dbevolution_RemoveForeignKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbevolution_eobject_is_not_abstract():
    assert not inspect.isabstract(dbevolution_EObject)


def test_dbevolution_eobject_constructor_exists():
    assert callable(dbevolution_EObject.__init__)


def test_dbevolution_eobject_constructor_args():
    sig = inspect.signature(dbevolution_EObject.__init__)
    params = list(sig.parameters.keys())



def test_diff_is_not_abstract():
    assert not inspect.isabstract(Diff)


def test_diff_constructor_exists():
    assert callable(Diff.__init__)


def test_diff_constructor_args():
    sig = inspect.signature(Diff.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_dbdiff_is_not_abstract():
    assert not inspect.isabstract(dbevolution_DBDiff)


def test_dbevolution_dbdiff_constructor_exists():
    assert callable(dbevolution_DBDiff.__init__)


def test_dbevolution_dbdiff_constructor_args():
    sig = inspect.signature(dbevolution_DBDiff.__init__)
    params = list(sig.parameters.keys())



def test_schemachange_is_not_abstract():
    assert not inspect.isabstract(SchemaChange)


def test_schemachange_constructor_exists():
    assert callable(SchemaChange.__init__)


def test_schemachange_constructor_args():
    sig = inspect.signature(SchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removeschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveSchema)


def test_dbevolution_removeschema_constructor_exists():
    assert callable(dbevolution_RemoveSchema.__init__)


def test_dbevolution_removeschema_constructor_args():
    sig = inspect.signature(dbevolution_RemoveSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updateschemacommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateSchemaCommentChange)


def test_dbevolution_updateschemacommentchange_constructor_exists():
    assert callable(dbevolution_UpdateSchemaCommentChange.__init__)


def test_dbevolution_updateschemacommentchange_constructor_args():
    sig = inspect.signature(dbevolution_UpdateSchemaCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_alterschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AlterSchema)


def test_dbevolution_alterschema_constructor_exists():
    assert callable(dbevolution_AlterSchema.__init__)


def test_dbevolution_alterschema_constructor_args():
    sig = inspect.signature(dbevolution_AlterSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_renameschemachange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RenameSchemaChange)


def test_dbevolution_renameschemachange_constructor_exists():
    assert callable(dbevolution_RenameSchemaChange.__init__)


def test_dbevolution_renameschemachange_constructor_args():
    sig = inspect.signature(dbevolution_RenameSchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddSchema)


def test_dbevolution_addschema_constructor_exists():
    assert callable(dbevolution_AddSchema.__init__)


def test_dbevolution_addschema_constructor_args():
    sig = inspect.signature(dbevolution_AddSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_schema_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Schema)


def test_dbevolution_schema_constructor_exists():
    assert callable(dbevolution_Schema.__init__)


def test_dbevolution_schema_constructor_args():
    sig = inspect.signature(dbevolution_Schema.__init__)
    params = list(sig.parameters.keys())



def test_sequencechange_is_not_abstract():
    assert not inspect.isabstract(SequenceChange)


def test_sequencechange_constructor_exists():
    assert callable(SequenceChange.__init__)


def test_sequencechange_constructor_args():
    sig = inspect.signature(SequenceChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removesequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveSequence)


def test_dbevolution_removesequence_constructor_exists():
    assert callable(dbevolution_RemoveSequence.__init__)


def test_dbevolution_removesequence_constructor_args():
    sig = inspect.signature(dbevolution_RemoveSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updatesequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateSequence)


def test_dbevolution_updatesequence_constructor_exists():
    assert callable(dbevolution_UpdateSequence.__init__)


def test_dbevolution_updatesequence_constructor_args():
    sig = inspect.signature(dbevolution_UpdateSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addsequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddSequence)


def test_dbevolution_addsequence_constructor_exists():
    assert callable(dbevolution_AddSequence.__init__)


def test_dbevolution_addsequence_constructor_args():
    sig = inspect.signature(dbevolution_AddSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_sequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Sequence)


def test_dbevolution_sequence_constructor_exists():
    assert callable(dbevolution_Sequence.__init__)


def test_dbevolution_sequence_constructor_args():
    sig = inspect.signature(dbevolution_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_foreignkeychange_is_not_abstract():
    assert not inspect.isabstract(ForeignKeyChange)


def test_foreignkeychange_constructor_exists():
    assert callable(ForeignKeyChange.__init__)


def test_foreignkeychange_constructor_args():
    sig = inspect.signature(ForeignKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updateforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateForeignKey)


def test_dbevolution_updateforeignkey_constructor_exists():
    assert callable(dbevolution_UpdateForeignKey.__init__)


def test_dbevolution_updateforeignkey_constructor_args():
    sig = inspect.signature(dbevolution_UpdateForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddForeignKey)


def test_dbevolution_addforeignkey_constructor_exists():
    assert callable(dbevolution_AddForeignKey.__init__)


def test_dbevolution_addforeignkey_constructor_args():
    sig = inspect.signature(dbevolution_AddForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_foreignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_ForeignKey)


def test_dbevolution_foreignkey_constructor_exists():
    assert callable(dbevolution_ForeignKey.__init__)


def test_dbevolution_foreignkey_constructor_args():
    sig = inspect.signature(dbevolution_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_indexchange_is_not_abstract():
    assert not inspect.isabstract(IndexChange)


def test_indexchange_constructor_exists():
    assert callable(IndexChange.__init__)


def test_indexchange_constructor_args():
    sig = inspect.signature(IndexChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updateindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateIndex)


def test_dbevolution_updateindex_constructor_exists():
    assert callable(dbevolution_UpdateIndex.__init__)


def test_dbevolution_updateindex_constructor_args():
    sig = inspect.signature(dbevolution_UpdateIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removeindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveIndex)


def test_dbevolution_removeindex_constructor_exists():
    assert callable(dbevolution_RemoveIndex.__init__)


def test_dbevolution_removeindex_constructor_args():
    sig = inspect.signature(dbevolution_RemoveIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddIndex)


def test_dbevolution_addindex_constructor_exists():
    assert callable(dbevolution_AddIndex.__init__)


def test_dbevolution_addindex_constructor_args():
    sig = inspect.signature(dbevolution_AddIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_index_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Index)


def test_dbevolution_index_constructor_exists():
    assert callable(dbevolution_Index.__init__)


def test_dbevolution_index_constructor_args():
    sig = inspect.signature(dbevolution_Index.__init__)
    params = list(sig.parameters.keys())



def test_primarykeychange_is_not_abstract():
    assert not inspect.isabstract(PrimaryKeyChange)


def test_primarykeychange_constructor_exists():
    assert callable(PrimaryKeyChange.__init__)


def test_primarykeychange_constructor_args():
    sig = inspect.signature(PrimaryKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removeprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemovePrimaryKey)


def test_dbevolution_removeprimarykey_constructor_exists():
    assert callable(dbevolution_RemovePrimaryKey.__init__)


def test_dbevolution_removeprimarykey_constructor_args():
    sig = inspect.signature(dbevolution_RemovePrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updateprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdatePrimaryKey)


def test_dbevolution_updateprimarykey_constructor_exists():
    assert callable(dbevolution_UpdatePrimaryKey.__init__)


def test_dbevolution_updateprimarykey_constructor_args():
    sig = inspect.signature(dbevolution_UpdatePrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddPrimaryKey)


def test_dbevolution_addprimarykey_constructor_exists():
    assert callable(dbevolution_AddPrimaryKey.__init__)


def test_dbevolution_addprimarykey_constructor_args():
    sig = inspect.signature(dbevolution_AddPrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_primarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_PrimaryKey)


def test_dbevolution_primarykey_constructor_exists():
    assert callable(dbevolution_PrimaryKey.__init__)


def test_dbevolution_primarykey_constructor_args():
    sig = inspect.signature(dbevolution_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_constraintchange_is_not_abstract():
    assert not inspect.isabstract(ConstraintChange)


def test_constraintchange_constructor_exists():
    assert callable(ConstraintChange.__init__)


def test_constraintchange_constructor_args():
    sig = inspect.signature(ConstraintChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updateconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateConstraint)


def test_dbevolution_updateconstraint_constructor_exists():
    assert callable(dbevolution_UpdateConstraint.__init__)


def test_dbevolution_updateconstraint_constructor_args():
    sig = inspect.signature(dbevolution_UpdateConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removeconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveConstraint)


def test_dbevolution_removeconstraint_constructor_exists():
    assert callable(dbevolution_RemoveConstraint.__init__)


def test_dbevolution_removeconstraint_constructor_args():
    sig = inspect.signature(dbevolution_RemoveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddConstraint)


def test_dbevolution_addconstraint_constructor_exists():
    assert callable(dbevolution_AddConstraint.__init__)


def test_dbevolution_addconstraint_constructor_args():
    sig = inspect.signature(dbevolution_AddConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_constraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Constraint)


def test_dbevolution_constraint_constructor_exists():
    assert callable(dbevolution_Constraint.__init__)


def test_dbevolution_constraint_constructor_args():
    sig = inspect.signature(dbevolution_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_tablechange_is_not_abstract():
    assert not inspect.isabstract(TableChange)


def test_tablechange_constructor_exists():
    assert callable(TableChange.__init__)


def test_tablechange_constructor_args():
    sig = inspect.signature(TableChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removetable_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveTable)


def test_dbevolution_removetable_constructor_exists():
    assert callable(dbevolution_RemoveTable.__init__)


def test_dbevolution_removetable_constructor_args():
    sig = inspect.signature(dbevolution_RemoveTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_renametablechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RenameTableChange)


def test_dbevolution_renametablechange_constructor_exists():
    assert callable(dbevolution_RenameTableChange.__init__)


def test_dbevolution_renametablechange_constructor_args():
    sig = inspect.signature(dbevolution_RenameTableChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updatetablecommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateTableCommentChange)


def test_dbevolution_updatetablecommentchange_constructor_exists():
    assert callable(dbevolution_UpdateTableCommentChange.__init__)


def test_dbevolution_updatetablecommentchange_constructor_args():
    sig = inspect.signature(dbevolution_UpdateTableCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_altertable_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AlterTable)


def test_dbevolution_altertable_constructor_exists():
    assert callable(dbevolution_AlterTable.__init__)


def test_dbevolution_altertable_constructor_args():
    sig = inspect.signature(dbevolution_AlterTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addtable_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddTable)


def test_dbevolution_addtable_constructor_exists():
    assert callable(dbevolution_AddTable.__init__)


def test_dbevolution_addtable_constructor_args():
    sig = inspect.signature(dbevolution_AddTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_table_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Table)


def test_dbevolution_table_constructor_exists():
    assert callable(dbevolution_Table.__init__)


def test_dbevolution_table_constructor_args():
    sig = inspect.signature(dbevolution_Table.__init__)
    params = list(sig.parameters.keys())



def test_dbdiff_is_not_abstract():
    assert not inspect.isabstract(DBDiff)


def test_dbdiff_constructor_exists():
    assert callable(DBDiff.__init__)


def test_dbdiff_constructor_args():
    sig = inspect.signature(DBDiff.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_sequencechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_SequenceChange)


def test_dbevolution_sequencechange_constructor_exists():
    assert callable(dbevolution_SequenceChange.__init__)


def test_dbevolution_sequencechange_constructor_args():
    sig = inspect.signature(dbevolution_SequenceChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_constraintchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_ConstraintChange)


def test_dbevolution_constraintchange_constructor_exists():
    assert callable(dbevolution_ConstraintChange.__init__)


def test_dbevolution_constraintchange_constructor_args():
    sig = inspect.signature(dbevolution_ConstraintChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_foreignkeychange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_ForeignKeyChange)


def test_dbevolution_foreignkeychange_constructor_exists():
    assert callable(dbevolution_ForeignKeyChange.__init__)


def test_dbevolution_foreignkeychange_constructor_args():
    sig = inspect.signature(dbevolution_ForeignKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_indexchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_IndexChange)


def test_dbevolution_indexchange_constructor_exists():
    assert callable(dbevolution_IndexChange.__init__)


def test_dbevolution_indexchange_constructor_args():
    sig = inspect.signature(dbevolution_IndexChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_schemachange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_SchemaChange)


def test_dbevolution_schemachange_constructor_exists():
    assert callable(dbevolution_SchemaChange.__init__)


def test_dbevolution_schemachange_constructor_args():
    sig = inspect.signature(dbevolution_SchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_primarykeychange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_PrimaryKeyChange)


def test_dbevolution_primarykeychange_constructor_exists():
    assert callable(dbevolution_PrimaryKeyChange.__init__)


def test_dbevolution_primarykeychange_constructor_args():
    sig = inspect.signature(dbevolution_PrimaryKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_columnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_ColumnChange)


def test_dbevolution_columnchange_constructor_exists():
    assert callable(dbevolution_ColumnChange.__init__)


def test_dbevolution_columnchange_constructor_args():
    sig = inspect.signature(dbevolution_ColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_tablechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_TableChange)


def test_dbevolution_tablechange_constructor_exists():
    assert callable(dbevolution_TableChange.__init__)


def test_dbevolution_tablechange_constructor_args():
    sig = inspect.signature(dbevolution_TableChange.__init__)
    params = list(sig.parameters.keys())



def test_comparison_is_not_abstract():
    assert not inspect.isabstract(Comparison)


def test_comparison_constructor_exists():
    assert callable(Comparison.__init__)


def test_comparison_constructor_args():
    sig = inspect.signature(Comparison.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_databasechangeset_is_not_abstract():
    assert not inspect.isabstract(dbevolution_DatabaseChangeSet)


def test_dbevolution_databasechangeset_constructor_exists():
    assert callable(dbevolution_DatabaseChangeSet.__init__)


def test_dbevolution_databasechangeset_constructor_args():
    sig = inspect.signature(dbevolution_DatabaseChangeSet.__init__)
    params = list(sig.parameters.keys())



def test_columnchange_is_not_abstract():
    assert not inspect.isabstract(ColumnChange)


def test_columnchange_constructor_exists():
    assert callable(ColumnChange.__init__)


def test_columnchange_constructor_args():
    sig = inspect.signature(ColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updatecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateColumnChange)


def test_dbevolution_updatecolumnchange_constructor_exists():
    assert callable(dbevolution_UpdateColumnChange.__init__)


def test_dbevolution_updatecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution_UpdateColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveColumnChange)


def test_dbevolution_removecolumnchange_constructor_exists():
    assert callable(dbevolution_RemoveColumnChange.__init__)


def test_dbevolution_removecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution_RemoveColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_updatecolumncommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_UpdateColumnCommentChange)


def test_dbevolution_updatecolumncommentchange_constructor_exists():
    assert callable(dbevolution_UpdateColumnCommentChange.__init__)


def test_dbevolution_updatecolumncommentchange_constructor_args():
    sig = inspect.signature(dbevolution_UpdateColumnCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_renamecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RenameColumnChange)


def test_dbevolution_renamecolumnchange_constructor_exists():
    assert callable(dbevolution_RenameColumnChange.__init__)


def test_dbevolution_renamecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution_RenameColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_addcolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution_AddColumnChange)


def test_dbevolution_addcolumnchange_constructor_exists():
    assert callable(dbevolution_AddColumnChange.__init__)


def test_dbevolution_addcolumnchange_constructor_args():
    sig = inspect.signature(dbevolution_AddColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_column_is_not_abstract():
    assert not inspect.isabstract(dbevolution_Column)


def test_dbevolution_column_constructor_exists():
    assert callable(dbevolution_Column.__init__)


def test_dbevolution_column_constructor_args():
    sig = inspect.signature(dbevolution_Column.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution_removeforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution_RemoveForeignKey)


def test_dbevolution_removeforeignkey_constructor_exists():
    assert callable(dbevolution_RemoveForeignKey.__init__)


def test_dbevolution_removeforeignkey_constructor_args():
    sig = inspect.signature(dbevolution_RemoveForeignKey.__init__)
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
dbevolution_EObject_strategy = st.builds(
    dbevolution_EObject,
)
Diff_strategy = st.builds(
    Diff,
)
dbevolution_DBDiff_strategy = st.builds(
    dbevolution_DBDiff,
)
SchemaChange_strategy = st.builds(
    SchemaChange,
)
dbevolution_RemoveSchema_strategy = st.builds(
    dbevolution_RemoveSchema,
)
dbevolution_UpdateSchemaCommentChange_strategy = st.builds(
    dbevolution_UpdateSchemaCommentChange,
)
dbevolution_AlterSchema_strategy = st.builds(
    dbevolution_AlterSchema,
)
dbevolution_RenameSchemaChange_strategy = st.builds(
    dbevolution_RenameSchemaChange,
)
dbevolution_AddSchema_strategy = st.builds(
    dbevolution_AddSchema,
)
dbevolution_Schema_strategy = st.builds(
    dbevolution_Schema,
)
SequenceChange_strategy = st.builds(
    SequenceChange,
)
dbevolution_RemoveSequence_strategy = st.builds(
    dbevolution_RemoveSequence,
)
dbevolution_UpdateSequence_strategy = st.builds(
    dbevolution_UpdateSequence,
)
dbevolution_AddSequence_strategy = st.builds(
    dbevolution_AddSequence,
)
dbevolution_Sequence_strategy = st.builds(
    dbevolution_Sequence,
)
ForeignKeyChange_strategy = st.builds(
    ForeignKeyChange,
)
dbevolution_UpdateForeignKey_strategy = st.builds(
    dbevolution_UpdateForeignKey,
)
dbevolution_AddForeignKey_strategy = st.builds(
    dbevolution_AddForeignKey,
)
dbevolution_ForeignKey_strategy = st.builds(
    dbevolution_ForeignKey,
)
IndexChange_strategy = st.builds(
    IndexChange,
)
dbevolution_UpdateIndex_strategy = st.builds(
    dbevolution_UpdateIndex,
)
dbevolution_RemoveIndex_strategy = st.builds(
    dbevolution_RemoveIndex,
)
dbevolution_AddIndex_strategy = st.builds(
    dbevolution_AddIndex,
)
dbevolution_Index_strategy = st.builds(
    dbevolution_Index,
)
PrimaryKeyChange_strategy = st.builds(
    PrimaryKeyChange,
)
dbevolution_RemovePrimaryKey_strategy = st.builds(
    dbevolution_RemovePrimaryKey,
)
dbevolution_UpdatePrimaryKey_strategy = st.builds(
    dbevolution_UpdatePrimaryKey,
)
dbevolution_AddPrimaryKey_strategy = st.builds(
    dbevolution_AddPrimaryKey,
)
dbevolution_PrimaryKey_strategy = st.builds(
    dbevolution_PrimaryKey,
)
ConstraintChange_strategy = st.builds(
    ConstraintChange,
)
dbevolution_UpdateConstraint_strategy = st.builds(
    dbevolution_UpdateConstraint,
)
dbevolution_RemoveConstraint_strategy = st.builds(
    dbevolution_RemoveConstraint,
)
dbevolution_AddConstraint_strategy = st.builds(
    dbevolution_AddConstraint,
)
dbevolution_Constraint_strategy = st.builds(
    dbevolution_Constraint,
)
TableChange_strategy = st.builds(
    TableChange,
)
dbevolution_RemoveTable_strategy = st.builds(
    dbevolution_RemoveTable,
)
dbevolution_RenameTableChange_strategy = st.builds(
    dbevolution_RenameTableChange,
)
dbevolution_UpdateTableCommentChange_strategy = st.builds(
    dbevolution_UpdateTableCommentChange,
)
dbevolution_AlterTable_strategy = st.builds(
    dbevolution_AlterTable,
)
dbevolution_AddTable_strategy = st.builds(
    dbevolution_AddTable,
)
dbevolution_Table_strategy = st.builds(
    dbevolution_Table,
)
DBDiff_strategy = st.builds(
    DBDiff,
)
dbevolution_SequenceChange_strategy = st.builds(
    dbevolution_SequenceChange,
)
dbevolution_ConstraintChange_strategy = st.builds(
    dbevolution_ConstraintChange,
)
dbevolution_ForeignKeyChange_strategy = st.builds(
    dbevolution_ForeignKeyChange,
)
dbevolution_IndexChange_strategy = st.builds(
    dbevolution_IndexChange,
)
dbevolution_SchemaChange_strategy = st.builds(
    dbevolution_SchemaChange,
)
dbevolution_PrimaryKeyChange_strategy = st.builds(
    dbevolution_PrimaryKeyChange,
)
dbevolution_ColumnChange_strategy = st.builds(
    dbevolution_ColumnChange,
)
dbevolution_TableChange_strategy = st.builds(
    dbevolution_TableChange,
)
Comparison_strategy = st.builds(
    Comparison,
)
dbevolution_DatabaseChangeSet_strategy = st.builds(
    dbevolution_DatabaseChangeSet,
)
ColumnChange_strategy = st.builds(
    ColumnChange,
)
dbevolution_UpdateColumnChange_strategy = st.builds(
    dbevolution_UpdateColumnChange,
)
dbevolution_RemoveColumnChange_strategy = st.builds(
    dbevolution_RemoveColumnChange,
)
dbevolution_UpdateColumnCommentChange_strategy = st.builds(
    dbevolution_UpdateColumnCommentChange,
)
dbevolution_RenameColumnChange_strategy = st.builds(
    dbevolution_RenameColumnChange,
)
dbevolution_AddColumnChange_strategy = st.builds(
    dbevolution_AddColumnChange,
)
dbevolution_Column_strategy = st.builds(
    dbevolution_Column,
)
dbevolution_RemoveForeignKey_strategy = st.builds(
    dbevolution_RemoveForeignKey,
)

@given(instance=dbevolution_EObject_strategy)
@settings(max_examples=50)
def test_dbevolution_eobject_instantiation(instance):
    assert isinstance(instance, dbevolution_EObject)

@given(instance=Diff_strategy)
@settings(max_examples=50)
def test_diff_instantiation(instance):
    assert isinstance(instance, Diff)

@given(instance=dbevolution_DBDiff_strategy)
@settings(max_examples=50)
def test_dbevolution_dbdiff_instantiation(instance):
    assert isinstance(instance, dbevolution_DBDiff)

@given(instance=SchemaChange_strategy)
@settings(max_examples=50)
def test_schemachange_instantiation(instance):
    assert isinstance(instance, SchemaChange)

@given(instance=dbevolution_RemoveSchema_strategy)
@settings(max_examples=50)
def test_dbevolution_removeschema_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveSchema)

@given(instance=dbevolution_UpdateSchemaCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution_updateschemacommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateSchemaCommentChange)

@given(instance=dbevolution_AlterSchema_strategy)
@settings(max_examples=50)
def test_dbevolution_alterschema_instantiation(instance):
    assert isinstance(instance, dbevolution_AlterSchema)

@given(instance=dbevolution_RenameSchemaChange_strategy)
@settings(max_examples=50)
def test_dbevolution_renameschemachange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameSchemaChange)

@given(instance=dbevolution_AddSchema_strategy)
@settings(max_examples=50)
def test_dbevolution_addschema_instantiation(instance):
    assert isinstance(instance, dbevolution_AddSchema)

@given(instance=dbevolution_Schema_strategy)
@settings(max_examples=50)
def test_dbevolution_schema_instantiation(instance):
    assert isinstance(instance, dbevolution_Schema)

@given(instance=SequenceChange_strategy)
@settings(max_examples=50)
def test_sequencechange_instantiation(instance):
    assert isinstance(instance, SequenceChange)

@given(instance=dbevolution_RemoveSequence_strategy)
@settings(max_examples=50)
def test_dbevolution_removesequence_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveSequence)

@given(instance=dbevolution_UpdateSequence_strategy)
@settings(max_examples=50)
def test_dbevolution_updatesequence_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateSequence)

@given(instance=dbevolution_AddSequence_strategy)
@settings(max_examples=50)
def test_dbevolution_addsequence_instantiation(instance):
    assert isinstance(instance, dbevolution_AddSequence)

@given(instance=dbevolution_Sequence_strategy)
@settings(max_examples=50)
def test_dbevolution_sequence_instantiation(instance):
    assert isinstance(instance, dbevolution_Sequence)

@given(instance=ForeignKeyChange_strategy)
@settings(max_examples=50)
def test_foreignkeychange_instantiation(instance):
    assert isinstance(instance, ForeignKeyChange)

@given(instance=dbevolution_UpdateForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution_updateforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateForeignKey)

@given(instance=dbevolution_AddForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution_addforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution_AddForeignKey)

@given(instance=dbevolution_ForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution_foreignkey_instantiation(instance):
    assert isinstance(instance, dbevolution_ForeignKey)

@given(instance=IndexChange_strategy)
@settings(max_examples=50)
def test_indexchange_instantiation(instance):
    assert isinstance(instance, IndexChange)

@given(instance=dbevolution_UpdateIndex_strategy)
@settings(max_examples=50)
def test_dbevolution_updateindex_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateIndex)

@given(instance=dbevolution_RemoveIndex_strategy)
@settings(max_examples=50)
def test_dbevolution_removeindex_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveIndex)

@given(instance=dbevolution_AddIndex_strategy)
@settings(max_examples=50)
def test_dbevolution_addindex_instantiation(instance):
    assert isinstance(instance, dbevolution_AddIndex)

@given(instance=dbevolution_Index_strategy)
@settings(max_examples=50)
def test_dbevolution_index_instantiation(instance):
    assert isinstance(instance, dbevolution_Index)

@given(instance=PrimaryKeyChange_strategy)
@settings(max_examples=50)
def test_primarykeychange_instantiation(instance):
    assert isinstance(instance, PrimaryKeyChange)

@given(instance=dbevolution_RemovePrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution_removeprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution_RemovePrimaryKey)

@given(instance=dbevolution_UpdatePrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution_updateprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdatePrimaryKey)

@given(instance=dbevolution_AddPrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution_addprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution_AddPrimaryKey)

@given(instance=dbevolution_PrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution_primarykey_instantiation(instance):
    assert isinstance(instance, dbevolution_PrimaryKey)

@given(instance=ConstraintChange_strategy)
@settings(max_examples=50)
def test_constraintchange_instantiation(instance):
    assert isinstance(instance, ConstraintChange)

@given(instance=dbevolution_UpdateConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution_updateconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateConstraint)

@given(instance=dbevolution_RemoveConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution_removeconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveConstraint)

@given(instance=dbevolution_AddConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution_addconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution_AddConstraint)

@given(instance=dbevolution_Constraint_strategy)
@settings(max_examples=50)
def test_dbevolution_constraint_instantiation(instance):
    assert isinstance(instance, dbevolution_Constraint)

@given(instance=TableChange_strategy)
@settings(max_examples=50)
def test_tablechange_instantiation(instance):
    assert isinstance(instance, TableChange)

@given(instance=dbevolution_RemoveTable_strategy)
@settings(max_examples=50)
def test_dbevolution_removetable_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveTable)

@given(instance=dbevolution_RenameTableChange_strategy)
@settings(max_examples=50)
def test_dbevolution_renametablechange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameTableChange)

@given(instance=dbevolution_UpdateTableCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution_updatetablecommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateTableCommentChange)

@given(instance=dbevolution_AlterTable_strategy)
@settings(max_examples=50)
def test_dbevolution_altertable_instantiation(instance):
    assert isinstance(instance, dbevolution_AlterTable)

@given(instance=dbevolution_AddTable_strategy)
@settings(max_examples=50)
def test_dbevolution_addtable_instantiation(instance):
    assert isinstance(instance, dbevolution_AddTable)

@given(instance=dbevolution_Table_strategy)
@settings(max_examples=50)
def test_dbevolution_table_instantiation(instance):
    assert isinstance(instance, dbevolution_Table)

@given(instance=DBDiff_strategy)
@settings(max_examples=50)
def test_dbdiff_instantiation(instance):
    assert isinstance(instance, DBDiff)

@given(instance=dbevolution_SequenceChange_strategy)
@settings(max_examples=50)
def test_dbevolution_sequencechange_instantiation(instance):
    assert isinstance(instance, dbevolution_SequenceChange)

@given(instance=dbevolution_ConstraintChange_strategy)
@settings(max_examples=50)
def test_dbevolution_constraintchange_instantiation(instance):
    assert isinstance(instance, dbevolution_ConstraintChange)

@given(instance=dbevolution_ForeignKeyChange_strategy)
@settings(max_examples=50)
def test_dbevolution_foreignkeychange_instantiation(instance):
    assert isinstance(instance, dbevolution_ForeignKeyChange)

@given(instance=dbevolution_IndexChange_strategy)
@settings(max_examples=50)
def test_dbevolution_indexchange_instantiation(instance):
    assert isinstance(instance, dbevolution_IndexChange)

@given(instance=dbevolution_SchemaChange_strategy)
@settings(max_examples=50)
def test_dbevolution_schemachange_instantiation(instance):
    assert isinstance(instance, dbevolution_SchemaChange)

@given(instance=dbevolution_PrimaryKeyChange_strategy)
@settings(max_examples=50)
def test_dbevolution_primarykeychange_instantiation(instance):
    assert isinstance(instance, dbevolution_PrimaryKeyChange)

@given(instance=dbevolution_ColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution_columnchange_instantiation(instance):
    assert isinstance(instance, dbevolution_ColumnChange)

@given(instance=dbevolution_TableChange_strategy)
@settings(max_examples=50)
def test_dbevolution_tablechange_instantiation(instance):
    assert isinstance(instance, dbevolution_TableChange)

@given(instance=Comparison_strategy)
@settings(max_examples=50)
def test_comparison_instantiation(instance):
    assert isinstance(instance, Comparison)

@given(instance=dbevolution_DatabaseChangeSet_strategy)
@settings(max_examples=50)
def test_dbevolution_databasechangeset_instantiation(instance):
    assert isinstance(instance, dbevolution_DatabaseChangeSet)

@given(instance=ColumnChange_strategy)
@settings(max_examples=50)
def test_columnchange_instantiation(instance):
    assert isinstance(instance, ColumnChange)

@given(instance=dbevolution_UpdateColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution_updatecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateColumnChange)

@given(instance=dbevolution_RemoveColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution_removecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveColumnChange)

@given(instance=dbevolution_UpdateColumnCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution_updatecolumncommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution_UpdateColumnCommentChange)

@given(instance=dbevolution_RenameColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution_renamecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution_RenameColumnChange)

@given(instance=dbevolution_AddColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution_addcolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution_AddColumnChange)

@given(instance=dbevolution_Column_strategy)
@settings(max_examples=50)
def test_dbevolution_column_instantiation(instance):
    assert isinstance(instance, dbevolution_Column)

@given(instance=dbevolution_RemoveForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution_removeforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution_RemoveForeignKey)
