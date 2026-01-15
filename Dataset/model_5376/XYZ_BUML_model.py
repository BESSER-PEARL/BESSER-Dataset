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
xyz_X = Class(name="xyz::X")
xyz_Y = Class(name="xyz::Y")
xyz_Z = Class(name="xyz::Z")

# xyz_X class attributes and methods

# xyz_Y class attributes and methods

# xyz_Z class attributes and methods

# Relationships
yes0: BinaryAssociation = BinaryAssociation(
    name="yes0",
    ends={
        Property(name="xyz_Y", type=xyz_X, multiplicity=Multiplicity(1, 1)),
        Property(name="xyz_X", type=xyz_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zes1: BinaryAssociation = BinaryAssociation(
    name="zes1",
    ends={
        Property(name="xyz_Z", type=xyz_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="xyz_Y2", type=xyz_Z, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xyz",
    types={xyz_X, xyz_Y, xyz_Z},
    associations={yes0, zes1},
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