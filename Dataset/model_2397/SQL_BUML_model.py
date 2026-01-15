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
sQL_Database = Class(name="sQL::Database")
sQL_Table = Class(name="sQL::Table")
sQL_Column = Class(name="sQL::Column")
sQL_PrimaryKey = Class(name="sQL::PrimaryKey")
sQL_ForeignKey = Class(name="sQL::ForeignKey")

# sQL_Database class attributes and methods

# sQL_Table class attributes and methods
sQL_Table_name: Property = Property(name="name", type=StringType)
sQL_Table.attributes={sQL_Table_name}

# sQL_Column class attributes and methods
sQL_Column_name: Property = Property(name="name", type=StringType)
sQL_Column_dataType: Property = Property(name="dataType", type=StringType)
sQL_Column_notNull: Property = Property(name="notNull", type=StringType)
sQL_Column.attributes={sQL_Column_dataType, sQL_Column_name, sQL_Column_notNull}

# sQL_PrimaryKey class attributes and methods

# sQL_ForeignKey class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="sQL_Table", type=sQL_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Database", type=sQL_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="sQL_Column", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table2", type=sQL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="sQL_Column9", type=sQL_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_PrimaryKey8", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)
columns10: BinaryAssociation = BinaryAssociation(
    name="columns10",
    ends={
        Property(name="sQL_Column12", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey11", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)
refTable13: BinaryAssociation = BinaryAssociation(
    name="refTable13",
    ends={
        Property(name="sQL_Table15", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey14", type=sQL_Table, multiplicity=Multiplicity(0, 1))
    }
)
refColumns16: BinaryAssociation = BinaryAssociation(
    name="refColumns16",
    ends={
        Property(name="sQL_Column18", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey17", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)
primaryKey3: BinaryAssociation = BinaryAssociation(
    name="primaryKey3",
    ends={
        Property(name="sQL_PrimaryKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table4", type=sQL_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreignKeys5: BinaryAssociation = BinaryAssociation(
    name="foreignKeys5",
    ends={
        Property(name="sQL_ForeignKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table6", type=sQL_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sQL",
    types={sQL_Database, sQL_Table, sQL_Column, sQL_PrimaryKey, sQL_ForeignKey},
    associations={tables0, columns1, columns7, columns10, refTable13, refColumns16, primaryKey3, foreignKeys5},
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