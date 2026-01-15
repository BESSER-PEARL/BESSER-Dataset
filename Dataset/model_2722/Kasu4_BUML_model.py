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
Kasu4_ClassB = Class(name="Kasu4::ClassB")
Kasu4_ClassA = Class(name="Kasu4::ClassA")

# Kasu4_ClassB class attributes and methods
Kasu4_ClassB_Name: Property = Property(name="Name", type=StringType)
Kasu4_ClassB.attributes={Kasu4_ClassB_Name}

# Kasu4_ClassA class attributes and methods
Kasu4_ClassA_Name: Property = Property(name="Name", type=StringType)
Kasu4_ClassA.attributes={Kasu4_ClassA_Name}

# Relationships
C_B0: BinaryAssociation = BinaryAssociation(
    name="C_B0",
    ends={
        Property(name="Kasu4_ClassB", type=Kasu4_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu4_ClassA", type=Kasu4_ClassB, multiplicity=Multiplicity(0, 9999))
    }
)
C_A1: BinaryAssociation = BinaryAssociation(
    name="C_A1",
    ends={
        Property(name="Kasu4_ClassA3", type=Kasu4_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu4_ClassB2", type=Kasu4_ClassA, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Kasu4",
    types={Kasu4_ClassB, Kasu4_ClassA},
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