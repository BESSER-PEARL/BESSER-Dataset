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
			EnumerationLiteral(name="INT")
    }
)

# Classes
sql_Model = Class(name="sql::Model")
sql_Database = Class(name="sql::Database")
sql_Table = Class(name="sql::Table")
sql_EObject = Class(name="sql::EObject")
sql_Column = Class(name="sql::Column")
sql_PrimaryKey = Class(name="sql::PrimaryKey")
sql_ForeignKey = Class(name="sql::ForeignKey")

# sql_Model class attributes and methods

# sql_Database class attributes and methods

# sql_Table class attributes and methods
sql_Table_name: Property = Property(name="name", type=StringType)
sql_Table.attributes={sql_Table_name}

# sql_EObject class attributes and methods

# sql_Column class attributes and methods
sql_Column_name: Property = Property(name="name", type=StringType)
sql_Column_type: Property = Property(name="type", type=StringType)
sql_Column_isNotNull: Property = Property(name="isNotNull", type=BooleanType)
sql_Column.attributes={sql_Column_isNotNull, sql_Column_type, sql_Column_name}

# sql_PrimaryKey class attributes and methods

# sql_ForeignKey class attributes and methods

# Relationships
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="sql_Database2", type=sql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sql_Table", type=sql_Database, multiplicity=Multiplicity(1, 1))
    }
)
database0: BinaryAssociation = BinaryAssociation(
    name="database0",
    ends={
        Property(name="sql_Database", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model", type=sql_Database, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facts3: BinaryAssociation = BinaryAssociation(
    name="facts3",
    ends={
        Property(name="sql_EObject", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Table4", type=sql_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localColumns6: BinaryAssociation = BinaryAssociation(
    name="localColumns6",
    ends={
        Property(name="sql_Column7", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ForeignKey", type=sql_Column, multiplicity=Multiplicity(0, 9999))
    }
)
col5: BinaryAssociation = BinaryAssociation(
    name="col5",
    ends={
        Property(name="sql_Column", type=sql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PrimaryKey", type=sql_Column, multiplicity=Multiplicity(0, 9999))
    }
)
foreignTable8: BinaryAssociation = BinaryAssociation(
    name="foreignTable8",
    ends={
        Property(name="sql_Table10", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ForeignKey9", type=sql_Table, multiplicity=Multiplicity(0, 1))
    }
)
foreignColumns11: BinaryAssociation = BinaryAssociation(
    name="foreignColumns11",
    ends={
        Property(name="sql_Column13", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ForeignKey12", type=sql_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Model, sql_Database, sql_Table, sql_EObject, sql_Column, sql_PrimaryKey, sql_ForeignKey, DataType},
    associations={tables1, database0, facts3, localColumns6, col5, foreignTable8, foreignColumns11},
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