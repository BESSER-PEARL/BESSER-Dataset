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
database_Column = Class(name="database::Column")
database_TableContainer = Class(name="database::TableContainer", is_abstract=True)
database_NamedElement = Class(name="database::NamedElement", is_abstract=True)
DatabaseElement = Class(name="DatabaseElement")
database_DataBase = Class(name="database::DataBase")
TableContainer = Class(name="TableContainer")
TypesLibraryUser = Class(name="TypesLibraryUser")
database_Schema = Class(name="database::Schema")
database_UserDefinedTypesLibrary = Class(name="database::UserDefinedTypesLibrary")
database_AbstractTable = Class(name="database::AbstractTable", is_abstract=True)
NamedElement = Class(name="NamedElement")
database_Type = Class(name="database::Type")
database_Sequence = Class(name="database::Sequence")
database_Index = Class(name="database::Index")
database_IndexElement = Class(name="database::IndexElement")
database_PrimaryKey = Class(name="database::PrimaryKey")
database_ForeignKey = Class(name="database::ForeignKey")
database_ForeignKeyElement = Class(name="database::ForeignKeyElement")
AbstractTable = Class(name="AbstractTable")
database_Table = Class(name="database::Table")
database_View = Class(name="database::View")
database_Constraint = Class(name="database::Constraint")
database_DatabaseElement = Class(name="database::DatabaseElement", is_abstract=True)

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
database_Column.attributes={database_Column_defaultValue, database_Column_nullable, database_Column_autoincrement, database_Column_inForeignKey, database_Column_unique, database_Column_inPrimaryKey}
database_Column.methods={database_Column_m_addToUniqueIndex, database_Column_m_removeFromUniqueIndex, database_Column_m_addToPrimaryKey, database_Column_m_removeFromPrimaryKey}

# database_TableContainer class attributes and methods

# database_NamedElement class attributes and methods
database_NamedElement_name: Property = Property(name="name", type=StringType)
database_NamedElement.attributes={database_NamedElement_name}

# DatabaseElement class attributes and methods

# database_DataBase class attributes and methods
database_DataBase_url: Property = Property(name="url", type=StringType)
database_DataBase.attributes={database_DataBase_url}

# TableContainer class attributes and methods

# TypesLibraryUser class attributes and methods

# database_Schema class attributes and methods

# database_UserDefinedTypesLibrary class attributes and methods

# database_AbstractTable class attributes and methods

# NamedElement class attributes and methods

# database_Type class attributes and methods

# database_Sequence class attributes and methods
database_Sequence_start: Property = Property(name="start", type=IntegerType)
database_Sequence_increment: Property = Property(name="increment", type=IntegerType)
database_Sequence_minValue: Property = Property(name="minValue", type=IntegerType)
database_Sequence_maxValue: Property = Property(name="maxValue", type=IntegerType)
database_Sequence.attributes={database_Sequence_increment, database_Sequence_minValue, database_Sequence_maxValue, database_Sequence_start}

# database_Index class attributes and methods
database_Index_qualifier: Property = Property(name="qualifier", type=StringType)
database_Index_unique: Property = Property(name="unique", type=BooleanType)
database_Index_cardinality: Property = Property(name="cardinality", type=IntegerType)
database_Index_indexType: Property = Property(name="indexType", type=StringType)
database_Index.attributes={database_Index_indexType, database_Index_qualifier, database_Index_cardinality, database_Index_unique}

# database_IndexElement class attributes and methods
database_IndexElement_asc: Property = Property(name="asc", type=BooleanType)
database_IndexElement.attributes={database_IndexElement_asc}

# database_PrimaryKey class attributes and methods

# database_ForeignKey class attributes and methods
database_ForeignKey_m_getSourceTable: Method = Method(name="getSourceTable", parameters={}, type=StringType)
database_ForeignKey_m_getTargetTable: Method = Method(name="getTargetTable", parameters={}, type=StringType)
database_ForeignKey.methods={database_ForeignKey_m_getSourceTable, database_ForeignKey_m_getTargetTable}

# database_ForeignKeyElement class attributes and methods

