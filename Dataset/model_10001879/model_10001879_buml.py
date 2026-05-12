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
S1 = Class(name="S1")
C1 = Class(name="C1")
C2 = Class(name="C2")
C3 = Class(name="C3")

# S1 class attributes and methods
S1_static_int_v1: Property = Property(name="static_int_v1", type=StringType)
S1_double_v2: Property = Property(name="double_v2", type=StringType)
S1.attributes={S1_double_v2, S1_static_int_v1}

# C1 class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods
C3_Integer_k: Property = Property(name="Integer_k", type=IntegerType)
C3_long_m: Property = Property(name="long_m", type=StringType)
C3.attributes={C3_long_m, C3_Integer_k}

# Domain Model
domain_model = DomainModel(
    name="_b66ygMUiEeidHYrYeMfZow",
    types={S1, C1, C2, C3},
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