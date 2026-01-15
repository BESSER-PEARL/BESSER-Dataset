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
modelA_A = Class(name="modelA::A")
modelA_B = Class(name="modelA::B")

# modelA_A class attributes and methods
modelA_A_a: Property = Property(name="a", type=IntegerType)
modelA_A.attributes={modelA_A_a}

# modelA_B class attributes and methods
modelA_B_b: Property = Property(name="b", type=BooleanType)
modelA_B.attributes={modelA_B_b}

# Domain Model
domain_model = DomainModel(
    name="modelA",
    types={modelA_A, modelA_B},
    associations={},
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