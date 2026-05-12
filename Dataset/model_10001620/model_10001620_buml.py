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
MyClass = Class(name="MyClass")
MyInterface_Interface = Class(name="MyInterface_Interface")
UseCase_UseCase = Class(name="UseCase_UseCase")
Actor_Actor = Class(name="Actor_Actor")
UseCase2_UseCase = Class(name="UseCase2_UseCase")

# MyClass class attributes and methods
MyClass_Abb: Property = Property(name="Abb", type=BooleanType)
MyClass_ABC: Property = Property(name="ABC", type=MyClass)
MyClass.attributes={MyClass_Abb, MyClass_ABC}

# MyInterface_Interface class attributes and methods

# UseCase_UseCase class attributes and methods

# Actor_Actor class attributes and methods

# UseCase2_UseCase class attributes and methods

# Relationships
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase0", type=UseCase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor1", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyInterface: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyInterface",
    ends={
        Property(name="myInterface2", type=MyInterface_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass3", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JfMJAHEBEee5HMQDnOR_kg",
    types={MyClass, MyInterface_Interface, UseCase_UseCase, Actor_Actor, UseCase2_UseCase},
    associations={Actor_UseCase, MyClass_MyInterface},
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