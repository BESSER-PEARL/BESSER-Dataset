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
genericTest_A = Class(name="genericTest::A")
genericTest_SomeType = Class(name="genericTest::SomeType")
genericTest_B = Class(name="genericTest::B")
genericTest_C = Class(name="genericTest::C")
genericTest_D = Class(name="genericTest::D")
genericTest_OtherType = Class(name="genericTest::OtherType")

# genericTest_A class attributes and methods

# genericTest_SomeType class attributes and methods

# genericTest_B class attributes and methods

# genericTest_C class attributes and methods

# genericTest_D class attributes and methods

# genericTest_OtherType class attributes and methods

# Relationships
someReference10: BinaryAssociation = BinaryAssociation(
    name="someReference10",
    ends={
        Property(name="genericTest_SomeType", type=genericTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="genericTest_A", type=genericTest_SomeType, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="genericTest",
    types={genericTest_A, genericTest_SomeType, genericTest_B, genericTest_C, genericTest_D, genericTest_OtherType},
    associations={someReference10},
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