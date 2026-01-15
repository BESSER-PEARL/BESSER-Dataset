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

# Enumerations
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="float")
    }
)

# Classes
mm_rdb_Structure = Class(name="mm::rdb::Structure")
Schema = Class(name="Schema")
mm_rdb_Schema = Class(name="mm::rdb::Schema")
Structure = Class(name="Structure")
Table = Class(name="Table")
Sequence = Class(name="Sequence")
Index = Class(name="Index")
mm_rdb_Sequence = Class(name="mm::rdb::Sequence")
mm_rdb_Index = Class(name="mm::rdb::Index")
mm_rdb_ModelRoot = Class(name="mm::rdb::ModelRoot", is_abstract=True)
mm_rdb_Operations = Class(name="mm::rdb::Operations")
ModelRoot = Class(name="ModelRoot")
ops_ModelOperation = Class(name="ops::ModelOperation")
mm_rdb_TableConstraint = Class(name="mm::rdb::TableConstraint", is_abstract=True)
mm_rdb_Unique = Class(name="mm::rdb::Unique")
mm_rdb_PrimaryKey = Class(name="mm::rdb::PrimaryKey")
mm_rdb_ForeignKey = Class(name="mm::rdb::ForeignKey")
mm_ops_ModelOperation = Class(name="mm::ops::ModelOperation", is_abstract=True)
Operations = Class(name="Operations")
mm_ops_AddSchema = Class(name="mm::ops::AddSchema")
ModelOperation = Class(name="ModelOperation")
Column = Class(name="Column")
mm_rdb_Table = Class(name="mm::rdb::Table")
TableConstraint = Class(name="TableConstraint")
mm_rdb_Column = Class(name="mm::rdb::Column")
mm_ops_AddColumn = Class(name="mm::ops::AddColumn")
mm_ops_AddPrimaryKey = Class(name="mm::ops::AddPrimaryKey")
mm_ops_AddForeignKey = Class(name="mm::ops::AddForeignKey")
mm_ops_AddSequence = Class(name="mm::ops::AddSequence")
mm_ops_AddTable = Class(name="mm::ops::AddTable")
mm_ops_AddIndex = Class(name="mm::ops::AddIndex")
mm_ops_RemoveNotNull = Class(name="mm::ops::RemoveNotNull")
mm_ops_RenameTable = Class(name="mm::ops::RenameTable")
mm_ops_RenameColumn = Class(name="mm::ops::RenameColumn")
mm_ops_SetColumnType = Class(name="mm::ops::SetColumnType")
mm_ops_AddUnique = Class(name="mm::ops::AddUnique")
mm_ops_AddNotNull = Class(name="mm::ops::AddNotNull")
mm_ops_RemoveDefaultValue = Class(name="mm::ops::RemoveDefaultValue")
mm_ops_RemoveTable = Class(name="mm::ops::RemoveTable")
mm_ops_RemoveColumn = Class(name="mm::ops::RemoveColumn")
mm_ops_RemoveConstraint = Class(name="mm::ops::RemoveConstraint")
mm_ops_SetDefaultValue = Class(name="mm::ops::SetDefaultValue")
mm_ops_NillRows = Class(name="mm::ops::NillRows")
mm_ops_InsertRows = Class(name="mm::ops::InsertRows")
mm_ops_RemoveIndex = Class(name="mm::ops::RemoveIndex")
mm_ops_RemoveSequence = Class(name="mm::ops::RemoveSequence")
mm_ops_UpdateRows = Class(name="mm::ops::UpdateRows")
mm_ops_HasNoInstances = Class(name="mm::ops::HasNoInstances")
mm_ops_GenerateSequenceNumbers = Class(name="mm::ops::GenerateSequenceNumbers")
mm_ops_DeleteRows = Class(name="mm::ops::DeleteRows")
mm_ops_HasNoOwnInstances = Class(name="mm::ops::HasNoOwnInstances")

# mm_rdb_Structure class attributes and methods

# Schema class attributes and methods

# mm_rdb_Schema class attributes and methods
mm_rdb_Schema_name: Property = Property(name="name", type=StringType)
mm_rdb_Schema.attributes={mm_rdb_Schema_name}

# Structure class attributes and methods

# Table class attributes and methods

# Sequence class attributes and methods

# Index class attributes and methods

