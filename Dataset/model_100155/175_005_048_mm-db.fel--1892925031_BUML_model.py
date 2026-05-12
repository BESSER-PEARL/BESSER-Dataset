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
Operation = Class(name="Operation")
mm_rdb_NamedElement = Class(name="mm_rdb_NamedElement", is_abstract=True)
mm_rdb_Database = Class(name="mm_rdb_Database")
NamedElement = Class(name="NamedElement")
Schema = Class(name="Schema")
mm_rdb_DbObject = Class(name="mm_rdb_DbObject", is_abstract=True)
mm_rdb_Schema = Class(name="mm_rdb_Schema")
DbObject = Class(name="DbObject")
Table = Class(name="Table")
Sequence = Class(name="Sequence")
mm_rdb_ModelRoot = Class(name="mm_rdb_ModelRoot")
Database = Class(name="Database")
TableConstraint = Class(name="TableConstraint")
mm_rdb_Sequence = Class(name="mm_rdb_Sequence")
mm_rdb_Constraint = Class(name="mm_rdb_Constraint", is_abstract=True)
mm_rdb_TableConstraint = Class(name="mm_rdb_TableConstraint", is_abstract=True)
rdb_Constraint = Class(name="rdb_Constraint")
rdb_NamedElement = Class(name="rdb_NamedElement")
Index = Class(name="Index")
mm_rdb_Relation = Class(name="mm_rdb_Relation", is_abstract=True)
mm_rdb_Table = Class(name="mm_rdb_Table")
rdb_DbObject = Class(name="rdb_DbObject")
rdb_Relation = Class(name="rdb_Relation")
PrimaryKey = Class(name="PrimaryKey")
mm_rdb_Index = Class(name="mm_rdb_Index")
TableColumn = Class(name="TableColumn")
mm_rdb_ColumnConstraint = Class(name="mm_rdb_ColumnConstraint", is_abstract=True)
Constraint = Class(name="Constraint")
mm_rdb_ForeignKey = Class(name="mm_rdb_ForeignKey")
mm_rdb_Column = Class(name="mm_rdb_Column", is_abstract=True)
mm_rdb_TableColumn = Class(name="mm_rdb_TableColumn")
Column = Class(name="Column")
ColumnConstraint = Class(name="ColumnConstraint")
mm_rdb_DeleteTable = Class(name="mm_rdb_DeleteTable")
mm_rdb_AddColumn = Class(name="mm_rdb_AddColumn")
mm_rdb_UniqueIndex = Class(name="mm_rdb_UniqueIndex")
mm_rdb_PrimaryKey = Class(name="mm_rdb_PrimaryKey")
UniqueIndex = Class(name="UniqueIndex")
mm_rdb_Operation = Class(name="mm_rdb_Operation", is_abstract=True)
ModelRoot = Class(name="ModelRoot")
mm_rdb_CreateTable = Class(name="mm_rdb_CreateTable")
mm_rdb_RenameTable = Class(name="mm_rdb_RenameTable")
mm_rdb_DeleteColumn = Class(name="mm_rdb_DeleteColumn")
mm_rdb_RenameColumn = Class(name="mm_rdb_RenameColumn")
mm_rdb_TypeChangeToColumn = Class(name="mm_rdb_TypeChangeToColumn")
mm_dml_Query = Class(name="mm_dml_Query")
Relation = Class(name="Relation")
dml_ColumnReference = Class(name="dml_ColumnReference")
mm_dml_ColumnReference = Class(name="mm_dml_ColumnReference")

# Operation class attributes and methods

# mm_rdb_NamedElement class attributes and methods
mm_rdb_NamedElement_name: Property = Property(name="name", type=StringType)
mm_rdb_NamedElement.attributes={mm_rdb_NamedElement_name}

# mm_rdb_Database class attributes and methods

# NamedElement class attributes and methods

# Schema class attributes and methods

# mm_rdb_DbObject class attributes and methods

# mm_rdb_Schema class attributes and methods

