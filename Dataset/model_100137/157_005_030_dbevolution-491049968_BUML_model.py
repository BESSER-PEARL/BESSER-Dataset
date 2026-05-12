####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
dbevolution_Column = Class(name="dbevolution_Column")
dbevolution_AddColumnChange = Class(name="dbevolution_AddColumnChange")
ColumnChange = Class(name="ColumnChange")
dbevolution_RemoveColumnChange = Class(name="dbevolution_RemoveColumnChange")
dbevolution_RenameColumnChange = Class(name="dbevolution_RenameColumnChange")
dbevolution_DatabaseChangeSet = Class(name="dbevolution_DatabaseChangeSet")
Comparison = Class(name="Comparison")
dbevolution_TableChange = Class(name="dbevolution_TableChange", is_abstract=True)
DBDiff = Class(name="DBDiff")
dbevolution_Table = Class(name="dbevolution_Table")
dbevolution_AddTable = Class(name="dbevolution_AddTable")
TableChange = Class(name="TableChange")
dbevolution_RemoveTable = Class(name="dbevolution_RemoveTable")
dbevolution_AlterTable = Class(name="dbevolution_AlterTable")
dbevolution_RenameTableChange = Class(name="dbevolution_RenameTableChange")
dbevolution_UpdateTableCommentChange = Class(name="dbevolution_UpdateTableCommentChange")
dbevolution_ColumnChange = Class(name="dbevolution_ColumnChange", is_abstract=True)
dbevolution_ConstraintChange = Class(name="dbevolution_ConstraintChange", is_abstract=True)
dbevolution_Constraint = Class(name="dbevolution_Constraint")
dbevolution_AddConstraint = Class(name="dbevolution_AddConstraint")
ConstraintChange = Class(name="ConstraintChange")
dbevolution_RemoveConstraint = Class(name="dbevolution_RemoveConstraint")
dbevolution_UpdateConstraint = Class(name="dbevolution_UpdateConstraint")
dbevolution_UpdateColumnChange = Class(name="dbevolution_UpdateColumnChange")
dbevolution_UpdateColumnCommentChange = Class(name="dbevolution_UpdateColumnCommentChange")
dbevolution_PrimaryKeyChange = Class(name="dbevolution_PrimaryKeyChange", is_abstract=True)
dbevolution_PrimaryKey = Class(name="dbevolution_PrimaryKey")
dbevolution_AddPrimaryKey = Class(name="dbevolution_AddPrimaryKey")
PrimaryKeyChange = Class(name="PrimaryKeyChange")
dbevolution_RemovePrimaryKey = Class(name="dbevolution_RemovePrimaryKey")
dbevolution_UpdatePrimaryKey = Class(name="dbevolution_UpdatePrimaryKey")
dbevolution_IndexChange = Class(name="dbevolution_IndexChange", is_abstract=True)
dbevolution_Index = Class(name="dbevolution_Index")
dbevolution_AddIndex = Class(name="dbevolution_AddIndex")
IndexChange = Class(name="IndexChange")
dbevolution_RemoveIndex = Class(name="dbevolution_RemoveIndex")
dbevolution_UpdateIndex = Class(name="dbevolution_UpdateIndex")
dbevolution_ForeignKeyChange = Class(name="dbevolution_ForeignKeyChange", is_abstract=True)
dbevolution_ForeignKey = Class(name="dbevolution_ForeignKey")
dbevolution_AddForeignKey = Class(name="dbevolution_AddForeignKey")
ForeignKeyChange = Class(name="ForeignKeyChange")
dbevolution_RemoveForeignKey = Class(name="dbevolution_RemoveForeignKey")
dbevolution_UpdateForeignKey = Class(name="dbevolution_UpdateForeignKey")
dbevolution_SequenceChange = Class(name="dbevolution_SequenceChange", is_abstract=True)
dbevolution_Sequence = Class(name="dbevolution_Sequence")
dbevolution_AddSequence = Class(name="dbevolution_AddSequence")
SequenceChange = Class(name="SequenceChange")
dbevolution_RemoveSequence = Class(name="dbevolution_RemoveSequence")
dbevolution_UpdateSequence = Class(name="dbevolution_UpdateSequence")
dbevolution_SchemaChange = Class(name="dbevolution_SchemaChange")
dbevolution_Schema = Class(name="dbevolution_Schema")
dbevolution_AddSchema = Class(name="dbevolution_AddSchema")
SchemaChange = Class(name="SchemaChange")
dbevolution_RemoveSchema = Class(name="dbevolution_RemoveSchema")
dbevolution_AlterSchema = Class(name="dbevolution_AlterSchema")
dbevolution_RenameSchemaChange = Class(name="dbevolution_RenameSchemaChange")
dbevolution_UpdateSchemaCommentChange = Class(name="dbevolution_UpdateSchemaCommentChange")
dbevolution_DBDiff = Class(name="dbevolution_DBDiff", is_abstract=True)
Diff = Class(name="Diff")
dbevolution_EObject = Class(name="dbevolution_EObject")