# mm_rdb_Sequence class attributes and methods
mm_rdb_Sequence_name: Property = Property(name="name", type=StringType)
mm_rdb_Sequence_startValue: Property = Property(name="startValue", type=IntegerType)
mm_rdb_Sequence.attributes={mm_rdb_Sequence_startValue, mm_rdb_Sequence_name}

# mm_rdb_Index class attributes and methods
mm_rdb_Index_name: Property = Property(name="name", type=StringType)
mm_rdb_Index.attributes={mm_rdb_Index_name}

# mm_rdb_ModelRoot class attributes and methods

# mm_rdb_Operations class attributes and methods

# ModelRoot class attributes and methods

# ops_ModelOperation class attributes and methods

# mm_rdb_TableConstraint class attributes and methods
mm_rdb_TableConstraint_name: Property = Property(name="name", type=StringType)
mm_rdb_TableConstraint.attributes={mm_rdb_TableConstraint_name}

# mm_rdb_Unique class attributes and methods

# mm_rdb_PrimaryKey class attributes and methods

# mm_rdb_ForeignKey class attributes and methods

# mm_ops_ModelOperation class attributes and methods

# Operations class attributes and methods

# mm_ops_AddSchema class attributes and methods
mm_ops_AddSchema_name: Property = Property(name="name", type=StringType)
mm_ops_AddSchema.attributes={mm_ops_AddSchema_name}

# ModelOperation class attributes and methods

# Column class attributes and methods

# mm_rdb_Table class attributes and methods
mm_rdb_Table_name: Property = Property(name="name", type=StringType)
mm_rdb_Table.attributes={mm_rdb_Table_name}

# TableConstraint class attributes and methods

# mm_rdb_Column class attributes and methods
mm_rdb_Column_isNillable: Property = Property(name="isNillable", type=StringType)
mm_rdb_Column_name: Property = Property(name="name", type=StringType)
mm_rdb_Column_type: Property = Property(name="type", type=StringType)
mm_rdb_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
mm_rdb_Column.attributes={mm_rdb_Column_type, mm_rdb_Column_defaultValue, mm_rdb_Column_name, mm_rdb_Column_isNillable}

# mm_ops_AddColumn class attributes and methods
mm_ops_AddColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddColumn_name: Property = Property(name="name", type=StringType)
mm_ops_AddColumn_type: Property = Property(name="type", type=StringType)
mm_ops_AddColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
mm_ops_AddColumn.attributes={mm_ops_AddColumn_owningTableName, mm_ops_AddColumn_type, mm_ops_AddColumn_defaultValue, mm_ops_AddColumn_name, mm_ops_AddColumn_owningSchemaName}

# mm_ops_AddPrimaryKey class attributes and methods
mm_ops_AddPrimaryKey_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddPrimaryKey_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddPrimaryKey_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddPrimaryKey_name: Property = Property(name="name", type=StringType)
mm_ops_AddPrimaryKey.attributes={mm_ops_AddPrimaryKey_name, mm_ops_AddPrimaryKey_owningSchemaName, mm_ops_AddPrimaryKey_owningTableName, mm_ops_AddPrimaryKey_constrainedColumnName}

# mm_ops_AddForeignKey class attributes and methods
mm_ops_AddForeignKey_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddForeignKey_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddForeignKey_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddForeignKey_name: Property = Property(name="name", type=StringType)
mm_ops_AddForeignKey_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_AddForeignKey.attributes={mm_ops_AddForeignKey_targetTableName, mm_ops_AddForeignKey_name, mm_ops_AddForeignKey_owningSchemaName, mm_ops_AddForeignKey_owningTableName, mm_ops_AddForeignKey_constrainedColumnName}

# mm_ops_AddSequence class attributes and methods
mm_ops_AddSequence_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddSequence_name: Property = Property(name="name", type=StringType)
mm_ops_AddSequence_startValue: Property = Property(name="startValue", type=IntegerType)
mm_ops_AddSequence.attributes={mm_ops_AddSequence_startValue, mm_ops_AddSequence_owningSchemaName, mm_ops_AddSequence_name}

# mm_ops_AddTable class attributes and methods
mm_ops_AddTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddTable_name: Property = Property(name="name", type=StringType)
mm_ops_AddTable.attributes={mm_ops_AddTable_owningSchemaName, mm_ops_AddTable_name}

