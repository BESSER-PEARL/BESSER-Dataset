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
mm_rdb_ModelRoot = Class(name="mm::rdb::ModelRoot")
Database = Class(name="Database")
Operation = Class(name="Operation")
mm_rdb_NamedElement = Class(name="mm::rdb::NamedElement", is_abstract=True)
mm_rdb_Database = Class(name="mm::rdb::Database")
NamedElement = Class(name="NamedElement")
Sequence = Class(name="Sequence")
Index = Class(name="Index")
Schema = Class(name="Schema")
mm_rdb_DbObject = Class(name="mm::rdb::DbObject", is_abstract=True)
mm_rdb_Schema = Class(name="mm::rdb::Schema")
DbObject = Class(name="DbObject")
Table = Class(name="Table")
PrimaryKey = Class(name="PrimaryKey")
mm_rdb_Relation = Class(name="mm::rdb::Relation", is_abstract=True)
mm_rdb_Table = Class(name="mm::rdb::Table")
rdb_DbObject = Class(name="rdb::DbObject")
rdb_Relation = Class(name="rdb::Relation")
mm_rdb_Constraint = Class(name="mm::rdb::Constraint", is_abstract=True)
mm_rdb_TableConstraint = Class(name="mm::rdb::TableConstraint", is_abstract=True)
rdb_Constraint = Class(name="rdb::Constraint")
rdb_NamedElement = Class(name="rdb::NamedElement")
TableColumn = Class(name="TableColumn")
TableConstraint = Class(name="TableConstraint")
mm_rdb_Sequence = Class(name="mm::rdb::Sequence")
mm_rdb_Column = Class(name="mm::rdb::Column", is_abstract=True)
mm_rdb_ColumnConstraint = Class(name="mm::rdb::ColumnConstraint", is_abstract=True)
Constraint = Class(name="Constraint")
mm_rdb_ForeignKey = Class(name="mm::rdb::ForeignKey")
mm_rdb_Index = Class(name="mm::rdb::Index")
mm_rdb_TableColumn = Class(name="mm::rdb::TableColumn")
Column = Class(name="Column")
ColumnConstraint = Class(name="ColumnConstraint")
mm_rdb_PrimaryKey = Class(name="mm::rdb::PrimaryKey")
UniqueIndex = Class(name="UniqueIndex")
mm_rdb_Operation = Class(name="mm::rdb::Operation", is_abstract=True)
ModelRoot = Class(name="ModelRoot")
mm_rdb_UniqueIndex = Class(name="mm::rdb::UniqueIndex")
mm_rdb_CreateTable = Class(name="mm::rdb::CreateTable")
mm_rdb_DeleteTable = Class(name="mm::rdb::DeleteTable")
mm_rdb_AddColumn = Class(name="mm::rdb::AddColumn")
mm_rdb_RenameTable = Class(name="mm::rdb::RenameTable")
mm_rdb_RenameColumn = Class(name="mm::rdb::RenameColumn")
mm_rdb_DeleteColumn = Class(name="mm::rdb::DeleteColumn")
mm_rdb_TypeChangeToColumn = Class(name="mm::rdb::TypeChangeToColumn")
mm_dml_Query = Class(name="mm::dml::Query")
Relation = Class(name="Relation")
dml_ColumnReference = Class(name="dml::ColumnReference")
mm_dml_ColumnReference = Class(name="mm::dml::ColumnReference")

# mm_rdb_ModelRoot class attributes and methods

# Database class attributes and methods

# Operation class attributes and methods

# mm_rdb_NamedElement class attributes and methods
mm_rdb_NamedElement_name: Property = Property(name="name", type=StringType)
mm_rdb_NamedElement.attributes={mm_rdb_NamedElement_name}

# mm_rdb_Database class attributes and methods

# NamedElement class attributes and methods

# Sequence class attributes and methods

# Index class attributes and methods

# Schema class attributes and methods

# mm_rdb_DbObject class attributes and methods

