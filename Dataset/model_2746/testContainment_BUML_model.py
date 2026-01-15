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
testcontainment_A = Class(name="testcontainment::A")
testcontainment_B = Class(name="testcontainment::B")

# testcontainment_A class attributes and methods

# testcontainment_B class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="B", type=testcontainment_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=testcontainment_B, multiplicity=Multiplicity(0, 9999))
    }
)
containedBs1: BinaryAssociation = BinaryAssociation(
    name="containedBs1",
    ends={
        Property(name="testcontainment_B", type=testcontainment_A, multiplicity=Multiplicity(1, 1)),
        Property(name="testcontainment_A", type=testcontainment_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="A", type=testcontainment_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=testcontainment_A, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testcontainment",
    types={testcontainment_A, testcontainment_B},
    associations={bs0, containedBs1, a2},
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