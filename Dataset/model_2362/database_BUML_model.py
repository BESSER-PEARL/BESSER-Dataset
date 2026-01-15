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
TypesLibraryUser = Class(name="TypesLibraryUser")
database_Schema = Class(name="database::Schema")
database_NamedElement = Class(name="database::NamedElement", is_abstract=True)
DatabaseElement = Class(name="DatabaseElement")
database_DataBase = Class(name="database::DataBase")
TableContainer = Class(name="TableContainer")
database_PrimaryKey = Class(name="database::PrimaryKey")
database_ForeignKey = Class(name="database::ForeignKey")
database_UserDefinedTypesLibrary = Class(name="database::UserDefinedTypesLibrary")
database_AbstractTable = Class(name="database::AbstractTable", is_abstract=True)
NamedElement = Class(name="NamedElement")
database_TableContainer = Class(name="database::TableContainer", is_abstract=True)
database_Column = Class(name="database::Column")
database_Index = Class(name="database::Index")
database_IndexElement = Class(name="database::IndexElement")
database_ForeignKeyElement = Class(name="database::ForeignKeyElement")
database_Type = Class(name="database::Type")
database_Sequence = Class(name="database::Sequence")
database_Table = Class(name="database::Table")
database_View = Class(name="database::View")
AbstractTable = Class(name="AbstractTable")
database_ViewElement = Class(name="database::ViewElement")
database_Constraint = Class(name="database::Constraint")
database_DatabaseElement = Class(name="database::DatabaseElement", is_abstract=True)

# TypesLibraryUser class attributes and methods

# database_Schema class attributes and methods

# database_NamedElement class attributes and methods
database_NamedElement_name: Property = Property(name="name", type=StringType)
database_NamedElement.attributes={database_NamedElement_name}

# DatabaseElement class attributes and methods

# database_DataBase class attributes and methods
database_DataBase_url: Property = Property(name="url", type=StringType)
database_DataBase.attributes={database_DataBase_url}

# TableContainer class attributes and methods

# database_PrimaryKey class attributes and methods

# database_ForeignKey class attributes and methods
database_ForeignKey_m_getSourceTable: Method = Method(name="getSourceTable", parameters={}, type=StringType)
database_ForeignKey_m_getTargetTable: Method = Method(name="getTargetTable", parameters={}, type=StringType)
database_ForeignKey.methods={database_ForeignKey_m_getSourceTable, database_ForeignKey_m_getTargetTable}

# database_UserDefinedTypesLibrary class attributes and methods

# database_AbstractTable class attributes and methods

# NamedElement class attributes and methods

# database_TableContainer class attributes and methods

# database_Column class attributes and methods
database_Column_nullable: Property = Property(name="nullable", type=BooleanType)
database_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
database_Column_autoincrement: Property = Property(name="autoincrement", type=BooleanType)
database_Column_inPrimaryKey: Property = Property(name="inPrimaryKey", type=BooleanType)
database_Column_inForeignKey: Property = Property(name="inForeignKey", type=BooleanType)
database_Column_unique: Property = Property(name="unique", type=BooleanType)
database_Column_m_addToPrimaryKey: Method = Method(name="addToPrimaryKey", parameters={})
database_Column_m_addToUniqueIndex: Method = Method(name="addToUniqueIndex", parameters={})
database_Column_m_removeFromPrimaryKey: Method = Method(name="removeFromPrimaryKey", parameters={})
database_Column_m_removeFromUniqueIndex: Method = Method(name="removeFromUniqueIndex", parameters={})
database_Column.attributes={database_Column_nullable, database_Column_unique, database_Column_autoincrement, database_Column_inPrimaryKey, database_Column_inForeignKey, database_Column_defaultValue}
database_Column.methods={database_Column_m_addToPrimaryKey, database_Column_m_removeFromPrimaryKey, database_Column_m_removeFromUniqueIndex, database_Column_m_addToUniqueIndex}

# database_Index class attributes and methods
database_Index_qualifier: Property = Property(name="qualifier", type=StringType)
database_Index_unique: Property = Property(name="unique", type=BooleanType)
database_Index_cardinality: Property = Property(name="cardinality", type=IntegerType)
database_Index_indexType: Property = Property(name="indexType", type=StringType)
database_Index.attributes={database_Index_unique, database_Index_indexType, database_Index_cardinality, database_Index_qualifier}

# database_IndexElement class attributes and methods
database_IndexElement_asc: Property = Property(name="asc", type=BooleanType)
database_IndexElement.attributes={database_IndexElement_asc}

# database_ForeignKeyElement class attributes and methods

# database_Type class attributes and methods

