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
AbcToNothing_C = Class(name="AbcToNothing::C")
AbcToNothing_A = Class(name="AbcToNothing::A")
AbcToNothing_classB = Class(name="AbcToNothing::classB")

# AbcToNothing_C class attributes and methods

# AbcToNothing_A class attributes and methods

# AbcToNothing_classB class attributes and methods

# Relationships
AtoC1: BinaryAssociation = BinaryAssociation(
    name="AtoC1",
    ends={
        Property(name="AbcToNothing_C", type=AbcToNothing_A, multiplicity=Multiplicity(1, 1)),
        Property(name="AbcToNothing_A2", type=AbcToNothing_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AtoB0: BinaryAssociation = BinaryAssociation(
    name="AtoB0",
    ends={
        Property(name="AbcToNothing_classB", type=AbcToNothing_A, multiplicity=Multiplicity(1, 1)),
        Property(name="AbcToNothing_A", type=AbcToNothing_classB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CtoB3: BinaryAssociation = BinaryAssociation(
    name="CtoB3",
    ends={
        Property(name="AbcToNothing_classB5", type=AbcToNothing_C, multiplicity=Multiplicity(1, 1)),
        Property(name="AbcToNothing_C4", type=AbcToNothing_classB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="AbcToNothing",
    types={AbcToNothing_C, AbcToNothing_A, AbcToNothing_classB},
    associations={AtoC1, AtoB0, CtoB3},
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