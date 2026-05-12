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
Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
Card = Class(name="Card")
CardTester = Class(name="CardTester")
Deck = Class(name="Deck")

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=StringType)
Card_pointValue: Property = Property(name="pointValue", type=IntegerType)
Card_rank: Property = Property(name="rank", type=StringType)
Card.attributes={Card_suit, Card_pointValue, Card_rank}

# CardTester class attributes and methods

# Deck class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_ehtUsEmfEemcCbHu8oEdZw",
    types={Card, CardTester, Deck, Suit},
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