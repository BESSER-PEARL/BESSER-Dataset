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
Kasu11_ClassC = Class(name="Kasu11::ClassC")
Kasu11_ClassA = Class(name="Kasu11::ClassA")
Kasu11_ClassB = Class(name="Kasu11::ClassB")

# Kasu11_ClassC class attributes and methods
Kasu11_ClassC_Name: Property = Property(name="Name", type=StringType)
Kasu11_ClassC.attributes={Kasu11_ClassC_Name}

# Kasu11_ClassA class attributes and methods
Kasu11_ClassA_Name: Property = Property(name="Name", type=StringType)
Kasu11_ClassA.attributes={Kasu11_ClassA_Name}

# Kasu11_ClassB class attributes and methods
Kasu11_ClassB_Name: Property = Property(name="Name", type=StringType)
Kasu11_ClassB.attributes={Kasu11_ClassB_Name}

# Relationships
C_C1: BinaryAssociation = BinaryAssociation(
    name="C_C1",
    ends={
        Property(name="ClassC", type=Kasu11_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="C_A2", type=Kasu11_ClassC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_B0: BinaryAssociation = BinaryAssociation(
    name="C_B0",
    ends={
        Property(name="ClassB", type=Kasu11_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="C_A", type=Kasu11_ClassB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_A3: BinaryAssociation = BinaryAssociation(
    name="C_A3",
    ends={
        Property(name="ClassA", type=Kasu11_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="C_B", type=Kasu11_ClassA, multiplicity=Multiplicity(1, 1))
    }
)
C_C4: BinaryAssociation = BinaryAssociation(
    name="C_C4",
    ends={
        Property(name="ClassC6", type=Kasu11_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="C_B5", type=Kasu11_ClassC, multiplicity=Multiplicity(0, 9999))
    }
)
C_A7: BinaryAssociation = BinaryAssociation(
    name="C_A7",
    ends={
        Property(name="ClassA8", type=Kasu11_ClassC, multiplicity=Multiplicity(1, 1)),
        Property(name="C_C", type=Kasu11_ClassA, multiplicity=Multiplicity(1, 1))
    }
)
C_B9: BinaryAssociation = BinaryAssociation(
    name="C_B9",
    ends={
        Property(name="ClassB11", type=Kasu11_ClassC, multiplicity=Multiplicity(1, 1)),
        Property(name="C_C10", type=Kasu11_ClassB, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Kasu11",
    types={Kasu11_ClassC, Kasu11_ClassA, Kasu11_ClassB},
    associations={C_C1, C_B0, C_A3, C_C4, C_A7, C_B9},
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