# AbstractTable class attributes and methods

# database_Table class attributes and methods

# database_View class attributes and methods
database_View_query: Property = Property(name="query", type=StringType)
database_View.attributes={database_View_query}

# database_Constraint class attributes and methods
database_Constraint_expression: Property = Property(name="expression", type=StringType)
database_Constraint.attributes={database_Constraint_expression}

# database_DatabaseElement class attributes and methods
database_DatabaseElement_ID: Property = Property(name="ID", type=StringType)
database_DatabaseElement_comments: Property = Property(name="comments", type=StringType)
database_DatabaseElement.attributes={database_DatabaseElement_comments, database_DatabaseElement_ID}

# Relationships
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="Column", type=database_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="TableContainer", type=database_AbstractTable, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=database_TableContainer, multiplicity=Multiplicity(1, 1))
    }
)
schemas0: BinaryAssociation = BinaryAssociation(
    name="schemas0",
    ends={
        Property(name="database_Schema", type=database_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DataBase", type=database_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defines1: BinaryAssociation = BinaryAssociation(
    name="defines1",
    ends={
        Property(name="database_UserDefinedTypesLibrary", type=database_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DataBase2", type=database_UserDefinedTypesLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="database_Type", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column12", type=database_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence13: BinaryAssociation = BinaryAssociation(
    name="sequence13",
    ends={
        Property(name="database_Sequence", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column14", type=database_Sequence, multiplicity=Multiplicity(0, 1))
    }
)
indexes5: BinaryAssociation = BinaryAssociation(
    name="indexes5",
    ends={
        Property(name="database_Index", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column", type=database_Index, multiplicity=Multiplicity(0, 9999))
    }
)
indexElements6: BinaryAssociation = BinaryAssociation(
    name="indexElements6",
    ends={
        Property(name="IndexElement", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=database_IndexElement, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey7: BinaryAssociation = BinaryAssociation(
    name="primaryKey7",
    ends={
        Property(name="PrimaryKey", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=database_PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
foreignKeys8: BinaryAssociation = BinaryAssociation(
    name="foreignKeys8",
    ends={
        Property(name="database_ForeignKey", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column9", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKeyElements10: BinaryAssociation = BinaryAssociation(
    name="foreignKeyElements10",
    ends={
        Property(name="ForeignKeyElement", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="fkColumn", type=database_ForeignKeyElement, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey20: BinaryAssociation = BinaryAssociation(
    name="primaryKey20",
    ends={
        Property(name="PrimaryKey22", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=database_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="AbstractTable", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns16", type=database_AbstractTable, multiplicity=Multiplicity(1, 1))
    }
)
elements17: BinaryAssociation = BinaryAssociation(
    name="elements17",
    ends={
        Property(name="database_IndexElement", type=database_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Index18", type=database_IndexElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner19: BinaryAssociation = BinaryAssociation(
    name="owner19",
    ends={
        Property(name="Table", type=database_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
elements34: BinaryAssociation = BinaryAssociation(
    name="elements34",
    ends={
        Property(name="database_ForeignKeyElement", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey35", type=database_ForeignKeyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner36: BinaryAssociation = BinaryAssociation(
    name="owner36",
    ends={
        Property(name="Table37", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="database_Table", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey39", type=database_Table, multiplicity=Multiplicity(0, 1))
    }
)
foreignKeys23: BinaryAssociation = BinaryAssociation(
    name="foreignKeys23",
    ends={
        Property(name="ForeignKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner24", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints25: BinaryAssociation = BinaryAssociation(
    name="constraints25",
    ends={
        Property(name="Constraint", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner26", type=database_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes27: BinaryAssociation = BinaryAssociation(
    name="indexes27",
    ends={
        Property(name="Index", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner28", type=database_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns29: BinaryAssociation = BinaryAssociation(
    name="columns29",
    ends={
        Property(name="Column30", type=database_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey", type=database_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner31: BinaryAssociation = BinaryAssociation(
    name="owner31",
    ends={
        Property(name="Table33", type=database_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey32", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
fkColumn40: BinaryAssociation = BinaryAssociation(
    name="fkColumn40",
    ends={
        Property(name="Column41", type=database_ForeignKeyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeyElements", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
pkColumn42: BinaryAssociation = BinaryAssociation(
    name="pkColumn42",
    ends={
        Property(name="database_Column44", type=database_ForeignKeyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKeyElement43", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
column45: BinaryAssociation = BinaryAssociation(
    name="column45",
    ends={
        Property(name="Column46", type=database_IndexElement, multiplicity=Multiplicity(1, 1)),
        Property(name="indexElements", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)
owner47: BinaryAssociation = BinaryAssociation(
    name="owner47",
    ends={
        Property(name="Table48", type=database_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
tables49: BinaryAssociation = BinaryAssociation(
    name="tables49",
    ends={
        Property(name="AbstractTable51", type=database_TableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner50", type=database_AbstractTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequences52: BinaryAssociation = BinaryAssociation(
    name="sequences52",
    ends={
        Property(name="database_Sequence53", type=database_TableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableContainer", type=database_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_database_Column_NamedElement = Generalization(general=NamedElement, specific=database_Column)
gen_database_NamedElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_NamedElement)
gen_database_DataBase_TableContainer = Generalization(general=TableContainer, specific=database_DataBase)
gen_database_DataBase_TypesLibraryUser = Generalization(general=TypesLibraryUser, specific=database_DataBase)
gen_database_AbstractTable_NamedElement = Generalization(general=NamedElement, specific=database_AbstractTable)
gen_database_View_AbstractTable = Generalization(general=AbstractTable, specific=database_View)
gen_database_Table_AbstractTable = Generalization(general=AbstractTable, specific=database_Table)
gen_database_Index_NamedElement = Generalization(general=NamedElement, specific=database_Index)
gen_database_PrimaryKey_NamedElement = Generalization(general=NamedElement, specific=database_PrimaryKey)
gen_database_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=database_ForeignKey)
gen_database_Schema_TableContainer = Generalization(general=TableContainer, specific=database_Schema)
gen_database_Sequence_NamedElement = Generalization(general=NamedElement, specific=database_Sequence)
gen_database_ForeignKeyElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_ForeignKeyElement)
gen_database_IndexElement_DatabaseElement = Generalization(general=DatabaseElement, specific=database_IndexElement)
gen_database_Constraint_NamedElement = Generalization(general=NamedElement, specific=database_Constraint)
gen_database_TableContainer_NamedElement = Generalization(general=NamedElement, specific=database_TableContainer)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_Column, database_TableContainer, database_NamedElement, DatabaseElement, database_DataBase, TableContainer, TypesLibraryUser, database_Schema, database_UserDefinedTypesLibrary, database_AbstractTable, NamedElement, database_Type, database_Sequence, database_Index, database_IndexElement, database_PrimaryKey, database_ForeignKey, database_ForeignKeyElement, AbstractTable, database_Table, database_View, database_Constraint, database_DatabaseElement},
    associations={columns3, owner4, schemas0, defines1, type11, sequence13, indexes5, indexElements6, primaryKey7, foreignKeys8, foreignKeyElements10, primaryKey20, owner15, elements17, owner19, elements34, owner36, target38, foreignKeys23, constraints25, indexes27, columns29, owner31, fkColumn40, pkColumn42, column45, owner47, tables49, sequences52},
    generalizations={gen_database_Column_NamedElement, gen_database_NamedElement_DatabaseElement, gen_database_DataBase_TableContainer, gen_database_DataBase_TypesLibraryUser, gen_database_AbstractTable_NamedElement, gen_database_View_AbstractTable, gen_database_Table_AbstractTable, gen_database_Index_NamedElement, gen_database_PrimaryKey_NamedElement, gen_database_ForeignKey_NamedElement, gen_database_Schema_TableContainer, gen_database_Sequence_NamedElement, gen_database_ForeignKeyElement_DatabaseElement, gen_database_IndexElement_DatabaseElement, gen_database_Constraint_NamedElement, gen_database_TableContainer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)