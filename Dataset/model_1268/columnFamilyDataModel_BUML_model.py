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
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="BOOLEAN")
    }
)

# Classes
columnFamilyDataModel_ColumnFamilyDataModel = Class(name="columnFamilyDataModel::ColumnFamilyDataModel")
columnFamilyDataModel_Table = Class(name="columnFamilyDataModel::Table")
columnFamilyDataModel_ColumnFamily = Class(name="columnFamilyDataModel::ColumnFamily")
columnFamilyDataModel_SimpleType = Class(name="columnFamilyDataModel::SimpleType")
Type = Class(name="Type")
columnFamilyDataModel_Collection = Class(name="columnFamilyDataModel::Collection", is_abstract=True)
columnFamilyDataModel_List = Class(name="columnFamilyDataModel::List")
Collection = Class(name="Collection")
columnFamilyDataModel_Set = Class(name="columnFamilyDataModel::Set")
columnFamilyDataModel_Map = Class(name="columnFamilyDataModel::Map")
columnFamilyDataModel_Tuple = Class(name="columnFamilyDataModel::Tuple")
columnFamilyDataModel_UserDefinedType = Class(name="columnFamilyDataModel::UserDefinedType")
columnFamilyDataModel_Field = Class(name="columnFamilyDataModel::Field")
columnFamilyDataModel_Column = Class(name="columnFamilyDataModel::Column")
columnFamilyDataModel_PartitionKey = Class(name="columnFamilyDataModel::PartitionKey")
columnFamilyDataModel_ClusteringKey = Class(name="columnFamilyDataModel::ClusteringKey")
columnFamilyDataModel_Type = Class(name="columnFamilyDataModel::Type", is_abstract=True)
columnFamilyDataModel_Key = Class(name="columnFamilyDataModel::Key", is_abstract=True)
Key = Class(name="Key")

# columnFamilyDataModel_ColumnFamilyDataModel class attributes and methods

# columnFamilyDataModel_Table class attributes and methods
columnFamilyDataModel_Table_name: Property = Property(name="name", type=StringType)
columnFamilyDataModel_Table.attributes={columnFamilyDataModel_Table_name}

# columnFamilyDataModel_ColumnFamily class attributes and methods
columnFamilyDataModel_ColumnFamily_name: Property = Property(name="name", type=StringType)
columnFamilyDataModel_ColumnFamily.attributes={columnFamilyDataModel_ColumnFamily_name}

# columnFamilyDataModel_SimpleType class attributes and methods
columnFamilyDataModel_SimpleType_type: Property = Property(name="type", type=StringType)
columnFamilyDataModel_SimpleType.attributes={columnFamilyDataModel_SimpleType_type}

# Type class attributes and methods

# columnFamilyDataModel_Collection class attributes and methods
columnFamilyDataModel_Collection_type: Property = Property(name="type", type=StringType)
columnFamilyDataModel_Collection.attributes={columnFamilyDataModel_Collection_type}

# columnFamilyDataModel_List class attributes and methods

# Collection class attributes and methods

# columnFamilyDataModel_Set class attributes and methods

# columnFamilyDataModel_Map class attributes and methods
columnFamilyDataModel_Map_keyType: Property = Property(name="keyType", type=StringType)
columnFamilyDataModel_Map.attributes={columnFamilyDataModel_Map_keyType}

# columnFamilyDataModel_Tuple class attributes and methods
columnFamilyDataModel_Tuple_types: Property = Property(name="types", type=StringType)
columnFamilyDataModel_Tuple.attributes={columnFamilyDataModel_Tuple_types}

# columnFamilyDataModel_UserDefinedType class attributes and methods
columnFamilyDataModel_UserDefinedType_name: Property = Property(name="name", type=StringType)
columnFamilyDataModel_UserDefinedType.attributes={columnFamilyDataModel_UserDefinedType_name}

# columnFamilyDataModel_Field class attributes and methods
columnFamilyDataModel_Field_name: Property = Property(name="name", type=StringType)
columnFamilyDataModel_Field.attributes={columnFamilyDataModel_Field_name}

# columnFamilyDataModel_Column class attributes and methods
columnFamilyDataModel_Column_name: Property = Property(name="name", type=StringType)
columnFamilyDataModel_Column.attributes={columnFamilyDataModel_Column_name}

# columnFamilyDataModel_PartitionKey class attributes and methods

# columnFamilyDataModel_ClusteringKey class attributes and methods

# columnFamilyDataModel_Type class attributes and methods

# columnFamilyDataModel_Key class attributes and methods

