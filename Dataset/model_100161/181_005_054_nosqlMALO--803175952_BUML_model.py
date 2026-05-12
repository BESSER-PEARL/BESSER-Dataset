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
PrimitiveTypeType: Enumeration = Enumeration(
    name="PrimitiveTypeType",
    literals={
            EnumerationLiteral(name="ascii"),
			EnumerationLiteral(name="bigint"),
			EnumerationLiteral(name="blob"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="counter"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="inet"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="timestamp"),
			EnumerationLiteral(name="timeuuid"),
			EnumerationLiteral(name="uuid"),
			EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="varint")
    }
)

ReplicaPlacementStrategies: Enumeration = Enumeration(
    name="ReplicaPlacementStrategies",
    literals={
            EnumerationLiteral(name="SimpleStrategy"),
			EnumerationLiteral(name="OldNetworkTopologyStrategy"),
			EnumerationLiteral(name="NetworkTopologyStrategy")
    }
)

CollectionTypeType: Enumeration = Enumeration(
    name="CollectionTypeType",
    literals={
            EnumerationLiteral(name="set"),
			EnumerationLiteral(name="list")
    }
)

# Classes
nosql_KeySpace = Class(name="nosql_KeySpace")
nosql_Column = Class(name="nosql_Column")
nosql_Type = Class(name="nosql_Type", is_abstract=True)
nosql_ColumnFamily = Class(name="nosql_ColumnFamily", is_abstract=True)
nosql_DataStructureType = Class(name="nosql_DataStructureType", is_abstract=True)
nosql_MapType = Class(name="nosql_MapType")
DataStructureType = Class(name="DataStructureType")
nosql_CollectionType = Class(name="nosql_CollectionType")
nosql_DynamicColumnFamily = Class(name="nosql_DynamicColumnFamily")
ColumnFamily = Class(name="ColumnFamily")
nosql_StaticColumnFamily = Class(name="nosql_StaticColumnFamily")
nosql_PrimitiveType = Class(name="nosql_PrimitiveType")
Type = Class(name="Type")

# nosql_KeySpace class attributes and methods
nosql_KeySpace_name: Property = Property(name="name", type=StringType)
nosql_KeySpace_replicationFactor: Property = Property(name="replicationFactor", type=StringType)
nosql_KeySpace_replicaPlacementStrategy: Property = Property(name="replicaPlacementStrategy", type=StringType)
nosql_KeySpace.attributes={nosql_KeySpace_replicationFactor, nosql_KeySpace_replicaPlacementStrategy, nosql_KeySpace_name}

# nosql_Column class attributes and methods
nosql_Column_name: Property = Property(name="name", type=StringType)
nosql_Column.attributes={nosql_Column_name}

# nosql_Type class attributes and methods

# nosql_ColumnFamily class attributes and methods
nosql_ColumnFamily_name: Property = Property(name="name", type=StringType)
nosql_ColumnFamily.attributes={nosql_ColumnFamily_name}

# nosql_DataStructureType class attributes and methods

# nosql_MapType class attributes and methods
nosql_MapType_keyType: Property = Property(name="keyType", type=StringType)
nosql_MapType_baseType: Property = Property(name="baseType", type=StringType)
nosql_MapType.attributes={nosql_MapType_keyType, nosql_MapType_baseType}

# DataStructureType class attributes and methods

# nosql_CollectionType class attributes and methods
nosql_CollectionType_kind: Property = Property(name="kind", type=StringType)
nosql_CollectionType_keyType: Property = Property(name="keyType", type=StringType)
nosql_CollectionType.attributes={nosql_CollectionType_kind, nosql_CollectionType_keyType}

# nosql_DynamicColumnFamily class attributes and methods

# ColumnFamily class attributes and methods

# nosql_StaticColumnFamily class attributes and methods

# nosql_PrimitiveType class attributes and methods
nosql_PrimitiveType_kind: Property = Property(name="kind", type=StringType)
nosql_PrimitiveType.attributes={nosql_PrimitiveType_kind}

# Type class attributes and methods

# Relationships
columns4: BinaryAssociation = BinaryAssociation(
    name="columns4",
    ends={
        Property(name="nosql_Column", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily5", type=nosql_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKey6: BinaryAssociation = BinaryAssociation(
    name="primaryKey6",
    ends={
        Property(name="nosql_Column8", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily7", type=nosql_Column, multiplicity=Multiplicity(1, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="nosql_Type", type=nosql_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Column10", type=nosql_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columnFamilies0: BinaryAssociation = BinaryAssociation(
    name="columnFamilies0",
    ends={
        Property(name="nosql_ColumnFamily", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace", type=nosql_ColumnFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyspace1: BinaryAssociation = BinaryAssociation(
    name="keyspace1",
    ends={
        Property(name="nosql_KeySpace3", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily2", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1))
    }
)
clusteringKey11: BinaryAssociation = BinaryAssociation(
    name="clusteringKey11",
    ends={
        Property(name="nosql_Column12", type=nosql_DynamicColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_DynamicColumnFamily", type=nosql_Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_nosql_DataStructureType_Type = Generalization(general=Type, specific=nosql_DataStructureType)
gen_nosql_MapType_DataStructureType = Generalization(general=DataStructureType, specific=nosql_MapType)
gen_nosql_CollectionType_DataStructureType = Generalization(general=DataStructureType, specific=nosql_CollectionType)
gen_nosql_DynamicColumnFamily_ColumnFamily = Generalization(general=ColumnFamily, specific=nosql_DynamicColumnFamily)
gen_nosql_StaticColumnFamily_ColumnFamily = Generalization(general=ColumnFamily, specific=nosql_StaticColumnFamily)
gen_nosql_PrimitiveType_Type = Generalization(general=Type, specific=nosql_PrimitiveType)

# Domain Model
domain_model = DomainModel(
    name="nosql",
    types={nosql_KeySpace, nosql_Column, nosql_Type, nosql_ColumnFamily, nosql_DataStructureType, nosql_MapType, DataStructureType, nosql_CollectionType, nosql_DynamicColumnFamily, ColumnFamily, nosql_StaticColumnFamily, nosql_PrimitiveType, Type, PrimitiveTypeType, ReplicaPlacementStrategies, CollectionTypeType},
    associations={columns4, primaryKey6, type9, columnFamilies0, keyspace1, clusteringKey11},
    generalizations={gen_nosql_DataStructureType_Type, gen_nosql_MapType_DataStructureType, gen_nosql_CollectionType_DataStructureType, gen_nosql_DynamicColumnFamily_ColumnFamily, gen_nosql_StaticColumnFamily_ColumnFamily, gen_nosql_PrimitiveType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)