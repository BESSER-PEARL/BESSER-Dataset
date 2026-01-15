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
TestMerge_A = Class(name="TestMerge::A")
TestMerge_C = Class(name="TestMerge::C")
A = Class(name="A")

# TestMerge_A class attributes and methods
TestMerge_A_someNewAttribute: Property = Property(name="someNewAttribute", type=StringType)
TestMerge_A.attributes={TestMerge_A_someNewAttribute}

# TestMerge_C class attributes and methods

# A class attributes and methods

# Generalizations
gen_TestMerge_C_A = Generalization(general=A, specific=TestMerge_C)

# Domain Model
domain_model = DomainModel(
    name="TestMerge",
    types={TestMerge_A, TestMerge_C, A},
    associations={},
    generalizations={gen_TestMerge_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)