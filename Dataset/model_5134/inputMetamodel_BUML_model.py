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
test_A = Class(name="test::A")
test_B = Class(name="test::B")
test_C = Class(name="test::C")

# test_A class attributes and methods
test_A_a: Property = Property(name="a", type=StringType)
test_A.attributes={test_A_a}

# test_B class attributes and methods
test_B_b: Property = Property(name="b", type=StringType)
test_B.attributes={test_B_b}

# test_C class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="test_B", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A", type=test_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, test_B, test_C},
    associations={b0},
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