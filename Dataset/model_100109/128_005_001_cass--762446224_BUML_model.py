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
cassandra_Keyspace = Class(name="cassandra_Keyspace")
cassandra_SuperColumn = Class(name="cassandra_SuperColumn")
cassandra_ColumnFamily = Class(name="cassandra_ColumnFamily")
cassandra_Row = Class(name="cassandra_Row")
cassandra_Column = Class(name="cassandra_Column")
cassandra_FloatType = Class(name="cassandra_FloatType")
cassandra_BooleanType = Class(name="cassandra_BooleanType")
cassandra_UUIDType = Class(name="cassandra_UUIDType")
cassandra_DataType = Class(name="cassandra_DataType")
cassandra_IntegerType = Class(name="cassandra_IntegerType")
DataType = Class(name="DataType")
cassandra_UTF8Type = Class(name="cassandra_UTF8Type")
cassandra_AsciiType = Class(name="cassandra_AsciiType")
cassandra_DoubleType = Class(name="cassandra_DoubleType")
cassandra_CounterColumnType = Class(name="cassandra_CounterColumnType")
cassandra_DecimalType = Class(name="cassandra_DecimalType")
cassandra_BytesType = Class(name="cassandra_BytesType")
cassandra_DateType = Class(name="cassandra_DateType")

# cassandra_Keyspace class attributes and methods
cassandra_Keyspace_name: Property = Property(name="name", type=StringType)
cassandra_Keyspace.attributes={cassandra_Keyspace_name}

# cassandra_SuperColumn class attributes and methods
cassandra_SuperColumn_key: Property = Property(name="key", type=StringType)
cassandra_SuperColumn.attributes={cassandra_SuperColumn_key}

# cassandra_ColumnFamily class attributes and methods
cassandra_ColumnFamily_name: Property = Property(name="name", type=StringType)
cassandra_ColumnFamily.attributes={cassandra_ColumnFamily_name}

# cassandra_Row class attributes and methods
cassandra_Row_key: Property = Property(name="key", type=StringType)
cassandra_Row.attributes={cassandra_Row_key}

# cassandra_Column class attributes and methods
cassandra_Column_key: Property = Property(name="key", type=StringType)
cassandra_Column_timestamp: Property = Property(name="timestamp", type=StringType)
cassandra_Column.attributes={cassandra_Column_timestamp, cassandra_Column_key}

# cassandra_FloatType class attributes and methods
cassandra_FloatType_value: Property = Property(name="value", type=FloatType)
cassandra_FloatType.attributes={cassandra_FloatType_value}

# cassandra_BooleanType class attributes and methods
cassandra_BooleanType_value: Property = Property(name="value", type=BooleanType)
cassandra_BooleanType.attributes={cassandra_BooleanType_value}

# cassandra_UUIDType class attributes and methods
cassandra_UUIDType_value: Property = Property(name="value", type=StringType)
cassandra_UUIDType.attributes={cassandra_UUIDType_value}

# cassandra_DataType class attributes and methods

# cassandra_IntegerType class attributes and methods
cassandra_IntegerType_value: Property = Property(name="value", type=IntegerType)
cassandra_IntegerType.attributes={cassandra_IntegerType_value}

# DataType class attributes and methods

# cassandra_UTF8Type class attributes and methods
cassandra_UTF8Type_value: Property = Property(name="value", type=StringType)
cassandra_UTF8Type.attributes={cassandra_UTF8Type_value}

# cassandra_AsciiType class attributes and methods
cassandra_AsciiType_value: Property = Property(name="value", type=StringType)
cassandra_AsciiType.attributes={cassandra_AsciiType_value}

# cassandra_DoubleType class attributes and methods
cassandra_DoubleType_value: Property = Property(name="value", type=FloatType)
cassandra_DoubleType.attributes={cassandra_DoubleType_value}

# cassandra_CounterColumnType class attributes and methods
cassandra_CounterColumnType_value: Property = Property(name="value", type=StringType)
cassandra_CounterColumnType.attributes={cassandra_CounterColumnType_value}

