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
Deck = Class(name="Deck")
Card = Class(name="Card")
Hand = Class(name="Hand")
EndCardPile = Class(name="EndCardPile")
CardCollection = Class(name="CardCollection")

# Deck class attributes and methods

# Card class attributes and methods
Card_Number: Property = Property(name="Number", type=IntegerType)
Card_Suit: Property = Property(name="Suit", type=StringType)
Card.attributes={Card_Suit, Card_Number}

# Hand class attributes and methods

# EndCardPile class attributes and methods

# CardCollection class attributes and methods
CardCollection_collection: Property = Property(name="collection", type=StringType)
CardCollection.attributes={CardCollection_collection}

# Relationships
CardCollection_Card: BinaryAssociation = BinaryAssociation(
    name="CardCollection_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(0, 1)),
        Property(name="cardCollection1", type=CardCollection, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c2080af3_baaf_4bb6_9ea6_a7eb16f1fd97",
    types={Deck, Card, Hand, EndCardPile, CardCollection},
    associations={CardCollection_Card},
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