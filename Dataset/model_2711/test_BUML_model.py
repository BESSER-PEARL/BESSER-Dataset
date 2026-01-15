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
A = Class(name="A")
test_C = Class(name="test::C")
test_Program = Class(name="test::Program")

# test_A class attributes and methods

# test_B class attributes and methods

# A class attributes and methods

# test_C class attributes and methods

# test_Program class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="test_B", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C", type=test_B, multiplicity=Multiplicity(0, 1))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="test_A", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C2", type=test_A, multiplicity=Multiplicity(0, 1))
    }
)
as3: BinaryAssociation = BinaryAssociation(
    name="as3",
    ends={
        Property(name="test_A4", type=test_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Program", type=test_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs5: BinaryAssociation = BinaryAssociation(
    name="cs5",
    ends={
        Property(name="test_C7", type=test_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Program6", type=test_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_B_A = Generalization(general=A, specific=test_B)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, test_B, A, test_C, test_Program},
    associations={b0, a1, as3, cs5},
    generalizations={gen_test_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)