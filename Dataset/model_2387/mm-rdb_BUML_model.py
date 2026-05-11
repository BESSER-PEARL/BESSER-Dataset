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
mm_rdb_ModelRoot = Class(name="mm_rdb_ModelRoot", is_abstract=True)
Index = Class(name="Index")
mm_rdb_Sequence = Class(name="mm_rdb_Sequence")
mm_rdb_Index = Class(name="mm_rdb_Index")
mm_rdb_Operations = Class(name="mm_rdb_Operations")
ModelRoot = Class(name="ModelRoot")
ops_ModelOperation = Class(name="ops_ModelOperation")
mm_rdb_Structure = Class(name="mm_rdb_Structure")
Schema = Class(name="Schema")
mm_rdb_Schema = Class(name="mm_rdb_Schema")
Structure = Class(name="Structure")
Table = Class(name="Table")
mm_rdb_PrimaryKey = Class(name="mm_rdb_PrimaryKey")
Sequence = Class(name="Sequence")
mm_rdb_ForeignKey = Class(name="mm_rdb_ForeignKey")
mm_ops_ModelOperation = Class(name="mm_ops_ModelOperation", is_abstract=True)
Column = Class(name="Column")
mm_rdb_Table = Class(name="mm_rdb_Table")
TableConstraint = Class(name="TableConstraint")
mm_rdb_Column = Class(name="mm_rdb_Column")
mm_rdb_TableConstraint = Class(name="mm_rdb_TableConstraint", is_abstract=True)
mm_rdb_Unique = Class(name="mm_rdb_Unique")
mm_ops_AddForeignKey = Class(name="mm_ops_AddForeignKey")
mm_ops_AddUnique = Class(name="mm_ops_AddUnique")
mm_ops_AddNotNull = Class(name="mm_ops_AddNotNull")
Operations = Class(name="Operations")
mm_ops_AddSchema = Class(name="mm_ops_AddSchema")
ModelOperation = Class(name="ModelOperation")
mm_ops_AddSequence = Class(name="mm_ops_AddSequence")
mm_ops_AddTable = Class(name="mm_ops_AddTable")
mm_ops_AddIndex = Class(name="mm_ops_AddIndex")
mm_ops_AddColumn = Class(name="mm_ops_AddColumn")
mm_ops_AddPrimaryKey = Class(name="mm_ops_AddPrimaryKey")
mm_ops_RemoveDefaultValue = Class(name="mm_ops_RemoveDefaultValue")
mm_ops_RemoveTable = Class(name="mm_ops_RemoveTable")
mm_ops_RemoveColumn = Class(name="mm_ops_RemoveColumn")
mm_ops_RemoveNotNull = Class(name="mm_ops_RemoveNotNull")
mm_ops_RenameTable = Class(name="mm_ops_RenameTable")
mm_ops_RenameColumn = Class(name="mm_ops_RenameColumn")
mm_ops_SetColumnType = Class(name="mm_ops_SetColumnType")
mm_ops_SetDefaultValue = Class(name="mm_ops_SetDefaultValue")
mm_ops_DeleteRows = Class(name="mm_ops_DeleteRows")
mm_ops_HasNoOwnInstances = Class(name="mm_ops_HasNoOwnInstances")
mm_ops_HasNoInstances = Class(name="mm_ops_HasNoInstances")
mm_ops_RemoveConstraint = Class(name="mm_ops_RemoveConstraint")
mm_ops_RemoveIndex = Class(name="mm_ops_RemoveIndex")
mm_ops_RemoveSequence = Class(name="mm_ops_RemoveSequence")
mm_ops_UpdateRows = Class(name="mm_ops_UpdateRows")
mm_ops_NillRows = Class(name="mm_ops_NillRows")
mm_ops_InsertRows = Class(name="mm_ops_InsertRows")
mm_ops_GenerateSequenceNumbers = Class(name="mm_ops_GenerateSequenceNumbers")

# mm_rdb_ModelRoot class attributes and methods

# Index class attributes and methods

# mm_rdb_Sequence class attributes and methods
mm_rdb_Sequence_name: Property = Property(name="name", type=StringType)
mm_rdb_Sequence_startValue: Property = Property(name="startValue", type=IntegerType)
mm_rdb_Sequence.attributes={mm_rdb_Sequence_name, mm_rdb_Sequence_startValue}

# mm_rdb_Index class attributes and methods
mm_rdb_Index_name: Property = Property(name="name", type=StringType)
mm_rdb_Index.attributes={mm_rdb_Index_name}

