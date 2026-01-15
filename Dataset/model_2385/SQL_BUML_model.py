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
            EnumerationLiteral(name="VARCHAR255"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="NUMERIC")
    }
)

# Classes
sQL_DataBase = Class(name="sQL::DataBase")
sQL_Table = Class(name="sQL::Table")
sQL_column = Class(name="sQL::column")
sQL_primaryKey = Class(name="sQL::primaryKey")
sQL_foreignKey = Class(name="sQL::foreignKey")

# sQL_DataBase class attributes and methods

# sQL_Table class attributes and methods
sQL_Table_name: Property = Property(name="name", type=StringType)
sQL_Table.attributes={sQL_Table_name}

# sQL_column class attributes and methods
sQL_column_name: Property = Property(name="name", type=StringType)
sQL_column_type: Property = Property(name="type", type=StringType)
sQL_column.attributes={sQL_column_name, sQL_column_type}

# sQL_primaryKey class attributes and methods
sQL_primaryKey_name: Property = Property(name="name", type=StringType)
sQL_primaryKey.attributes={sQL_primaryKey_name}

# sQL_foreignKey class attributes and methods
sQL_foreignKey_name: Property = Property(name="name", type=StringType)
sQL_foreignKey.attributes={sQL_foreignKey_name}

# Relationships
reftable7: BinaryAssociation = BinaryAssociation(
    name="reftable7",
    ends={
        Property(name="sQL_Table9", type=sQL_foreignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_foreignKey8", type=sQL_Table, multiplicity=Multiplicity(0, 1))
    }
)
ref10: BinaryAssociation = BinaryAssociation(
    name="ref10",
    ends={
        Property(name="sQL_column12", type=sQL_foreignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_foreignKey11", type=sQL_column, multiplicity=Multiplicity(0, 1))
    }
)
Tables0: BinaryAssociation = BinaryAssociation(
    name="Tables0",
    ends={
        Property(name="sQL_Table", type=sQL_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_DataBase", type=sQL_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="sQL_column", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table2", type=sQL_column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey3: BinaryAssociation = BinaryAssociation(
    name="primaryKey3",
    ends={
        Property(name="sQL_primaryKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table4", type=sQL_primaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreignkeys5: BinaryAssociation = BinaryAssociation(
    name="foreignkeys5",
    ends={
        Property(name="sQL_foreignKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table6", type=sQL_foreignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sQL",
    types={sQL_DataBase, sQL_Table, sQL_column, sQL_primaryKey, sQL_foreignKey, DataType},
    associations={reftable7, ref10, Tables0, columns1, primaryKey3, foreignkeys5},
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