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

# Enumerations
CardValue: Enumeration = Enumeration(
    name="CardValue",
    literals={
            
    }
)

# Classes
Card = Class(name="Card")

# Card class attributes and methods
Card_name: Property = Property(name="name", type=StringType)
Card_value: Property = Property(name="value", type=IntegerType)
Card.attributes={Card_name, Card_value}

# Domain Model
domain_model = DomainModel(
    name="_t3p0wNWnEeehRMl7r1_c5g",
    types={Card, CardValue},
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