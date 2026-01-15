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
database_DataBase = Class(name="database::DataBase")
database_Table = Class(name="database::Table")
NamedElement = Class(name="NamedElement")
database_Column = Class(name="database::Column")
database_Index = Class(name="database::Index")
database_PrimaryKey = Class(name="database::PrimaryKey")
database_Unique = Class(name="database::Unique")
Index = Class(name="Index")
database_NamedElement = Class(name="database::NamedElement", is_abstract=True)

# database_DataBase class attributes and methods
database_DataBase_m_getTable: Method = Method(name="getTable", parameters={Parameter(name='tableName')}, type=StringType)
database_DataBase.methods={database_DataBase_m_getTable}

# database_Table class attributes and methods
database_Table_storageEngine: Property = Property(name="storageEngine", type=StringType)
database_Table_collation: Property = Property(name="collation", type=StringType)
database_Table_m_getColumn: Method = Method(name="getColumn", parameters={Parameter(name='columnName')}, type=StringType)
database_Table_m_getIndex: Method = Method(name="getIndex", parameters={Parameter(name='indexName')}, type=StringType)
database_Table.attributes={database_Table_collation, database_Table_storageEngine}
database_Table.methods={database_Table_m_getIndex, database_Table_m_getColumn}

# NamedElement class attributes and methods

# database_Column class attributes and methods
database_Column_type: Property = Property(name="type", type=StringType)
database_Column_nullable: Property = Property(name="nullable", type=BooleanType)
database_Column_default: Property = Property(name="default", type=StringType)
database_Column_length: Property = Property(name="length", type=IntegerType)
database_Column_collation: Property = Property(name="collation", type=StringType)
database_Column.attributes={database_Column_type, database_Column_collation, database_Column_default, database_Column_nullable, database_Column_length}

# database_Index class attributes and methods

# database_PrimaryKey class attributes and methods

# database_Unique class attributes and methods

# Index class attributes and methods

# database_NamedElement class attributes and methods
database_NamedElement_name: Property = Property(name="name", type=StringType)
database_NamedElement.attributes={database_NamedElement_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="database_Table", type=database_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DataBase", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataBase1: BinaryAssociation = BinaryAssociation(
    name="dataBase1",
    ends={
        Property(name="database_DataBase3", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table2", type=database_DataBase, multiplicity=Multiplicity(0, 1))
    }
)
columns4: BinaryAssociation = BinaryAssociation(
    name="columns4",
    ends={
        Property(name="database_Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table5", type=database_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
indexes6: BinaryAssociation = BinaryAssociation(
    name="indexes6",
    ends={
        Property(name="database_Index", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table7", type=database_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey8: BinaryAssociation = BinaryAssociation(
    name="primaryKey8",
    ends={
        Property(name="database_PrimaryKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table9", type=database_PrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
uniques10: BinaryAssociation = BinaryAssociation(
    name="uniques10",
    ends={
        Property(name="database_Unique", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table11", type=database_Unique, multiplicity=Multiplicity(0, 9999))
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="database_Column14", type=database_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Index13", type=database_Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_database_Table_NamedElement = Generalization(general=NamedElement, specific=database_Table)
gen_database_Column_NamedElement = Generalization(general=NamedElement, specific=database_Column)
gen_database_PrimaryKey_Index = Generalization(general=Index, specific=database_PrimaryKey)
gen_database_Index_NamedElement = Generalization(general=NamedElement, specific=database_Index)
gen_database_Unique_Index = Generalization(general=Index, specific=database_Unique)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_DataBase, database_Table, NamedElement, database_Column, database_Index, database_PrimaryKey, database_Unique, Index, database_NamedElement},
    associations={tables0, dataBase1, columns4, indexes6, primaryKey8, uniques10, columns12},
    generalizations={gen_database_Table_NamedElement, gen_database_Column_NamedElement, gen_database_PrimaryKey_Index, gen_database_Index_NamedElement, gen_database_Unique_Index},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)