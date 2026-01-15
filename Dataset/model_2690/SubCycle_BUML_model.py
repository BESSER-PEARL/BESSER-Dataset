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
cycle_A = Class(name="cycle::A")
cycle_B = Class(name="cycle::B")
cycle_C = Class(name="cycle::C")

# cycle_A class attributes and methods
cycle_A_i: Property = Property(name="i", type=IntegerType)
cycle_A_j: Property = Property(name="j", type=IntegerType)
cycle_A.attributes={cycle_A_i, cycle_A_j}

# cycle_B class attributes and methods
cycle_B_x: Property = Property(name="x", type=FloatType)
cycle_B_y: Property = Property(name="y", type=FloatType)
cycle_B.attributes={cycle_B_x, cycle_B_y}

# cycle_C class attributes and methods

# Relationships
myBs0: BinaryAssociation = BinaryAssociation(
    name="myBs0",
    ends={
        Property(name="cycle_B", type=cycle_A, multiplicity=Multiplicity(1, 1)),
        Property(name="cycle_A", type=cycle_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myA1: BinaryAssociation = BinaryAssociation(
    name="myA1",
    ends={
        Property(name="cycle_A3", type=cycle_B, multiplicity=Multiplicity(1, 1)),
        Property(name="cycle_B2", type=cycle_A, multiplicity=Multiplicity(0, 1))
    }
)
myC4: BinaryAssociation = BinaryAssociation(
    name="myC4",
    ends={
        Property(name="cycle_C", type=cycle_B, multiplicity=Multiplicity(1, 1)),
        Property(name="cycle_B5", type=cycle_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myA6: BinaryAssociation = BinaryAssociation(
    name="myA6",
    ends={
        Property(name="cycle_A8", type=cycle_C, multiplicity=Multiplicity(1, 1)),
        Property(name="cycle_C7", type=cycle_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="cycle",
    types={cycle_A, cycle_B, cycle_C},
    associations={myBs0, myA1, myC4, myA6},
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