# DbObject class attributes and methods

# Table class attributes and methods

# Sequence class attributes and methods

# mm_rdb_ModelRoot class attributes and methods

# Database class attributes and methods

# TableConstraint class attributes and methods

# mm_rdb_Sequence class attributes and methods
mm_rdb_Sequence_cacheSize: Property = Property(name="cacheSize", type=IntegerType)
mm_rdb_Sequence.attributes={mm_rdb_Sequence_cacheSize}

# mm_rdb_Constraint class attributes and methods

# mm_rdb_TableConstraint class attributes and methods

# rdb_Constraint class attributes and methods

# rdb_NamedElement class attributes and methods

# Index class attributes and methods

# mm_rdb_Relation class attributes and methods
mm_rdb_Relation_m_getColumns: Method = Method(name="getColumns", parameters={}, type=StringType)
mm_rdb_Relation.methods={mm_rdb_Relation_m_getColumns}

# mm_rdb_Table class attributes and methods
mm_rdb_Table_m_getPrimaryColumn: Method = Method(name="getPrimaryColumn", parameters={}, type=StringType)
mm_rdb_Table_m_getColumns: Method = Method(name="getColumns", parameters={}, type=StringType)
mm_rdb_Table.methods={mm_rdb_Table_m_getColumns, mm_rdb_Table_m_getPrimaryColumn}

# rdb_DbObject class attributes and methods

# rdb_Relation class attributes and methods

# PrimaryKey class attributes and methods

# mm_rdb_Index class attributes and methods

# TableColumn class attributes and methods

# mm_rdb_ColumnConstraint class attributes and methods

# Constraint class attributes and methods

# mm_rdb_ForeignKey class attributes and methods

# mm_rdb_Column class attributes and methods
mm_rdb_Column_m_getOwningTable: Method = Method(name="getOwningTable", parameters={}, type=StringType)
mm_rdb_Column.methods={mm_rdb_Column_m_getOwningTable}

# mm_rdb_TableColumn class attributes and methods
mm_rdb_TableColumn_type: Property = Property(name="type", type=StringType)
mm_rdb_TableColumn_m_getOwningTable: Method = Method(name="getOwningTable", parameters={}, type=StringType)
mm_rdb_TableColumn.attributes={mm_rdb_TableColumn_type}
mm_rdb_TableColumn.methods={mm_rdb_TableColumn_m_getOwningTable}

# Column class attributes and methods

# ColumnConstraint class attributes and methods

# mm_rdb_DeleteTable class attributes and methods
mm_rdb_DeleteTable_m_deleteTable: Method = Method(name="deleteTable", parameters={Parameter(name='mm_deletedTable', type=StringType)}, type=BooleanType)
mm_rdb_DeleteTable.methods={mm_rdb_DeleteTable_m_deleteTable}

# mm_rdb_AddColumn class attributes and methods
mm_rdb_AddColumn_newColumnName: Property = Property(name="newColumnName", type=StringType)
mm_rdb_AddColumn_m_addColumn: Method = Method(name="addColumn", parameters={Parameter(name='mm_changedTable', type=StringType), Parameter(name='mm_newColumnName', type=StringType), Parameter(name='mm_columnConstrains', type=StringType)}, type=BooleanType)
mm_rdb_AddColumn.attributes={mm_rdb_AddColumn_newColumnName}
mm_rdb_AddColumn.methods={mm_rdb_AddColumn_m_addColumn}

# mm_rdb_UniqueIndex class attributes and methods

# mm_rdb_PrimaryKey class attributes and methods

# UniqueIndex class attributes and methods

# mm_rdb_Operation class attributes and methods

# ModelRoot class attributes and methods

