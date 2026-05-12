import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PrimaryKeyChange,
    dbevolution::RemovePrimaryKey,
    dbevolution::AddPrimaryKey,
    dbevolution::PrimaryKey,
    ConstraintChange,
    dbevolution::RemoveConstraint,
    dbevolution::UpdateConstraint,
    dbevolution::AddConstraint,
    dbevolution::Constraint,
    TableChange,
    dbevolution::RemoveTable,
    dbevolution::RenameTableChange,
    dbevolution::UpdateTableCommentChange,
    dbevolution::AlterTable,
    dbevolution::AddTable,
    dbevolution::Table,
    DBDiff,
    dbevolution::PrimaryKeyChange,
    dbevolution::ConstraintChange,
    dbevolution::ColumnChange,
    dbevolution::TableChange,
    Comparison,
    dbevolution::DatabaseChangeSet,
    ColumnChange,
    dbevolution::UpdateColumnChange,
    dbevolution::RemoveColumnChange,
    dbevolution::UpdateColumnCommentChange,
    dbevolution::RenameColumnChange,
    dbevolution::AddColumnChange,
    dbevolution::Column,
    dbevolution::EObject,
    Diff,
    dbevolution::DBDiff,
    SchemaChange,
    dbevolution::RemoveSchema,
    dbevolution::AlterSchema,
    dbevolution::UpdateSchemaCommentChange,
    dbevolution::RenameSchemaChange,
    dbevolution::AddSchema,
    dbevolution::Schema,
    dbevolution::SchemaChange,
    SequenceChange,
    dbevolution::RemoveSequence,
    dbevolution::UpdateSequence,
    dbevolution::AddSequence,
    dbevolution::Sequence,
    dbevolution::SequenceChange,
    ForeignKeyChange,
    dbevolution::UpdateForeignKey,
    dbevolution::RemoveForeignKey,
    dbevolution::AddForeignKey,
    dbevolution::ForeignKey,
    dbevolution::ForeignKeyChange,
    IndexChange,
    dbevolution::UpdateIndex,
    dbevolution::RemoveIndex,
    dbevolution::AddIndex,
    dbevolution::Index,
    dbevolution::IndexChange,
    dbevolution::UpdatePrimaryKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primarykeychange_is_not_abstract():
    assert not inspect.isabstract(PrimaryKeyChange)


def test_primarykeychange_constructor_exists():
    assert callable(PrimaryKeyChange.__init__)


def test_primarykeychange_constructor_args():
    sig = inspect.signature(PrimaryKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removeprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemovePrimaryKey)


def test_dbevolution::removeprimarykey_constructor_exists():
    assert callable(dbevolution::RemovePrimaryKey.__init__)


def test_dbevolution::removeprimarykey_constructor_args():
    sig = inspect.signature(dbevolution::RemovePrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddPrimaryKey)


def test_dbevolution::addprimarykey_constructor_exists():
    assert callable(dbevolution::AddPrimaryKey.__init__)


def test_dbevolution::addprimarykey_constructor_args():
    sig = inspect.signature(dbevolution::AddPrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::primarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::PrimaryKey)


def test_dbevolution::primarykey_constructor_exists():
    assert callable(dbevolution::PrimaryKey.__init__)


