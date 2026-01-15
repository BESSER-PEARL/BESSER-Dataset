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
ic_TopLevelClass = Class(name="ic::TopLevelClass")
ic_sub1_A1 = Class(name="ic::sub1::A1")
ic_sub1_A2 = Class(name="ic::sub1::A2")
ic_sub1_A3 = Class(name="ic::sub1::A3")
ic_sub2_B1 = Class(name="ic::sub2::B1")
ic_sub2_B2 = Class(name="ic::sub2::B2")
ic_sub2_B3 = Class(name="ic::sub2::B3")

# ic_TopLevelClass class attributes and methods

# ic_sub1_A1 class attributes and methods

# ic_sub1_A2 class attributes and methods

# ic_sub1_A3 class attributes and methods

# ic_sub2_B1 class attributes and methods

# ic_sub2_B2 class attributes and methods

# ic_sub2_B3 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="ic",
    types={ic_TopLevelClass, ic_sub1_A1, ic_sub1_A2, ic_sub1_A3, ic_sub2_B1, ic_sub2_B2, ic_sub2_B3},
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