# mm_rdb_CreateTable class attributes and methods
mm_rdb_CreateTable_tableName: Property = Property(name="tableName", type=StringType)
mm_rdb_CreateTable_m_createTable: Method = Method(name="createTable", parameters={Parameter(name='mm_tableConstraints', type=StringType), Parameter(name='mm_generateID', type=StringType), Parameter(name='mm_tableName', type=StringType), Parameter(name='mm_tableColumns', type=StringType), Parameter(name='mm_primaryKey', type=StringType)}, type=BooleanType)
mm_rdb_CreateTable.attributes={mm_rdb_CreateTable_tableName}
mm_rdb_CreateTable.methods={mm_rdb_CreateTable_m_createTable}

# mm_rdb_RenameTable class attributes and methods
mm_rdb_RenameTable_newName: Property = Property(name="newName", type=StringType)
mm_rdb_RenameTable_m_renameTable: Method = Method(name="renameTable", parameters={Parameter(name='mm_newName', type=StringType), Parameter(name='mm_renamedTable', type=StringType)}, type=BooleanType)
mm_rdb_RenameTable.attributes={mm_rdb_RenameTable_newName}
mm_rdb_RenameTable.methods={mm_rdb_RenameTable_m_renameTable}

# mm_rdb_DeleteColumn class attributes and methods
mm_rdb_DeleteColumn_m_deleteColumn: Method = Method(name="deleteColumn", parameters={Parameter(name='mm_changedTable', type=StringType), Parameter(name='mm_deleteColumn', type=StringType)}, type=BooleanType)
mm_rdb_DeleteColumn.methods={mm_rdb_DeleteColumn_m_deleteColumn}

# mm_rdb_RenameColumn class attributes and methods
mm_rdb_RenameColumn_newColumnName: Property = Property(name="newColumnName", type=StringType)
mm_rdb_RenameColumn_m_renameColumn: Method = Method(name="renameColumn", parameters={Parameter(name='mm_changedTable', type=StringType), Parameter(name='mm_newColumnName', type=StringType), Parameter(name='mm_renamedColumn', type=StringType)}, type=BooleanType)
mm_rdb_RenameColumn.attributes={mm_rdb_RenameColumn_newColumnName}
mm_rdb_RenameColumn.methods={mm_rdb_RenameColumn_m_renameColumn}

# mm_rdb_TypeChangeToColumn class attributes and methods
mm_rdb_TypeChangeToColumn_newType: Property = Property(name="newType", type=StringType)
mm_rdb_TypeChangeToColumn_m_typeChangeToColumn: Method = Method(name="typeChangeToColumn", parameters={Parameter(name='mm_newType', type=StringType), Parameter(name='mm_changedTable', type=StringType), Parameter(name='mm_changedTypeColumn', type=StringType)}, type=BooleanType)
mm_rdb_TypeChangeToColumn.attributes={mm_rdb_TypeChangeToColumn_newType}
mm_rdb_TypeChangeToColumn.methods={mm_rdb_TypeChangeToColumn_m_typeChangeToColumn}

# mm_dml_Query class attributes and methods

# Relation class attributes and methods

# dml_ColumnReference class attributes and methods

# mm_dml_ColumnReference class attributes and methods