# cassandra_DecimalType class attributes and methods
cassandra_DecimalType_value: Property = Property(name="value", type=StringType)
cassandra_DecimalType.attributes={cassandra_DecimalType_value}

# cassandra_BytesType class attributes and methods
cassandra_BytesType_value: Property = Property(name="value", type=StringType)
cassandra_BytesType.attributes={cassandra_BytesType_value}

# cassandra_DateType class attributes and methods
cassandra_DateType_value: Property = Property(name="value", type=StringType)
cassandra_DateType.attributes={cassandra_DateType_value}

# Relationships
supercolumns5: BinaryAssociation = BinaryAssociation(
    name="supercolumns5",
    ends={
        Property(name="cassandra_SuperColumn", type=cassandra_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_Row6", type=cassandra_SuperColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnfamilies0: BinaryAssociation = BinaryAssociation(
    name="columnfamilies0",
    ends={
        Property(name="cassandra_ColumnFamily", type=cassandra_Keyspace, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_Keyspace", type=cassandra_ColumnFamily, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rows1: BinaryAssociation = BinaryAssociation(
    name="rows1",
    ends={
        Property(name="cassandra_Row", type=cassandra_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_ColumnFamily2", type=cassandra_Row, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="cassandra_Column", type=cassandra_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_Row4", type=cassandra_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="cassandra_DataType", type=cassandra_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_Column8", type=cassandra_DataType, multiplicity=Multiplicity(1, 1))
    }
)
columns9: BinaryAssociation = BinaryAssociation(
    name="columns9",
    ends={
        Property(name="cassandra_Column11", type=cassandra_SuperColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="cassandra_SuperColumn10", type=cassandra_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_cassandra_FloatType_DataType = Generalization(general=DataType, specific=cassandra_FloatType)
gen_cassandra_BooleanType_DataType = Generalization(general=DataType, specific=cassandra_BooleanType)
gen_cassandra_UUIDType_DataType = Generalization(general=DataType, specific=cassandra_UUIDType)
gen_cassandra_IntegerType_DataType = Generalization(general=DataType, specific=cassandra_IntegerType)
gen_cassandra_UTF8Type_DataType = Generalization(general=DataType, specific=cassandra_UTF8Type)
gen_cassandra_AsciiType_DataType = Generalization(general=DataType, specific=cassandra_AsciiType)
gen_cassandra_DoubleType_DataType = Generalization(general=DataType, specific=cassandra_DoubleType)
gen_cassandra_CounterColumnType_DataType = Generalization(general=DataType, specific=cassandra_CounterColumnType)
gen_cassandra_DecimalType_DataType = Generalization(general=DataType, specific=cassandra_DecimalType)
gen_cassandra_BytesType_DataType = Generalization(general=DataType, specific=cassandra_BytesType)
gen_cassandra_DateType_DataType = Generalization(general=DataType, specific=cassandra_DateType)

# Domain Model
domain_model = DomainModel(
    name="cassandra",
    types={cassandra_Keyspace, cassandra_SuperColumn, cassandra_ColumnFamily, cassandra_Row, cassandra_Column, cassandra_FloatType, cassandra_BooleanType, cassandra_UUIDType, cassandra_DataType, cassandra_IntegerType, DataType, cassandra_UTF8Type, cassandra_AsciiType, cassandra_DoubleType, cassandra_CounterColumnType, cassandra_DecimalType, cassandra_BytesType, cassandra_DateType},
    associations={supercolumns5, columnfamilies0, rows1, columns3, value7, columns9},
    generalizations={gen_cassandra_FloatType_DataType, gen_cassandra_BooleanType_DataType, gen_cassandra_UUIDType_DataType, gen_cassandra_IntegerType_DataType, gen_cassandra_UTF8Type_DataType, gen_cassandra_AsciiType_DataType, gen_cassandra_DoubleType_DataType, gen_cassandra_CounterColumnType_DataType, gen_cassandra_DecimalType_DataType, gen_cassandra_BytesType_DataType, gen_cassandra_DateType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)