# mm_rdb_Schema class attributes and methods

# DbObject class attributes and methods

# Table class attributes and methods

# PrimaryKey class attributes and methods

# mm_rdb_Relation class attributes and methods
mm_rdb_Relation_m_getColumns: Method = Method(name="getColumns", parameters={}, type=StringType)
mm_rdb_Relation.methods={mm_rdb_Relation_m_getColumns}

# mm_rdb_Table class attributes and methods
mm_rdb_Table_m_getColumns: Method = Method(name="getColumns", parameters={}, type=StringType)
mm_rdb_Table_m_getPrimaryColumn: Method = Method(name="getPrimaryColumn", parameters={}, type=StringType)
mm_rdb_Table.methods={mm_rdb_Table_m_getPrimaryColumn, mm_rdb_Table_m_getColumns}

# rdb_DbObject class attributes and methods

# rdb_Relation class attributes and methods

# mm_rdb_Constraint class attributes and methods

# mm_rdb_TableConstraint class attributes and methods

# rdb_Constraint class attributes and methods

# rdb_NamedElement class attributes and methods

# TableColumn class attributes and methods

# TableConstraint class attributes and methods

# mm_rdb_Sequence class attributes and methods
mm_rdb_Sequence_cacheSize: Property = Property(name="cacheSize", type=IntegerType)
mm_rdb_Sequence.attributes={mm_rdb_Sequence_cacheSize}

# mm_rdb_Column class attributes and methods
mm_rdb_Column_m_getOwningTable: Method = Method(name="getOwningTable", parameters={}, type=StringType)
mm_rdb_Column.methods={mm_rdb_Column_m_getOwningTable}

# mm_rdb_ColumnConstraint class attributes and methods

# Constraint class attributes and methods

# mm_rdb_ForeignKey class attributes and methods

# mm_rdb_Index class attributes and methods

# mm_rdb_TableColumn class attributes and methods
mm_rdb_TableColumn_type: Property = Property(name="type", type=StringType)
mm_rdb_TableColumn_m_getOwningTable: Method = Method(name="getOwningTable", parameters={}, type=StringType)
mm_rdb_TableColumn.attributes={mm_rdb_TableColumn_type}
mm_rdb_TableColumn.methods={mm_rdb_TableColumn_m_getOwningTable}

# Column class attributes and methods

# ColumnConstraint class attributes and methods

# mm_rdb_PrimaryKey class attributes and methods

# UniqueIndex class attributes and methods

# mm_rdb_Operation class attributes and methods

# ModelRoot class attributes and methods

# mm_rdb_UniqueIndex class attributes and methods

# mm_rdb_CreateTable class attributes and methods
mm_rdb_CreateTable_tableName: Property = Property(name="tableName", type=StringType)
mm_rdb_CreateTable_m_createTable: Method = Method(name="createTable", parameters={Parameter(name='tableName'), Parameter(name='generateID'), Parameter(name='tableConstraints'), Parameter(name='tableColumns'), Parameter(name='primaryKey')}, type=BooleanType)
mm_rdb_CreateTable.attributes={mm_rdb_CreateTable_tableName}
mm_rdb_CreateTable.methods={mm_rdb_CreateTable_m_createTable}

# mm_rdb_DeleteTable class attributes and methods
mm_rdb_DeleteTable_m_deleteTable: Method = Method(name="deleteTable", parameters={Parameter(name='deletedTable')}, type=BooleanType)
mm_rdb_DeleteTable.methods={mm_rdb_DeleteTable_m_deleteTable}

# mm_rdb_AddColumn class attributes and methods
mm_rdb_AddColumn_newColumnName: Property = Property(name="newColumnName", type=StringType)
mm_rdb_AddColumn_m_addColumn: Method = Method(name="addColumn", parameters={Parameter(name='newColumnName'), Parameter(name='columnConstrains'), Parameter(name='changedTable')}, type=BooleanType)
mm_rdb_AddColumn.attributes={mm_rdb_AddColumn_newColumnName}
mm_rdb_AddColumn.methods={mm_rdb_AddColumn_m_addColumn}

