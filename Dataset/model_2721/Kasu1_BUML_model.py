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
Kasu1_ClassA = Class(name="Kasu1::ClassA")
Kasu1_ClassB = Class(name="Kasu1::ClassB")

# Kasu1_ClassA class attributes and methods
Kasu1_ClassA_Name: Property = Property(name="Name", type=StringType)
Kasu1_ClassA.attributes={Kasu1_ClassA_Name}

# Kasu1_ClassB class attributes and methods
Kasu1_ClassB_Name: Property = Property(name="Name", type=StringType)
Kasu1_ClassB.attributes={Kasu1_ClassB_Name}

# Relationships
C_B0: BinaryAssociation = BinaryAssociation(
    name="C_B0",
    ends={
        Property(name="Kasu1_ClassB", type=Kasu1_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu1_ClassA", type=Kasu1_ClassB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_A1: BinaryAssociation = BinaryAssociation(
    name="C_A1",
    ends={
        Property(name="Kasu1_ClassA3", type=Kasu1_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu1_ClassB2", type=Kasu1_ClassA, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Kasu1",
    types={Kasu1_ClassA, Kasu1_ClassB},
    associations={C_B0, C_A1},
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