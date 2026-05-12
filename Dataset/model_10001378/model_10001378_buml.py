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
Actor_Actor = Class(name="Actor_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
Actor2_Actor = Class(name="Actor2_Actor")
Actor3_Actor = Class(name="Actor3_Actor")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
Class_ = Class(name="Class")
Class2 = Class(name="Class2")

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# Actor2_Actor class attributes and methods

# Actor3_Actor class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# Class class attributes and methods

# Class2 class attributes and methods

# Relationships
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase0", type=UseCase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase3",
    ends={
        Property(name="useCase32", type=UseCase3_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor3", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase24", type=UseCase2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor5", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3DvnUCH8EeqqcaoAsxFIeg",
    types={Actor_Actor, UseCase_UseCase, Actor2_Actor, Actor3_Actor, UseCase2_UseCase, UseCase3_UseCase, Class_, Class2},
    associations={Actor_UseCase, Actor_UseCase3, Actor_UseCase2},
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