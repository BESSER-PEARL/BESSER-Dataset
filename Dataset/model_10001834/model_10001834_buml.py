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
ClassA = Class(name="ClassA")
T = Class(name="T")
ClassB = Class(name="ClassB")
T1 = Class(name="T1")
Actor_Actor = Class(name="Actor_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")

# ClassA class attributes and methods
ClassA_flag: Property = Property(name="flag", type=BooleanType)
ClassA.attributes={ClassA_flag}

# T class attributes and methods

# ClassB class attributes and methods

# T1 class attributes and methods

# Actor_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_Z0GkwETJEeeTJ_4Vl2J2rQ",
    types={ClassA, T, ClassB, T1, Actor_Actor, UseCase_UseCase, MyClass, MyClass2, MyClass3, MyClass4},
    associations={},
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