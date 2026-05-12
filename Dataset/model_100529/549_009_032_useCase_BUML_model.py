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
UseCase_Extend = Class(name="UseCase_Extend")
UseCase = Class(name="UseCase")
UseCase_Actor = Class(name="UseCase_Actor")
NamedElement = Class(name="NamedElement")
UseCase_UseCase = Class(name="UseCase_UseCase")
Include = Class(name="Include")
Extend = Class(name="Extend")
UseCase_Include = Class(name="UseCase_Include")
UseCase_UseCaseContainer = Class(name="UseCase_UseCaseContainer")
UseCase_BehavioredClassifier = Class(name="UseCase_BehavioredClassifier")
UseCase_NamedElement = Class(name="UseCase_NamedElement", is_abstract=True)
UseCase_Association = Class(name="UseCase_Association")
Actor = Class(name="Actor")

# UseCase_Extend class attributes and methods

# UseCase class attributes and methods

# UseCase_Actor class attributes and methods

# NamedElement class attributes and methods

# UseCase_UseCase class attributes and methods

# Include class attributes and methods

# Extend class attributes and methods

# UseCase_Include class attributes and methods

# UseCase_UseCaseContainer class attributes and methods

# UseCase_BehavioredClassifier class attributes and methods

# UseCase_NamedElement class attributes and methods
UseCase_NamedElement_name: Property = Property(name="name", type=StringType)
UseCase_NamedElement.attributes={UseCase_NamedElement_name}

# UseCase_Association class attributes and methods

# Actor class attributes and methods

# Relationships
include0: BinaryAssociation = BinaryAssociation(
    name="include0",
    ends={
        Property(name="Include", type=UseCase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_UseCase", type=Include, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
extend1: BinaryAssociation = BinaryAssociation(
    name="extend1",
    ends={
        Property(name="Extend", type=UseCase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_UseCase2", type=Extend, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
extension3: BinaryAssociation = BinaryAssociation(
    name="extension3",
    ends={
        Property(name="UseCase", type=UseCase_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_Extend", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
includingCase4: BinaryAssociation = BinaryAssociation(
    name="includingCase4",
    ends={
        Property(name="UseCase5", type=UseCase_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_Include", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
ownedElement6: BinaryAssociation = BinaryAssociation(
    name="ownedElement6",
    ends={
        Property(name="NamedElement", type=UseCase_UseCaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_UseCaseContainer", type=NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor7: BinaryAssociation = BinaryAssociation(
    name="actor7",
    ends={
        Property(name="Actor", type=UseCase_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_Association", type=Actor, multiplicity=Multiplicity(0, 1))
    }
)
useCase8: BinaryAssociation = BinaryAssociation(
    name="useCase8",
    ends={
        Property(name="UseCase10", type=UseCase_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCase_Association9", type=UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UseCase_Actor_NamedElement = Generalization(general=NamedElement, specific=UseCase_Actor)
gen_UseCase_UseCase_NamedElement = Generalization(general=NamedElement, specific=UseCase_UseCase)
gen_UseCase_Association_NamedElement = Generalization(general=NamedElement, specific=UseCase_Association)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={UseCase_Extend, UseCase, UseCase_Actor, NamedElement, UseCase_UseCase, Include, Extend, UseCase_Include, UseCase_UseCaseContainer, UseCase_BehavioredClassifier, UseCase_NamedElement, UseCase_Association, Actor},
    associations={include0, extend1, extension3, includingCase4, ownedElement6, actor7, useCase8},
    generalizations={gen_UseCase_Actor_NamedElement, gen_UseCase_UseCase_NamedElement, gen_UseCase_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)