# Relationships
targetDB1: BinaryAssociation = BinaryAssociation(
    name="targetDB1",
    ends={
        Property(name="mm_rdb_ModelRoot2", type=Database, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Database3", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1))
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="Operation", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="modelRoot", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas5: BinaryAssociation = BinaryAssociation(
    name="schemas5",
    ends={
        Property(name="Schema", type=mm_rdb_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Database", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables6: BinaryAssociation = BinaryAssociation(
    name="tables6",
    ends={
        Property(name="Table", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequences7: BinaryAssociation = BinaryAssociation(
    name="sequences7",
    ends={
        Property(name="Sequence", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema8", type=Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceDB0: BinaryAssociation = BinaryAssociation(
    name="sourceDB0",
    ends={
        Property(name="Database", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ModelRoot", type=Database, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints15: BinaryAssociation = BinaryAssociation(
    name="constraints15",
    ends={
        Property(name="TableConstraint", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema16: BinaryAssociation = BinaryAssociation(
    name="owningSchema16",
    ends={
        Property(name="Schema17", type=mm_rdb_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="sequences", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningTable18: BinaryAssociation = BinaryAssociation(
    name="owningTable18",
    ends={
        Property(name="Table19", type=mm_rdb_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
indexes9: BinaryAssociation = BinaryAssociation(
    name="indexes9",
    ends={
        Property(name="Index", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema10", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema11: BinaryAssociation = BinaryAssociation(
    name="owningSchema11",
    ends={
        Property(name="Schema12", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
primaryKey13: BinaryAssociation = BinaryAssociation(
    name="primaryKey13",
    ends={
        Property(name="PrimaryKey", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Table", type=PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
ownedColumns14: BinaryAssociation = BinaryAssociation(
    name="ownedColumns14",
    ends={
        Property(name="TableColumn", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="_owningTable", type=TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns31: BinaryAssociation = BinaryAssociation(
    name="columns31",
    ends={
        Property(name="TableColumn32", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index", type=TableColumn, multiplicity=Multiplicity(1, 9999))
    }
)
indexedTable33: BinaryAssociation = BinaryAssociation(
    name="indexedTable33",
    ends={
        Property(name="Table35", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index34", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
owningSchema36: BinaryAssociation = BinaryAssociation(
    name="owningSchema36",
    ends={
        Property(name="Schema37", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningColumn20: BinaryAssociation = BinaryAssociation(
    name="owningColumn20",
    ends={
        Property(name="TableColumn22", type=mm_rdb_ColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints21", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
targetTable23: BinaryAssociation = BinaryAssociation(
    name="targetTable23",
    ends={
        Property(name="Table24", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constrainedColumn25: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn25",
    ends={
        Property(name="TableColumn27", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey26", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
_owningTable28: BinaryAssociation = BinaryAssociation(
    name="_owningTable28",
    ends={
        Property(name="Table29", type=mm_rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedColumns", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constraints30: BinaryAssociation = BinaryAssociation(
    name="constraints30",
    ends={
        Property(name="ColumnConstraint", type=mm_rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="owningColumn", type=ColumnConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renamedTable52: BinaryAssociation = BinaryAssociation(
    name="renamedTable52",
    ends={
        Property(name="Table53", type=mm_rdb_RenameTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameTable", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
deletedTable54: BinaryAssociation = BinaryAssociation(
    name="deletedTable54",
    ends={
        Property(name="Table55", type=mm_rdb_DeleteTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteTable", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
underlyingIndex38: BinaryAssociation = BinaryAssociation(
    name="underlyingIndex38",
    ends={
        Property(name="Index39", type=mm_rdb_UniqueIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_UniqueIndex", type=Index, multiplicity=Multiplicity(1, 1))
    }
)
modelRoot40: BinaryAssociation = BinaryAssociation(
    name="modelRoot40",
    ends={
        Property(name="ModelRoot", type=mm_rdb_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=ModelRoot, multiplicity=Multiplicity(1, 1))
    }
)
tableColumns41: BinaryAssociation = BinaryAssociation(
    name="tableColumns41",
    ends={
        Property(name="TableColumn42", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable", type=TableColumn, multiplicity=Multiplicity(0, 9999))
    }
)
tableConstraints43: BinaryAssociation = BinaryAssociation(
    name="tableConstraints43",
    ends={
        Property(name="TableConstraint45", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable44", type=TableConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey46: BinaryAssociation = BinaryAssociation(
    name="primaryKey46",
    ends={
        Property(name="PrimaryKey48", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable47", type=PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
generateID49: BinaryAssociation = BinaryAssociation(
    name="generateID49",
    ends={
        Property(name="Sequence51", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable50", type=Sequence, multiplicity=Multiplicity(1, 1))
    }
)
changedTypeColumn68: BinaryAssociation = BinaryAssociation(
    name="changedTypeColumn68",
    ends={
        Property(name="TableColumn70", type=mm_rdb_TypeChangeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_TypeChangeToColumn69", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
changedTable71: BinaryAssociation = BinaryAssociation(
    name="changedTable71",
    ends={
        Property(name="Table72", type=mm_rdb_DeleteColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
deleteColumn73: BinaryAssociation = BinaryAssociation(
    name="deleteColumn73",
    ends={
        Property(name="TableColumn75", type=mm_rdb_DeleteColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteColumn74", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
changedTable56: BinaryAssociation = BinaryAssociation(
    name="changedTable56",
    ends={
        Property(name="Table57", type=mm_rdb_AddColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_AddColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
columnConstrains58: BinaryAssociation = BinaryAssociation(
    name="columnConstrains58",
    ends={
        Property(name="ColumnConstraint60", type=mm_rdb_AddColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_AddColumn59", type=ColumnConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
changedTable61: BinaryAssociation = BinaryAssociation(
    name="changedTable61",
    ends={
        Property(name="Table62", type=mm_rdb_RenameColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
renamedColumn63: BinaryAssociation = BinaryAssociation(
    name="renamedColumn63",
    ends={
        Property(name="TableColumn65", type=mm_rdb_RenameColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameColumn64", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
changedTable66: BinaryAssociation = BinaryAssociation(
    name="changedTable66",
    ends={
        Property(name="Table67", type=mm_rdb_TypeChangeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_TypeChangeToColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
columnReferences76: BinaryAssociation = BinaryAssociation(
    name="columnReferences76",
    ends={
        Property(name="dml_ColumnReference", type=mm_dml_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_dml_Query", type=dml_ColumnReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reference77: BinaryAssociation = BinaryAssociation(
    name="reference77",
    ends={
        Property(name="Column", type=mm_dml_ColumnReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_dml_ColumnReference", type=Column, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mm_rdb_Database_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_Database)
gen_mm_rdb_DbObject_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_DbObject)
gen_mm_rdb_Schema_DbObject = Generalization(general=DbObject, specific=mm_rdb_Schema)
gen_mm_rdb_Sequence_DbObject = Generalization(general=DbObject, specific=mm_rdb_Sequence)
gen_mm_rdb_Constraint_DbObject = Generalization(general=DbObject, specific=mm_rdb_Constraint)
gen_mm_rdb_TableConstraint_rdb_Constraint = Generalization(general=rdb_Constraint, specific=mm_rdb_TableConstraint)
gen_mm_rdb_TableConstraint_rdb_NamedElement = Generalization(general=rdb_NamedElement, specific=mm_rdb_TableConstraint)
gen_mm_rdb_Table_rdb_DbObject = Generalization(general=rdb_DbObject, specific=mm_rdb_Table)
gen_mm_rdb_Table_rdb_Relation = Generalization(general=rdb_Relation, specific=mm_rdb_Table)
gen_mm_rdb_Index_DbObject = Generalization(general=DbObject, specific=mm_rdb_Index)
gen_mm_rdb_ColumnConstraint_Constraint = Generalization(general=Constraint, specific=mm_rdb_ColumnConstraint)
gen_mm_rdb_ForeignKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_ForeignKey)
gen_mm_rdb_Column_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_Column)
gen_mm_rdb_TableColumn_Column = Generalization(general=Column, specific=mm_rdb_TableColumn)
gen_mm_rdb_DeleteTable_Operation = Generalization(general=Operation, specific=mm_rdb_DeleteTable)
gen_mm_rdb_AddColumn_Operation = Generalization(general=Operation, specific=mm_rdb_AddColumn)
gen_mm_rdb_UniqueIndex_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_UniqueIndex)
gen_mm_rdb_PrimaryKey_UniqueIndex = Generalization(general=UniqueIndex, specific=mm_rdb_PrimaryKey)
gen_mm_rdb_CreateTable_Operation = Generalization(general=Operation, specific=mm_rdb_CreateTable)
gen_mm_rdb_RenameTable_Operation = Generalization(general=Operation, specific=mm_rdb_RenameTable)
gen_mm_rdb_DeleteColumn_Operation = Generalization(general=Operation, specific=mm_rdb_DeleteColumn)
gen_mm_rdb_RenameColumn_Operation = Generalization(general=Operation, specific=mm_rdb_RenameColumn)
gen_mm_rdb_TypeChangeToColumn_Operation = Generalization(general=Operation, specific=mm_rdb_TypeChangeToColumn)
gen_mm_dml_Query_Relation = Generalization(general=Relation, specific=mm_dml_Query)
gen_mm_dml_ColumnReference_Column = Generalization(general=Column, specific=mm_dml_ColumnReference)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={Operation, mm_rdb_NamedElement, mm_rdb_Database, NamedElement, Schema, mm_rdb_DbObject, mm_rdb_Schema, DbObject, Table, Sequence, mm_rdb_ModelRoot, Database, TableConstraint, mm_rdb_Sequence, mm_rdb_Constraint, mm_rdb_TableConstraint, rdb_Constraint, rdb_NamedElement, Index, mm_rdb_Relation, mm_rdb_Table, rdb_DbObject, rdb_Relation, PrimaryKey, mm_rdb_Index, TableColumn, mm_rdb_ColumnConstraint, Constraint, mm_rdb_ForeignKey, mm_rdb_Column, mm_rdb_TableColumn, Column, ColumnConstraint, mm_rdb_DeleteTable, mm_rdb_AddColumn, mm_rdb_UniqueIndex, mm_rdb_PrimaryKey, UniqueIndex, mm_rdb_Operation, ModelRoot, mm_rdb_CreateTable, mm_rdb_RenameTable, mm_rdb_DeleteColumn, mm_rdb_RenameColumn, mm_rdb_TypeChangeToColumn, mm_dml_Query, Relation, dml_ColumnReference, mm_dml_ColumnReference},
    associations={targetDB1, operations4, schemas5, tables6, sequences7, sourceDB0, constraints15, owningSchema16, owningTable18, indexes9, owningSchema11, primaryKey13, ownedColumns14, columns31, indexedTable33, owningSchema36, owningColumn20, targetTable23, constrainedColumn25, _owningTable28, constraints30, renamedTable52, deletedTable54, underlyingIndex38, modelRoot40, tableColumns41, tableConstraints43, primaryKey46, generateID49, changedTypeColumn68, changedTable71, deleteColumn73, changedTable56, columnConstrains58, changedTable61, renamedColumn63, changedTable66, columnReferences76, reference77},
    generalizations={gen_mm_rdb_Database_NamedElement, gen_mm_rdb_DbObject_NamedElement, gen_mm_rdb_Schema_DbObject, gen_mm_rdb_Sequence_DbObject, gen_mm_rdb_Constraint_DbObject, gen_mm_rdb_TableConstraint_rdb_Constraint, gen_mm_rdb_TableConstraint_rdb_NamedElement, gen_mm_rdb_Table_rdb_DbObject, gen_mm_rdb_Table_rdb_Relation, gen_mm_rdb_Index_DbObject, gen_mm_rdb_ColumnConstraint_Constraint, gen_mm_rdb_ForeignKey_TableConstraint, gen_mm_rdb_Column_NamedElement, gen_mm_rdb_TableColumn_Column, gen_mm_rdb_DeleteTable_Operation, gen_mm_rdb_AddColumn_Operation, gen_mm_rdb_UniqueIndex_TableConstraint, gen_mm_rdb_PrimaryKey_UniqueIndex, gen_mm_rdb_CreateTable_Operation, gen_mm_rdb_RenameTable_Operation, gen_mm_rdb_DeleteColumn_Operation, gen_mm_rdb_RenameColumn_Operation, gen_mm_rdb_TypeChangeToColumn_Operation, gen_mm_dml_Query_Relation, gen_mm_dml_ColumnReference_Column},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)