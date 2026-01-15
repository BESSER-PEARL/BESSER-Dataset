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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="BLOB")
    }
)

# Classes
model_DatabaseVersions = Class(name="model::DatabaseVersions")
model_DatabaseVersion = Class(name="model::DatabaseVersion")
model_Database = Class(name="model::Database")
TableMapping = Class(name="TableMapping")
ColumnMapping = Class(name="ColumnMapping")
NameProvider = Class(name="NameProvider")
Table = Class(name="Table")
View = Class(name="View")
Trigger = Class(name="Trigger")
Index = Class(name="Index")
model_common_NameProvider = Class(name="model::common::NameProvider", is_abstract=True)
model_common_MappingEntry = Class(name="model::common::MappingEntry")
model_common_StringToTableMappingEntryMap = Class(name="model::common::StringToTableMappingEntryMap")
model_common_StringToColumnMappingEntryMap = Class(name="model::common::StringToColumnMappingEntryMap")
model_common_TableMapping = Class(name="model::common::TableMapping")
StringToTableMappingEntryMap = Class(name="StringToTableMappingEntryMap")
model_common_ColumnMapping = Class(name="model::common::ColumnMapping")
StringToColumnMappingEntryMap = Class(name="StringToColumnMappingEntryMap")
table_model_Database = Class(name="table::model::Database")
Column = Class(name="Column")
TableConstraint = Class(name="TableConstraint")
model_table_TableConstraint = Class(name="model::table::TableConstraint", is_abstract=True)
model_table_PrimaryKeyTableConstraint = Class(name="model::table::PrimaryKeyTableConstraint")
IndexedColumn = Class(name="IndexedColumn")
model_table_UniqueTableConstraint = Class(name="model::table::UniqueTableConstraint")
model_table_CheckTableConstraint = Class(name="model::table::CheckTableConstraint")
Expression = Class(name="Expression")
model_table_Table = Class(name="model::table::Table")
model_column_Column = Class(name="model::column::Column")
ColumnConstraint = Class(name="ColumnConstraint")
model_column_IndexedColumn = Class(name="model::column::IndexedColumn")
model_column_ColumnConstraint = Class(name="model::column::ColumnConstraint", is_abstract=True)
model_table_ForeignKeyTableConstraint = Class(name="model::table::ForeignKeyTableConstraint")
model_column_PrimaryKeyColumnConstraint = Class(name="model::column::PrimaryKeyColumnConstraint")
model_column_ForeignKeyColumnConstraint = Class(name="model::column::ForeignKeyColumnConstraint")
model_column_NotNullColumnConstraint = Class(name="model::column::NotNullColumnConstraint")
model_column_UniqueColumnConstraint = Class(name="model::column::UniqueColumnConstraint")
model_column_CheckColumnConstraint = Class(name="model::column::CheckColumnConstraint")
model_column_DefaultValueColumnConstraint = Class(name="model::column::DefaultValueColumnConstraint", is_abstract=True)
model_column_DefaultExpressionValueColumnConstraint = Class(name="model::column::DefaultExpressionValueColumnConstraint")
model_column_DefaultStringValueColumnConstraint = Class(name="model::column::DefaultStringValueColumnConstraint")
model_column_DefaultIntegerValueColumnConstraint = Class(name="model::column::DefaultIntegerValueColumnConstraint")
model_view_View = Class(name="model::view::View")
view_model_Database = Class(name="view::model::Database")
model_index_Index = Class(name="model::index::Index", is_abstract=True)
index_model_Database = Class(name="index::model::Database")
model_trigger_Trigger = Class(name="model::trigger::Trigger")
trigger_model_Database = Class(name="trigger::model::Database")
model_expression_Expression = Class(name="model::expression::Expression", is_abstract=True)
model_column_DefaultRealValueColumnConstraint = Class(name="model::column::DefaultRealValueColumnConstraint")

