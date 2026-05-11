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
A = Class(name="A")
C = Class(name="C")
tests_A = Class(name="tests_A")
ObjectUnionOf_A_B = Class(name="ObjectUnionOf_A_B")
tests_B = Class(name="tests_B")
ObjectIntersectionOf_A_C = Class(name="ObjectIntersectionOf_A_C")
tests_C = Class(name="tests_C")
tests_ObjectUnionOf_A_B = Class(name="tests_ObjectUnionOf_A_B", is_abstract=True)
tests_ObjectIntersectionOf_A_C = Class(name="tests_ObjectIntersectionOf_A_C", is_abstract=True)

# A class attributes and methods

# C class attributes and methods

# tests_A class attributes and methods

# ObjectUnionOf_A_B class attributes and methods

# tests_B class attributes and methods

# ObjectIntersectionOf_A_C class attributes and methods

# tests_C class attributes and methods

# tests_ObjectUnionOf_A_B class attributes and methods

# tests_ObjectIntersectionOf_A_C class attributes and methods

# Relationships
foo0: BinaryAssociation = BinaryAssociation(
    name="foo0",
    ends={
        Property(name="tests_ObjectUnionOf_A_B", type=tests_A, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_A", type=tests_ObjectUnionOf_A_B, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tests_ObjectIntersectionOf_A_C_A = Generalization(general=A, specific=tests_ObjectIntersectionOf_A_C)
gen_tests_ObjectIntersectionOf_A_C_C = Generalization(general=C, specific=tests_ObjectIntersectionOf_A_C)
gen_tests_A_ObjectUnionOf_A_B = Generalization(general=ObjectUnionOf_A_B, specific=tests_A)
gen_tests_B_ObjectIntersectionOf_A_C = Generalization(general=ObjectIntersectionOf_A_C, specific=tests_B)
gen_tests_B_ObjectUnionOf_A_B = Generalization(general=ObjectUnionOf_A_B, specific=tests_B)

# Domain Model
domain_model = DomainModel(
    name="tests",
    types={A, C, tests_A, ObjectUnionOf_A_B, tests_B, ObjectIntersectionOf_A_C, tests_C, tests_ObjectUnionOf_A_B, tests_ObjectIntersectionOf_A_C},
    associations={foo0},
    generalizations={gen_tests_ObjectIntersectionOf_A_C_A, gen_tests_ObjectIntersectionOf_A_C_C, gen_tests_A_ObjectUnionOf_A_B, gen_tests_B_ObjectIntersectionOf_A_C, gen_tests_B_ObjectUnionOf_A_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)