def test_dbevolution::primarykey_constructor_args():
    sig = inspect.signature(dbevolution::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_constraintchange_is_not_abstract():
    assert not inspect.isabstract(ConstraintChange)


def test_constraintchange_constructor_exists():
    assert callable(ConstraintChange.__init__)


def test_constraintchange_constructor_args():
    sig = inspect.signature(ConstraintChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removeconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveConstraint)


def test_dbevolution::removeconstraint_constructor_exists():
    assert callable(dbevolution::RemoveConstraint.__init__)


def test_dbevolution::removeconstraint_constructor_args():
    sig = inspect.signature(dbevolution::RemoveConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updateconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateConstraint)


def test_dbevolution::updateconstraint_constructor_exists():
    assert callable(dbevolution::UpdateConstraint.__init__)


def test_dbevolution::updateconstraint_constructor_args():
    sig = inspect.signature(dbevolution::UpdateConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addconstraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddConstraint)


def test_dbevolution::addconstraint_constructor_exists():
    assert callable(dbevolution::AddConstraint.__init__)


def test_dbevolution::addconstraint_constructor_args():
    sig = inspect.signature(dbevolution::AddConstraint.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::constraint_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Constraint)


def test_dbevolution::constraint_constructor_exists():
    assert callable(dbevolution::Constraint.__init__)


def test_dbevolution::constraint_constructor_args():
    sig = inspect.signature(dbevolution::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_tablechange_is_not_abstract():
    assert not inspect.isabstract(TableChange)


def test_tablechange_constructor_exists():
    assert callable(TableChange.__init__)


def test_tablechange_constructor_args():
    sig = inspect.signature(TableChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removetable_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveTable)


def test_dbevolution::removetable_constructor_exists():
    assert callable(dbevolution::RemoveTable.__init__)


def test_dbevolution::removetable_constructor_args():
    sig = inspect.signature(dbevolution::RemoveTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::renametablechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RenameTableChange)


def test_dbevolution::renametablechange_constructor_exists():
    assert callable(dbevolution::RenameTableChange.__init__)


def test_dbevolution::renametablechange_constructor_args():
    sig = inspect.signature(dbevolution::RenameTableChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updatetablecommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateTableCommentChange)


def test_dbevolution::updatetablecommentchange_constructor_exists():
    assert callable(dbevolution::UpdateTableCommentChange.__init__)


def test_dbevolution::updatetablecommentchange_constructor_args():
    sig = inspect.signature(dbevolution::UpdateTableCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::altertable_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AlterTable)


def test_dbevolution::altertable_constructor_exists():
    assert callable(dbevolution::AlterTable.__init__)


def test_dbevolution::altertable_constructor_args():
    sig = inspect.signature(dbevolution::AlterTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addtable_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddTable)


def test_dbevolution::addtable_constructor_exists():
    assert callable(dbevolution::AddTable.__init__)


def test_dbevolution::addtable_constructor_args():
    sig = inspect.signature(dbevolution::AddTable.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::table_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Table)


def test_dbevolution::table_constructor_exists():
    assert callable(dbevolution::Table.__init__)


def test_dbevolution::table_constructor_args():
    sig = inspect.signature(dbevolution::Table.__init__)
    params = list(sig.parameters.keys())



def test_dbdiff_is_not_abstract():
    assert not inspect.isabstract(DBDiff)


def test_dbdiff_constructor_exists():
    assert callable(DBDiff.__init__)


def test_dbdiff_constructor_args():
    sig = inspect.signature(DBDiff.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::primarykeychange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::PrimaryKeyChange)


def test_dbevolution::primarykeychange_constructor_exists():
    assert callable(dbevolution::PrimaryKeyChange.__init__)


def test_dbevolution::primarykeychange_constructor_args():
    sig = inspect.signature(dbevolution::PrimaryKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::constraintchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::ConstraintChange)


def test_dbevolution::constraintchange_constructor_exists():
    assert callable(dbevolution::ConstraintChange.__init__)


def test_dbevolution::constraintchange_constructor_args():
    sig = inspect.signature(dbevolution::ConstraintChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::columnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::ColumnChange)


def test_dbevolution::columnchange_constructor_exists():
    assert callable(dbevolution::ColumnChange.__init__)


def test_dbevolution::columnchange_constructor_args():
    sig = inspect.signature(dbevolution::ColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::tablechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::TableChange)


def test_dbevolution::tablechange_constructor_exists():
    assert callable(dbevolution::TableChange.__init__)


def test_dbevolution::tablechange_constructor_args():
    sig = inspect.signature(dbevolution::TableChange.__init__)
    params = list(sig.parameters.keys())



def test_comparison_is_not_abstract():
    assert not inspect.isabstract(Comparison)


def test_comparison_constructor_exists():
    assert callable(Comparison.__init__)


def test_comparison_constructor_args():
    sig = inspect.signature(Comparison.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::databasechangeset_is_not_abstract():
    assert not inspect.isabstract(dbevolution::DatabaseChangeSet)


def test_dbevolution::databasechangeset_constructor_exists():
    assert callable(dbevolution::DatabaseChangeSet.__init__)


def test_dbevolution::databasechangeset_constructor_args():
    sig = inspect.signature(dbevolution::DatabaseChangeSet.__init__)
    params = list(sig.parameters.keys())



def test_columnchange_is_not_abstract():
    assert not inspect.isabstract(ColumnChange)


def test_columnchange_constructor_exists():
    assert callable(ColumnChange.__init__)


def test_columnchange_constructor_args():
    sig = inspect.signature(ColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updatecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateColumnChange)


def test_dbevolution::updatecolumnchange_constructor_exists():
    assert callable(dbevolution::UpdateColumnChange.__init__)


def test_dbevolution::updatecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution::UpdateColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveColumnChange)


def test_dbevolution::removecolumnchange_constructor_exists():
    assert callable(dbevolution::RemoveColumnChange.__init__)


def test_dbevolution::removecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution::RemoveColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updatecolumncommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateColumnCommentChange)


def test_dbevolution::updatecolumncommentchange_constructor_exists():
    assert callable(dbevolution::UpdateColumnCommentChange.__init__)


def test_dbevolution::updatecolumncommentchange_constructor_args():
    sig = inspect.signature(dbevolution::UpdateColumnCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::renamecolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RenameColumnChange)


def test_dbevolution::renamecolumnchange_constructor_exists():
    assert callable(dbevolution::RenameColumnChange.__init__)


def test_dbevolution::renamecolumnchange_constructor_args():
    sig = inspect.signature(dbevolution::RenameColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addcolumnchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddColumnChange)


def test_dbevolution::addcolumnchange_constructor_exists():
    assert callable(dbevolution::AddColumnChange.__init__)


def test_dbevolution::addcolumnchange_constructor_args():
    sig = inspect.signature(dbevolution::AddColumnChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::column_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Column)


def test_dbevolution::column_constructor_exists():
    assert callable(dbevolution::Column.__init__)


def test_dbevolution::column_constructor_args():
    sig = inspect.signature(dbevolution::Column.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::eobject_is_not_abstract():
    assert not inspect.isabstract(dbevolution::EObject)


def test_dbevolution::eobject_constructor_exists():
    assert callable(dbevolution::EObject.__init__)


def test_dbevolution::eobject_constructor_args():
    sig = inspect.signature(dbevolution::EObject.__init__)
    params = list(sig.parameters.keys())



def test_diff_is_not_abstract():
    assert not inspect.isabstract(Diff)


def test_diff_constructor_exists():
    assert callable(Diff.__init__)


def test_diff_constructor_args():
    sig = inspect.signature(Diff.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::dbdiff_is_not_abstract():
    assert not inspect.isabstract(dbevolution::DBDiff)


def test_dbevolution::dbdiff_constructor_exists():
    assert callable(dbevolution::DBDiff.__init__)


def test_dbevolution::dbdiff_constructor_args():
    sig = inspect.signature(dbevolution::DBDiff.__init__)
    params = list(sig.parameters.keys())



def test_schemachange_is_not_abstract():
    assert not inspect.isabstract(SchemaChange)


def test_schemachange_constructor_exists():
    assert callable(SchemaChange.__init__)


def test_schemachange_constructor_args():
    sig = inspect.signature(SchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removeschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveSchema)


def test_dbevolution::removeschema_constructor_exists():
    assert callable(dbevolution::RemoveSchema.__init__)


def test_dbevolution::removeschema_constructor_args():
    sig = inspect.signature(dbevolution::RemoveSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::alterschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AlterSchema)


def test_dbevolution::alterschema_constructor_exists():
    assert callable(dbevolution::AlterSchema.__init__)


def test_dbevolution::alterschema_constructor_args():
    sig = inspect.signature(dbevolution::AlterSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updateschemacommentchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateSchemaCommentChange)


def test_dbevolution::updateschemacommentchange_constructor_exists():
    assert callable(dbevolution::UpdateSchemaCommentChange.__init__)


def test_dbevolution::updateschemacommentchange_constructor_args():
    sig = inspect.signature(dbevolution::UpdateSchemaCommentChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::renameschemachange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RenameSchemaChange)


def test_dbevolution::renameschemachange_constructor_exists():
    assert callable(dbevolution::RenameSchemaChange.__init__)


def test_dbevolution::renameschemachange_constructor_args():
    sig = inspect.signature(dbevolution::RenameSchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addschema_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddSchema)


def test_dbevolution::addschema_constructor_exists():
    assert callable(dbevolution::AddSchema.__init__)


def test_dbevolution::addschema_constructor_args():
    sig = inspect.signature(dbevolution::AddSchema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::schema_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Schema)


def test_dbevolution::schema_constructor_exists():
    assert callable(dbevolution::Schema.__init__)


def test_dbevolution::schema_constructor_args():
    sig = inspect.signature(dbevolution::Schema.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::schemachange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::SchemaChange)


def test_dbevolution::schemachange_constructor_exists():
    assert callable(dbevolution::SchemaChange.__init__)


def test_dbevolution::schemachange_constructor_args():
    sig = inspect.signature(dbevolution::SchemaChange.__init__)
    params = list(sig.parameters.keys())



def test_sequencechange_is_not_abstract():
    assert not inspect.isabstract(SequenceChange)


def test_sequencechange_constructor_exists():
    assert callable(SequenceChange.__init__)


def test_sequencechange_constructor_args():
    sig = inspect.signature(SequenceChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removesequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveSequence)


def test_dbevolution::removesequence_constructor_exists():
    assert callable(dbevolution::RemoveSequence.__init__)


def test_dbevolution::removesequence_constructor_args():
    sig = inspect.signature(dbevolution::RemoveSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updatesequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateSequence)


def test_dbevolution::updatesequence_constructor_exists():
    assert callable(dbevolution::UpdateSequence.__init__)


def test_dbevolution::updatesequence_constructor_args():
    sig = inspect.signature(dbevolution::UpdateSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addsequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddSequence)


def test_dbevolution::addsequence_constructor_exists():
    assert callable(dbevolution::AddSequence.__init__)


def test_dbevolution::addsequence_constructor_args():
    sig = inspect.signature(dbevolution::AddSequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::sequence_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Sequence)


def test_dbevolution::sequence_constructor_exists():
    assert callable(dbevolution::Sequence.__init__)


def test_dbevolution::sequence_constructor_args():
    sig = inspect.signature(dbevolution::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::sequencechange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::SequenceChange)


def test_dbevolution::sequencechange_constructor_exists():
    assert callable(dbevolution::SequenceChange.__init__)


def test_dbevolution::sequencechange_constructor_args():
    sig = inspect.signature(dbevolution::SequenceChange.__init__)
    params = list(sig.parameters.keys())



def test_foreignkeychange_is_not_abstract():
    assert not inspect.isabstract(ForeignKeyChange)


def test_foreignkeychange_constructor_exists():
    assert callable(ForeignKeyChange.__init__)


def test_foreignkeychange_constructor_args():
    sig = inspect.signature(ForeignKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updateforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateForeignKey)


def test_dbevolution::updateforeignkey_constructor_exists():
    assert callable(dbevolution::UpdateForeignKey.__init__)


def test_dbevolution::updateforeignkey_constructor_args():
    sig = inspect.signature(dbevolution::UpdateForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removeforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveForeignKey)


def test_dbevolution::removeforeignkey_constructor_exists():
    assert callable(dbevolution::RemoveForeignKey.__init__)


def test_dbevolution::removeforeignkey_constructor_args():
    sig = inspect.signature(dbevolution::RemoveForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addforeignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddForeignKey)


def test_dbevolution::addforeignkey_constructor_exists():
    assert callable(dbevolution::AddForeignKey.__init__)


def test_dbevolution::addforeignkey_constructor_args():
    sig = inspect.signature(dbevolution::AddForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::foreignkey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::ForeignKey)


def test_dbevolution::foreignkey_constructor_exists():
    assert callable(dbevolution::ForeignKey.__init__)


def test_dbevolution::foreignkey_constructor_args():
    sig = inspect.signature(dbevolution::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::foreignkeychange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::ForeignKeyChange)


def test_dbevolution::foreignkeychange_constructor_exists():
    assert callable(dbevolution::ForeignKeyChange.__init__)


def test_dbevolution::foreignkeychange_constructor_args():
    sig = inspect.signature(dbevolution::ForeignKeyChange.__init__)
    params = list(sig.parameters.keys())



def test_indexchange_is_not_abstract():
    assert not inspect.isabstract(IndexChange)


def test_indexchange_constructor_exists():
    assert callable(IndexChange.__init__)


def test_indexchange_constructor_args():
    sig = inspect.signature(IndexChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updateindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdateIndex)


def test_dbevolution::updateindex_constructor_exists():
    assert callable(dbevolution::UpdateIndex.__init__)


def test_dbevolution::updateindex_constructor_args():
    sig = inspect.signature(dbevolution::UpdateIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::removeindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution::RemoveIndex)


def test_dbevolution::removeindex_constructor_exists():
    assert callable(dbevolution::RemoveIndex.__init__)


def test_dbevolution::removeindex_constructor_args():
    sig = inspect.signature(dbevolution::RemoveIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::addindex_is_not_abstract():
    assert not inspect.isabstract(dbevolution::AddIndex)


def test_dbevolution::addindex_constructor_exists():
    assert callable(dbevolution::AddIndex.__init__)


def test_dbevolution::addindex_constructor_args():
    sig = inspect.signature(dbevolution::AddIndex.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::index_is_not_abstract():
    assert not inspect.isabstract(dbevolution::Index)


def test_dbevolution::index_constructor_exists():
    assert callable(dbevolution::Index.__init__)


def test_dbevolution::index_constructor_args():
    sig = inspect.signature(dbevolution::Index.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::indexchange_is_not_abstract():
    assert not inspect.isabstract(dbevolution::IndexChange)


def test_dbevolution::indexchange_constructor_exists():
    assert callable(dbevolution::IndexChange.__init__)


def test_dbevolution::indexchange_constructor_args():
    sig = inspect.signature(dbevolution::IndexChange.__init__)
    params = list(sig.parameters.keys())



def test_dbevolution::updateprimarykey_is_not_abstract():
    assert not inspect.isabstract(dbevolution::UpdatePrimaryKey)


def test_dbevolution::updateprimarykey_constructor_exists():
    assert callable(dbevolution::UpdatePrimaryKey.__init__)


def test_dbevolution::updateprimarykey_constructor_args():
    sig = inspect.signature(dbevolution::UpdatePrimaryKey.__init__)
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
PrimaryKeyChange_strategy = st.builds(
    PrimaryKeyChange,
)
dbevolution::RemovePrimaryKey_strategy = st.builds(
    dbevolution::RemovePrimaryKey,
)
dbevolution::AddPrimaryKey_strategy = st.builds(
    dbevolution::AddPrimaryKey,
)
dbevolution::PrimaryKey_strategy = st.builds(
    dbevolution::PrimaryKey,
)
ConstraintChange_strategy = st.builds(
    ConstraintChange,
)
dbevolution::RemoveConstraint_strategy = st.builds(
    dbevolution::RemoveConstraint,
)
dbevolution::UpdateConstraint_strategy = st.builds(
    dbevolution::UpdateConstraint,
)
dbevolution::AddConstraint_strategy = st.builds(
    dbevolution::AddConstraint,
)
dbevolution::Constraint_strategy = st.builds(
    dbevolution::Constraint,
)
TableChange_strategy = st.builds(
    TableChange,
)
dbevolution::RemoveTable_strategy = st.builds(
    dbevolution::RemoveTable,
)
dbevolution::RenameTableChange_strategy = st.builds(
    dbevolution::RenameTableChange,
)
dbevolution::UpdateTableCommentChange_strategy = st.builds(
    dbevolution::UpdateTableCommentChange,
)
dbevolution::AlterTable_strategy = st.builds(
    dbevolution::AlterTable,
)
dbevolution::AddTable_strategy = st.builds(
    dbevolution::AddTable,
)
dbevolution::Table_strategy = st.builds(
    dbevolution::Table,
)
DBDiff_strategy = st.builds(
    DBDiff,
)
dbevolution::PrimaryKeyChange_strategy = st.builds(
    dbevolution::PrimaryKeyChange,
)
dbevolution::ConstraintChange_strategy = st.builds(
    dbevolution::ConstraintChange,
)
dbevolution::ColumnChange_strategy = st.builds(
    dbevolution::ColumnChange,
)
dbevolution::TableChange_strategy = st.builds(
    dbevolution::TableChange,
)
Comparison_strategy = st.builds(
    Comparison,
)
dbevolution::DatabaseChangeSet_strategy = st.builds(
    dbevolution::DatabaseChangeSet,
)
ColumnChange_strategy = st.builds(
    ColumnChange,
)
dbevolution::UpdateColumnChange_strategy = st.builds(
    dbevolution::UpdateColumnChange,
)
dbevolution::RemoveColumnChange_strategy = st.builds(
    dbevolution::RemoveColumnChange,
)
dbevolution::UpdateColumnCommentChange_strategy = st.builds(
    dbevolution::UpdateColumnCommentChange,
)
dbevolution::RenameColumnChange_strategy = st.builds(
    dbevolution::RenameColumnChange,
)
dbevolution::AddColumnChange_strategy = st.builds(
    dbevolution::AddColumnChange,
)
dbevolution::Column_strategy = st.builds(
    dbevolution::Column,
)
dbevolution::EObject_strategy = st.builds(
    dbevolution::EObject,
)
Diff_strategy = st.builds(
    Diff,
)
dbevolution::DBDiff_strategy = st.builds(
    dbevolution::DBDiff,
)
SchemaChange_strategy = st.builds(
    SchemaChange,
)
dbevolution::RemoveSchema_strategy = st.builds(
    dbevolution::RemoveSchema,
)
dbevolution::AlterSchema_strategy = st.builds(
    dbevolution::AlterSchema,
)
dbevolution::UpdateSchemaCommentChange_strategy = st.builds(
    dbevolution::UpdateSchemaCommentChange,
)
dbevolution::RenameSchemaChange_strategy = st.builds(
    dbevolution::RenameSchemaChange,
)
dbevolution::AddSchema_strategy = st.builds(
    dbevolution::AddSchema,
)
dbevolution::Schema_strategy = st.builds(
    dbevolution::Schema,
)
dbevolution::SchemaChange_strategy = st.builds(
    dbevolution::SchemaChange,
)
SequenceChange_strategy = st.builds(
    SequenceChange,
)
dbevolution::RemoveSequence_strategy = st.builds(
    dbevolution::RemoveSequence,
)
dbevolution::UpdateSequence_strategy = st.builds(
    dbevolution::UpdateSequence,
)
dbevolution::AddSequence_strategy = st.builds(
    dbevolution::AddSequence,
)
dbevolution::Sequence_strategy = st.builds(
    dbevolution::Sequence,
)
dbevolution::SequenceChange_strategy = st.builds(
    dbevolution::SequenceChange,
)
ForeignKeyChange_strategy = st.builds(
    ForeignKeyChange,
)
dbevolution::UpdateForeignKey_strategy = st.builds(
    dbevolution::UpdateForeignKey,
)
dbevolution::RemoveForeignKey_strategy = st.builds(
    dbevolution::RemoveForeignKey,
)
dbevolution::AddForeignKey_strategy = st.builds(
    dbevolution::AddForeignKey,
)
dbevolution::ForeignKey_strategy = st.builds(
    dbevolution::ForeignKey,
)
dbevolution::ForeignKeyChange_strategy = st.builds(
    dbevolution::ForeignKeyChange,
)
IndexChange_strategy = st.builds(
    IndexChange,
)
dbevolution::UpdateIndex_strategy = st.builds(
    dbevolution::UpdateIndex,
)
dbevolution::RemoveIndex_strategy = st.builds(
    dbevolution::RemoveIndex,
)
dbevolution::AddIndex_strategy = st.builds(
    dbevolution::AddIndex,
)
dbevolution::Index_strategy = st.builds(
    dbevolution::Index,
)
dbevolution::IndexChange_strategy = st.builds(
    dbevolution::IndexChange,
)
dbevolution::UpdatePrimaryKey_strategy = st.builds(
    dbevolution::UpdatePrimaryKey,
)

@given(instance=PrimaryKeyChange_strategy)
@settings(max_examples=50)
def test_primarykeychange_instantiation(instance):
    assert isinstance(instance, PrimaryKeyChange)

@given(instance=dbevolution::RemovePrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution::removeprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution::RemovePrimaryKey)

@given(instance=dbevolution::AddPrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution::addprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution::AddPrimaryKey)

@given(instance=dbevolution::PrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution::primarykey_instantiation(instance):
    assert isinstance(instance, dbevolution::PrimaryKey)

@given(instance=ConstraintChange_strategy)
@settings(max_examples=50)
def test_constraintchange_instantiation(instance):
    assert isinstance(instance, ConstraintChange)

@given(instance=dbevolution::RemoveConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution::removeconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveConstraint)

@given(instance=dbevolution::UpdateConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution::updateconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateConstraint)

@given(instance=dbevolution::AddConstraint_strategy)
@settings(max_examples=50)
def test_dbevolution::addconstraint_instantiation(instance):
    assert isinstance(instance, dbevolution::AddConstraint)

@given(instance=dbevolution::Constraint_strategy)
@settings(max_examples=50)
def test_dbevolution::constraint_instantiation(instance):
    assert isinstance(instance, dbevolution::Constraint)

@given(instance=TableChange_strategy)
@settings(max_examples=50)
def test_tablechange_instantiation(instance):
    assert isinstance(instance, TableChange)

@given(instance=dbevolution::RemoveTable_strategy)
@settings(max_examples=50)
def test_dbevolution::removetable_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveTable)

@given(instance=dbevolution::RenameTableChange_strategy)
@settings(max_examples=50)
def test_dbevolution::renametablechange_instantiation(instance):
    assert isinstance(instance, dbevolution::RenameTableChange)

@given(instance=dbevolution::UpdateTableCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution::updatetablecommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateTableCommentChange)

@given(instance=dbevolution::AlterTable_strategy)
@settings(max_examples=50)
def test_dbevolution::altertable_instantiation(instance):
    assert isinstance(instance, dbevolution::AlterTable)

@given(instance=dbevolution::AddTable_strategy)
@settings(max_examples=50)
def test_dbevolution::addtable_instantiation(instance):
    assert isinstance(instance, dbevolution::AddTable)

@given(instance=dbevolution::Table_strategy)
@settings(max_examples=50)
def test_dbevolution::table_instantiation(instance):
    assert isinstance(instance, dbevolution::Table)

@given(instance=DBDiff_strategy)
@settings(max_examples=50)
def test_dbdiff_instantiation(instance):
    assert isinstance(instance, DBDiff)

@given(instance=dbevolution::PrimaryKeyChange_strategy)
@settings(max_examples=50)
def test_dbevolution::primarykeychange_instantiation(instance):
    assert isinstance(instance, dbevolution::PrimaryKeyChange)

@given(instance=dbevolution::ConstraintChange_strategy)
@settings(max_examples=50)
def test_dbevolution::constraintchange_instantiation(instance):
    assert isinstance(instance, dbevolution::ConstraintChange)

@given(instance=dbevolution::ColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution::columnchange_instantiation(instance):
    assert isinstance(instance, dbevolution::ColumnChange)

@given(instance=dbevolution::TableChange_strategy)
@settings(max_examples=50)
def test_dbevolution::tablechange_instantiation(instance):
    assert isinstance(instance, dbevolution::TableChange)

@given(instance=Comparison_strategy)
@settings(max_examples=50)
def test_comparison_instantiation(instance):
    assert isinstance(instance, Comparison)

@given(instance=dbevolution::DatabaseChangeSet_strategy)
@settings(max_examples=50)
def test_dbevolution::databasechangeset_instantiation(instance):
    assert isinstance(instance, dbevolution::DatabaseChangeSet)

@given(instance=ColumnChange_strategy)
@settings(max_examples=50)
def test_columnchange_instantiation(instance):
    assert isinstance(instance, ColumnChange)

@given(instance=dbevolution::UpdateColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution::updatecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateColumnChange)

@given(instance=dbevolution::RemoveColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution::removecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveColumnChange)

@given(instance=dbevolution::UpdateColumnCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution::updatecolumncommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateColumnCommentChange)

@given(instance=dbevolution::RenameColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution::renamecolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution::RenameColumnChange)

@given(instance=dbevolution::AddColumnChange_strategy)
@settings(max_examples=50)
def test_dbevolution::addcolumnchange_instantiation(instance):
    assert isinstance(instance, dbevolution::AddColumnChange)

@given(instance=dbevolution::Column_strategy)
@settings(max_examples=50)
def test_dbevolution::column_instantiation(instance):
    assert isinstance(instance, dbevolution::Column)

@given(instance=dbevolution::EObject_strategy)
@settings(max_examples=50)
def test_dbevolution::eobject_instantiation(instance):
    assert isinstance(instance, dbevolution::EObject)

@given(instance=Diff_strategy)
@settings(max_examples=50)
def test_diff_instantiation(instance):
    assert isinstance(instance, Diff)

@given(instance=dbevolution::DBDiff_strategy)
@settings(max_examples=50)
def test_dbevolution::dbdiff_instantiation(instance):
    assert isinstance(instance, dbevolution::DBDiff)

@given(instance=SchemaChange_strategy)
@settings(max_examples=50)
def test_schemachange_instantiation(instance):
    assert isinstance(instance, SchemaChange)

@given(instance=dbevolution::RemoveSchema_strategy)
@settings(max_examples=50)
def test_dbevolution::removeschema_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveSchema)

@given(instance=dbevolution::AlterSchema_strategy)
@settings(max_examples=50)
def test_dbevolution::alterschema_instantiation(instance):
    assert isinstance(instance, dbevolution::AlterSchema)

@given(instance=dbevolution::UpdateSchemaCommentChange_strategy)
@settings(max_examples=50)
def test_dbevolution::updateschemacommentchange_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateSchemaCommentChange)

@given(instance=dbevolution::RenameSchemaChange_strategy)
@settings(max_examples=50)
def test_dbevolution::renameschemachange_instantiation(instance):
    assert isinstance(instance, dbevolution::RenameSchemaChange)

@given(instance=dbevolution::AddSchema_strategy)
@settings(max_examples=50)
def test_dbevolution::addschema_instantiation(instance):
    assert isinstance(instance, dbevolution::AddSchema)

@given(instance=dbevolution::Schema_strategy)
@settings(max_examples=50)
def test_dbevolution::schema_instantiation(instance):
    assert isinstance(instance, dbevolution::Schema)

@given(instance=dbevolution::SchemaChange_strategy)
@settings(max_examples=50)
def test_dbevolution::schemachange_instantiation(instance):
    assert isinstance(instance, dbevolution::SchemaChange)

@given(instance=SequenceChange_strategy)
@settings(max_examples=50)
def test_sequencechange_instantiation(instance):
    assert isinstance(instance, SequenceChange)

@given(instance=dbevolution::RemoveSequence_strategy)
@settings(max_examples=50)
def test_dbevolution::removesequence_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveSequence)

@given(instance=dbevolution::UpdateSequence_strategy)
@settings(max_examples=50)
def test_dbevolution::updatesequence_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateSequence)

@given(instance=dbevolution::AddSequence_strategy)
@settings(max_examples=50)
def test_dbevolution::addsequence_instantiation(instance):
    assert isinstance(instance, dbevolution::AddSequence)

@given(instance=dbevolution::Sequence_strategy)
@settings(max_examples=50)
def test_dbevolution::sequence_instantiation(instance):
    assert isinstance(instance, dbevolution::Sequence)

@given(instance=dbevolution::SequenceChange_strategy)
@settings(max_examples=50)
def test_dbevolution::sequencechange_instantiation(instance):
    assert isinstance(instance, dbevolution::SequenceChange)

@given(instance=ForeignKeyChange_strategy)
@settings(max_examples=50)
def test_foreignkeychange_instantiation(instance):
    assert isinstance(instance, ForeignKeyChange)

@given(instance=dbevolution::UpdateForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution::updateforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateForeignKey)

@given(instance=dbevolution::RemoveForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution::removeforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveForeignKey)

@given(instance=dbevolution::AddForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution::addforeignkey_instantiation(instance):
    assert isinstance(instance, dbevolution::AddForeignKey)

@given(instance=dbevolution::ForeignKey_strategy)
@settings(max_examples=50)
def test_dbevolution::foreignkey_instantiation(instance):
    assert isinstance(instance, dbevolution::ForeignKey)

@given(instance=dbevolution::ForeignKeyChange_strategy)
@settings(max_examples=50)
def test_dbevolution::foreignkeychange_instantiation(instance):
    assert isinstance(instance, dbevolution::ForeignKeyChange)

@given(instance=IndexChange_strategy)
@settings(max_examples=50)
def test_indexchange_instantiation(instance):
    assert isinstance(instance, IndexChange)

@given(instance=dbevolution::UpdateIndex_strategy)
@settings(max_examples=50)
def test_dbevolution::updateindex_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdateIndex)

@given(instance=dbevolution::RemoveIndex_strategy)
@settings(max_examples=50)
def test_dbevolution::removeindex_instantiation(instance):
    assert isinstance(instance, dbevolution::RemoveIndex)

@given(instance=dbevolution::AddIndex_strategy)
@settings(max_examples=50)
def test_dbevolution::addindex_instantiation(instance):
    assert isinstance(instance, dbevolution::AddIndex)

@given(instance=dbevolution::Index_strategy)
@settings(max_examples=50)
def test_dbevolution::index_instantiation(instance):
    assert isinstance(instance, dbevolution::Index)

@given(instance=dbevolution::IndexChange_strategy)
@settings(max_examples=50)
def test_dbevolution::indexchange_instantiation(instance):
    assert isinstance(instance, dbevolution::IndexChange)

@given(instance=dbevolution::UpdatePrimaryKey_strategy)
@settings(max_examples=50)
def test_dbevolution::updateprimarykey_instantiation(instance):
    assert isinstance(instance, dbevolution::UpdatePrimaryKey)
