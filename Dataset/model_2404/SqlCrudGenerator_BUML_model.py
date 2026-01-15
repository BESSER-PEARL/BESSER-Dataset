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
ENUM_DATA_TYPE: Enumeration = Enumeration(
    name="ENUM_DATA_TYPE",
    literals={
            EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="VARYING"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="VARBINARY"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="VARBINARY_M"),
			EnumerationLiteral(name="BINARY_M"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="INTERVAL"),
			EnumerationLiteral(name="ARRAY"),
			EnumerationLiteral(name="MULTISET"),
			EnumerationLiteral(name="XML"),
			EnumerationLiteral(name="CHARACTER_M"),
			EnumerationLiteral(name="VARCHAR_M"),
			EnumerationLiteral(name="VARYING_M"),
			EnumerationLiteral(name="BOOLEAN_M"),
			EnumerationLiteral(name="TIMESTAMP_M"),
			EnumerationLiteral(name="INTEGER_M"),
			EnumerationLiteral(name="SMALLINT_M"),
			EnumerationLiteral(name="INT_M"),
			EnumerationLiteral(name="BIGINT_M"),
			EnumerationLiteral(name="DECIMAL_M"),
			EnumerationLiteral(name="NUMERIC_M"),
			EnumerationLiteral(name="FLOAT_M"),
			EnumerationLiteral(name="REAL_M"),
			EnumerationLiteral(name="DATE_M"),
			EnumerationLiteral(name="TIME_M"),
			EnumerationLiteral(name="INTERVAL_M"),
			EnumerationLiteral(name="ARRAY_M"),
			EnumerationLiteral(name="MULTISET_M"),
			EnumerationLiteral(name="XML_M")
    }
)

# Classes
sqlCrudGenerator_Schema = Class(name="sqlCrudGenerator::Schema")
sqlCrudGenerator_Table = Class(name="sqlCrudGenerator::Table")
sqlCrudGenerator_DataType = Class(name="sqlCrudGenerator::DataType")
sqlCrudGenerator_Column = Class(name="sqlCrudGenerator::Column")
sqlCrudGenerator_PrimaryKey = Class(name="sqlCrudGenerator::PrimaryKey")
sqlCrudGenerator_ForeignKey = Class(name="sqlCrudGenerator::ForeignKey")

# sqlCrudGenerator_Schema class attributes and methods
sqlCrudGenerator_Schema_name: Property = Property(name="name", type=StringType)
sqlCrudGenerator_Schema.attributes={sqlCrudGenerator_Schema_name}

# sqlCrudGenerator_Table class attributes and methods
sqlCrudGenerator_Table_name: Property = Property(name="name", type=StringType)
sqlCrudGenerator_Table.attributes={sqlCrudGenerator_Table_name}

# sqlCrudGenerator_DataType class attributes and methods
sqlCrudGenerator_DataType_dataType: Property = Property(name="dataType", type=StringType)
sqlCrudGenerator_DataType_precision: Property = Property(name="precision", type=IntegerType)
sqlCrudGenerator_DataType.attributes={sqlCrudGenerator_DataType_precision, sqlCrudGenerator_DataType_dataType}

# sqlCrudGenerator_Column class attributes and methods
sqlCrudGenerator_Column_name: Property = Property(name="name", type=StringType)
sqlCrudGenerator_Column.attributes={sqlCrudGenerator_Column_name}

# sqlCrudGenerator_PrimaryKey class attributes and methods

# sqlCrudGenerator_ForeignKey class attributes and methods

# Relationships
foreignsKeys5: BinaryAssociation = BinaryAssociation(
    name="foreignsKeys5",
    ends={
        Property(name="sqlCrudGenerator_Table6", type=sqlCrudGenerator_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sqlCrudGenerator_ForeignKey", type=sqlCrudGenerator_Table, multiplicity=Multiplicity(1, 1))
    }
)
dataType7: BinaryAssociation = BinaryAssociation(
    name="dataType7",
    ends={
        Property(name="sqlCrudGenerator_DataType", type=sqlCrudGenerator_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_Column8", type=sqlCrudGenerator_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ids9: BinaryAssociation = BinaryAssociation(
    name="ids9",
    ends={
        Property(name="sqlCrudGenerator_Column11", type=sqlCrudGenerator_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_PrimaryKey10", type=sqlCrudGenerator_Column, multiplicity=Multiplicity(0, 9999))
    }
)
refsTo12: BinaryAssociation = BinaryAssociation(
    name="refsTo12",
    ends={
        Property(name="sqlCrudGenerator_Column14", type=sqlCrudGenerator_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_ForeignKey13", type=sqlCrudGenerator_Column, multiplicity=Multiplicity(0, 1))
    }
)
reference15: BinaryAssociation = BinaryAssociation(
    name="reference15",
    ends={
        Property(name="sqlCrudGenerator_Table17", type=sqlCrudGenerator_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_ForeignKey16", type=sqlCrudGenerator_Table, multiplicity=Multiplicity(0, 1))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="sqlCrudGenerator_Table", type=sqlCrudGenerator_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_Schema", type=sqlCrudGenerator_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refsFrom18: BinaryAssociation = BinaryAssociation(
    name="refsFrom18",
    ends={
        Property(name="sqlCrudGenerator_Column20", type=sqlCrudGenerator_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_ForeignKey19", type=sqlCrudGenerator_Column, multiplicity=Multiplicity(0, 1))
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="sqlCrudGenerator_Column", type=sqlCrudGenerator_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_Table2", type=sqlCrudGenerator_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey3: BinaryAssociation = BinaryAssociation(
    name="primaryKey3",
    ends={
        Property(name="sqlCrudGenerator_PrimaryKey", type=sqlCrudGenerator_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlCrudGenerator_Table4", type=sqlCrudGenerator_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sqlCrudGenerator",
    types={sqlCrudGenerator_Schema, sqlCrudGenerator_Table, sqlCrudGenerator_DataType, sqlCrudGenerator_Column, sqlCrudGenerator_PrimaryKey, sqlCrudGenerator_ForeignKey, ENUM_DATA_TYPE},
    associations={foreignsKeys5, dataType7, ids9, refsTo12, reference15, tables0, refsFrom18, columns1, primaryKey3},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)