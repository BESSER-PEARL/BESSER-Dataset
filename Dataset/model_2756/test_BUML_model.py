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
test_Compo = Class(name="test::Compo")
test_B = Class(name="test::B")
test_A = Class(name="test::A")

# test_Compo class attributes and methods

# test_B class attributes and methods
test_B_name: Property = Property(name="name", type=StringType)
test_B.attributes={test_B_name}

# test_A class attributes and methods
test_A_listen: Property = Property(name="listen", type=IntegerType)
test_A.attributes={test_A_listen}

# Relationships
Ab3: BinaryAssociation = BinaryAssociation(
    name="Ab3",
    ends={
        Property(name="test_B5", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A4", type=test_B, multiplicity=Multiplicity(0, 9999))
    }
)
Bs0: BinaryAssociation = BinaryAssociation(
    name="Bs0",
    ends={
        Property(name="test_B", type=test_Compo, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Compo", type=test_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
As1: BinaryAssociation = BinaryAssociation(
    name="As1",
    ends={
        Property(name="test_A", type=test_Compo, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Compo2", type=test_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Compo, test_B, test_A},
    associations={Ab3, Bs0, As1},
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