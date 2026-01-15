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
mytest_A = Class(name="mytest::A")
mytest_B = Class(name="mytest::B")
mytest_MyRoot = Class(name="mytest::MyRoot")

# mytest_A class attributes and methods

# mytest_B class attributes and methods

# mytest_MyRoot class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="mytest",
    types={mytest_A, mytest_B, mytest_MyRoot},
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