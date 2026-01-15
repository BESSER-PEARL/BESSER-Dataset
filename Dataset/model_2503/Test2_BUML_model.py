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
test2_A = Class(name="test2::A")
test2_B = Class(name="test2::B")
test2_test2sub1_D = Class(name="test2::test2sub1::D")
test2_test2sub1_D2 = Class(name="test2::test2sub1::D2")
D = Class(name="D")
test2_test2sub2_E = Class(name="test2::test2sub2::E")
test2_C = Class(name="test2::C")
B = Class(name="B")

# test2_A class attributes and methods

# test2_B class attributes and methods

# test2_test2sub1_D class attributes and methods

# test2_test2sub1_D2 class attributes and methods

# D class attributes and methods

# test2_test2sub2_E class attributes and methods

# test2_C class attributes and methods

# B class attributes and methods

# Relationships
refToB0: BinaryAssociation = BinaryAssociation(
    name="refToB0",
    ends={
        Property(name="test2_B", type=test2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test2_A", type=test2_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test2_test2sub1_D2_D = Generalization(general=D, specific=test2_test2sub1_D2)
gen_test2_C_B = Generalization(general=B, specific=test2_C)

# Domain Model
domain_model = DomainModel(
    name="test2",
    types={test2_A, test2_B, test2_test2sub1_D, test2_test2sub1_D2, D, test2_test2sub2_E, test2_C, B},
    associations={refToB0},
    generalizations={gen_test2_test2sub1_D2_D, gen_test2_C_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)