# dbevolution_Column class attributes and methods

# dbevolution_AddColumnChange class attributes and methods

# ColumnChange class attributes and methods

# dbevolution_RemoveColumnChange class attributes and methods

# dbevolution_RenameColumnChange class attributes and methods

# dbevolution_DatabaseChangeSet class attributes and methods

# Comparison class attributes and methods

# dbevolution_TableChange class attributes and methods

# DBDiff class attributes and methods

# dbevolution_Table class attributes and methods

# dbevolution_AddTable class attributes and methods

# TableChange class attributes and methods

# dbevolution_RemoveTable class attributes and methods

# dbevolution_AlterTable class attributes and methods

# dbevolution_RenameTableChange class attributes and methods

# dbevolution_UpdateTableCommentChange class attributes and methods

# dbevolution_ColumnChange class attributes and methods

# dbevolution_ConstraintChange class attributes and methods

# dbevolution_Constraint class attributes and methods

# dbevolution_AddConstraint class attributes and methods

# ConstraintChange class attributes and methods

# dbevolution_RemoveConstraint class attributes and methods

# dbevolution_UpdateConstraint class attributes and methods

# dbevolution_UpdateColumnChange class attributes and methods

# dbevolution_UpdateColumnCommentChange class attributes and methods

# dbevolution_PrimaryKeyChange class attributes and methods

# dbevolution_PrimaryKey class attributes and methods

# dbevolution_AddPrimaryKey class attributes and methods

# PrimaryKeyChange class attributes and methods

# dbevolution_RemovePrimaryKey class attributes and methods

# dbevolution_UpdatePrimaryKey class attributes and methods

# dbevolution_IndexChange class attributes and methods

# dbevolution_Index class attributes and methods

# dbevolution_AddIndex class attributes and methods

# IndexChange class attributes and methods

# dbevolution_RemoveIndex class attributes and methods

# dbevolution_UpdateIndex class attributes and methods

# dbevolution_ForeignKeyChange class attributes and methods

# dbevolution_ForeignKey class attributes and methods

# dbevolution_AddForeignKey class attributes and methods

# ForeignKeyChange class attributes and methods

# dbevolution_RemoveForeignKey class attributes and methods

# dbevolution_UpdateForeignKey class attributes and methods

# dbevolution_SequenceChange class attributes and methods

# dbevolution_Sequence class attributes and methods

# dbevolution_AddSequence class attributes and methods

# SequenceChange class attributes and methods

# dbevolution_RemoveSequence class attributes and methods

# dbevolution_UpdateSequence class attributes and methods

# dbevolution_SchemaChange class attributes and methods

# dbevolution_Schema class attributes and methods

# dbevolution_AddSchema class attributes and methods

# SchemaChange class attributes and methods