# mm_rdb_Operations class attributes and methods

# ModelRoot class attributes and methods

# ops_ModelOperation class attributes and methods

# mm_rdb_Structure class attributes and methods

# Schema class attributes and methods

# mm_rdb_Schema class attributes and methods
mm_rdb_Schema_name: Property = Property(name="name", type=StringType)
mm_rdb_Schema.attributes={mm_rdb_Schema_name}

# Structure class attributes and methods

# Table class attributes and methods

# mm_rdb_PrimaryKey class attributes and methods

# Sequence class attributes and methods

# mm_rdb_ForeignKey class attributes and methods

# mm_ops_ModelOperation class attributes and methods

# Column class attributes and methods

# mm_rdb_Table class attributes and methods
mm_rdb_Table_name: Property = Property(name="name", type=StringType)
mm_rdb_Table.attributes={mm_rdb_Table_name}

# TableConstraint class attributes and methods

# mm_rdb_Column class attributes and methods
mm_rdb_Column_name: Property = Property(name="name", type=StringType)
mm_rdb_Column_type: Property = Property(name="type", type=StringType)
mm_rdb_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
mm_rdb_Column_isNillable: Property = Property(name="isNillable", type=StringType)
mm_rdb_Column.attributes={mm_rdb_Column_defaultValue, mm_rdb_Column_name, mm_rdb_Column_isNillable, mm_rdb_Column_type}

# mm_rdb_TableConstraint class attributes and methods
mm_rdb_TableConstraint_name: Property = Property(name="name", type=StringType)
mm_rdb_TableConstraint.attributes={mm_rdb_TableConstraint_name}

# mm_rdb_Unique class attributes and methods

# mm_ops_AddForeignKey class attributes and methods
mm_ops_AddForeignKey_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddForeignKey_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddForeignKey_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddForeignKey_name: Property = Property(name="name", type=StringType)
mm_ops_AddForeignKey_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_AddForeignKey.attributes={mm_ops_AddForeignKey_constrainedColumnName, mm_ops_AddForeignKey_targetTableName, mm_ops_AddForeignKey_owningSchemaName, mm_ops_AddForeignKey_owningTableName, mm_ops_AddForeignKey_name}

# mm_ops_AddUnique class attributes and methods
mm_ops_AddUnique_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddUnique_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddUnique_constrainedColumnNames: Property = Property(name="constrainedColumnNames", type=StringType)
mm_ops_AddUnique_name: Property = Property(name="name", type=StringType)
mm_ops_AddUnique.attributes={mm_ops_AddUnique_constrainedColumnNames, mm_ops_AddUnique_name, mm_ops_AddUnique_owningSchemaName, mm_ops_AddUnique_owningTableName}

# mm_ops_AddNotNull class attributes and methods
mm_ops_AddNotNull_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddNotNull_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddNotNull_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddNotNull.attributes={mm_ops_AddNotNull_owningSchemaName, mm_ops_AddNotNull_constrainedColumnName, mm_ops_AddNotNull_owningTableName}

# Operations class attributes and methods

# mm_ops_AddSchema class attributes and methods
mm_ops_AddSchema_name: Property = Property(name="name", type=StringType)
mm_ops_AddSchema.attributes={mm_ops_AddSchema_name}

# ModelOperation class attributes and methods

# mm_ops_AddSequence class attributes and methods
mm_ops_AddSequence_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddSequence_name: Property = Property(name="name", type=StringType)
mm_ops_AddSequence_startValue: Property = Property(name="startValue", type=IntegerType)
mm_ops_AddSequence.attributes={mm_ops_AddSequence_name, mm_ops_AddSequence_startValue, mm_ops_AddSequence_owningSchemaName}

# mm_ops_AddTable class attributes and methods
mm_ops_AddTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddTable_name: Property = Property(name="name", type=StringType)
mm_ops_AddTable.attributes={mm_ops_AddTable_name, mm_ops_AddTable_owningSchemaName}

# mm_ops_AddIndex class attributes and methods
mm_ops_AddIndex_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddIndex_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddIndex_name: Property = Property(name="name", type=StringType)
mm_ops_AddIndex_columnsNames: Property = Property(name="columnsNames", type=StringType)
mm_ops_AddIndex.attributes={mm_ops_AddIndex_owningSchemaName, mm_ops_AddIndex_name, mm_ops_AddIndex_columnsNames, mm_ops_AddIndex_owningTableName}