# model_DatabaseVersions class attributes and methods
model_DatabaseVersions_fileName: Property = Property(name="fileName", type=StringType)
model_DatabaseVersions_packageName: Property = Property(name="packageName", type=StringType)
model_DatabaseVersions_m_getFirstVersion: Method = Method(name="getFirstVersion", parameters={}, type=StringType)
model_DatabaseVersions_m_getLastVersion: Method = Method(name="getLastVersion", parameters={}, type=StringType)
model_DatabaseVersions_m_createVersion: Method = Method(name="createVersion", parameters={}, type=StringType)
model_DatabaseVersions.attributes={model_DatabaseVersions_fileName, model_DatabaseVersions_packageName}
model_DatabaseVersions.methods={model_DatabaseVersions_m_getFirstVersion, model_DatabaseVersions_m_createVersion, model_DatabaseVersions_m_getLastVersion}

# model_DatabaseVersion class attributes and methods

# model_Database class attributes and methods

# TableMapping class attributes and methods

# ColumnMapping class attributes and methods

# NameProvider class attributes and methods

# Table class attributes and methods

# View class attributes and methods

# Trigger class attributes and methods

# Index class attributes and methods

# model_common_NameProvider class attributes and methods
model_common_NameProvider_name: Property = Property(name="name", type=StringType)
model_common_NameProvider.attributes={model_common_NameProvider_name}

# model_common_MappingEntry class attributes and methods
model_common_MappingEntry_previous: Property = Property(name="previous", type=StringType)
model_common_MappingEntry_current: Property = Property(name="current", type=StringType)
model_common_MappingEntry.attributes={model_common_MappingEntry_current, model_common_MappingEntry_previous}

# model_common_StringToTableMappingEntryMap class attributes and methods
model_common_StringToTableMappingEntryMap_key: Property = Property(name="key", type=StringType)
model_common_StringToTableMappingEntryMap.attributes={model_common_StringToTableMappingEntryMap_key}

# model_common_StringToColumnMappingEntryMap class attributes and methods
model_common_StringToColumnMappingEntryMap_key: Property = Property(name="key", type=StringType)
model_common_StringToColumnMappingEntryMap.attributes={model_common_StringToColumnMappingEntryMap_key}

# model_common_TableMapping class attributes and methods
model_common_TableMapping_m_getPrevious: Method = Method(name="getPrevious", parameters={Parameter(name='current')}, type=StringType)
model_common_TableMapping_m_getAllPrevious: Method = Method(name="getAllPrevious", parameters={})
model_common_TableMapping_m_getCurrent: Method = Method(name="getCurrent", parameters={Parameter(name='previous')}, type=StringType)
model_common_TableMapping_m_getAllCurrent: Method = Method(name="getAllCurrent", parameters={})
model_common_TableMapping_m_entries: Method = Method(name="entries", parameters={})
model_common_TableMapping_m_put: Method = Method(name="put", parameters={Parameter(name='previous'), Parameter(name='current')})
model_common_TableMapping.methods={model_common_TableMapping_m_getAllPrevious, model_common_TableMapping_m_getCurrent, model_common_TableMapping_m_getPrevious, model_common_TableMapping_m_entries, model_common_TableMapping_m_put, model_common_TableMapping_m_getAllCurrent}

# StringToTableMappingEntryMap class attributes and methods

# model_common_ColumnMapping class attributes and methods
model_common_ColumnMapping_m_getPrevious: Method = Method(name="getPrevious", parameters={Parameter(name='current')}, type=StringType)
model_common_ColumnMapping_m_getAllPrevious: Method = Method(name="getAllPrevious", parameters={})
model_common_ColumnMapping_m_getAllCurrent: Method = Method(name="getAllCurrent", parameters={})
model_common_ColumnMapping_m_put: Method = Method(name="put", parameters={Parameter(name='previous'), Parameter(name='current')})
model_common_ColumnMapping_m_entries: Method = Method(name="entries", parameters={})
model_common_ColumnMapping_m_getCurrent: Method = Method(name="getCurrent", parameters={Parameter(name='previous')}, type=StringType)
model_common_ColumnMapping.methods={model_common_ColumnMapping_m_put, model_common_ColumnMapping_m_getAllCurrent, model_common_ColumnMapping_m_getAllPrevious, model_common_ColumnMapping_m_getCurrent, model_common_ColumnMapping_m_entries, model_common_ColumnMapping_m_getPrevious}

# StringToColumnMappingEntryMap class attributes and methods

# table_model_Database class attributes and methods

# Column class attributes and methods

