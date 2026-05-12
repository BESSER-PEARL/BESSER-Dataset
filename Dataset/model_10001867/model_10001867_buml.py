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
Interface_Interface = Class(name="Interface_Interface")
Class_ = Class(name="Class")
Actor_Actor = Class(name="Actor_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
Actor2_Actor = Class(name="Actor2_Actor")
mahasiswa = Class(name="mahasiswa")

# Interface_Interface class attributes and methods

# Class class attributes and methods
Class__attribute: Property = Property(name="attribute", type=StringType)
Class_.attributes={Class__attribute}

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# Actor2_Actor class attributes and methods

# mahasiswa class attributes and methods
mahasiswa_nim: Property = Property(name="nim", type=StringType)
mahasiswa.attributes={mahasiswa_nim}

# Relationships
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase0", type=UseCase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
UseCase3_Actor: BinaryAssociation = BinaryAssociation(
    name="UseCase3_Actor",
    ends={
        Property(name="actor2", type=Actor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase33", type=UseCase3_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
UseCase2_Actor: BinaryAssociation = BinaryAssociation(
    name="UseCase2_Actor",
    ends={
        Property(name="actor4", type=Actor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase25", type=UseCase2_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_aO1YwN5zEeeAyLDAJ12_fg",
    types={Interface_Interface, Class_, Actor_Actor, UseCase_UseCase, UseCase2_UseCase, UseCase3_UseCase, Actor2_Actor, mahasiswa},
    associations={Actor_UseCase, UseCase3_Actor, UseCase2_Actor},
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