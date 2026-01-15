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
a_A1 = Class(name="a::A1")
B1 = Class(name="B1")
B2 = Class(name="B2")
a_A2 = Class(name="a::A2")

# a_A1 class attributes and methods

# B1 class attributes and methods

# B2 class attributes and methods

# a_A2 class attributes and methods

# Relationships
a10: BinaryAssociation = BinaryAssociation(
    name="a10",
    ends={
        Property(name="a_A1", type=a_A2, multiplicity=Multiplicity(1, 1)),
        Property(name="a_A2", type=a_A1, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_a_A1_B1 = Generalization(general=B1, specific=a_A1)
gen_a_A1_B2 = Generalization(general=B2, specific=a_A1)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_A1, B1, B2, a_A2},
    associations={a10},
    generalizations={gen_a_A1_B1, gen_a_A1_B2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)