# dbevolution_RemoveSchema class attributes and methods

# dbevolution_AlterSchema class attributes and methods

# dbevolution_RenameSchemaChange class attributes and methods

# dbevolution_UpdateSchemaCommentChange class attributes and methods

# dbevolution_DBDiff class attributes and methods

# Diff class attributes and methods

# dbevolution_EObject class attributes and methods

# Relationships
column5: BinaryAssociation = BinaryAssociation(
    name="column5",
    ends={
        Property(name="dbevolution_Column", type=dbevolution_ColumnChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_ColumnChange", type=dbevolution_Column, multiplicity=Multiplicity(1, 1))
    }
)
newColumn6: BinaryAssociation = BinaryAssociation(
    name="newColumn6",
    ends={
        Property(name="dbevolution_Column7", type=dbevolution_RenameColumnChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_RenameColumnChange", type=dbevolution_Column, multiplicity=Multiplicity(1, 1))
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="dbevolution_Table", type=dbevolution_TableChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_TableChange", type=dbevolution_Table, multiplicity=Multiplicity(1, 1))
    }
)
newTable1: BinaryAssociation = BinaryAssociation(
    name="newTable1",
    ends={
        Property(name="dbevolution_Table2", type=dbevolution_RenameTableChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_RenameTableChange", type=dbevolution_Table, multiplicity=Multiplicity(1, 1))
    }
)
newTable3: BinaryAssociation = BinaryAssociation(
    name="newTable3",
    ends={
        Property(name="dbevolution_Table4", type=dbevolution_UpdateTableCommentChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateTableCommentChange", type=dbevolution_Table, multiplicity=Multiplicity(1, 1))
    }
)
constraint17: BinaryAssociation = BinaryAssociation(
    name="constraint17",
    ends={
        Property(name="dbevolution_Constraint", type=dbevolution_ConstraintChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_ConstraintChange", type=dbevolution_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
primaryKey8: BinaryAssociation = BinaryAssociation(
    name="primaryKey8",
    ends={
        Property(name="dbevolution_PrimaryKey", type=dbevolution_PrimaryKeyChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_PrimaryKeyChange", type=dbevolution_PrimaryKey, multiplicity=Multiplicity(1, 1))
    }
)
newPrimaryKey9: BinaryAssociation = BinaryAssociation(
    name="newPrimaryKey9",
    ends={
        Property(name="dbevolution_PrimaryKey10", type=dbevolution_UpdatePrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdatePrimaryKey", type=dbevolution_PrimaryKey, multiplicity=Multiplicity(1, 1))
    }
)
index11: BinaryAssociation = BinaryAssociation(
    name="index11",
    ends={
        Property(name="dbevolution_Index", type=dbevolution_IndexChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_IndexChange", type=dbevolution_Index, multiplicity=Multiplicity(1, 1))
    }
)
newIndex12: BinaryAssociation = BinaryAssociation(
    name="newIndex12",
    ends={
        Property(name="dbevolution_Index13", type=dbevolution_UpdateIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateIndex", type=dbevolution_Index, multiplicity=Multiplicity(1, 1))
    }
)
foreignKey14: BinaryAssociation = BinaryAssociation(
    name="foreignKey14",
    ends={
        Property(name="dbevolution_ForeignKey", type=dbevolution_ForeignKeyChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_ForeignKeyChange", type=dbevolution_ForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
newForeignKey15: BinaryAssociation = BinaryAssociation(
    name="newForeignKey15",
    ends={
        Property(name="dbevolution_ForeignKey16", type=dbevolution_UpdateForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateForeignKey", type=dbevolution_ForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
newConstraint18: BinaryAssociation = BinaryAssociation(
    name="newConstraint18",
    ends={
        Property(name="dbevolution_Constraint19", type=dbevolution_UpdateConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateConstraint", type=dbevolution_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
sequence20: BinaryAssociation = BinaryAssociation(
    name="sequence20",
    ends={
        Property(name="dbevolution_Sequence", type=dbevolution_SequenceChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_SequenceChange", type=dbevolution_Sequence, multiplicity=Multiplicity(1, 1))
    }
)
newSequence21: BinaryAssociation = BinaryAssociation(
    name="newSequence21",
    ends={
        Property(name="dbevolution_Sequence22", type=dbevolution_UpdateSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateSequence", type=dbevolution_Sequence, multiplicity=Multiplicity(1, 1))
    }
)
schema23: BinaryAssociation = BinaryAssociation(
    name="schema23",
    ends={
        Property(name="dbevolution_Schema", type=dbevolution_SchemaChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_SchemaChange", type=dbevolution_Schema, multiplicity=Multiplicity(1, 1))
    }
)
newSchema24: BinaryAssociation = BinaryAssociation(
    name="newSchema24",
    ends={
        Property(name="dbevolution_Schema25", type=dbevolution_RenameSchemaChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_RenameSchemaChange", type=dbevolution_Schema, multiplicity=Multiplicity(1, 1))
    }
)
newSchema26: BinaryAssociation = BinaryAssociation(
    name="newSchema26",
    ends={
        Property(name="dbevolution_Schema27", type=dbevolution_UpdateSchemaCommentChange, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_UpdateSchemaCommentChange", type=dbevolution_Schema, multiplicity=Multiplicity(1, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="dbevolution_EObject", type=dbevolution_DBDiff, multiplicity=Multiplicity(1, 1)),
        Property(name="dbevolution_DBDiff", type=dbevolution_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dbevolution_AddColumnChange_ColumnChange = Generalization(general=ColumnChange, specific=dbevolution_AddColumnChange)
gen_dbevolution_RemoveColumnChange_ColumnChange = Generalization(general=ColumnChange, specific=dbevolution_RemoveColumnChange)
gen_dbevolution_RenameColumnChange_ColumnChange = Generalization(general=ColumnChange, specific=dbevolution_RenameColumnChange)
gen_dbevolution_DatabaseChangeSet_Comparison = Generalization(general=Comparison, specific=dbevolution_DatabaseChangeSet)
gen_dbevolution_TableChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_TableChange)
gen_dbevolution_AddTable_TableChange = Generalization(general=TableChange, specific=dbevolution_AddTable)
gen_dbevolution_RemoveTable_TableChange = Generalization(general=TableChange, specific=dbevolution_RemoveTable)
gen_dbevolution_AlterTable_TableChange = Generalization(general=TableChange, specific=dbevolution_AlterTable)
gen_dbevolution_RenameTableChange_TableChange = Generalization(general=TableChange, specific=dbevolution_RenameTableChange)
gen_dbevolution_UpdateTableCommentChange_TableChange = Generalization(general=TableChange, specific=dbevolution_UpdateTableCommentChange)
gen_dbevolution_ColumnChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_ColumnChange)
gen_dbevolution_ConstraintChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_ConstraintChange)
gen_dbevolution_AddConstraint_ConstraintChange = Generalization(general=ConstraintChange, specific=dbevolution_AddConstraint)
gen_dbevolution_RemoveConstraint_ConstraintChange = Generalization(general=ConstraintChange, specific=dbevolution_RemoveConstraint)
gen_dbevolution_UpdateColumnChange_ColumnChange = Generalization(general=ColumnChange, specific=dbevolution_UpdateColumnChange)
gen_dbevolution_UpdateColumnCommentChange_ColumnChange = Generalization(general=ColumnChange, specific=dbevolution_UpdateColumnCommentChange)
gen_dbevolution_PrimaryKeyChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_PrimaryKeyChange)
gen_dbevolution_AddPrimaryKey_PrimaryKeyChange = Generalization(general=PrimaryKeyChange, specific=dbevolution_AddPrimaryKey)
gen_dbevolution_RemovePrimaryKey_PrimaryKeyChange = Generalization(general=PrimaryKeyChange, specific=dbevolution_RemovePrimaryKey)
gen_dbevolution_UpdatePrimaryKey_PrimaryKeyChange = Generalization(general=PrimaryKeyChange, specific=dbevolution_UpdatePrimaryKey)
gen_dbevolution_IndexChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_IndexChange)
gen_dbevolution_AddIndex_IndexChange = Generalization(general=IndexChange, specific=dbevolution_AddIndex)
gen_dbevolution_RemoveIndex_IndexChange = Generalization(general=IndexChange, specific=dbevolution_RemoveIndex)
gen_dbevolution_UpdateIndex_IndexChange = Generalization(general=IndexChange, specific=dbevolution_UpdateIndex)
gen_dbevolution_ForeignKeyChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_ForeignKeyChange)
gen_dbevolution_AddForeignKey_ForeignKeyChange = Generalization(general=ForeignKeyChange, specific=dbevolution_AddForeignKey)
gen_dbevolution_RemoveForeignKey_ForeignKeyChange = Generalization(general=ForeignKeyChange, specific=dbevolution_RemoveForeignKey)
gen_dbevolution_UpdateForeignKey_ForeignKeyChange = Generalization(general=ForeignKeyChange, specific=dbevolution_UpdateForeignKey)
gen_dbevolution_UpdateConstraint_ConstraintChange = Generalization(general=ConstraintChange, specific=dbevolution_UpdateConstraint)
gen_dbevolution_SequenceChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_SequenceChange)
gen_dbevolution_AddSequence_SequenceChange = Generalization(general=SequenceChange, specific=dbevolution_AddSequence)
gen_dbevolution_RemoveSequence_SequenceChange = Generalization(general=SequenceChange, specific=dbevolution_RemoveSequence)
gen_dbevolution_UpdateSequence_SequenceChange = Generalization(general=SequenceChange, specific=dbevolution_UpdateSequence)
gen_dbevolution_SchemaChange_DBDiff = Generalization(general=DBDiff, specific=dbevolution_SchemaChange)
gen_dbevolution_AddSchema_SchemaChange = Generalization(general=SchemaChange, specific=dbevolution_AddSchema)
gen_dbevolution_RemoveSchema_SchemaChange = Generalization(general=SchemaChange, specific=dbevolution_RemoveSchema)
gen_dbevolution_AlterSchema_SchemaChange = Generalization(general=SchemaChange, specific=dbevolution_AlterSchema)
gen_dbevolution_RenameSchemaChange_SchemaChange = Generalization(general=SchemaChange, specific=dbevolution_RenameSchemaChange)
gen_dbevolution_UpdateSchemaCommentChange_SchemaChange = Generalization(general=SchemaChange, specific=dbevolution_UpdateSchemaCommentChange)
gen_dbevolution_DBDiff_Diff = Generalization(general=Diff, specific=dbevolution_DBDiff)

# Domain Model
domain_model = DomainModel(
    name="dbevolution",
    types={dbevolution_Column, dbevolution_AddColumnChange, ColumnChange, dbevolution_RemoveColumnChange, dbevolution_RenameColumnChange, dbevolution_DatabaseChangeSet, Comparison, dbevolution_TableChange, DBDiff, dbevolution_Table, dbevolution_AddTable, TableChange, dbevolution_RemoveTable, dbevolution_AlterTable, dbevolution_RenameTableChange, dbevolution_UpdateTableCommentChange, dbevolution_ColumnChange, dbevolution_ConstraintChange, dbevolution_Constraint, dbevolution_AddConstraint, ConstraintChange, dbevolution_RemoveConstraint, dbevolution_UpdateConstraint, dbevolution_UpdateColumnChange, dbevolution_UpdateColumnCommentChange, dbevolution_PrimaryKeyChange, dbevolution_PrimaryKey, dbevolution_AddPrimaryKey, PrimaryKeyChange, dbevolution_RemovePrimaryKey, dbevolution_UpdatePrimaryKey, dbevolution_IndexChange, dbevolution_Index, dbevolution_AddIndex, IndexChange, dbevolution_RemoveIndex, dbevolution_UpdateIndex, dbevolution_ForeignKeyChange, dbevolution_ForeignKey, dbevolution_AddForeignKey, ForeignKeyChange, dbevolution_RemoveForeignKey, dbevolution_UpdateForeignKey, dbevolution_SequenceChange, dbevolution_Sequence, dbevolution_AddSequence, SequenceChange, dbevolution_RemoveSequence, dbevolution_UpdateSequence, dbevolution_SchemaChange, dbevolution_Schema, dbevolution_AddSchema, SchemaChange, dbevolution_RemoveSchema, dbevolution_AlterSchema, dbevolution_RenameSchemaChange, dbevolution_UpdateSchemaCommentChange, dbevolution_DBDiff, Diff, dbevolution_EObject},
    associations={column5, newColumn6, table0, newTable1, newTable3, constraint17, primaryKey8, newPrimaryKey9, index11, newIndex12, foreignKey14, newForeignKey15, newConstraint18, sequence20, newSequence21, schema23, newSchema24, newSchema26, target28},
    generalizations={gen_dbevolution_AddColumnChange_ColumnChange, gen_dbevolution_RemoveColumnChange_ColumnChange, gen_dbevolution_RenameColumnChange_ColumnChange, gen_dbevolution_DatabaseChangeSet_Comparison, gen_dbevolution_TableChange_DBDiff, gen_dbevolution_AddTable_TableChange, gen_dbevolution_RemoveTable_TableChange, gen_dbevolution_AlterTable_TableChange, gen_dbevolution_RenameTableChange_TableChange, gen_dbevolution_UpdateTableCommentChange_TableChange, gen_dbevolution_ColumnChange_DBDiff, gen_dbevolution_ConstraintChange_DBDiff, gen_dbevolution_AddConstraint_ConstraintChange, gen_dbevolution_RemoveConstraint_ConstraintChange, gen_dbevolution_UpdateColumnChange_ColumnChange, gen_dbevolution_UpdateColumnCommentChange_ColumnChange, gen_dbevolution_PrimaryKeyChange_DBDiff, gen_dbevolution_AddPrimaryKey_PrimaryKeyChange, gen_dbevolution_RemovePrimaryKey_PrimaryKeyChange, gen_dbevolution_UpdatePrimaryKey_PrimaryKeyChange, gen_dbevolution_IndexChange_DBDiff, gen_dbevolution_AddIndex_IndexChange, gen_dbevolution_RemoveIndex_IndexChange, gen_dbevolution_UpdateIndex_IndexChange, gen_dbevolution_ForeignKeyChange_DBDiff, gen_dbevolution_AddForeignKey_ForeignKeyChange, gen_dbevolution_RemoveForeignKey_ForeignKeyChange, gen_dbevolution_UpdateForeignKey_ForeignKeyChange, gen_dbevolution_UpdateConstraint_ConstraintChange, gen_dbevolution_SequenceChange_DBDiff, gen_dbevolution_AddSequence_SequenceChange, gen_dbevolution_RemoveSequence_SequenceChange, gen_dbevolution_UpdateSequence_SequenceChange, gen_dbevolution_SchemaChange_DBDiff, gen_dbevolution_AddSchema_SchemaChange, gen_dbevolution_RemoveSchema_SchemaChange, gen_dbevolution_AlterSchema_SchemaChange, gen_dbevolution_RenameSchemaChange_SchemaChange, gen_dbevolution_UpdateSchemaCommentChange_SchemaChange, gen_dbevolution_DBDiff_Diff},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)