# mm_ops_AddColumn class attributes and methods
mm_ops_AddColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddColumn_name: Property = Property(name="name", type=StringType)
mm_ops_AddColumn_type: Property = Property(name="type", type=StringType)
mm_ops_AddColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
mm_ops_AddColumn.attributes={mm_ops_AddColumn_type, mm_ops_AddColumn_owningTableName, mm_ops_AddColumn_defaultValue, mm_ops_AddColumn_owningSchemaName, mm_ops_AddColumn_name}

# mm_ops_AddPrimaryKey class attributes and methods
mm_ops_AddPrimaryKey_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_AddPrimaryKey_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_AddPrimaryKey_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_AddPrimaryKey_name: Property = Property(name="name", type=StringType)
mm_ops_AddPrimaryKey.attributes={mm_ops_AddPrimaryKey_constrainedColumnName, mm_ops_AddPrimaryKey_name, mm_ops_AddPrimaryKey_owningSchemaName, mm_ops_AddPrimaryKey_owningTableName}

# mm_ops_RemoveDefaultValue class attributes and methods
mm_ops_RemoveDefaultValue_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveDefaultValue_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveDefaultValue_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_RemoveDefaultValue.attributes={mm_ops_RemoveDefaultValue_owningColumnName, mm_ops_RemoveDefaultValue_owningSchemaName, mm_ops_RemoveDefaultValue_owningTableName}

# mm_ops_RemoveTable class attributes and methods
mm_ops_RemoveTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveTable_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveTable.attributes={mm_ops_RemoveTable_name, mm_ops_RemoveTable_owningSchemaName}

# mm_ops_RemoveColumn class attributes and methods
mm_ops_RemoveColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveColumn_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveColumn.attributes={mm_ops_RemoveColumn_owningTableName, mm_ops_RemoveColumn_owningSchemaName, mm_ops_RemoveColumn_name}

# mm_ops_RemoveNotNull class attributes and methods
mm_ops_RemoveNotNull_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveNotNull_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveNotNull_constrainedColumnName: Property = Property(name="constrainedColumnName", type=StringType)
mm_ops_RemoveNotNull.attributes={mm_ops_RemoveNotNull_owningSchemaName, mm_ops_RemoveNotNull_owningTableName, mm_ops_RemoveNotNull_constrainedColumnName}

# mm_ops_RenameTable class attributes and methods
mm_ops_RenameTable_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RenameTable_name: Property = Property(name="name", type=StringType)
mm_ops_RenameTable_newName: Property = Property(name="newName", type=StringType)
mm_ops_RenameTable.attributes={mm_ops_RenameTable_owningSchemaName, mm_ops_RenameTable_name, mm_ops_RenameTable_newName}

# mm_ops_RenameColumn class attributes and methods
mm_ops_RenameColumn_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RenameColumn_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RenameColumn_name: Property = Property(name="name", type=StringType)
mm_ops_RenameColumn_newName: Property = Property(name="newName", type=StringType)
mm_ops_RenameColumn.attributes={mm_ops_RenameColumn_owningSchemaName, mm_ops_RenameColumn_name, mm_ops_RenameColumn_owningTableName, mm_ops_RenameColumn_newName}

# mm_ops_SetColumnType class attributes and methods
mm_ops_SetColumnType_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_SetColumnType_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_SetColumnType_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_SetColumnType_newType: Property = Property(name="newType", type=StringType)
mm_ops_SetColumnType_oldType: Property = Property(name="oldType", type=StringType)
mm_ops_SetColumnType.attributes={mm_ops_SetColumnType_oldType, mm_ops_SetColumnType_newType, mm_ops_SetColumnType_owningSchemaName, mm_ops_SetColumnType_owningTableName, mm_ops_SetColumnType_owningColumnName}

# mm_ops_SetDefaultValue class attributes and methods
mm_ops_SetDefaultValue_owningColumnName: Property = Property(name="owningColumnName", type=StringType)
mm_ops_SetDefaultValue_newDefaultValue: Property = Property(name="newDefaultValue", type=StringType)
mm_ops_SetDefaultValue_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_SetDefaultValue_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_SetDefaultValue.attributes={mm_ops_SetDefaultValue_owningSchemaName, mm_ops_SetDefaultValue_owningColumnName, mm_ops_SetDefaultValue_owningTableName, mm_ops_SetDefaultValue_newDefaultValue}