# database_Sequence class attributes and methods
database_Sequence_minValue: Property = Property(name="minValue", type=StringType)
database_Sequence_maxValue: Property = Property(name="maxValue", type=StringType)
database_Sequence_cacheSize: Property = Property(name="cacheSize", type=StringType)
database_Sequence_cycle: Property = Property(name="cycle", type=BooleanType)
database_Sequence_start: Property = Property(name="start", type=StringType)
database_Sequence_increment: Property = Property(name="increment", type=StringType)
database_Sequence.attributes={database_Sequence_cacheSize, database_Sequence_start, database_Sequence_maxValue, database_Sequence_minValue, database_Sequence_cycle, database_Sequence_increment}

# database_Table class attributes and methods

# database_View class attributes and methods
database_View_query: Property = Property(name="query", type=StringType)
database_View.attributes={database_View_query}

# AbstractTable class attributes and methods

# database_ViewElement class attributes and methods
database_ViewElement_name: Property = Property(name="name", type=StringType)
database_ViewElement_alias: Property = Property(name="alias", type=StringType)
database_ViewElement.attributes={database_ViewElement_name, database_ViewElement_alias}

# database_Constraint class attributes and methods
database_Constraint_expression: Property = Property(name="expression", type=StringType)
database_Constraint.attributes={database_Constraint_expression}

# database_DatabaseElement class attributes and methods
database_DatabaseElement_ID: Property = Property(name="ID", type=StringType)
database_DatabaseElement_comments: Property = Property(name="comments", type=StringType)
database_DatabaseElement_techID: Property = Property(name="techID", type=StringType)
database_DatabaseElement.attributes={database_DatabaseElement_comments, database_DatabaseElement_techID, database_DatabaseElement_ID}

