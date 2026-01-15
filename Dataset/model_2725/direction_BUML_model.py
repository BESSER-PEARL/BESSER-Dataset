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
direction_A = Class(name="direction::A")
direction_B = Class(name="direction::B")
A = Class(name="A")
direction_C = Class(name="direction::C")

# direction_A class attributes and methods
direction_A_name: Property = Property(name="name", type=StringType)
direction_A.attributes={direction_A_name}

# direction_B class attributes and methods

# A class attributes and methods

# direction_C class attributes and methods

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="direction_A", type=direction_C, multiplicity=Multiplicity(1, 1)),
        Property(name="direction_C", type=direction_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="direction_B", type=direction_C, multiplicity=Multiplicity(1, 1)),
        Property(name="direction_C2", type=direction_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_direction_B_A = Generalization(general=A, specific=direction_B)

# Domain Model
domain_model = DomainModel(
    name="direction",
    types={direction_A, direction_B, A, direction_C},
    associations={as0, bs1},
    generalizations={gen_direction_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)