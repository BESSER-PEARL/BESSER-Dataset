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
C1 = Class(name="C1")
C2 = Class(name="C2")

# C1 class attributes and methods
C1_vv1: Property = Property(name="vv1", type=IntegerType)
C1.attributes={C1_vv1}

# C2 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_31WIEK34EemHYc7DDM2g2A",
    types={C1, C2},
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