# Relationships
schemas0: BinaryAssociation = BinaryAssociation(
    name="schemas0",
    ends={
        Property(name="database_Schema", type=database_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DataBase", type=database_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexElements5: BinaryAssociation = BinaryAssociation(
    name="indexElements5",
    ends={
        Property(name="IndexElement", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=database_IndexElement, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey6: BinaryAssociation = BinaryAssociation(
    name="primaryKey6",
    ends={
        Property(name="PrimaryKey", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=database_PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
defines1: BinaryAssociation = BinaryAssociation(
    name="defines1",
    ends={
        Property(name="database_UserDefinedTypesLibrary", type=database_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DataBase2", type=database_UserDefinedTypesLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="TableContainer", type=database_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=database_TableContainer, multiplicity=Multiplicity(1, 1))
    }
)
indexes4: BinaryAssociation = BinaryAssociation(
    name="indexes4",
    ends={
        Property(name="database_Index", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column", type=database_Index, multiplicity=Multiplicity(0, 9999))
    }
)
elements16: BinaryAssociation = BinaryAssociation(
    name="elements16",
    ends={
        Property(name="database_IndexElement", type=database_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Index17", type=database_IndexElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys7: BinaryAssociation = BinaryAssociation(
    name="foreignKeys7",
    ends={
        Property(name="database_ForeignKey", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column8", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKeyElements9: BinaryAssociation = BinaryAssociation(
    name="foreignKeyElements9",
    ends={
        Property(name="ForeignKeyElement", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="fkColumn", type=database_ForeignKeyElement, multiplicity=Multiplicity(0, 9999))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="database_Type", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column11", type=database_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence12: BinaryAssociation = BinaryAssociation(
    name="sequence12",
    ends={
        Property(name="Sequence", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns13", type=database_Sequence, multiplicity=Multiplicity(0, 1))
    }
)
owner14: BinaryAssociation = BinaryAssociation(
    name="owner14",
    ends={
        Property(name="Table", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns15", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
indexes30: BinaryAssociation = BinaryAssociation(
    name="indexes30",
    ends={
        Property(name="Index", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner31", type=database_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns32: BinaryAssociation = BinaryAssociation(
    name="columns32",
    ends={
        Property(name="Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner33", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="Table19", type=database_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns20: BinaryAssociation = BinaryAssociation(
    name="columns20",
    ends={
        Property(name="database_ViewElement", type=database_View, multiplicity=Multiplicity(1, 1)),
        Property(name="database_View", type=database_ViewElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables21: BinaryAssociation = BinaryAssociation(
    name="tables21",
    ends={
        Property(name="database_ViewElement23", type=database_View, multiplicity=Multiplicity(1, 1)),
        Property(name="database_View22", type=database_ViewElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey24: BinaryAssociation = BinaryAssociation(
    name="primaryKey24",
    ends={
        Property(name="PrimaryKey25", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=database_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreignKeys26: BinaryAssociation = BinaryAssociation(
    name="foreignKeys26",
    ends={
        Property(name="ForeignKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner27", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints28: BinaryAssociation = BinaryAssociation(
    name="constraints28",
    ends={
        Property(name="Constraint", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner29", type=database_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fkColumn45: BinaryAssociation = BinaryAssociation(
    name="fkColumn45",
    ends={
        Property(name="Column46", type=database_ForeignKeyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeyElements", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
pkColumn47: BinaryAssociation = BinaryAssociation(
    name="pkColumn47",
    ends={
        Property(name="database_Column49", type=database_ForeignKeyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKeyElement48", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
columns34: BinaryAssociation = BinaryAssociation(
    name="columns34",
    ends={
        Property(name="Column35", type=database_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey", type=database_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner36: BinaryAssociation = BinaryAssociation(
    name="owner36",
    ends={
        Property(name="Table38", type=database_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey37", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
elements39: BinaryAssociation = BinaryAssociation(
    name="elements39",
    ends={
        Property(name="database_ForeignKeyElement", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey40", type=database_ForeignKeyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner41: BinaryAssociation = BinaryAssociation(
    name="owner41",
    ends={
        Property(name="Table42", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="database_Table", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey44", type=database_Table, multiplicity=Multiplicity(0, 1))
    }
)
columns54: BinaryAssociation = BinaryAssociation(
    name="columns54",
    ends={
        Property(name="Column55", type=database_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence", type=database_Column, multiplicity=Multiplicity(0, 9999))
    }
)
column50: BinaryAssociation = BinaryAssociation(
    name="column50",
    ends={
        Property(name="Column51", type=database_IndexElement, multiplicity=Multiplicity(1, 1)),
        Property(name="indexElements", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
owner52: BinaryAssociation = BinaryAssociation(
    name="owner52",
    ends={
        Property(name="Table53", type=database_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
tables56: BinaryAssociation = BinaryAssociation(
    name="tables56",
    ends={
        Property(name="AbstractTable", type=database_TableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner57", type=database_AbstractTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequences58: BinaryAssociation = BinaryAssociation(
    name="sequences58",
    ends={
        Property(name="database_Sequence", type=database_TableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableContainer", type=database_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_database_DataBase_TableContainer = Generalization(general=TableContainer, specific=database_DataBase)
gen_database_DataBase_TypesLibraryUser = Generalization(general=TypesLibraryUser, specific=database_DataBase)
gen_database_NamedElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_NamedElement)
gen_database_AbstractTable_NamedElement = Generalization(general=NamedElement, specific=database_AbstractTable)
gen_database_Column_NamedElement = Generalization(general=NamedElement, specific=database_Column)
gen_database_Index_NamedElement = Generalization(general=NamedElement, specific=database_Index)
gen_database_View_AbstractTable = Generalization(general=AbstractTable, specific=database_View)
gen_database_Table_AbstractTable = Generalization(general=AbstractTable, specific=database_Table)
gen_database_PrimaryKey_NamedElement = Generalization(general=NamedElement, specific=database_PrimaryKey)
gen_database_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=database_ForeignKey)
gen_database_ForeignKeyElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_ForeignKeyElement)
gen_database_IndexElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_IndexElement)
gen_database_Constraint_NamedElement = Generalization(general=NamedElement, specific=database_Constraint)
gen_database_Schema_TableContainer = Generalization(general=TableContainer, specific=database_Schema)
gen_database_Sequence_NamedElement = Generalization(general=NamedElement, specific=database_Sequence)
gen_database_TableContainer_NamedElement = Generalization(general=NamedElement, specific=database_TableContainer)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={TypesLibraryUser, database_Schema, database_NamedElement, DatabaseElement, database_DataBase, TableContainer, database_PrimaryKey, database_ForeignKey, database_UserDefinedTypesLibrary, database_AbstractTable, NamedElement, database_TableContainer, database_Column, database_Index, database_IndexElement, database_ForeignKeyElement, database_Type, database_Sequence, database_Table, database_View, AbstractTable, database_ViewElement, database_Constraint, database_DatabaseElement},
    associations={schemas0, indexElements5, primaryKey6, defines1, owner3, indexes4, elements16, foreignKeys7, foreignKeyElements9, type10, sequence12, owner14, indexes30, columns32, owner18, columns20, tables21, primaryKey24, foreignKeys26, constraints28, fkColumn45, pkColumn47, columns34, owner36, elements39, owner41, target43, columns54, column50, owner52, tables56, sequences58},
    generalizations={gen_database_DataBase_TableContainer, gen_database_DataBase_TypesLibraryUser, gen_database_NamedElement_DatabaseElement, gen_database_AbstractTable_NamedElement, gen_database_Column_NamedElement, gen_database_Index_NamedElement, gen_database_View_AbstractTable, gen_database_Table_AbstractTable, gen_database_PrimaryKey_NamedElement, gen_database_ForeignKey_NamedElement, gen_database_ForeignKeyElement_DatabaseElement, gen_database_IndexElement_DatabaseElement, gen_database_Constraint_NamedElement, gen_database_Schema_TableContainer, gen_database_Sequence_NamedElement, gen_database_TableContainer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)