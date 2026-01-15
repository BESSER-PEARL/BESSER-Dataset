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
Kasu2_ClassA = Class(name="Kasu2::ClassA")
Kasu2_ClassB = Class(name="Kasu2::ClassB")
Kasu2_Root = Class(name="Kasu2::Root")

# Kasu2_ClassA class attributes and methods
Kasu2_ClassA_Name: Property = Property(name="Name", type=StringType)
Kasu2_ClassA.attributes={Kasu2_ClassA_Name}

# Kasu2_ClassB class attributes and methods
Kasu2_ClassB_Name: Property = Property(name="Name", type=StringType)
Kasu2_ClassB.attributes={Kasu2_ClassB_Name}

# Kasu2_Root class attributes and methods

# Relationships
C_B0: BinaryAssociation = BinaryAssociation(
    name="C_B0",
    ends={
        Property(name="ClassB", type=Kasu2_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="C_A", type=Kasu2_ClassB, multiplicity=Multiplicity(0, 9999))
    }
)
C_R1: BinaryAssociation = BinaryAssociation(
    name="C_R1",
    ends={
        Property(name="Root", type=Kasu2_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="C_A2", type=Kasu2_Root, multiplicity=Multiplicity(1, 1))
    }
)
C_A3: BinaryAssociation = BinaryAssociation(
    name="C_A3",
    ends={
        Property(name="ClassA", type=Kasu2_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="C_B", type=Kasu2_ClassA, multiplicity=Multiplicity(1, 1))
    }
)
C_A4: BinaryAssociation = BinaryAssociation(
    name="C_A4",
    ends={
        Property(name="ClassA5", type=Kasu2_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="C_R", type=Kasu2_ClassA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Kasu2",
    types={Kasu2_ClassA, Kasu2_ClassB, Kasu2_Root},
    associations={C_B0, C_R1, C_A3, C_A4},
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