# mm_ops_AddIndex class attributes and methods
mm_ops_AddIndex_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddIndex_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddIndex_name: Property = Property(name="name", type=StringType)
mm_ops_AddIndex_columnsNames: Property = Property(name="columnsNames", type=StringType)
mm_ops_AddIndex.attributes={mm_ops_AddIndex_name, mm_ops_AddIndex_owningSchemaName, mm_ops_AddIndex_columnsNames, mm_ops_AddIndex_owningTableName}

# mm_ops_RemoveNotNull class attributes and methods
mm_ops_RemoveNotNull_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveNotNull_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveNotNull_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_RemoveNotNull.attributes={mm_ops_RemoveNotNull_owningSchemaName, mm_ops_RemoveNotNull_owningTableName, mm_ops_RemoveNotNull_constrainedColumnName}

# mm_ops_RenameTable class attributes and methods
mm_ops_RenameTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RenameTable_name: Property = Property(name="name", type=StringType)
mm_ops_RenameTable_newName: Property = Property(name="newName", type=StringType)
mm_ops_RenameTable.attributes={mm_ops_RenameTable_name, mm_ops_RenameTable_owningSchemaName, mm_ops_RenameTable_newName}

# mm_ops_RenameColumn class attributes and methods
mm_ops_RenameColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RenameColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RenameColumn_name: Property = Property(name="name", type=StringType)
mm_ops_RenameColumn_newName: Property = Property(name="newName", type=StringType)
mm_ops_RenameColumn.attributes={mm_ops_RenameColumn_name, mm_ops_RenameColumn_owningSchemaName, mm_ops_RenameColumn_newName, mm_ops_RenameColumn_owningTableName}

# mm_ops_SetColumnType class attributes and methods
mm_ops_SetColumnType_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_SetColumnType_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_SetColumnType_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_SetColumnType_newType: Property = Property(name="newType", type=StringType)
mm_ops_SetColumnType_oldType: Property = Property(name="oldType", type=StringType)
mm_ops_SetColumnType.attributes={mm_ops_SetColumnType_owningSchemaName, mm_ops_SetColumnType_oldType, mm_ops_SetColumnType_owningTableName, mm_ops_SetColumnType_newType, mm_ops_SetColumnType_owningColumnName}

# mm_ops_AddUnique class attributes and methods
mm_ops_AddUnique_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddUnique_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddUnique_constrainedColumnNames: Property = Property(name="constrainedColumnNames", type=StringType)
mm_ops_AddUnique_name: Property = Property(name="name", type=StringType)
mm_ops_AddUnique.attributes={mm_ops_AddUnique_owningSchemaName, mm_ops_AddUnique_owningTableName, mm_ops_AddUnique_constrainedColumnNames, mm_ops_AddUnique_name}

# mm_ops_AddNotNull class attributes and methods
mm_ops_AddNotNull_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddNotNull_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddNotNull_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddNotNull.attributes={mm_ops_AddNotNull_owningTableName, mm_ops_AddNotNull_owningSchemaName, mm_ops_AddNotNull_constrainedColumnName}

# mm_ops_RemoveDefaultValue class attributes and methods
mm_ops_RemoveDefaultValue_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveDefaultValue_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveDefaultValue_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_RemoveDefaultValue.attributes={mm_ops_RemoveDefaultValue_owningSchemaName, mm_ops_RemoveDefaultValue_owningColumnName, mm_ops_RemoveDefaultValue_owningTableName}

# mm_ops_RemoveTable class attributes and methods
mm_ops_RemoveTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveTable_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveTable.attributes={mm_ops_RemoveTable_owningSchemaName, mm_ops_RemoveTable_name}

# mm_ops_RemoveColumn class attributes and methods
mm_ops_RemoveColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveColumn_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveColumn.attributes={mm_ops_RemoveColumn_owningTableName, mm_ops_RemoveColumn_owningSchemaName, mm_ops_RemoveColumn_name}

# mm_ops_RemoveConstraint class attributes and methods
mm_ops_RemoveConstraint_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveConstraint_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveConstraint_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveConstraint.attributes={mm_ops_RemoveConstraint_name, mm_ops_RemoveConstraint_owningSchemaName, mm_ops_RemoveConstraint_owningTableName}

