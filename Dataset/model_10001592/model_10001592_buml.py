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
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
UseCase4_UseCase = Class(name="UseCase4_UseCase")
UseCase5_UseCase = Class(name="UseCase5_UseCase")
Class_ = Class(name="Class")
UseCase6_UseCase = Class(name="UseCase6_UseCase")
UseCase7_UseCase = Class(name="UseCase7_UseCase")

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# UseCase4_UseCase class attributes and methods

# UseCase5_UseCase class attributes and methods

# Class class attributes and methods

# UseCase6_UseCase class attributes and methods

# UseCase7_UseCase class attributes and methods

# Relationships
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase0", type=UseCase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase22", type=UseCase2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor3", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase6: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase6",
    ends={
        Property(name="useCase64", type=UseCase6_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor5", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase7: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase7",
    ends={
        Property(name="useCase76", type=UseCase7_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor7", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_HxQqQOUCEeekKLRLyKXO4Q",
    types={Actor_Actor, UseCase_UseCase, UseCase2_UseCase, UseCase3_UseCase, UseCase4_UseCase, UseCase5_UseCase, Class_, UseCase6_UseCase, UseCase7_UseCase},
    associations={Actor_UseCase, Actor_UseCase2, Actor_UseCase6, Actor_UseCase7},
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