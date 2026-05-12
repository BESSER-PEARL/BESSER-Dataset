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
Component_Component = Class(name="Component_Component")
Actor2_Actor = Class(name="Actor2_Actor")
Package_Class = Class(name="Package_Class")
Package_Class2 = Class(name="Package_Class2")
UseCase_external = Class(name="UseCase_external")

# Actor_Actor class attributes and methods

# Component_Component class attributes and methods

# Actor2_Actor class attributes and methods

# Package_Class class attributes and methods

# Package_Class2 class attributes and methods

# UseCase_external class attributes and methods

# Relationships
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase0", type=UseCase_external, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Class_Class2: BinaryAssociation = BinaryAssociation(
    name="Class_Class2",
    ends={
        Property(name="class22", type=Package_Class2, multiplicity=Multiplicity(0, 1)),
        Property(name="class3", type=Package_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_U_BUgOCuEee1VcqWCkiVQg",
    types={Actor_Actor, Component_Component, Actor2_Actor, Package_Class, Package_Class2, UseCase_external},
    associations={Actor_UseCase, Class_Class2},
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