# mm_rdb_RenameTable class attributes and methods
mm_rdb_RenameTable_newName: Property = Property(name="newName", type=StringType)
mm_rdb_RenameTable_m_renameTable: Method = Method(name="renameTable", parameters={Parameter(name='renamedTable'), Parameter(name='newName')}, type=BooleanType)
mm_rdb_RenameTable.attributes={mm_rdb_RenameTable_newName}
mm_rdb_RenameTable.methods={mm_rdb_RenameTable_m_renameTable}

# mm_rdb_RenameColumn class attributes and methods
mm_rdb_RenameColumn_newColumnName: Property = Property(name="newColumnName", type=StringType)
mm_rdb_RenameColumn_m_renameColumn: Method = Method(name="renameColumn", parameters={Parameter(name='changedTable'), Parameter(name='renamedColumn'), Parameter(name='newColumnName')}, type=BooleanType)
mm_rdb_RenameColumn.attributes={mm_rdb_RenameColumn_newColumnName}
mm_rdb_RenameColumn.methods={mm_rdb_RenameColumn_m_renameColumn}

# mm_rdb_DeleteColumn class attributes and methods
mm_rdb_DeleteColumn_m_deleteColumn: Method = Method(name="deleteColumn", parameters={Parameter(name='deleteColumn'), Parameter(name='changedTable')}, type=BooleanType)
mm_rdb_DeleteColumn.methods={mm_rdb_DeleteColumn_m_deleteColumn}

# mm_rdb_TypeChangeToColumn class attributes and methods
mm_rdb_TypeChangeToColumn_newType: Property = Property(name="newType", type=StringType)
mm_rdb_TypeChangeToColumn_m_typeChangeToColumn: Method = Method(name="typeChangeToColumn", parameters={Parameter(name='changedTable'), Parameter(name='newType'), Parameter(name='changedTypeColumn')}, type=BooleanType)
mm_rdb_TypeChangeToColumn.attributes={mm_rdb_TypeChangeToColumn_newType}
mm_rdb_TypeChangeToColumn.methods={mm_rdb_TypeChangeToColumn_m_typeChangeToColumn}

# mm_dml_Query class attributes and methods

# Relation class attributes and methods

# dml_ColumnReference class attributes and methods

# mm_dml_ColumnReference class attributes and methods

