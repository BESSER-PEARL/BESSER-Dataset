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
rdbms_Column = Class(name="rdbms::Column")
rdbms_RDBMSModel = Class(name="rdbms::RDBMSModel")
rdbms_Table = Class(name="rdbms::Table")
rdbms_ForeignKey = Class(name="rdbms::ForeignKey")

# rdbms_Column class attributes and methods
rdbms_Column_name: Property = Property(name="name", type=StringType)
rdbms_Column_type: Property = Property(name="type", type=StringType)
rdbms_Column.attributes={rdbms_Column_name, rdbms_Column_type}

# rdbms_RDBMSModel class attributes and methods

# rdbms_Table class attributes and methods
rdbms_Table_name: Property = Property(name="name", type=StringType)
rdbms_Table.attributes={rdbms_Table_name}

# rdbms_ForeignKey class attributes and methods

# Relationships
containsColumns1: BinaryAssociation = BinaryAssociation(
    name="containsColumns1",
    ends={
        Property(name="rdbms_Column", type=rdbms_RDBMSModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RDBMSModel2", type=rdbms_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
containsTables0: BinaryAssociation = BinaryAssociation(
    name="containsTables0",
    ends={
        Property(name="rdbms_Table", type=rdbms_RDBMSModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RDBMSModel", type=rdbms_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
containsForeignKeys3: BinaryAssociation = BinaryAssociation(
    name="containsForeignKeys3",
    ends={
        Property(name="rdbms_ForeignKey", type=rdbms_RDBMSModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RDBMSModel4", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
foreignKeys5: BinaryAssociation = BinaryAssociation(
    name="foreignKeys5",
    ends={
        Property(name="rdbms_ForeignKey7", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table6", type=rdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns8: BinaryAssociation = BinaryAssociation(
    name="columns8",
    ends={
        Property(name="rdbms_Column10", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table9", type=rdbms_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKey11: BinaryAssociation = BinaryAssociation(
    name="primaryKey11",
    ends={
        Property(name="rdbms_Column13", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table12", type=rdbms_Column, multiplicity=Multiplicity(1, 9999))
    }
)
references14: BinaryAssociation = BinaryAssociation(
    name="references14",
    ends={
        Property(name="rdbms_Table16", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey15", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns17: BinaryAssociation = BinaryAssociation(
    name="columns17",
    ends={
        Property(name="rdbms_Column19", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey18", type=rdbms_Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rdbms",
    types={rdbms_Column, rdbms_RDBMSModel, rdbms_Table, rdbms_ForeignKey},
    associations={containsColumns1, containsTables0, containsForeignKeys3, foreignKeys5, columns8, primaryKey11, references14, columns17},
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