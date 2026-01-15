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
hExample_1_LHS_A = Class(name="hExample::1::LHS::A")
hExample_1_LHS_B = Class(name="hExample::1::LHS::B")

# hExample_1_LHS_A class attributes and methods

# hExample_1_LHS_B class attributes and methods
hExample_1_LHS_B_name: Property = Property(name="name", type=StringType)
hExample_1_LHS_B.attributes={hExample_1_LHS_B_name}

# Relationships
ref0: BinaryAssociation = BinaryAssociation(
    name="ref0",
    ends={
        Property(name="hExample_1_LHS_B", type=hExample_1_LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_1_LHS_A", type=hExample_1_LHS_B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="hExample_1_LHS",
    types={hExample_1_LHS_A, hExample_1_LHS_B},
    associations={ref0},
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