# mm_ops_SetDefaultValue class attributes and methods
mm_ops_SetDefaultValue_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_SetDefaultValue_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_SetDefaultValue_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_SetDefaultValue_newDefaultValue: Property = Property(name="newDefaultValue", type=StringType)
mm_ops_SetDefaultValue.attributes={mm_ops_SetDefaultValue_owningTableName, mm_ops_SetDefaultValue_owningSchemaName, mm_ops_SetDefaultValue_owningColumnName, mm_ops_SetDefaultValue_newDefaultValue}

# mm_ops_NillRows class attributes and methods
mm_ops_NillRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_NillRows_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_NillRows_columnName: Property = Property(name="columnName", type=StringType)
mm_ops_NillRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_NillRows.attributes={mm_ops_NillRows_whereCondition, mm_ops_NillRows_tableName, mm_ops_NillRows_columnName, mm_ops_NillRows_owningSchemaName}

# mm_ops_InsertRows class attributes and methods
mm_ops_InsertRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_InsertRows_sourceTableName: Property = Property(name="sourceTableName", type=StringType)
mm_ops_InsertRows_sourceColumnsNames: Property = Property(name="sourceColumnsNames", type=StringType)
mm_ops_InsertRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_InsertRows_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_InsertRows_targetColumnNames: Property = Property(name="targetColumnNames", type=StringType)
mm_ops_InsertRows.attributes={mm_ops_InsertRows_targetColumnNames, mm_ops_InsertRows_sourceTableName, mm_ops_InsertRows_owningSchemaName, mm_ops_InsertRows_targetTableName, mm_ops_InsertRows_whereCondition, mm_ops_InsertRows_sourceColumnsNames}

# mm_ops_RemoveIndex class attributes and methods
mm_ops_RemoveIndex_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveIndex_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveIndex.attributes={mm_ops_RemoveIndex_owningSchemaName, mm_ops_RemoveIndex_name}

# mm_ops_RemoveSequence class attributes and methods
mm_ops_RemoveSequence_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveSequence_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveSequence.attributes={mm_ops_RemoveSequence_owningSchemaName, mm_ops_RemoveSequence_name}

# mm_ops_UpdateRows class attributes and methods
mm_ops_UpdateRows_sourceTableName: Property = Property(name="sourceTableName", type=StringType)
mm_ops_UpdateRows_sourceColumnName: Property = Property(name="sourceColumnName", type=StringType)
mm_ops_UpdateRows_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_UpdateRows_targetColumnName: Property = Property(name="targetColumnName", type=StringType)
mm_ops_UpdateRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_UpdateRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_UpdateRows.attributes={mm_ops_UpdateRows_owningSchemaName, mm_ops_UpdateRows_sourceColumnName, mm_ops_UpdateRows_whereCondition, mm_ops_UpdateRows_targetColumnName, mm_ops_UpdateRows_targetTableName, mm_ops_UpdateRows_sourceTableName}

# mm_ops_HasNoInstances class attributes and methods
mm_ops_HasNoInstances_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_HasNoInstances_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_HasNoInstances.attributes={mm_ops_HasNoInstances_tableName, mm_ops_HasNoInstances_owningSchemaName}

# mm_ops_GenerateSequenceNumbers class attributes and methods
mm_ops_GenerateSequenceNumbers_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_GenerateSequenceNumbers_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_GenerateSequenceNumbers_columnName: Property = Property(name="columnName", type=StringType)
mm_ops_GenerateSequenceNumbers_sequenceName: Property = Property(name="sequenceName", type=StringType)
mm_ops_GenerateSequenceNumbers.attributes={mm_ops_GenerateSequenceNumbers_sequenceName, mm_ops_GenerateSequenceNumbers_owningSchemaName, mm_ops_GenerateSequenceNumbers_columnName, mm_ops_GenerateSequenceNumbers_tableName}

# mm_ops_DeleteRows class attributes and methods
mm_ops_DeleteRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_DeleteRows_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_DeleteRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_DeleteRows.attributes={mm_ops_DeleteRows_owningSchemaName, mm_ops_DeleteRows_whereCondition, mm_ops_DeleteRows_tableName}

# mm_ops_HasNoOwnInstances class attributes and methods
mm_ops_HasNoOwnInstances_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_HasNoOwnInstances_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_HasNoOwnInstances_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_HasNoOwnInstances.attributes={mm_ops_HasNoOwnInstances_tableName, mm_ops_HasNoOwnInstances_whereCondition, mm_ops_HasNoOwnInstances_owningSchemaName}