# mm_ops_DeleteRows class attributes and methods
mm_ops_DeleteRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_DeleteRows_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_DeleteRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_DeleteRows.attributes={mm_ops_DeleteRows_whereCondition, mm_ops_DeleteRows_tableName, mm_ops_DeleteRows_owningSchemaName}

# mm_ops_HasNoOwnInstances class attributes and methods
mm_ops_HasNoOwnInstances_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_HasNoOwnInstances_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_HasNoOwnInstances_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_HasNoOwnInstances.attributes={mm_ops_HasNoOwnInstances_whereCondition, mm_ops_HasNoOwnInstances_tableName, mm_ops_HasNoOwnInstances_owningSchemaName}

# mm_ops_HasNoInstances class attributes and methods
mm_ops_HasNoInstances_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_HasNoInstances_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_HasNoInstances.attributes={mm_ops_HasNoInstances_tableName, mm_ops_HasNoInstances_owningSchemaName}

# mm_ops_RemoveConstraint class attributes and methods
mm_ops_RemoveConstraint_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveConstraint_owningTableName: Property = Property(name="owningTableName", type=StringType)
mm_ops_RemoveConstraint_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveConstraint.attributes={mm_ops_RemoveConstraint_owningSchemaName, mm_ops_RemoveConstraint_owningTableName, mm_ops_RemoveConstraint_name}

# mm_ops_RemoveIndex class attributes and methods
mm_ops_RemoveIndex_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveIndex_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveIndex.attributes={mm_ops_RemoveIndex_owningSchemaName, mm_ops_RemoveIndex_name}

# mm_ops_RemoveSequence class attributes and methods
mm_ops_RemoveSequence_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_RemoveSequence_name: Property = Property(name="name", type=StringType)
mm_ops_RemoveSequence.attributes={mm_ops_RemoveSequence_owningSchemaName, mm_ops_RemoveSequence_name}

# mm_ops_UpdateRows class attributes and methods
mm_ops_UpdateRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_UpdateRows_sourceTableName: Property = Property(name="sourceTableName", type=StringType)
mm_ops_UpdateRows_sourceColumnName: Property = Property(name="sourceColumnName", type=StringType)
mm_ops_UpdateRows_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_UpdateRows_targetColumnName: Property = Property(name="targetColumnName", type=StringType)
mm_ops_UpdateRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_UpdateRows.attributes={mm_ops_UpdateRows_sourceTableName, mm_ops_UpdateRows_whereCondition, mm_ops_UpdateRows_targetTableName, mm_ops_UpdateRows_targetColumnName, mm_ops_UpdateRows_sourceColumnName, mm_ops_UpdateRows_owningSchemaName}

# mm_ops_NillRows class attributes and methods
mm_ops_NillRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_NillRows_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_NillRows_columnName: Property = Property(name="columnName", type=StringType)
mm_ops_NillRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_NillRows.attributes={mm_ops_NillRows_owningSchemaName, mm_ops_NillRows_whereCondition, mm_ops_NillRows_tableName, mm_ops_NillRows_columnName}

# mm_ops_InsertRows class attributes and methods
mm_ops_InsertRows_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_InsertRows_sourceTableName: Property = Property(name="sourceTableName", type=StringType)
mm_ops_InsertRows_sourceColumnsNames: Property = Property(name="sourceColumnsNames", type=StringType)
mm_ops_InsertRows_whereCondition: Property = Property(name="whereCondition", type=StringType)
mm_ops_InsertRows_targetTableName: Property = Property(name="targetTableName", type=StringType)
mm_ops_InsertRows_targetColumnNames: Property = Property(name="targetColumnNames", type=StringType)
mm_ops_InsertRows.attributes={mm_ops_InsertRows_targetColumnNames, mm_ops_InsertRows_sourceTableName, mm_ops_InsertRows_sourceColumnsNames, mm_ops_InsertRows_owningSchemaName, mm_ops_InsertRows_targetTableName, mm_ops_InsertRows_whereCondition}

# mm_ops_GenerateSequenceNumbers class attributes and methods
mm_ops_GenerateSequenceNumbers_owningSchemaName: Property = Property(name="owningSchemaName", type=StringType)
mm_ops_GenerateSequenceNumbers_tableName: Property = Property(name="tableName", type=StringType)
mm_ops_GenerateSequenceNumbers_columnName: Property = Property(name="columnName", type=StringType)
mm_ops_GenerateSequenceNumbers_sequenceName: Property = Property(name="sequenceName", type=StringType)
mm_ops_GenerateSequenceNumbers.attributes={mm_ops_GenerateSequenceNumbers_owningSchemaName, mm_ops_GenerateSequenceNumbers_columnName, mm_ops_GenerateSequenceNumbers_tableName, mm_ops_GenerateSequenceNumbers_sequenceName}