# TableConstraint class attributes and methods

# model_table_TableConstraint class attributes and methods
model_table_TableConstraint_name: Property = Property(name="name", type=StringType)
model_table_TableConstraint.attributes={model_table_TableConstraint_name}

# model_table_PrimaryKeyTableConstraint class attributes and methods

# IndexedColumn class attributes and methods

# model_table_UniqueTableConstraint class attributes and methods

# model_table_CheckTableConstraint class attributes and methods

# Expression class attributes and methods

# model_table_Table class attributes and methods

# model_column_Column class attributes and methods
model_column_Column_type: Property = Property(name="type", type=StringType)
model_column_Column.attributes={model_column_Column_type}

# ColumnConstraint class attributes and methods

# model_column_IndexedColumn class attributes and methods

# model_column_ColumnConstraint class attributes and methods
model_column_ColumnConstraint_name: Property = Property(name="name", type=StringType)
model_column_ColumnConstraint.attributes={model_column_ColumnConstraint_name}

# model_table_ForeignKeyTableConstraint class attributes and methods

# model_column_PrimaryKeyColumnConstraint class attributes and methods

# model_column_ForeignKeyColumnConstraint class attributes and methods

# model_column_NotNullColumnConstraint class attributes and methods

# model_column_UniqueColumnConstraint class attributes and methods

# model_column_CheckColumnConstraint class attributes and methods

# model_column_DefaultValueColumnConstraint class attributes and methods

# model_column_DefaultExpressionValueColumnConstraint class attributes and methods

# model_column_DefaultStringValueColumnConstraint class attributes and methods

# model_column_DefaultIntegerValueColumnConstraint class attributes and methods

# model_view_View class attributes and methods

# view_model_Database class attributes and methods

# model_index_Index class attributes and methods

# index_model_Database class attributes and methods

# model_trigger_Trigger class attributes and methods

# trigger_model_Database class attributes and methods

# model_expression_Expression class attributes and methods

# model_column_DefaultRealValueColumnConstraint class attributes and methods