# Relationships
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="rdb", type=mm_rdb_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="ops", type=ops_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas1: BinaryAssociation = BinaryAssociation(
    name="schemas1",
    ends={
        Property(name="rdb2", type=mm_rdb_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningStructure3: BinaryAssociation = BinaryAssociation(
    name="owningStructure3",
    ends={
        Property(name="rdb4", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Structure", type=Structure, multiplicity=Multiplicity(1, 1))
    }
)
tables5: BinaryAssociation = BinaryAssociation(
    name="tables5",
    ends={
        Property(name="rdb6", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Table", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequence7: BinaryAssociation = BinaryAssociation(
    name="sequence7",
    ends={
        Property(name="rdb8", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Sequence", type=Sequence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indexes9: BinaryAssociation = BinaryAssociation(
    name="indexes9",
    ends={
        Property(name="rdb10", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Index", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema11: BinaryAssociation = BinaryAssociation(
    name="owningSchema11",
    ends={
        Property(name="rdb13", type=mm_rdb_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema12", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningSchema14: BinaryAssociation = BinaryAssociation(
    name="owningSchema14",
    ends={
        Property(name="rdb16", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema15", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningTable29: BinaryAssociation = BinaryAssociation(
    name="owningTable29",
    ends={
        Property(name="rdb31", type=mm_rdb_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Table30", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
uniqueColumns32: BinaryAssociation = BinaryAssociation(
    name="uniqueColumns32",
    ends={
        Property(name="Column33", type=mm_rdb_Unique, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Unique", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedColumn34: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn34",
    ends={
        Property(name="Column35", type=mm_rdb_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_PrimaryKey", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
targetTable36: BinaryAssociation = BinaryAssociation(
    name="targetTable36",
    ends={
        Property(name="Table37", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constrainedColumn38: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn38",
    ends={
        Property(name="Column40", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey39", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
owningOperations41: BinaryAssociation = BinaryAssociation(
    name="owningOperations41",
    ends={
        Property(name="rdb42", type=mm_ops_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="Operations", type=Operations, multiplicity=Multiplicity(1, 1))
    }
)
columns17: BinaryAssociation = BinaryAssociation(
    name="columns17",
    ends={
        Property(name="Column", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
owningSchema18: BinaryAssociation = BinaryAssociation(
    name="owningSchema18",
    ends={
        Property(name="rdb20", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema19", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns21: BinaryAssociation = BinaryAssociation(
    name="columns21",
    ends={
        Property(name="rdb23", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Column22", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints24: BinaryAssociation = BinaryAssociation(
    name="constraints24",
    ends={
        Property(name="rdb25", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableConstraint", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTable26: BinaryAssociation = BinaryAssociation(
    name="owningTable26",
    ends={
        Property(name="rdb28", type=mm_rdb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Table27", type=Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mm_rdb_Structure_ModelRoot = Generalization(general=ModelRoot, specific=mm_rdb_Structure)
gen_mm_rdb_Operations_ModelRoot = Generalization(general=ModelRoot, specific=mm_rdb_Operations)
gen_mm_rdb_Unique_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_Unique)
gen_mm_rdb_PrimaryKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_PrimaryKey)
gen_mm_rdb_ForeignKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_ForeignKey)
gen_mm_ops_AddSchema_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddSchema)
gen_mm_ops_AddColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddColumn)
gen_mm_ops_AddPrimaryKey_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddPrimaryKey)
gen_mm_ops_AddForeignKey_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddForeignKey)
gen_mm_ops_AddSequence_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddSequence)
gen_mm_ops_AddTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddTable)
gen_mm_ops_AddIndex_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddIndex)
gen_mm_ops_RemoveNotNull_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveNotNull)
gen_mm_ops_RenameTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RenameTable)
gen_mm_ops_RenameColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RenameColumn)
gen_mm_ops_SetColumnType_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_SetColumnType)
gen_mm_ops_AddUnique_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddUnique)
gen_mm_ops_AddNotNull_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddNotNull)
gen_mm_ops_RemoveDefaultValue_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveDefaultValue)
gen_mm_ops_RemoveTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveTable)
gen_mm_ops_RemoveColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveColumn)
gen_mm_ops_RemoveConstraint_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveConstraint)
gen_mm_ops_SetDefaultValue_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_SetDefaultValue)
gen_mm_ops_NillRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_NillRows)
gen_mm_ops_InsertRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_InsertRows)
gen_mm_ops_RemoveIndex_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveIndex)
gen_mm_ops_RemoveSequence_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveSequence)
gen_mm_ops_UpdateRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_UpdateRows)
gen_mm_ops_HasNoInstances_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_HasNoInstances)
gen_mm_ops_GenerateSequenceNumbers_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_GenerateSequenceNumbers)
gen_mm_ops_DeleteRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_DeleteRows)
gen_mm_ops_HasNoOwnInstances_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_HasNoOwnInstances)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={mm_rdb_Structure, Schema, mm_rdb_Schema, Structure, Table, Sequence, Index, mm_rdb_Sequence, mm_rdb_Index, mm_rdb_ModelRoot, mm_rdb_Operations, ModelRoot, ops_ModelOperation, mm_rdb_TableConstraint, mm_rdb_Unique, mm_rdb_PrimaryKey, mm_rdb_ForeignKey, mm_ops_ModelOperation, Operations, mm_ops_AddSchema, ModelOperation, Column, mm_rdb_Table, TableConstraint, mm_rdb_Column, mm_ops_AddColumn, mm_ops_AddPrimaryKey, mm_ops_AddForeignKey, mm_ops_AddSequence, mm_ops_AddTable, mm_ops_AddIndex, mm_ops_RemoveNotNull, mm_ops_RenameTable, mm_ops_RenameColumn, mm_ops_SetColumnType, mm_ops_AddUnique, mm_ops_AddNotNull, mm_ops_RemoveDefaultValue, mm_ops_RemoveTable, mm_ops_RemoveColumn, mm_ops_RemoveConstraint, mm_ops_SetDefaultValue, mm_ops_NillRows, mm_ops_InsertRows, mm_ops_RemoveIndex, mm_ops_RemoveSequence, mm_ops_UpdateRows, mm_ops_HasNoInstances, mm_ops_GenerateSequenceNumbers, mm_ops_DeleteRows, mm_ops_HasNoOwnInstances, PrimitiveType},
    associations={operations0, schemas1, owningStructure3, tables5, sequence7, indexes9, owningSchema11, owningSchema14, owningTable29, uniqueColumns32, constrainedColumn34, targetTable36, constrainedColumn38, owningOperations41, columns17, owningSchema18, columns21, constraints24, owningTable26},
    generalizations={gen_mm_rdb_Structure_ModelRoot, gen_mm_rdb_Operations_ModelRoot, gen_mm_rdb_Unique_TableConstraint, gen_mm_rdb_PrimaryKey_TableConstraint, gen_mm_rdb_ForeignKey_TableConstraint, gen_mm_ops_AddSchema_ModelOperation, gen_mm_ops_AddColumn_ModelOperation, gen_mm_ops_AddPrimaryKey_ModelOperation, gen_mm_ops_AddForeignKey_ModelOperation, gen_mm_ops_AddSequence_ModelOperation, gen_mm_ops_AddTable_ModelOperation, gen_mm_ops_AddIndex_ModelOperation, gen_mm_ops_RemoveNotNull_ModelOperation, gen_mm_ops_RenameTable_ModelOperation, gen_mm_ops_RenameColumn_ModelOperation, gen_mm_ops_SetColumnType_ModelOperation, gen_mm_ops_AddUnique_ModelOperation, gen_mm_ops_AddNotNull_ModelOperation, gen_mm_ops_RemoveDefaultValue_ModelOperation, gen_mm_ops_RemoveTable_ModelOperation, gen_mm_ops_RemoveColumn_ModelOperation, gen_mm_ops_RemoveConstraint_ModelOperation, gen_mm_ops_SetDefaultValue_ModelOperation, gen_mm_ops_NillRows_ModelOperation, gen_mm_ops_InsertRows_ModelOperation, gen_mm_ops_RemoveIndex_ModelOperation, gen_mm_ops_RemoveSequence_ModelOperation, gen_mm_ops_UpdateRows_ModelOperation, gen_mm_ops_HasNoInstances_ModelOperation, gen_mm_ops_GenerateSequenceNumbers_ModelOperation, gen_mm_ops_DeleteRows_ModelOperation, gen_mm_ops_HasNoOwnInstances_ModelOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)