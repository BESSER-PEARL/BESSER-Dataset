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
Kasu3_ClassC = Class(name="Kasu3::ClassC")
Kasu3_ClassA = Class(name="Kasu3::ClassA")
Kasu3_ClassB = Class(name="Kasu3::ClassB")

# Kasu3_ClassC class attributes and methods
Kasu3_ClassC_Name: Property = Property(name="Name", type=StringType)
Kasu3_ClassC.attributes={Kasu3_ClassC_Name}

# Kasu3_ClassA class attributes and methods
Kasu3_ClassA_Name: Property = Property(name="Name", type=StringType)
Kasu3_ClassA.attributes={Kasu3_ClassA_Name}

# Kasu3_ClassB class attributes and methods
Kasu3_ClassB_Name: Property = Property(name="Name", type=StringType)
Kasu3_ClassB.attributes={Kasu3_ClassB_Name}

# Relationships
C_A1: BinaryAssociation = BinaryAssociation(
    name="C_A1",
    ends={
        Property(name="Kasu3_ClassA3", type=Kasu3_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu3_ClassB2", type=Kasu3_ClassA, multiplicity=Multiplicity(1, 1))
    }
)
C_B0: BinaryAssociation = BinaryAssociation(
    name="C_B0",
    ends={
        Property(name="Kasu3_ClassB", type=Kasu3_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="Kasu3_ClassA", type=Kasu3_ClassB, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Kasu3",
    types={Kasu3_ClassC, Kasu3_ClassA, Kasu3_ClassB},
    associations={C_A1, C_B0},
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