# Relationships
sourceDB0: BinaryAssociation = BinaryAssociation(
    name="sourceDB0",
    ends={
        Property(name="Database", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ModelRoot", type=Database, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="rdb", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetDB1: BinaryAssociation = BinaryAssociation(
    name="targetDB1",
    ends={
        Property(name="Database3", type=mm_rdb_ModelRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ModelRoot2", type=Database, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tables6: BinaryAssociation = BinaryAssociation(
    name="tables6",
    ends={
        Property(name="Table", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="rdb7", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1))
    }
)
sequences8: BinaryAssociation = BinaryAssociation(
    name="sequences8",
    ends={
        Property(name="rdb9", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Sequence", type=Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes10: BinaryAssociation = BinaryAssociation(
    name="indexes10",
    ends={
        Property(name="rdb11", type=mm_rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Index", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas5: BinaryAssociation = BinaryAssociation(
    name="schemas5",
    ends={
        Property(name="Schema", type=mm_rdb_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Database", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema12: BinaryAssociation = BinaryAssociation(
    name="owningSchema12",
    ends={
        Property(name="rdb14", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema13", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
primaryKey15: BinaryAssociation = BinaryAssociation(
    name="primaryKey15",
    ends={
        Property(name="PrimaryKey", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Table", type=PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
owningSchema20: BinaryAssociation = BinaryAssociation(
    name="owningSchema20",
    ends={
        Property(name="rdb22", type=mm_rdb_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema21", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningTable23: BinaryAssociation = BinaryAssociation(
    name="owningTable23",
    ends={
        Property(name="rdb25", type=mm_rdb_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Table24", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
ownedColumns16: BinaryAssociation = BinaryAssociation(
    name="ownedColumns16",
    ends={
        Property(name="rdb17", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableColumn", type=TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints18: BinaryAssociation = BinaryAssociation(
    name="constraints18",
    ends={
        Property(name="rdb19", type=mm_rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableConstraint", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetTable29: BinaryAssociation = BinaryAssociation(
    name="targetTable29",
    ends={
        Property(name="Table30", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constrainedColumn31: BinaryAssociation = BinaryAssociation(
    name="constrainedColumn31",
    ends={
        Property(name="TableColumn33", type=mm_rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_ForeignKey32", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
owningColumn26: BinaryAssociation = BinaryAssociation(
    name="owningColumn26",
    ends={
        Property(name="rdb28", type=mm_rdb_ColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="TableColumn27", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
columns39: BinaryAssociation = BinaryAssociation(
    name="columns39",
    ends={
        Property(name="TableColumn40", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index", type=TableColumn, multiplicity=Multiplicity(1, 9999))
    }
)
_owningTable34: BinaryAssociation = BinaryAssociation(
    name="_owningTable34",
    ends={
        Property(name="rdb36", type=mm_rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="Table35", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constraints37: BinaryAssociation = BinaryAssociation(
    name="constraints37",
    ends={
        Property(name="rdb38", type=mm_rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="ColumnConstraint", type=ColumnConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
underlyingIndex47: BinaryAssociation = BinaryAssociation(
    name="underlyingIndex47",
    ends={
        Property(name="Index48", type=mm_rdb_UniqueIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_UniqueIndex", type=Index, multiplicity=Multiplicity(1, 1))
    }
)
modelRoot49: BinaryAssociation = BinaryAssociation(
    name="modelRoot49",
    ends={
        Property(name="rdb50", type=mm_rdb_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelRoot", type=ModelRoot, multiplicity=Multiplicity(1, 1))
    }
)
indexedTable41: BinaryAssociation = BinaryAssociation(
    name="indexedTable41",
    ends={
        Property(name="Table43", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_Index42", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
owningSchema44: BinaryAssociation = BinaryAssociation(
    name="owningSchema44",
    ends={
        Property(name="rdb46", type=mm_rdb_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema45", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
tableColumns51: BinaryAssociation = BinaryAssociation(
    name="tableColumns51",
    ends={
        Property(name="TableColumn52", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable", type=TableColumn, multiplicity=Multiplicity(0, 9999))
    }
)
tableConstraints53: BinaryAssociation = BinaryAssociation(
    name="tableConstraints53",
    ends={
        Property(name="TableConstraint55", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable54", type=TableConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey56: BinaryAssociation = BinaryAssociation(
    name="primaryKey56",
    ends={
        Property(name="PrimaryKey58", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable57", type=PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
deletedTable64: BinaryAssociation = BinaryAssociation(
    name="deletedTable64",
    ends={
        Property(name="Table65", type=mm_rdb_DeleteTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteTable", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
generateID59: BinaryAssociation = BinaryAssociation(
    name="generateID59",
    ends={
        Property(name="Sequence61", type=mm_rdb_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_CreateTable60", type=Sequence, multiplicity=Multiplicity(1, 1))
    }
)
renamedTable62: BinaryAssociation = BinaryAssociation(
    name="renamedTable62",
    ends={
        Property(name="Table63", type=mm_rdb_RenameTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameTable", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
columnConstrains68: BinaryAssociation = BinaryAssociation(
    name="columnConstrains68",
    ends={
        Property(name="mm_rdb_AddColumn69", type=ColumnConstraint, multiplicity=Multiplicity(0, 9999)),
        Property(name="ColumnConstraint70", type=mm_rdb_AddColumn, multiplicity=Multiplicity(1, 1))
    }
)
changedTable71: BinaryAssociation = BinaryAssociation(
    name="changedTable71",
    ends={
        Property(name="Table72", type=mm_rdb_RenameColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
changedTable66: BinaryAssociation = BinaryAssociation(
    name="changedTable66",
    ends={
        Property(name="Table67", type=mm_rdb_AddColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_AddColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
changedTable76: BinaryAssociation = BinaryAssociation(
    name="changedTable76",
    ends={
        Property(name="Table77", type=mm_rdb_TypeChangeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_TypeChangeToColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
changedTypeColumn78: BinaryAssociation = BinaryAssociation(
    name="changedTypeColumn78",
    ends={
        Property(name="TableColumn80", type=mm_rdb_TypeChangeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_TypeChangeToColumn79", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
renamedColumn73: BinaryAssociation = BinaryAssociation(
    name="renamedColumn73",
    ends={
        Property(name="TableColumn75", type=mm_rdb_RenameColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_RenameColumn74", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
columnReferences86: BinaryAssociation = BinaryAssociation(
    name="columnReferences86",
    ends={
        Property(name="dml_ColumnReference", type=mm_dml_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_dml_Query", type=dml_ColumnReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reference87: BinaryAssociation = BinaryAssociation(
    name="reference87",
    ends={
        Property(name="Column", type=mm_dml_ColumnReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_dml_ColumnReference", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
changedTable81: BinaryAssociation = BinaryAssociation(
    name="changedTable81",
    ends={
        Property(name="Table82", type=mm_rdb_DeleteColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
deleteColumn83: BinaryAssociation = BinaryAssociation(
    name="deleteColumn83",
    ends={
        Property(name="TableColumn85", type=mm_rdb_DeleteColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_rdb_DeleteColumn84", type=TableColumn, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mm_rdb_Database_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_Database)
gen_mm_rdb_DbObject_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_DbObject)
gen_mm_rdb_Schema_DbObject = Generalization(general=DbObject, specific=mm_rdb_Schema)
gen_mm_rdb_Table_rdb_DbObject = Generalization(general=rdb_DbObject, specific=mm_rdb_Table)
gen_mm_rdb_Table_rdb_Relation = Generalization(general=rdb_Relation, specific=mm_rdb_Table)
gen_mm_rdb_Constraint_DbObject = Generalization(general=DbObject, specific=mm_rdb_Constraint)
gen_mm_rdb_TableConstraint_rdb_Constraint = Generalization(general=rdb_Constraint, specific=mm_rdb_TableConstraint)
gen_mm_rdb_TableConstraint_rdb_NamedElement = Generalization(general=rdb_NamedElement, specific=mm_rdb_TableConstraint)
gen_mm_rdb_Sequence_DbObject = Generalization(general=DbObject, specific=mm_rdb_Sequence)
gen_mm_rdb_Column_NamedElement = Generalization(general=NamedElement, specific=mm_rdb_Column)
gen_mm_rdb_ColumnConstraint_Constraint = Generalization(general=Constraint, specific=mm_rdb_ColumnConstraint)
gen_mm_rdb_ForeignKey_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_ForeignKey)
gen_mm_rdb_Index_DbObject = Generalization(general=DbObject, specific=mm_rdb_Index)
gen_mm_rdb_TableColumn_Column = Generalization(general=Column, specific=mm_rdb_TableColumn)
gen_mm_rdb_PrimaryKey_UniqueIndex = Generalization(general=UniqueIndex, specific=mm_rdb_PrimaryKey)
gen_mm_rdb_UniqueIndex_TableConstraint = Generalization(general=TableConstraint, specific=mm_rdb_UniqueIndex)
gen_mm_rdb_CreateTable_Operation = Generalization(general=Operation, specific=mm_rdb_CreateTable)
gen_mm_rdb_DeleteTable_Operation = Generalization(general=Operation, specific=mm_rdb_DeleteTable)
gen_mm_rdb_AddColumn_Operation = Generalization(general=Operation, specific=mm_rdb_AddColumn)
gen_mm_rdb_RenameTable_Operation = Generalization(general=Operation, specific=mm_rdb_RenameTable)
gen_mm_rdb_RenameColumn_Operation = Generalization(general=Operation, specific=mm_rdb_RenameColumn)
gen_mm_rdb_DeleteColumn_Operation = Generalization(general=Operation, specific=mm_rdb_DeleteColumn)
gen_mm_rdb_TypeChangeToColumn_Operation = Generalization(general=Operation, specific=mm_rdb_TypeChangeToColumn)
gen_mm_dml_Query_Relation = Generalization(general=Relation, specific=mm_dml_Query)
gen_mm_dml_ColumnReference_Column = Generalization(general=Column, specific=mm_dml_ColumnReference)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={mm_rdb_ModelRoot, Database, Operation, mm_rdb_NamedElement, mm_rdb_Database, NamedElement, Sequence, Index, Schema, mm_rdb_DbObject, mm_rdb_Schema, DbObject, Table, PrimaryKey, mm_rdb_Relation, mm_rdb_Table, rdb_DbObject, rdb_Relation, mm_rdb_Constraint, mm_rdb_TableConstraint, rdb_Constraint, rdb_NamedElement, TableColumn, TableConstraint, mm_rdb_Sequence, mm_rdb_Column, mm_rdb_ColumnConstraint, Constraint, mm_rdb_ForeignKey, mm_rdb_Index, mm_rdb_TableColumn, Column, ColumnConstraint, mm_rdb_PrimaryKey, UniqueIndex, mm_rdb_Operation, ModelRoot, mm_rdb_UniqueIndex, mm_rdb_CreateTable, mm_rdb_DeleteTable, mm_rdb_AddColumn, mm_rdb_RenameTable, mm_rdb_RenameColumn, mm_rdb_DeleteColumn, mm_rdb_TypeChangeToColumn, mm_dml_Query, Relation, dml_ColumnReference, mm_dml_ColumnReference},
    associations={sourceDB0, operations4, targetDB1, tables6, sequences8, indexes10, schemas5, owningSchema12, primaryKey15, owningSchema20, owningTable23, ownedColumns16, constraints18, targetTable29, constrainedColumn31, owningColumn26, columns39, _owningTable34, constraints37, underlyingIndex47, modelRoot49, indexedTable41, owningSchema44, tableColumns51, tableConstraints53, primaryKey56, deletedTable64, generateID59, renamedTable62, columnConstrains68, changedTable71, changedTable66, changedTable76, changedTypeColumn78, renamedColumn73, columnReferences86, reference87, changedTable81, deleteColumn83},
    generalizations={gen_mm_rdb_Database_NamedElement, gen_mm_rdb_DbObject_NamedElement, gen_mm_rdb_Schema_DbObject, gen_mm_rdb_Table_rdb_DbObject, gen_mm_rdb_Table_rdb_Relation, gen_mm_rdb_Constraint_DbObject, gen_mm_rdb_TableConstraint_rdb_Constraint, gen_mm_rdb_TableConstraint_rdb_NamedElement, gen_mm_rdb_Sequence_DbObject, gen_mm_rdb_Column_NamedElement, gen_mm_rdb_ColumnConstraint_Constraint, gen_mm_rdb_ForeignKey_TableConstraint, gen_mm_rdb_Index_DbObject, gen_mm_rdb_TableColumn_Column, gen_mm_rdb_PrimaryKey_UniqueIndex, gen_mm_rdb_UniqueIndex_TableConstraint, gen_mm_rdb_CreateTable_Operation, gen_mm_rdb_DeleteTable_Operation, gen_mm_rdb_AddColumn_Operation, gen_mm_rdb_RenameTable_Operation, gen_mm_rdb_RenameColumn_Operation, gen_mm_rdb_DeleteColumn_Operation, gen_mm_rdb_TypeChangeToColumn_Operation, gen_mm_dml_Query_Relation, gen_mm_dml_ColumnReference_Column},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)