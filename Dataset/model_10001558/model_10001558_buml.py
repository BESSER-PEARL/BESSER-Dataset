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
I_Interface = Class(name="I_Interface")
S = Class(name="S", is_abstract=True)
C1 = Class(name="C1", is_abstract=True)
C2 = Class(name="C2", is_abstract=True)
C3 = Class(name="C3")

# I_Interface class attributes and methods

# S class attributes and methods
S_v1: Property = Property(name="v1", type=StringType)
S.attributes={S_v1}

# C1 class attributes and methods
C1_b: Property = Property(name="b", type=StringType)
C1.attributes={C1_b}

# C2 class attributes and methods

# C3 class attributes and methods
C3_K: Property = Property(name="K", type=IntegerType)
C3.attributes={C3_K}

# Domain Model
domain_model = DomainModel(
    name="_F_QPwNwIEeiJYbNjsZ3wUw",
    types={I_Interface, S, C1, C2, C3},
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