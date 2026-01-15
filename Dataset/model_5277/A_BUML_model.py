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
a_A = Class(name="a::A")
a_EObject = Class(name="a::EObject")
a_B = Class(name="a::B")

# a_A class attributes and methods

# a_EObject class attributes and methods

# a_B class attributes and methods

# Relationships
eobject0: BinaryAssociation = BinaryAssociation(
    name="eobject0",
    ends={
        Property(name="a_EObject", type=a_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a_A", type=a_EObject, multiplicity=Multiplicity(0, 1))
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="a_B", type=a_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a_A2", type=a_B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_A, a_EObject, a_B},
    associations={eobject0, b1},
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