# Relationships
versions0: BinaryAssociation = BinaryAssociation(
    name="versions0",
    ends={
        Property(name="model_DatabaseVersion", type=model_DatabaseVersions, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DatabaseVersions", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="model_Database", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DatabaseVersion2", type=model_Database, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
previousVersion4: BinaryAssociation = BinaryAssociation(
    name="previousVersion4",
    ends={
        Property(name="DatabaseVersion", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="nextVersion", type=model_DatabaseVersion, multiplicity=Multiplicity(0, 1))
    }
)
nextVersion6: BinaryAssociation = BinaryAssociation(
    name="nextVersion6",
    ends={
        Property(name="DatabaseVersion7", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="previousVersion", type=model_DatabaseVersion, multiplicity=Multiplicity(0, 1))
    }
)
tableMapping8: BinaryAssociation = BinaryAssociation(
    name="tableMapping8",
    ends={
        Property(name="TableMapping", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DatabaseVersion9", type=TableMapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnMapping10: BinaryAssociation = BinaryAssociation(
    name="columnMapping10",
    ends={
        Property(name="ColumnMapping", type=model_DatabaseVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DatabaseVersion11", type=ColumnMapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tables12: BinaryAssociation = BinaryAssociation(
    name="tables12",
    ends={
        Property(name="table", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Table", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views13: BinaryAssociation = BinaryAssociation(
    name="views13",
    ends={
        Property(name="view", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="View", type=View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers14: BinaryAssociation = BinaryAssociation(
    name="triggers14",
    ends={
        Property(name="trigger", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Trigger", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes15: BinaryAssociation = BinaryAssociation(
    name="indexes15",
    ends={
        Property(name="index", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Index", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prev2entryMap16: BinaryAssociation = BinaryAssociation(
    name="prev2entryMap16",
    ends={
        Property(name="StringToTableMappingEntryMap", type=model_common_TableMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_common_TableMapping", type=StringToTableMappingEntryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
curr2entryMap17: BinaryAssociation = BinaryAssociation(
    name="curr2entryMap17",
    ends={
        Property(name="StringToTableMappingEntryMap19", type=model_common_TableMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_common_TableMapping18", type=StringToTableMappingEntryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prev2entryMap20: BinaryAssociation = BinaryAssociation(
    name="prev2entryMap20",
    ends={
        Property(name="StringToColumnMappingEntryMap", type=model_common_ColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_common_ColumnMapping", type=StringToColumnMappingEntryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
curr2entryMap21: BinaryAssociation = BinaryAssociation(
    name="curr2entryMap21",
    ends={
        Property(name="StringToColumnMappingEntryMap23", type=model_common_ColumnMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="model_common_ColumnMapping22", type=StringToColumnMappingEntryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database24: BinaryAssociation = BinaryAssociation(
    name="database24",
    ends={
        Property(name="Database", type=model_table_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=table_model_Database, multiplicity=Multiplicity(1, 1))
    }
)
columns25: BinaryAssociation = BinaryAssociation(
    name="columns25",
    ends={
        Property(name="column", type=model_table_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Column", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints26: BinaryAssociation = BinaryAssociation(
    name="constraints26",
    ends={
        Property(name="table27", type=model_table_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableConstraint", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table28: BinaryAssociation = BinaryAssociation(
    name="table28",
    ends={
        Property(name="table30", type=model_table_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Table29", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
columns31: BinaryAssociation = BinaryAssociation(
    name="columns31",
    ends={
        Property(name="IndexedColumn", type=model_table_PrimaryKeyTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_PrimaryKeyTableConstraint", type=IndexedColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
columns32: BinaryAssociation = BinaryAssociation(
    name="columns32",
    ends={
        Property(name="IndexedColumn33", type=model_table_UniqueTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_UniqueTableConstraint", type=IndexedColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression34: BinaryAssociation = BinaryAssociation(
    name="expression34",
    ends={
        Property(name="Expression", type=model_table_CheckTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_CheckTableConstraint", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columns35: BinaryAssociation = BinaryAssociation(
    name="columns35",
    ends={
        Property(name="Column36", type=model_table_ForeignKeyTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_ForeignKeyTableConstraint", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
foreignTable37: BinaryAssociation = BinaryAssociation(
    name="foreignTable37",
    ends={
        Property(name="Table39", type=model_table_ForeignKeyTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_ForeignKeyTableConstraint38", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
foreignColumns40: BinaryAssociation = BinaryAssociation(
    name="foreignColumns40",
    ends={
        Property(name="Column42", type=model_table_ForeignKeyTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_table_ForeignKeyTableConstraint41", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
table43: BinaryAssociation = BinaryAssociation(
    name="table43",
    ends={
        Property(name="table45", type=model_column_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Table44", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
constraints46: BinaryAssociation = BinaryAssociation(
    name="constraints46",
    ends={
        Property(name="column47", type=model_column_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ColumnConstraint", type=ColumnConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column48: BinaryAssociation = BinaryAssociation(
    name="column48",
    ends={
        Property(name="Column49", type=model_column_IndexedColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="model_column_IndexedColumn", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
foreignTable53: BinaryAssociation = BinaryAssociation(
    name="foreignTable53",
    ends={
        Property(name="Table54", type=model_column_ForeignKeyColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_column_ForeignKeyColumnConstraint", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
foreignColumn55: BinaryAssociation = BinaryAssociation(
    name="foreignColumn55",
    ends={
        Property(name="Column57", type=model_column_ForeignKeyColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_column_ForeignKeyColumnConstraint56", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
expression58: BinaryAssociation = BinaryAssociation(
    name="expression58",
    ends={
        Property(name="Expression59", type=model_column_CheckColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_column_CheckColumnConstraint", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
column50: BinaryAssociation = BinaryAssociation(
    name="column50",
    ends={
        Property(name="column52", type=model_column_ColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Column51", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
database60: BinaryAssociation = BinaryAssociation(
    name="database60",
    ends={
        Property(name="Database61", type=model_view_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=view_model_Database, multiplicity=Multiplicity(1, 1))
    }
)
database62: BinaryAssociation = BinaryAssociation(
    name="database62",
    ends={
        Property(name="Database63", type=model_index_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=index_model_Database, multiplicity=Multiplicity(1, 1))
    }
)
database64: BinaryAssociation = BinaryAssociation(
    name="database64",
    ends={
        Property(name="Database65", type=model_trigger_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=trigger_model_Database, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_Database_NameProvider = Generalization(general=NameProvider, specific=model_Database)
gen_model_table_PrimaryKeyTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=model_table_PrimaryKeyTableConstraint)
gen_model_table_UniqueTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=model_table_UniqueTableConstraint)
gen_model_table_CheckTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=model_table_CheckTableConstraint)
gen_model_table_Table_NameProvider = Generalization(general=NameProvider, specific=model_table_Table)
gen_model_column_Column_NameProvider = Generalization(general=NameProvider, specific=model_column_Column)
gen_model_table_ForeignKeyTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=model_table_ForeignKeyTableConstraint)
gen_model_column_PrimaryKeyColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_PrimaryKeyColumnConstraint)
gen_model_column_ForeignKeyColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_ForeignKeyColumnConstraint)
gen_model_column_NotNullColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_NotNullColumnConstraint)
gen_model_column_UniqueColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_UniqueColumnConstraint)
gen_model_column_CheckColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_CheckColumnConstraint)
gen_model_column_DefaultValueColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=model_column_DefaultValueColumnConstraint)
gen_model_view_View_NameProvider = Generalization(general=NameProvider, specific=model_view_View)
gen_model_trigger_Trigger_NameProvider = Generalization(general=NameProvider, specific=model_trigger_Trigger)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_DatabaseVersions, model_DatabaseVersion, model_Database, TableMapping, ColumnMapping, NameProvider, Table, View, Trigger, Index, model_common_NameProvider, model_common_MappingEntry, model_common_StringToTableMappingEntryMap, model_common_StringToColumnMappingEntryMap, model_common_TableMapping, StringToTableMappingEntryMap, model_common_ColumnMapping, StringToColumnMappingEntryMap, table_model_Database, Column, TableConstraint, model_table_TableConstraint, model_table_PrimaryKeyTableConstraint, IndexedColumn, model_table_UniqueTableConstraint, model_table_CheckTableConstraint, Expression, model_table_Table, model_column_Column, ColumnConstraint, model_column_IndexedColumn, model_column_ColumnConstraint, model_table_ForeignKeyTableConstraint, model_column_PrimaryKeyColumnConstraint, model_column_ForeignKeyColumnConstraint, model_column_NotNullColumnConstraint, model_column_UniqueColumnConstraint, model_column_CheckColumnConstraint, model_column_DefaultValueColumnConstraint, model_column_DefaultExpressionValueColumnConstraint, model_column_DefaultStringValueColumnConstraint, model_column_DefaultIntegerValueColumnConstraint, model_view_View, view_model_Database, model_index_Index, index_model_Database, model_trigger_Trigger, trigger_model_Database, model_expression_Expression, model_column_DefaultRealValueColumnConstraint, DataType},
    associations={versions0, database1, previousVersion4, nextVersion6, tableMapping8, columnMapping10, tables12, views13, triggers14, indexes15, prev2entryMap16, curr2entryMap17, prev2entryMap20, curr2entryMap21, database24, columns25, constraints26, table28, columns31, columns32, expression34, columns35, foreignTable37, foreignColumns40, table43, constraints46, column48, foreignTable53, foreignColumn55, expression58, column50, database60, database62, database64},
    generalizations={gen_model_Database_NameProvider, gen_model_table_PrimaryKeyTableConstraint_TableConstraint, gen_model_table_UniqueTableConstraint_TableConstraint, gen_model_table_CheckTableConstraint_TableConstraint, gen_model_table_Table_NameProvider, gen_model_column_Column_NameProvider, gen_model_table_ForeignKeyTableConstraint_TableConstraint, gen_model_column_PrimaryKeyColumnConstraint_ColumnConstraint, gen_model_column_ForeignKeyColumnConstraint_ColumnConstraint, gen_model_column_NotNullColumnConstraint_ColumnConstraint, gen_model_column_UniqueColumnConstraint_ColumnConstraint, gen_model_column_CheckColumnConstraint_ColumnConstraint, gen_model_column_DefaultValueColumnConstraint_ColumnConstraint, gen_model_view_View_NameProvider, gen_model_trigger_Trigger_NameProvider},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)