# Relationships
sequence4: BinaryAssociation = BinaryAssociation(
    name="sequence4",
    ends={
        Property(name="owningSchema5", type=Sequence, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Sequence", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1))
    }
)
indexes6: BinaryAssociation = BinaryAssociation(
    name="indexes6",
    ends={
        Property(name="Index", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema7", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema8: BinaryAssociation = BinaryAssociation(
    name="owningSchema8",
    ends={
        Property(name="Schema9", type=mm_rdb_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="ModelOperation", type=mm_rdb_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperations", type=ops_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas1: BinaryAssociation = BinaryAssociation(
    name="schemas1",
    ends={
        Property(name="Schema", type=mm_rdb_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStructure", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningStructure2: BinaryAssociation = BinaryAssociation(
    name="owningStructure2",
    ends={
        Property(name="Structure", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schemas", type=Structure, multiplicity=Multiplicity(1, 1))
    }
)
uniqueColumns23: BinaryAssociation = BinaryAssociation(
    name="uniqueColumns23",
    ends={
        Property(name="Column24", type=mm_rdb_Unique, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Unique", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables3: BinaryAssociation = BinaryAssociation(
    name="tables3",
    ends={
        Property(name="Table", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainedColumn25: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn25",
    ends={
        Property(name="Column26", type=mm_rdb_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_PrimaryKey", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
targetTable27: BinaryAssociation = BinaryAssociation(
    name="targetTable27",
    ends={
        Property(name="Table28", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constrainedColumn29: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn29",
    ends={
        Property(name="Column31", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey30", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
owningSchema10: BinaryAssociation = BinaryAssociation(
    name="owningSchema10",
    ends={
        Property(name="Schema11", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="Column", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
owningSchema13: BinaryAssociation = BinaryAssociation(
    name="owningSchema13",
    ends={
        Property(name="Schema14", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns15: BinaryAssociation = BinaryAssociation(
    name="columns15",
    ends={
        Property(name="Column16", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints17: BinaryAssociation = BinaryAssociation(
    name="constraints17",
    ends={
        Property(name="TableConstraint", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable18", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTable19: BinaryAssociation = BinaryAssociation(
    name="owningTable19",
    ends={
        Property(name="Table20", type=mm_rdb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
owningTable21: BinaryAssociation = BinaryAssociation(
    name="owningTable21",
    ends={
        Property(name="Table22", type=mm_rdb_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
owningOperations32: BinaryAssociation = BinaryAssociation(
    name="owningOperations32",
    ends={
        Property(name="Operations", type=mm_ops_ModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=Operations, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mm_rdb_Operations_ModelRoot = Generalization(general=ModelRoot, specific=mm_rdb_Operations)
gen_mm_rdb_Structure_ModelRoot = Generalization(general=ModelRoot, specific=mm_rdb_Structure)
gen_mm_rdb_PrimaryKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_PrimaryKey)
gen_mm_rdb_ForeignKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_ForeignKey)
gen_mm_rdb_Unique_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_Unique)
gen_mm_ops_AddForeignKey_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddForeignKey)
gen_mm_ops_AddUnique_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddUnique)
gen_mm_ops_AddNotNull_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddNotNull)
gen_mm_ops_AddSchema_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddSchema)
gen_mm_ops_AddSequence_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddSequence)
gen_mm_ops_AddTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddTable)
gen_mm_ops_AddIndex_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddIndex)
gen_mm_ops_AddColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddColumn)
gen_mm_ops_AddPrimaryKey_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_AddPrimaryKey)
gen_mm_ops_RemoveDefaultValue_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveDefaultValue)
gen_mm_ops_RemoveTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveTable)
gen_mm_ops_RemoveColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveColumn)
gen_mm_ops_RemoveNotNull_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveNotNull)
gen_mm_ops_RenameTable_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RenameTable)
gen_mm_ops_RenameColumn_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RenameColumn)
gen_mm_ops_SetColumnType_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_SetColumnType)
gen_mm_ops_SetDefaultValue_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_SetDefaultValue)
gen_mm_ops_InsertRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_InsertRows)
gen_mm_ops_DeleteRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_DeleteRows)
gen_mm_ops_HasNoOwnInstances_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_HasNoOwnInstances)
gen_mm_ops_HasNoInstances_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_HasNoInstances)
gen_mm_ops_RemoveConstraint_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveConstraint)
gen_mm_ops_RemoveIndex_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveIndex)
gen_mm_ops_RemoveSequence_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_RemoveSequence)
gen_mm_ops_UpdateRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_UpdateRows)
gen_mm_ops_NillRows_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_NillRows)
gen_mm_ops_GenerateSequenceNumbers_ModelOperation = Generalization(general=ModelOperation, specific=mm_ops_GenerateSequenceNumbers)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={mm_rdb_ModelRoot, Index, mm_rdb_Sequence, mm_rdb_Index, mm_rdb_Operations, ModelRoot, ops_ModelOperation, mm_rdb_Structure, Schema, mm_rdb_Schema, Structure, Table, mm_rdb_PrimaryKey, Sequence, mm_rdb_ForeignKey, mm_ops_ModelOperation, Column, mm_rdb_Table, TableConstraint, mm_rdb_Column, mm_rdb_TableConstraint, mm_rdb_Unique, mm_ops_AddForeignKey, mm_ops_AddUnique, mm_ops_AddNotNull, Operations, mm_ops_AddSchema, ModelOperation, mm_ops_AddSequence, mm_ops_AddTable, mm_ops_AddIndex, mm_ops_AddColumn, mm_ops_AddPrimaryKey, mm_ops_RemoveDefaultValue, mm_ops_RemoveTable, mm_ops_RemoveColumn, mm_ops_RemoveNotNull, mm_ops_RenameTable, mm_ops_RenameColumn, mm_ops_SetColumnType, mm_ops_SetDefaultValue, mm_ops_DeleteRows, mm_ops_HasNoOwnInstances, mm_ops_HasNoInstances, mm_ops_RemoveConstraint, mm_ops_RemoveIndex, mm_ops_RemoveSequence, mm_ops_UpdateRows, mm_ops_NillRows, mm_ops_InsertRows, mm_ops_GenerateSequenceNumbers, PrimitiveType},
    associations={sequence4, indexes6, owningSchema8, operations0, schemas1, owningStructure2, uniqueColumns23, tables3, constrainedColumn25, targetTable27, constrainedColumn29, owningSchema10, columns12, owningSchema13, columns15, constraints17, owningTable19, owningTable21, owningOperations32},
    generalizations={gen_mm_rdb_Operations_ModelRoot, gen_mm_rdb_Structure_ModelRoot, gen_mm_rdb_PrimaryKey_TableConstraint, gen_mm_rdb_ForeignKey_TableConstraint, gen_mm_rdb_Unique_TableConstraint, gen_mm_ops_AddForeignKey_ModelOperation, gen_mm_ops_AddUnique_ModelOperation, gen_mm_ops_AddNotNull_ModelOperation, gen_mm_ops_AddSchema_ModelOperation, gen_mm_ops_AddSequence_ModelOperation, gen_mm_ops_AddTable_ModelOperation, gen_mm_ops_AddIndex_ModelOperation, gen_mm_ops_AddColumn_ModelOperation, gen_mm_ops_AddPrimaryKey_ModelOperation, gen_mm_ops_RemoveDefaultValue_ModelOperation, gen_mm_ops_RemoveTable_ModelOperation, gen_mm_ops_RemoveColumn_ModelOperation, gen_mm_ops_RemoveNotNull_ModelOperation, gen_mm_ops_RenameTable_ModelOperation, gen_mm_ops_RenameColumn_ModelOperation, gen_mm_ops_SetColumnType_ModelOperation, gen_mm_ops_SetDefaultValue_ModelOperation, gen_mm_ops_InsertRows_ModelOperation, gen_mm_ops_DeleteRows_ModelOperation, gen_mm_ops_HasNoOwnInstances_ModelOperation, gen_mm_ops_HasNoInstances_ModelOperation, gen_mm_ops_RemoveConstraint_ModelOperation, gen_mm_ops_RemoveIndex_ModelOperation, gen_mm_ops_RemoveSequence_ModelOperation, gen_mm_ops_UpdateRows_ModelOperation, gen_mm_ops_NillRows_ModelOperation, gen_mm_ops_GenerateSequenceNumbers_ModelOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)