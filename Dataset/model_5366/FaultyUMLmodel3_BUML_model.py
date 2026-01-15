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
FaultyUMLmodel3_A = Class(name="FaultyUMLmodel3::A")

# FaultyUMLmodel3_A class attributes and methods
FaultyUMLmodel3_A_a: Property = Property(name="a", type=IntegerType)
FaultyUMLmodel3_A_b: Property = Property(name="b", type=IntegerType)
FaultyUMLmodel3_A_c: Property = Property(name="c", type=IntegerType)
FaultyUMLmodel3_A_d: Property = Property(name="d", type=IntegerType)
FaultyUMLmodel3_A.attributes={FaultyUMLmodel3_A_d, FaultyUMLmodel3_A_a, FaultyUMLmodel3_A_b, FaultyUMLmodel3_A_c}

# Domain Model
domain_model = DomainModel(
    name="FaultyUMLmodel3",
    types={FaultyUMLmodel3_A},
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