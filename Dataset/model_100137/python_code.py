from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dbevolution_EObject:

    pass
class Diff:

    pass
class dbevolution_DBDiff(Diff):

    pass
class SchemaChange:

    pass
class dbevolution_UpdateSchemaCommentChange(SchemaChange):

    pass
class dbevolution_RenameSchemaChange(SchemaChange):

    pass
class dbevolution_RemoveSchema(SchemaChange):

    pass
class dbevolution_AlterSchema(SchemaChange):

    pass
class dbevolution_AddSchema(SchemaChange):

    pass
class dbevolution_Schema:

    pass
class SequenceChange:

    pass
class dbevolution_RemoveSequence(SequenceChange):

    pass
class dbevolution_UpdateSequence(SequenceChange):

    pass
class dbevolution_AddSequence(SequenceChange):

    pass
class dbevolution_Sequence:

    pass
class ForeignKeyChange:

    pass
class dbevolution_RemoveForeignKey(ForeignKeyChange):

    pass
class dbevolution_UpdateForeignKey(ForeignKeyChange):

    pass
class dbevolution_AddForeignKey(ForeignKeyChange):

    pass
class dbevolution_ForeignKey:

    pass
class IndexChange:

    pass
class dbevolution_UpdateIndex(IndexChange):

    pass
class dbevolution_RemoveIndex(IndexChange):

    pass
class dbevolution_AddIndex(IndexChange):

    pass
class dbevolution_Index:

    pass
class PrimaryKeyChange:

    pass
class dbevolution_UpdatePrimaryKey(PrimaryKeyChange):

    pass
class dbevolution_RemovePrimaryKey(PrimaryKeyChange):

    pass
class dbevolution_AddPrimaryKey(PrimaryKeyChange):

    pass
class dbevolution_PrimaryKey:

    pass
class ConstraintChange:

    pass
class dbevolution_UpdateConstraint(ConstraintChange):

    pass
class dbevolution_RemoveConstraint(ConstraintChange):

    pass
class dbevolution_AddConstraint(ConstraintChange):

    pass
class dbevolution_Constraint:

    pass
class TableChange:

    pass
class dbevolution_UpdateTableCommentChange(TableChange):

    pass
class dbevolution_RemoveTable(TableChange):

    pass
class dbevolution_RenameTableChange(TableChange):

    pass
class dbevolution_AlterTable(TableChange):

    pass
class dbevolution_AddTable(TableChange):

    pass
class dbevolution_Table:

    pass
class DBDiff:

    pass
class dbevolution_ColumnChange(DBDiff):

    pass
class dbevolution_SchemaChange(DBDiff):

    pass
class dbevolution_IndexChange(DBDiff):

    pass
class dbevolution_PrimaryKeyChange(DBDiff):

    pass
class dbevolution_SequenceChange(DBDiff):

    pass
class dbevolution_ConstraintChange(DBDiff):

    pass
class dbevolution_ForeignKeyChange(DBDiff):

    pass
class dbevolution_TableChange(DBDiff):

    pass
class Comparison:

    pass
class dbevolution_DatabaseChangeSet(Comparison):

    pass
class ColumnChange:

    pass
class dbevolution_UpdateColumnCommentChange(ColumnChange):

    pass
class dbevolution_RenameColumnChange(ColumnChange):

    pass
class dbevolution_RemoveColumnChange(ColumnChange):

    pass
class dbevolution_UpdateColumnChange(ColumnChange):

    pass
class dbevolution_AddColumnChange(ColumnChange):

    pass
class dbevolution_Column:

    pass