# Key class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="columnFamilyDataModel_Table", type=columnFamilyDataModel_ColumnFamilyDataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_ColumnFamilyDataModel", type=columnFamilyDataModel_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields14: BinaryAssociation = BinaryAssociation(
    name="fields14",
    ends={
        Property(name="columnFamilyDataModel_Field", type=columnFamilyDataModel_UserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_UserDefinedType", type=columnFamilyDataModel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnFamilies1: BinaryAssociation = BinaryAssociation(
    name="columnFamilies1",
    ends={
        Property(name="columnFamilyDataModel_ColumnFamily", type=columnFamilyDataModel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Table2", type=columnFamilyDataModel_ColumnFamily, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="columnFamilyDataModel_Column", type=columnFamilyDataModel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Table4", type=columnFamilyDataModel_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partitionKeys5: BinaryAssociation = BinaryAssociation(
    name="partitionKeys5",
    ends={
        Property(name="columnFamilyDataModel_PartitionKey", type=columnFamilyDataModel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Table6", type=columnFamilyDataModel_PartitionKey, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clusteringKeys7: BinaryAssociation = BinaryAssociation(
    name="clusteringKeys7",
    ends={
        Property(name="columnFamilyDataModel_ClusteringKey", type=columnFamilyDataModel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Table8", type=columnFamilyDataModel_ClusteringKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="columnFamilyDataModel_Type", type=columnFamilyDataModel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Column10", type=columnFamilyDataModel_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnFamily11: BinaryAssociation = BinaryAssociation(
    name="columnFamily11",
    ends={
        Property(name="columnFamilyDataModel_ColumnFamily13", type=columnFamilyDataModel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Column12", type=columnFamilyDataModel_ColumnFamily, multiplicity=Multiplicity(0, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="columnFamilyDataModel_Type17", type=columnFamilyDataModel_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Field16", type=columnFamilyDataModel_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
column18: BinaryAssociation = BinaryAssociation(
    name="column18",
    ends={
        Property(name="columnFamilyDataModel_Column19", type=columnFamilyDataModel_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="columnFamilyDataModel_Key", type=columnFamilyDataModel_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_columnFamilyDataModel_SimpleType_Type = Generalization(general=Type, specific=columnFamilyDataModel_SimpleType)
gen_columnFamilyDataModel_Collection_Type = Generalization(general=Type, specific=columnFamilyDataModel_Collection)
gen_columnFamilyDataModel_List_Collection = Generalization(general=Collection, specific=columnFamilyDataModel_List)
gen_columnFamilyDataModel_Set_Collection = Generalization(general=Collection, specific=columnFamilyDataModel_Set)
gen_columnFamilyDataModel_Map_Collection = Generalization(general=Collection, specific=columnFamilyDataModel_Map)
gen_columnFamilyDataModel_Tuple_Type = Generalization(general=Type, specific=columnFamilyDataModel_Tuple)
gen_columnFamilyDataModel_UserDefinedType_Type = Generalization(general=Type, specific=columnFamilyDataModel_UserDefinedType)
gen_columnFamilyDataModel_PartitionKey_Key = Generalization(general=Key, specific=columnFamilyDataModel_PartitionKey)
gen_columnFamilyDataModel_ClusteringKey_Key = Generalization(general=Key, specific=columnFamilyDataModel_ClusteringKey)

# Domain Model
domain_model = DomainModel(
    name="columnFamilyDataModel",
    types={columnFamilyDataModel_ColumnFamilyDataModel, columnFamilyDataModel_Table, columnFamilyDataModel_ColumnFamily, columnFamilyDataModel_SimpleType, Type, columnFamilyDataModel_Collection, columnFamilyDataModel_List, Collection, columnFamilyDataModel_Set, columnFamilyDataModel_Map, columnFamilyDataModel_Tuple, columnFamilyDataModel_UserDefinedType, columnFamilyDataModel_Field, columnFamilyDataModel_Column, columnFamilyDataModel_PartitionKey, columnFamilyDataModel_ClusteringKey, columnFamilyDataModel_Type, columnFamilyDataModel_Key, Key, PrimitiveType},
    associations={tables0, fields14, columnFamilies1, columns3, partitionKeys5, clusteringKeys7, type9, columnFamily11, type15, column18},
    generalizations={gen_columnFamilyDataModel_SimpleType_Type, gen_columnFamilyDataModel_Collection_Type, gen_columnFamilyDataModel_List_Collection, gen_columnFamilyDataModel_Set_Collection, gen_columnFamilyDataModel_Map_Collection, gen_columnFamilyDataModel_Tuple_Type, gen_columnFamilyDataModel_UserDefinedType_Type, gen_columnFamilyDataModel_PartitionKey_Key, gen_columnFamilyDataModel_ClusteringKey_Key},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)